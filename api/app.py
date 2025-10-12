from __future__ import annotations
import os, sqlite3, json
from pathlib import Path
from flask import Flask, request, jsonify
import joblib
import pandas as pd
from schema import MatchFeatures
from wait_for_model import wait

MODEL_DIR = Path(os.getenv("MODEL_DIR", "/shared/model"))
DB_PATH = os.getenv("DB_PATH", "/shared/predictions.db")
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8000"))

app = Flask(__name__)

# Ensure model exists (when container starts after trainer)
wait()

MODEL_PATH = MODEL_DIR / "model.pkl"
META_PATH = MODEL_DIR / "metadata.json"
model = joblib.load(MODEL_PATH)
meta = json.loads(META_PATH.read_text()) if META_PATH.exists() else {}

# Use the learned class order from the model
MODEL_CLASSES = list(getattr(getattr(model, "classes_", []), "tolist", lambda: getattr(model, "classes_", []))()) \
                if hasattr(model, "classes_") else meta.get("classes", [])

# SQLite init
Path(DB_PATH).parent.mkdir(parents=True, exist_ok=True)
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cur = conn.cursor()
cur.execute(
    """
    CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ts DATETIME DEFAULT CURRENT_TIMESTAMP,
        features_json TEXT NOT NULL,
        pred_label TEXT NOT NULL,
        proba_H REAL,
        proba_D REAL,
        proba_A REAL
    )
    """
)
conn.commit()

@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": MODEL_PATH.exists(), "classes": MODEL_CLASSES}

@app.post("/predict")
def predict():
    try:
        payload = request.get_json(force=True)
        item = MatchFeatures(**payload)
        df = pd.DataFrame([{k: getattr(item, k) for k in item.model_fields.keys()}])

        proba = None
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(df)[0]
        label = model.predict(df)[0]

        # Map probabilities to correct labels as learned by the model
        prob_map = None
        if proba is not None and MODEL_CLASSES:
            prob_map = {cls: float(p) for cls, p in zip(MODEL_CLASSES, proba)}

        result = {
            "prediction": str(label),
            "classes": MODEL_CLASSES,
            "probabilities": prob_map,
        }

        def p_of(c):
            if proba is None or not MODEL_CLASSES:
                return None
            try:
                idx = MODEL_CLASSES.index(c)
                return float(proba[idx])
            except ValueError:
                return None

        # Log into SQLite
        cur.execute(
            "INSERT INTO predictions (features_json, pred_label, proba_H, proba_D, proba_A) VALUES (?, ?, ?, ?, ?)",
            (
                json.dumps(payload),
                str(label),
                p_of("H"),
                p_of("D"),
                p_of("A"),
            ),
        )
        conn.commit()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)