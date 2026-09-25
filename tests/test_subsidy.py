from src.subsidy import subsidy_inr, net_capex_inr
import pytest
def test_slabs():
    assert subsidy_inr(1) == 30000.0
    assert subsidy_inr(2) == 60000.0
    assert subsidy_inr(3) == 78000.0
def test_net():
    assert net_capex_inr(440000, 8) == 362000.0
def test_bad():
    import pytest as _p
    with _p.raises(ValueError):
        subsidy_inr(0)
