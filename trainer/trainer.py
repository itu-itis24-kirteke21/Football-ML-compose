from __future__ import annotations
import os, json
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib

from features import build_features, BASIC_FEATURES

MODEL_DIR = Path(os.getenv("MODEL_DIR", "/shared/model"))
DATA_PATH = os.getenv("DATA_PATH", "/app/data/matches.csv")
RANDOM_STATE = int(os.getenv("RANDOM_STATE", "42"))
TARGET = os.getenv("TARGET", "outcome")

MODEL_DIR.mkdir(parents=True, exist_ok=True)
MODEL_PATH = MODEL_DIR / "model.pkl"
META_PATH = MODEL_DIR / "metadata.json"


def _synthetic_dataset(n: int = 2000, seed: int = 42)-> pd.DataFrame:
    rng = np.random.default_rng(seed)
    # Generate ELOs and squad values (millions €)
    home_elo = rng.normal(1600, 100, n)
    away_elo = rng.normal(1600, 100, n)
    home_squad_value = rng.normal(250, 80, n).clip(20, None)
    away_squad_value = rng.normal(250, 80, n).clip(20, None)

    # Recent form: 0..1 scaled points-per-game last 5
    home_form = rng.uniform(0, 1, n)
    away_form = rng.uniform(0, 1, n)

    # Goals last 5
    home_goals_last5 = rng.poisson(1.6, n)
    away_goals_last5 = rng.poisson(1.4, n)

    # True logit using differences
    z = (
        0.008 * (home_elo-away_elo)
        + 0.006 * (home_squad_value-away_squad_value)
        + 1.2 * (home_form-away_form)
        + 0.15 * (home_goals_last5-away_goals_last5)
        + 0.35 # home advantage
    )

    p_home = 1 / (1 + np.exp(-z))
    # Three-way: derive draw/away heuristically
    p_draw = 0.22 + rng.normal(0, 0.03, n)
    p_draw = np.clip(p_draw, 0.05, 0.5)
    p_away = 1-p_home-p_draw
    # Fix negatives
    p_away = np.maximum(p_away, 0.01)
    # Normalize
    s = p_home + p_draw + p_away
    p_home, p_draw, p_away = p_home / s, p_draw / s, p_away / s

    picks = []
    for ph, pdw, pa in zip(p_home, p_draw, p_away):
        r = rng.uniform()
        if r < ph:
            picks.append("H")
        elif r < ph + pdw:
            picks.append("D")
        else:
            picks.append("A")

    return pd.DataFrame({
    "home_elo": home_elo.round(0),
    "away_elo": away_elo.round(0),
    "home_squad_value": home_squad_value.round(1),
    "away_squad_value": away_squad_value.round(1),
    "home_form": home_form.round(3),
    "away_form": away_form.round(3),
    "home_goals_last5": home_goals_last5,
    "away_goals_last5": away_goals_last5,
    "outcome": picks,
    })

def load_or_generate(path: str)-> pd.DataFrame:
    p = Path(path)
    if p.exists():
        return pd.read_csv(p)
    print("[trainer] No data file found. Generating synthetic dataset…")
    df = _synthetic_dataset()
    p.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(p, index=False)
    return df


def main():
    df = load_or_generate(DATA_PATH)
    X, y = build_features(df)

    # Pipeline: scale then multinomial logistic regression
    pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", LogisticRegression(max_iter=200, random_state=RANDOM_STATE)),
    ])

    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=RANDOM_STATE, stratify=y
    )

    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)

    print("[trainer] Classification report:\n", classification_report(y_test, y_pred))

    joblib.dump(pipe, MODEL_PATH)
    meta = {
        "features": BASIC_FEATURES,
        "classes": ["H", "D", "A"],
        "target": "outcome",
        "model_path": str(MODEL_PATH),
    }
    META_PATH.write_text(json.dumps(meta, indent=2))
    print(f"[trainer] Saved model to {MODEL_PATH}")


if __name__ == "__main__":
    main()