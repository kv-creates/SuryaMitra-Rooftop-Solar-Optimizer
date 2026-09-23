from fastapi.testclient import TestClient
from src.api import app
c = TestClient(app)
def test_lifetime():
    r = c.post("/lifetime", json={"annual_kwh": 14000, "years": 25})
    assert r.status_code == 200
    assert r.json()["lifetime_kwh"] > 300000
    assert r.json()["co2_tonnes"] > 200
