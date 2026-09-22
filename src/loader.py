"""CSV loader for data/sample_rooftops.csv."""
from __future__ import annotations
import csv, pathlib
def load_rooftops(path: str = "data/sample_rooftops.csv") -> list[dict]:
    p = pathlib.Path(path)
    if not p.exists():
        raise FileNotFoundError(f"missing {path}")
    rows = []
    with p.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            rows.append({"id": r["id"], "lat_deg": float(r["lat_deg"]), "area_m2": float(r["area_m2"]), "tilt_deg": float(r["tilt_deg"])})
    if not rows:
        raise ValueError("empty rooftop file")
    return rows
