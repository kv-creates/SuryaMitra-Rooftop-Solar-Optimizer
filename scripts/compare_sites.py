import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from src.loader import load_rooftops
from src.optimizer import annual_yield_kwh
rows = load_rooftops()
comp = sorted([{"id": r["id"], "annual_kwh": annual_yield_kwh(r["lat_deg"], r["area_m2"], tilt_deg=r["tilt_deg"])["annual_kwh"]} for r in rows], key=lambda x: -x["annual_kwh"])
pathlib.Path("reports").mkdir(exist_ok=True)
pathlib.Path("reports/comparison.json").write_text(json.dumps(comp, indent=2))
print(f"ranked {len(comp)} sites")
