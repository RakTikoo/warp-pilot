"""p91_chain.py — P9-1 moving-shell remainder chain (steps a,b,c).

Pre-registration: CHECKPOINT9.md P9-1 (bars fixed there, not altered).
float64, system python3.

STEP (a) build (i): PG embedding with TOTAL lapse consistent with
the superposed shift.  Construction:
  W_tot(x)  = W_bg^exact(x) - bGP_sh(r_rel) n_rel   [as P8-2 local]
  Phi_tot   = Phi_bg(r_bg) + a_sh(r_rel)            [areal total lapse
              function of the clean P8-2 areal two-centre metric]
  alpha_tot = sqrt( exp(2 Phi_tot) + |W_tot|^2 )
  gamma = delta,  g_ti = W_tot,i,  g_tt = -alpha_tot^2 + |W_tot|^2
              = -exp(2 Phi_tot)  (areal g_tt reproduced exactly).
Consistency checks built in: shell off -> alpha_tot = 1 exactly
(PG Schwarzschild); background off -> alpha_tot^2 = e^{2a}/u_sh,
i.e. the exact single-centre GP transform of the isolated shell
(P8-2's shell-only lapse is recovered ONLY in that limit; at two
centres P8-2 used that shell-only lapse over the superposed shift,
which is the inconsistency removed here).
Build (ii) note: an exact areal->PG coordinate transform would need
a time reparam t -> t - F(x) with gamma_areal - delta =
e^{2Phi} gradF x gradF (rank 1); the two-centre areal gamma-delta is
the sum of TWO rank-1 terms along n_bg and n_rel, which are not
parallel off-axis, so no such F exists globally — build (i) is the
route taken; (ii) is obstructed as an exact flat-slice transform.

STEP (b): edge-resolved audit, h to 0.025 in the edge band, plus an
exact isolated shell audited with the identical stencil/points.
STEP (c): beta=0.02 cosine window, centre moving (xc = d zhat +
beta t xhat), genuinely time-dependent, audited at t=0 with the
Phase-7 non-stationary auditor, in BOTH slicings (PG-consistent and
areal two-centre with the same moving centre + window component).
"""
import json
import sys
import time

import numpy as np
from scipy.interpolate import CubicSpline

sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase5')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase7')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase8')
import shell as sh                  # noqa: E402
import h4_resolved_shell as h4      # noqa: E402
from p74_auditor import einstein_at_points_td, wrap_stationary  # noqa: E402
import p82_areal as areal_mod       # noqa: E402  (builder reuse)

DTYPE = np.float64
EIGHT_PI = 8.0 * np.pi
M_BG = 1.0
DS = (50.0, 100.0)
XHAT = np.array([1.0, 0.0, 0.0])
ZHAT = np.array([0.0, 0.0, 1.0])
OUT = '/home/hatch/workspace/warp-pilot/phase9/results/p91_chain.json'

out = {'task': 'P9-1 remainder chain', 'python': sys.version,
       'numpy': np.__version__, 'gate': {}, 'edge': {}, 'moving': {},
       'controls': {}}


def save():
    with open(OUT, 'w') as f:
        json.dump(out, f, indent=1, default=float)


def region_dict(That, pts_rel):
    rm = h4.region_margins(That, pts_rel)
    d = {}
    for reg, entry in rm['regions'].items():
        raw = entry['raw']
        d[reg] = None if raw is None else {
            'nec': raw['nec'], 'worst': raw['worst'],
            'typeI_frac': raw['typeI_frac'], 'nec_r': raw['nec_r']}
    return d


# ---------------------------------------------------------------------------
prof_flat = h4.solve_in_background(('flat',), shell_on=True)
prof_off = h4.solve_in_background(('flat',), shell_on=False)
_rg = prof_flat['r']
_ash = CubicSpline(_rg, prof_flat['a_sh'])
_msh = CubicSpline(_rg, prof_flat['m_sh'])
_rmax = float(_rg[-1])
print(f"flat solve s={prof_flat['s']:.4f} core1d NEC="
      f"{prof_flat['static1d_core']['nec']:+.3e}")


def pg_fields(pts, xc, shell_on=True, bg_on=True):
    pts = np.asarray(pts, dtype=DTYPE)
    P = len(pts)
    if bg_on:
        r_bg = np.linalg.norm(pts, axis=1)
        rs_bg = np.where(r_bg > 0, r_bg, 1.0)
        n_bg = pts / rs_bg[:, None]
        u_bg = np.maximum(1.0 - 2.0 * M_BG / rs_bg, 1e-12)
        Phi_bg = 0.5 * np.log(u_bg)
        W_bg = -np.sqrt(2.0 * M_BG / rs_bg)[:, None] * n_bg
    else:
        Phi_bg = np.zeros(P); W_bg = np.zeros((P, 3))
        u_bg = np.ones(P)
    rel = pts - xc[None, :]
    r_rel = np.linalg.norm(rel, axis=1)
    rs_rel = np.where(r_rel > 0, r_rel, 1.0)
    n_rel = rel / rs_rel[:, None]
    if shell_on:
        rc = np.clip(r_rel, 0.0, _rmax)
        ash = _ash(rc); m_sh = _msh(rc)
        u_sh = np.maximum(1.0 - 2.0 * m_sh / np.maximum(rc, 1e-9), 1e-9)
        bGP = np.exp(ash) * np.sqrt(np.maximum(1.0 - u_sh, 0.0)) / np.sqrt(u_sh)
    else:
        ash = np.zeros(P); bGP = np.zeros(P)
    Phi_tot = Phi_bg + ash
    W = W_bg - bGP[:, None] * n_rel
    alpha = np.sqrt(np.exp(2.0 * Phi_tot) + np.sum(W ** 2, axis=1))
    return alpha, W, Phi_tot, r_rel


def make_pg(beta=0.0, d=50.0, shell_on=True, bg_on=True, moving=True):
    centre0 = d * ZHAT if bg_on else np.zeros(3)

    def gtfunc(t, pts):
        pts = np.asarray(pts, dtype=DTYPE)
        P = len(pts)
        xc = centre0 + (beta * t * XHAT if moving else 0.0)
        alpha, W, _, r_rel = pg_fields(pts, xc, shell_on, bg_on)
        if beta != 0.0:
            S = sh.shift_S(r_rel, h4.R1, h4.R2, 'cos', 1.0, [h4.R1, h4.R2])
            W = W - (S * beta)[:, None] * XHAT[None, :]
            alpha = np.sqrt(alpha ** 2 + 0.0)  # lapse unchanged by window ansatz
        g = np.zeros((P, 4, 4), dtype=DTYPE)
        g[:, 0, 0] = -alpha ** 2 + np.sum(W ** 2, axis=1)
        g[:, 0, 1:] = W; g[:, 1:, 0] = W
        for i in range(3):
            g[:, i + 1, i + 1] = 1.0
        return g
    return gtfunc


def make_areal_moving(beta=0.0, d=50.0):
    """Areal two-centre (p82_areal builder, prof_flat) with moving
    centre + cosine window component g_tx = -S*beta."""
    ash_s = CubicSpline(_rg, prof_flat['a_sh'])
    msh_s = CubicSpline(_rg, prof_flat['m_sh'])
    centre0 = d * ZHAT

    def gtfunc(t, pts):
        pts = np.asarray(pts, dtype=DTYPE)
        P = len(pts)
        xc = centre0 + beta * t * XHAT
        r_bg = np.linalg.norm(pts, axis=1)
        rs_bg = np.where(r_bg > 0, r_bg, 1.0)
        n_bg = pts / rs_bg[:, None]
        rel = pts - xc[None, :]
        r_rel = np.linalg.norm(rel, axis=1)
        rs_rel = np.where(r_rel > 0, r_rel, 1.0)
        n_rel = rel / rs_rel[:, None]
        Phi_bg = 0.5 * np.log(np.maximum(1.0 - 2.0 * M_BG / rs_bg, 1e-12))
        rc = np.clip(r_rel, 0.0, _rmax)
        Phi = Phi_bg + ash_s(rc)
        m_sh = msh_s(rc)
        eb_sh = 1.0 / np.maximum(1.0 - 2.0 * m_sh / rs_rel, 1e-9) - 1.0
        eb_bg = 1.0 / np.maximum(1.0 - 2.0 * M_BG / rs_bg, 1e-12) - 1.0
        g = np.zeros((P, 4, 4), dtype=DTYPE)
        g[:, 0, 0] = -np.exp(2.0 * Phi)
        gam = np.eye(3)[None] + eb_bg[:, None, None] * n_bg[:, :, None] * n_bg[:, None, :] \
            + eb_sh[:, None, None] * n_rel[:, :, None] * n_rel[:, None, :]
        g[:, 1:, 1:] = gam
        if beta != 0.0:
            S = sh.shift_S(r_rel, h4.R1, h4.R2, 'cos', 1.0, [h4.R1, h4.R2])
            g[:, 0, 1] = g[:, 1, 0] = -S * beta
        return g
    return gtfunc


def binding_decomp(That_pt, n_dir=4000):
    rng = np.random.default_rng(7)
    dd = rng.normal(size=(n_dir, 3)); dd /= np.linalg.norm(dd, axis=1)[:, None]
    T00 = That_pt[0, 0]; T0i = That_pt[0, 1:]; Tij = That_pt[1:, 1:]
    quad = np.einsum('njk,ij,ik->ni', Tij[None], dd, dd)[0]
    vals = T00 + 2.0 * (dd @ T0i) + quad
    j = int(np.argmin(vals))
    return {'nec_sampled': float(vals[j]), 'dir': dd[j].tolist(),
            'rho_term': float(T00), 'flux_term': float(2.0 * dd[j] @ T0i),
            'stress_term': float(quad[j])}


def audit_full(gt, pts, pts_rel, h, ht=None):
    _, That, margins = einstein_at_points_td(gt, 0.0, pts, h=h, ht=h if ht is None else ht)
    return That, margins, region_dict(That, pts_rel)


# ===========================================================================
t0 = time.time()
pts_rel = h4.sample_points(3.5)
rad_rel = np.linalg.norm(pts_rel, axis=1)

# ---- consistency identities (analytic, evaluated numerically) -------------
chk_pts = pts_rel + (50.0 * ZHAT)[None, :]
a_off, W_off, _, _ = pg_fields(chk_pts, 50.0 * ZHAT, shell_on=False, bg_on=True)
a_iso, W_iso, _, _ = pg_fields(chk_pts, 50.0 * ZHAT, shell_on=True, bg_on=False)
rc_ = np.clip(rad_rel, 0.0, _rmax)
u_sh_ = np.maximum(1.0 - 2.0 * _msh(rc_) / np.maximum(rc_, 1e-9), 1e-9)
alpha_iso_exact = np.exp(_ash(rc_)) / np.sqrt(u_sh_)
out['controls']['lapse_identities'] = {
    'shell_off_alpha_minus_1_max': float(np.max(np.abs(a_off - 1.0))),
    'bg_off_alpha_vs_exact_GP_max_err': float(np.max(np.abs(a_iso - alpha_iso_exact)))}
print('lapse identities:', out['controls']['lapse_identities'])

# ---- STEP (a) GATE: PG-consistent beta=0 vs areal record -------------------
AREAL = {50.0: {'cavity': -1.4252e-8, 'core': 4.5670849e-05},
         100.0: {'cavity': -1.4412e-8, 'core': 4.6281659e-05}}
for d in DS:
    key = f'd={d:g}'
    pts = pts_rel + (d * ZHAT)[None, :]
    # bg-only control
    gt_bg = make_pg(0.0, d, shell_on=False)
    G, _, _ = einstein_at_points_td(gt_bg, 0.0, pts, h=0.1, ht=0.1)
    out['controls'][key] = {'pg_bg_only_max_abs_T_h0.1':
                            float(np.max(np.abs(G)) / EIGHT_PI)}
    print(f"[ctrl {key}] PG bg-only max|T| h=0.1: {out['controls'][key]['pg_bg_only_max_abs_T_h0.1']:.2e}")
    gt = make_pg(0.0, d)
    row = {}
    for h in (0.3, 0.2, 0.1):
        _, _, regs = audit_full(gt, pts, pts_rel, h)
        row[f'h={h}'] = regs
        print(f"[PGcons {key}] h={h}: cavity NEC={regs['cavity']['nec']:+.4e} "
              f"(r={regs['cavity']['nec_r']:.2f}) core NEC={regs['core']['nec']:+.4e} "
              f"coreTypeI={regs['core']['typeI_frac']:.3f} taper={regs['taper']['nec']:+.3e} "
              f"ext={regs['exterior']['nec']:+.3e}")
    r01 = row['h=0.1']
    row['gate_vs_areal_record'] = {
        'areal_cavity_nec': AREAL[d]['cavity'], 'areal_core_nec': AREAL[d]['core'],
        'cavity_at_FD_floor': bool(abs(r01['cavity']['nec']) <= 5e-7),
        'core_within_20pct_of_areal': bool(abs(r01['core']['nec'] - AREAL[d]['core'])
                                           <= 0.2 * AREAL[d]['core']),
        'core_typeI_gt_0.99': bool(r01['core']['typeI_frac'] > 0.99)}
    out['gate'][key] = row
    save()

# ---- STEP (b) EDGE-RESOLVED AUDIT ------------------------------------------
dirs = h4.fib_dirs(26)
edge_rad = np.linspace(7.5, 9.2, 18)
edge_rel = np.concatenate([dirs * rr for rr in edge_rad]).astype(DTYPE)
edge_r = np.linalg.norm(edge_rel, axis=1)


def edge_stats(gt, pts, h):
    _, _, margins = einstein_at_points_td(gt, 0.0, pts, h=h, ht=h)
    nec = margins['nec']
    cav = edge_r < 9.0
    interior = edge_r <= 8.41
    at89 = np.isclose(edge_r, 8.9, atol=0.051)
    return {'cavity_worst_nec': float(np.min(nec[cav])),
            'interior_r<=8.41_worst_nec': float(np.min(nec[interior])),
            'edge_r8.9_worst_nec': float(np.min(nec[at89])),
            'cavity_typeI_frac': float(np.mean(margins['typeI'][cav]))}


for d in DS:
    key = f'd={d:g}'
    pts_e = edge_rel + (d * ZHAT)[None, :]
    builders = {'areal': wrap_stationary(areal_mod.make_areal_gfunc(prof_flat, d, shell_on=True)),
                'pg_consistent': make_pg(0.0, d)}
    if d == 50.0:
        builders['pg_isolated_exact'] = make_pg(0.0, d, bg_on=False)
    erow = {}
    for name, gt in builders.items():
        erow[name] = {}
        for h in (0.1, 0.05, 0.025):
            st = edge_stats(gt, pts_e, h)
            erow[name][f'h={h}'] = st
            print(f"[EDGE {key} {name}] h={h}: cav={st['cavity_worst_nec']:+.4e} "
                  f"int={st['interior_r<=8.41_worst_nec']:+.4e} "
                  f"@8.9={st['edge_r8.9_worst_nec']:+.4e}")
    out['edge'][key] = erow
    save()

# ---- STEP (c) BETA=0.02 WINDOW TEST ----------------------------------------
for d in DS:
    key = f'd={d:g}'
    pts = pts_rel + (d * ZHAT)[None, :]
    mrow = {}
    for name, gt in (('pg_consistent', make_pg(0.02, d)),
                     ('areal', make_areal_moving(0.02, d))):
        srow = {}
        That01 = marg01 = None
        for h in (0.2, 0.1):
            That, margins, regs = audit_full(gt, pts, pts_rel, h)
            srow[f'h={h}'] = regs
            print(f"[MOVE {key} {name}] h={h}: cavity NEC={regs['cavity']['nec']:+.4e} "
                  f"(r={regs['cavity']['nec_r']:.2f}) core NEC={regs['core']['nec']:+.4e} "
                  f"coreTypeI={regs['core']['typeI_frac']:.3f} taper={regs['taper']['nec']:+.3e} "
                  f"ext={regs['exterior']['nec']:+.3e}")
            if h == 0.1:
                That01, marg01 = That, margins
        # anatomy at binding cavity point (h=0.1)
        nec = marg01['nec'].copy()
        cav_mask = rad_rel < h4.S_LO
        nec_m = nec.copy(); nec_m[~cav_mask] = np.inf
        j = int(np.argmin(nec_m))
        Tp = That01[j]
        srow['anatomy_h0.1'] = {
            'r_rel': float(rad_rel[j]), 'nec': float(nec[j]),
            'typeI': bool(marg01['typeI'][j]),
            'rho_euler': float(Tp[0, 0]), 'T0i': Tp[0, 1:].tolist(),
            'stress_eigs': np.linalg.eigvalsh(Tp[1:, 1:]).tolist(),
            'binding': binding_decomp(Tp),
            'cavity_interior_r<=8.41_nec': float(np.min(nec[cav_mask & (rad_rel <= 8.41)]))}
        mrow[name] = srow
    out['moving'][key] = mrow
    save()

out['runtime_s'] = time.time() - t0
save()
print(f"wrote {OUT} in {out['runtime_s']:.0f}s")
