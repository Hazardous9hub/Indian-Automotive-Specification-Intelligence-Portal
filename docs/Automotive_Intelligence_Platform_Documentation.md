# Indian Automotive Specification & Performance Intelligence Platform

## Technical Project Documentation & Competition Dossier

> **🏆 1st Place Winner** — **Tableau & Data Visualization Challenge 2026**  
> Organized by **The National Institute of Engineering (NIE), Mysuru** & **HackerRank Campus Crew** on [Unstop](https://unstop.com/competitions/tableau-data-visualization-challenge-2026-national-institute-of-engineering-nie-mysuru-1753895)  
> **Team:** S.P.B Data Team  
> **Authors:**
> - **Shivaling Battarki** ([@Hazardous9hub](https://github.com/Hazardous9hub) | [LinkedIn](https://www.linkedin.com/in/shivaling-93000/) | `shivalingb09@gmail.com`)
> - **Pragatheswaran M** ([@Pragatheswaran-M](https://github.com/Pragatheswaran-M) | [LinkedIn](https://www.linkedin.com/in/pragatheswaranm/) | `pragathes224@gmail.com`)
> - **Basavaraj Kale** ([@basawaraj849](https://github.com/basawaraj849) | [LinkedIn](https://www.linkedin.com/in/basawarajkale/) | `kale.sbasawaraj@gmail.com`)

---

## 🔗 Project Links

- 📊 **Interactive Tableau Dashboard**: [Tableau Public Live Link](https://public.tableau.com/app/profile/shivaling.battarki/viz/VehicleSpecificationInteractiveDashboard/INTERACTIVESPECSDETAILS?publish=yes)
- 🌐 **Deployed Web Intelligence Portal**: [GitHub Pages Live Link](https://hazardous9hub.github.io/Indian-Automotive-Specification-Intelligence-Portal/)
- 💼 **LinkedIn Project Walkthrough**: [Official LinkedIn Breakdown](https://lnkd.in/p/gVCpZ_Jw)
- 💻 **GitHub Repository**: [Hazardous9hub/Indian-Automotive-Specification-Intelligence-Portal](https://github.com/Hazardous9hub/Indian-Automotive-Specification-Intelligence-Portal)

---

## 1. Executive Summary & Core Project Idea

The Indian automotive sector is experiencing a multi-dimensional evolution: concurrent adoption of Bharat NCAP safety benchmarks, high-voltage EV skateboard architectures, multi-fuel powertrains (Petrol, Diesel, EV, CNG), and shifting price segments. 

However, existing resources remain fragmented:
- **Consumer Portals (CarDekho, CarWale)** present technical specification sheets in isolation without macro segment benchmarking.
- **Corporate BI Dashboards** typically show abstract aggregate charts with no visual link to the physical vehicle.

### The Solution: A Synchronized Two-Layer Architecture
1. **Analytical BI Core in Tableau**: 10,000 simulated/calibrated records generated around 30 Indian vehicle baseline profiles spanning 16 OEMs, analyzing price-performance frontiers, category averages, safety compliance, and dual-model comparisons.
2. **Interactive Web Showroom**: A lightweight, client-side web application embedded directly inside Tableau via URL Web Page actions, displaying vehicle cutouts, a 6-axis performance radar chart, and engineering conflict diagnostics.

Selecting any model, silhouette, or fuel type in Tableau triggers URL parameter actions (`?model=<Model>&brand=<Brand>&fuel=<Fuel>`), updating the embedded showroom without page reloads.

---

## 2. Development Workflow & Tool Attribution

To maintain academic and professional transparency:

- **Tableau Dashboards & Analytical Modeling**: The S.P.B Data Team independently designed and constructed the Tableau workbooks, calculated fields (`HP_per_Lakh_INR`, `Filter_Selected_A_or_B`, `Model_Comparison_Slot`, `Safety_Stars_Display`), parameter architectures, dual-axis encodings, shape mappings, and visual layouts. Google Antigravity was not used to build the Tableau dashboards.
- **Interactive Web Portal**: The web portal (`index.html`) was developed with technical assistance from **Google's Antigravity IDE**, which assisted in writing and optimizing the vanilla HTML5, CSS Grid, Canvas 2D telemetry, and URL parameter parser logic. The team directed requirements, verified calculations, and integrated the portal into the project and Tableau.
- **Tableau-to-Web Integration**: Connected via Tableau's native Web Page Dashboard Object driven by parameter-based URL Actions.

---

## 3. Data Engineering & Domain Calibration Pipeline

### 3.1 Initial Dataset Challenges
The raw competition dataset of 10,000 rows contained synthetic anomalies typical of uncalibrated data generators:
- Two-wheelers listed at ₹15,00,000 with 300 HP engine ratings.
- Commercial transit buses listed with petrol engines and 25 km/l fuel efficiency.
- Electric vehicles listed with 45-liter liquid fuel tanks.

### 3.2 Calibration Methodology
The team authored an automated calibration engine (`scripts/calibrate_entire_ecosystem.py`) to ground every row in Indian automotive reality:
1. **Anchor Profiles**: Established 30 authentic baseline profiles (`MODEL_SPECS`) across 16 OEMs (Tata Motors, Mahindra, Maruti Suzuki, Hyundai, Honda, Toyota, MG, Isuzu, Force, Eicher, Ashok Leyland, Volvo, Hero, Bajaj, TVS, Suzuki).
2. **Controlled Variance**: Synthesized realistic Gaussian variance (±3.5%) around authentic baseline specifications across 10,000 records:
   - **Tata Nexon EV**: ~₹16.7L, 145 HP, 215 Nm, 465 km certified ARAI range, 40.5 kWh battery, 5★ NCAP, 205 mm clearance.
   - **Hyundai Creta**: ~₹14.9L, 160 HP, 253 Nm, 18.2 kmpl ARAI, 50L fuel tank, 4.5★ NCAP, 190 mm clearance.
   - **Volvo 9400 Bus**: ~₹57.8L, 380 HP, 1752 Nm, 4.5 kmpl, 400L tank, 5★ NCAP, 240 mm clearance.
   - **Honda Activa 6G**: ~₹83k, 7.8 HP, 8.9 Nm, 50 kmpl ARAI, 5.3L tank, 162 mm clearance.
3. **Data Integrity**: Handled null values, verified valid powertrain-fuel compatibility, and established standardized numeric data types for Tableau integration.

---

## 4. Web Portal Technical Architecture

### 4.1 Implementation
- **Zero-Dependency Architecture**: Built using vanilla HTML5, CSS3 Grid/Flexbox, and Canvas 2D API with local GSAP (`assets/gsap.min.js`) for pedestal transitions. No heavy external frameworks or UI kits were used.
- **Monotonic Slate Theme**: Uses a dark slate palette (`#111827` base, `#182335` card surface, `#283950` borders, `#38bdf8` steel-blue accents, and `#f8fafc` typography) matching Tableau's executive color scheme.
- **6-Axis Canvas Radar Telemetry**: Normalizes Power, Torque, Range/Mileage, Safety, Boot Capacity, and Ground Clearance against category averages.
- **Conflict Diagnostics**: Rules engine detecting physical mismatches (e.g., selecting Electric silhouette with Petrol fuel) with an auto-resolve mechanism.
- **URL Parameter Router**: Client-side parameter parser reading query strings to focus the active vehicle model and update specifications instantly.

---

## 5. Tableau Dashboard Walkthrough & Verified Chart Encodings

### 5.1 Dashboard 1: Master Specification & Market Intelligence Cockpit (`INTERACTIVE SPECS DETAILS`)
1. **Executive KPI Ribbon (Top)**:
   - Total Monitored Fleet: 30 benchmark models across 16 OEMs.
   - Segment Median Ex-Showroom Price (INR).
   - Fleet Average Engine Output (HP).
   - Bharat/Global NCAP 5-Star Safety Compliance Rate.
2. **Price vs. Horsepower Market Positioning (Scatter Plot)**:
   - **X-Axis**: Engine Output in Horsepower (0 to 400 HP).
   - **Y-Axis**: Ex-Showroom Price in Lakhs (₹0L to ₹65L).
   - **Color Encoding**: 🟢 Pure Electric (EV), 🟡 Petrol (ICE), 🔵 Diesel (ICE).
   - **Size Encoding**: Peak Torque (Nm).
   - **Detail**: Sliced across Brand and Model.
3. **Category Benchmark (Dual-Axis Chart)**:
   - **Columns**: Vehicle Category (Hatchback, Sedan, SUV, Commercial, Bus, Motorcycle, Scooter, etc.).
   - **Primary Axis (Vertical Bars)**: Average Price in Lakhs (INR), colored by Fuel Type.
   - **Secondary Axis (Circle Dots)**: Average certified ARAI fuel efficiency (km/l) or EV driving range (km), highlighted in red dots with value labels.
4. **Safety & Occupant Protection Matrix**:
   - Visualizes Bharat/Global NCAP star ratings against standard airbag counts across budget tiers.
5. **Electric Vehicle (EV) Profiler**:
   - Compares battery pack capacities (kWh) directly against certified ARAI range for India's mass EV models (Nexon EV, XUV400, ZS EV).
6. **Embedded Interactive Portal Object**:
   - Embedded web frame responding to user filter clicks via parameter-driven URL dashboard actions.

### 5.2 Dashboard 2: Standalone Head-to-Head 2-Model Comparator (`MODEL COMPARATOR`)
An offline comparative tool that operates independently within Tableau:
1. **Model A & Model B Selectors**: Two synchronized String parameters populated from `[Model]`.
2. **Side-by-Side Vehicle Cards**: Displays custom shape marks from the `Indian_Vehicles` shape palette with price, category, and fuel badges.
3. **Head-to-Head Specification Matrix**: Side-by-side tabular comparison across 8 core dimensions: Price, HP, Torque, ARAI Efficiency/Range, NCAP Rating, Airbags, Boot Capacity, and Ground Clearance.
4. **Performance Advantage Diverging Bar**: Visual delta bars indicating which vehicle leads in Power (HP), Torque (Nm), and Cargo volume (Liters).

---

## 6. Complete Tableau Calculations & Formulas

```tableau
// 1. Comparator Filter (keeps only the two selected models in view)
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

// 4. Tableau-to-Web URL Action
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

## 7. Verified Visual Encodings & Chart Selection Rationale

| Visualization | Chart Type | Dimensions & Measures | Visual Rationale |
| :--- | :--- | :--- | :--- |
| **Market Positioning** | Scatter Plot | X: Horsepower (HP), Y: Price in Lakhs (INR), Color: Fuel Type, Size: Torque (Nm) | Surfaces the value frontier and power density per price tier. |
| **Category Benchmarking** | Dual-Axis Chart | Cols: Category, Rows 1: Avg Price (Bars by Fuel), Rows 2: Avg Mileage/Range (Red Dots) | Evaluates acquisition price against daily operating economy on a single canvas. |
| **Occupant Safety** | Heatmap / Step Matrix | Rows: NCAP Stars, Cols: Airbag Counts | Evaluates the democratization of passive safety across vehicle segments. |
| **EV Profiler** | Dual-Metric Card | Battery kWh vs. Certified ARAI Range km | Correlates battery capacity with certified driving autonomy. |
| **Comparator Matrix** | Tabular Matrix | Measure Names (Rows), Model Slot (Cols) | Facilitates direct side-by-side engineering evaluation. |
| **Performance Delta** | Diverging Horizontal Bar | Measure Values (Cols), Selected Models (Color) | Quantifies lead margins in Horsepower, Torque, and Cargo capacity. |

---

## 8. Strategic Market Insights & Analytical Findings

1. **The ₹15L–₹22L Mid-SUV Value Crossover**:
   Vehicles in the ₹14L–₹18L tier (Creta, Nexon, Scorpio N) exhibit the highest horsepower-per-lakh ratio (8.5 to 10.9 HP/Lakh) while achieving 5-star NCAP compliance.
2. **Commercial Fleet Decarbonization**:
   Heavy commercial vehicles (Volvo 9400, JanBus) deliver up to 1,750 Nm torque but operate at ~4.5 km/l. Electrification or alternative fuels in this tier offer high potential for aggregate carbon reduction.
3. **Two-Wheeler Urban Mobility Foundation**:
   Sub-₹1 Lakh commuter vehicles (Activa, Splendor) exceed 50 km/l fuel economy, anchoring urban last-mile transport efficiency.

---

## 9. Limitations & Project Context

- **Simulated Variance**: While anchored in verified OEM baseline specifications, the 10,000 dataset records contain simulated Gaussian variance (±3.5%) around those baselines for competition modeling. They should not be interpreted as official factory build sheets.
- **Tableau Web Object Dependency**: In Tableau Desktop or Tableau Public, the embedded web container requires an active internet connection to load the GitHub Pages application.
- **Analytical Scope**: Conclusions represent findings from the competition modeling scenario and are intended as decision-support demonstrations rather than definitive industry-wide absolutes.

---

## 10. Project Team & Acknowledgements

### S.P.B Data Team:
- **Shivaling Battarki** ([@Hazardous9hub](https://github.com/Hazardous9hub) | [LinkedIn](https://www.linkedin.com/in/shivaling-93000/) | `shivalingb09@gmail.com`)
- **Pragatheswaran M** ([@Pragatheswaran-M](https://github.com/Pragatheswaran-M) | [LinkedIn](https://www.linkedin.com/in/pragatheswaranm/) | `pragathes224@gmail.com`)
- **Basavaraj Kale** ([@basawaraj849](https://github.com/basawaraj849) | [LinkedIn](https://www.linkedin.com/in/basawarajkale/) | `kale.sbasawaraj@gmail.com`)

### Event Acknowledgements:
Organized by **The National Institute of Engineering (NIE), Mysuru** and **HackerRank Campus Crew** via **Unstop** (Tableau & Data Visualization Challenge 2026). Special thanks to **Chandan Shridhar Hegde**, **Dr. Vanamala C K**, and the evaluation committee.
