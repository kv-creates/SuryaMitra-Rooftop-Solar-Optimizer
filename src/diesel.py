"""Diesel generator offset calculator."""
from __future__ import annotations
DIESEL_L_PER_KWH = 0.28
DIESEL_RS_PER_L = 92.0
def diesel_saved_litres(solar_kwh: float) -> float:
    if solar_kwh < 0:
        raise ValueError("solar_kwh must be >= 0")
    return round(solar_kwh * DIESEL_L_PER_KWH, 2)
def diesel_saved_inr(solar_kwh: float) -> float:
    return round(diesel_saved_litres(solar_kwh) * DIESEL_RS_PER_L, 2)
