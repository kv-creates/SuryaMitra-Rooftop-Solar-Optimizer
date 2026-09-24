from src.inverter import ac_yield_kwh
from src.battery import backup_hours
from src.psh import annual_psh
import pytest
def test_ac_zero():
    assert ac_yield_kwh(0) == 0.0
def test_backup_zero_batt():
    assert backup_hours(0, 2) == 0.0
def test_psh_high_lat():
    assert annual_psh(60.0) >= 0
def test_backup_bad_load():
    with pytest.raises(ValueError):
        backup_hours(10, 0)
