from src.forecast import synthetic_day, tmy_annual_ghi
def test_day_len():
    d = synthetic_day(19.07, 105)
    assert len(d) == 24
    assert max(r["ghi"] for r in d) > 0
def test_night_low():
    d = synthetic_day(19.07, 105)
    assert d[0]["ghi"] == 0.0
def test_tmy():
    assert tmy_annual_ghi(19.07) > 1_000_000
