import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from src.optimizer import annual_yield_kwh
from src.finance import system_cost_inr, annual_savings_inr
from src.subsidy import net_capex_inr
fig, ax = plt.subplots(figsize=(8, 4))
xs, ys = [], []
for area in (20, 30, 40, 60, 80):
    a = annual_yield_kwh(19.07, float(area), tilt_deg=15.0)["annual_kwh"]
    capex = net_capex_inr(system_cost_inr(area * 0.20), area * 0.20)
    pb = capex / annual_savings_inr(a)
    xs.append(area); ys.append(round(pb, 2))
ax.bar(xs, ys, color="#0b3d91", label="payback yrs (net capex)")
ax.set_title("Payback vs Rooftop Area (Mumbai, with subsidy)")
ax.set_xlabel("area m2"); ax.set_ylabel("years")
ax.legend()
fig.tight_layout()
pathlib.Path("docs/images").mkdir(parents=True, exist_ok=True)
fig.savefig("docs/images/payback-chart.png", dpi=150)
print("wrote payback-chart.png")
