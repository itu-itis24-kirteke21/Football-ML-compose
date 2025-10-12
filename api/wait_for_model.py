from __future__ import annotations
import os, time
from pathlib import Path

MODEL_DIR = Path(os.getenv("MODEL_DIR", "/shared/model"))
MODEL_PATH = MODEL_DIR / "model.pkl"

def wait(timeout: int = 300, poll: float = 1.0)-> None:
    t0 = time.time()
    while time.time()- t0 < timeout:
        if MODEL_PATH.exists():
            return
        time.sleep(poll)
    raise TimeoutError(f"Model not found at {MODEL_PATH} within {timeout}s")