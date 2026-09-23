"""Residential tariffs by state (INR/kWh, 2026 indicative)."""
from __future__ import annotations
TARIFFS = {"MH": 8.0, "DL": 6.5, "KA": 7.2, "TN": 6.8, "GJ": 6.2, "RJ": 7.5, "UP": 6.9, "WB": 7.0}
DEFAULT_TARIFF = 8.0
def tariff_for(state: str) -> float:
    if not isinstance(state, str) or not state:
        raise ValueError("state code required")
    return TARIFFS.get(state.upper(), DEFAULT_TARIFF)
def supported_states() -> list[str]:
    return sorted(TARIFFS)
