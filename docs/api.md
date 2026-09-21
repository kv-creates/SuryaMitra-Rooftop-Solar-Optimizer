# API
- GET /health -> status ok
- GET /ghi?lat_deg=19.07&day=105&hour=12 -> ghi_wm2, with validation error object on bad input
- POST /yield {lat_deg, day, area_m2, eff, tilt_deg, ambient_c} -> daily_kwh, daily_ghi_whm2
- POST /optimize {lat_deg, day, area_m2} -> best tilt, annual kWh, capex, LCOE, payback
Run: `uvicorn src.api:app --reload`
