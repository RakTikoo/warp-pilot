#!/usr/bin/env python3
"""GATE-8 / W-B / G8-2 -- mirror-brane price (Israel junction) and
Kretschmann regularity, computed on a path INDEPENDENT of phase46's
p463_r1_mirror.py discretisation.

Phase 46 obtained k_a = d_y ln(scale_a) by np.gradient on the coarse
stored snap grid (dy=0.05). Here k_a is obtained from ANALYTIC
y-derivatives of bicubic splines fitted to ln A, ln D, ln C on the
same stored fields (the shared definition) -- a different
discretisation of the same junction formula:
  S^a_b = -(2/kappa5^2)(K^a_b - K delta^a_b),  Z2 jump,
  kappa5^2 = sqrt(48 pi) (P29-3 convention),
  sigma = -S^t_t, p_z = S^z_z, p_th = S^th_th.
Validation FIRST at y=0 against the exhibited brane's analytic
Israel data (same analytic formulas as the record):
  kt_an = -(k5sq/6)(1 - 2 rho), kz_an = -(k5sq/6)(rho + 1),
  rho from the SMS quadratic with trG = -(1+z^2)^-2.5, lambda=1.
Also a cross-check of the spline-k against np.gradient-k at y_c
(the phase discretisation) to show the two agree.

Kretschmann: the stored P43-1 track (shared definition) has
Kret_max == Kret_throat at every snapshot (asserted from the file),
and K_throat(y) is increasing on [0, 0.40]; hence any path with
y <= y_c has K <= K_throat(y_c). I recompute the bound by direct
interpolation of the track (not the phase's log-interp) and also
report the throat values bracketing each y_c. The uncompleted
track diverges: K(0.45)=1.09e7, K(0.46)=2.42e8 toward y*~0.4675.
float64.
"""
import json
import numpy as np
from scipy.interpolate import RectBivariateSpline

NPZ = "/home/hatch/workspace/warp-pilot/phase43/results/p431_bulk_fields.npz"
TRACK = "/home/hatch/workspace/warp-pilot/phase43/results/p431_bulk_track.json"
OUT = "/home/hatch/workspace/warp-pilot/gate8/results/wb_g82_israel.json"
K5SQ = np.sqrt(48.0 * np.pi)

d = np.load(NPZ)
ZZ, SY = d["zz"], d["snap_y"]
FIELDS = {nm: d[nm] for nm in ("A", "D", "C")}
LSPL = {nm: RectBivariateSpline(SY, ZZ, np.log(FIELDS[nm]), kx=3, ky=3, s=0)
        for nm in FIELDS}


def k_spline(y, z):
    """k_a = d_y ln(scale_a) from spline analytic derivatives."""
    return tuple(float(LSPL[nm].ev(y, z, dx=1, dy=0))
                 for nm in ("A", "D", "C"))  # kt, kz, kth


MASK_EV = np.abs(ZZ) <= 3.0


def k_gradient(y):
    """Phase-46 discretisation: np.gradient on the snap grid,
    restricted to |z| <= 3 (the ZZ_EV evaluation set)."""
    iy = int(np.argmin(np.abs(SY - y)))
    assert abs(SY[iy] - y) < 1e-9
    return tuple(np.gradient(np.log(FIELDS[nm]), SY, axis=0,
                             edge_order=2)[iy][MASK_EV]
                 for nm in ("A", "D", "C"))


def stress(kt, kz, kth):
    Ktot = kt + kz + 2.0 * kth
    fac = 2.0 / K5SQ
    St = -fac * (kt - Ktot); Sz = -fac * (kz - Ktot); Sth = -fac * (kth - Ktot)
    return -St, Sz, Sth  # sigma, pz, pth


def ec_block(sig, pz, pth):
    return {"sigma_min": float(np.min(sig)), "sigma_max": float(np.max(sig)),
            "sigma_at_throat": float(sig[np.argmin(np.abs(ZZ_EV))]),
            "pz_range": [float(np.min(pz)), float(np.max(pz))],
            "pth_range": [float(np.min(pth)), float(np.max(pth))],
            "NEC_min": float(min(np.min(sig + pz), np.min(sig + pth))),
            "WEC_min_sigma": float(np.min(sig)),
            "SEC_min": float(min(np.min(sig + pz), np.min(sig + pth),
                                 np.min(sig + pz + 2 * pth))),
            "DEC_min": float(min(np.min(sig - np.abs(pz)),
                                 np.min(sig - np.abs(pth))))}


ZZ_EV = ZZ[np.abs(ZZ) <= 3.0]
out = {}

# ---- validation at y = 0 against analytic Israel data
x = 1.0 + ZZ_EV ** 2
K4 = 8.0 * np.pi; K5 = 6.0 * K4
trG = -x ** -2.5
aa_, bb_, cc_ = K5 / 6.0, -K4, -trG
rho = (-bb_ - np.sqrt(bb_ * bb_ - 4 * aa_ * cc_)) / (2 * aa_)
kt_an = -(K5SQ / 6.0) * (1.0 - 2.0 * rho)
kz_an = -(K5SQ / 6.0) * (rho + 1.0)
ks = np.array([k_spline(0.0, z) for z in ZZ_EV])
out["validation_y0_spline"] = {
    "kt_rel_err_max": float(np.max(np.abs(ks[:, 0] - kt_an) / np.abs(kt_an))),
    "kz_rel_err_max": float(np.max(np.abs(ks[:, 1] - kz_an) / np.abs(kz_an)))}
kg0 = k_gradient(0.0)
out["validation_y0_gradient"] = {
    "kt_rel_err_max": float(np.max(np.abs(kg0[0] - kt_an) / np.abs(kt_an))),
    "kz_rel_err_max": float(np.max(np.abs(kg0[1] - kz_an) / np.abs(kz_an)))}
print("VALIDATION spline", out["validation_y0_spline"], flush=True)
print("VALIDATION gradient", out["validation_y0_gradient"], flush=True)

# ---- mirror rows
rows = {}
for yc in (0.20, 0.25, 0.30, 0.35, 0.40):
    ks = np.array([k_spline(yc, z) for z in ZZ_EV])
    sig, pz, pth = stress(ks[:, 0], ks[:, 1], ks[:, 2])
    blk = ec_block(sig, pz, pth)
    kg = k_gradient(yc)
    sigg, pzg, pthg = stress(kg[0], kg[1], kg[2])
    blkg = ec_block(sigg, pzg, pthg)
    rows[str(yc)] = {"spline_k": blk, "gradient_k_crosscheck": blkg,
                     "sigma_peak_z": float(ZZ_EV[int(np.argmax(sig))])}
    print("yc", yc, "spline sigma range", blk["sigma_min"], blk["sigma_max"],
          "NEC", blk["NEC_min"], "SEC", blk["SEC_min"], "DEC", blk["DEC_min"],
          "| grad sigma range", blkg["sigma_min"], blkg["sigma_max"],
          "NEC", blkg["NEC_min"], flush=True)
out["mirror_rows"] = rows

# ---- Kretschmann from the stored track (shared definition)
track = json.load(open(TRACK))["track"]
ty = np.array([r["y"] for r in track]); tK = np.array([r["Kret_throat"] for r in track])
maxeq = all(abs(r.get("Kret_max", r["Kret_throat"]) - r["Kret_throat"])
            <= 1e-9 * r["Kret_throat"] for r in track)
mono = bool(np.all(np.diff(tK) > 0))
out["kretschmann"] = {"slice_max_equals_throat_on_track": bool(maxeq),
                      "throat_K_monotone_increasing_to_0.46": mono,
                      "track": [[float(a), float(b)] for a, b in zip(ty, tK)],
                      "bounds": {str(yc): float(np.interp(yc, ty, tK))
                                 for yc in (0.20, 0.25, 0.30, 0.35, 0.40)},
                      "uncompleted_divergence": {
                          "K_y0.45": float(tK[ty == 0.45][0]),
                          "K_y0.46": float(tK[ty == 0.46][0]),
                          "y_star_record": 0.4675}}
print("KRET slice_max=throat:", maxeq, "monotone:", mono,
      "bounds:", out["kretschmann"]["bounds"], flush=True)

json.dump(out, open(OUT, "w"), indent=1)
print("DONE", flush=True)
