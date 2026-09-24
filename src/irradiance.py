"""Clear-sky irradiance and solar geometry. Pure functions, no I/O."""
import math

SOLAR_CONSTANT = 1361.0  # W/m2

def solar_declination(day_of_year: int) -> float:
    """Declination in radians. Cooper equation."""
    if not 1 <= day_of_year <= 366:
        raise ValueError("day_of_year must be 1..366")
    return math.radians(23.45) * math.sin(2 * math.pi * (284 + day_of_year) / 365.0)

def hour_angle(hour: float) -> float:
    """Hour angle in radians from local solar time hour (0..24)."""
    if not 0.0 <= hour <= 24.0:
        raise ValueError("hour must be 0..24")
    return math.radians(15.0 * (hour - 12.0))

def cos_zenith(lat_deg: float, day_of_year: int, hour: float) -> float:
    """Cosine of solar zenith angle, clamped to [-1, 1]."""
    lat = math.radians(lat_deg)
    dec = solar_declination(day_of_year)
    ha = hour_angle(hour)
    cz = math.sin(lat) * math.sin(dec) + math.cos(lat) * math.cos(dec) * math.cos(ha)
    return max(-1.0, min(1.0, cz))

def ghi_clear_sky(lat_deg: float, day_of_year: int, hour: float) -> float:
    """Clear-sky GHI in W/m2. Zero at night. Simple Hottel-inspired scaling."""
    cz = cos_zenith(lat_deg, day_of_year, hour)
    if cz <= 0.0:
        return 0.0
    # atmospheric attenuation 0.75 at zenith, scaled by air mass ~ 1/cz
    air_mass = 1.0 / max(cz, 0.15)
    tau = 0.75 ** (air_mass ** 0.678)
    return round(SOLAR_CONSTANT * cz * tau, 3)

def daily_ghi(lat_deg: float, day_of_year: int) -> float:
    """Daily insolation Wh/m2 by 15-min integration of clear-sky GHI."""
    total = 0.0
    h = 0.0
    while h < 24.0:
        total += ghi_clear_sky(lat_deg, day_of_year, h + 0.125) * 0.25
        h += 0.25
    return round(total, 2)


def sunrise_sunset(lat_deg: float, day_of_year: int) -> dict:
    """Sunrise/sunset hours (solar time) and day length. Polar day/night guarded."""
    import math
    lat = math.radians(lat_deg)
    dec = solar_declination(day_of_year)
    cos_h = -math.tan(lat) * math.tan(dec)
    if cos_h < -1.0:
        return {"sunrise": 0.0, "sunset": 24.0, "daylight_h": 24.0, "polar": "day"}
    if cos_h > 1.0:
        return {"sunrise": 12.0, "sunset": 12.0, "daylight_h": 0.0, "polar": "night"}
    h = math.degrees(math.acos(cos_h)) / 15.0
    return {"sunrise": round(12 - h, 2), "sunset": round(12 + h, 2),
            "daylight_h": round(2 * h, 2), "polar": "none"}
