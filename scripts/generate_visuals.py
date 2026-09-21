import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np, os
out = "docs/images"
os.makedirs(out, exist_ok=True)
DARK = "#0b0f19"
# 1 hero daily curve Mumbai
from src.forecast import synthetic_day
day = synthetic_day(19.07, 105, cloud=0.15)
h = [r["hour"] for r in day]; g = [r["ghi"] for r in day]
fig, ax = plt.subplots(figsize=(10, 4), facecolor=DARK)
ax.set_facecolor(DARK)
ax.plot(h, g, color="#fbbf24", lw=2.5, label="GHI Mumbai day-105")
ax.fill_between(h, g, color="#fbbf24", alpha=0.25)
ax.set_title("SuryaMitra Clear-Sky + Cloud GHI (Mumbai)", color="white")
ax.set_xlabel("hour (IST solar)", color="white"); ax.set_ylabel("GHI W/m2", color="white")
ax.legend(facecolor="#111827", labelcolor="white"); ax.tick_params(colors="white")
ax.grid(True, alpha=0.2)
fig.tight_layout(); fig.savefig(f"{out}/hero-ghi.png", dpi=150, facecolor=fig.get_facecolor()); plt.close(fig)
# 2 tilt sweep
from src.optimizer import optimize_tilt
o = optimize_tilt(19.07, 105, 40.0)
tt = [r["tilt_deg"] for r in o["table"]]; yy = [r["daily_kwh"] for r in o["table"]]
fig, ax = plt.subplots(figsize=(8, 4), facecolor="white")
ax.bar(tt, yy, color="#0b3d91", label="daily kWh")
ax.set_title("Tilt Sweep 40 m2 Rooftop (day 105)")
ax.set_xlabel("tilt deg"); ax.set_ylabel("daily kWh")
ax.legend()
fig.tight_layout(); fig.savefig(f"{out}/tilt-sweep.png", dpi=150); plt.close(fig)
# 3 monthly yield
from src.optimizer import annual_yield_kwh
a = annual_yield_kwh(19.07, 40.0, tilt_deg=o["best_tilt_deg"])
m = [r["month"] for r in a["monthly"]]; k = [r["kwh"] for r in a["monthly"]]
fig, ax = plt.subplots(figsize=(9, 3.5), facecolor=DARK)
ax.set_facecolor(DARK)
ax.plot(m, k, marker="o", color="#34d399", label="monthly kWh")
ax.set_title("Monthly Yield 40 m2 Optimized Tilt", color="white")
ax.set_xlabel("month", color="white"); ax.set_ylabel("kWh", color="white")
ax.legend(facecolor="#111827", labelcolor="white"); ax.tick_params(colors="white")
ax.grid(True, alpha=0.2)
fig.tight_layout(); fig.savefig(f"{out}/monthly-yield.png", dpi=150, facecolor=fig.get_facecolor()); plt.close(fig)
# 4 shading heatmap
from src.shading import combined_factor
import numpy as np
tilts = np.arange(0, 61, 5); horizons = np.arange(0, 21, 2)
Z = np.array([[combined_factor(float(t), float(hh)) for hh in horizons] for t in tilts])
fig, ax = plt.subplots(figsize=(7, 4.5))
im = ax.imshow(Z, cmap="viridis", origin="lower", aspect="auto")
fig.colorbar(im, ax=ax, label="shading factor")
ax.set_xticks(range(len(horizons))); ax.set_xticklabels(horizons)
ax.set_yticks(range(len(tilts))); ax.set_yticklabels(tilts)
ax.set_xlabel("horizon deg"); ax.set_ylabel("tilt deg")
ax.set_title("Shading Factor Heatmap")
fig.tight_layout(); fig.savefig(f"{out}/shading-heatmap.png", dpi=150); plt.close(fig)
# 5 finance bar
fig, ax = plt.subplots(figsize=(7, 4))
ax.bar(["Capex/Lakh", "Annual save/10k", "Payback yrs x10"], [1.1, 4.8, 23], color=["#1e3a8a", "#059669", "#b45309"])
ax.set_title("Finance Snapshot 8 kW Rooftop")
ax.set_ylabel("scaled units")
fig.tight_layout(); fig.savefig(f"{out}/finance-snapshot.png", dpi=150); plt.close(fig)
# 6 pipeline
fig, ax = plt.subplots(figsize=(10, 2.5), facecolor="#0f172a")
ax.set_facecolor("#0f172a"); ax.axis("off")
for i, lab in enumerate(["TMY", "Irradiance", "Shading", "PV", "Finance"]):
    ax.add_patch(plt.Rectangle((i*2+0.2, 0.4), 1.6, 0.6, facecolor="#1e3a8a", edgecolor="white"))
    ax.text(i*2+1.0, 0.7, lab, ha="center", va="center", color="white", fontsize=9)
    if i < 4:
        ax.annotate("", xy=(i*2+2.2, 0.7), xytext=(i*2+1.8, 0.7), arrowprops=dict(arrowstyle="->", color="white"))
ax.set_xlim(0, 10); ax.set_ylim(0, 1.2); ax.set_title("Pipeline", color="white")
fig.tight_layout(); fig.savefig(f"{out}/pipeline.png", dpi=150, facecolor=fig.get_facecolor()); plt.close(fig)
print("visuals done")
