"""Battery sizing for backup hours and night load."""
from __future__ import annotations
def battery_kwh(night_kwh: float, autonomy_days: float = 1.0, dod: float = 0.9, roundtrip: float = 0.92) -> float:
    """Usable-to-nameplate sizing with depth-of-discharge and round-trip eff."""
    if night_kwh < 0 or autonomy_days <= 0 or not 0.5 <= dod <= 1.0 or not 0.8 <= roundtrip <= 1.0:
        raise ValueError("check night_kwh >= 0, autonomy > 0, dod 0.5..1, roundtrip 0.8..1")
    return round(night_kwh * autonomy_days / (dod * roundtrip), 2)
def backup_hours(battery_kwh_rated: float, load_kw: float, dod: float = 0.9) -> float:
    if battery_kwh_rated < 0 or load_kw <= 0:
        raise ValueError("battery >= 0 and load > 0 required")
    return round(battery_kwh_rated * dod / load_kw, 2)
