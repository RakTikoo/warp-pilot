"""
p163_robust.py — Phase 16, P16-3: margin-robustness map of the ONE dynamic
configuration P16-1 found legal at every audited instant: the BREATHING wall
at delta=0.5, T=40 (worst-instant SEC margin +7.20e-06, Type I 1.0 at all 12
instants, h=0.15-confirmed; static twin worst margin +1.19e-05).

Per CHECKPOINT16.md §P16-3 (registered honesty constraint, binding): the
auditor is KINEMATIC — prescribed metric, no matter model, no Einstein
evolution. This script measures how the worst-instant EC margins degrade
under small PRESCRIBED perturbations of the profile parameters (the
thickness of the legal island in parameter space) and whether the margins
drift over 3 consecutive prescribed periods. It does NOT and cannot
establish dynamical stability in the evolution sense.

Perturbations (one at a time, then selected pairs), nominal in brackets:
  M_geom [2.0]:  +/-1% (1.98, 2.02), +/-5% (1.90, 2.10)
  R1 centre [10]: +/-0.25, +/-0.5      R2 centre [20]: +/-0.25, +/-0.5
  wd [3.0]: 2.5, 3.5
  oscillation phase offset: pi/4, pi/2 (exact slice rotations; a pure phase
    shift of a periodic prescription — included for completeness, expected
    null up to instant-sampling phase)
  amplitude delta [0.5]: 0.4, 0.6, 0.75  (delta=1.0 already KILLed in P16-1)
  period T [40]: 30, 60  (slice set identical; only the rate changes)
Pairs: (M+5%, d=0.6), (M-5%, d=0.6), (M+5%, wd=2.5), (M-5%, T=30),
  (d=0.6, T=30), (d=0.6, wd=2.5), (R1+0.5, R2-0.5), (R1-0.5, R2+0.5).

Audit: phase7/p74_auditor via p161_dynamic machinery (DynamicShell,
audit_instant), 8 instants per period (>=8 per brief), h=0.3 primary;
any config whose worst-instant core margin flips sign gets an h=0.15
re-audit at its worst instant. float64. Per-config JSON checkpoints under
results/p163_parts/ so an interrupted run resumes.
"""
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase7')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase16')
import shell as sh                       # noqa: E402
from p161_dynamic import DynamicShell, audit_instant, NS, NR  # noqa: E402

DTYPE = np.float64
HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, 'results')
PARTS = os.path.join(RES, 'p163_parts')
os.makedirs(PARTS, exist_ok=True)

NOM = dict(M=2.0, R1c=10.0, R2c=20.0, wd=3.0, delta=0.5, T=40.0, phase=0.0)
BETA0 = 0.02
N_INST = 8


def build_slices_gen(cfg):
    profs = []
    for i in range(NS):
        t = i * cfg['T'] / NS
        s = np.sin(2 * np.pi * t / cfg['T'] + cfg['phase'])
        R1 = cfg['R1c'] - cfg['delta'] * s
        R2 = cfg['R2c'] + cfg['delta'] * s
        profs.append(sh.build_shell(R1, R2, cfg['M'], kind='edgepeaked',
                                    params={'wd': cfg['wd'], 'floor': 0.2},
                                    s_rho=2.0, s_P=1.16, Nr=NR))
    return profs


def make_dyn(cfg, slices=None):
    if slices is None:
        slices = build_slices_gen(cfg)

    def param_fn(t, cfg=cfg):
        s = np.sin(2 * np.pi * t / cfg['T'] + cfg['phase'])
        return (cfg['R1c'] - cfg['delta'] * s,
                cfg['R2c'] + cfg['delta'] * s, BETA0)
    return DynamicShell(cfg['T'], slices, param_fn)


def audit_config(name, cfg, slices=None):
    """Audit N_INST instants over one period; h=0.15 confirm on sign flip."""
    dyn = make_dyn(cfg, slices=slices)
    instants = [k * cfg['T'] / N_INST for k in range(N_INST)]
    rows = []
    for t in instants:
        r = audit_instant(dyn.gtfunc, t, 0.3, f'{name} dyn')
        rows.append({'t': r['t'], 'core_worst': r['core']['worst'],
                     'core': {k: r['core'][k] for k in
                              ('nec', 'wec', 'sec', 'dec')},
                     'typeI_frac': r['core']['typeI_frac']})
    worst = min(rows, key=lambda r: r['core_worst'])
    out = {'name': name, 'cfg': {k: float(v) for k, v in cfg.items()},
           'instants': rows,
           'worst_instant_core_worst': worst['core_worst'],
           'worst_t': worst['t'],
           'worst_instant_core': worst['core'],
           'min_typeI_frac': min(r['typeI_frac'] for r in rows),
           'legal': bool(worst['core_worst'] > 0
                         and min(r['typeI_frac'] for r in rows) >= 1.0)}
    if worst['core_worst'] <= 0 or out['min_typeI_frac'] < 1.0:
        c = audit_instant(dyn.gtfunc, worst['t'], 0.15, f'{name} confirm')
        out['confirm_h015'] = {'t': c['t'], 'core_worst': c['core']['worst'],
                               'core': {k: c['core'][k] for k in
                                        ('nec', 'wec', 'sec', 'dec')},
                               'typeI_frac': c['core']['typeI_frac']}
    print(f"  {name}: worst={out['worst_instant_core_worst']:+.3e} "
          f"at t={worst['t']:.1f} typeI_min={out['min_typeI_frac']:.3f} "
          f"legal={out['legal']}", flush=True)
    return out, dyn


def run_one(name, cfg, slices=None):
    path = os.path.join(PARTS, f'{name}.json')
    if os.path.exists(path):
        print(f'  {name}: cached', flush=True)
        return json.load(open(path)), None
    t0 = time.time()
    out, dyn = audit_config(name, cfg, slices=slices)
    out['wall_s'] = time.time() - t0
    with open(path, 'w') as f:
        json.dump(out, f, indent=1, default=float)
    return out, dyn


def C(**kw):
    cfg = dict(NOM)
    cfg.update(kw)
    return cfg


def main():
    t00 = time.time()
    results = {}

    # ---- nominal + slice-reuse variants (T, phase) + 3-period drift ----
    print('== nominal (build slices once)', flush=True)
    nom_slices = build_slices_gen(NOM)
    nom, nom_dyn = run_one('nominal', NOM, slices=nom_slices)
    results['nominal'] = nom

    # drift: periods 2 and 3 at the nominal config (same dyn object;
    # gtfunc wraps t mod T and param_fn is exactly periodic, so this is a
    # check that the prescribed prescription repeats, NOT an evolution)
    drift_path = os.path.join(PARTS, 'drift3.json')
    if os.path.exists(drift_path):
        results['drift3'] = json.load(open(drift_path))
        print('  drift3: cached', flush=True)
    else:
        per = {1: [r['core_worst'] for r in nom['instants']]}
        for p in (2, 3):
            ws = []
            for k in range(N_INST):
                t = (p - 1) * NOM['T'] + k * NOM['T'] / N_INST
                r = audit_instant(nom_dyn.gtfunc, t, 0.3, f'drift p{p}')
                ws.append(r['core']['worst'])
            per[p] = ws
        drift = {'period_worst_core': {str(p): min(v) for p, v in per.items()},
                 'period1_worsts': per[1], 'period2_worsts': per[2],
                 'period3_worsts': per[3],
                 'max_abs_dev_vs_period1': float(max(
                     max(abs(np.array(per[p]) - np.array(per[1])))
                     for p in (2, 3)))}
        with open(drift_path, 'w') as f:
            json.dump(drift, f, indent=1, default=float)
        results['drift3'] = drift
        print(f"  drift3: worsts "
              f"{drift['period_worst_core']} maxdev "
              f"{drift['max_abs_dev_vs_period1']:.3e}", flush=True)

    for name, cfg in (('T30', C(T=30.0)), ('T60', C(T=60.0))):
        out, _ = run_one(name, cfg, slices=nom_slices)
        results[name] = out
    # phase offsets: rotating the slice list by k = phase/(2pi)*NS is the
    # exact same prescription with a shifted time origin
    for name, ph in (('phase_pi4', np.pi / 4), ('phase_pi2', np.pi / 2)):
        k = int(round(ph / (2 * np.pi) * NS))
        rot = nom_slices[k:] + nom_slices[:k]
        out, _ = run_one(name, C(phase=float(ph)), slices=rot)
        results[name] = out

    # ---- one-at-a-time (fresh slices each) ----
    singles = [
        ('M_p1pct', C(M=2.02)), ('M_m1pct', C(M=1.98)),
        ('M_p5pct', C(M=2.10)), ('M_m5pct', C(M=1.90)),
        ('R1_p025', C(R1c=10.25)), ('R1_m025', C(R1c=9.75)),
        ('R1_p05', C(R1c=10.5)), ('R1_m05', C(R1c=9.5)),
        ('R2_p025', C(R2c=20.25)), ('R2_m025', C(R2c=19.75)),
        ('R2_p05', C(R2c=20.5)), ('R2_m05', C(R2c=19.5)),
        ('wd_2.5', C(wd=2.5)), ('wd_3.5', C(wd=3.5)),
        ('delta_0.4', C(delta=0.4)), ('delta_0.6', C(delta=0.6)),
        ('delta_0.75', C(delta=0.75)),
    ]
    for name, cfg in singles:
        out, _ = run_one(name, cfg)
        results[name] = out

    # ---- two-at-a-time ----
    pairs = [
        ('pair_Mp5_d0.6', C(M=2.10, delta=0.6)),
        ('pair_Mm5_d0.6', C(M=1.90, delta=0.6)),
        ('pair_Mp5_wd2.5', C(M=2.10, wd=2.5)),
        ('pair_Mm5_T30', C(M=1.90, T=30.0)),
        ('pair_d0.6_T30', C(delta=0.6, T=30.0)),
        ('pair_d0.6_wd2.5', C(delta=0.6, wd=2.5)),
        ('pair_R1p05_R2m05', C(R1c=10.5, R2c=19.5)),
        ('pair_R1m05_R2p05', C(R1c=9.5, R2c=20.5)),
    ]
    for name, cfg in pairs:
        out, _ = run_one(name, cfg)
        results[name] = out

    with open(os.path.join(RES, 'p163_robust.json'), 'w') as f:
        json.dump({'nominal_cfg': {k: float(v) for k, v in NOM.items()},
                   'n_instants_per_config': N_INST, 'h_primary': 0.3,
                   'results': results,
                   'total_wall_s': time.time() - t00}, f, indent=1,
                  default=float)
    print(f'TOTAL {time.time()-t00:.0f}s — wrote p163_robust.json',
          flush=True)


if __name__ == '__main__':
    main()
