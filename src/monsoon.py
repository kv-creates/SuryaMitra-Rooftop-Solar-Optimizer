"""Month-wise cloud derate for Indian monsoon (Mumbai-tuned defaults)."""
from __future__ import annotations
MONSOON_CLOUD = {1: 0.10, 2: 0.10, 3: 0.12, 4: 0.15, 5: 0.20, 6: 0.55,
                 7: 0.65, 8: 0.60, 9: 0.45, 10: 0.25, 11: 0.12, 12: 0.10}
def cloud_for_month(month: int) -> float:
    if not 1 <= month <= 12:
        raise ValueError("month must be 1..12")
    return MONSOON_CLOUD[month]
def derated_monthly(monthly: list[dict]) -> list[dict]:
    """Apply (1-cloud) factor to annual_yield monthly table."""
    out = []
    for r in monthly:
        c = cloud_for_month(r["month"])
        out.append({"month": r["month"], "kwh": round(r["kwh"] * (1 - c), 2), "cloud": c})
    return out
