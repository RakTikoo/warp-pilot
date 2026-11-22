#!/usr/bin/env python3
"""
F4-4: Resolve the Phase 3 E_J conservation residual.

Phase 3 (p31_horndeski.py) found E_J (MRV eq. 80 / App. A CalEc) leaves a
smooth residual (-0.176 near throat), dominated by the F4 term
-2 pi'^4 J'' F4. Intake comparison vs the arXiv LaTeX source
(papers/mrv_src/apr-17-19.tex, eq. CalEc) and the arXiv HTML shows the
paper's first F4 term in E_J is

  -(B^2 pi'^4 / 2) * [ -A'^2 B/A^2 + A'(5B'J+2BJ')/(AJ)
                       + 2 (A''BJ + 5AB'J' + 2ABJ'')/(AJ) ] F4

which at A=B=1 reduces to  -2 pi'^4 (J''/J) F4 .
Phase 3's simplified CJ dropped the 1/J. This script:

  (1) recomputes E_J with the corrected term (all other terms exactly
      as Phase 3, whose E_A/E_B transcriptions are validated);
  (2) implements E_J INDEPENDENTLY, term by term, from the LaTeX CalEc
      specialised to A=B=1, K=G5=F5=0 (fresh transcription);
  (3) implements E_pi DIRECTLY from the LaTeX CalEphi (J_H, S_H, JS_BH
      specialised) -- an equation Phase 3 never implemented. By the
      Bianchi identity, E_J and E_pi residuals are equivalent when
      E_A=E_B=0; two independent transcriptions agreeing is the test.

float64 throughout. Every number computed in-run.
"""
import json
import sys
import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase3')
import p31_horndeski as p31

TAU = p31.TAU


def ej_corrected_and_independent(d):
    """Returns (EJ_old, EJ_corr, EJ_latex) using Phase 3 background dict."""
    EA, EB, EJ_old, CA, CB = p31.eom_residuals(d)
    J, Jp, Jpp = d['J'], d['Jp'], d['Jpp']
    pip, pipp, X, Xp = d['pip'], d['pipp'], d['X'], d['Xp']
    G4, G4X, G4pi, G4piX, G4pipi = d['G4'], d['G4X'], d['G4pi'], d['G4piX'], d['G4pipi']
    F4, F4X, F4pi = d['F4'], d['F4X'], d['F4pi']
    F = d['F']

    # (1) corrected: replace -2 pip^4 Jpp F4  with  -2 pip^4 (Jpp/J) F4
    EJ_corr = EJ_old + 2.0 * pip**4 * Jpp * F4 - 2.0 * pip**4 * (Jpp / J) * F4

    # (2) independent LaTeX CalEc, A=B=1 (A'=A''=B'=0), K=G5=F5=0:
    # E_J = F - (2J''/J) G4
    #   - pi' [ 2J'/J + 2J''/J' + 2 grp ] G4pi ,  grp=(pi''-J''pi'/J')/pi'
    #   + X (4J''/J) G4X + X' (2J'/J) G4X + 4X G4pipi
    #   + 2 pi' (2J'/J - X'/X) X G4piX
    #   - 2 pi'^4 (J''/J) F4
    #   - (2J'/J) pi'^3 [ 4 pi'' F4 + pi'^2 F4pi - pi'^2 pi'' F4X ]
    with np.errstate(divide='ignore', invalid='ignore'):
        grp = (pipp - Jpp * pip / Jp) / pip
    EJ_latex = (F
                - (2.0 * Jpp / J) * G4
                - pip * (2.0 * Jp / J + 2.0 * Jpp / Jp + 2.0 * grp) * G4pi
                + X * (4.0 * Jpp / J) * G4X
                + Xp * (2.0 * Jp / J) * G4X
                + 4.0 * X * G4pipi
                + 2.0 * pip * (2.0 * Jp / J - Xp / X) * X * G4piX
                - 2.0 * pip**4 * (Jpp / J) * F4
                - (2.0 * Jp / J) * pip**3 * (4.0 * pipp * F4 + pip**2 * F4pi
                                             - pip**2 * pipp * F4X))
    return EJ_old, EJ_corr, EJ_latex


def epi_direct(r):
    """E_pi from LaTeX CalEphi specialised to A=B=1, K=G5=F5=0.

    E_pi = (1/J^2) d/dr [ J^2 J' J_H ] - S_H + JS_BH   (sqrt factors = 1)
    with the finite combination Q := J^2 J' J_H computed without 1/J'
    singularities:
      Q = J^2 pi' F_X + 2 pi' (1-J'^2) G4X - 8 J J' X G4piX
    S_H = -F_pi - (2/J)((1-J'^2)/J - 2J'') G4pi
          + [ (X'/X)(4J'/J) + 4J'^2/J^2 ] X G4piX
    JS_BH = -4 pi'^2 [ (4J'J''/J^2) pi' + (6J'^2/J^2) pi'' ] F4
            - (12 J'^2/J^2) pi'^4 F4pi
            + pi'^4 [ (4J'J''/J^2) pi' + (18 J'^2/J^2) pi'' ] F4X
            + (4 J'^2/J^2) pi'^6 F4piX
    F_pi = f0_pi + f1_pi X + f2_pi X^2 (partial wrt pi at fixed X).
    F4piX = d f41 / d pi.
    Q'(r) by central differences on the analytic Q(r).
    """
    r = np.atleast_1d(np.asarray(r, dtype=np.float64))

    def Q_of(rr):
        d = p31.theory_on_bg(np.atleast_1d(rr))
        return (d['J']**2 * d['pip'] * d['FX']
                + 2.0 * d['pip'] * (1.0 - d['Jp']**2) * d['G4X']
                - 8.0 * d['J'] * d['Jp'] * d['X'] * d['G4piX'])

    h = 1e-4
    Qp = (Q_of(r + h) - Q_of(r - h)) / (2 * h)

    d = p31.theory_on_bg(r)
    J, Jp, Jpp = d['J'], d['Jp'], d['Jpp']
    pip, pipp, X, Xp = d['pip'], d['pipp'], d['X'], d['Xp']
    # F_pi at fixed X: complex-step in s on f0+f1*X0+f2*X0^2
    s = d['s']
    Fpi = np.empty_like(r)
    for i in range(len(r)):
        X0 = X[i]
        def F_of_s(ss, X0=X0):
            f2v = p31.f2_s(np.atleast_1d(ss))
            f1v = p31.f1_s(np.atleast_1d(ss), f2v)
            f0v = p31.f0_s(np.atleast_1d(ss), f1v, f2v)
            return f0v + f1v * X0 + f2v * X0**2
        Fpi[i] = float(p31.dpi(lambda ss: F_of_s(ss), np.atleast_1d(s[i]))[0])
    F4piX = p31.dpi(p31.f41_s, s)

    SH = (-Fpi
          - (2.0 / J) * ((1.0 - Jp**2) / J - 2.0 * Jpp) * d['G4pi']
          + ((Xp / X) * (4.0 * Jp / J) + 4.0 * Jp**2 / J**2) * X * d['G4piX'])
    JSBH = (-4.0 * pip**2 * ((4.0 * Jp * Jpp / J**2) * pip
                             + (6.0 * Jp**2 / J**2) * pipp) * d['F4']
            - (12.0 * Jp**2 / J**2) * pip**4 * d['F4pi']
            + pip**4 * ((4.0 * Jp * Jpp / J**2) * pip
                        + (18.0 * Jp**2 / J**2) * pipp) * d['F4X']
            + (4.0 * Jp**2 / J**2) * pip**6 * F4piX)
    Epi = Qp / J**2 - SH + JSBH
    return Epi


def main():
    res = {'task': 'F4-4 conservation residual (E_J / E_pi)'}
    r = np.linspace(-60, 60, 12001)
    d = p31.theory_on_bg(r)
    EJ_old, EJ_corr, EJ_latex = ej_corrected_and_independent(d)
    mask = np.abs(r) > 0.5
    mask20 = mask & (np.abs(r) < 20)

    def stats(x, m):
        return dict(absmax=float(np.max(np.abs(x[m]))),
                    at_r=float(r[m][int(np.argmax(np.abs(x[m])))]))
    res['EJ_old_phase3'] = dict(masked=stats(EJ_old, mask),
                                near_throat=stats(EJ_old, mask20))
    res['EJ_corrected'] = dict(masked=stats(EJ_corr, mask),
                               near_throat=stats(EJ_corr, mask20))
    res['EJ_independent_latex'] = dict(masked=stats(EJ_latex, mask),
                                       near_throat=stats(EJ_latex, mask20))
    res['corr_vs_latex_maxdiff'] = float(np.max(np.abs(EJ_corr - EJ_latex)[mask]))

    # term anatomy at r=5, old vs corrected F4 piece
    d5 = p31.theory_on_bg(np.array([5.0]))
    oldF4 = -2.0 * d5['pip']**4 * d5['Jpp'] * d5['F4']
    newF4 = -2.0 * d5['pip']**4 * (d5['Jpp'] / d5['J']) * d5['F4']
    res['anatomy_r5'] = dict(J=float(d5['J'][0]), old_F4_term=float(oldF4[0]),
                             corrected_F4_term=float(newF4[0]))

    # samples of corrected residual
    for rr in (0.55, 1.0, 5.0, 12.0, 40.0):
        i = int(np.argmin(np.abs(r - rr)))
        res[f'EJ_corrected_at_r{rr}'] = float(EJ_corr[i])
        res[f'EJ_old_at_r{rr}'] = float(EJ_old[i])

    # E_pi direct (evaluate on coarser grid; Q' by finite differences)
    rp = np.linspace(-40, 40, 801)
    rp = rp[np.abs(rp) > 0.5]
    Epi = epi_direct(rp)
    res['Epi_direct'] = dict(absmax=float(np.max(np.abs(Epi))),
                             at_r=float(rp[int(np.argmax(np.abs(Epi)))]),
                             median_abs=float(np.median(np.abs(Epi))))
    for rr in (1.0, 5.0, 12.0):
        i = int(np.argmin(np.abs(rp - rr)))
        res[f'Epi_at_r{rr}'] = float(Epi[i])

    res['verdict'] = ('PENDING coordinator review')
    with open('/home/hatch/workspace/warp-pilot/phase4/results/p44_ej.json', 'w') as fh:
        json.dump(res, fh, indent=2)
    print(json.dumps(res, indent=2))


if __name__ == '__main__':
    main()
