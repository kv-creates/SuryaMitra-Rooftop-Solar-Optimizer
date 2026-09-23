from src.carbon import co2_avoided_tonnes, trees_equivalent
import pytest
def test_co2():
    assert co2_avoided_tonnes(14000, 25) > 200
def test_trees():
    assert trees_equivalent(10) == 450.0
def test_invalid():
    with pytest.raises(ValueError):
        co2_avoided_tonnes(-1)
