"""Demo CLI: end-to-end yield + finance for a Mumbai rooftop."""
from .pv import daily_yield_kwh
from .optimizer import optimize_tilt, annual_yield_kwh
from .finance import system_cost_inr, annual_savings_inr, lcoe_inr_per_kwh, payback_years, npv_inr

def demo():
    lat, day, area = 19.07, 105, 40.0
    print(f"SuryaMitra demo: lat={lat} day={day} area={area}m2")
    o = optimize_tilt(lat, day, area)
    print("best tilt:", o["best_tilt_deg"], "daily kWh:", o["best_daily_kwh"])
    a = annual_yield_kwh(lat, area, tilt_deg=o["best_tilt_deg"])
    print("annual kWh:", a["annual_kwh"])
    kw = area * 0.20
    capex = system_cost_inr(kw)
    sav = annual_savings_inr(a["annual_kwh"])
    print("capex INR:", capex, "savings INR/yr:", sav)
    print("LCOE INR/kWh:", lcoe_inr_per_kwh(capex, a["annual_kwh"]))
    print("payback yrs:", payback_years(capex, sav))
    print("NPV INR:", npv_inr(capex, sav))

if __name__ == "__main__":
    demo()
