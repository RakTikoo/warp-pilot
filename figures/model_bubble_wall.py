#!/usr/bin/env python3
"""3D model: the Phase 314 pointwise member's bubble wall, coloured by the
required density rho_req.

Everything is evaluated with the programme's stored Gate-35 evaluator
(gate35/work/g35_rho.py) -- the member's (S, N, M) profiles live in that
stored code and in phase314/results/p314_results.json; the radial band of
the mesh is the Gate-35 certified domain, read from the stored Gate-35
region ranges (gate35-claims/results/g35_item1_results.json). No profile
numbers are typed into this script.

Products:
  model_bubble_wall_view1.png / view2.png  wall surface at the radius of
                                           maximum angular density contrast,
                                           two viewing angles
  model_bubble_wall_shell.png              cutaway of the exported shell mesh
  bubble_wall_shell.obj                    shell mesh with vertex colours
  bubble_wall_shell.stl                    same mesh, binary STL
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
sys.path.insert(0, f"{ROOT}/gate35/work")
import g35_rho  # noqa: E402  stored Gate-35 evaluator

p314 = json.load(open(f"{ROOT}/phase314/results/p314_results.json"))
g35 = json.load(open(f"{ROOT}/gate35-claims/results/g35_item1_results.json"))
prof = p314["headline_member"]["profile"]
regions = g35["floors_d"]["regions"]
r_lo = min(v["range"][0] for v in regions.values())   # certified band, stored
r_hi = max(v["range"][1] for v in regions.values())
gmin = g35["search_c"]["global_min"]
print(f"member profile (stored): {prof}; certified band [{r_lo}, {r_hi}]; "
      f"continuum min {gmin['rho']:.6e} at r={gmin['r']}")

# --- radius of maximum angular contrast, from the stored evaluator ---
us = np.linspace(0, 1, 81)
best = None
for r in np.arange(r_lo, r_hi + 1e-9, 0.05):
    v = g35_rho.rho_ru(float(r), us)
    c = float(v.max() - v.min())
    if best is None or c > best[1]:
        best = (float(r), c)
r_wall = best[0]
print(f"wall surface radius (max angular contrast): r = {r_wall:.2f}, "
      f"contrast {best[1]:.3e}")

def sphere_grid(r, nth, nph):
    """Nodes on a sphere; theta from the +x (motion) axis. Returns X,Y,Z,u."""
    th = np.linspace(0, np.pi, nth)
    ph = np.linspace(0, 2 * np.pi, nph)
    TH, PH = np.meshgrid(th, ph, indexing="ij")
    X = r * np.cos(TH)
    Y = r * np.sin(TH) * np.cos(PH)
    Z = r * np.sin(TH) * np.sin(PH)
    return X, Y, Z, np.cos(TH) ** 2

def cell_colours(vals, norm):
    c = 0.25 * (vals[:-1, :-1] + vals[1:, :-1] + vals[:-1, 1:] + vals[1:, 1:])
    return cm.viridis(norm(c))

# --- renders: wall surface at r_wall, two angles ---
X, Y, Z, U = sphere_grid(r_wall, 97, 145)
RHO = g35_rho.rho_ru(r_wall, U)
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
    ax.set_title(f"Pointwise member: bubble wall at r = {r_wall:.2f}, coloured by "
                 f"$\\rho_\\mathrm{{req}}$\nGate-35 continuum minimum over the volume: "
                 f"{gmin['rho']:.4e} (at r = {gmin['r']:.0f}) — positive throughout",
                 fontsize=10.5)
    mappable = cm.ScalarMappable(norm=norm, cmap="viridis")
    mappable.set_array(RHO)
    cb = fig.colorbar(mappable, ax=ax, shrink=0.62, pad=0.08)
    cb.set_label("$\\rho_\\mathrm{req}$ (bracket units)")
    out = f"{FIG}/model_bubble_wall_{tag}.png"
    fig.savefig(out, dpi=200, facecolor="white")
    plt.close(fig)
    print("wrote", out)

# --- shell mesh over the certified band [r_lo, r_hi] ---
def sphere_nodes(r, nth, nph):
    th = np.linspace(0, np.pi, nth)
    ph = np.linspace(0, 2 * np.pi, nph)
    TH, PH = np.meshgrid(th, ph, indexing="ij")
    P = np.stack([r * np.cos(TH), r * np.sin(TH) * np.cos(PH),
                  r * np.sin(TH) * np.sin(PH)], axis=-1)
    return P, np.cos(TH) ** 2

NTH, NPH = 97, 128
verts, cols, faces = [], [], []
all_rho = {}
for r in (r_hi, r_lo):
    P, U = sphere_nodes(r, NTH, NPH)
    all_rho[r] = g35_rho.rho_ru(r, U)
vmin = min(v.min() for v in all_rho.values())
vmax = max(v.max() for v in all_rho.values())
norm_m = Normalize(vmin, vmax)
for r, flip in ((r_hi, False), (r_lo, True)):
    P, U = sphere_nodes(r, NTH, NPH)
    base = len(verts)
    rgb = cm.viridis(norm_m(all_rho[r]))[:, :, :3]
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
      f"rho range on mesh [{vmin:.4e}, {vmax:.4e}] (all positive)")

with open(f"{FIG}/bubble_wall_shell.obj", "w") as f:
    f.write("# Phase 314 pointwise member -- bubble wall shell, Gate-35 band "
            f"[{r_lo}, {r_hi}]\n# vertex colours = rho_req from the stored "
            "Gate-35 evaluator (gate35/work/g35_rho.py),\n# viridis-normalised "
            f"over the two mesh surfaces' range [{vmin:.6e}, {vmax:.6e}]\n")
    for v, c in zip(verts, cols):
        f.write(f"v {v[0]:.6f} {v[1]:.6f} {v[2]:.6f} "
                f"{c[0]:.4f} {c[1]:.4f} {c[2]:.4f}\n")
    for a, b, c in faces:
        f.write(f"f {a + 1} {b + 1} {c + 1}\n")
print("wrote", f"{FIG}/bubble_wall_shell.obj")

with open(f"{FIG}/bubble_wall_shell.stl", "wb") as f:
    f.write(b"\0" * 80)
    f.write(struct.pack("<I", len(faces)))
    for a, b, c in faces:
        pa, pb, pc = verts[a], verts[b], verts[c]
        n = np.cross(pb - pa, pc - pa)
        ln = np.linalg.norm(n)
        n = n / ln if ln > 0 else n
        f.write(struct.pack("<12fH", n[0], n[1], n[2], pa[0], pa[1], pa[2],
                            pb[0], pb[1], pb[2], pc[0], pc[1], pc[2], 0))
print("wrote", f"{FIG}/bubble_wall_shell.stl")

# --- cutaway preview of the exported shell: the y > 0 half is removed so
# the shell's thickness and inner surface are visible; the two flat rims
# are the cut faces, coloured by rho at the cut plane ---
fig = plt.figure(figsize=(8.4, 7.4))
fig.patch.set_facecolor("white")
ax = fig.add_subplot(111, projection="3d")
# colour scale for the cutaway spans the whole band (the density peak lives
# mid-wall, above both mesh surfaces' values)
_us_b = np.linspace(0, 1, 41)
_band = np.concatenate([g35_rho.rho_ru(float(r), _us_b)
                        for r in np.linspace(r_lo, r_hi, 41)])
norm_b = Normalize(float(_band.min()), float(_band.max()))
print(f"cutaway band colour range [{_band.min():.4e}, {_band.max():.4e}]")
NTHc, NPHc = 65, 49
th_c = np.linspace(0, np.pi, NTHc)
ph_c = np.linspace(np.pi / 2, 3 * np.pi / 2, NPHc)   # y <= 0 half kept
THc, PHc = np.meshgrid(th_c, ph_c, indexing="ij")
Uc = np.cos(THc) ** 2
for r in (r_hi, r_lo):
    Xc = r * np.cos(THc)
    Yc = r * np.sin(THc) * np.cos(PHc)
    Zc = r * np.sin(THc) * np.sin(PHc)
    fc = cell_colours(g35_rho.rho_ru(r, Uc), norm_b)
    ax.plot_surface(Xc, Yc, Zc, facecolors=fc, shade=False, linewidth=0,
                    antialiased=False)
for ph0 in (np.pi / 2, 3 * np.pi / 2):                # cut-face rims
    rr = np.linspace(r_lo, r_hi, 21)
    RR, TT = np.meshgrid(rr, th_c, indexing="ij")
    Xr = RR * np.cos(TT)
    Yr = RR * np.sin(TT) * np.cos(ph0)
    Zr = RR * np.sin(TT) * np.sin(ph0)
    rho_r = np.array([g35_rho.rho_ru(float(a), np.cos(TT[0]) ** 2)
                      for a in rr])
    fc = cell_colours(rho_r, norm_b)
    ax.plot_surface(Xr, Yr, Zr, facecolors=fc, shade=False,
                    linewidth=0, antialiased=False)
ax.view_init(elev=15, azim=38)
ax.set_xlabel("x (motion axis $\\hat{x}$)")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title(f"Exported shell mesh (cutaway): wall band r ∈ [{r_lo:.0f}, {r_hi:.0f}], "
             f"coloured by $\\rho_\\mathrm{{req}}$\nGate-35 continuum minimum "
             f"{gmin['rho']:.4e} — density positive throughout the band",
             fontsize=10.5)
mappable = cm.ScalarMappable(norm=norm_b, cmap="viridis")
mappable.set_array([float(_band.min()), float(_band.max())])
cb = fig.colorbar(mappable, ax=ax, shrink=0.62, pad=0.08)
cb.set_label("$\\rho_\\mathrm{req}$ (bracket units)")
out = f"{FIG}/model_bubble_wall_shell.png"
fig.savefig(out, dpi=200, facecolor="white")
print("wrote", out)
