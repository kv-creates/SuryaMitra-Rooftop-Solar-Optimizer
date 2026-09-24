import sys, pathlib, json, csv
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from src.optimizer import annual_yield_kwh
rows = list(csv.DictReader(open("data/commercial_sites.csv")))
out = [{"id": r["id"], "annual_kwh": annual_yield_kwh(float(r["lat_deg"]), float(r["area_m2"]), tilt_deg=float(r["tilt_deg"]))["annual_kwh"]} for r in rows]
pathlib.Path("reports/commercial_results.json").write_text(json.dumps(out, indent=2))
print(f"wrote {len(out)} commercial sites")
