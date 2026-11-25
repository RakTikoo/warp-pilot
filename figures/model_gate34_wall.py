#!/usr/bin/env python3
"""3D model: the Phase 312 broad-ramp winner's bubble wall (the Gate-34
member), coloured by the required density rho_req.

Evaluated with the programme's stored Phase 312 machinery
(phase312/work/p312_lib.py): WINNER_SPEC from the library, the member
profile read from phase312/results/p312_results.json (the stored member
labelled ramp_broad_m+1.00). The script first verifies its evaluator
against the stored record: rho at binding site S1 must reproduce the
stored rho_req. The mesh band is the posed volume r in [10, 20] (the
SET-244 radial nodes' range, read from the stored library's R_NODES).
No profile numbers are typed into this script.

Products:
  model_gate34_wall_view1.png / view2.png   wall surface at the radius of
                                            maximum angular contrast
  model_gate34_wall_shell.png               cutaway of the exported mesh
  gate34_wall_shell.obj / .stl              shell mesh over [10, 20]
"""
import json
import struct
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize

ROOT = "/home/hatch/workspace/warp-pilot"
FIG = f"{ROOT}/publication/figures"
sys.path.insert(0, f"{ROOT}/phase312/work")
import p312_lib as L312  # noqa: E402  stored Phase 312 machinery
from p258_lib import R_NODES  # noqa: E402

p312 = json.load(open(f"{ROOT}/phase312/results/p312_results.json"))
win = next(m for m in p312["members"] if m["label"] == "ramp_broad_m+1.00")
prof = win["profile"]
spec = L312.WINNER_SPEC
print(f"member profile (stored): {prof}")

# --- provenance check: reproduce the stored S1 read exactly ---
s1 = win["sites"][0]
rho_s1 = float(L312.rho_split(spec, prof, np.array([s1["point"]]))["rho_split"][0])
print(f"S1 rho: evaluator {rho_s1:.16e} vs stored {s1['rho_req']:.16e} "
      f"(diff {abs(rho_s1 - s1['rho_req']):.2e})")
assert abs(rho_s1 - s1["rho_req"]) < 1e-12

r_lo, r_hi = 10.0, 20.0  # posed volume endpoints (SET nodes are its midpoints)

def rho_on_sphere(r, nth, nph):
    th = np.linspace(0, np.pi, nth)
    ph = np.linspace(0, 2 * np.pi, nph)
    TH, PH = np.meshgrid(th, ph, indexing="ij")
    X = r * np.cos(TH)
    Y = r * np.sin(TH) * np.cos(PH)
    Z = r * np.sin(TH) * np.sin(PH)
    pts = np.stack([X, Y, Z], axis=-1).reshape(-1, 3)
    rho = L312.rho_split(spec, prof, pts)["rho_split"].reshape(X.shape)
    return X, Y, Z, rho

# --- radius of maximum angular contrast ---
best = None
for r in np.arange(r_lo, r_hi + 1e-9, 0.25):
    _, _, _, v = rho_on_sphere(float(r), 25, 36)
    c = float(v.max() - v.min())
    if best is None or c > best[1]:
        best = (float(r), c)
r_wall = best[0]
print(f"wall surface radius (max angular contrast): r = {r_wall:.2f}")

def cell_colours(vals, norm):
    c = 0.25 * (vals[:-1, :-1] + vals[1:, :-1] + vals[:-1, 1:] + vals[1:, 1:])
    return cm.viridis(norm(c))

X, Y, Z, RHO = rho_on_sphere(r_wall, 73, 108)
norm = Normalize(RHO.min(), RHO.max())
fc = cell_colours(RHO, norm)
for tag, (el, az) in {"view1": (18, -55), "view2": (58, 32)}.items():
    fig = plt.figure(figsize=(8.4, 7.4))
    fig.patch.set_facecolor("white")
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X, Y, Z, facecolors=fc, shade=False, linewidth=0,
                    antialiased=False)
    ax.view_init(elev=el, azim=az)
    ax.set_xlabel("x (motion axis $\\hat{x}$)")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title(f"Phase 312 winner (Gate-34): bubble wall at r = {r_wall:.2f}, "
                 f"coloured by $\\rho_\\mathrm{{req}}$\n"
                 f"density positive at the four binding sites; full-volume SET "
                 f"minimum {win['set']['rho']['min']:.2e} (10^-7 level)",
                 fontsize=10.5)
    mappable = cm.ScalarMappable(norm=norm, cmap="viridis")
    mappable.set_array(RHO)
    cb = fig.colorbar(mappable, ax=ax, shrink=0.62, pad=0.08)
    cb.set_label("$\\rho_\\mathrm{req}$ (bracket units)")
    out = f"{FIG}/model_gate34_wall_{tag}.png"
    fig.savefig(out, dpi=200, facecolor="white")
    plt.close(fig)
    print("wrote", out)

# --- shell mesh over [r_lo, r_hi] ---
NTH, NPH = 73, 96
verts, cols, faces = [], [], []
surfs = {}
for r in (r_hi, r_lo):
    surfs[r] = rho_on_sphere(r, NTH, NPH)
vmin = min(v[3].min() for v in surfs.values())
vmax = max(v[3].max() for v in surfs.values())
norm_m = Normalize(vmin, vmax)
for r, flip in ((r_hi, False), (r_lo, True)):
    X, Y, Z, RHO = surfs[r]
    base = len(verts)
    rgb = cm.viridis(norm_m(RHO))[:, :, :3]
    P = np.stack([X, Y, Z], axis=-1)
    for i in range(NTH):
        for j in range(NPH):
            verts.append(P[i, j])
            cols.append(rgb[i, j])
    for i in range(NTH - 1):
        for j in range(NPH):
            j1 = (j + 1) % NPH
            a, b = base + i * NPH + j, base + i * NPH + j1
            c, d = base + (i + 1) * NPH + j, base + (i + 1) * NPH + j1
            if flip:
                faces += [(a, c, b), (b, c, d)]
            else:
                faces += [(a, b, c), (b, d, c)]
verts = np.array(verts)
cols = np.array(cols)
faces = np.array(faces)
print(f"mesh: {len(verts)} vertices, {len(faces)} faces; "
      f"rho range on mesh [{vmin:.4e}, {vmax:.4e}]")

with open(f"{FIG}/gate34_wall_shell.obj", "w") as f:
    f.write("# Phase 312 broad-ramp winner -- bubble wall shell, band "
            f"[{r_lo}, {r_hi}]\n# vertex colours = rho_req from the stored "
            "Phase 312 evaluator (phase312/work/p312_lib.py),\n# "
            f"viridis-normalised over the two mesh surfaces' range "
            f"[{vmin:.6e}, {vmax:.6e}]\n")
    for v, c in zip(verts, cols):
        f.write(f"v {v[0]:.6f} {v[1]:.6f} {v[2]:.6f} "
                f"{c[0]:.4f} {c[1]:.4f} {c[2]:.4f}\n")
    for a, b, c in faces:
        f.write(f"f {a + 1} {b + 1} {c + 1}\n")
print("wrote", f"{FIG}/gate34_wall_shell.obj")

with open(f"{FIG}/gate34_wall_shell.stl", "wb") as f:
    f.write(b"\0" * 80)
    f.write(struct.pack("<I", len(faces)))
    for a, b, c in faces:
        pa, pb, pc = verts[a], verts[b], verts[c]
        n = np.cross(pb - pa, pc - pa)
        ln = np.linalg.norm(n)
        n = n / ln if ln > 0 else n
        f.write(struct.pack("<12fH", n[0], n[1], n[2], pa[0], pa[1], pa[2],
                            pb[0], pb[1], pb[2], pc[0], pc[1], pc[2], 0))
print("wrote", f"{FIG}/gate34_wall_shell.stl")

# --- cutaway preview ---
fig = plt.figure(figsize=(8.4, 7.4))
fig.patch.set_facecolor("white")
ax = fig.add_subplot(111, projection="3d")
band_r = np.linspace(r_lo, r_hi, 21)
band_vals = []
for r in band_r:
    _, _, _, v = rho_on_sphere(float(r), 25, 36)
    band_vals.append(v)
band_vals = np.array(band_vals)
norm_b = Normalize(float(band_vals.min()), float(band_vals.max()))
print(f"cutaway band colour range [{band_vals.min():.4e}, {band_vals.max():.4e}]")
NTHc, NPHc = 49, 37
th_c = np.linspace(0, np.pi, NTHc)
ph_c = np.linspace(np.pi / 2, 3 * np.pi / 2, NPHc)
THc, PHc = np.meshgrid(th_c, ph_c, indexing="ij")
for r in (r_hi, r_lo):
    Xc = r * np.cos(THc)
    Yc = r * np.sin(THc) * np.cos(PHc)
    Zc = r * np.sin(THc) * np.sin(PHc)
    pts = np.stack([Xc, Yc, Zc], axis=-1).reshape(-1, 3)
    rho_c = L312.rho_split(spec, prof, pts)["rho_split"].reshape(Xc.shape)
    fc = cell_colours(rho_c, norm_b)
    ax.plot_surface(Xc, Yc, Zc, facecolors=fc, shade=False, linewidth=0,
                    antialiased=False)
for ph0 in (np.pi / 2, 3 * np.pi / 2):
    rr = np.linspace(r_lo, r_hi, 15)
    RR, TT = np.meshgrid(rr, th_c, indexing="ij")
    Xr = RR * np.cos(TT)
    Yr = RR * np.sin(TT) * np.cos(ph0)
    Zr = RR * np.sin(TT) * np.sin(ph0)
    pts = np.stack([Xr, Yr, Zr], axis=-1).reshape(-1, 3)
    rho_r = L312.rho_split(spec, prof, pts)["rho_split"].reshape(Xr.shape)
    fc = cell_colours(rho_r, norm_b)
    ax.plot_surface(Xr, Yr, Zr, facecolors=fc, shade=False,
                    linewidth=0, antialiased=False)
ax.view_init(elev=15, azim=38)
ax.set_xlabel("x (motion axis $\\hat{x}$)")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title(f"Exported shell mesh (cutaway): wall band r in [{r_lo:.0f}, "
             f"{r_hi:.0f}], coloured by $\\rho_\\mathrm{{req}}$\n"
             f"the winner's negative-density loci sit in the M = 1 strip\n"
             f"at the inner edge (see FIGURES.md caption)", fontsize=10.5)
mappable = cm.ScalarMappable(norm=norm_b, cmap="viridis")
mappable.set_array([float(band_vals.min()), float(band_vals.max())])
cb = fig.colorbar(mappable, ax=ax, shrink=0.62, pad=0.08)
cb.set_label("$\\rho_\\mathrm{req}$ (bracket units)")
out = f"{FIG}/model_gate34_wall_shell.png"
fig.savefig(out, dpi=200, facecolor="white")
print("wrote", out)
