from src.tariffs import tariff_for, supported_states
import pytest
def test_known():
    assert tariff_for("MH") == 8.0
    assert tariff_for("dl") == 6.5
def test_fallback():
    assert tariff_for("XX") == 8.0
def test_states():
    assert "MH" in supported_states()
def test_invalid():
    with pytest.raises(ValueError):
        tariff_for("")
