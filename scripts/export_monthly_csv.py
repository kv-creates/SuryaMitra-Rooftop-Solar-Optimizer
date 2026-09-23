import sys, pathlib, csv
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from src.optimizer import annual_yield_kwh
a = annual_yield_kwh(19.07, 40.0, tilt_deg=15.0)
pathlib.Path("reports").mkdir(exist_ok=True)
with open("reports/monthly_yield.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["month", "kwh"])
    w.writeheader(); w.writerows(a["monthly"])
print("wrote reports/monthly_yield.csv")
