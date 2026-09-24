import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from src.optimizer import annual_yield_kwh
from src.finance import system_cost_inr, annual_savings_inr, payback_years
a = annual_yield_kwh(19.07, 40.0, tilt_deg=15.0)
capex = system_cost_inr(40.0 * 0.20)
sav = annual_savings_inr(a["annual_kwh"])
pb = payback_years(capex, sav)
html = f"<html><body><h1>SuryaMitra 40m2 Mumbai</h1><p>Annual {a["annual_kwh"]} kWh, capex INR {capex}, payback {pb} yrs.</p></body></html>"
pathlib.Path("reports").mkdir(exist_ok=True)
pathlib.Path("reports/summary.html").write_text(html)
print("wrote reports/summary.html")
