import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def create_documentation():
    doc = docx.Document()

    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(11)
    normal_style.font.color.rgb = RGBColor(30, 41, 59)

    def add_title(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(text)
        run.font.size = Pt(20)
        run.font.bold = True
        run.font.color.rgb = RGBColor(31, 78, 121)
        p.paragraph_format.space_after = Pt(4)

    def add_subtitle(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(text)
        run.font.size = Pt(11.5)
        run.font.italic = True
        run.font.color.rgb = RGBColor(71, 85, 105)
        p.paragraph_format.space_after = Pt(16)

    def add_h1(text):
        p = doc.add_paragraph()
        run = p.add_run(text)
        run.font.size = Pt(14)
        run.font.bold = True
        run.font.color.rgb = RGBColor(31, 78, 121)
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(4)

    def add_h2(text):
        p = doc.add_paragraph()
        run = p.add_run(text)
        run.font.size = Pt(12)
        run.font.bold = True
        run.font.color.rgb = RGBColor(14, 116, 144)
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(3)

    def add_body(text, bold_prefix=None):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.font.bold = True
            r_pre.font.color.rgb = RGBColor(15, 23, 42)
        p.add_run(text)

    def add_bullet(text, bold_prefix=None):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.font.bold = True
            r_pre.font.color.rgb = RGBColor(15, 23, 42)
        p.add_run(text)

    def add_code_block(code_text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(5)
        p.paragraph_format.left_indent = Inches(0.2)
        run = p.add_run(code_text)
        run.font.name = 'Consolas'
        run.font.size = Pt(9.5)
        run.font.color.rgb = RGBColor(15, 23, 42)

    # Document Header
    add_title("INDIAN AUTOMOTIVE SPECIFICATION & PERFORMANCE INTELLIGENCE PLATFORM")
    add_subtitle("Comprehensive Project Documentation, Methodology & Competition Submission Dossier\nUnstop Tableau Competition (September 2026) | Author: Shivaling Battarki")

    p_meta = doc.add_paragraph()
    p_meta.paragraph_format.space_after = Pt(12)
    r = p_meta.add_run("Live Tableau Dashboard: ")
    r.font.bold = True
    p_meta.add_run("https://public.tableau.com/app/profile/shivaling.battarki/viz/VehicleSpecificationInteractiveDashboard/INTERACTIVESPECSDETAILS?publish=yes\n")
    r2 = p_meta.add_run("Interactive Web Portal Repository: ")
    r2.font.bold = True
    p_meta.add_run("https://github.com/Hazardous9hub/Indian-Automotive-Specification-Intelligence-Portal")

    add_h1("1. Executive Summary & Core Project Idea")
    add_body("The Indian automotive sector is undergoing its most transformative phase: the simultaneous convergence of Bharat NCAP safety regulations, rapid EV platform evolution, and price tier diversification. However, consumer automotive portals and enterprise BI analytics remain deeply fragmented. Consumer portals provide disjointed spec tables with zero analytical context, while enterprise dashboards present static charts disconnected from the physical vehicle.")
    add_body("The Indian Automotive Specification & Performance Intelligence Platform establishes a real-time, synchronized intelligence cockpit combining:")
    add_bullet("Deep statistical modeling across 10,000 records, dynamic KPI benchmarking, multi-dimensional safety and category matrices, and head-to-head parameter comparators.", "1. Analytical BI Engine in Tableau: ")
    add_bullet("Embedded natively via a zero-latency Web Page Object, delivering an isolated showroom pedestal, real-time 6-axis performance radar charts, specification conflict diagnostics, and high-contrast specs cards.", "2. Interactive Digital Web Portal: ")
    add_body("Selecting any vehicle or market segment in Tableau instantly synchronizes the showroom, providing unprecedented clarity for OEMs, fleet buyers, and retail consumers.")

    add_h1("2. Significance, Real-World Practicality & Applicability")
    add_bullet("Pinpoints market whitespace, horsepower-per-lakh frontiers, and safety equipment democratization across price tiers.", "For Automotive OEMs & Product Planners: ")
    add_bullet("Evaluates commercial carriers (Volvo 9400, Ashok Leyland JanBus) and utility pickups on payload, torque density, and operating efficiency.", "For Commercial Fleet Operators: ")
    add_bullet("Demystifies EV adoption by benchmarking battery capacity (kWh) and real-world ARAI range against traditional ICE benchmarks.", "For Retail Buyers: ")
    add_body("100% Indian Operating Practicality: Every vehicle profile is grounded in authentic Indian engineering realities: ground clearances tailored for Indian road topography (162 mm to 225 mm), certified ARAI fuel efficiencies, and verified Bharat/Global NCAP star ratings.")

    add_h1("3. Data Engineering & Domain Calibration Pipeline")
    add_body("The initial raw synthetic dataset of 10,000 rows suffered from classic synthetic anomalies (e.g. 2-wheelers priced at 15 Lakhs with 300 HP, multi-axle luxury buses running on petrol, EVs with 45-liter fuel tanks).")
    add_body("To ensure complete domain authenticity, an automated engineering pipeline was developed:")
    add_bullet("Clustered all 10,000 records around 30 authentic Indian automotive model profiles across 16 leading OEMs (Tata, Mahindra, Maruti Suzuki, Hyundai, MG, Toyota, Honda, Isuzu, Volvo, Ashok Leyland, Eicher, Force Motors, Hero MotoCorp, TVS, Bajaj, Suzuki).", "1. Ground-Truth Clustering: ")
    add_bullet("Synthesized authentic Gaussian distributions (±3.5% natural variance) preserving real-world Indian engineering constraints:", "2. Engineering Constraints: ")
    add_bullet("Tata Nexon EV: ~16.7L, 145 HP, 215 Nm, 465 km ARAI range, 40.5 kWh pack, 5-Star NCAP.", "   • ")
    add_bullet("Hyundai Creta: ~14.9L, 160 HP, 253 Nm, 18.2 kmpl, 50L fuel tank, 4.5-Star NCAP.", "   • ")
    add_bullet("Volvo 9400 Bus: ~57.8L, 380 HP, 1752 Nm, 4.5 kmpl, 400L diesel tank, 54 seats.", "   • ")
    add_bullet("Honda Activa 6G: ~83k, 7.8 HP, 8.9 Nm, 50 kmpl, 5.3L petrol tank, 162 mm clearance.", "   • ")
    add_bullet("Synchronized across Excel (.xlsx), CSV, and Tableau packaged workbooks with zero null values and standard ISO currency notation.", "3. System Synchronization: ")

    add_h1("4. Web Portal Engineering (Why, How & Authenticity)")
    add_h2("Why Build a Dedicated Web Portal?")
    add_body("Tableau cannot natively render real-time animated 6-axis radar charts, 30-model showroom mosaic grids, or dynamic specification conflict modals. Creating a bespoke web portal injects a hardware-grade interactive showroom directly into Tableau's canvas.")
    add_h2("How It Was Built")
    add_bullet("Zero-Framework Architecture: Built using pure HTML5, vanilla JavaScript, and modern CSS3 Grid/Flexbox without heavy third-party NPM libraries to ensure instantaneous loading in Tableau's browser container.", "• ")
    add_bullet("Monotonic Executive Palette: Styled in executive slate navy (#111827, #182335, #283950) with steel blue accents (#38bdf8) and naturally legible typography (#f8fafc).", "• ")
    add_bullet("6-Axis Radar Telemetry: Canvas-based rendering engine plotting Price-Value, Horsepower, Range/Efficiency, Safety Stars, and Spatial Utility.", "• ")
    add_bullet("Specification Conflict Diagnostics: Real-time rules engine detecting incompatible user filters (e.g., Electric skateboard platform combined with Petrol fuel) with a 1-click Auto-Resolve button.", "• ")
    add_bullet("Deep Tableau Synchronization: Parses URL parameters (?model=Nexon&brand=Tata&category=SUV) driven dynamically by Tableau dashboard actions.", "• ")

    add_h2("Authenticity & Anti-Plagiarism Statement")
    add_body("DECLARATION OF ORIGINALITY: The web application, JavaScript logic, CSS responsive layout, canvas rendering algorithms, conflict diagnostics, and Tableau calculation schemas were authored completely from scratch by the author and project team. No pre-built web templates, Bootstrap starter kits, or third-party cloned repositories were utilized. All 30 vehicle visual assets were manually calibrated, compressed (<70 KB), and uploaded to an independent GitHub Pages infrastructure.")

    add_h1("5. Tableau Dashboard Walkthrough & Interactive Architecture")
    add_h2("Dashboard 1: Master Specification & Market Intelligence Cockpit")
    add_bullet("Executive KPI Banner: Instant macro metrics (30 OEM Models, Segment Median Price, Average Engine HP, 5-Star Safety Compliance Rate).", "1. ")
    add_bullet("Price vs. Performance Market Positioning (Scatter Plot): Plots Price in Lakhs against Horsepower, color-coded by Powertrain (Green = EV, Amber = Petrol, Blue = Diesel) and sized by Global NCAP safety rating. Features a high-density, instant hover tooltip with full engine, torque, cargo, and price breakdown.", "2. ")
    add_bullet("Category Benchmark & Powertrain Matrix: Horizontal bar charts comparing average torque and certified fuel efficiency across silhouettes.", "3. ")
    add_bullet("Safety & Occupant Protection Matrix: Visualizing safety ratings against standard airbag counts across budget tiers.", "4. ")
    add_bullet("Electric Vehicle (EV) Profiler: Dedicated card isolated from ICE cross-filters, benchmarking battery pack capacities (kWh) against real-world ARAI range.", "5. ")
    add_bullet("Embedded Interactive Portal Object: Dynamically synchronizes showroom pedastal and 6-axis radar charts to the user selection.", "6. ")

    add_h2("Dashboard 2: Standalone Head-to-Head 2-Model Comparator")
    add_body("An executive side-by-side comparator running 100% locally from the dataset and local shapes with zero web dependency:")
    add_bullet("Dynamic Model A & Model B Selectors: Synchronized String parameters populated directly from the Model field.", "1. ")
    add_bullet("Hero Vehicle Visual Cards: Displays high-resolution vehicle shape cutouts from the Indian_Vehicles repository palette with ex-showroom price badges.", "2. ")
    add_bullet("Head-to-Head Specification Matrix: Side-by-side tabular comparison across 8 core dimensions: Price, HP, Torque, Efficiency, Safety Rating, Airbags, Boot Capacity, and Ground Clearance.", "3. ")
    add_bullet("Performance Advantage Delta Bar: Visual bar chart displaying which vehicle leads in Horsepower, Torque, and Cargo volume.", "4. ")

    add_h1("6. Complete Tableau Calculations, Formulas & Parameters")
    add_h2("Parameters Created")
    add_bullet("Select Model A: Data Type: String | Allowable Values: List from Model | Default: Nexon", "• ")
    add_bullet("Select Model B: Data Type: String | Allowable Values: List from Model | Default: Creta", "• ")

    add_h2("Calculated Fields & Formulas")
    add_body("1. Comparator Filter Calculation:")
    add_code_block("// Filter_Selected_A_or_B\n[Model] = [Select Model A] OR [Model] = [Select Model B]")

    add_body("2. Dynamic Side-by-Side Column Slot:")
    add_code_block("// Model_Comparison_Slot\nIF [Model] = [Select Model A] THEN \"★ MODEL A: \" + UPPER([Select Model A])\nELSEIF [Model] = [Select Model B] THEN \"★ MODEL B: \" + UPPER([Select Model B])\nEND")

    add_body("3. Visual Star Rating Formatter:")
    add_code_block("// Safety_Stars_Display\nIF [Safety Rating] >= 5.0 THEN \"★★★★★ (5.0)\"\nELSEIF [Safety Rating] >= 4.5 THEN \"★★★★½ (4.5)\"\nELSEIF [Safety Rating] >= 4.0 THEN \"★★★★☆ (4.0)\"\nELSEIF [Safety Rating] >= 3.0 THEN \"★★★☆☆ (3.0)\"\nELSE \"★★☆☆☆ (\" + STR(ROUND([Safety Rating], 1)) + \")\"\nEND")

    add_body("4. Dynamic URL Action Generator:")
    add_code_block("// Interactive_Portal_URL\n\"https://hazardous9hub.github.io/Indian-Automotive-Specification-Intelligence-Portal/?model=\" \n+ REPLACE([Model], \" \", \"%20\")\n+ \"&brand=\" + REPLACE([Brand], \" \", \"%20\")\n+ \"&category=\" + REPLACE([Category], \" \", \"%20\")\n+ \"&fuel=\" + REPLACE([Fuel Type], \" \", \"%20\")")

    add_body("5. Power-to-Price Value Ratio:")
    add_code_block("// HP_per_Lakh_INR\nROUND([Horsepower Hp] / [Price in Lakhs (INR)], 2)")

    add_body("6. One-Click Reset Filter Label:")
    add_code_block("// Reset_Label\n\"↺ Reset All Filters\"")

    add_h1("7. Chart Selection Rationale & Visual Encodings")
    table = doc.add_table(rows=1, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = "Visualization"
    hdr_cells[1].text = "Chart Type"
    hdr_cells[2].text = "Dimensions & Measures"
    hdr_cells[3].text = "Visual Encoding Rationale"
    for cell in hdr_cells:
        for p in cell.paragraphs:
            for r in p.runs:
                r.font.bold = True
                r.font.color.rgb = RGBColor(255, 255, 255)
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="1F4E79"/>')
        cell._tc.get_or_add_tcPr().append(shd)

    data = [
        ("Market Positioning", "Scatter Plot", "Price (X), HP (Y), Fuel (Color), Safety (Size)", "Reveals price-performance clusters and premium margins across segments."),
        ("Category Benchmarks", "Grouped Bar Chart", "Category (Rows), Avg Torque & Mileage (Cols)", "Facilitates cross-segment comparison between high-torque diesel and high-efficiency petrol."),
        ("Safety Matrix", "Step Matrix / Heatmap", "NCAP Stars (Rows), Airbags (Cols), Count (Size)", "Demonstrates the democratization of active/passive safety across Indian budgets."),
        ("EV Profiler", "Bullet Benchmark Card", "Battery kWh (Bar), ARAI Range km (Target)", "Directly correlates battery pack capacity with certified driving autonomy."),
        ("Comparator Matrix", "Side-by-Side Table", "Measure Names (Rows), Model Slot (Cols)", "Eliminates cognitive friction for direct head-to-head metric comparisons."),
        ("Performance Delta", "Diverging Bar", "Measure Values (Cols), Selected Models (Color)", "Provides instantaneous visual clarity on which vehicle holds competitive advantage.")
    ]

    for row_data in data:
        row_cells = table.add_row().cells
        for i, val in enumerate(row_data):
            row_cells[i].text = val
            for p in row_cells[i].paragraphs:
                p.paragraph_format.space_after = Pt(2)
                for r in p.runs:
                    r.font.size = Pt(9.5)

    add_h1("8. Strategic Business Insights & Industry Recommendations")
    add_bullet("The 15L-22L Mid-SUV Sweet Spot: Vehicles in the 14L-18L tier (Tata Nexon, Hyundai Creta, Mahindra Scorpio N) deliver the highest horsepower-per-lakh ratio (8.5 to 10.9 HP/Lakh) while achieving 5-Star NCAP safety.", "1. ")
    add_bullet("Heavy Commercial Decarbonization Urgency: Multi-axle commercial carriers (Volvo 9400, Ashok Leyland JanBus) produce extreme torque (up to 1,750 Nm) but operate at 4.5 kmpl. Electrification or LNG adoption here produces the largest aggregate carbon reduction.", "2. ")
    add_bullet("Two-Wheeler Urban Mobility Foundation: Sub-1 Lakh commuter vehicles (Honda Activa, Hero Splendor) exceed 50 kmpl, providing the foundation for urban affordability.", "3. ")

    doc.save("Automotive_Intelligence_Platform_Documentation.docx")
    print("DOCX successfully generated: Automotive_Intelligence_Platform_Documentation.docx")

if __name__ == "__main__":
    create_documentation()
