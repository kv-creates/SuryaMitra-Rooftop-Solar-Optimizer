from fastapi.testclient import TestClient
from src.api import app
c = TestClient(app)
def test_battery():
    r = c.get("/battery", params={"night_kwh": 10})
    assert r.status_code == 200
    assert r.json()["battery_kwh"] > 10
def test_battery_bad():
    r = c.get("/battery", params={"night_kwh": -5})
    assert "error" in r.json()
