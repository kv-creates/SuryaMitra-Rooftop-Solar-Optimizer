from src.pv import dc_power_kw, daily_yield_kwh, cell_temperature
def test_night_zero():
    assert dc_power_kw(0, 40, 0.20, 30, 15, 19.07) == 0.0
def test_zero_area():
    assert daily_yield_kwh(19.07, 105, 0.0) == 0.0
def test_day_positive():
    assert daily_yield_kwh(19.07, 105, 40.0) > 5.0
def test_cell_temp():
    assert cell_temperature(30, 800) > 30
