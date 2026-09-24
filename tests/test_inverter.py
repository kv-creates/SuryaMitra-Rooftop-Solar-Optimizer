from src.inverter import clipping_loss, ac_yield_kwh, recommended_kw
import pytest
def test_no_clip():
    assert clipping_loss(1.0) == 0.0
def test_clip_positive():
    assert clipping_loss(1.4) > 0
def test_ac():
    assert 9000 < ac_yield_kwh(10000) < 10000
def test_size():
    assert recommended_kw(8.0) > 6.0
def test_invalid():
    with pytest.raises(ValueError):
        clipping_loss(2.0)
