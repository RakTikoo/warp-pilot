#!/usr/bin/env python
"""
Gate-33 Item 3: vector/pixel-grade extraction of YBBY (arXiv:1311.7144) Fig. 7 geometry.

Sources (arXiv e-print source files, on disk in ybby_src/):
  - EA-constraints.pdf : the combined (c+,c-) summary panel (paper Fig. 1 left):
    main linear panel (c+ in [0,1], c- in [0,1]) + zoom inset
    (c+ in [0,~0.0365], c- in [0,0.004]) with the combined binary-pulsar
    region drawn as a single filled purple polygon (fill rgb(50%,0%,50%)).
  - The four individual panels that make up Fig. 7 (fig:Pdot-EA) are separate
    files in the same source: Pdot-constraint-NSWD-Bhat (J1141-6545),
    Pdot-constraint-NSWD-Antoniadis (J0348+0432), Pdot-constraint-NSNS
    (J0737-3039), alpha-constraint-NSWD (J1738+0333).  They are log-log
    (c+ in [1e-3,1], c- in [1e-3,1e-1] plotted) with green-hatched bands.

Method:
  EA file: parse pdftocairo -svg output; calibrate the inset axes from the
  drawn tick marks (exact vector segments); convert the purple polygon's
  vertices to (c+,c-) and slice it.
  Panels: rasterise at 600 dpi with pdftocairo, segment green hatch pixels,
  calibrate log axes from pdftotext -bbox tick-label centres
  (checked against axis anchors in the EA file to <=0.09 pt).

Outputs g33_fig7_data.json next to this script's outputs in fig7_extract/.
"""
import json, re, subprocess, sys
from pathlib import Path
import numpy as np
from PIL import Image

WORK = Path(__file__).resolve().parent
SRC = WORK / "ybby_src"
OUT = WORK / "fig7_extract"
OUT.mkdir(exist_ok=True)

def to_svg(pdf, name):
    p = OUT / f"g33_fig7_{name}.svg"
    if not p.exists():
        subprocess.run(["pdftocairo", "-svg", str(pdf), str(p)], check=True)
    return p.read_text()

def to_png600(pdf, name):
    prefix = OUT / f"g33_fig7_600_{name}"
    p = Path(str(prefix) + "-1.png")
    if not p.exists():
        subprocess.run(["pdftocairo", "-png", "-r", "600", str(pdf), str(prefix)], check=True)
    return p

def parse_paths(svg):
    body = svg[svg.find("</defs>"):]
    out = []
    for e in re.findall(r"<path[^>]*>", body):
        dm = re.search(r'd="([^"]*)"', e)
        if not dm:
            continue
        pts = [(float(a), float(b)) for a, b in re.findall(r"[ML]\s*([\d.]+)\s+([\d.]+)", dm.group(1))]
        fm = re.search(r'fill="([^"]*)"', e)
        out.append((fm.group(1) if fm else None, pts))
    return out

# ---------------------------------------------------------------- EA combined
svg = to_svg(SRC / "EA-constraints.pdf", "EA-constraints")
paths = parse_paths(svg)
purple = [pts for fill, pts in paths if fill == "rgb(50%, 0%, 50%)"]
assert len(purple) == 3, f"expected 3 purple paths, got {len(purple)}"
inset_poly = max(purple, key=lambda p: (max(x for x, y in p) - min(x for x, y in p)))
legend = min(purple, key=lambda p: len(p))
main_poly = [p for p in purple if p is not inset_poly and p is not legend][0]

# Inset tick marks (exact vector segments found in the SVG):
#   left-axis ticks at SVG y = 33.08 (c-=0.004), 85.66 (0.002), 138.24 (0)
#   bottom-axis ticks at SVG x = 172.156 (c+=0), 202.20 (0.01), 262.29 (0.03)
IN_X0, IN_SX = 172.155781, 3004.45      # c+ = (x - IN_X0)/IN_SX
IN_Y0, IN_SY = 138.235802, 26290.0      # c- = (IN_Y0 - y)/IN_SY
# tick-fit residuals: dx(0.01)=30.044->3004.4/u, dx(0.03)=90.134->3004.5/u
#                     dy(0.002)=52.58, dy(0.004)=105.16 -> 26290/u exact

def inset_data(pts):
    return [((x - IN_X0) / IN_SX, (IN_Y0 - y) / IN_SY) for x, y in pts]

poly = inset_data(inset_poly)          # ordered polygon vertices, data coords
main_data = [((x - 113.601573) / 292.775, (313.898427 - y) / 292.775) for x, y in main_poly]

def slice_at_cm(poly, cm):
    """c+ interval(s) of horizontal slice at given c- through polygon."""
    xs = []
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]; x2, y2 = poly[(i + 1) % n]
        if (y1 - cm) * (y2 - cm) < 0:
            t = (cm - y1) / (y2 - y1)
            xs.append(x1 + t * (x2 - x1))
        elif y2 == cm and y1 != cm:
            xs.append(x2)
    xs = sorted(xs)
    return [(xs[i], xs[i + 1]) for i in range(0, len(xs) - 1, 2)]

def top_boundary(poly, cp):
    """max c- of polygon at given c+ (vertical slice)."""
    ys = []
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]; x2, y2 = poly[(i + 1) % n]
        if (x1 - cp) * (x2 - cp) < 0:
            t = (cp - x1) / (x2 - x1)
            ys.append(y1 + t * (y2 - y1))
    return max(ys) if ys else None

tests = {"a_cV10": 1.590e-3, "b_cornerB": 0.16586208, "c_cV2": 5.089e-5}
ea = {"polygon_data_coords": poly,
      "main_panel_polygon_data_coords": main_data,
      "max_cm_vertex": max(poly, key=lambda p: p[1]),
      "top_at_left_edge_vertex": poly[21],   # vertex 22: top of left chain
      "slices": {}, "top_boundary_samples": {}}
for k, cm in tests.items():
    ea["slices"][k] = {"cm": cm, "cp_intervals": slice_at_cm(poly, cm)}
for cp in [0.0, 0.000630, 0.001678, 0.004467, 0.006100, 0.01, 0.02, 0.032396]:
    ea["top_boundary_samples"][str(cp)] = top_boundary(poly, cp)

# ---------------------------------------------------------------- panels
# log-log calibration from pdftotext -bbox tick-label centres (PDF pt):
#   x: 10^-3 -> 38.4115, 10^-2 -> 93.9615, 10^-1 -> 149.512  (55.55 pt/dec)
#   y: 10^-1 -> 8.086,  10^-2 -> 61.986,  10^-3 -> 115.886   (53.90 pt/dec)
PX = 600 / 72.0
def panel_cal(Xpt, Ypt):
    logcp = -3 + (Xpt - 38.4115) / 55.55
    logcm = -3 + (115.886 - Ypt) / 53.90
    return 10 ** logcp, 10 ** logcm

panels = {}
for name, label in [("Pdot-constraint-NSWD-Bhat", "J1141-6545"),
                    ("Pdot-constraint-NSWD-Antoniadis", "J0348+0432"),
                    ("Pdot-constraint-NSNS", "J0737-3039"),
                    ("alpha-constraint-NSWD", "J1738+0333")]:
    png = to_png600(SRC / f"{name}.pdf", name)
    a = np.asarray(Image.open(png).convert("RGB")).astype(int)
    R, G, B = a[:, :, 0], a[:, :, 1], a[:, :, 2]
    green = (G > 150) & (R < 120) & (B < 120)
    res = {"label": label}
    # row band for c- = 1.590e-3
    for key, cm in tests.items():
        logcm = np.log10(cm)
        Ypt = 115.886 - (logcm + 3) * 53.90
        row = int(round(Ypt * PX))
        if row < 0 or row >= green.shape[0]:
            res[key] = {"cm": cm, "row_in_plot": False}
            continue
        band = green[max(0, row - 3):row + 4, :].any(axis=0)
        # restrict to plot box x: c+ in [7e-4, 1.05] -> Xpt in [30, 208]
        band[:int(30 * PX)] = False; band[int(208 * PX):] = False
        xs = np.nonzero(band)[0]
        if len(xs) == 0:
            res[key] = {"cm": cm, "row_in_plot": True, "green_in_row": False}
        else:
            # hatch gaps: report overall extent and coverage fraction
            lo, hi = xs.min(), xs.max()
            cov = band[lo:hi + 1].mean()
            res[key] = {"cm": cm, "row_in_plot": True, "green_in_row": True,
                        "cp_lo": panel_cal(lo / PX, Ypt)[0],
                        "cp_hi": panel_cal(hi / PX, Ypt)[0],
                        "hatch_coverage_in_span": float(cov)}
    # band top at small c+: for columns c+ in [0.004, 0.03], highest green row
    tops = []
    for cp in [0.004, 0.006, 0.01, 0.02, 0.03]:
        Xpt = 38.4115 + (np.log10(cp) + 3) * 55.55
        col = int(round(Xpt * PX))
        colg = green[:, max(0, col - 2):col + 3].any(axis=1)
        # exclude legend rows (Ypt < 50)
        colg[:int(50 * PX)] = False
        ys = np.nonzero(colg)[0]
        tops.append((cp, panel_cal(Xpt, ys.min() / PX)[1] if len(ys) else None))
    res["band_top_cm_at_cp"] = tops
    panels[name] = res

data = {"EA_combined": ea, "panels": panels,
        "calibration": {
            "EA_inset": {"cp": f"c+ = (x_svg - {IN_X0})/{IN_SX}",
                         "cm": f"c- = ({IN_Y0} - y_svg)/{IN_SY}",
                         "tick_residuals": "x ticks: 3004.4 vs 3004.5 per unit (rel 3e-5); y ticks: 52.58 per 0.002 twice, exact"},
            "panels": "log-log; x 55.55 pt/dec from label centres 38.4115@1e-3, 93.9615@1e-2, 149.512@1e-1; y 53.90 pt/dec from 115.886@1e-3, 61.986@1e-2, 8.086@1e-1"}}
(OUT / "g33_fig7_data.json").write_text(json.dumps(data, indent=1, default=str))
print(json.dumps({"EA_slices": ea["slices"], "EA_max": ea["max_cm_vertex"],
                  "EA_top_samples": ea["top_boundary_samples"],
                  "panels": panels}, indent=1, default=str))
