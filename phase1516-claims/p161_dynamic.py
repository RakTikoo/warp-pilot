"""
p161_dynamic.py — Phase 16, P16-1: genuinely time-dependent Finalist-A shells.

Construction (per CHECKPOINT16.md §P16-1 and task spec):
  * shell profiles precomputed with shell.build_shell on a time grid of
    NS=32 slices over one period (periodic);
  * each slice's radial profiles a(r), b(r) are cubic splines in r;
  * gtfunc(t, pts) evaluates all slice splines at the points' radii and
    interpolates the metric functions in t with a PERIODIC cubic spline;
  * the shift window S(r,t) and beta(t) are known in closed form per
    variant and are evaluated analytically at t (they are part of the
    prescribed metric, exactly as in shell.shell_point_factory).
  * audit: phase7/p74_auditor.einstein_at_points_td (reused, unmodified),
    h=0.3 primary (ht=h), h=0.15 confirmation at the worst instant.
  * masks mirror verify_finalist.audit_block: scale = max|That| over
    components; sig = scale > max(1e-7, 1e-3*|rho_peak|);
    core = scale > 1e-5. Margins reported on the core mask (the
    Finalist-A headline "+1.19e-5, Type I 1.0" is a core number).

Variants (M_geom = 2.0 fixed everywhere; T = 40 primary):
  (i)  breathing: R1(t) = 10 - d*sin(2 pi t/T), R2(t) = 20 + d*sin(2 pi t/T),
       d in {0.5, 1.0}; wall thickness 10+2 d sin, centre fixed at 15;
       shift window ws = [R1(t), R2(t)] follows the wall; edgepeaked
       wd=3.0/floor=0.2, s_rho=2.0, s_P=1.16, beta=0.02.
       T=200 quasi-static control for d=1.0 (6 instants).
  (ii) oscillating shift: static Finalist-A profile, beta(t) =
       0.02*(1 + A sin(2 pi t/T)), A in {0.5, 1.0}, T=40.
       Frozen-slice margins (stationary slice at the same instant's
       beta, run through the same TD auditor) computed alongside, so
       time-derivative contributions are separated.
  (iii) travelling density wave: 'gauss' profile wd=3.0, peak centre
       Rm(t) = 15 + L*sin(2 pi t/T), L in {2, 4} (L=4 sweeps [11,19]),
       R1=10, R2=20 static, beta=0.02, T=40.

float64 everywhere. Run pieces: gate | breathing | shift | travelling | static
Each piece checkpoints its own JSON under phase16/results/.
"""
import json
import os
import sys
import time

import numpy as np
from scipy.interpolate import CubicSpline

sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase7')
import shell as sh                       # noqa: E402
import verify_metric as vm               # noqa: E402
from p74_auditor import einstein_at_points_td, wrap_stationary  # noqa: E402

DTYPE = np.float64
HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, 'results')
os.makedirs(RES, exist_ok=True)

M_G = 2.0
BETA0 = 0.02
NS = 32                      # slices per period (>=33 nodes incl. periodic wrap)
NR = 4001                    # radial grid for build_shell (Finalist-A fidelity)
BASE = dict(kind='edgepeaked', params={'wd': 3.0, 'floor': 0.2},
            s_rho=2.0, s_P=1.16)


# --------------------------------------------------------------------------
# sampling points (verify_finalist.dense_points-style, shell-focused)
# --------------------------------------------------------------------------
def fib_dirs(n):
    i = np.arange(n)
    phi = np.arccos(1 - 2 * (i + 0.5) / n)
    th = np.pi * (1 + 5 ** 0.5) * i
    return np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi),
                     np.cos(phi)], axis=1)


DIRS = fib_dirs(26)
RAD_SHELL = np.linspace(8.0, 22.0, 29)          # dr = 0.5
RAD_CAV = np.array([2.0, 4.0, 6.0])
PTS_SHELL = np.concatenate([DIRS * r for r in RAD_SHELL]).astype(DTYPE)
PTS_CAV = np.concatenate([DIRS * r for r in RAD_CAV]).astype(DTYPE)
PTS = np.concatenate([PTS_SHELL, PTS_CAV])
N_SHELL = len(PTS_SHELL)
# radial volume weights for the shell sample (per direction point)
W_SHELL = np.concatenate([np.full(26, 4 * np.pi * r * r * 0.5 / 26.0)
                          for r in RAD_SHELL])


# --------------------------------------------------------------------------
# dynamic metric from precomputed slices
# --------------------------------------------------------------------------
class DynamicShell:
    """gtfunc(t, pts) by periodic cubic interpolation in t of slice
    profiles a(r), b(r); S and beta analytic in t."""

    def __init__(self, T, slice_profiles, param_fn):
        """slice_profiles: list of NS build_shell dicts at t_i = i*T/NS.
        param_fn(t) -> (R1, R2, beta) analytic at time t."""
        self.T = float(T)
        self.param_fn = param_fn
        self.tn = np.linspace(0.0, self.T, NS, endpoint=False)
        self.a_sp = [CubicSpline(p['r'], p['a']) for p in slice_profiles]
        self.b_sp = [CubicSpline(p['r'], p['b']) for p in slice_profiles]
        self.rmax = slice_profiles[0]['r'][-1]

    def gtfunc(self, t, pts):
        pts = np.asarray(pts, dtype=DTYPE)
        r = np.sqrt(np.sum(pts ** 2, axis=1))
        rc = np.clip(r, 0.0, self.rmax)
        A = np.stack([sp(rc) for sp in self.a_sp])      # (NS, P)
        B = np.stack([sp(rc) for sp in self.b_sp])
        # scipy periodic BC needs the wrapped endpoint included
        tn_e = np.concatenate([self.tn, [self.T]])
        A_e = np.concatenate([A, A[:1]], axis=0)
        B_e = np.concatenate([B, B[:1]], axis=0)
        tt = float(t) % self.T
        a = CubicSpline(tn_e, A_e, axis=0, bc_type='periodic')(tt)
        b = CubicSpline(tn_e, B_e, axis=0, bc_type='periodic')(tt)
        R1, R2, beta = self.param_fn(float(t))
        S = sh.shift_S(r, R1, R2, 'cos', 1.0, [R1, R2])
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


def build_slices(T, prof_fn):
    """prof_fn(t) -> build_shell kwargs dict (R1, R2, kind, params)."""
    profs = []
    for i in range(NS):
        t = i * T / NS
        kw = prof_fn(t)
        profs.append(sh.build_shell(kw['R1'], kw['R2'], M_G, kind=kw['kind'],
                                    params=kw['params'], s_rho=BASE['s_rho'],
                                    s_P=BASE['s_P'], Nr=NR))
    return profs


# --------------------------------------------------------------------------
# audit helpers
# --------------------------------------------------------------------------
def summarise(That, m, label):
    scale = np.max(np.abs(That), axis=(1, 2))
    rho_peak = float(np.max(That[:, 0, 0]))
    thr = max(1e-7, 1e-3 * abs(rho_peak))
    out = {'label': label, 'rho_peak': rho_peak}
    for name, mask in (('sig', scale > thr), ('core', scale > 1e-5)):
        if mask.sum() == 0:
            out[name] = None
            continue
        d = {k: float(np.min(m[k][mask])) for k in ('nec', 'wec', 'sec', 'dec')}
        d['worst'] = min(d.values())
        d['typeI_frac'] = float(np.mean(m['typeI'][mask]))
        d['n'] = int(mask.sum())
        out[name] = d
    out['cavity_max_scale'] = float(np.max(scale[N_SHELL:]))
    out['shell_max_scale'] = float(np.max(scale[:N_SHELL]))
    # cavity-only core summary
    cav = np.zeros(len(That), dtype=bool); cav[N_SHELL:] = True
    cmask = cav & (scale > 1e-5)
    out['cavity_core'] = None
    if cmask.sum():
        d = {k: float(np.min(m[k][cmask])) for k in ('nec', 'wec', 'sec', 'dec')}
        d['worst'] = min(d.values())
        d['typeI_frac'] = float(np.mean(m['typeI'][cmask]))
        d['n'] = int(cmask.sum())
        out['cavity_core'] = d
    # exoticity proxies on the shell sample
    That_sh = That[:N_SHELL]
    out['E_neg_euler_shell'] = float(np.sum(
        np.minimum(That_sh[:, 0, 0], 0.0) * W_SHELL))
    nec_sh = m['nec'][:N_SHELL]
    out['NEC_neg_int_shell'] = float(np.sum(np.minimum(nec_sh, 0.0) * W_SHELL))
    out['mean_neg_nec_depth_core'] = None
    core = scale > 1e-5
    if core.sum():
        neg = np.minimum(m['nec'][core], 0.0)
        out['mean_neg_nec_depth_core'] = float(np.mean(neg))
    return out


def audit_instant(gtfunc, t, h, label):
    G, That, m = einstein_at_points_td(gtfunc, t, PTS, h=h, ht=h)
    s = summarise(That, m, label)
    s['t'] = float(t); s['h'] = float(h)
    # worst core point location
    scale = np.max(np.abs(That), axis=(1, 2))
    core = scale > 1e-5
    if core.sum():
        idx = np.where(core)[0][np.argmin(m['dec'][core])]
        s['worst_dec_radius'] = float(np.linalg.norm(PTS[idx]))
        s['worst_dec_point'] = [float(x) for x in PTS[idx]]
    return s


def run_variant(name, dyn, instants, h=0.3, frozen_fn=None, frozen_instants=()):
    """dyn: DynamicShell. frozen_fn(t) -> stationary gfunc at that instant."""
    rows = []
    for k, t in enumerate(instants):
        t0 = time.time()
        row = audit_instant(dyn.gtfunc, t, h, f'{name} dyn')
        if frozen_fn is not None and k in frozen_instants:
            gf = wrap_stationary(frozen_fn(t))
            row['frozen'] = audit_instant(gf, t, h, f'{name} frozen')
        row['wall_s'] = time.time() - t0
        rows.append(row)
        cw = row['core']['worst'] if row['core'] else None
        print(f"  {name} t={t:.2f} core worst={cw} "
              f"typeI={row['core']['typeI_frac'] if row['core'] else None} "
              f"({row['wall_s']:.0f}s)", flush=True)
    return rows


def aggregate(rows, static_row):
    core_worsts = [r['core']['worst'] for r in rows if r['core']]
    typeI_min = min(r['core']['typeI_frac'] for r in rows if r['core'])
    agg = {
        'n_instants': len(rows),
        'worst_instant_core': {
            k: float(min(r['core'][k] for r in rows if r['core']))
            for k in ('nec', 'wec', 'sec', 'dec', 'worst')},
        'worst_instant_sig_worst': float(min(
            r['sig']['worst'] for r in rows if r['sig'])),
        'min_typeI_frac_core': float(typeI_min),
        'time_avg_E_neg_euler_shell': float(np.mean(
            [r['E_neg_euler_shell'] for r in rows])),
        'time_avg_NEC_neg_int_shell': float(np.mean(
            [r['NEC_neg_int_shell'] for r in rows])),
        'time_avg_mean_neg_nec_depth_core': float(np.mean(
            [r['mean_neg_nec_depth_core'] for r in rows
             if r['mean_neg_nec_depth_core'] is not None])),
    }
    if static_row is not None:
        agg['static_comparison'] = {
            'static_E_neg_euler_shell': static_row['E_neg_euler_shell'],
            'static_NEC_neg_int_shell': static_row['NEC_neg_int_shell'],
            'static_mean_neg_nec_depth_core':
                static_row['mean_neg_nec_depth_core'],
            'delta_E_neg': agg['time_avg_E_neg_euler_shell']
                           - static_row['E_neg_euler_shell'],
            'delta_NEC_neg_int': agg['time_avg_NEC_neg_int_shell']
                                 - static_row['NEC_neg_int_shell'],
        }
    # frozen-vs-dynamic (where present)
    fd = []
    for r in rows:
        if 'frozen' in r and r['frozen']['core'] and r['core']:
            fd.append({'t': r['t'],
                       'dyn_core_worst': r['core']['worst'],
                       'frozen_core_worst': r['frozen']['core']['worst'],
                       'dyn_core_nec': r['core']['nec'],
                       'frozen_core_nec': r['frozen']['core']['nec'],
                       'dyn_typeI': r['core']['typeI_frac'],
                       'frozen_typeI': r['frozen']['core']['typeI_frac']})
    if fd:
        agg['frozen_vs_dynamic'] = fd
    return agg


def worst_instant(rows):
    return min((r for r in rows if r['core']), key=lambda r: r['core']['worst'])


def confirm_h015(dyn, rows, frozen_fn=None):
    w = worst_instant(rows)
    out = {'t_worst': w['t'], 'dyn_h015': audit_instant(
        dyn.gtfunc, w['t'], 0.15, 'confirm dyn h=0.15')}
    if frozen_fn is not None:
        out['frozen_h015'] = audit_instant(
            wrap_stationary(frozen_fn(w['t'])), w['t'], 0.15,
            'confirm frozen h=0.15')
    return out


def dump(obj, fname):
    with open(os.path.join(RES, fname), 'w') as f:
        json.dump(obj, f, indent=1, default=float)
    print('wrote', fname, flush=True)


# --------------------------------------------------------------------------
# variant constructors
# --------------------------------------------------------------------------
def finalist_prof():
    return sh.build_shell(10.0, 20.0, M_G, kind=BASE['kind'],
                          params=BASE['params'], s_rho=BASE['s_rho'],
                          s_P=BASE['s_P'], Nr=NR)


def finalist_gfunc(beta=BETA0):
    return sh.shell_point_factory(finalist_prof(), beta, 'cos', 1.0,
                                  [10.0, 20.0])


def make_breathing(delta, T):
    def prof_fn(t):
        s = np.sin(2 * np.pi * t / T)
        return dict(R1=10.0 - delta * s, R2=20.0 + delta * s,
                    kind=BASE['kind'], params=dict(BASE['params']))

    def param_fn(t):
        s = np.sin(2 * np.pi * t / T)
        return 10.0 - delta * s, 20.0 + delta * s, BETA0
    return DynamicShell(T, build_slices(T, prof_fn), param_fn)


def make_shift(A, T):
    prof = finalist_prof()

    def prof_fn(t):
        return dict(R1=10.0, R2=20.0, kind=BASE['kind'],
                    params=dict(BASE['params']))

    def param_fn(t):
        return 10.0, 20.0, BETA0 * (1.0 + A * np.sin(2 * np.pi * t / T))
    # single static profile for all slices (profile does not change)
    return DynamicShell(T, [prof] * NS, param_fn), prof


def make_travelling(Lam, T):
    def prof_fn(t):
        Rm = 15.0 + Lam * np.sin(2 * np.pi * t / T)
        return dict(R1=10.0, R2=20.0, kind='gauss',
                    params={'Rm': Rm, 'wd': 3.0})

    def param_fn(t):
        return 10.0, 20.0, BETA0
    return DynamicShell(T, build_slices(T, prof_fn), param_fn)


# --------------------------------------------------------------------------
# pieces
# --------------------------------------------------------------------------
def piece_static():
    gf = finalist_gfunc()
    row = audit_instant(wrap_stationary(gf), 0.0, 0.3, 'static Finalist-A TD')
    row15 = audit_instant(wrap_stationary(gf), 0.0, 0.15, 'static h=0.15')
    dump({'static_h03': row, 'static_h015': row15}, 'p161_static.json')
    return row


def piece_gate():
    out = {}
    # Gate 1: breathing machinery at delta=0 must reproduce stationary audit
    dyn0 = make_breathing(0.0, 40.0)
    row_dyn = audit_instant(dyn0.gtfunc, 0.0, 0.3, 'gate delta=0 interp')
    row_dyn2 = audit_instant(dyn0.gtfunc, 7.3, 0.3, 'gate delta=0 interp t=7.3')
    gf = finalist_gfunc()
    row_st = audit_instant(wrap_stationary(gf), 0.0, 0.3, 'gate stationary')
    out['delta0_interp_h03'] = row_dyn
    out['delta0_interp_h03_t7.3'] = row_dyn2
    out['stationary_h03'] = row_st
    out['core_worst_interp'] = row_dyn['core']['worst']
    out['core_worst_stationary'] = row_st['core']['worst']
    out['abs_diff_core_worst'] = abs(row_dyn['core']['worst']
                                    - row_st['core']['worst'])
    print('GATE core worst interp', row_dyn['core']['worst'],
          'stationary', row_st['core']['worst'], flush=True)
    dump(out, 'p161_gate.json')
    return out


def piece_breathing():
    static = json.load(open(os.path.join(RES, 'p161_static.json')))['static_h03']
    for delta, T, n_inst, tag in ((0.5, 40.0, 12, 'breathing_d0.5_T40'),
                                  (1.0, 40.0, 12, 'breathing_d1.0_T40'),
                                  (1.0, 200.0, 6, 'breathing_d1.0_T200')):
        print(f'== {tag}: building slices', flush=True)
        dyn = make_breathing(delta, T)
        instants = [k * T / n_inst for k in range(n_inst)]
        rows = run_variant(tag, dyn, instants)
        agg = aggregate(rows, static)
        conf = confirm_h015(dyn, rows)
        dump({'variant': tag, 'delta': delta, 'T': T,
              'parametrisation': 'R1=10-d sin(2 pi t/T), R2=20+d sin, '
                                 'ws=[R1(t),R2(t)], beta=0.02, M=2.0',
              'instants': rows, 'aggregate': agg, 'confirm_h015': conf},
             f'p161_{tag}.json')


def piece_shift():
    static = json.load(open(os.path.join(RES, 'p161_static.json')))['static_h03']
    for A, tag, frz in ((0.5, 'shift_A0.5_T40', (0, 3, 6, 9)),
                        (1.0, 'shift_A1.0_T40', tuple(range(12)))):
        print(f'== {tag}: building', flush=True)
        dyn, prof = make_shift(A, 40.0)

        def frozen_fn(t, A=A, prof=prof):
            beta = BETA0 * (1.0 + A * np.sin(2 * np.pi * t / 40.0))
            return sh.shell_point_factory(prof, beta, 'cos', 1.0, [10.0, 20.0])
        instants = [k * 40.0 / 12 for k in range(12)]
        rows = run_variant(tag, dyn, instants, frozen_fn=frozen_fn,
                           frozen_instants=frz)
        agg = aggregate(rows, static)
        conf = confirm_h015(dyn, rows, frozen_fn=frozen_fn)
        dump({'variant': tag, 'A': A, 'T': 40.0,
              'parametrisation': 'beta(t)=0.02(1+A sin(2 pi t/40)), static '
                                 'Finalist-A profile',
              'instants': rows, 'aggregate': agg, 'confirm_h015': conf},
             f'p161_{tag}.json')


def piece_travelling():
    static = json.load(open(os.path.join(RES, 'p161_static.json')))['static_h03']
    for Lam, tag in ((2.0, 'travelling_L2_T40'), (4.0, 'travelling_L4_T40')):
        print(f'== {tag}: building slices', flush=True)
        dyn = make_travelling(Lam, 40.0)
        instants = [k * 40.0 / 12 for k in range(12)]
        rows = run_variant(tag, dyn, instants)
        agg = aggregate(rows, static)
        conf = confirm_h015(dyn, rows)
        dump({'variant': tag, 'Lambda': Lam, 'T': 40.0,
              'parametrisation': "gauss wd=3.0, Rm(t)=15+L sin(2 pi t/40), "
                                 "R1=10, R2=20, beta=0.02, M=2.0",
              'instants': rows, 'aggregate': agg, 'confirm_h015': conf},
             f'p161_{tag}.json')


if __name__ == '__main__':
    which = sys.argv[1] if len(sys.argv) > 1 else 'all'
    t00 = time.time()
    if which in ('static', 'all'):
        piece_static()
    if which in ('gate', 'all'):
        piece_gate()
    if which in ('breathing', 'all'):
        piece_breathing()
    if which in ('shift', 'all'):
        piece_shift()
    if which in ('travelling', 'all'):
        piece_travelling()
    print(f'TOTAL {time.time()-t00:.0f}s')
