from src.finance import lcoe_inr_per_kwh, payback_years, npv_inr
import pytest
def test_lcoe_range():
    v = lcoe_inr_per_kwh(110000, 6000)
    assert 1.0 < v < 12.0
def test_payback():
    assert 2 < payback_years(110000, 48000) < 10
def test_npv_positive():
    assert npv_inr(110000, 48000) > 0
def test_invalid():
    with pytest.raises(ValueError):
        payback_years(0, 100)
