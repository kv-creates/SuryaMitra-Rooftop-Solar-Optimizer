from fastapi.testclient import TestClient
from src.api import app
c = TestClient(app)
def test_health():
    assert c.get("/health").json()["status"] == "ok"
def test_yield():
    r = c.post("/yield", json={"lat_deg": 19.07, "day": 105, "area_m2": 40, "eff": 0.2, "tilt_deg": 15, "ambient_c": 30})
    assert r.status_code == 200
    assert r.json()["daily_kwh"] > 0
def test_optimize():
    r = c.post("/optimize", json={"lat_deg": 19.07, "day": 105, "area_m2": 40})
    assert r.status_code == 200
    assert "payback_years" in r.json()
def test_ghi_validation():
    r = c.get("/ghi", params={"lat_deg": 999, "day": 105, "hour": 12})
    assert "error" in r.json()
