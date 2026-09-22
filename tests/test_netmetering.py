from src.finance import net_metering_credit
import pytest
def test_credit():
    assert net_metering_credit(2000, 5000) == 5000*8.0-2000*3.5
def test_floor_zero():
    assert net_metering_credit(20000, 1000) == 0.0
def test_invalid():
    with pytest.raises(ValueError):
        net_metering_credit(-1, 100)
