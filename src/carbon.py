"""CO2 avoidance from solar generation (Indian grid factor)."""
from __future__ import annotations
GRID_FACTOR_KG_PER_KWH = 0.82
def co2_avoided_tonnes(annual_kwh: float, years: int = 25) -> float:
    if annual_kwh < 0 or years <= 0:
        raise ValueError("annual_kwh >= 0 and years > 0 required")
    return round(annual_kwh * years * GRID_FACTOR_KG_PER_KWH / 1000.0, 2)
def trees_equivalent(tonnes: float) -> float:
    if tonnes < 0:
        raise ValueError("tonnes must be >= 0")
    return round(tonnes * 45.0, 1)
