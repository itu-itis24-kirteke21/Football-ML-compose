from __future__ import annotations
import pandas as pd


BASIC_FEATURES = [
"home_elo", "away_elo",
"home_squad_value", "away_squad_value",
"home_form", "away_form",
"home_goals_last5", "away_goals_last5",
]


LABEL_COL = "outcome" # {"H","D","A"}


ENCODERS = {}


def build_features(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    X = df[BASIC_FEATURES].copy()
    y = df[LABEL_COL].copy()
    return X, y