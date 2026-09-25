from src.diesel import diesel_saved_litres, diesel_saved_inr
import pytest
def test_litres():
    assert diesel_saved_litres(1000) == 280.0
def test_inr():
    assert diesel_saved_inr(1000) > 20000
def test_bad():
    import pytest as _p
    with _p.raises(ValueError):
        diesel_saved_litres(-1)
