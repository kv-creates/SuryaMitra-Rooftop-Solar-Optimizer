from src.loader import load_rooftops
import pytest
def test_load():
    rows = load_rooftops()
    assert len(rows) == 5
    assert rows[0]["area_m2"] > 0
def test_missing():
    with pytest.raises(FileNotFoundError):
        load_rooftops("data/nope.csv")
