from src.psh import peak_sun_hours, annual_psh
import pytest
def test_psh_range():
    assert 3.0 < peak_sun_hours(19.07, 105) < 8.0
def test_annual():
    assert 1500 < annual_psh(19.07) < 2500
def test_invalid():
    import pytest as _p
    with _p.raises(ValueError):
        peak_sun_hours(19.07, 105, cloud=2.0)
