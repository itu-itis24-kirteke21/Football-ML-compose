from __future__ import annotations
from pydantic import BaseModel, Field

class MatchFeatures(BaseModel):
    home_elo: float = Field(..., examples=[1650])
    away_elo: float = Field(..., examples=[1580])
    home_squad_value: float = Field(..., description="€ millions", examples=[320])
    away_squad_value: float = Field(..., description="€ millions", examples=[220])
    home_form: float = Field(..., ge=0, le=1, examples=[0.72])
    away_form: float = Field(..., ge=0, le=1, examples=[0.41])
    home_goals_last5: int = Field(..., ge=0, examples=[8])
    away_goals_last5: int = Field(..., ge=0, examples=[5])