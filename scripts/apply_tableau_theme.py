import re

with open("3d_viewer/index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Swap Radar and Scatter in HTML
old_charts_block = """    <!-- Comparative Analytics & Scatter Plots -->
    <div class="charts-row">
      <!-- Price vs Power Scatter Plot -->
      <div class="chart-panel-card">
        <div class="chart-header">
          <span class="chart-title" id="scatterChartTitle">Market Positioning: Price vs Horsepower</span>
          <span id="scatterChartSub" style="font-size:0.65rem; color:var(--accent-sky); font-weight:700;">Cyan Dot = Selected Vehicle</span>
        </div>
        <div class="chart-canvas-wrap">
          <canvas id="scatterCanvas"></canvas>
        </div>
      </div>

      <!-- Performance Multi-Axis Radar -->
      <div class="chart-panel-card">
        <div class="chart-header">
          <span class="chart-title" id="radarChartTitle">Fleet-Wide Performance Spectrum</span>
          <span id="radarChartSub" style="font-size:0.65rem; color:var(--text-muted); font-weight:700;">Overall Fleet Average (30 Models) vs EV Benchmark (3 Models)</span>
        </div>
        <div class="chart-canvas-wrap">
          <canvas id="radarCanvas"></canvas>
        </div>
      </div>
    </div>"""

new_charts_block = """    <!-- Comparative Analytics: Radar Chart First (Immediate Visibility in Tableau), Scatter Plot Below -->
    <div class="charts-row">
      <!-- Performance Multi-Axis Radar (FIRST) -->
      <div class="chart-panel-card" style="border-top:3px solid var(--tab-blue);">
        <div class="chart-header">
          <span class="chart-title" id="radarChartTitle">Fleet-Wide Performance Spectrum (6-Axis Telemetry)</span>
          <span id="radarChartSub" style="font-size:0.68rem; color:var(--tab-blue); font-weight:700;">Active Vehicle Radar Benchmark</span>
        </div>
        <div class="chart-canvas-wrap">
          <canvas id="radarCanvas"></canvas>
        </div>
      </div>

      <!-- Price vs Power Scatter Plot (SECOND / BELOW) -->
      <div class="chart-panel-card">
        <div class="chart-header">
          <span class="chart-title" id="scatterChartTitle">Market Positioning: Price vs Horsepower</span>
          <span id="scatterChartSub" style="font-size:0.68rem; color:var(--accent-sky); font-weight:700;">Market Cluster Positioning</span>
        </div>
        <div class="chart-canvas-wrap">
          <canvas id="scatterCanvas"></canvas>
        </div>
      </div>
    </div>"""

if old_charts_block in content:
    content = content.replace(old_charts_block, new_charts_block)
    print("SUCCESS: Swapped Radar (First) and Scatter Plot (Second) in HTML!")
else:
    print("WARNING: Could not find exact old_charts_block in HTML")

# 2. Update :root variables for Tableau Theme
old_root_pattern = r":root\s*\{.*?\}"
new_root = """:root {
      /* Official Tableau Executive Clean Palette */
      --bg-dark: #f8fafc;
      --bg-surface: #ffffff;
      --card-bg: #ffffff;
      --card-border: #cbd5e1;
      --card-border-hover: #1f4e79;
      --text-main: #0f172a;
      --text-muted: #475569;
      --text-dim: #64748b;
      --table-accent: #1f4e79;

      /* Official Tableau 10 Data Colors */
      --tab-blue: #1f4e79;
      --tab-orange: #f28e2c;
      --tab-red: #e15759;
      --tab-teal: #76b7b2;
      --tab-green: #59a14f;
      --tab-yellow: #edc948;
      --tab-purple: #b07aa1;
      --tab-pink: #ff9da7;

      /* High-Contrast Badges & Accents */
      --accent-cyan: #0284c7;
      --accent-sky: #0369a1;
      --accent-emerald: #15803d;
      --accent-amber: #b45309;
      --accent-rose: #b91c1c;
      --accent-indigo: #1f4e79;
      --accent-purple: #7e22ce;
    }"""

content = re.sub(old_root_pattern, new_root, content, count=1, flags=re.DOTALL)
print("SUCCESS: Replaced :root with Tableau Executive Palette!")

# 3. Update body background
content = re.sub(r"body\s*\{[^}]*\}", """body {
      background-color: #f8fafc;
      background: #f8fafc;
      color: #0f172a;
      font-family: 'Plus Jakarta Sans', sans-serif;
      min-height: 100vh;
      overflow-x: hidden;
      padding: 6px 12px 20px 12px;
      line-height: 1.35;
    }""", content, count=1)

# 4. Enhance Spec Cards styling
spec_cards_enhancement = """
    /* Elevated High-Contrast Technical Specs Cards */
    .spec-module-card {
      background: #ffffff !important;
      border: 1px solid #cbd5e1 !important;
      border-left: 4px solid var(--tab-blue) !important;
      border-radius: 8px !important;
      padding: 10px 12px !important;
      box-shadow: 0 2px 8px rgba(15, 23, 42, 0.06) !important;
      transition: all 0.2s ease;
    }
    .spec-module-card:hover {
      border-color: var(--tab-blue) !important;
      box-shadow: 0 4px 14px rgba(31, 78, 121, 0.15) !important;
    }
    .val-metric-large {
      color: #0f172a !important;
      font-size: 1.35rem !important;
      font-weight: 800 !important;
    }
    .val-metric-unit {
      color: #475569 !important;
      font-size: 0.85rem !important;
      font-weight: 700 !important;
    }
    .module-icon-tag {
      color: var(--tab-blue) !important;
      font-weight: 800 !important;
      font-size: 0.72rem !important;
      text-transform: uppercase;
      letter-spacing: 0.03em;
    }
    .module-subtext {
      color: #64748b !important;
      font-size: 0.72rem !important;
    }
    .spec-gauge-track {
      background: #e2e8f0 !important;
    }
    .single-hero-stage {
      background: #ffffff !important;
      border: 1px solid #cbd5e1 !important;
      box-shadow: 0 4px 16px rgba(15, 23, 42, 0.05) !important;
    }
    .chart-panel-card {
      background: #ffffff !important;
      border: 1px solid #cbd5e1 !important;
      box-shadow: 0 2px 8px rgba(15, 23, 42, 0.05) !important;
    }
    .chart-title {
      color: #0f172a !important;
      font-weight: 800 !important;
    }
    .top-header {
      border-bottom: 1px solid #e2e8f0 !important;
    }
    .portal-title {
      color: #0f172a !important;
    }
    .brand-section-header, .filter-block-title {
      color: #334155 !important;
    }
    .pill-btn, .body-style-btn, .brand-logo-tile {
      background: #ffffff !important;
      border: 1px solid #cbd5e1 !important;
      color: #334155 !important;
    }
    .pill-btn:hover, .body-style-btn:hover, .brand-logo-tile:hover {
      border-color: var(--tab-blue) !important;
      color: var(--tab-blue) !important;
    }
    .pill-btn.active, .body-style-btn.active, .brand-logo-tile.active {
      background: #1f4e79 !important;
      border-color: #1f4e79 !important;
      color: #ffffff !important;
    }
    .kpi-card {
      background: #ffffff !important;
      border: 1px solid #cbd5e1 !important;
      box-shadow: 0 2px 6px rgba(15, 23, 42, 0.05) !important;
    }
    .kpi-label {
      color: #475569 !important;
    }
    .kpi-value {
      color: #0f172a !important;
    }
    .kpi-sub {
      color: #64748b !important;
    }
"""

content = content.replace("</style>", spec_cards_enhancement + "\n  </style>")

# 5. Update Canvas text & grid colors in scatter and radar
# Replace dark canvas text/grid references with light palette
content = content.replace("ctx.strokeStyle = '#1f2a44'", "ctx.strokeStyle = '#e2e8f0'")
content = content.replace('ctx.strokeStyle = "rgba(255, 255, 255, 0.1)"', 'ctx.strokeStyle = "rgba(15, 23, 42, 0.12)"')
content = content.replace('ctx.fillStyle = "#9ca3af"', 'ctx.fillStyle = "#475569"')
content = content.replace('ctx.fillStyle = "#e5e7eb"', 'ctx.fillStyle = "#0f172a"')
content = content.replace('ctx.fillStyle = "#ffffff"', 'ctx.fillStyle = "#0f172a"')
content = content.replace('ctx.strokeStyle = "rgba(255, 255, 255, 0.15)"', 'ctx.strokeStyle = "rgba(15, 23, 42, 0.15)"')
content = content.replace('ctx.fillStyle = "rgba(255, 255, 255, 0.85)"', 'ctx.fillStyle = "rgba(15, 23, 42, 0.85)"')

with open("3d_viewer/index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: Applied Tableau Light Theme, Highlighted Spec Cards, and moved Radar above Scatter Plot!")
