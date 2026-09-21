"""Shading and soiling losses. All factors in 0..1 (1 = no loss)."""
from __future__ import annotations

def horizon_loss(tilt_deg: float, horizon_deg: float = 0.0) -> float:
    """Loss from distant horizon obstruction. horizon_deg 0..40."""
    if not 0.0 <= tilt_deg <= 90.0:
        raise ValueError("tilt_deg must be 0..90")
    if not 0.0 <= horizon_deg <= 40.0:
        raise ValueError("horizon_deg must be 0..40")
    return round(max(0.0, 1.0 - 0.004 * horizon_deg * (1.0 + tilt_deg / 90.0)), 4)

def interrow_loss(tilt_deg: float, gcr: float = 0.5) -> float:
    """Inter-row shading factor from ground coverage ratio 0.2..0.9."""
    if not 0.2 <= gcr <= 0.9:
        raise ValueError("gcr must be 0.2..0.9")
    if not 0.0 <= tilt_deg <= 60.0:
        raise ValueError("tilt_deg must be 0..60 for rooftop rows")
    loss = 0.02 + 0.10 * gcr * (tilt_deg / 60.0)
    return round(max(0.0, 1.0 - loss), 4)

def soiling_loss(pm25: float = 40.0, days_since_clean: int = 15) -> float:
    """Soiling factor from PM2.5 and cleaning interval."""
    if pm25 < 0 or days_since_clean < 0:
        raise ValueError("pm25 and days_since_clean must be >= 0")
    loss = min(0.15, 0.0004 * pm25 * (days_since_clean ** 0.7))
    return round(1.0 - loss, 4)

def combined_factor(tilt_deg: float, horizon_deg: float = 5.0, gcr: float = 0.5,
                    pm25: float = 40.0, days_since_clean: int = 15) -> float:
    """Product of all shading/soiling factors."""
    return round(
        horizon_loss(tilt_deg, horizon_deg)
        * interrow_loss(tilt_deg, gcr)
        * soiling_loss(pm25, days_since_clean),
        4,
    )
