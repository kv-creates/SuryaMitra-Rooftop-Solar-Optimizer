import json, pathlib
comp = json.loads(pathlib.Path("reports/comparison.json").read_text())
lines = ["# Site Comparison", "", "| Site | Annual kWh |", "|---|---|"] + [f"| {c['id']} | {c['annual_kwh']} |" for c in comp]
pathlib.Path("reports/comparison.md").write_text("\n".join(lines) + "\n")
print("wrote comparison.md")
