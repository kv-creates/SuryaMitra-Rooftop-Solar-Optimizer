import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from src.finance import payback_years
quotes = [{"vendor": "A", "kw": 8.0, "capex": 440000, "annual_kwh": 14000}, {"vendor": "B", "kw": 8.0, "capex": 400000, "annual_kwh": 13200}]
lines = ["# Quote Comparison", "", "| Vendor | kW | Capex | kWh/yr | Payback |", "|---|---|---|---|---|"]
for q in quotes:
    pb = payback_years(q["capex"], q["annual_kwh"] * 8.0)
    lines.append("| %s | %s | %s | %s | %s |" % (q["vendor"], q["kw"], q["capex"], q["annual_kwh"], pb))
pathlib.Path("reports").mkdir(exist_ok=True)
pathlib.Path("reports/quotes.md").write_text("\n".join(lines) + "\n")
print("wrote quotes.md")
