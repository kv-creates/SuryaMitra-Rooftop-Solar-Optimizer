"""Inverter sizing: DC/AC ratio, clipping loss, efficiency."""
from __future__ import annotations
def clipping_loss(dc_ac_ratio: float) -> float:
    """Annual clipping fraction from DC/AC ratio 1.0..1.5."""
    if not 1.0 <= dc_ac_ratio <= 1.5:
        raise ValueError("dc_ac_ratio must be 1.0..1.5")
    return round(max(0.0, (dc_ac_ratio - 1.15) * 0.06), 4)
def ac_yield_kwh(dc_kwh: float, dc_ac_ratio: float = 1.2, inv_eff: float = 0.97) -> float:
    if dc_kwh < 0 or not 0.9 <= inv_eff <= 0.99:
        raise ValueError("dc_kwh >= 0 and inv_eff 0.9..0.99 required")
    return round(dc_kwh * (1 - clipping_loss(dc_ac_ratio)) * inv_eff, 2)
def recommended_kw(dc_kw: float) -> float:
    if dc_kw <= 0:
        raise ValueError("dc_kw must be > 0")
    return round(dc_kw / 1.2, 2)
