"""O&M schedule: cleaning reminders and inspection intervals."""
from __future__ import annotations
def cleans_per_year(pm25: float) -> int:
    if pm25 < 0:
        raise ValueError("pm25 must be >= 0")
    if pm25 < 40:
        return 12
    if pm25 < 80:
        return 24
    return 36
def annual_om_inr(kw: float, rate_per_kw: float = 550.0) -> float:
    if kw <= 0 or rate_per_kw <= 0:
        raise ValueError("kw and rate must be > 0")
    return round(kw * rate_per_kw, 2)
