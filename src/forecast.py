"""Synthetic TMY + noise forecast for demo and visuals."""
from __future__ import annotations
import math, random
from .irradiance import ghi_clear_sky

def synthetic_day(lat_deg: float, day: int, cloud: float = 0.15, seed: int = 7) -> list[dict]:
    """24 hourly GHI values with deterministic pseudo-cloud noise."""
    if not 0.0 <= cloud <= 0.9:
        raise ValueError("cloud must be 0..0.9")
    rng = random.Random(seed + day)
    out = []
    for h in range(24):
        base = ghi_clear_sky(lat_deg, day, float(h) + 0.5)
        dip = 1.0 - cloud * (0.5 + 0.5 * math.sin(h / 3.0 + seed)) * rng.uniform(0.4, 1.0)
        ghi = round(max(0.0, base * dip), 2)
        out.append({"hour": h, "ghi": ghi})
    return out

def tmy_annual_ghi(lat_deg: float, cloud: float = 0.15) -> float:
    """Annual Wh/m2 from 12 mid-month synthetic days scaled to months."""
    mids = [15, 45, 74, 105, 135, 166, 196, 227, 258, 288, 319, 349]
    dim = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    tot = 0.0
    for d, n in zip(mids, dim):
        day = synthetic_day(lat_deg, d, cloud)
        tot += sum(r["ghi"] for r in day) * n
    return round(tot, 2)
