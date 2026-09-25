"""PM Surya Ghar subsidy slabs (INR, 2026).

Hardened: non-positive kW/capex rejected, net capex floored at zero.
"""
from __future__ import annotations
def subsidy_inr(kw: float) -> float:
    if kw <= 0:
        raise ValueError("kw must be > 0")
    if kw <= 1:
        return 30000.0
    if kw <= 2:
        return 60000.0
    return 78000.0
def net_capex_inr(capex: float, kw: float) -> float:
    if capex <= 0:
        raise ValueError("capex must be > 0")
    return round(max(0.0, capex - subsidy_inr(kw)), 2)
