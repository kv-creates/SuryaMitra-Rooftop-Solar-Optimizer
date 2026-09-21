import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
"""Run demo and write sample_results.json."""
import json
from src.optimizer import optimize_tilt, annual_yield_kwh
from src.finance import system_cost_inr, annual_savings_inr, lcoe_inr_per_kwh, payback_years
o = optimize_tilt(19.07, 105, 40.0)
a = annual_yield_kwh(19.07, 40.0, tilt_deg=o["best_tilt_deg"])
kw = 40.0 * 0.20
capex = system_cost_inr(kw)
sav = annual_savings_inr(a["annual_kwh"])
out = {"best_tilt_deg": o["best_tilt_deg"], "annual_kwh": a["annual_kwh"], "capex_inr": capex, "lcoe": lcoe_inr_per_kwh(capex, a["annual_kwh"]), "payback": payback_years(capex, sav)}
open("sample_results.json", "w").write(json.dumps(out, indent=2))
print(out)
