from src.om import cleans_per_year, annual_om_inr
import pytest
def test_cleans():
    assert cleans_per_year(20) == 12
    assert cleans_per_year(100) == 36
def test_cost():
    assert annual_om_inr(8) == 4400.0
def test_bad():
    import pytest as _p
    with _p.raises(ValueError):
        cleans_per_year(-1)
