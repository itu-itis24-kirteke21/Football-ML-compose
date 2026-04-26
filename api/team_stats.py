from __future__ import annotations

# Static dictionary mapping team names (from football-data.org) to their model features.
# Stats are approximate for demonstration purposes.
TEAM_STATS: dict[str, dict[str, float | int]] = {
    "Arsenal FC": {
        "home_elo": 1880, "away_elo": 1880,
        "home_squad_value": 1100, "away_squad_value": 1100,
        "home_form": 0.85, "away_form": 0.80,
        "home_goals_last5": 12, "away_goals_last5": 10
    },
    "Manchester City FC": {
        "home_elo": 1950, "away_elo": 1950,
        "home_squad_value": 1200, "away_squad_value": 1200,
        "home_form": 0.90, "away_form": 0.85,
        "home_goals_last5": 15, "away_goals_last5": 12
    },
    "Liverpool FC": {
        "home_elo": 1870, "away_elo": 1870,
        "home_squad_value": 900, "away_squad_value": 900,
        "home_form": 0.82, "away_form": 0.75,
        "home_goals_last5": 11, "away_goals_last5": 9
    },
    "Aston Villa FC": {
        "home_elo": 1780, "away_elo": 1780,
        "home_squad_value": 600, "away_squad_value": 600,
        "home_form": 0.70, "away_form": 0.65,
        "home_goals_last5": 9, "away_goals_last5": 7
    },
    "Tottenham Hotspur FC": {
        "home_elo": 1790, "away_elo": 1790,
        "home_squad_value": 750, "away_squad_value": 750,
        "home_form": 0.60, "away_form": 0.55,
        "home_goals_last5": 10, "away_goals_last5": 8
    },
    "Chelsea FC": {
        "home_elo": 1760, "away_elo": 1760,
        "home_squad_value": 950, "away_squad_value": 950,
        "home_form": 0.55, "away_form": 0.50,
        "home_goals_last5": 8, "away_goals_last5": 6
    },
    "Manchester United FC": {
        "home_elo": 1770, "away_elo": 1770,
        "home_squad_value": 850, "away_squad_value": 850,
        "home_form": 0.50, "away_form": 0.45,
        "home_goals_last5": 7, "away_goals_last5": 5
    },
    "Newcastle United FC": {
        "home_elo": 1785, "away_elo": 1785,
        "home_squad_value": 650, "away_squad_value": 650,
        "home_form": 0.65, "away_form": 0.60,
        "home_goals_last5": 9, "away_goals_last5": 7
    },
    "West Ham United FC": {
        "home_elo": 1740, "away_elo": 1740,
        "home_squad_value": 450, "away_squad_value": 450,
        "home_form": 0.45, "away_form": 0.40,
        "home_goals_last5": 6, "away_goals_last5": 4
    },
    "Brighton & Hove Albion FC": {
        "home_elo": 1750, "away_elo": 1750,
        "home_squad_value": 500, "away_squad_value": 500,
        "home_form": 0.50, "away_form": 0.45,
        "home_goals_last5": 7, "away_goals_last5": 5
    },
    "Wolverhampton Wanderers FC": {
        "home_elo": 1710, "away_elo": 1710,
        "home_squad_value": 350, "away_squad_value": 350,
        "home_form": 0.40, "away_form": 0.35,
        "home_goals_last5": 5, "away_goals_last5": 3
    },
    "Fulham FC": {
        "home_elo": 1720, "away_elo": 1720,
        "home_squad_value": 340, "away_squad_value": 340,
        "home_form": 0.42, "away_form": 0.38,
        "home_goals_last5": 5, "away_goals_last5": 4
    },
    "AFC Bournemouth": {
        "home_elo": 1705, "away_elo": 1705,
        "home_squad_value": 300, "away_squad_value": 300,
        "home_form": 0.45, "away_form": 0.40,
        "home_goals_last5": 6, "away_goals_last5": 5
    },
    "Crystal Palace FC": {
        "home_elo": 1715, "away_elo": 1715,
        "home_squad_value": 400, "away_squad_value": 400,
        "home_form": 0.48, "away_form": 0.44,
        "home_goals_last5": 6, "away_goals_last5": 4
    },
    "Brentford FC": {
        "home_elo": 1725, "away_elo": 1725,
        "home_squad_value": 420, "away_squad_value": 420,
        "home_form": 0.40, "away_form": 0.35,
        "home_goals_last5": 5, "away_goals_last5": 3
    },
    "Everton FC": {
        "home_elo": 1690, "away_elo": 1690,
        "home_squad_value": 350, "away_squad_value": 350,
        "home_form": 0.35, "away_form": 0.30,
        "home_goals_last5": 4, "away_goals_last5": 2
    },
    "Nottingham Forest FC": {
        "home_elo": 1680, "away_elo": 1680,
        "home_squad_value": 380, "away_squad_value": 380,
        "home_form": 0.30, "away_form": 0.25,
        "home_goals_last5": 4, "away_goals_last5": 3
    },
    "Luton Town FC": {
        "home_elo": 1640, "away_elo": 1640,
        "home_squad_value": 100, "away_squad_value": 100,
        "home_form": 0.25, "away_form": 0.20,
        "home_goals_last5": 3, "away_goals_last5": 2
    },
    "Burnley FC": {
        "home_elo": 1650, "away_elo": 1650,
        "home_squad_value": 250, "away_squad_value": 250,
        "home_form": 0.20, "away_form": 0.15,
        "home_goals_last5": 3, "away_goals_last5": 2
    },
    "Sheffield United FC": {
        "home_elo": 1620, "away_elo": 1620,
        "home_squad_value": 150, "away_squad_value": 150,
        "home_form": 0.15, "away_form": 0.10,
        "home_goals_last5": 2, "away_goals_last5": 1
    },
    "Leicester City FC": {
        "home_elo": 1700, "away_elo": 1700,
        "home_squad_value": 280, "away_squad_value": 280,
        "home_form": 0.40, "away_form": 0.35,
        "home_goals_last5": 5, "away_goals_last5": 3
    },
    "Ipswich Town FC": {
        "home_elo": 1650, "away_elo": 1650,
        "home_squad_value": 150, "away_squad_value": 150,
        "home_form": 0.30, "away_form": 0.25,
        "home_goals_last5": 4, "away_goals_last5": 2
    },
    "Southampton FC": {
        "home_elo": 1680, "away_elo": 1680,
        "home_squad_value": 250, "away_squad_value": 250,
        "home_form": 0.35, "away_form": 0.30,
        "home_goals_last5": 4, "away_goals_last5": 3
    },
    "Leeds United FC": {
        "home_elo": 1710, "away_elo": 1710,
        "home_squad_value": 220, "away_squad_value": 220,
        "home_form": 0.55, "away_form": 0.50,
        "home_goals_last5": 7, "away_goals_last5": 5
    },
    "Sunderland AFC": {
        "home_elo": 1685, "away_elo": 1685,
        "home_squad_value": 120, "away_squad_value": 120,
        "home_form": 0.52, "away_form": 0.48,
        "home_goals_last5": 6, "away_goals_last5": 4
    }
}
