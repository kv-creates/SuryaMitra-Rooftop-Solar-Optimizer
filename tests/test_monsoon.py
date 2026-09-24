from src.monsoon import cloud_for_month, derated_monthly
import pytest
def test_july_cloudy():
    assert cloud_for_month(7) > cloud_for_month(1)
def test_derate():
    m = [{"month": 7, "kwh": 1000}]
    assert derated_monthly(m)[0]["kwh"] < 1000
def test_invalid():
    with pytest.raises(ValueError):
        cloud_for_month(13)
