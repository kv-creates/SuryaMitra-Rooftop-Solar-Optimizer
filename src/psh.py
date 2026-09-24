"""Peak sun hours from daily insolation."""
from __future__ import annotations
from .irradiance import daily_ghi
def peak_sun_hours(lat_deg: float, day_of_year: int, cloud: float = 0.15) -> float:
    """PSH = clear-sky daily GHI x (1-cloud) / 1000."""
    if not 0.0 <= cloud <= 0.9:
        raise ValueError("cloud must be 0..0.9")
    return round(daily_ghi(lat_deg, day_of_year) * (1 - cloud) / 1000.0, 2)
def annual_psh(lat_deg: float, cloud: float = 0.15) -> float:
    mids = [15, 45, 74, 105, 135, 166, 196, 227, 258, 288, 319, 349]
    dim = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return round(sum(peak_sun_hours(lat_deg, d, cloud) * n for d, n in zip(mids, dim)), 1)
