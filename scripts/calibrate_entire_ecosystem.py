import re
import json
import numpy as np
import pandas as pd
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Authentic ground-truth specs for each of the 30 models
MODEL_SPECS = {
    # 2-WHEELERS: SCOOTERS (Price: ~80k-95k, 8-9 HP, 9-10 Nm, 48-52 kmpl, 0 bags, 2 seats, 0 boot or underseat 18-22L)
    "Activa": {
        "brand": "Honda", "category": "Scooter", "fuel": "Petrol",
        "engine_cc": 110, "hp": 7.8, "torque": 8.9, "mileage": 50.0, "ev_range": 0,
        "tank": 5.3, "transmissions": ["CVT", "Automatic"], "drivetrain": "RWD",
        "seats": 2, "weight": 106, "clearance": 162, "boot": 18, "top_speed": 85, "accel": 16.5,
        "price_base": 78000, "price_top": 89000, "airbags": 0, "safety": 3.5
    },
    "Jupiter": {
        "brand": "TVS", "category": "Scooter", "fuel": "Petrol",
        "engine_cc": 113, "hp": 7.9, "torque": 8.8, "mileage": 51.5, "ev_range": 0,
        "tank": 6.0, "transmissions": ["CVT", "Automatic"], "drivetrain": "RWD",
        "seats": 2, "weight": 107, "clearance": 163, "boot": 21, "top_speed": 85, "accel": 16.8,
        "price_base": 76000, "price_top": 88000, "airbags": 0, "safety": 3.5
    },
    "Access 125": {
        "brand": "Suzuki", "category": "Scooter", "fuel": "Petrol",
        "engine_cc": 124, "hp": 8.7, "torque": 10.0, "mileage": 48.0, "ev_range": 0,
        "tank": 5.0, "transmissions": ["CVT", "Automatic"], "drivetrain": "RWD",
        "seats": 2, "weight": 104, "clearance": 160, "boot": 22, "top_speed": 92, "accel": 15.2,
        "price_base": 82000, "price_top": 94000, "airbags": 0, "safety": 4.0
    },

    # 2-WHEELERS: MOTORCYCLES (Price: ~80k-1.7L, 8-24 HP, 9-21 Nm, 42-66 kmpl, 0 bags, 2 seats)
    "Splendor": {
        "brand": "Hero", "category": "Motorcycle", "fuel": "Petrol",
        "engine_cc": 97, "hp": 8.0, "torque": 8.1, "mileage": 65.5, "ev_range": 0,
        "tank": 9.8, "transmissions": ["Manual"], "drivetrain": "RWD",
        "seats": 2, "weight": 112, "clearance": 165, "boot": 0, "top_speed": 87, "accel": 18.0,
        "price_base": 74000, "price_top": 84000, "airbags": 0, "safety": 3.5
    },
    "Pulsar": {
        "brand": "Bajaj", "category": "Motorcycle", "fuel": "Petrol",
        "engine_cc": 249, "hp": 24.1, "torque": 21.5, "mileage": 43.8, "ev_range": 0,
        "tank": 14.0, "transmissions": ["Manual"], "drivetrain": "RWD",
        "seats": 2, "weight": 164, "clearance": 165, "boot": 0, "top_speed": 138, "accel": 9.5,
        "price_base": 138000, "price_top": 158000, "airbags": 0, "safety": 4.0
    },
    "Apache": {
        "brand": "TVS", "category": "Motorcycle", "fuel": "Petrol",
        "engine_cc": 198, "hp": 20.8, "torque": 17.2, "mileage": 42.0, "ev_range": 0,
        "tank": 12.0, "transmissions": ["Manual"], "drivetrain": "RWD",
        "seats": 2, "weight": 153, "clearance": 180, "boot": 0, "top_speed": 128, "accel": 10.2,
        "price_base": 125000, "price_top": 145000, "airbags": 0, "safety": 4.0
    },

    # HATCHBACKS (Price: ~5.6L - 11.2L, 82-120 HP, 113-172 Nm, 20-25 kmpl, 2-6 bags, 5 seats)
    "Tiago": {
        "brand": "Tata", "category": "Hatchback", "fuel": "Petrol",
        "engine_cc": 1199, "hp": 86.0, "torque": 113.0, "mileage": 20.0, "ev_range": 0,
        "tank": 35.0, "transmissions": ["Manual", "AMT"], "drivetrain": "FWD",
        "seats": 5, "weight": 982, "clearance": 170, "boot": 242, "top_speed": 150, "accel": 14.3,
        "price_base": 560000, "price_top": 810000, "airbags": [2, 4], "safety": 4.0
    },
    "Swift": {
        "brand": "Maruti Suzuki", "category": "Hatchback", "fuel": "Petrol",
        "engine_cc": 1197, "hp": 82.0, "torque": 112.0, "mileage": 25.7, "ev_range": 0,
        "tank": 37.0, "transmissions": ["Manual", "AMT"], "drivetrain": "FWD",
        "seats": 5, "weight": 920, "clearance": 163, "boot": 265, "top_speed": 165, "accel": 12.5,
        "price_base": 649000, "price_top": 960000, "airbags": [6], "safety": 4.0
    },
    "i20": {
        "brand": "Hyundai", "category": "Hatchback", "fuel": "Petrol",
        "engine_cc": 998, "hp": 120.0, "torque": 172.0, "mileage": 20.0, "ev_range": 0,
        "tank": 37.0, "transmissions": ["Manual", "Automatic", "CVT"], "drivetrain": "FWD",
        "seats": 5, "weight": 1040, "clearance": 170, "boot": 311, "top_speed": 175, "accel": 10.2,
        "price_base": 704000, "price_top": 1120000, "airbags": [6], "safety": 4.0
    },

    # SEDANS (Price: ~9.5L - 17.4L, 105-160 HP, 138-253 Nm, 18-21 kmpl, 4-6 bags, 5 seats)
    "Ciaz": {
        "brand": "Maruti Suzuki", "category": "Sedan", "fuel": "Petrol",
        "engine_cc": 1462, "hp": 105.0, "torque": 138.0, "mileage": 20.6, "ev_range": 0,
        "tank": 43.0, "transmissions": ["Manual", "Automatic"], "drivetrain": "FWD",
        "seats": 5, "weight": 1060, "clearance": 170, "boot": 510, "top_speed": 175, "accel": 11.5,
        "price_base": 940000, "price_top": 1230000, "airbags": [2, 4], "safety": 4.0
    },
    "City": {
        "brand": "Honda", "category": "Sedan", "fuel": "Petrol",
        "engine_cc": 1498, "hp": 121.0, "torque": 145.0, "mileage": 18.4, "ev_range": 0,
        "tank": 40.0, "transmissions": ["Manual", "CVT"], "drivetrain": "FWD",
        "seats": 5, "weight": 1125, "clearance": 165, "boot": 506, "top_speed": 185, "accel": 10.4,
        "price_base": 1180000, "price_top": 1630000, "airbags": [4, 6], "safety": 5.0
    },
    "Verna": {
        "brand": "Hyundai", "category": "Sedan", "fuel": "Petrol",
        "engine_cc": 1482, "hp": 160.0, "torque": 253.0, "mileage": 20.6, "ev_range": 0,
        "tank": 45.0, "transmissions": ["Manual", "Automatic", "CVT"], "drivetrain": "FWD",
        "seats": 5, "weight": 1210, "clearance": 170, "boot": 528, "top_speed": 210, "accel": 8.1,
        "price_base": 1100000, "price_top": 1740000, "airbags": [6], "safety": 5.0
    },

    # SUVS (Price: ~8.2L - 24.5L, 120-203 HP, 170-380 Nm, 13-18 kmpl, 6 bags, 5-7 seats)
    "Nexon": {
        "brand": "Tata", "category": "SUV", "fuel": "Petrol",
        "engine_cc": 1199, "hp": 120.0, "torque": 170.0, "mileage": 17.4, "ev_range": 0,
        "tank": 44.0, "transmissions": ["Manual", "AMT", "Automatic"], "drivetrain": "FWD",
        "seats": 5, "weight": 1255, "clearance": 208, "boot": 382, "top_speed": 180, "accel": 11.2,
        "price_base": 815000, "price_top": 1580000, "airbags": [6], "safety": 5.0
    },
    "Creta": {
        "brand": "Hyundai", "category": "SUV", "fuel": "Petrol",
        "engine_cc": 1482, "hp": 160.0, "torque": 253.0, "mileage": 18.2, "ev_range": 0,
        "tank": 50.0, "transmissions": ["Manual", "Automatic", "CVT"], "drivetrain": "FWD",
        "seats": 5, "weight": 1330, "clearance": 190, "boot": 433, "top_speed": 190, "accel": 8.9,
        "price_base": 1100000, "price_top": 2015000, "airbags": [6], "safety": 4.5
    },
    "Scorpio N": {
        "brand": "Mahindra", "category": "SUV", "fuel": "Petrol",
        "engine_cc": 1997, "hp": 203.0, "torque": 380.0, "mileage": 13.7, "ev_range": 0,
        "tank": 57.0, "transmissions": ["Manual", "Automatic"], "drivetrain": "RWD",
        "seats": 7, "weight": 2060, "clearance": 187, "boot": 460, "top_speed": 175, "accel": 10.3,
        "price_base": 1385000, "price_top": 2454000, "airbags": [6], "safety": 5.0
    },

    # ELECTRIC VEHICLES (Price: ~14.5L - 25.8L, 145-177 HP, 215-310 Nm, 0 kmpl, 450-465 km range, 6 bags, 5 seats)
    "Nexon EV": {
        "brand": "Tata", "category": "Electric Vehicle", "fuel": "Electric",
        "engine_cc": 0, "hp": 145.0, "torque": 215.0, "mileage": 0.0, "ev_range": 465.0,
        "tank": 0.0, "transmissions": ["Automatic"], "drivetrain": "FWD",
        "seats": 5, "weight": 1400, "clearance": 190, "boot": 350, "top_speed": 150, "accel": 8.9,
        "price_base": 1449000, "price_top": 1949000, "airbags": [6], "safety": 5.0
    },
    "XUV400": {
        "brand": "Mahindra", "category": "Electric Vehicle", "fuel": "Electric",
        "engine_cc": 0, "hp": 150.0, "torque": 310.0, "mileage": 0.0, "ev_range": 456.0,
        "tank": 0.0, "transmissions": ["Automatic"], "drivetrain": "FWD",
        "seats": 5, "weight": 1578, "clearance": 200, "boot": 378, "top_speed": 150, "accel": 8.3,
        "price_base": 1549000, "price_top": 1939000, "airbags": [6], "safety": 5.0
    },
    "ZS EV": {
        "brand": "MG", "category": "Electric Vehicle", "fuel": "Electric",
        "engine_cc": 0, "hp": 177.0, "torque": 280.0, "mileage": 0.0, "ev_range": 461.0,
        "tank": 0.0, "transmissions": ["Automatic"], "drivetrain": "FWD",
        "seats": 5, "weight": 1620, "clearance": 177, "boot": 448, "top_speed": 175, "accel": 8.5,
        "price_base": 1898000, "price_top": 2580000, "airbags": [6], "safety": 5.0
    },

    # VANS (Price: ~5.3L - 26.5L, 81-150 HP, 104-360 Nm, 11-20 kmpl)
    "Eeco": {
        "brand": "Maruti Suzuki", "category": "Van", "fuel": "Diesel",
        "engine_cc": 1197, "hp": 81.0, "torque": 104.0, "mileage": 19.7, "ev_range": 0,
        "tank": 40.0, "transmissions": ["Manual"], "drivetrain": "RWD",
        "seats": 7, "weight": 1050, "clearance": 160, "boot": 540, "top_speed": 120, "accel": 15.7,
        "price_base": 532000, "price_top": 658000, "airbags": [2], "safety": 3.0
    },
    "Traveller": {
        "brand": "Force", "category": "Van", "fuel": "Diesel",
        "engine_cc": 2596, "hp": 115.0, "torque": 350.0, "mileage": 14.0, "ev_range": 0,
        "tank": 70.0, "transmissions": ["Manual"], "drivetrain": "RWD",
        "seats": 14, "weight": 2680, "clearance": 190, "boot": 1200, "top_speed": 110, "accel": 22.0,
        "price_base": 1450000, "price_top": 1980000, "airbags": [2], "safety": 3.5
    },
    "Innova": {
        "brand": "Toyota", "category": "Van", "fuel": "Diesel",
        "engine_cc": 2393, "hp": 150.0, "torque": 360.0, "mileage": 15.6, "ev_range": 0,
        "tank": 55.0, "transmissions": ["Manual", "Automatic"], "drivetrain": "RWD",
        "seats": 7, "weight": 1820, "clearance": 178, "boot": 300, "top_speed": 170, "accel": 12.8,
        "price_base": 1999000, "price_top": 2850000, "airbags": [7], "safety": 5.0
    },

    # PICKUP TRUCKS (Price: ~8.8L - 24.5L, 76-163 HP, 200-360 Nm, 14-15 kmpl)
    "Bolero Pickup": {
        "brand": "Mahindra", "category": "Pickup Truck", "fuel": "Diesel",
        "engine_cc": 2523, "hp": 76.0, "torque": 200.0, "mileage": 14.3, "ev_range": 0,
        "tank": 60.0, "transmissions": ["Manual"], "drivetrain": "RWD",
        "seats": 2, "weight": 1760, "clearance": 185, "boot": 1500, "top_speed": 115, "accel": 21.0,
        "price_base": 885000, "price_top": 1040000, "airbags": [1, 2], "safety": 3.0
    },
    "Yodha": {
        "brand": "Tata", "category": "Pickup Truck", "fuel": "Diesel",
        "engine_cc": 2200, "hp": 100.0, "torque": 250.0, "mileage": 14.8, "ev_range": 0,
        "tank": 52.0, "transmissions": ["Manual"], "drivetrain": "RWD",
        "seats": 2, "weight": 1850, "clearance": 210, "boot": 1700, "top_speed": 120, "accel": 19.5,
        "price_base": 920000, "price_top": 1075000, "airbags": [1, 2], "safety": 3.5
    },
    "D-Max": {
        "brand": "Isuzu", "category": "Pickup Truck", "fuel": "Diesel",
        "engine_cc": 1898, "hp": 163.0, "torque": 360.0, "mileage": 14.5, "ev_range": 0,
        "tank": 76.0, "transmissions": ["Manual", "Automatic"], "drivetrain": "AWD",
        "seats": 5, "weight": 1935, "clearance": 225, "boot": 1200, "top_speed": 160, "accel": 12.0,
        "price_base": 1950000, "price_top": 2700000, "airbags": [6], "safety": 4.5
    },

    # COMMERCIAL TRUCKS (Price: ~23.5L - 42.5L, 204-280 HP, 568-1100 Nm, 3.8-6.0 kmpl)
    "Boss": {
        "brand": "Ashok Leyland", "category": "Truck", "fuel": "Diesel",
        "engine_cc": 3839, "hp": 204.0, "torque": 613.0, "mileage": 5.8, "ev_range": 0,
        "tank": 208.0, "transmissions": ["Manual", "AMT"], "drivetrain": "RWD",
        "seats": 3, "weight": 7200, "clearance": 230, "boot": 0, "top_speed": 100, "accel": 26.0,
        "price_base": 2350000, "price_top": 3270000, "airbags": [1], "safety": 4.0
    },
    "Pro 3015": {
        "brand": "Eicher", "category": "Truck", "fuel": "Diesel",
        "engine_cc": 3760, "hp": 211.0, "torque": 568.0, "mileage": 6.2, "ev_range": 0,
        "tank": 190.0, "transmissions": ["Manual"], "drivetrain": "RWD",
        "seats": 3, "weight": 6800, "clearance": 230, "boot": 0, "top_speed": 90, "accel": 28.0,
        "price_base": 2500000, "price_top": 3240000, "airbags": [1], "safety": 4.0
    },
    "Prima": {
        "brand": "Tata", "category": "Truck", "fuel": "Diesel",
        "engine_cc": 6700, "hp": 280.0, "torque": 1100.0, "mileage": 3.8, "ev_range": 0,
        "tank": 300.0, "transmissions": ["Manual", "AMT"], "drivetrain": "RWD",
        "seats": 2, "weight": 11500, "clearance": 260, "boot": 0, "top_speed": 105, "accel": 29.0,
        "price_base": 3800000, "price_top": 4500000, "airbags": [2], "safety": 4.5
    },

    # COMMERCIAL BUSES (Price: ~28.5L - 58.0L, 140-380 HP, 400-1750 Nm, 4.5-12.0 kmpl)
    "Starbus": {
        "brand": "Tata", "category": "Bus", "fuel": "Diesel",
        "engine_cc": 3783, "hp": 140.0, "torque": 400.0, "mileage": 12.0, "ev_range": 0,
        "tank": 160.0, "transmissions": ["Manual", "Automatic"], "drivetrain": "RWD",
        "seats": 32, "weight": 5200, "clearance": 210, "boot": 2500, "top_speed": 95, "accel": 25.0,
        "price_base": 2600000, "price_top": 3100000, "airbags": [1], "safety": 4.0
    },
    "JanBus": {
        "brand": "Ashok Leyland", "category": "Bus", "fuel": "Diesel",
        "engine_cc": 5660, "hp": 222.0, "torque": 580.0, "mileage": 4.8, "ev_range": 0,
        "tank": 250.0, "transmissions": ["Manual", "Automatic"], "drivetrain": "RWD",
        "seats": 42, "weight": 9500, "clearance": 210, "boot": 4500, "top_speed": 90, "accel": 27.0,
        "price_base": 3200000, "price_top": 3600000, "airbags": [1], "safety": 4.0
    },
    "9400": {
        "brand": "Volvo", "category": "Bus", "fuel": "Diesel",
        "engine_cc": 10800, "hp": 380.0, "torque": 1750.0, "mileage": 4.5, "ev_range": 0,
        "tank": 400.0, "transmissions": ["Automatic"], "drivetrain": "RWD",
        "seats": 54, "weight": 14800, "clearance": 240, "boot": 9500, "top_speed": 110, "accel": 24.0,
        "price_base": 5500000, "price_top": 6200000, "airbags": [2], "safety": 5.0
    }
}

print(f"Loaded specifications for all {len(MODEL_SPECS)} models.")

# 1. Calibrate vehicle_specification_dataset_10000_rows.csv
np.random.seed(42)
df = pd.read_csv("vehicle_specification_dataset_10000_rows.csv")
print(f"Original dataset rows: {len(df)}")

new_rows = []
for idx, row in df.iterrows():
    m_name = row["model"].strip()
    spec = MODEL_SPECS.get(m_name)
    if not spec:
        raise ValueError(f"Unknown model: {m_name}")
    
    # Generate realistic variant tier: 0 = Base, 1 = Mid, 2 = Top
    tier = np.random.choice([0, 1, 2], p=[0.35, 0.45, 0.20])
    tier_ratio = 0.0 if tier == 0 else (0.5 if tier == 1 else 1.0)
    
    # Price
    p_spread = spec["price_top"] - spec["price_base"]
    noise_p = np.random.normal(0, 0.015) * spec["price_base"]
    price = int(spec["price_base"] + (p_spread * tier_ratio) + noise_p)
    price = max(price, int(spec["price_base"] * 0.95))
    
    # Transmission & Drivetrain
    trans = np.random.choice(spec["transmissions"])
    drive = spec["drivetrain"]
    
    # Horsepower & Torque (tiny engine tolerance +/- 1%)
    hp = round(spec["hp"] * (1 + np.random.normal(0, 0.01)), 1)
    if spec["category"] in ["Scooter", "Motorcycle"]:
        hp = round(hp, 1)
        torque = round(spec["torque"] * (1 + np.random.normal(0, 0.01)), 1)
    else:
        hp = int(round(hp))
        torque = int(round(spec["torque"] * (1 + np.random.normal(0, 0.01))))
        
    # Mileage & EV Range
    if spec["fuel"] == "Electric":
        mileage = 0.0
        ev_range = round(spec["ev_range"] * (1 + np.random.normal(0, 0.02)), 1)
        tank = 0
        engine_cc = 0
    else:
        mileage = round(spec["mileage"] * (1 + np.random.normal(0, 0.02)), 1)
        ev_range = 0
        tank = spec["tank"]
        engine_cc = spec["engine_cc"]
        
    # Airbags
    bags_val = spec.get("airbags", 0)
    if isinstance(bags_val, list):
        airbags = bags_val[min(tier, len(bags_val)-1)]
    else:
        airbags = int(bags_val)
        
    safety = spec["safety"]
    seats = spec["seats"]
    weight = int(spec["weight"] * (1 + np.random.normal(0, 0.01)))
    clearance = int(spec["clearance"] + np.random.choice([-2, 0, 2]))
    boot = spec["boot"]
    top_speed = int(spec["top_speed"] + np.random.choice([-3, 0, 3]))
    accel = round(spec["accel"] * (1 + np.random.normal(0, 0.02)), 1)
    
    new_rows.append({
        "vehicle_id": row["vehicle_id"],
        "brand": spec["brand"],
        "model": m_name,
        "vehicle_category": spec["category"],
        "fuel_type": spec["fuel"],
        "engine_cc": engine_cc,
        "horsepower_hp": hp,
        "torque_nm": torque,
        "mileage_kmpl": mileage,
        "fuel_tank_capacity_liters": tank,
        "ev_range_km": ev_range,
        "transmission": trans,
        "drivetrain": drive,
        "seating_capacity": seats,
        "vehicle_weight_kg": weight,
        "ground_clearance_mm": clearance,
        "boot_space_liters": boot,
        "top_speed_kmph": top_speed,
        "acceleration_0_100_sec": accel,
        "price_inr": price,
        "airbags": airbags,
        "safety_rating": safety
    })

calibrated_df = pd.DataFrame(new_rows)
calibrated_df.to_csv("vehicle_specification_dataset_10000_rows.csv", index=False)
print("SUCCESS: Calibrated vehicle_specification_dataset_10000_rows.csv (10,000 rows)")

# 2. Build vehicle_models_30_profiles.csv & vehicle_models_30_scored.csv
profile_rows = []
for m_name, spec in MODEL_SPECS.items():
    m_df = calibrated_df[calibrated_df["model"] == m_name]
    profile_rows.append({
        "brand": spec["brand"],
        "model": m_name,
        "vehicle_category": spec["category"],
        "fuel_type": spec["fuel"],
        "transmission": m_df["transmission"].mode()[0],
        "drivetrain": spec["drivetrain"],
        "price_inr": round(m_df["price_inr"].mean(), 1),
        "horsepower_hp": round(m_df["horsepower_hp"].mean(), 1),
        "torque_nm": round(m_df["torque_nm"].mean(), 1),
        "mileage_kmpl": round(m_df["mileage_kmpl"].mean(), 2),
        "ev_range_km": round(m_df["ev_range_km"].mean(), 1),
        "engine_cc": spec["engine_cc"],
        "fuel_tank_capacity_liters": spec["tank"],
        "seating_capacity": spec["seats"],
        "vehicle_weight_kg": round(m_df["vehicle_weight_kg"].mean(), 1),
        "ground_clearance_mm": round(m_df["ground_clearance_mm"].mean(), 1),
        "boot_space_liters": spec["boot"],
        "top_speed_kmph": round(m_df["top_speed_kmph"].mean(), 1),
        "acceleration_0_100_sec": round(m_df["acceleration_0_100_sec"].mean(), 2),
        "airbags": round(m_df["airbags"].mean(), 1),
        "safety_rating": spec["safety"],
        "sample_count": len(m_df)
    })

prof_df = pd.DataFrame(profile_rows).sort_values(by=["vehicle_category", "price_inr"])
prof_df.to_csv("vehicle_models_30_profiles.csv", index=False)
print("SUCCESS: Generated vehicle_models_30_profiles.csv")

# 3. Build updated visual assets CSV
base_url = "https://hazardous9hub.github.io/Indian-Automotive-Specification-Intelligence-Portal"
v_clean_map = {
    "Boss": "ashok_leyland_boss", "JanBus": "ashok_leyland_janbus", "Pulsar": "bajaj_pulsar",
    "Pro 3015": "eicher_pro_3015", "Traveller": "force_traveller", "Splendor": "hero_splendor",
    "Activa": "honda_activa", "City": "honda_city", "Creta": "hyundai_creta",
    "Verna": "hyundai_verna", "i20": "hyundai_i20", "D-Max": "isuzu_d-max",
    "ZS EV": "mg_zs_ev", "Bolero Pickup": "mahindra_bolero_pickup", "Scorpio N": "mahindra_scorpio_n",
    "XUV400": "mahindra_xuv400", "Ciaz": "maruti_suzuki_ciaz", "Eeco": "maruti_suzuki_eeco",
    "Swift": "maruti_suzuki_swift", "Access 125": "suzuki_access_125", "Apache": "tvs_apache",
    "Jupiter": "tvs_jupiter", "Nexon": "tata_nexon", "Nexon EV": "tata_nexon_ev",
    "Prima": "tata_prima", "Starbus": "tata_starbus", "Tiago": "tata_tiago",
    "Yodha": "tata_yodha", "Innova": "toyota_innova", "9400": "volvo_9400"
}

logo_clean_map = {
    "Ashok Leyland": "ashok_leyland.svg", "Bajaj": "bajaj.svg", "Eicher": "eicher.svg",
    "Force": "force.svg", "Hero": "hero.svg", "Honda": "honda.svg", "Hyundai": "hyundai.svg",
    "Isuzu": "isuzu.svg", "MG": "mg.svg", "Mahindra": "mahindra.svg", "Maruti Suzuki": "maruti_suzuki.svg",
    "Suzuki": "suzuki.svg", "TVS": "tvs.svg", "Tata": "tata.svg", "Toyota": "toyota.svg", "Volvo": "volvo.svg"
}

archetype_map = {
    "Scooter": "car", "Motorcycle": "car", "Hatchback": "car", "Sedan": "car",
    "SUV": "suv", "Electric Vehicle": "car", "Van": "truck", "Pickup Truck": "truck",
    "Truck": "truck", "Bus": "truck"
}

visual_rows = []
tableau_url_rows = []

for _, r in prof_df.iterrows():
    m = r["model"]
    b = r["brand"]
    cat = r["vehicle_category"]
    fuel = r["fuel_type"]
    v_slug = v_clean_map[m]
    logo_file = logo_clean_map[b]
    
    png_url = f"{base_url}/assets/vehicles/{v_slug}.png"
    jpg_url = f"{base_url}/assets/vehicles/{v_slug}.jpg"
    logo_url = f"{base_url}/assets/logos/{logo_file}"
    cat_slug = cat.lower().replace(" ", "_") + ".svg"
    cat_url = f"{base_url}/assets/body_styles/{cat_slug}"
    portal_url = f"{base_url}/?brand={b.replace(' ', '+')}&model={m.replace(' ', '+')}&fuel={fuel}"
    
    visual_rows.append({
        "brand": b,
        "model": m,
        "vehicle_category": cat,
        "fuel_type": fuel,
        "transmission": r["transmission"],
        "drivetrain": r["drivetrain"],
        "price_inr": r["price_inr"],
        "horsepower_hp": r["horsepower_hp"],
        "torque_nm": r["torque_nm"],
        "mileage_kmpl": r["mileage_kmpl"],
        "ev_range_km": r["ev_range_km"],
        "safety_rating": r["safety_rating"],
        "airbags": r["airbags"],
        "brand_logo_file": f"assets/logos/{logo_file}",
        "vehicle_image_file": f"assets/vehicles/{v_slug}.png",
        "powertrain_icon_file": f"assets/powertrains/{fuel.lower()}.svg",
        "transmission_icon_file": f"assets/transmissions/{r['transmission'].lower()}.svg",
        "drivetrain_icon_file": f"assets/drivetrains/{r['drivetrain'].lower()}.svg",
        "model_3d_archetype": archetype_map[cat]
    })
    
    tableau_url_rows.append({
        "Brand": b,
        "Model": m,
        "Category": cat,
        "Fuel Type": fuel,
        "Avg Price (INR)": r["price_inr"],
        "Horsepower (HP)": r["horsepower_hp"],
        "Torque (Nm)": r["torque_nm"],
        "Efficiency (kmpl / km)": r["ev_range_km"] if fuel == "Electric" else r["mileage_kmpl"],
        "Safety Rating": r["safety_rating"],
        "Vehicle PNG URL (Tableau Image Role)": png_url,
        "Vehicle JPG URL": jpg_url,
        "Brand Logo URL": logo_url,
        "Category Icon URL": cat_url,
        "Interactive Portal URL": portal_url
    })

vis_df = pd.DataFrame(visual_rows)
vis_df.to_csv("vehicle_visual_assets_updated.csv", index=False)
vis_df.to_csv("3d_viewer/vehicle_visual_assets.csv", index=False)
print("SUCCESS: Updated vehicle_visual_assets_updated.csv and 3d_viewer/vehicle_visual_assets.csv")

tab_df = pd.DataFrame(tableau_url_rows)
tab_df.to_csv("vehicle_image_urls_for_tableau.csv", index=False)

# Build formatted Excel
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Vehicle URLs for Tableau"
headers = list(tab_df.columns)
ws.append(headers)

header_fill = PatternFill(start_color="1F4E79", end_color="1F4E79", fill_type="solid")
header_font = Font(name="Segoe UI", size=11, bold=True, color="FFFFFF")
header_border = Border(
    left=Side(style="thin", color="B0C4DE"), right=Side(style="thin", color="B0C4DE"),
    top=Side(style="medium", color="1F4E79"), bottom=Side(style="medium", color="1F4E79")
)

for col_num, header in enumerate(headers, 1):
    c = ws.cell(row=1, column=col_num)
    c.fill = header_fill
    c.font = header_font
    c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    c.border = header_border

link_font = Font(name="Segoe UI", size=10, color="0066CC", underline="single")
text_font = Font(name="Segoe UI", size=10)
bold_font = Font(name="Segoe UI", size=10, bold=True)
alt_fill = PatternFill(start_color="F4F8FC", end_color="F4F8FC", fill_type="solid")
white_fill = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")
thin_border = Border(
    left=Side(style="thin", color="E0E6ED"), right=Side(style="thin", color="E0E6ED"),
    top=Side(style="thin", color="E0E6ED"), bottom=Side(style="thin", color="E0E6ED")
)

for row_idx, row_data in enumerate(tab_df.values, 2):
    fill_to_use = alt_fill if (row_idx % 2 == 1) else white_fill
    for col_idx, val in enumerate(row_data, 1):
        c = ws.cell(row=row_idx, column=col_idx)
        c.value = val
        c.border = thin_border
        c.fill = fill_to_use
        
        if col_idx in [1, 2]:
            c.font = bold_font
            c.alignment = Alignment(horizontal="left", vertical="center")
        elif col_idx in [3, 4, 9]:
            c.font = text_font
            c.alignment = Alignment(horizontal="center", vertical="center")
        elif col_idx in [5, 6, 7, 8]:
            c.font = text_font
            c.alignment = Alignment(horizontal="right", vertical="center")
            if col_idx == 5:
                c.number_format = '"₹"#,##,##0'
        else:
            c.font = link_font
            c.hyperlink = str(val)
            c.alignment = Alignment(horizontal="left", vertical="center")

ws.row_dimensions[1].height = 28
for r in range(2, len(tab_df) + 2):
    ws.row_dimensions[r].height = 22

for col in ws.columns:
    max_len = max(len(str(cell.value or "")) for cell in col)
    col_letter = get_column_letter(col[0].column)
    ws.column_dimensions[col_letter].width = min(max(max_len + 3, 14), 58)

wb.save("vehicle_image_urls_for_tableau.xlsx")
print("SUCCESS: Updated vehicle_image_urls_for_tableau.xlsx")
