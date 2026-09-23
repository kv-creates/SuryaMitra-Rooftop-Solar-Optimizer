import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from src.loader import load_rooftops
from src.optimizer import annual_yield_kwh
from src.tariffs import tariff_for
from src.finance import annual_savings_inr
out = []
for r in load_rooftops():
    a = annual_yield_kwh(r["lat_deg"], r["area_m2"], tilt_deg=r["tilt_deg"])
    t = tariff_for("MH")
    out.append({"id": r["id"], "annual_kwh": a["annual_kwh"], "savings_inr": annual_savings_inr(a["annual_kwh"], t)})
pathlib.Path("reports").mkdir(exist_ok=True)
pathlib.Path("reports/multisite_results.json").write_text(json.dumps(out, indent=2))
print(f"wrote {len(out)} sites")
