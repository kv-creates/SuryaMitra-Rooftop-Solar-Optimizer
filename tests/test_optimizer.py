from src.optimizer import optimize_tilt, annual_yield_kwh
import pytest
def test_best_tilt():
    o = optimize_tilt(19.07, 105, 40.0)
    assert o["best_daily_kwh"] > 0
    assert len(o["table"]) == 7
def test_annual():
    a = annual_yield_kwh(19.07, 40.0)
    assert a["annual_kwh"] > 5000
    assert len(a["monthly"]) == 12
def test_zero_area_invalid():
    with pytest.raises(ValueError):
        optimize_tilt(19.07, 105, 0.0)
