"""Recommended fixed tilt per state capital latitude."""
from __future__ import annotations
STATE_TILT = {"MH": 19, "DL": 29, "KA": 13, "TN": 13, "GJ": 23, "RJ": 27, "UP": 27, "WB": 23}
def recommended_tilt(state: str) -> float:
    if not isinstance(state, str) or not state:
        raise ValueError("state code required")
    return float(STATE_TILT.get(state.upper(), 18))
def tilt_table() -> list[dict]:
    return [{"state": s, "tilt_deg": t} for s, t in sorted(STATE_TILT.items())]
