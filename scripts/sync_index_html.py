import re
import json
import pandas as pd

prof_df = pd.read_csv("vehicle_models_30_profiles.csv").set_index("model")

with open("3d_viewer/index.html", "r", encoding="utf-8") as f:
    content = f.read()

m = re.search(r"(const\s+MASTER_VEHICLES\s*=\s*)(\[\s*\{.*?\}\s*\]);", content, re.DOTALL)
if not m:
    print("Could not find MASTER_VEHICLES")
    exit(1)

vehicles = json.loads(m.group(2))
print(f"Loaded {len(vehicles)} vehicles from index.html")

for v in vehicles:
    m_name = v["model"]
    if m_name in prof_df.index:
        p = prof_df.loc[m_name]
        v["brand"] = p["brand"]
        v["category"] = p["vehicle_category"]
        v["fuel"] = p["fuel_type"]
        v["price_inr"] = int(p["price_inr"])
        v["price"] = round(p["price_inr"] / 100000.0, 2)
        v["hp"] = float(p["horsepower_hp"]) if p["vehicle_category"] in ["Scooter", "Motorcycle"] else int(round(p["horsepower_hp"]))
        v["torque"] = float(p["torque_nm"]) if p["vehicle_category"] in ["Scooter", "Motorcycle"] else int(round(p["torque_nm"]))
        v["eff"] = float(p["ev_range_km"]) if p["fuel_type"] == "Electric" else float(p["mileage_kmpl"])
        v["safety"] = float(p["safety_rating"])
        v["bags"] = int(round(p["airbags"]))
        v["seats"] = int(p["seating_capacity"])
        v["ground_clearance"] = int(round(p["ground_clearance_mm"]))
        v["boot_space"] = int(p["boot_space_liters"])
        v["top_speed"] = int(round(p["top_speed_kmph"]))
        v["accel"] = float(p["acceleration_0_100_sec"])

new_json = json.dumps(vehicles, indent=2)
new_content = content[:m.start(2)] + new_json + content[m.end(2):]

with open("3d_viewer/index.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("SUCCESS: Synced 3d_viewer/index.html with authentic calibrated specifications!")
