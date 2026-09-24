from src.tilt_tables import recommended_tilt, tilt_table
import pytest
def test_mh():
    assert recommended_tilt("MH") == 19
def test_fallback():
    assert recommended_tilt("XX") == 18
def test_table():
    assert len(tilt_table()) == 8
def test_invalid():
    with pytest.raises(ValueError):
        recommended_tilt("")
