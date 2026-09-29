# 🚗 Indian Automotive Specification & Performance Intelligence Portal

[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-brightgreen?style=for-the-badge&logo=github)](https://hazardous9hub.github.io/Indian-Automotive-Specification-Intelligence-Portal/)
[![Tableau Compatible](https://img.shields.io/badge/Tableau-Web%20Action%20Ready-blue?style=for-the-badge&logo=tableau)](https://hazardous9hub.github.io/Indian-Automotive-Specification-Intelligence-Portal/)
[![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)](LICENSE)

An executive, high-performance interactive automotive intelligence portal engineered for the **Unstop Tableau Competition 2026**. Designed to bridge macro market analytics with deep vehicle-level engineering telemetry across **30 representative models from 16 leading Indian OEMs**.

🔗 **Live Portal**: [https://hazardous9hub.github.io/Indian-Automotive-Specification-Intelligence-Portal/](https://hazardous9hub.github.io/Indian-Automotive-Specification-Intelligence-Portal/)

---

## 🌟 Key Architecture & Capabilities

### 1. Dual-Mode Studio Pedestal (GSAP Morphing)
- **All-Models Showroom Mosaic (Default View)**:
  - Displays all 30 benchmark vehicle models together in miniature scale on a single 205px studio pedestal.
  - Pulsing guidance banner: `✨ Select your preference from the filters above or click any model below to inspect`.
  - Color-coded fuel indicators (Green = EV, Amber = Petrol, Blue = Diesel, Cyan = CNG).
- **Focused Single-Vehicle Cockpit**:
  - Activated by clicking any miniature card or selecting any filter (Brand, Powertrain, Silhouette, Customer Interest, Seating, Budget).
  - Smooth morphing transition powered by **GSAP 3.12.5**.
  - Calibrated aspect-ratio zoom factors (`VEHICLE_ZOOM_SCALES`), isolated authentic cutouts, and studio underglow pedestal.

### 2. Multi-Axis Performance Radar Chart
- **Fleet Spectrum Mode (Overall View)**:
  - Displays the **Overall Indian Automotive Market Spectrum**:
    - **Tableau Blue (`#60a5fa`) polygon**: 30-Model Fleet-Wide Average benchmark across Price-Value, Horsepower, Range/Efficiency, Safety, and Cabin/Boot dimensions.
    - **Tableau Emerald (`#59a14f`) dashed polygon**: EV & High-Tech Sector Benchmark.
- **Comparative Vehicle Mode**:
  - Plots the active vehicle's 5-axis telemetry against its specific category benchmark (e.g., SUV vs SUV peers, EV vs EV benchmark).

### 3. Dynamic Indian Market Flank Telemetry
- Left flank: Engine displacement, transmission, drivetrain architecture, horsepower with dynamic percentage delta vs category average, peak torque, and 0-100 km/h acceleration.
- Right flank: Real-world range / fuel efficiency (with electric-aware km ARAI vs ICE km/l ARAI), NCAP safety star rating, airbags, ground clearance, and **Cabin, Cargo & Fuel Tank / Battery Pack capacity**.

### 4. Interactive Scatter Analytics
- Multi-dimensional **Price vs. Horsepower positioning matrix** with segment color-coding and **Market Fleet Median** callout.

### 5. Official Tableau-Compatible Dark Theme
- Compliant with competition color palette: `#0b1220` background, `#0f1a2b` card surface, `#1f2a44` borders, `#60a5fa` accents, and `#e5e7eb` typography.
- URL Parameter routing ready for Tableau Dashboard Web Page Actions (`?brand=<OEM>&model=<Model>&budget=<MaxBudget>`).

---

## 🛠️ Technology Stack
- **Frontend Core**: Vanilla HTML5, Canvas 2D Rendering Engine, CSS Grid & Flexbox
- **Animation Framework**: GreenSock Animation Platform (GSAP 3.12.5)
- **Typography**: Space Grotesk & Plus Jakarta Sans
- **Graphics & Assets**: High-resolution authentic isolated vehicle PNGs, official vector SVG brand logos
- **Deployment**: GitHub Pages (Zero-dependency static hosting)

---

## 🚀 Local Development
To run this portal locally:
```bash
# Clone the repository
git clone https://github.com/Hazardous9hub/Indian-Automotive-Specification-Intelligence-Portal.git

# Navigate into directory
cd Indian-Automotive-Specification-Intelligence-Portal

# Start any static web server (e.g. Python)
python -m http.server 8000
```
Open `http://localhost:8000/index.html` in your web browser.

---

## 👨‍💻 Author
**Shivaling Battarki** ([@Hazardous9hub](https://github.com/Hazardous9hub))
