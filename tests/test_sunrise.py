from src.irradiance import sunrise_sunset
def test_mumbai_daylength():
    r = sunrise_sunset(19.07, 105)
    assert 11.0 < r["daylight_h"] < 14.0
    assert r["polar"] == "none"
def test_polar_night():
    r = sunrise_sunset(-75.0, 200)
    assert r["daylight_h"] in (0.0, 24.0)
