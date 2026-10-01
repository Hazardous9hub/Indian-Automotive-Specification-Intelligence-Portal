# INDIAN AUTOMOTIVE SPECIFICATION & PERFORMANCE INTELLIGENCE PLATFORM
## Technical Project Documentation & Competition Submission Dossier
**Competition:** Unstop Tableau & Data Visualization Challenge (September 2026)  
**Team Name:** S.P.B Data Team  
**Authors (S.P.B Data Team):**
1. **Shivaling Battarki** (Team Lead \| `shivalingb09@gmail.com` \| GitHub: [@Hazardous9hub](https://github.com/Hazardous9hub) \| LinkedIn: [shivaling-93000](https://www.linkedin.com/in/shivaling-93000/))
2. **Pragatheswaran M** (Data Engineering & Domain Calibration \| `pragathes224@gmail.com` \| GitHub: [@Pragatheswaran-M](https://github.com/Pragatheswaran-M) \| LinkedIn: [pragatheswaranm](https://www.linkedin.com/in/pragatheswaranm/))
3. **Basawaraj Kale** (Research & Analytical Validation \| `kale.sbasawaraj@gmail.com` \| GitHub: [@basawaraj849](https://github.com/basawaraj849) \| LinkedIn: [basawarajkale](https://www.linkedin.com/in/basawarajkale/))

**Live Tableau Dashboard:** [Tableau Public Link](https://public.tableau.com/app/profile/shivaling.battarki/viz/VehicleSpecificationInteractiveDashboard/INTERACTIVESPECSDETAILS?publish=yes)  
**Live Portal Repository:** [GitHub Repository](https://github.com/Hazardous9hub/Indian-Automotive-Specification-Intelligence-Portal)  

---

## 1. Executive Summary & Core Project Idea

The Indian automotive sector is undergoing its most radical transformation since the 1990s: the concurrent convergence of Bharat NCAP safety benchmarks, high-voltage EV skateboard architectures, multi-fuel powertrains (Petrol, Diesel, EV, CNG), and rapid price tier migration. However, consumer automotive portals and enterprise OEM analytics remain severely fragmented:
- Consumer portals (CarDekho, CarWale) provide disjointed specification tables without analytical cross-segment context.
- Traditional enterprise BI dashboards present static charts detached from the emotional and physical reality of the vehicle.

### The Breakthrough Solution
The **Indian Automotive Specification & Performance Intelligence Platform** creates a **two-way synchronized ecosystem** bridging:
1. **An Analytical Engine in Tableau:** Deep statistical modeling across 10,000 records, dynamic KPI benchmarking, multi-dimensional safety and category matrices, and head-to-head parameter comparators.
2. **A Responsive Interactive Web Portal:** Embedded natively inside Tableau via a zero-latency Web Page Object, providing an isolated showroom pedestal, real-time 6-axis performance radar charts, conflict detection engines, and high-contrast specs cards.

This integration delivers an executive cockpit where clicking any model or segment in Tableau instantly commands the visual and technical showroom, enabling automotive OEMs, fleet managers, and retail buyers to derive instantaneous intelligence.

---

## 2. Significance, Practicality & Real-World Applicability

### Commercial Significance
- **For Automotive OEMs & Product Planners:** Instantly identify market whitespace (e.g., the safety-to-cost gap between ₹12L and ₹18L SUVs).
- **For Fleet Procurement Directors:** Evaluate commercial vehicles (Starbus, JanBus, 9400, Pro 3015) vs. commercial utility pickups on lifecycle payload, engine torque density, and fuel economy.
- **For Retail Buyers:** Demystify EV adoption by comparing total battery pack size (kWh) vs. certified ARAI range against traditional ICE benchmarks.

### Practicality in the Indian Market
- **100% Indian Market Calibration:** All 30 representative profiles (from an ₹83,000 Honda Activa up to a ₹58 Lakh Volvo 9400 Multi-Axle Luxury Bus) are calibrated to authentic Indian ex-showroom pricing, ARAI certified fuel figures, Bharat/Global NCAP star ratings, and exact ground clearances engineered for Indian road topography.
- **Offline & Online Resilience:** Operates with high reliability on Tableau Public, using optimized vehicle cutouts (<70 KB per asset to guarantee compliance with Tableau’s strict 200 KB Image Role limit) and self-contained JavaScript visualization libraries.

---

## 3. Data Engineering & Domain Calibration Pipeline

### 3.1 Initial Dataset Challenges
The raw synthetic dataset of 10,000 rows exhibited critical domain anomalies common in synthetic data generation:
- Scooters and 2-wheelers listed at ₹15,00,000 with 300 HP engines.
- Commercial multi-axle buses listed with petrol engines and 25 km/l mileage.
- Electric vehicles listed with 45-liter fuel tanks.

### 3.2 Systematic Cleaning & Calibration Methodology
We built automated calibration engines (`calibrate_entire_ecosystem.py` and `apply_tableau_theme.py`) to systematically re-anchor every row:
1. **Mathematical Grounding:** Clustered records into 30 representative Indian vehicle profiles across 16 leading OEMs (Tata Motors, Mahindra, Maruti Suzuki, Hyundai, MG, Toyota, Honda, Isuzu, Volvo, Ashok Leyland, Eicher, Force Motors, Hero MotoCorp, TVS, Bajaj, Suzuki).
2. **Deterministic Distributions:** Synthesized natural variance (±3.5% gaussian variance) around authentic OEM base specs across 10,000 records:
   - **Tata Nexon EV:** ~₹16.7L, 145 HP, 215 Nm, 465 km ARAI range, 40.5 kWh pack, 5★ NCAP, 205 mm clearance.
   - **Hyundai Creta:** ~₹14.9L, 160 HP, 253 Nm, 18.2 kmpl, 50L tank, 4.5★ NCAP, 190 mm clearance.
   - **Volvo 9400 Bus:** ~₹57.8L, 380 HP, 1752 Nm, 4.5 kmpl, 400L tank, 5★ NCAP, 54 seats.
   - **Honda Activa 6G:** ~₹83k, 7.8 HP, 8.9 Nm, 50 kmpl, 5.3L tank, 162 mm clearance.
3. **Data Integrity Guarantee:** Zero null values, standardized ISO currency notation (INR / Lakhs), normalized category labels, and synchronized CSV/XLSX assets.

---

## 4. Web Portal Engineering (Why, How & Authenticity)

### 4.1 Why Build a Dedicated Web Portal?
Tableau's native shape rendering cannot natively draw real-time animated multi-axis radar webs, reactive conflict warning modals, or smooth CSS-accelerated showroom carousels. Building the portal allows us to embed a **high-precision hardware interface** inside Tableau's canvas.

### 4.2 How It Was Engineered
- **Architecture:** Zero-framework, vanilla HTML5, modern CSS3 Grid/Flexbox, and Canvas API. Zero heavy NPM dependencies for instantaneous loading in Tableau's CEF (Chromium Embedded Framework) browser.
- **Monotonic Executive Palette:** Engineered with a deep slate/navy palette (`#111827` base, `#182335` surfaces, `#283950` borders, `#38bdf8` steel blue accents, and `#f8fafc` text) that integrates into Tableau Desktop and Tableau Public.
- **Dynamic 6-Axis Radar Telemetry:** Custom HTML5 canvas engine rendering Price-Value, Horsepower, Range/Efficiency, Safety Stars, and Spatial Utility with animated dual-polygon overlays.
- **Specification Conflict Engine:** A diagnostic rules engine that detects physical incompatibilities (e.g., selecting an Electric Skateboard platform with Petrol fuel) and provides a 1-click Auto-Resolve button.
- **Tableau Deep Linking:** Bi-directional communication parsing URL query parameters:
  `?model=Nexon&category=SUV&fuel=Petrol&brand=Tata` automatically focuses the showroom pedestal and radar benchmark.

### 4.3 Authenticity & Anti-Plagiarism Statement
> **AUTHENTICITY DECLARATION:**  
> The web application, JavaScript logic, CSS layout, canvas rendering algorithms, conflict diagnostics, and Tableau calculation schemas were **created entirely from scratch by the author**. No pre-built web templates, Bootstrap kits, or cloned external repositories were utilized. All vehicle cutouts were manually processed and compressed to meet enterprise benchmarks.

---

## 5. Tableau Dashboard Walkthrough & Interactive Architecture

### 5.1 Dashboard 1: Master Specification & Market Intelligence Cockpit
1. **Executive KPI Ribbon (Top):**
   - Total Monitored Fleet: 30 OEM Models across 16 Brands.
   - Market Median Ex-Showroom Price: Dynamic across filtered segments.
   - Average Powertrain Output: Contextual horsepower benchmarks.
   - Bharat/Global NCAP 5-Star Compliance Rate.
2. **Price vs. Performance Market Positioning (Scatter Plot):**
   - **X-Axis:** Acquisition Price in Lakhs (₹0L to ₹65L).
   - **Y-Axis:** Engine Output in Horsepower (0 to 400 HP).
   - **Visual Encoding:** Color-coded by Fuel Type (Green = EV, Amber = Petrol, Blue = Diesel). Sized by Safety Rating.
   - **Hover Experience:** Clean, high-density text tooltip providing complete engine, torque, cargo, and price breakdown.
3. **Category Benchmark & Powertrain Matrix:**
   - Multi-measure bar charts highlighting average torque output and fuel economy across vehicle silhouettes (SUV, Sedan, Hatchback, Commercial, Bus, Two-Wheeler).
4. **Safety & Occupant Protection Matrix:**
   - Visualizing Global NCAP stars against standard airbag counts across budget tiers.
5. **Electric Vehicle (EV) Profiler:**
   - Dedicated segment card isolated from ICE cross-filter contamination, comparing battery pack capacities (kWh) against real-world ARAI range for Nexon EV, XUV400, and ZS EV.
6. **Embedded Interactive Portal Object:**
   - Sits in the lower canvas, dynamically synchronizing to the user's Tableau selections via URL dashboard actions.

### 5.2 Dashboard 2: Standalone Head-to-Head 2-Model Comparator
An offline comparative tool that operates independently of the web container:
1. **Dynamic Model A & Model B Selectors:** Two synchronized String parameters populated from `[Model]`.
2. **Side-by-Side Hero Vehicle Cards:** Displays high-resolution vehicle shape cutouts from the `Indian_Vehicles` repository palette with ex-showroom price badges.
3. **Head-to-Head Specification Matrix:** Complete side-by-side tabular comparison across 8 core dimensions: Price, HP, Torque, Efficiency, Safety Rating, Airbags, Boot Capacity, and Ground Clearance.
4. **Performance Advantage Diverging Bar:** Visual delta chart showing which vehicle takes the lead in Power, Torque, and Cargo volume.

---

## 6. Complete Tableau Calculations & Formulas

### 1. Model Comparator Filter
```tableau
// Name: Filter_Selected_A_or_B
// Purpose: Isolates canvas to the two user-selected models
[Model] = [Select Model A] OR [Model] = [Select Model B]
```

### 2. Side-by-Side Column Slot
```tableau
// Name: Model_Comparison_Slot
// Purpose: Splits data into dedicated side-by-side comparison columns
IF [Model] = [Select Model A] THEN "★ MODEL A: " + UPPER([Select Model A])
ELSEIF [Model] = [Select Model B] THEN "★ MODEL B: " + UPPER([Select Model B])
END
```

### 3. Star Rating Formatter
```tableau
// Name: Safety_Stars_Display
// Purpose: Converts numerical safety score into visual stars
IF [Safety Rating] >= 5.0 THEN "★★★★★ (5.0)"
ELSEIF [Safety Rating] >= 4.5 THEN "★★★★½ (4.5)"
ELSEIF [Safety Rating] >= 4.0 THEN "★★★★☆ (4.0)"
ELSEIF [Safety Rating] >= 3.0 THEN "★★★☆☆ (3.0)"
ELSE "★★☆☆☆ (" + STR(ROUND([Safety Rating], 1)) + ")"
END
```

### 4. Interactive URL Action Trigger
```tableau
// Name: Interactive_Portal_URL
// Purpose: Constructs URL with parameters to drive embedded portal
"https://hazardous9hub.github.io/Indian-Automotive-Specification-Intelligence-Portal/?model=" 
+ REPLACE([Model], " ", "%20")
+ "&brand=" + REPLACE([Brand], " ", "%20")
+ "&category=" + REPLACE([Category], " ", "%20")
+ "&fuel=" + REPLACE([Fuel Type], " ", "%20")
```

### 5. Power-to-Price Value Ratio
```tableau
// Name: HP_per_Lakh_INR
// Purpose: Measures mechanical performance delivered per unit investment
ROUND([Horsepower Hp] / [Price in Lakhs (INR)], 2)
```

### 6. One-Click Reset Filter Label
```tableau
// Name: Reset_Label
// Purpose: Provides clickable text for dashboard filter reset action
"↺ Reset All Filters"
```

---

## 7. Visual Encodings & Chart Selection Rationale

| Visualization | Chart Type | Dimensions & Measures | Visual Rationale |
| :--- | :--- | :--- | :--- |
| **Market Positioning** | Scatter Plot | Price (X), HP (Y), Fuel (Color), Safety (Size) | Reveals market density and performance premiums across price brackets. |
| **Category Benchmarking** | Grouped Horizontal Bar | Category (Rows), Avg Torque & Mileage (Cols) | Facilitates cross-segment comparison between high-torque diesels and high-efficiency petrols. |
| **Occupant Safety** | Step Matrix / Heatmap | NCAP Stars (Rows), Airbags (Cols), Model Count (Size) | Demonstrates the democratization of safety equipment in the Indian mass market. |
| **EV Profiler** | Dual-Metric Bullet Card | Battery kWh (Bar), ARAI Range km (Target) | Directly correlates battery pack investment with driving autonomy. |
| **Comparator Matrix** | Side-by-Side Tabular Matrix | Measure Names (Rows), Model Slot (Cols) | Eliminates cognitive friction for direct vehicle comparisons. |
| **Performance Delta** | Diverging Bar Chart | Measure Values (Cols), Selected Models (Color) | Highlights the competitive delta between vehicles. |

---

## 8. Strategic Insights & Industry Recommendations

1. **The ₹15L–₹22L Mid-SUV Value Crossover:**
   Vehicles in the ₹14L–₹18L bracket (Tata Nexon, Hyundai Creta, Mahindra Scorpio N) deliver the highest horsepower-per-lakh ratio (between 8.5 and 10.9 HP/Lakh) while delivering 5-star NCAP safety, making this the most contested value battlefield in India.
2. **The Commercial Efficiency Divide:**
   Multi-axle commercial carriers (Volvo 9400, Ashok Leyland JanBus) exhibit extreme torque density (up to 1,750 Nm), but operate at fuel economies below 5 km/l. Electrification or LNG transition in this heavy tier represents the highest potential for aggregate carbon reduction.
3. **The Two-Wheeler Mobility Anchor:**
   Sub-₹1 Lakh commuter vehicles (Honda Activa, Hero Splendor) deliver over 50 km/l fuel economy, anchoring India’s urban last-mile transportation efficiency.

---

## 9. Conclusion & Team Details
The **Indian Automotive Specification & Performance Intelligence Platform** pairs Tableau’s analytical modeling with a responsive, embedded web intelligence showroom. By grounding every data point in authentic Indian market reality, this project offers an intuitive, technically rigorous tool built for executive decision-making.

---

### Project Team (S.P.B Data Team)
- **Shivaling Battarki** — *Team Lead \| Analytics, Tableau Dashboards & Architecture*  
  GitHub: [@Hazardous9hub](https://github.com/Hazardous9hub) • LinkedIn: [shivaling-93000](https://www.linkedin.com/in/shivaling-93000/) • Email: `shivalingb09@gmail.com`
- **Pragatheswaran M** — *Data Engineering & Domain Calibration*  
  GitHub: [@Pragatheswaran-M](https://github.com/Pragatheswaran-M) • LinkedIn: [pragatheswaranm](https://www.linkedin.com/in/pragatheswaranm/) • Email: `pragathes224@gmail.com`
- **Basawaraj Kale** — *Research & Analytical Validation*  
  GitHub: [@basawaraj849](https://github.com/basawaraj849) • LinkedIn: [basawarajkale](https://www.linkedin.com/in/basawarajkale/) • Email: `kale.sbasawaraj@gmail.com`
- **Event**: Unstop Tableau & Data Visualization Challenge (National Institute of Engineering - NIE Mysuru, September 2026)
