from src.irradiance import ghi_clear_sky, daily_ghi, cos_zenith
import pytest
def test_noon_positive():
    assert ghi_clear_sky(19.07, 105, 12.0) > 400
def test_night_zero():
    assert ghi_clear_sky(19.07, 105, 0.0) == 0.0
def test_daily_positive():
    assert daily_ghi(19.07, 105) > 3000
def test_invalid_day():
    with pytest.raises(ValueError):
        ghi_clear_sky(19.07, 400, 12.0)
