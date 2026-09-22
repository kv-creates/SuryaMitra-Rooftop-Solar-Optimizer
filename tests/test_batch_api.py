from fastapi.testclient import TestClient
from src.api import app
c = TestClient(app)
def test_batch():
    body = {"sites": [{"lat_deg": 19.07, "day": 105, "area_m2": 40, "eff": 0.2, "tilt_deg": 15, "ambient_c": 30}]}
    r = c.post("/batch_yield", json=body)
    assert r.status_code == 200
    assert r.json()["results"][0]["daily_kwh"] > 0
