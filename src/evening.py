"""Evening peak load estimator."""
from __future__ import annotations
def evening_peak_kw(day_kwh: float, evening_frac: float = 0.35) -> float:
    if day_kwh < 0 or not 0.0 <= evening_frac <= 0.8:
        raise ValueError("day_kwh >= 0 and evening_frac 0..0.8 required")
    return round(day_kwh * evening_frac / 4.0, 3)
