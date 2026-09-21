from src.shading import horizon_loss, interrow_loss, soiling_loss, combined_factor
import pytest
def test_factors_range():
    for f in [horizon_loss(15), interrow_loss(15), soiling_loss(), combined_factor(15)]:
        assert 0.7 < f <= 1.0
def test_invalid_tilt():
    with pytest.raises(ValueError):
        horizon_loss(120)
def test_invalid_gcr():
    with pytest.raises(ValueError):
        interrow_loss(15, gcr=5.0)
