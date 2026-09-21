# Architecture
TMY -> Irradiance (`src/irradiance.py`) -> Shading (`src/shading.py`) -> PV (`src/pv.py`) -> Optimizer (`src/optimizer.py`) -> Finance (`src/finance.py`) -> API (`src/api.py`).
All modules are pure functions except API. No network calls. Deterministic synthetic weather via seeded RNG.
