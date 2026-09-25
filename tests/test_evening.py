from src.evening import evening_peak_kw
import pytest
def test_peak():
    assert evening_peak_kw(20) > 0
def test_bad():
    import pytest as _p
    with _p.raises(ValueError):
        evening_peak_kw(-1)
