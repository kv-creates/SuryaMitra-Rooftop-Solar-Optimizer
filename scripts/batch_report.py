import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from src.loader import load_rooftops
from src.optimizer import annual_yield_kwh
from src.finance import system_cost_inr, annual_savings_inr, payback_years
rows = load_rooftops()
lines = ["# Batch Report", ""]
for r in rows:
    a = annual_yield_kwh(r["lat_deg"], r["area_m2"], tilt_deg=r["tilt_deg"])
    kw = r["area_m2"]*0.20
    capex = system_cost_inr(kw)
    sav = annual_savings_inr(a["annual_kwh"])
    pb = payback_years(capex, sav)
    lines.append(f"- {r["id"]}: {a["annual_kwh"]} kWh/yr, capex INR {capex}, payback {pb} yrs")
pathlib.Path("reports/mumbai_batch.md").parent.mkdir(parents=True, exist_ok=True)
pathlib.Path("reports/mumbai_batch.md").write_text("\n".join(lines)+"\n")
print("\n".join(lines))
