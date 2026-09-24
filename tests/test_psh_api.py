from fastapi.testclient import TestClient
from src.api import app
c = TestClient(app)
def test_psh():
    r = c.get("/psh", params={"lat_deg": 19.07, "day": 105})
    assert r.status_code == 200
    assert 3.0 < r.json()["psh_hours"] < 8.0
def test_psh_bad():
    r = c.get("/psh", params={"lat_deg": 999, "day": 105})
    assert "error" in r.json()
