from src.optimizer import optimize_azimuth
def test_azimuth_best():
    o = optimize_azimuth(19.07, 105, 40.0)
    assert o["best_azim_deg"] == 180
    assert len(o["table"]) == 5
    assert o["best_daily_kwh"] > 0
