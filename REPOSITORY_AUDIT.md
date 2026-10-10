# 📋 Comprehensive Repository Authenticity & Documentation Audit

**Project:** Indian Automotive Specification & Performance Intelligence Platform  
**Repository:** [Hazardous9hub/Indian-Automotive-Specification-Intelligence-Portal](https://github.com/Hazardous9hub/Indian-Automotive-Specification-Intelligence-Portal)  
**Live Tableau Dashboard:** [Tableau Public Link](https://public.tableau.com/app/profile/shivaling.battarki/viz/VehicleSpecificationInteractiveDashboard/INTERACTIVESPECSDETAILS?publish=yes)  
**Live Web Portal:** [GitHub Pages Link](https://hazardous9hub.github.io/Indian-Automotive-Specification-Intelligence-Portal/)  
**LinkedIn Post:** [Official LinkedIn Announcement](https://lnkd.in/p/gVCpZ_Jw)  
**Team:** S.P.B Data Team (Shivaling Battarki, Pragatheswaran M, Basawaraj Kale)  
**Competition:** Tableau & Data Visualization Challenge 2026 (National Institute of Engineering - NIE Mysuru & HackerRank Campus Crew on Unstop) — **1st Place Winner** 🏆  
**Audit Date:** October 10, 2026  

---

## 1. Executive Summary & Audit Purpose

The purpose of this audit is to systematically review all documentation, codebases, datasets, and public claims across the repository to ensure **100% authenticity, technical consistency, and transparent attribution**. 

In particular, this audit reconciles the public communication on LinkedIn with the GitHub repository:
- **Tableau Dashboards**: Conceived, designed, and constructed independently by the **S.P.B Data Team**.
- **Interactive Web Portal**: Developed with technical assistance from **Google's Antigravity IDE** for frontend code architecture, Canvas 2D telemetry, and URL parameter handling.
- **Connection**: Tableau and the web portal are joined via Tableau's native Web Page Dashboard Object driven by **URL Actions** (`?model=<Model>&brand=<Brand>&fuel=<Fuel>`).

This audit report identifies existing discrepancies, unsupported promotional claims, and broken/inconsistent references, and outlines a verifiable, phased plan to synchronize the repository with authentic project reality.

---

## 2. Current Repository Structure

The git repository is located at `D:\Unstop Tableau Comptition Sep 2026\Vehicle Specification Dataset\3d_viewer`.

```
Indian-Automotive-Specification-Intelligence-Portal/
├── assets/
│   ├── body_styles/                      # 8 SVG silhouette category icons
│   ├── logos/                            # 16 SVG OEM brand logos
│   ├── powertrains/                      # 3 SVG fuel badge icons (Petrol, Diesel, EV)
│   ├── vehicles/                         # 30 master vehicle JPG & PNG cutouts
│   ├── vehicles_v2/                      # 30 compressed transparent PNG cutouts (<70 KB)
│   ├── gsap.min.js                       # Standalone GreenSock animation library
│   └── resolved_vehicle_images.json      # Asset mapping metadata
├── data/
│   ├── vehicle_specification_dataset_10000_rows.csv   # Recalibrated dataset (10,000 rows, CSV)
│   ├── vehicle_specification_dataset_10000_rows.xlsx  # Recalibrated dataset (Excel)
│   ├── vehicle_models_30_profiles.csv                 # 30 authentic OEM baseline specifications
│   ├── vehicle_image_urls_for_tableau.csv             # Tableau Image Role & hosted asset URLs
│   └── vehicle_image_urls_for_tableau.xlsx            # Tableau Image Role mapping (Excel)
├── docs/
│   ├── S.P.B_DATA_TEAM_Automotive_Intelligence_Platform_Documentation.pdf  # Project PDF Dossier
│   ├── Automotive_Intelligence_Platform_Documentation.docx                  # Editable Word Document
│   └── Automotive_Intelligence_Platform_Documentation.md                   # Markdown Documentation
├── scripts/
│   ├── calibrate_entire_ecosystem.py     # Python script calibrating 10k synthetic rows to OEM baselines
│   ├── apply_tableau_theme.py            # XML color harmonizer script for Tableau workbook
│   ├── sync_index_html.py                # Dataset-to-HTML synchronization script
│   ├── optimize_all_images.py            # Image compression and transparent border cropper
│   └── create_docs.py                    # Python-docx documentation generator
├── tableau/
│   ├── Vehicle_Specification_Master_Dashboard.twbx    # Packaged Tableau Workbook (2.4 MB)
│   └── Vehicle_Specification_Master_Dashboard.twb     # Raw XML Tableau Workbook
├── index.html                            # Standalone web portal & embedded showroom (5,430 lines)
├── vehicle_visual_assets.csv             # Metadata catalog for all visual assets
├── LICENSE                               # MIT License
└── README.md                             # Main repository documentation
```

---

## 3. Current README Assessment & Gap Analysis

| Section | Current State | Assessment | Recommended Action |
| :--- | :--- | :--- | :--- |
| **Title & Milestone** | Mentions Unstop competition & NIE Mysuru. | Accurate, but does not explicitly highlight the **1st Place Winner** outcome celebrated on LinkedIn. | Update header badge and subtitle to reflect 1st Place win. |
| **Team Attribution** | Lists Shivaling Battarki, Pragatheswaran M, Basawaraj Kale with roles. | Accurate, but LinkedIn post used a simpler peer format without formal corporate titles. | Offer team section reflecting clean collaborative structure. |
| **Development Attribution** | Claims: *"The web application code, canvas radar charts, and conflict detection logic were hand-coded without Bootstrap, website templates, or external UI kits."* | **Critical Gap**: Misleadingly implies the team manually typed 5,400+ lines of HTML/JS with zero AI tooling, contradicting the LinkedIn post which explicitly credited Google Antigravity. | **Correct immediately**: Transparently state that the web portal was built with the assistance of Google Antigravity IDE, while Tableau dashboards were built by the team. |
| **Chart Descriptions** | Describes *Category Benchmark* as comparing torque (Nm) and certified fuel efficiency. | **Technical Inconsistency**: In the actual Tableau dashboard, *Category Benchmark* is a dual-axis vertical bar chart comparing **Average Price in Lakhs (INR)** (bars) and **Average Mileage / EV Range** (dots). It does not plot torque on that view. | Correct chart metric descriptions to match the actual Tableau worksheet. |
| **Promotional Tone** | Uses buzzwords like *"zero-latency"*, *"complete harmony"*, *"executive cockpit"*. | Over-promotional and reads like AI marketing copy. | Replace with neutral technical terms: *"client-side rendering"*, *"parameter-driven URL action"*, *"market overview"*. |
| **Visual Evidence** | README has zero screenshots. | Critical weakness: visitors cannot see the dashboards or web portal without clicking external links. | Embed 3-4 screenshots directly in the README (Master Dashboard, Comparator, Web Portal, Certificate). |
| **Historical Directory Name** | Directory named `3d_viewer`. | Potential confusion: the project is an interactive 2D pedestal with Canvas radar, not a 3D WebGL renderer. | Clarify in documentation that `3d_viewer` was an initial project working directory name. |

---

## 4. Claims Requiring Team Verification vs. Confirmed Facts

### Confirmed by Repository & Code:
1. **Dataset Size & Structure**: `data/vehicle_specification_dataset_10000_rows.csv` contains exactly 10,000 rows across 16 OEMs and 30 specific vehicle models.
2. **Tableau Integration Mechanism**: Tableau dashboard uses a Web Page Object configured with URL parameter action: `?model=<Model>&brand=<Brand>&category=<Category>&fuel=<Fuel Type>`.
3. **Web Portal Technology**: `index.html` is a standalone client-side application using vanilla JavaScript, Canvas 2D API for the radar and scatter plots, and local GSAP (`assets/gsap.min.js`) for pedestal transitions. No React, Vue, Tailwind CDN, or Bootstrap dependencies exist in production.
4. **Tableau Dashboards**:
   - Dashboard 1: `INTERACTIVE SPECS DETAILS` (KPI banner, Price vs HP scatter plot, Category Benchmark dual-axis, Safety Matrix, EV Profiler, Embedded Web Object).
   - Dashboard 2: `MODEL COMPARATOR` (Dual parameters `Select Model A` / `Select Model B`, shape mark cards, tabular comparison matrix, delta advantage bars).

### Requiring Team Confirmation:
1. **Teammate Name Spelling**: The LinkedIn post uses `Basavaraj Kale` (with a 'v'), whereas git commits and earlier markdown files used `Basawaraj Kale` (with a 'w'). The team should confirm their preferred official spelling.
2. **Original Competition Dataset**: The README states that raw competition data had synthetic contradictions (e.g. 300 HP petrol scooters). Confirmation that this calibration was performed as part of phase 1 data cleaning.
3. **Screenshot Selection for README**: Confirm whether to use the 3 existing PNG screenshots (`Interactive_Specs_dashboard.png`, `Model_Comaparator_SS.png`, `Webpage_portal_screrenshot.png`) plus a clean render of `Shivaling Battarki.pdf` (certificate).

---

## 5. Development Attribution Corrections

To ensure complete transparency and academic/professional honesty, the attribution section must be updated to explicitly differentiate roles:

### What the Team Built:
- **Ideation & Analytical Formulation**: Identifying the gap between isolated consumer spec sheets and abstract BI scatter plots.
- **Tableau Analytical Engineering**: Designing both dashboards (`INTERACTIVE SPECS DETAILS` and `MODEL COMPARATOR`), creating all calculated fields (`HP_per_Lakh_INR`, `Filter_Selected_A_or_B`, `Model_Comparison_Slot`, `Safety_Stars_Display`), configuring dual-axis charts, custom shape palettes, and parameter controls.
- **Automotive Domain Calibration**: Defining the 30 realistic baseline vehicle profiles (`MODEL_SPECS` in `scripts/calibrate_entire_ecosystem.py`) anchored in authentic ARAI fuel efficiencies, Bharat NCAP safety ratings, and Indian road clearances.
- **Tableau URL Action Binding**: Architecting the parameter pass-through syntax to synchronize Tableau with external web containers.

### What Google Antigravity IDE Assisted With:
- **Web Portal Development**: Providing agentic code generation and refactoring to produce `index.html`, including:
  - The HTML5 Canvas 2D radar telemetry renderer.
  - The client-side parameter parser (`URLSearchParams`) and alias normalizer.
  - The specification conflict detection and auto-resolve state machine.
  - Image optimization and transparent PNG cutout formatting (`scripts/optimize_all_images.py`).

### Accurate Replacement for Originality Declaration:
> **PROJECT & DEVELOPMENT DECLARATION:**  
> This project was created by the **S.P.B Data Team** for the **Unstop Tableau Data Visualization Challenge 2026** (organized by NIE Mysuru & HackerRank Campus Crew).  
> - **Analytical Architecture & Tableau Dashboards**: 100% designed, calculated, and built by the project team.  
> - **Web Intelligence Portal**: Developed with the technical assistance of **Google's Antigravity IDE**, which assisted in writing and optimizing the zero-dependency HTML5, CSS Grid, and Canvas telemetry logic.  
> - **Data Engineering**: Raw competition figures were recalibrated via Python to eliminate synthetic anomalies and ground all 10,000 records in authentic Indian automotive specifications.

---

## 6. Proposed README Outline

A clean, authentic, and well-structured README outline:

1. **Header & Badges**
   - Title: Indian Automotive Specification & Performance Intelligence Platform
   - Winner Callout: 1st Place Winner — Tableau Data Visualization Challenge 2026 (NIE Mysuru & HackerRank Campus Crew on Unstop)
   - Status badges: Live Tableau Dashboard, Live Web Portal, Calibrated Dataset, License
2. **Project Team**
   - Clean, collaborative team table (Names, GitHub profiles, LinkedIn links, emails — avoiding inflated corporate titles)
3. **Problem Statement & Analytical Questions**
   - The isolation gap in automotive spec sheets vs. abstract BI reporting
   - Key analytical questions answered by the platform
4. **Platform Architecture**
   - Synchronized two-layer design diagram (Macro Analytical BI $\longleftrightarrow$ URL Parameters $\longleftrightarrow$ Micro Showroom Telemetry)
5. **Tableau Dashboards Overview**
   - Dashboard 1: Master Specification & Market Intelligence Cockpit (KPI banner, Price vs HP scatter plot, Category benchmark dual-axis, Safety matrix, EV profiler)
   - Dashboard 2: Head-to-Head 2-Model Comparator (Dual parameter selection, shape cards, comparison table, delta bars)
6. **Embedded Web Portal Overview**
   - 6-Axis Canvas Performance Radar
   - Parameter Handshake (`?model=...`)
   - Conflict Detection Engine
7. **Data Calibration & Methodology**
   - Original synthetic dataset challenges
   - 10,000-row calibration methodology across 30 authentic Indian reference vehicles
8. **Development Workflow & Tool Attribution**
   - Explicit breakdown: Team-built Tableau workbooks vs. Antigravity-assisted web portal code
9. **Visual Showcase (Embedded Screenshots)**
   - Winner Certificate
   - Master Dashboard screenshot
   - Model Comparator screenshot
   - Web Showroom screenshot
10. **Repository Directory Guide & Reproducibility**
    - File guide (`data/`, `tableau/`, `scripts/`, `docs/`, `assets/`)
    - How to run locally (`python -m http.server 8000`)

---

## 7. Proposed Documentation Architecture

Currently, the `docs/` folder contains duplicate versions of the same dossier in three formats:
1. `docs/Automotive_Intelligence_Platform_Documentation.md` (Markdown source)
2. `docs/Automotive_Intelligence_Platform_Documentation.docx` (Generated Word document)
3. `docs/S.P.B_DATA_TEAM_Automotive_Intelligence_Platform_Documentation.pdf` (Compiled PDF)

### Proposed Architecture:
- Treat `docs/Automotive_Intelligence_Platform_Documentation.md` as the single canonical source of truth.
- Update `scripts/create_docs.py` to regenerate the `.docx` and `.pdf` files only when the markdown source changes.
- Ensure the documentation dossier has the exact same attribution statement, chart metric descriptions, and team credits as the README.
- Add a dedicated `docs/screenshots/` folder containing the 4 primary project screenshots referenced by the README.

---

## 8. Screenshot Requirements for README

To make the GitHub repository visually engaging, the following 4 images should be added to `docs/screenshots/` (or `assets/screenshots/`) and linked via Markdown:

| Image File | Description | Purpose |
| :--- | :--- | :--- |
| `01_winner_certificate.png` | Official Certificate of Appreciation from HackerRank / NIE Mysuru | Immediate verification of 1st place milestone |
| `02_master_specs_dashboard.png` | High-res view of `Interactive_Specs_dashboard.png` | Demonstrates the primary analytical BI cockpit |
| `03_model_comparator.png` | High-res view of `Model_Comaparator_SS.png` | Demonstrates the 2-model parameter comparator |
| `04_web_portal_showroom.png` | High-res view of `Webpage_portal_screrenshot.png` | Demonstrates the Canvas radar and visual showroom |

---

## 9. Proposed File-Change List

### Files to Update:
1. `README.md`: Implement proposed outline, correct attribution, remove exaggerated copy, fix chart metrics, embed screenshots.
2. `docs/Automotive_Intelligence_Platform_Documentation.md`: Align claims, attribution, and chart descriptions with the updated README.
3. `scripts/create_docs.py`: Update text strings so regenerated `.docx` files reflect the accurate attribution and chart descriptions.

### Files to Add:
1. `REPOSITORY_AUDIT.md`: This comprehensive audit document.
2. `docs/screenshots/` (4 PNG assets for visual documentation).

### Protected Files (DO NOT MODIFY):
- `index.html` (Application logic intact)
- `tableau/Vehicle_Specification_Master_Dashboard.twbx` & `.twb` (Tableau workbook intact)
- `data/*` (All CSV and XLSX datasets intact)
- `scripts/calibrate_entire_ecosystem.py`, `scripts/sync_index_html.py`, `scripts/optimize_all_images.py`
- `assets/*` (All image assets, icons, logos, and libraries intact)

---

## 10. Step-by-Step Implementation Plan

Following team approval of this audit:

- [ ] **Step 1: Asset Preparation**  
  Copy and organize the 4 project screenshots into `docs/screenshots/` inside the git repository.
- [ ] **Step 2: Rewrite `README.md`**  
  Apply the revised outline with grounded technical language, honest Antigravity attribution for the web portal, corrected chart metrics, and embedded image links.
- [ ] **Step 3: Update `docs/Automotive_Intelligence_Platform_Documentation.md`**  
  Synchronize the long-form project documentation with the revised README claims.
- [ ] **Step 4: Update `scripts/create_docs.py` & Regenerate Word Dossier**  
  Ensure documentation generation scripts output identical attribution.
- [ ] **Step 5: Verification & Pre-Commit Review**  
  Inspect `git diff` to confirm zero touched files in protected paths (`index.html`, datasets, Tableau files).
- [ ] **Step 6: Git Commit & Push to Main**  
  Commit changes with clean, co-authored commit message and push to GitHub remote.
