from __future__ import annotations
import requests
import os

API_URL = "https://api.football-data.org/v4/competitions/PL/matches?status=SCHEDULED"

def get_upcoming_matches(api_key: str | None, limit: int = 5) -> list[dict]:
    """
    Fetches upcoming scheduled matches for the Premier League.
    """
    if not api_key:
        print("[fetcher] No API key provided. Skipping fetch.")
        return []

    headers = {"X-Auth-Token": api_key}
    try:
        response = requests.get(API_URL, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        matches = data.get("matches", [])
        return matches[:limit]
    except Exception as e:
        print(f"[fetcher] Error fetching matches: {e}")
        return []
