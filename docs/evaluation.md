# Evaluation
- Mumbai 40 m2, 20 percent eff, tilt 15 deg: daily ~28-34 kWh day-105, annual ~9-11 MWh.
- Best tilt for lat 19 deg converges to 15-20 deg in grid search.
- LCOE INR 3-5 per kWh vs grid INR 8: payback 2-4 years typical.
- Edge cases: night GHI zero, zero area yields zero, invalid inputs raise ValueError or return error object.

- Inverter: 8 kW DC -> ~6.7 kW AC at 1.2 ratio, ~97 percent eff.
- Battery: 10 kWh night load -> ~12.1 kWh nameplate.
- PSH Mumbai ~5.5/day; monsoon-derated annual ~15 percent below clear-sky.
