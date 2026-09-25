from fastapi.testclient import TestClient
from src.api import app
c = TestClient(app)
def test_sub():
    r = c.get("/subsidy", params={"kw": 3})
    assert r.json()["subsidy_inr"] == 78000.0
def test_sub_bad():
    assert "error" in c.get("/subsidy", params={"kw": 0}).json()
