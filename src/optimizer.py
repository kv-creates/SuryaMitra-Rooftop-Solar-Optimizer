"""Tilt/azimuth grid-search optimizer."""
from __future__ import annotations
from .pv import daily_yield_kwh

def optimize_tilt(lat_deg: float, day: int, area_m2: float, eff: float = 0.20,
                  ambient_c: float = 30.0, tilts: tuple = (0, 5, 10, 15, 20, 25, 30)) -> dict:
    """Search discrete tilts, return best tilt and yields table."""
    if area_m2 <= 0:
        raise ValueError("area_m2 must be > 0")
    rows = []
    for t in tilts:
        y = daily_yield_kwh(lat_deg, day, area_m2, eff, float(t), ambient_c)
        rows.append({"tilt_deg": float(t), "daily_kwh": y})
    best = max(rows, key=lambda r: r["daily_kwh"])
    return {"best_tilt_deg": best["tilt_deg"], "best_daily_kwh": best["daily_kwh"], "table": rows}

def annual_yield_kwh(lat_deg: float, area_m2: float, eff: float = 0.20,
                     tilt_deg: float = 15.0, ambient_c: float = 30.0) -> dict:
    """Annual kWh by sampling 12 mid-month days and scaling."""
    mids = [15, 45, 74, 105, 135, 166, 196, 227, 258, 288, 319, 349]
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0.0
    monthly = []
    for m, d in enumerate(mids):
        y = daily_yield_kwh(lat_deg, d, area_m2, eff, tilt_deg, ambient_c)
        me = round(y * days_in_month[m], 2)
        monthly.append({"month": m + 1, "kwh": me})
        total += me
    return {"annual_kwh": round(total, 2), "monthly": monthly}
