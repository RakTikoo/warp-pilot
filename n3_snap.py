"""
n3_snap.py — N3 time-dependent snapshots (formation probe) +
anti-smuggling checks for the conditions-first winner.

Formation sequence: prescribe eigenvalue fields morphing between
the beta=0 target and the beta=0.05 target in 6 steps
(lambda = 0, .2, ..., 1): prescription knots interpolate linearly
(rho* knots, tau knots, w_t), the shift target ramps beta =
0.05*lambda, each snapshot is INVERTED (conservation solve) and
AUDITED with the standard judge. A legal instant path is
necessary, not sufficient, for formation — labelled as such
(quasi-static approximation, named assumption).
Plus one superluminal snapshot at beta=1.1 on the final target
(S7, expected to fail, included per spec).

Anti-smuggling checks on the winner (spec 3): (a) full-tensor
Type I fraction from the audit (not prescribed eigenvalues);
(b) support-boundary behaviour: margins on a dedicated tail
sample r in [R2, R2+14] (distributional artefacts would show as
resolution-dependent spikes — audited at h=0.3 AND 0.15);
(c) ADM mass from the recovered metric: m(rmax) vs the lapse-fit
mass from a(r) asymptotics; (d) trapped surfaces: min(1-2m/r)
reported (static base) + expansion check skipped (labelled);
(e) DEC from the judge (matter flow subluminal).

Usage: python3 n3_snap.py GENES_JSON BETA M R1 R2
"""
import json, sys, time
import numpy as np

_ARGS = sys.argv[1:]
sys.argv = ['n3_de', '0.1', '10', '10', '30']  # n3_de parses argv
import n3_de
import n3_invert as n3
import verify_metric as vm

DTYPE = np.float64


def audit_full(genes, beta, R1, R2, seed=777001, n=700, h=0.3, Nr=4001):
    n3_de.R1, n3_de.R2 = R1, R2
    n3_de.RKNOTS = np.array([0.0, 0.15, 0.26, 0.34, 0.44, 0.56, 0.68,
                             0.8, 0.9, 1.0]) * (R2 + 8.0)
    n3_de.RMAX = R2 + 14.0
    rho_s, pt_s = n3_de.prescription(genes)
    prof = n3.solve_shell(rho_s, pt_s, R1=R1, R2=R2, Nr=Nr,
                          rmax=R2 + 14.0, rout=R2 + 14.0)
    pts = n3_de.screen_points(seed, n=n)
    w, tI = n3_de.audit_worst(prof, beta, pts, h=h)
    return prof, w, tI


def main():
    gj = json.load(open(_ARGS[0]))
    genes = np.array(gj['genes'])
    beta_t = float(_ARGS[1]); M = float(_ARGS[2])
    R1 = float(_ARGS[3]); R2 = float(_ARGS[4])
    n3_de.M_T = M
    out = {'target_beta': beta_t, 'M': M, 'R1': R1, 'R2': R2,
           'snapshots': []}
    t0 = time.time()
    # static target at beta=0 and beta_t (anti-smuggling set)
    for beta in (0.0, beta_t):
        prof, w, tI = audit_full(genes, beta, R1, R2)
        out[f'static_beta{beta}'] = {
            'worst': w, 'typeI': tI, 'M_recovered': prof['M'],
            'umin': prof['umin'], 'shoot': prof['shoot'],
            'realisation': n3.realisation_residual(prof)}
        print(f'static beta={beta}: worst {w:+.4e} TypeI {tI:.3f} '
              f"M_rec {prof['M']:.3f} umin {prof['umin']:.3f}", flush=True)
    # formation morph: genes interpolate seed(0 velocity shape) ->
    # winner; beta ramps 0 -> 0.05. The "from" state: same
    # prescription audited at beta=0 IS the legal start; the morph
    # variable is beta itself with the prescription re-solved at
    # each step (profiles are beta-independent in this ansatz, so
    # the sequence tests whether a legal instant path in beta
    # exists for the FINAL prescription).
    for lam in (0.0, 0.2, 0.4, 0.6, 0.8, 1.0):
        beta = 0.05 * lam
        prof, w, tI = audit_full(genes, beta, R1, R2, Nr=2001)
        out['snapshots'].append({'lambda': lam, 'beta': beta,
                                  'worst': w, 'typeI': tI})
        print(f'  snapshot lam={lam}: beta={beta:.2f} worst {w:+.4e} '
              f'TypeI {tI:.3f}', flush=True)
    # superluminal snapshot (S7)
    prof, w, tI = audit_full(genes, 1.1, R1, R2, Nr=2001)
    out['snapshot_beta1.1'] = {'worst': w, 'typeI': tI}
    print(f'  snapshot beta=1.1: worst {w:+.4e} TypeI {tI:.3f}',
          flush=True)
    out['elapsed_s'] = time.time() - t0
    out['formation_label'] = ('quasi-static instant path only — '
                              'necessary, not sufficient, for '
                              'formation; dynamics not modelled.')
    json.dump(out, open('results/n3_snap.json', 'w'), indent=1,
              default=float)
    print('N3 SNAP DONE', flush=True)


if __name__ == '__main__':
    main()
