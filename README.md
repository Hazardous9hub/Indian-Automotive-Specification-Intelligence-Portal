# 🚗 Indian Automotive Specification & Performance Intelligence Platform

> **Unstop Tableau & Data Visualization Challenge 2026**  
> Organized by **National Institute of Engineering (NIE), Mysuru** on [Unstop](https://unstop.com/competitions/tableau-data-visualization-challenge-2026-national-institute-of-engineering-nie-mysuru-1753895)  
> **Team Project Submission by S.P.B Data Team**

[![Live Tableau Dashboard](https://img.shields.io/badge/Tableau%20Public-Interactive%20Dashboard-E9762B?style=for-the-badge&logo=tableau&logoColor=white)](https://public.tableau.com/app/profile/shivaling.battarki/viz/VehicleSpecificationInteractiveDashboard/INTERACTIVESPECSDETAILS?publish=yes)
[![Live Web Portal](https://img.shields.io/badge/Live%20Portal-GitHub%20Pages-0284c7?style=for-the-badge&logo=github&logoColor=white)](https://hazardous9hub.github.io/Indian-Automotive-Specification-Intelligence-Portal/)
[![Dataset](https://img.shields.io/badge/Dataset-10%2C000%20Calibrated%20Rows-10b981?style=for-the-badge&logo=databricks&logoColor=white)](data/vehicle_specification_dataset_10000_rows.csv)
[![Competition](https://img.shields.io/badge/Unstop-Tableau%20Challenge%202026-6366f1?style=for-the-badge)](https://unstop.com/competitions/tableau-data-visualization-challenge-2026-national-institute-of-engineering-nie-mysuru-1753895)
[![License](https://img.shields.io/badge/License-MIT-gray?style=for-the-badge)](LICENSE)

---

## 👥 Project Team & Competition Details

| Member | GitHub | LinkedIn | Email |
| :--- | :---: | :---: | :--- |
| **Shivaling Battarki** | [@Hazardous9hub](https://github.com/Hazardous9hub) | [LinkedIn](https://www.linkedin.com/in/shivaling-93000/) | [Gmail]`shivalingb09@gmail.com` |
| **Pragatheswaran M** | [@Pragatheswaran-M](https://github.com/Pragatheswaran-M) | [LinkedIn](https://www.linkedin.com/in/pragatheswaranm/) | `pragathes224@gmail.com` |
| **Basawaraj Kale** | [@basawaraj849](https://github.com/basawaraj849) | [LinkedIn](https://www.linkedin.com/in/basawarajkale/) | `kale.sbasawaraj@gmail.com` |

| Competition Attribute | Details |
| :--- | :--- |
| **Event Name** | **Tableau & Data Visualization Challenge 2026** |
| **Organized By** | **National Institute of Engineering (NIE), Mysuru** via **Unstop** ([Competition Page](https://unstop.com/competitions/tableau-data-visualization-challenge-2026-national-institute-of-engineering-nie-mysuru-1753895)) |
| **Competition Track** | Automotive Specifications & Market Analytics |
| **Team Name** | **S.P.B Data Team** |
| **Primary Project Links** | • [Live Tableau Public Dashboard](https://public.tableau.com/app/profile/shivaling.battarki/viz/VehicleSpecificationInteractiveDashboard/INTERACTIVESPECSDETAILS?publish=yes)<br>• [Live Hosted Web Intelligence Portal](https://hazardous9hub.github.io/Indian-Automotive-Specification-Intelligence-Portal/) |
| **Documentation & Assets** | • [Official Project Documentation (PDF)](docs/S.P.B_DATA_TEAM_Automotive_Intelligence_Platform_Documentation.pdf)<br>• [Editable Documentation (DOCX)](docs/Automotive_Intelligence_Platform_Documentation.docx)<br>• [Master Tableau Workbook (.twbx)](tableau/Vehicle_Specification_Master_Dashboard.twbx) |

---

## 📌 Project Overview

Most car-buying portals (like CarWale or CarDekho) present spec sheets in isolation, giving buyers no sense of how a car compares across its wider segment. On the other side, typical corporate BI dashboards show abstract bar and scatter charts with zero connection to the physical car itself.

Our team set out to fix this problem for the Unstop competition by building a **synchronized two-layer analytics platform**:

1. **Analytical Core in Tableau**: 10,000 records modeled across 30 authentic Indian vehicles, calculating price-performance curves, safety equipment distribution, category averages, and head-to-head comparisons.
2. **Interactive Digital Showroom (Embedded via URL Actions)**: A lightweight web application embedded directly inside Tableau that responds to user clicks in real time, showing isolated vehicle cutouts, a 6-axis performance radar chart, and a specification conflict checker.

Clicking any vehicle, fuel type, or silhouette in Tableau immediately filters the charts and updates the embedded showroom below without lag or page reloads.

---

## 📊 Tableau Dashboards

### Dashboard 1: Master Specification & Market Intelligence Cockpit
Built to give product teams, fleet buyers, and car shoppers an instant snapshot of where vehicles sit in the Indian market:
- **Executive KPI Banner**: Displays the active model count, segment median ex-showroom price, average engine output (HP), and 5-star safety compliance rate.
- **Price vs. Horsepower Positioning Scatter Plot**:
  - X-Axis: Ex-showroom price (₹0 to ₹65 Lakhs).
  - Y-Axis: Engine output (0 to 400 HP).
  - Encoded by Powertrain: 🟢 Electric (EV), 🟡 Petrol, 🔵 Diesel. Sized by NCAP safety rating.
  - Hover Tooltip: High-density text tooltip showing exact displacement, torque, certified ARAI economy/range, boot volume, and airbag count with zero lag.
- **Category Benchmark Matrix**: Compares torque output (Nm) and certified fuel efficiency (km/l or km) across hatchbacks, sedans, SUVs, commercial trucks, buses, and 2-wheelers.
- **Safety Matrix**: Shows NCAP star ratings against standard airbag counts across budget bands.
- **EV Profiler**: Cleanly separated from internal combustion filters to compare battery pack sizes (kWh) directly against certified ARAI range for India's major electric models (Nexon EV, XUV400, ZS EV).
- **Embedded Web Showroom**: Responds dynamically to Tableau filter clicks via parameter-driven URL actions.

### Dashboard 2: Head-to-Head 2-Model Comparator
A standalone comparison tool that works entirely inside Tableau without requiring internet access or the web container:
- **Two Dropdown Parameters**: Pick any vehicle in `[Select Model A]` and any vehicle in `[Select Model B]`.
- **Vehicle Image Cards**: Renders vehicle cutouts using custom Tableau shapes from the `Indian_Vehicles` palette alongside brand and ex-showroom price tags.
- **Specification Comparison Matrix**: Side-by-side table comparing Price, Horsepower, Torque, ARAI Efficiency, Safety Rating, Airbag count, Boot capacity, and Ground clearance.
- **Delta Advantage Bars**: Quick horizontal bars highlighting which model leads in Power, Torque, and Cargo capacity.

---

## 🌐 Embedded Digital Showroom Features

We wrote a custom zero-dependency web interface (`index.html`) using clean HTML5, CSS Grid, and Canvas API so it loads instantly inside Tableau's embedded browser:
- **Dual-View Showroom**:
  - *Fleet Mosaic*: A 30-car miniature gallery color-coded by powertrain.
  - *Single Vehicle Stage*: Smooth GSAP transition to an isolated vehicle cutout with individual scale calibration (`VEHICLE_ZOOM_SCALES`).
- **6-Axis HTML5 Canvas Radar**:
  - Compares Price-Value, Horsepower, Range/Efficiency, Safety, and Cabin/Boot space.
  - Plots the active model directly against its segment benchmark (e.g. Creta vs Mid-SUV average, or Nexon EV vs EV segment average).
- **Price vs. Power Canvas Scatter Plot**: Visualizes the market median point (142 HP, ₹14.5 Lakhs) and highlights the chosen model.
- **Specification Conflict Engine**: Catches conflicting filter selections (for example, picking an Electric silhouette with Petrol fuel) and offers a 1-click Auto-Resolve button instead of breaking or showing blank screens.
- **Monotonic Slate Theme**: Designed in `#111827` slate-navy with `#38bdf8` steel blue accents to blend with Tableau's interface without harsh bright glare.
- **Stacked Vertical Layout**: Radar chart is placed directly above the scatter plot so viewers can scroll naturally within Tableau's web object container.

---

## 🛠️ Data Calibration & Engineering

The raw synthetic dataset provided for the challenge had major domain contradictions (such as 300 HP petrol scooters priced at ₹15 Lakhs, and 50-passenger buses running on petrol with 25 km/l mileage).

Our team wrote an automated calibration script (`scripts/calibrate_entire_ecosystem.py`) to ground all 10,000 rows in Indian automotive reality across 16 OEMs and 30 benchmark vehicles:

| Brand | Model | Category | Fuel | Ex-Showroom (INR) | Power (HP) | Torque (Nm) | ARAI Economy | Safety | Boot | Ground Clearance |
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

Every record includes realistic variance (±3.5%) around certified OEM specifications, with valid fuel tank/battery capacities and clearance values suitable for Indian road conditions.

---

## 🧮 Tableau Calculations & Logic

```tableau
// 1. Comparator Filter (keeps only the two selected models on sheet)
[Model] = [Select Model A] OR [Model] = [Select Model B]

// 2. Dynamic Column Header for Comparison Table
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

// 4. Bi-Directional URL Action to Command Embedded Web Portal
"https://hazardous9hub.github.io/Indian-Automotive-Specification-Intelligence-Portal/?model=" 
+ REPLACE([Model], " ", "%20")
+ "&brand=" + REPLACE([Brand], " ", "%20")
+ "&category=" + REPLACE([Category], " ", "%20")
+ "&fuel=" + REPLACE([Fuel Type], " ", "%20")

// 5. Horsepower per Lakh Index (Value Metric)
ROUND([Horsepower Hp] / [Price in Lakhs (INR)], 2)

// 6. Reset Filters Button Label
"↺ Reset All Filters"
```

---

## 📁 Repository Structure

```
Indian-Automotive-Specification-Intelligence-Portal/
├── assets/                               # Visual assets optimized to under 70 KB
│   ├── vehicles_v2/                      # Optimized transparent PNG vehicle cutouts
│   ├── vehicles/                         # Master vehicle cutouts
│   ├── logos/                            # 16 Official OEM vector logos
│   ├── body_styles/, powertrains/        # Technical silhouette and fuel badge icons
│   └── gsap.min.js                       # Animation library for smooth transitions
├── data/                                 # Calibrated datasets
│   ├── vehicle_specification_dataset_10000_rows.csv   # 10,000 calibrated rows (CSV)
│   ├── vehicle_specification_dataset_10000_rows.xlsx  # 10,000 calibrated rows (Excel)
│   ├── vehicle_models_30_profiles.csv                 # Reference profiles for all 30 models
│   ├── vehicle_image_urls_for_tableau.csv             # Tableau Image Role mapping
│   └── vehicle_image_urls_for_tableau.xlsx            # Tableau Image Role mapping (Excel)
├── docs/                                 # Project documentation
│   ├── S.P.B_DATA_TEAM_Automotive_Intelligence_Platform_Documentation.pdf # Final PDF
│   ├── Automotive_Intelligence_Platform_Documentation.docx                 # Editable Word Doc
│   └── Automotive_Intelligence_Platform_Documentation.md                  # Markdown Dossier
├── scripts/                              # Data engineering & utility scripts
│   ├── calibrate_entire_ecosystem.py     # 10,000-row calibration engine
│   ├── apply_tableau_theme.py            # Color harmonizer for dashboard
│   ├── sync_index_html.py                # Dataset-to-web synchronizer
│   ├── optimize_all_images.py            # Image compression pipeline (<70 KB)
│   └── create_docs.py                    # Script used to generate documentation
├── tableau/                              # Tableau workbooks
│   ├── Vehicle_Specification_Master_Dashboard.twbx    # Packaged Tableau workbook (2.4 MB)
│   └── Vehicle_Specification_Master_Dashboard.twb     # Raw XML workbook file
├── index.html                            # Interactive web intelligence showroom (GitHub Pages)
├── vehicle_visual_assets.csv             # Metadata manifest for all vehicle assets
└── README.md                             # Repository overview and team details
```

---

## 🏆 Originality & Integrity Statement

> **TEAM DECLARATION:**  
> This project was designed and built from scratch by the **S.P.B Data Team** specifically for the **Unstop Tableau Competition (September 2026)**.
> - The analytical models, Tableau calculations, and dashboard designs were built by the team.
> - The web application code, canvas radar charts, and conflict detection logic were hand-coded without Bootstrap, website templates, or external UI kits.
> - All vehicle image cutouts were manually gathered, cropped, and compressed below 70 KB to respect Tableau's image role constraints.
> - The dataset was independently recalibrated from raw figures to reflect real-world Indian automotive specifications.

---

## 📬 Contact & Team Acknowledgements

- **Team Name**: **S.P.B Data Team**
- **Authors & Collaborators**:
  1. **Shivaling Battarki** — *Team Lead \| Analytics, Tableau Dashboards & Architecture*  
     GitHub: [@Hazardous9hub](https://github.com/Hazardous9hub) • LinkedIn: [shivaling-93000](https://www.linkedin.com/in/shivaling-93000/) • Email: `shivalingb09@gmail.com`
  2. **Pragatheswaran M** — *Data Engineering & Domain Calibration*  
     GitHub: [@Pragatheswaran-M](https://github.com/Pragatheswaran-M) • LinkedIn: [pragatheswaranm](https://www.linkedin.com/in/pragatheswaranm/) • Email: `pragathes224@gmail.com`
  3. **Basawaraj Kale** — *Research & Analytical Validation*  
     GitHub: [@basawaraj849](https://github.com/basawaraj849) • LinkedIn: [basawarajkale](https://www.linkedin.com/in/basawarajkale/) • Email: `kale.sbasawaraj@gmail.com`
- **Competition**: **Tableau & Data Visualization Challenge 2026** (Organized by **National Institute of Engineering - NIE Mysuru** on [Unstop](https://unstop.com/competitions/tableau-data-visualization-challenge-2026-national-institute-of-engineering-nie-mysuru-1753895))
