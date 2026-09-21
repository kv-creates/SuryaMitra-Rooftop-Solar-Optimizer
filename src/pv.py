"""PV power model with temperature derating and tilt gain.

Hardened: night/zero-area return 0.0, eff validated, derate clamped 0.5..1.05.
"""
from __future__ import annotations
import math
from .irradiance import ghi_clear_sky
from .shading import combined_factor

def cell_temperature(ambient_c: float, ghi: float, noct: float = 45.0) -> float:
    """Cell temp from ambient + irradiance. NOCT model."""
    if ghi < 0:
        raise ValueError("ghi must be >= 0")
    return round(ambient_c + (noct - 20.0) / 800.0 * ghi, 3)

def tilt_gain(tilt_deg: float, lat_deg: float) -> float:
    """Empirical tilt gain vs flat: peak near latitude tilt, capped."""
    if not 0.0 <= tilt_deg <= 60.0:
        raise ValueError("tilt_deg must be 0..60")
    opt = min(abs(lat_deg), 35.0)
    gain = 1.0 + 0.18 * math.cos(math.radians(tilt_deg - opt)) - 0.18 * math.cos(math.radians(opt))
    # flat (0 deg) gives baseline < 1 when lat high; normalize so flat ~1.0
    flat = 1.0 + 0.18 * math.cos(math.radians(opt)) - 0.18 * math.cos(math.radians(opt))
    return round(gain / flat, 4)

def dc_power_kw(ghi: float, area_m2: float, eff: float, ambient_c: float,
                tilt_deg: float, lat_deg: float, temp_coeff: float = -0.0038) -> float:
    """Instantaneous DC kW. Handles night and zero-area safely."""
    if area_m2 < 0 or not 0.0 <= eff <= 0.30:
        raise ValueError("area_m2 >= 0 and eff in 0..0.30 required")
    if ghi <= 0 or area_m2 == 0:
        return 0.0
    tcell = cell_temperature(ambient_c, ghi)
    derate = 1.0 + temp_coeff * (tcell - 25.0)
    derate = max(0.5, min(1.05, derate))
    p = ghi * area_m2 * eff / 1000.0 * derate * tilt_gain(tilt_deg, lat_deg)
    return round(max(0.0, p), 4)

def daily_yield_kwh(lat_deg: float, day: int, area_m2: float, eff: float = 0.20,
                    tilt_deg: float = 15.0, ambient_c: float = 30.0,
                    horizon_deg: float = 5.0) -> float:
    """Daily kWh via 15-min integration with shading factor."""
    if area_m2 == 0:
        return 0.0
    shade = combined_factor(tilt_deg, horizon_deg)
    e = 0.0
    h = 0.0
    while h < 24.0:
        ghi = ghi_clear_sky(lat_deg, day, h + 0.125) * shade
        e += dc_power_kw(ghi, area_m2, eff, ambient_c, tilt_deg, lat_deg) * 0.25
        h += 0.25
    return round(e, 3)
