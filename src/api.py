"""FastAPI surface with strict validation (no crashes on bad input).

Hardened: /ghi returns error object on out-of-range, pydantic bounds all POST bodies.
"""
from fastapi import FastAPI
from pydantic import BaseModel, Field
from .irradiance import ghi_clear_sky, daily_ghi
from .pv import daily_yield_kwh
from .optimizer import optimize_tilt, annual_yield_kwh
from .finance import system_cost_inr, annual_savings_inr, lcoe_inr_per_kwh, payback_years

app = FastAPI(title="SuryaMitra Rooftop Solar Optimizer", version="0.1.0")

class YieldReq(BaseModel):
    lat_deg: float = Field(ge=-90, le=90)
    day: int = Field(ge=1, le=366)
    area_m2: float = Field(ge=0, le=10000)
    eff: float = Field(ge=0.05, le=0.30)
    tilt_deg: float = Field(ge=0, le=60)
    ambient_c: float = Field(ge=-10, le=55)

class OptimizeReq(BaseModel):
    lat_deg: float = Field(ge=-90, le=90)
    day: int = Field(ge=1, le=366)
    area_m2: float = Field(gt=0, le=10000)

@app.get("/health")
def health():
    return {"status": "ok", "version": "0.1.0"}

@app.get("/ghi")
def ghi(lat_deg: float, day: int, hour: float):
    if not -90 <= lat_deg <= 90 or not 1 <= day <= 366 or not 0 <= hour <= 24:
        return {"error": "lat_deg -90..90, day 1..366, hour 0..24 required"}
    return {"ghi_wm2": ghi_clear_sky(lat_deg, day, hour)}

@app.post("/yield")
def yld(b: YieldReq):
    return {
        "daily_kwh": daily_yield_kwh(b.lat_deg, b.day, b.area_m2, b.eff, b.tilt_deg, b.ambient_c),
        "daily_ghi_whm2": daily_ghi(b.lat_deg, b.day),
    }

from .lifetime import lifetime_kwh
from .carbon import co2_avoided_tonnes
from .tariffs import tariff_for


class LifetimeReq(BaseModel):
    annual_kwh: float = Field(gt=0, le=1000000)
    years: int = Field(ge=1, le=30)


class BatchReq(BaseModel):
    sites: list[YieldReq]

@app.post("/batch_yield")
def batch(b: BatchReq):
    return {"results": [{"daily_kwh": daily_yield_kwh(s.lat_deg, s.day, s.area_m2, s.eff, s.tilt_deg, s.ambient_c)} for s in b.sites]}

@app.post("/optimize")
def opt(b: OptimizeReq):
    o = optimize_tilt(b.lat_deg, b.day, b.area_m2)
    a = annual_yield_kwh(b.lat_deg, b.area_m2, tilt_deg=o["best_tilt_deg"])
    kw = round(b.area_m2 * 0.20 / 1.0, 3)
    capex = system_cost_inr(max(kw, 0.1))
    sav = annual_savings_inr(a["annual_kwh"])
    return {
        "best_tilt_deg": o["best_tilt_deg"],
        "best_daily_kwh": o["best_daily_kwh"],
        "annual_kwh": a["annual_kwh"],
        "capex_inr": capex,
        "lcoe_inr_per_kwh": lcoe_inr_per_kwh(capex, a["annual_kwh"]),
        "payback_years": payback_years(capex, sav),
    }


@app.post("/lifetime")
def lifetime(b: LifetimeReq):
    e = lifetime_kwh(b.annual_kwh, b.years)
    return {"lifetime_kwh": e["lifetime_kwh"], "co2_tonnes": co2_avoided_tonnes(b.annual_kwh, b.years)}
