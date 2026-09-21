from src.pv import dc_power_kw, daily_yield_kwh
from src.irradiance import ghi_clear_sky
from src.pv import cell_temperature
import pytest
def test_negative_ghi_rejected():
    with pytest.raises(ValueError):
        cell_temperature(30, -5)
def test_zero_area_power():
    assert dc_power_kw(800, 0.0, 0.2, 30, 15, 19.07) == 0.0
def test_polar_night():
    assert ghi_clear_sky(-75.0, 200, 0.0) == 0.0
def test_high_lat_daily_nonnegative():
    assert daily_yield_kwh(70.0, 15, 10.0) >= 0.0
def test_sample_results_exists():
    import json, pathlib
    d = json.loads(pathlib.Path("sample_results.json").read_text())
    assert d["annual_kwh"] > 5000
