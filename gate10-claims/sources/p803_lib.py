"""
p803_lib.py — P80-3 SOURCE-MODULATED COMPOSITION shared library.
Python: programme venv ~/workspace/warp-pilot/venv/bin/python, float64.

MACHINERY ROUTE (recorded): REUSE of Phase 73's P73-1 source-space
machinery (phase73/p731_lib.py chain algebra, itself the registered
adaptation of phase50/p501_recon.py lines 100-140), generalised from
P73-1's single (10,30) shell to an arbitrary shell profile:
  per shell s with support [R1s,R2s], width Ws=R2s-R1s:
    chain grid r in [0, hi+1], dr=2.5e-4, r_m inserted exactly,
    hi = R2s + 0.3*Ws, lo = R1s - 0.3*Ws (P73-1 EXTENDED-domain rule:
    primary domain failed its endpoint read, extended is the
    construction; knots [lo,lo,lo, linspace(lo,hi,10), hi,hi,hi]);
    rhohat = rho_s(r)/max(rho_s) from the shell profile's own
    rho_trial (CubicSpline), clipped >= 0;
    g0 = rhohat^q * tanh((r_m-r)/0.05) * exp(sum_i a_i B_i(r));
    lambda = -I_in/I_out (balance); F cumulative, reset past r_m;
    S_s(r) = 1 - k * int(F/s^2) ds, k = 1/int(F/s^2). Nothing clipped.
  design vector per shell: 14 numbers (12 a_i, q, r_m) — the
  procaccia_anatomy.md 14-number pattern.

COMPOSITION (Phase 46 P46-2 / phase41 p413 pattern, unchanged):
  backgrounds: frontier class — outer (5,10) M=1.9125 edgepeaked
  wd=1.0/floor=0.1 s_rho=1.0 s_P=0.58; inner (2,4) M=0.765 x0.4 copy
  (wd=0.4, s_rho=0.4, s_P=0.232) — TOV profiles from shell.build_shell;
  composed background via p413 build_composed (m_comp = m_i + m_o;
  outer TOV re-integrated against m_comp; a_comp integrated inward).
  staircase shift V(r) = beta_o * S_o(r) + beta_i * S_i(r)
  (payload beta_o+beta_i inside the inner shell, beta_o in the
  cavity, 0 outside — the P41-3 staircase with each cosine window
  replaced by that shell's source-modulated S).
  HELD SHIFTS (CHECKPOINT80 §P80-3: both shells' shifts held at
  their alone values, P46-2 protocol): for shell s,
    beta_s^comp = beta_s^alone * exp(a_comp(r_mid,s) - a_alone,s(r_mid,s))
  so W_s = beta_s^comp * exp(-a_comp(r_mid,s)) equals the alone
  characteristic orthonormal shift W_s^alone =
  beta_s^alone * exp(-a_alone,s(r_mid,s)) exactly (to fp).
AUDIT: gate-standard wa_auditor (direct-d2 FD, dGamma algebraic)
PRIMARY; Phase-1 judge + wa_diag 4th-order as second paths.
"""
import sys
import numpy as np
from scipy.interpolate import BSpline, CubicSpline
from scipy.integrate import cumulative_trapezoid

sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase41')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate6')
import shell as sh
import wa_auditor as wa
from p413_audit import build_composed, audit_points, region_of, fib_dirs

DTYPE = np.float64
W_SWITCH = DTYPE(0.05)
DR = DTYPE(2.5e-4)
KINDS = ('nec', 'wec', 'sec', 'dec')


def frontier_outer():
    return sh.build_shell(5.0, 10.0, 1.9125, kind='edgepeaked',
                          params={'wd': 1.0, 'floor': 0.1},
                          s_rho=1.0, s_P=0.58, Nr=4001)


def frontier_inner():
    return sh.build_shell(2.0, 4.0, 0.765, kind='edgepeaked',
                          params={'wd': 0.4, 'floor': 0.1},
                          s_rho=0.4, s_P=0.232, Nr=4001)


# ---------------------------------------------------------------- chain
def shell_span(prof):
    W = prof['R2'] - prof['R1']
    return prof['R1'] - 0.3 * W, prof['R2'] + 0.3 * W


def chain(prof, x, dr=None):
    """Source->flux->shift chain for one shell profile (P73-1 pattern).
    dr defaults to the registered 2.5e-4; a coarser dr is used ONLY
    inside the screening objective (S is a double integral of a smooth
    source; the verdict factories always use the default)."""
    if dr is None:
        dr = DR
    x = np.asarray(x, dtype=DTYPE)
    a_i, q, r_m = x[:12], DTYPE(x[12]), DTYPE(x[13])
    lo, hi = shell_span(prof)
    rmax = hi + 1.0
    r = np.arange(0.0, rmax + 1e-12, float(dr), dtype=DTYPE)
    if not np.any(r == r_m):
        r = np.unique(np.sort(np.r_[r, r_m]))
    rho_s = CubicSpline(prof['r'], prof['rho_trial'])
    rho_max = float(np.max(prof['rho_trial']))
    rhohat = np.maximum(rho_s(r), 0.0) / rho_max
    knots = np.r_[[lo] * 3, np.linspace(lo, hi, 10), [hi] * 3]
    rc = np.clip(r, lo, hi)
    B = np.array([BSpline(knots, np.eye(12)[i], 3, extrapolate=False)(rc)
                  for i in range(12)])
    B = np.nan_to_num(B)
    g0 = (rhohat ** q) * np.tanh((r_m - r) / W_SWITCH) * np.exp(a_i @ B)
    u = g0 * r ** 2
    i_m = int(np.searchsorted(r, r_m))
    I_in = float(np.trapezoid(u[:i_m + 1], r[:i_m + 1]))
    I_out = float(np.trapezoid(u[i_m:], r[i_m:]))
    lam = -I_in / I_out
    g = np.where(r < r_m, g0, lam * g0)
    Fcum = cumulative_trapezoid(g * r ** 2, r, initial=0.0)
    F = np.where(r <= r_m, Fcum, Fcum - Fcum[-1])
    with np.errstate(divide='ignore', invalid='ignore'):
        Fr2 = np.where(r > 0, F / r ** 2, 0.0)
    I = cumulative_trapezoid(Fr2, r, initial=0.0)
    k = 1.0 / float(I[-1])
    S = 1.0 - k * I
    bal = float(np.trapezoid(g * r ** 2, r))
    bal_ref = float(np.trapezoid(np.abs(g) * r ** 2, r))
    seg = (r >= lo) & (r <= hi)
    dS = np.diff(S[seg])
    return {'r': r, 'S': S, 'g': g, 'F': F, 'lam': float(lam), 'k': float(k),
            'S_lo_minus1': float(S[np.argmin(np.abs(r - lo))] - 1.0),
            'S_hi': float(S[np.argmin(np.abs(r - hi))]),
            'lo': float(lo), 'hi': float(hi), 'rmax': float(rmax),
            'balance_rel': abs(bal) / bal_ref,
            'monotone_violation': float(max(0.0, dS.max())) if len(dS) else 0.0,
            'rho_max': rho_max}


def S_spline(prof, x, dr=None):
    ch = chain(prof, x, dr=dr)
    return CubicSpline(ch['r'], ch['S']), ch


class FastAloneObjective:
    """Clone-algebra screening objective for one shell alone
    (p731_lib.SourceObjective pattern): static metric parts at the 19
    FD offsets precomputed once; per evaluation only g_ti changes.
    Points: the audit set restricted to r in [R1-1, R2+1] (the region
    the shift acts on). Score: two-number instrument (eigenvalue
    worst margin at Type-I points, sampled NEC at non-Type-I points,
    minned over all four ECs). SCREENING ONLY."""

    def __init__(self, prof, beta, pts, h=0.3):
        sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase50')
        import p503_lib as L
        self._L = L
        self.prof = prof; self.beta = beta; self.h = h
        self.pts = np.asarray(pts, dtype=DTYPE)
        a_s = CubicSpline(prof['r'], prof['a'])
        b_s = CubicSpline(prof['r'], prof['b'])
        rmax = prof['r'][-1]
        self.gstatic = []; self.roff = []
        for off in L.OFFSETS19:
            pp = self.pts + h * np.array(off, dtype=DTYPE)
            r = np.sqrt(np.sum(pp ** 2, axis=1))
            rc = np.clip(r, 0.0, rmax)
            a = a_s(rc); b = b_s(rc)
            P = pp.shape[0]
            g = np.zeros((P, 4, 4), dtype=DTYPE)
            g[:, 0, 0] = -np.exp(2 * a)
            eb = np.exp(2 * b) - 1.0
            rsafe = np.where(r > 0, r, 1.0)
            n = pp / rsafe[:, None]
            for i in range(3):
                for j in range(3):
                    g[:, 1 + i, 1 + j] = eb * n[:, i] * n[:, j]
                g[:, 1 + i, 1 + i] += 1.0
            self.gstatic.append(g); self.roff.append(r)

    def __call__(self, x):
        spl, ch = S_spline(self.prof, x, dr=DTYPE(2e-3))
        gd = {}
        for idx, off in enumerate(self._L.OFFSETS19):
            r = self.roff[idx]
            S = spl(np.clip(r, 0.0, ch['rmax']))
            g = self.gstatic[idx].copy()
            g[:, 0, 1] = g[:, 1, 0] = -S * self.beta
            gd[off] = g
        G, g0 = self._L.einstein_from_gdict(gd, self.h)
        That = wa.eulerian_that(g0, G / wa.EIGHT_PI)
        m = wa.margins_from_that(That)
        m['sampled_nec'] = wa.sampled_nec_min(That)
        scale = np.max(np.abs(That), axis=(1, 2))
        rho_peak = float(np.max(That[:, 0, 0]))
        thr = max(1e-9 * (10.0 / self.prof['R1']) ** 2, 1e-3 * abs(rho_peak))
        sig = scale > thr
        if not np.any(sig):
            return -1e-3
        w = np.where(m['typeI'], m['nec'], m['sampled_nec']).copy()
        for kk in ('wec', 'sec', 'dec'):
            w = np.minimum(w, np.where(m['typeI'], m[kk], m['sampled_nec']))
        return float(np.min(w[sig]))


def bounds_for(prof):
    lo, hi = shell_span(prof)
    return [(-2.0, 2.0)] * 12 + [(0.5, 3.0), (lo + 0.25, hi - 0.25)]


def zero_start(prof):
    lo, hi = shell_span(prof)
    return np.array([0.0] * 12 + [1.47837873, 0.5 * (lo + hi)], dtype=DTYPE)


# ---------------------------------------------------------------- factories
def alone_gfunc(prof, beta, x):
    """Single shell, source-modulated shift S(r)*beta."""
    a_s = CubicSpline(prof['r'], prof['a'])
    b_s = CubicSpline(prof['r'], prof['b'])
    rmax_prof = prof['r'][-1]
    spl, ch = S_spline(prof, x)
    rmax_ch = ch['rmax']

    def gfunc(pts):
        pts = np.asarray(pts, dtype=DTYPE)
        r = np.sqrt(np.sum(pts ** 2, axis=1))
        rc = np.clip(r, 0.0, rmax_prof)
        a = a_s(rc); b = b_s(rc)
        S = spl(np.clip(r, 0.0, rmax_ch))
        P = pts.shape[0]
        g = np.zeros((P, 4, 4), dtype=DTYPE)
        g[:, 0, 0] = -np.exp(2 * a)
        g[:, 0, 1] = g[:, 1, 0] = -S * beta
        eb = np.exp(2 * b) - 1.0
        rsafe = np.where(r > 0, r, 1.0)
        n = pts / rsafe[:, None]
        for i in range(3):
            for j in range(3):
                g[:, 1 + i, 1 + j] = eb * n[:, i] * n[:, j]
            g[:, 1 + i, 1 + i] += 1.0
        return g
    gfunc.chain = ch
    return gfunc


def composed_gfunc_src(comp, prof_o, prof_i, x_o, x_i):
    """Composed metric: p413 background (a_comp, b_comp splines) with
    V(r) = beta_o S_o(r) + beta_i S_i(r), S from each shell's chain."""
    a_s = CubicSpline(comp['r'], comp['a'])
    b_s = CubicSpline(comp['r'], comp['b'])
    rmax = comp['r'][-1]
    spl_o, ch_o = S_spline(prof_o, x_o)
    spl_i, ch_i = S_spline(prof_i, x_i)
    bo, bi = comp['beta_o'], comp['beta_i']

    def gfunc(pts):
        pts = np.asarray(pts, dtype=DTYPE)
        r = np.sqrt(np.sum(pts ** 2, axis=1))
        rc = np.clip(r, 0.0, rmax)
        a = a_s(rc); b = b_s(rc)
        V = (bo * spl_o(np.clip(r, 0.0, ch_o['rmax']))
             + bi * spl_i(np.clip(r, 0.0, ch_i['rmax'])))
        P = pts.shape[0]
        g = np.zeros((P, 4, 4), dtype=DTYPE)
        g[:, 0, 0] = -np.exp(2 * a)
        g[:, 0, 1] = g[:, 1, 0] = -V
        eb = np.exp(2 * b) - 1.0
        rsafe = np.where(r > 0, r, 1.0)
        n = pts / rsafe[:, None]
        for i in range(3):
            for j in range(3):
                g[:, 1 + i, 1 + j] = eb * n[:, i] * n[:, j]
            g[:, 1 + i, 1 + i] += 1.0
        return g
    gfunc.chains = (ch_o, ch_i)
    return gfunc


# ---------------------------------------------------------------- held-W
def held_betas(prof_o, prof_i, beta_o_alone, beta_i_alone):
    """Dual held-W re-equilibration (P52-3 dual_betas pattern, on the
    p413 composed background). Returns (beta_o, beta_i, anatomy, comp0)."""
    comp0 = build_composed(prof_o, prof_i, 0.0, 0.0)
    rmi = 0.5 * (prof_i['R1'] + prof_i['R2'])
    rmo = 0.5 * (prof_o['R1'] + prof_o['R2'])
    ac_i = float(np.interp(rmi, comp0['r'], comp0['a']))
    aa_i = float(np.interp(rmi, prof_i['r'], prof_i['a']))
    ac_o = float(np.interp(rmo, comp0['r'], comp0['a']))
    aa_o = float(np.interp(rmo, prof_o['r'], prof_o['a']))
    beta_i = float(beta_i_alone * np.exp(ac_i - aa_i))
    beta_o = float(beta_o_alone * np.exp(ac_o - aa_o))
    W_i = float(beta_i_alone * np.exp(-aa_i))
    W_o = float(beta_o_alone * np.exp(-aa_o))
    a_pay = float(np.interp(0.5 * prof_i['R1'], comp0['r'], comp0['a']))
    anat = {
        'r_mid_inner': rmi, 'r_mid_outer': rmo,
        'a_comp_inner_mid': ac_i, 'a_alone_inner_mid': aa_i,
        'a_comp_outer_mid': ac_o, 'a_alone_outer_mid': aa_o,
        'lapse_factor_inner': float(np.exp(ac_i - aa_i)),
        'lapse_factor_outer': float(np.exp(ac_o - aa_o)),
        'beta_i_alone': beta_i_alone, 'beta_o_alone': beta_o_alone,
        'beta_i_comp': beta_i, 'beta_o_comp': beta_o,
        'W_i_alone': W_i, 'W_o_alone': W_o,
        'W_i_held': float(beta_i * np.exp(-ac_i)),
        'W_o_held': float(beta_o * np.exp(-ac_o)),
        'W_i_rel_err': float(abs(beta_i * np.exp(-ac_i) - W_i) / W_i),
        'W_o_rel_err': float(abs(beta_o * np.exp(-ac_o) - W_o) / W_o),
        'W_payload_sum': float(W_i + W_o),
        'payload_coord': float(beta_o + beta_i),
        'payload_relat': float((beta_o + beta_i) / (1 + beta_o * beta_i)),
        'W_payload_local': float((beta_o + beta_i) * np.exp(-a_pay)),
        'a_comp_payload': a_pay,
    }
    return beta_o, beta_i, anat, comp0


# ---------------------------------------------------------------- audit
def _sig_mask(That):
    scale = np.max(np.abs(That), axis=(1, 2))
    rho_peak = float(np.max(That[:, 0, 0]))
    thr = max(1e-11, 1e-3 * abs(rho_peak))
    return scale > thr, rho_peak, thr


def summarise_gs(gfunc, pts, h, region_fn=None):
    """Gate-standard summarise (p523_lib pattern). Non-Type-I points
    count against the row: regional worst is taken over Type-I points
    for margins, with typeI_frac + n_non_typeI carrying the failure;
    min_sampled_nec is over ALL significant points (the cross-check
    that catches non-Type-I patches, Phase-50 lesson)."""
    m = wa.audit(gfunc, pts, h)
    That = m['That']
    sig, rho_peak, thr = _sig_mask(That)
    ti = m['typeI']
    out = {'h': h, 'auditor': 'gate_standard', 'n_pts': int(len(pts)),
           'n_sig': int(np.sum(sig)), 'rho_peak': rho_peak, 'thr': float(thr),
           'typeI_frac_sig': float(np.mean(ti[sig])) if np.any(sig) else None,
           'n_sig_non_typeI': int(np.sum(sig & ~ti))}
    for k in KINDS:
        v = m[k][sig & ti]
        v = v[~np.isnan(v)]
        out['min_' + k] = float(np.min(v)) if v.size else None
    vals = [out['min_' + k] for k in KINDS if out['min_' + k] is not None]
    out['worst'] = float(min(vals)) if vals else None
    out['worst_kind'] = (min((k for k in KINDS if out['min_' + k] is not None),
                             key=lambda k: out['min_' + k]) if vals else None)
    sn = m['sampled_nec'][sig]
    out['min_sampled_nec_all_sig'] = float(np.nanmin(sn)) if sn.size else None
    snti = m['sampled_nec'][sig & ti]
    out['min_sampled_nec'] = float(np.nanmin(snti)) if snti.size else None
    if region_fn is not None:
        rr = np.sqrt(np.sum(pts ** 2, axis=1))
        regs = {}
        for reg in ('payload', 'inner_wall', 'cavity', 'outer_wall', 'exterior'):
            sel = sig & np.array([region_fn(x) == reg for x in rr])
            if np.any(sel):
                tisel = sel & ti
                entry = {'n_sig': int(np.sum(sel)),
                         'n_non_typeI': int(np.sum(sel & ~ti)),
                         'typeI_frac': float(np.mean(ti[sel]))}
                for k in KINDS:
                    v = m[k][tisel]
                    v = v[~np.isnan(v)]
                    entry['min_' + k] = float(np.min(v)) if v.size else None
                vv = [entry['min_' + k] for k in KINDS if entry['min_' + k] is not None]
                entry['worst'] = float(min(vv)) if vv else None
                entry['worst_kind'] = (min((k for k in KINDS if entry['min_' + k] is not None),
                                           key=lambda k: entry['min_' + k]) if vv else None)
                sreg = m['sampled_nec'][sel]
                entry['min_sampled_nec_all'] = float(np.nanmin(sreg)) if sreg.size else None
                if vv:
                    stack = np.stack([np.where(tisel, m[k], np.inf) for k in KINDS])
                    entry['worst_r'] = float(rr[np.argmin(np.min(stack, axis=0))])
                regs[reg] = entry
        out['regions'] = regs
    return out


def screen_points(R2, nrad=20, ndir=26, seed=11):
    """Reduced screening set for one shell alone (audit_points pattern,
    thinned radii)."""
    dirs = fib_dirs(ndir, seed)
    rad = np.linspace(0.4, 1.45 * R2, nrad)
    rad = np.unique(np.round(np.r_[rad, [0.21, 0.29, 0.39, 0.45, 0.51, 0.62,
                                         0.78, 0.95] * np.array(R2)], 6))
    rad = rad[rad > 0.3]
    return np.concatenate([dirs * rr for rr in rad]), rad


def screen_score(gfunc, pts, h=0.3):
    """Two-number screening score (P73-1 pattern): min over significant
    points of (eigenvalue worst margin at Type-I points, sampled NEC
    at non-Type-I points), further minned with all-EC margins.
    SCREENING ONLY — never a verdict."""
    m = wa.audit(gfunc, pts, h)
    That = m['That']
    sig, _, _ = _sig_mask(That)
    if not np.any(sig):
        return -1e-3, {}
    w = np.where(m['typeI'], m['nec'], m['sampled_nec']).copy()
    for kk in ('wec', 'sec', 'dec'):
        w = np.minimum(w, np.where(m['typeI'], m[kk], m['sampled_nec']))
    return float(np.min(w[sig])), {'n_sig': int(np.sum(sig)),
                                   'typeI_frac_sig': float(np.mean(m['typeI'][sig]))}
