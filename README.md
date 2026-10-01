# 🚗 Indian Automotive Specification & Performance Intelligence Platform

[![Live Tableau Dashboard](https://img.shields.io/badge/Tableau%20Public-Live%20Dashboard-E9762B?style=for-the-badge&logo=tableau&logoColor=white)](https://public.tableau.com/app/profile/shivaling.battarki/viz/VehicleSpecificationInteractiveDashboard/INTERACTIVESPECSDETAILS?publish=yes)
[![Live Web Portal](https://img.shields.io/badge/Live%20Showroom-GitHub%20Pages-0284c7?style=for-the-badge&logo=github&logoColor=white)](https://hazardous9hub.github.io/Indian-Automotive-Specification-Intelligence-Portal/)
[![Dataset](https://img.shields.io/badge/Dataset-10%2C000%20Calibrated%20Rows-10b981?style=for-the-badge&logo=databricks&logoColor=white)](data/vehicle_specification_dataset_10000_rows.csv)
[![Competition](https://img.shields.io/badge/Unstop-Tableau%20Competition%202026-6366f1?style=for-the-badge)]([https://unstop.com](https://unstop.com/competitions/tableau-data-visualization-challenge-2026-national-institute-of-engineering-nie-mysuru-1753895))
[![License](https://img.shields.io/badge/License-MIT-gray?style=for-the-badge)](LICENSE)

An enterprise-grade automotive intelligence platform submitted to the **Unstop Tableau Competition (September 2026)**. Built to bridge macro-statistical market analytics with vehicle-level engineering telemetry across **10,000 Indian automotive records** and **30 benchmark models across 16 leading OEMs**.

---

## 🔗 Quick Links

- 📊 **Tableau Public Dashboard**: [Interactive Automotive Intelligence Dashboard](https://public.tableau.com/app/profile/shivaling.battarki/viz/VehicleSpecificationInteractiveDashboard/INTERACTIVESPECSDETAILS?publish=yes)
- 🌐 **Live Web Intelligence Portal**: [Interactive Digital Showroom & Radar Telemetry](https://hazardous9hub.github.io/Indian-Automotive-Specification-Intelligence-Portal/)
- 📄 **Official Submission PDF**: [S.P.B Data Team Documentation (PDF)](docs/S.P.B_DATA_TEAM_Automotive_Intelligence_Platform_Documentation.pdf)
- 📝 **Editable Documentation**: [Microsoft Word Document (DOCX)](docs/Automotive_Intelligence_Platform_Documentation.docx) | [Markdown Dossier (MD)](docs/Automotive_Intelligence_Platform_Documentation.md)
- 📦 **Master Tableau Packaged Workbook**: [Download .twbx (2.4 MB)](tableau/Vehicle_Specification_Master_Dashboard.twbx)

---

## 🌟 Executive Summary & Dual-Engine Architecture

The platform addresses a critical gap in automotive analytics: consumer portals offer fragmented tables with zero cross-segment intelligence, while traditional BI dashboards show static charts detached from the vehicle's visual identity. 

This platform connects two synchronized systems:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                     TABLEAU ANALYTICAL INTELLIGENCE ENGINE                      │
│   • 10,000 Calibrated Indian Automotive Records (₹0.8L to ₹58L)                 │
│   • Macro KPI Banner • Price vs. Performance Scatter • Category Benchmark       │
│   • Safety Matrix (NCAP vs Airbags) • Dedicated Electric Vehicle (EV) Profiler  │
│   • Standalone Head-to-Head 2-Model Comparator Dashboard                        │
└────────────────────────────────────────┬────────────────────────────────────────┘
                                         │  Bi-directional URL Action Parameters
                                         │  (?model=Nexon&brand=Tata&fuel=Petrol)
                                         ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    EMBEDDED DIGITAL SHOWROOM & WEB TELEMETRY                    │
│   • Dual-View Studio Showcase: 30-Model Fleet Mosaic & Isolated Vehicle Pedestal│
│   • Real-Time 6-Axis Canvas Performance Radar (Active vs Category Benchmark)    │
│   • Instant Specification Conflict Detection & Auto-Resolution Engine           │
│   • Monotonic Executive Slate Theme (#111827) & High-Contrast Highlight Cards   │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 📊 Tableau Dashboard Suite

### Dashboard 1: Master Specification & Market Intelligence Cockpit
1. **Executive KPI Ribbon**: Instant macro metrics (30 OEM Models, Segment Median Ex-Showroom Price, Average Powertrain Output in HP, Bharat/Global NCAP 5-Star Compliance Rate).
2. **Price vs. Performance Market Positioning (Scatter Plot)**: 
   - X-Axis: Acquisition Price (₹0L to ₹65L) | Y-Axis: Horsepower Output (0 to 400 HP).
   - Color-coded by Powertrain: 🟢 Electric (EV), 🟡 Petrol, 🔵 Diesel. Sized by NCAP Safety Rating.
   - Clean, high-density text hover tooltip with zero lag.
3. **Category Benchmark Matrix**: Horizontal comparative analytics evaluating engine torque (Nm) and certified fuel economy (kmpl) across body silhouettes.
4. **Safety & Occupant Protection Matrix**: Heatmap cross-referencing NCAP stars against standard airbag distributions across budget tiers.
5. **Electric Vehicle (EV) Profiler**: Dedicated EV analysis isolated from ICE cross-filters, comparing battery pack sizes (kWh) against real-world certified ARAI range.
6. **Embedded Interactive Portal Object**: Seamlessly updates the showroom pedestal and 6-axis radar charts via URL actions.

### Dashboard 2: Standalone Head-to-Head 2-Model Comparator
An offline, self-contained comparative tool that operates independently of the web container:
- **Synchronized Model Parameters**: `[Select Model A]` and `[Select Model B]` dynamically populated from all 30 vehicles.
- **Hero Vehicle Visual Cards**: Displays authentic vehicle shape cutouts from the `Indian_Vehicles` repository palette with ex-showroom price badges.
- **Head-to-Head Specification Matrix**: Side-by-side tabular comparison across 8 core dimensions: Price, HP, Torque, Efficiency, Safety Rating, Airbags, Boot Capacity, and Ground Clearance.
- **Performance Advantage Delta Bar**: Visual diverging bar chart displaying which vehicle leads in Power, Torque, and Cargo volume.

---

## 🌐 Web Intelligence Portal Highlights

- **Dual-View Showcase Pedestal**:
  - **30-Model Mosaic Grid**: View all 30 benchmark vehicles in a compact miniature gallery with fuel color coding.
  - **Focused Single-Vehicle Stage**: Smooth GSAP animated transition displaying isolated vehicle cutouts on a studio pedestal with calibrated scaling (`VEHICLE_ZOOM_SCALES`).
- **6-Axis HTML5 Canvas Performance Radar**: Custom canvas engine rendering Price-Value, Horsepower, Range/Efficiency, Safety Stars, and Spatial Utility (Seats + Boot volume) with dual-polygon benchmark comparisons.
- **Price vs. Horsepower Scatter Plot**: Interactive canvas scatter plot showing market positioning with the market fleet median callout.
- **Specification Conflict Engine**: Real-time diagnostic engine that detects incompatible user filter combinations (e.g., selecting an Electric vehicle platform combined with Petrol fuel) and provides an instant 1-click Auto-Resolve button.
- **Zero-Framework Architecture**: Built using pure HTML5, vanilla JavaScript, and modern CSS3 Grid/Flexbox without heavy NPM frameworks, guaranteeing instant loading within Tableau's CEF browser container.
- **Executive Monotonic Slate Palette**: Calibrated palette (`#111827` base, `#182335` panels, `#283950` borders, `#38bdf8` steel blue accents, `#f8fafc` text) for high contrast, clean visibility, and zero eye strain.
- **Vertical Stacked Visualization**: Radar benchmark chart stacked directly above the scatter plot for clean, natural vertical scrolling inside Tableau.

---

## 📁 Repository Directory Structure

```
Indian-Automotive-Specification-Intelligence-Portal/
├── assets/                               # Optimized visual assets (<70 KB each)
│   ├── body_styles/                      # Body style silhouette icons
│   ├── drivetrains/                      # FWD, RWD, AWD technical badges
│   ├── logos/                            # 16 Official OEM vector logos
│   ├── powertrains/                      # Petrol, Diesel, EV, CNG icons
│   ├── transmissions/                    # Manual, Automatic, AMT, CVT badges
│   ├── vehicles/                         # Primary vehicle image cutouts
│   ├── vehicles_v2/                      # Tableau Image Role optimized PNGs (<70 KB)
│   └── gsap.min.js                       # GreenSock Animation Platform library
├── data/                                 # Calibrated Indian automotive datasets
│   ├── vehicle_specification_dataset_10000_rows.csv   # Master 10,000-record dataset
│   ├── vehicle_specification_dataset_10000_rows.xlsx  # Master Excel dataset
│   ├── vehicle_models_30_profiles.csv                 # 30 OEM Model benchmark profiles
│   ├── vehicle_image_urls_for_tableau.csv             # Tableau Image Role URL mapping
│   └── vehicle_image_urls_for_tableau.xlsx            # Tableau Image Role Excel mapping
├── docs/                                 # Complete documentation dossier
│   ├── S.P.B_DATA_TEAM_Automotive_Intelligence_Platform_Documentation.pdf # Submission PDF
│   ├── Automotive_Intelligence_Platform_Documentation.docx                 # Editable Word doc
│   └── Automotive_Intelligence_Platform_Documentation.md                  # Markdown doc
├── scripts/                              # Automated data engineering pipeline
│   ├── calibrate_entire_ecosystem.py     # 10,000-row domain calibration engine
│   ├── apply_tableau_theme.py            # Tableau color harmony & theme generator
│   ├── sync_index_html.py                # Portal & dataset synchronization script
│   ├── optimize_all_images.py            # PNG compression script (<70 KB limit)
│   └── create_docs.py                    # Automated Word document generator
├── tableau/                              # Tableau packaged workbooks
│   ├── Vehicle_Specification_Master_Dashboard.twbx    # Final submitted workbook (2.4 MB)
│   └── Vehicle_Specification_Master_Dashboard.twb     # Tableau XML workbook definition
├── index.html                            # Live interactive web portal (GitHub Pages root)
├── vehicle_visual_assets.csv             # Image metadata and asset manifest
└── README.md                             # Project overview & documentation
```

---

## 🛠️ Data Engineering & Domain Calibration

The starting raw synthetic dataset of 10,000 rows was systematically anchored to real-world Indian automotive specifications across **16 OEMs** and **30 models**:

| Brand | Model | Category | Fuel | Ex-Showroom (INR) | Power (HP) | Torque (Nm) | ARAI Efficiency | Safety (NCAP) | Boot (L) | Ground Clearance |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Tata** | Nexon EV | Electric SUV | Electric | ₹16,74,700 | 145 HP | 215 Nm | 465.7 km | 5.0 ★ | 350 L | 205 mm |
| **Hyundai** | Creta | Mid SUV | Petrol | ₹14,90,970 | 160 HP | 253 Nm | 18.2 kmpl | 4.5 ★ | 433 L | 190 mm |
| **Mahindra** | Scorpio N | Full SUV | Petrol | ₹18,59,890 | 203 HP | 380 Nm | 13.7 kmpl | 5.0 ★ | 460 L | 187 mm |
| **Tata** | Tiago | Hatchback | Petrol | ₹6,65,750 | 86 HP | 113 Nm | 20.0 kmpl | 4.0 ★ | 242 L | 170 mm |
| **Maruti Suzuki** | Swift | Hatchback | Petrol | ₹7,79,030 | 82 HP | 112 Nm | 25.7 kmpl | 4.0 ★ | 265 L | 163 mm |
| **Honda** | City | Sedan | Petrol | ₹13,81,260 | 121 HP | 145 Nm | 18.4 kmpl | 5.0 ★ | 506 L | 165 mm |
| **Volvo** | 9400 | Luxury Bus | Diesel | ₹57,78,210 | 380 HP | 1752 Nm | 4.5 kmpl | 5.0 ★ | 9500 L | 240 mm |
| **Ashok Leyland** | JanBus | City Bus | Diesel | ₹33,64,130 | 222 HP | 580 Nm | 4.8 kmpl | 4.0 ★ | 4500 L | 210 mm |
| **Isuzu** | D-Max | Pickup Truck | Diesel | ₹22,76,940 | 163 HP | 360 Nm | 14.5 kmpl | 4.5 ★ | 1200 L | 225 mm |
| **Honda** | Activa 6G | Scooter | Petrol | ₹82,870 | 7.8 HP | 8.9 Nm | 50.0 kmpl | 3.5 ★ | 18 L | 162 mm |

---

## 🧮 Key Tableau Formulas

```tableau
// 1. Model Comparator Filter Flag
[Model] = [Select Model A] OR [Model] = [Select Model B]

// 2. Dynamic Side-by-Side Column Slot
IF [Model] = [Select Model A] THEN "★ MODEL A: " + UPPER([Select Model A])
ELSEIF [Model] = [Select Model B] THEN "★ MODEL B: " + UPPER([Select Model B])
END

// 3. Safety Stars Formatter
IF [Safety Rating] >= 5.0 THEN "★★★★★ (5.0)"
ELSEIF [Safety Rating] >= 4.5 THEN "★★★★½ (4.5)"
ELSEIF [Safety Rating] >= 4.0 THEN "★★★★☆ (4.0)"
ELSEIF [Safety Rating] >= 3.0 THEN "★★★☆☆ (3.0)"
ELSE "★★☆☆☆ (" + STR(ROUND([Safety Rating], 1)) + ")"
END

// 4. Dynamic Interactive URL Generator
"https://hazardous9hub.github.io/Indian-Automotive-Specification-Intelligence-Portal/?model=" 
+ REPLACE([Model], " ", "%20")
+ "&brand=" + REPLACE([Brand], " ", "%20")
+ "&category=" + REPLACE([Category], " ", "%20")
+ "&fuel=" + REPLACE([Fuel Type], " ", "%20")

// 5. HP per Lakh INR Value Index
ROUND([Horsepower Hp] / [Price in Lakhs (INR)], 2)

// 6. Reset Filters Button Text
"↺ Reset All Filters"
```

---

## 🏆 Authenticity & Competition Integrity Declaration

> **DECLARATION OF ORIGINALITY:**  
> This project, including all analytical modeling, domain dataset calibration, responsive web portal source code, custom canvas telemetry, and Tableau calculated fields, was **created 100% from scratch by the author and project team** for the Unstop Tableau Competition (September 2026). No third-party UI templates, commercial dashboard kits, or cloned web repositories were used.

---

## 👨‍💻 Author & Team Information

- **Authors**:
  1. Shivaling Battarki (shivalingb09@gmail.com)
  2. Pragatheswaran M (pragathes224@gmail.com)
  3. Basawaraj (kale.sbasawaraj@gmail.com)
- **Team**: S.P.B Data Team
- **Competition**: Unstop Tableau Competition (September 2026)
- **GitHub**: [@Hazardous9hub](https://github.com/Hazardous9hub)
