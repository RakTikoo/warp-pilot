"""Supplementary check: position of the drawn Cherenkov/stability (light-blue)
boundary in the EA inset relative to the purple combined region's left edge.

Method: 600-dpi raster of EA-constraints.pdf; light blue = RGB ~(222,240,255).
At c- = 2.5e-3 the purple region does not cover the Cherenkov line, so the
first light-blue pixel in that row measures the drawn line directly.
An earlier tile-union test on the SVG was discarded: main-panel light-blue
tiles overlap the inset's SVG coordinate area and contaminate it.
"""
import numpy as np
from PIL import Image
from pathlib import Path

a = np.asarray(Image.open(Path(__file__).parent / "fig7_extract" / "g33_fig7_EA600-1.png").convert("RGB")).astype(int)
PX = 600 / 72.0
lb = (np.abs(a[:, :, 0] - 222) < 25) & (np.abs(a[:, :, 1] - 240) < 20) & (a[:, :, 2] > 240)
# inset calibration (PDF pt): origin (115.066, 127.166); 3004.45 pt per unit c+; 26290 pt per unit c-
for cm in [2.5e-3]:
    Ypt = 127.166 - cm * 26290
    row = int(round(Ypt * PX))
    band = lb[max(0, row - 2):row + 3, :].any(axis=0)
    xs = np.nonzero(band)[0]
    xs = xs[(xs / PX > 110) & (xs / PX < 230)]
    cp_first = (xs.min() / PX - 115.066) / 3004.45
    print(f"c-={cm}: drawn Cherenkov line at c+ = {cp_first:.6f}; "
          f"analytic c+/(3(1-c+)) line at {3*cm/(1+3*cm):.6f}")
print("At c-=1.590e-3: purple left edge c+ = 0.004671 (vector); Cherenkov line by "
      "linear continuation of the drawn line from (0,0) through (0.007234, 2.5e-3): "
      "c+ = 0.004601 -> purple edge is 7e-5 (in c+) to the allowed (right) side, "
      "i.e. coincident within ~1 line width.")
