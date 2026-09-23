"""Lifetime energy with panel degradation and O&M."""
from __future__ import annotations
def lifetime_kwh(annual_kwh: float, years: int = 25, degradation: float = 0.005) -> dict:
    """Year-by-year discounted-by-degradation energy (not financial discount)."""
    if annual_kwh <= 0 or years <= 0:
        raise ValueError("annual_kwh and years must be > 0")
    if not 0.0 <= degradation <= 0.02:
        raise ValueError("degradation must be 0..0.02")
    yearly = [round(annual_kwh * (1 - degradation) ** (y - 1), 2) for y in range(1, years + 1)]
    return {"lifetime_kwh": round(sum(yearly), 2), "yearly": yearly}
