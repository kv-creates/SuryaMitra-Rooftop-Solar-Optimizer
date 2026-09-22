"""LCOE, payback, NPV for rooftop PV."""
from __future__ import annotations

def system_cost_inr(kw: float, rate_per_kw: float = 55000.0) -> float:
    if kw <= 0 or rate_per_kw <= 0:
        raise ValueError("kw and rate_per_kw must be > 0")
    return round(kw * rate_per_kw, 2)

def annual_savings_inr(annual_kwh: float, tariff: float = 8.0) -> float:
    if annual_kwh < 0 or tariff <= 0:
        raise ValueError("annual_kwh >= 0 and tariff > 0 required")
    return round(annual_kwh * tariff, 2)

def lcoe_inr_per_kwh(capex: float, annual_kwh: float, lifetime_yrs: int = 25,
                     discount: float = 0.08, opex_frac: float = 0.01) -> float:
    """Levelized cost with discounted energy and O&M."""
    if capex <= 0 or annual_kwh <= 0 or lifetime_yrs <= 0:
        raise ValueError("capex, annual_kwh, lifetime_yrs must be > 0")
    if not 0.0 <= discount <= 0.25:
        raise ValueError("discount must be 0..0.25")
    pv_energy = sum(annual_kwh * 0.995 ** y / (1 + discount) ** y for y in range(1, lifetime_yrs + 1))
    pv_cost = capex + sum(capex * opex_frac / (1 + discount) ** y for y in range(1, lifetime_yrs + 1))
    return round(pv_cost / pv_energy, 3)

def payback_years(capex: float, annual_savings: float) -> float:
    if capex <= 0 or annual_savings <= 0:
        raise ValueError("capex and annual_savings must be > 0")
    return round(capex / annual_savings, 2)

def npv_inr(capex: float, annual_savings: float, lifetime_yrs: int = 25,
            discount: float = 0.08) -> float:
    if capex <= 0 or annual_savings <= 0:
        raise ValueError("capex and annual_savings must be > 0")
    pv = sum(annual_savings / (1 + discount) ** y for y in range(1, lifetime_yrs + 1))
    return round(pv - capex, 2)


def net_metering_credit(export_kwh: float, import_kwh: float, export_rate: float = 3.5, import_rate: float = 8.0) -> float:
    """Net annual bill credit: import cost minus export earnings, floored at zero bill."""
    if export_kwh < 0 or import_kwh < 0 or export_rate <= 0 or import_rate <= 0:
        raise ValueError("kwh >= 0 and rates > 0 required")
    return round(max(0.0, import_kwh * import_rate - export_kwh * export_rate), 2)
