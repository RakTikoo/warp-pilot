#!/usr/bin/env python3
"""3D model: Gate-13 composed payload configuration -- nested shells.

Geometry read from stored files only: shell supports regex-extracted from
the stored bundle code (gate13-claims/code/wa_profiles.py build_shell calls
and region_name cuts); row anatomy (held payload, shell betas) from the
stored composed-results file (gate13-claims/sources/p1161_composed.json).

Products:
  model_payload_shells_view1.png / view2.png   translucent nested shells
  payload_shells.obj                           mesh with per-component colours
  payload_shells.stl                           same mesh, binary STL
"""
import json
import re
import struct

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

ROOT = "/home/hatch/workspace/warp-pilot"
FIG = f"{ROOT}/publication/figures"

code = open(f"{ROOT}/gate13-claims/code/wa_profiles.py").read()
shells = sorted((float(a), float(b)) for a, b in
                re.findall(r"build_shell\((\d+\.\d+),\s*(\d+\.\d+)", code))
(i1, i2), (o1, o2) = shells[0], shells[1]
comp = json.load(open(f"{ROOT}/gate13-claims/sources/p1161_composed.json"))
best_key, best = max(comp["rows"].items(),
                     key=lambda kv: kv[1]["anatomy"]["payload_relat"])
anat = best["anatomy"]
print(f"stored geometry: payload r<{i1}, inner shell [{i1}, {i2}], "
      f"cavity ({i2}, {o1}), outer shell [{o1}, {o2}]; row {best_key}: "
      f"payload {anat['payload_relat']}, beta_i {anat['beta_i_alone']}, "
      f"beta_o {anat['beta_o_alone']}")

COMPONENTS = [  # (radius, colour hex, label, alpha in renders)
    (i1, "#f2d16b", f"payload region (r < {i1:.0f})", 1.0),
    (i1, "#3d7ea6", None, 0.45),
    (i2, "#3d7ea6", f"inner shell [{i1:.0f}, {i2:.0f}], β = {anat['beta_i_alone']}", 0.45),
    (o1, "#e07a5f", None, 0.32),
    (o2, "#e07a5f", f"outer shell [{o1:.0f}, {o2:.0f}], β = {anat['beta_o_alone']}", 0.32),
]

def sphere(r, nth, nph):
    th = np.linspace(0, np.pi, nth)
    ph = np.linspace(0, 2 * np.pi, nph)
    TH, PH = np.meshgrid(th, ph, indexing="ij")
    return (r * np.sin(TH) * np.cos(PH), r * np.sin(TH) * np.sin(PH),
            r * np.cos(TH))

for tag, (el, az) in {"view1": (20, -50), "view2": (58, 28)}.items():
    fig = plt.figure(figsize=(8.6, 7.6))
    fig.patch.set_facecolor("white")
    ax = fig.add_subplot(111, projection="3d")
    for r, hexcol, _lab, alpha in COMPONENTS:
        X, Y, Z = sphere(r, 49, 73)
        ax.plot_surface(X, Y, Z, color=hexcol, alpha=alpha, shade=True,
                        linewidth=0, antialiased=False)
    ax.view_init(elev=el, azim=az)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title("Gate-13 composed payload configuration — nested shells\n"
                 f"held payload {anat['payload_relat']:.5f}c "
                 f"(row {best_key}); cavity ({i2:.0f}, {o1:.0f}) between the shells",
                 fontsize=10.5)
    handles = [Line2D([0], [0], marker="o", ls="", ms=10, color=c,
                      label=l) for _r, c, l, _a in COMPONENTS if l]
    ax.legend(handles=handles, fontsize=9, loc="upper left")
    out = f"{FIG}/model_payload_shells_{tag}.png"
    fig.savefig(out, dpi=200, facecolor="white")
    plt.close(fig)
    print("wrote", out)

# --- exportable mesh ---
def hex2rgb(h):
    return tuple(int(h[i:i + 2], 16) / 255 for i in (1, 3, 5))

NTH, NPH = 73, 96
verts, cols, faces = [], [], []
for r, hexcol, _lab, _a in COMPONENTS:
    th = np.linspace(0, np.pi, NTH)
    ph = np.linspace(0, 2 * np.pi, NPH)
    TH, PH = np.meshgrid(th, ph, indexing="ij")
    P = np.stack([r * np.sin(TH) * np.cos(PH), r * np.sin(TH) * np.sin(PH),
                  r * np.cos(TH)], axis=-1)
    base = len(verts)
    for i in range(NTH):
        for j in range(NPH):
            verts.append(P[i, j])
            cols.append(hex2rgb(hexcol))
    for i in range(NTH - 1):
        for j in range(NPH):
            j1 = (j + 1) % NPH
            a, b = base + i * NPH + j, base + i * NPH + j1
            c, d = base + (i + 1) * NPH + j, base + (i + 1) * NPH + j1
            faces += [(a, b, c), (b, d, c)]
verts = np.array(verts)
faces = np.array(faces)
print(f"mesh: {len(verts)} vertices, {len(faces)} faces")

with open(f"{FIG}/payload_shells.obj", "w") as f:
    f.write("# Gate-13 composed payload configuration (Phase 116 row "
            f"{best_key})\n# radii from gate13-claims/code/wa_profiles.py; "
            "one colour per component\n")
    for v, c in zip(verts, cols):
        f.write(f"v {v[0]:.6f} {v[1]:.6f} {v[2]:.6f} "
                f"{c[0]:.4f} {c[1]:.4f} {c[2]:.4f}\n")
    for a, b, c in faces:
        f.write(f"f {a + 1} {b + 1} {c + 1}\n")
print("wrote", f"{FIG}/payload_shells.obj")

with open(f"{FIG}/payload_shells.stl", "wb") as f:
    f.write(b"\0" * 80)
    f.write(struct.pack("<I", len(faces)))
    for a, b, c in faces:
        pa, pb, pc = verts[a], verts[b], verts[c]
        n = np.cross(pb - pa, pc - pa)
        ln = np.linalg.norm(n)
        n = n / ln if ln > 0 else n
        f.write(struct.pack("<12fH", n[0], n[1], n[2], pa[0], pa[1], pa[2],
                            pb[0], pb[1], pb[2], pc[0], pc[1], pc[2], 0))
print("wrote", f"{FIG}/payload_shells.stl")
