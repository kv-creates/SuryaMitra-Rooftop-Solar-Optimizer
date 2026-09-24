# Operations
- Python 3.11+. `pip install -r requirements.txt`
- `python scripts/generate_visuals.py` regenerates docs/images/*.png
- `pytest -q` runs 30+ tests
- `python -m src.main` runs Mumbai demo
- Docker: `docker build -t suryamitra .` then run port 8000.

Note: commits use verified author email so they count toward GitHub contributions.


- `python scripts/compare_sites.py` ranks rooftops; `python scripts/export_monthly_csv.py` writes monthly CSV.
- `python scripts/summary_html.py` builds a one-page HTML summary in reports/.
