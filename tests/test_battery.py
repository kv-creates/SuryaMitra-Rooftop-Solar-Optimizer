from src.battery import battery_kwh, backup_hours
import pytest
def test_size():
    assert battery_kwh(10) > 10
def test_backup():
    assert backup_hours(10, 2) == 4.5
def test_invalid():
    with pytest.raises(ValueError):
        battery_kwh(-1)
