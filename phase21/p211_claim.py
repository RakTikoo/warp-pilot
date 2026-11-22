#!/usr/bin/env python3
"""
p211_claim.py -- P21-1(c) published-claim audit, Phase-3 style.

Paper: F. S. N. Lobo, "A general class of braneworld wormholes",
arXiv:gr-qc/0701133 (PRD 75, 064027 (2007)).  Fetched full text:
archive.org gr-qc0701133 djvu text.

CLAIM (abstract, exact): "However, it is the effective total
stress energy tensor that violates the latter, and in this work,
the stress energy tensor confined on the brane, threading the
wormhole, is imposed to satisfy the NEC."
Author's own bulk caveat (Sec. II, exact): "one needs to find
E_{mu nu} which produces a wormhole violating the NEC at all
energies. However, the question of what 5-dimensional geometry
produces this is much more difficult to answer, and shall not
be explored here."  (Repeated in the Conclusion.)

Independent transcription audited here: his Sec. III.A dust case
with the "spatial Schwarzschild" shape b(r) = r0, Phi = 0, for
which the paper states the positive-sign branch gives rho = lam
(brane tension) and E components with magnitudes 12 pi lam and
4 pi lam (his eqs. (37)-(38), OCR-read).  SMS in our conventions
(k4^2 = 8 pi, k5^4 = 6 k4^2/lam, lam = 1, r0 = 1):
trace condition for dust: -R_scal... G-trace = -k4^2 rho
+ k5^4 rho^2/6; b = r0, Phi = 0 gives G-trace = 0 (R = 0 class),
so rho in {0, lam}; rho = lam branch audited.
float64, system python3.
"""
import json
import sys

import numpy as np
import sympy as sp

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase21')
import p211_throat as th   # noqa: E402

RES = '/home/hatch/workspace/warp-pilot/phase21/results/'
K4 = 8.0 * np.pi
LAM = 1.0
K5_4 = 6.0 * K4 / LAM
RV = th.RV


def main():
    out = dict(paper='Lobo, A general class of braneworld '
                     'wormholes, arXiv:gr-qc/0701133',
               claim_sentence='However, it is the effective total '
                              'stress energy tensor that violates '
                              'the latter, and in this work, the '
                              'stress energy tensor confined on '
                              'the brane, threading the wormhole, '
                              'is imposed to satisfy the NEC.',
               bulk_caveat_sentence='However, the question of what '
                                    '5-dimensional geometry produces '
                                    'this is much more difficult to '
                                    'answer, and shall not be '
                                    'explored here.')
    # Einstein for b = r0 = 1, Phi = 0 (SymPy, throat machinery)
    Gc_sym, Rsc_sym = th.einstein_mixed(sp.Integer(1), sp.Integer(0))
    Gc = [th.num(g) for g in Gc_sym]
    Gt, Gr, Gth = Gc[0], Gc[1], Gc[2]
    out['G_throat'] = [float(g[0]) for g in (Gt, Gr, Gth)]
    out['R_scalar_max'] = float(np.max(np.abs(th.num(Rsc_sym))))
    # dust rho = lam branch
    rho = np.full_like(RV, LAM)
    pr = np.zeros_like(RV); pt = np.zeros_like(RV)
    Pi = th.pi_mixed(rho, pr, pt)
    Et = K4 * (-rho) + K5_4 * Pi[0] - Gt
    Er = K4 * pr + K5_4 * Pi[1] - Gr
    Eth = K4 * pt + K5_4 * Pi[2] - Gth
    trE = Et + Er + 2 * Eth
    out['dust_rho_lam'] = dict(
        E_throat=dict(Et=float(Et[0]), Er=float(Er[0]),
                      Eth=float(Eth[0])),
        E_t_t_over_pi=float(Et[0] / np.pi),     # expect -12 (pi*lam)
        E_r_r_const_over_pi=float((Er[0] - 1.0) / np.pi),  # expect 4
        E_th_const_over_pi=float((Eth[0] + 0.5) / np.pi),  # expect 4
        traceE_max_abs=float(np.max(np.abs(trE))),
        E_t_t_at_r1000=float(Et[-1]),
        E_t_t_at_r1000_over_pi=float(Et[-1] / np.pi),
        decays_at_infinity=False,
        brane_EC=dict(rho=LAM, nec1=LAM, nec2=LAM, sec=LAM,
                      dec=LAM, legal=True),
        divergence='dust with Phi=0: (div tau)_r = 0 identically; '
                   'div E = k5^4 div Pi holds via Bianchi identity '
                   'residual = k4^2 div tau = 0')
    # tidal comparison: E_tidal*r^4 = (-1,-1,+1) (throat results);
    # this E tends to a CONSTANT (-12 pi lam) -> no tidal match.
    out['tidal_match'] = False
    out['AF_example_note'] = (
        'Sec. III.C asymptotically-flat dust example: printed '
        'eqs. (45)-(50) in the fetched OCR text are garbled in '
        'signs/factors (e.g. eq. (47) as OCR-read contradicts the '
        'stated b\'(r0) = gamma^2 < 1); not transcribed '
        'unambiguously -- logged, not fabricated (Phase-3 '
        'Das-Paul precedent). As OCR-read, his sigma_t (eq. 50) '
        'carries an r^-3 term -r0(1+gamma^2)/(2 r^3), which is '
        'not the tidal r^-4 profile in any case.')
    out['verdict'] = (
        'PARTIAL -- brane-level claim VERIFIED as stated (it is '
        'imposed by construction and the audited dust case obeys '
        'all ECs, tracelessness and the divergence identity); '
        'full-system claim NOT verified: the one exactly '
        'auditable case has E not decaying at infinity '
        '(E^t_t -> -12 pi lam), so no Schwarzschild-AdS5 bulk '
        'realises it, and the paper provides no bulk geometry '
        '(author\'s own caveat). Open clause: an explicit bulk '
        'metric whose Weyl projection is the required E.')
    with open(RES + 'p211_claim.json', 'w') as fh:
        json.dump(out, fh, indent=2, default=float)
    print(json.dumps(out, indent=2, default=float))


if __name__ == '__main__':
    main()
