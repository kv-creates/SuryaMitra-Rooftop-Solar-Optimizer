from src.lifetime import lifetime_kwh
import pytest
def test_lifetime_total():
    r = lifetime_kwh(14000)
    assert 300000 < r["lifetime_kwh"] < 14000*25
    assert len(r["yearly"]) == 25
    assert r["yearly"][0] > r["yearly"][-1]
def test_invalid():
    with pytest.raises(ValueError):
        lifetime_kwh(-5)
