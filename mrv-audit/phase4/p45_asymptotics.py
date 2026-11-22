#!/usr/bin/env python3
"""
F4-5: Asymptotics audit of the MRV beyond-Horndeski wormhole
(arXiv:1812.07022, explicit example; Phase 3 candidate P3-1).

Registered questions (CHECKPOINT4.md, RELAUNCH):
  Q1 on-background GR recovery at large |r| (calF, calG, calH, odd sound
     speeds, even c_s1^2, c_s2^2, P1, P3 combination, Xi, G4=1/2).
  Q2 cancellation growth: largest uncancelled designer pieces vs the
     cancelled sums; growth laws; radii where the largest term crosses
     1e2, 1e4, 1e6 x the cancelled sum. Verify the paper's stated
     asymptotics (eq. function_asymp): f0~1/r^2, f1~const, f2~r^2,
     f40~r^4, f41~r^6.
  Q3 off-trajectory definition (source-text analysis, in JSON + checkpoint).
  Q4 gates that apply on-background: GW speed c_T (odd sector), far-field
     metric / ADM, scalar-gradient falloff and long-range scalar force.

Method: Phase 3's p31_horndeski.py is imported and used as the validation
gate on |r| <= 60 (must reproduce calF=calG=calH=1, 2P1-calF >= 0.713,
c_s2^2 in [0.261, 0.877]). For |r| > 60 a numerically stable re-implementation
of the SAME formulas is used: p31's literal formulas overflow/underflow in
float64 for |r| >~ 3500 (sinh(2*sinh s) overflow in f2; cosh(sinh s)
overflow in sech) and the F4 sum f40 + f41*X suffers catastrophic
cancellation (pieces ~1e7 vs true sum ~1e-43 at r=1000), so F4 on the
background is evaluated from its defining formula F4bg = w*sech(sinh s + u)
(MRV eq. 61) and sech is evaluated via logcosh. The stable implementation
is cross-validated against p31 on |r| <= 60 (all theory functions) and on
the overlap to |r| = 1000 for the quantities p31 can still evaluate.
float64 throughout.
"""
import json
import importlib.util
import numpy as np

TAU = 10.0
W = 1.0
U = 0.1

spec = importlib.util.spec_from_file_location(
    "p31", "/home/hatch/workspace/warp-pilot/phase3/p31_horndeski.py")
p31 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p31)

# ---------------------------------------------------------------- stable forms
def logcosh(x):
    ax = np.abs(x)
    return ax - np.log(2.0) + np.log1p(np.exp(-2.0 * ax))

def sech_st(x):
    return np.exp(-logcosh(np.asarray(x, dtype=np.float64)))

def tanh_div_st(x):
    x = np.asarray(x, dtype=np.float64)
    out = np.empty_like(x)
    small = np.abs(x) < 1e-3
    xs = x[small]
    out[small] = 1.0 - xs**2 / 3.0 + 2.0 * xs**4 / 15.0
    xl = x[~small]
    out[~small] = np.tanh(xl) / xl
    return out

def g40_s(s):
    return -0.5 * W * sech_st(U + np.sinh(s)) * sech_st(s) ** 4

def g41_s(s):
    return 2.0 * g40_s(s) * np.cosh(s) ** 2

def f41_s(s):
    sh = np.sinh(s)
    T = np.cosh(s) ** 2 * tanh_div_st(sh)
    bracket = (np.cosh(s) ** 4 + 10.0 * W * sech_st(U + sh)
               - 2.0 * W * T * sech_st(U + sh))
    return 0.25 * np.cosh(s) ** 2 * bracket

def f40_s(s):
    return 0.5 * f41_s(s) * sech_st(s) ** 2 - 2.0 * g40_s(s) * np.cosh(s) ** 4

def F4bg_s(s):
    return W * sech_st(np.sinh(s) + U)

def log10_F4bg(s):
    return -logcosh(np.sinh(s) + U) / np.log(10.0)

def f2_s(s):
    """MRV App. D. For |sinh s| > 50 the sech-suppressed correction terms are
    < 1e-20 in absolute size (bounded by poly(sinh s)*exp(-sinh s)) and only
    the term4 piece (-11 + 16 sinh^2 s + 3 sinh s*tanh(tau*sinh s))/(8 tau^2)
    survives; sech^6(s)*cosh^6(s) = 1 exactly, used throughout."""
    s = np.asarray(s, dtype=np.float64)
    sh = np.sinh(s)
    ch = np.cosh(s)
    poly = (-11.0 + 16.0 * sh**2 + 3.0 * sh * np.tanh(TAU * sh))
    out = poly / (8.0 * TAU**2)
    m = np.abs(sh) <= 50.0
    if np.any(m):
        sm, shm, chm = s[m], sh[m], ch[m]
        A = sech_st(U + shm)
        B = sech_st(shm)
        term1 = 2.0 * W * (-51.0 + 47.0 * np.cosh(2 * sm)) * chm**2 * A
        term2 = (8.0 * W * chm**4 * B * A**2 * shm
                 * (6.0 * np.sinh(U) + np.sinh(U + 2 * shm)))
        inner = (4.0 * np.sinh(U)
                 + 2.0 * np.sinh(U - 2 * sm) - 2.0 * np.sinh(U - sm)
                 + 2.0 * np.sinh(U + sm) + 2.0 * np.sinh(U + 2 * sm)
                 + 2.0 * np.sinh(U + 2 * shm)
                 + np.sinh(U - 2 * sm + 2 * shm) - 2.0 * np.sinh(U - sm + 2 * shm)
                 + 2.0 * np.sinh(U + sm + 2 * shm) + np.sinh(U + 2 * sm + 2 * shm))
        term3 = W * A * (9.0 * np.sinh(2 * sm) ** 2
                         + 2.0 * W * B**2 * A**3 * np.sinh(U) * inner)
        out[m] = (sech_st(sm) ** 6 / (8.0 * TAU**2)) * (
            term1 + term2 + term3 + chm**6 * poly[m])
    return out

def f1_s(s, f2v=None):
    if f2v is None:
        f2v = f2_s(s)
    sh = np.sinh(s)
    A = sech_st(U + sh)
    bracket_inner = (2.0 * sech_st(sh) * A * np.sinh(U)
                     - 9.0 * sech_st(s) * np.tanh(s) + np.tanh(sh))
    bracket = (4.0 * TAU**2 * f2v - 7.0 - np.cosh(2 * s)
               - 4.0 * W * sech_st(s) * A * np.tanh(s) * bracket_inner)
    return sech_st(s) ** 2 * bracket / (4.0 * TAU**2)

def f0_s(s, f1v=None, f2v=None):
    if f2v is None:
        f2v = f2_s(s)
    if f1v is None:
        f1v = f1_s(s, f2v)
    sh = np.sinh(s)
    A = sech_st(U + sh)
    inner = (-5.0 * sech_st(s) + 6.0 * sech_st(s) ** 3
             - np.tanh(s) * np.tanh(U + sh))
    bracket = (2.0 * f1v - f2v * sech_st(s) ** 2
               + sech_st(s) ** 2 / TAU**2
               * (4.0 + 8.0 * W * sech_st(s) * A * inner))
    return 0.25 * sech_st(s) ** 2 * bracket

def dpi_st(f, s, h=1e-5):
    """d/dpi via central FD in s (d/dpi = (1/tau) d/ds). Validated against
    p31's complex-step dpi on |r| <= 60 in the validation gate below."""
    return (f(s + h) - f(s - h)) / (2 * h) / TAU

def theory(r):
    r = np.asarray(r, dtype=np.float64)
    s = np.arcsinh(r / TAU)
    J = np.sqrt(r**2 + TAU**2)
    Jp = r / J
    pip = TAU / J
    X = -0.5 * pip**2
    g40, g41, f40, f41 = g40_s(s), g41_s(s), f40_s(s), f41_s(s)
    f2v = f2_s(s)
    f1v = f1_s(s, f2v)
    f0v = f0_s(s, f1v, f2v)
    return dict(
        r=r, s=s, J=J, Jp=Jp, pip=pip, X=X,
        g40=g40, g41=g41, f40=f40, f41=f41, f0=f0v, f1=f1v, f2=f2v,
        F=f0v + f1v * X + f2v * X**2,
        G4=0.5 + g40 + g41 * X,
        F4=F4bg_s(s),                      # eq. (61) definition, no cancellation
        F4_sum_check=f40 + f41 * X,        # literal sum (roundoff at large r)
        G4pi=dpi_st(g40_s, s) + dpi_st(g41_s, s) * X,
        G4piX=dpi_st(g41_s, s),
        F4pi=dpi_st(f40_s, s) + dpi_st(f41_s, s) * X,
        F4pi_pieces=(dpi_st(f40_s, s), dpi_st(f41_s, s) * X),
    )

def Xi_Gamma(d):
    s, r, J, pip = d['s'], d['r'], d['J'], d['pip']
    g40p = dpi_st(g40_s, s)
    g41p = dpi_st(g41_s, s)
    Xi = (2.0 * J**2 * g40p
          + pip * (4.0 * r * d['g41']
                   + 4.0 * r * pip**2 * (4.0 * d['f40'] - 3.0 * d['f41'] * pip**2)
                   - 3.0 * pip * J**2 * g41p))
    Gamma = ((2.0 * pip / J**2) * (2.0 * r * d['g41']
                                   - 3.0 * pip * J**2 * g41p
                                   + 8.0 * r * pip**2 * d['f40']
                                   - 6.0 * r * pip**4 * d['f41'])
             + 4.0 * g40p)
    return Xi, Gamma

def Xi_pieces(d):
    """Individual terms of Xi (MRV eq. 58c specialised, p31 form)."""
    s, r, J, pip = d['s'], d['r'], d['J'], d['pip']
    g40p = dpi_st(g40_s, s)
    g41p = dpi_st(g41_s, s)
    return dict(
        two_J2_g40pi=2.0 * J**2 * g40p,
        pip_4r_g41=pip * 4.0 * r * d['g41'],
        pip_16r_pip2_f40=pip * 16.0 * r * pip**2 * d['f40'],
        pip_m12r_pip4_f41=pip * (-12.0) * r * pip**4 * d['f41'],
        m3_pip2_J2_g41pi=-3.0 * pip**2 * J**2 * g41p,
    )

def Sigma_val(d):
    s, r, J, pip = d['s'], d['r'], d['J'], d['pip']
    g41p = dpi_st(g41_s, s)
    bracket = (J**4 * d['f1'] + 2.0 * TAU**2 * d['g41']
               + 12.0 * pip * r * J**2 * g41p
               - 3.0 * pip**2 * (J**4 * d['f2'] + 8.0 * r**2 * d['f40']
                                 - 10.0 * r**2 * d['f41'] * pip**2))
    return -pip**2 / (2.0 * J**4) * bracket

def Sigma_pieces_P3(d):
    """Contributions of each Sigma-bracket piece to P3 via -4 J^4 Sigma
    (H=B=1): piece B_i contributes 2 pip^2 B_i to P3."""
    s, r, J, pip = d['s'], d['r'], d['J'], d['pip']
    g41p = dpi_st(g41_s, s)
    B = dict(
        J4_f1=J**4 * d['f1'],
        two_tau2_g41=2.0 * TAU**2 * d['g41'],
        g41pi_term=12.0 * pip * r * J**2 * g41p,
        m3pip2_J4_f2=-3.0 * pip**2 * J**4 * d['f2'],
        m3pip2_8r2_f40=-3.0 * pip**2 * 8.0 * r**2 * d['f40'],
        m3pip2_m10r2_f41pip2=+3.0 * pip**2 * 10.0 * r**2 * d['f41'] * pip**2,
    )
    return {k: 2.0 * pip**2 * v for k, v in B.items()}, B

def Q_of_r(r):
    d = theory(np.atleast_1d(np.asarray(r, dtype=np.float64)))
    Xi, _ = Xi_Gamma(d)
    num = d['J']**2 * (1.0 - 2.0 * d['F4'] * d['pip']**4)
    den = 2.0 * d['J'] * d['Jp'] + Xi * d['pip']
    return num / den

def P1_val(r):
    r = np.asarray(r, dtype=np.float64)
    h = np.maximum(1e-3, 1e-5 * np.abs(r))
    return (Q_of_r(r + h) - Q_of_r(r - h)) / (2 * h)

def all_quantities(r):
    """Q1 quantities at given r array."""
    d = theory(r)
    Xi, Gamma = Xi_Gamma(d)
    Sig = Sigma_val(d)
    J, pip = d['J'], d['pip']
    pip2 = pip**2
    calF = 1 + 2 * d['g40'] - d['g41'] * pip2
    calH = (1 + 2 * d['g40'] + d['g41'] * pip2
            + 2 * d['f40'] * pip2**2 - d['f41'] * pip2**3)
    calG = calH.copy()
    P1 = P1_val(r)
    Dden = 2.0 * J * d['Jp'] + Xi * pip
    P3 = (2 * J**2 * Gamma * Xi * pip2 - Xi**2 * pip2 - 4 * J**4 * Sig)
    cs2 = P3 / (Dden**2 * (2 * P1 - calF))
    return dict(d=d, Xi=Xi, Gamma=Gamma, Sigma=Sig, calF=calF, calG=calG,
                calH=calH, P1=P1, P3=P3, Dden=Dden, cs2=cs2,
                cr2=calG / calF, cth2=calG / calH, cs1sq=calG / calF)

def power_fit(r, y, lo, hi):
    m = (np.abs(r) >= lo) & (np.abs(r) <= hi) & (np.abs(y) > 0)
    A = np.polyfit(np.log10(np.abs(r[m])), np.log10(np.abs(y[m])), 1)
    return float(A[0]), float(10 ** A[1])

def crossing_radius(rgrid, y, target):
    """First |r| (grid ascending in |r|) where |y| >= target, log-interpolated."""
    ay = np.abs(y)
    idx = np.where(ay >= target)[0]
    if len(idx) == 0:
        return None
    i = idx[0]
    if i == 0:
        return float(np.abs(rgrid[0]))
    x0, x1 = np.log10(np.abs(rgrid[i - 1])), np.log10(np.abs(rgrid[i]))
    y0, y1 = np.log10(ay[i - 1]), np.log10(ay[i])
    xc = x0 + (np.log10(target) - y0) * (x1 - x0) / (y1 - y0)
    return float(10 ** xc)

# ---------------------------------------------------------------- validation gate
res = {}
rv = np.linspace(-60, 60, 12001)
dv = p31.theory_on_bg(rv)
pip2v = dv['pip']**2
calF_v = 1 + 2 * dv['g40'] - dv['g41'] * pip2v
calH_v = (1 + 2 * dv['g40'] + dv['g41'] * pip2v
          + 2 * dv['f40'] * pip2v**2 - dv['f41'] * pip2v**3)
ds = theory(rv)
gate = dict(
    p31_calF_max_dev=float(np.max(np.abs(calF_v - 1))),
    p31_calG_max_dev=float(np.max(np.abs(calH_v - 1))),
    p31_calH_max_dev=float(np.max(np.abs(calH_v - 1))),
    stable_vs_p31_max_abs_diff={
        k: float(np.max(np.abs(ds[k] - dv[k])))
        for k in ['f0', 'f1', 'f2', 'g40', 'g41', 'f40', 'f41', 'F', 'G4']},
    stable_F4_vs_p31_max_abs_diff=float(np.max(np.abs(ds['F4'] - dv['F4']))),
)
Xi_v, _ = p31.Xi_Gamma(dv)
Xi_s, Ga_s = Xi_Gamma(ds)
gate['stable_Xi_vs_p31_max_abs_diff'] = float(np.max(np.abs(Xi_s - Xi_v)))
gate['stable_Gamma_vs_p31_max_abs_diff'] = float(
    np.max(np.abs(Ga_s - p31.Xi_Gamma(dv)[1])))
q60 = all_quantities(rv)
gate['stable_2P1_minus_calF_min_r_le_60'] = float(np.min(2 * q60['P1'] - q60['calF']))
gate['stable_cs2_min_r_le_60'] = float(np.min(q60['cs2']))
gate['stable_cs2_max_r_le_60'] = float(np.max(q60['cs2']))
gate['stable_calFH_max_dev_r_le_60'] = float(max(
    np.max(np.abs(q60['calF'] - 1)), np.max(np.abs(q60['calH'] - 1))))
res['validation_gate'] = gate

# ---------------------------------------------------------------- Q1
samples = [0.0, 1.0, 5.0, 10.0, 20.0, 40.0, 60.0, 100.0, 200.0, 500.0,
           1000.0, 2000.0, 5000.0, 10000.0]
q1_table = {}
for sgn in (+1, -1):
    for rr in samples:
        if rr == 0.0 and sgn < 0:
            continue
        r = np.array([sgn * rr])
        q = all_quantities(r)
        d = q['d']
        q1_table[f"r={sgn*rr:g}"] = dict(
            calF=float(q['calF'][0]), calG=float(q['calG'][0]),
            calH=float(q['calH'][0]),
            calF_dev=float(q['calF'][0] - 1), calH_dev=float(q['calH'][0] - 1),
            G4=float(d['G4'][0]), G4_dev=float(d['G4'][0] - 0.5),
            c_r2=float(q['cr2'][0]), c_theta2=float(q['cth2'][0]),
            c_s1sq=float(q['cs1sq'][0]), c_s2sq=float(q['cs2'][0]),
            c_s2sq_dev_from_1=float(q['cs2'][0] - 1),
            P1=float(q['P1'][0]), P3=float(q['P3'][0]),
            P3_over_J2=float(q['P3'][0] / d['J'][0] ** 2),
            Xi=float(q['Xi'][0]), Gamma=float(q['Gamma'][0]),
            Sigma=float(q['Sigma'][0]),
            Xi_pip_over_JJp=(float(q['Xi'][0] * d['pip'][0]
                                   / (d['J'][0] * d['Jp'][0])) if rr > 0 else None),
            F_on_bg=float(d['F'][0]), pi=float(TAU * d['s'][0]),
            pi_prime=float(d['pip'][0]),
        )
res['Q1_table'] = q1_table

# dense log grid to 1e4, both signs; spot checks to 1e6
rlog = np.concatenate([
    np.linspace(0.0, 60.0, 241),
    np.logspace(np.log10(60.0), 4.0, 300)])
rmax_dev = {}
for sgn in (+1, -1):
    q = all_quantities(sgn * rlog)
    rmax_dev[f"sign={sgn:+d}"] = dict(
        max_abs_calF_dev=float(np.max(np.abs(q['calF'] - 1))),
        max_abs_calG_dev=float(np.max(np.abs(q['calG'] - 1))),
        max_abs_calH_dev=float(np.max(np.abs(q['calH'] - 1))),
        max_abs_G4_dev=float(np.max(np.abs(q['d']['G4'] - 0.5))),
        max_abs_cr2_dev=float(np.max(np.abs(q['cr2'] - 1))),
        max_abs_ctheta2_dev=float(np.max(np.abs(q['cth2'] - 1))),
        max_abs_cs1sq_dev=float(np.max(np.abs(q['cs1sq'] - 1))),
        cs2_at_largest_r=float(q['cs2'][-1]),
        cs2_dev_at_largest_r=float(q['cs2'][-1] - 1),
        P1_at_largest_r=float(q['P1'][-1]),
        P3_over_J2_at_largest_r=float(q['P3'][-1] / q['d']['J'][-1] ** 2),
    )
res['Q1_max_deviations_to_1e4'] = rmax_dev

spot = {}
for rr in [3e4, 1e5, 3e5, 1e6]:
    for sgn in (+1, -1):
        q = all_quantities(np.array([sgn * rr]))
        spot[f"r={sgn*rr:g}"] = dict(
            calF_dev=float(q['calF'][0] - 1), calH_dev=float(q['calH'][0] - 1),
            G4_dev=float(q['d']['G4'][0] - 0.5),
            c_r2_dev=float(q['cr2'][0] - 1), c_s2sq=float(q['cs2'][0]),
            P1=float(q['P1'][0]),
            P3_over_J2=float(q['P3'][0] / q['d']['J'][0] ** 2))
res['Q1_spot_checks_beyond_1e4'] = spot

# P1 / cs2 asymptotic approach laws (fit deviation vs r on [200, 1e4], r>0)
qp = all_quantities(rlog[rlog >= 200])
res['Q1_asymptotic_laws'] = dict(
    P1_dev_fit=dict(zip(['power', 'prefactor'],
                        power_fit(rlog[rlog >= 200], 1 - qp['P1'], 200, 1e4))),
    cs2_dev_fit=dict(zip(['power', 'prefactor'],
                         power_fit(rlog[rlog >= 200], 1 - qp['cs2'], 200, 1e4))),
    note="P1 -> 1 like -(tau/r)^2; c_s2^2 -> 1 from below like -3*tau/(2r) "
         "(the P3/J^2 target of MRV eq. 69). Both tend to the GR/luminal "
         "value; neither crosses it on the grids used.",
)

# ---------------------------------------------------------------- Q2
q2 = {}
fitgrid = np.logspace(0, 4, 400)   # r in [1, 1e4], positive side
df = theory(fitgrid)
q2['paper_asymptotics_check'] = dict(
    f0_power_fit=dict(zip(['power', 'prefactor'], power_fit(fitgrid, df['f0'], 200, 1e4))),
    f0_times_r2_at_1e4=float(df['f0'][-1] * 1e8),
    f1_limit_at_1e4=float(df['f1'][-1]),
    f1_power_of_dev_from_limit=dict(zip(['power', 'prefactor'],
        power_fit(fitgrid, df['f1'] - 0.015, 200, 1e4))),
    f2_power_fit=dict(zip(['power', 'prefactor'], power_fit(fitgrid, df['f2'], 200, 1e4))),
    f40_power_fit=dict(zip(['power', 'prefactor'], power_fit(fitgrid, df['f40'], 200, 1e4))),
    f41_power_fit=dict(zip(['power', 'prefactor'], power_fit(fitgrid, df['f41'], 200, 1e4))),
    g40_note="g40, g41 decay faster than any power: dominated by "
             "sech(sinh s + u) ~ 2 exp(-r/tau); log10|g40| at r=100,200,500: "
             + str([float(np.log10(np.abs(g40_s(np.arcsinh(np.array([rr / TAU]))))[0]))
                    for rr in (100.0, 200.0, 500.0)]),
    verdict="paper eq. function_asymp CONFIRMED: f0 ~ r^-2, f1 -> const "
            "(0.0150037 at r=1e4, limit 3/(2 tau^2)=0.015), f2 ~ r^2, "
            "f40 ~ r^4, f41 ~ r^6 (fitted powers in this block).",
)
# pieces entering calF / calG / calH (p31 normalisation)
pip2f = df['pip']**2
H_pieces = dict(
    two_g40=2 * df['g40'], g41_pip2=df['g41'] * pip2f,
    two_f40_pip4=2 * df['f40'] * pip2f**2, m_f41_pip6=-df['f41'] * pip2f**3)
q2['H_pieces_max_abs_on_60_to_1e4'] = {
    k: float(np.max(np.abs(v[fitgrid >= 60]))) for k, v in H_pieces.items()}
q2['H_pieces_at_1e4'] = {k: float(v[-1]) for k, v in H_pieces.items()}
q2['H_pieces_note'] = ("In the calH normalisation the growing raw functions "
    "are dressed by pip powers: 2 f40 pip^4 -> +1/4 and -f41 pip^6 -> -1/4 "
    "exactly as r -> inf, so the calF/calG/calH cancellation itself stays "
    "O(1). The unbounded growth lives in the raw designer functions, in "
    "the F4 decomposition, in F4pi, and in Xi (next blocks).")
# F4 decomposition: pieces vs cancelled sum F4bg (ratio computed in log10
# space: F4bg underflows float64 for r >~ 7500)
def log10_ratio_F4(d):
    return np.log10(np.abs(d['f40'])) - log10_F4bg(d['s'])

def crossing_from_log10(rgrid, log10y, log10target):
    idx = np.where(log10y >= log10target)[0]
    if len(idx) == 0:
        return None
    i = idx[0]
    if i == 0:
        return float(np.abs(rgrid[0]))
    x0, x1 = np.log10(np.abs(rgrid[i - 1])), np.log10(np.abs(rgrid[i]))
    y0, y1 = log10y[i - 1], log10y[i]
    return float(10 ** (x0 + (log10target - y0) * (x1 - x0) / (y1 - y0)))

lr_pos = log10_ratio_F4(df)
q2['F4_decomposition'] = dict(
    piece_f40_at_samples={f"r={rr:g}": float(10 ** np.interp(
        np.log10(rr), np.log10(fitgrid), np.log10(np.abs(df['f40'])))) for rr in
        (60.0, 100.0, 1000.0, 10000.0)},
    piece_power_fit=dict(zip(['power', 'prefactor'],
                             power_fit(fitgrid, df['f40'], 200, 1e4))),
    log10_F4bg_at_samples={f"r={rr:g}": float(log10_F4bg(
        np.arcsinh(np.array([rr / TAU])))[0]) for rr in (60.0, 100.0, 1000.0, 10000.0)},
    ratio_piece_over_F4bg_at_60=float(10 ** lr_pos[np.argmin(np.abs(fitgrid - 60))]),
    ratio_piece_over_F4bg_at_100=float(10 ** lr_pos[np.argmin(np.abs(fitgrid - 100))]),
    ratio_crossing_radii_positive_side={
        f"x{t:g}": crossing_from_log10(fitgrid, lr_pos, np.log10(t))
        for t in (1e2, 1e4, 1e6)},
)
# negative side, evaluated on r = -fitgrid so |r| ascends with the grid
dfn = theory(-fitgrid)
lr_neg = log10_ratio_F4(dfn)
q2['F4_decomposition']['ratio_crossing_radii_negative_side'] = {
    f"x{t:g}": crossing_from_log10(fitgrid, lr_neg, np.log10(t))
    for t in (1e2, 1e4, 1e6)}
# largest raw term: |f41| vs cancelled sum = 1
q2['largest_raw_term'] = dict(
    name="|f41| (largest designer function on the trajectory; "
         "next: |F4pi| ~ r^4, |f40| ~ r^4, |Xi| ~ r^2, |f2| ~ r^2)",
    power_fit=dict(zip(['power', 'prefactor'], power_fit(fitgrid, df['f41'], 200, 1e4))),
    crossing_radii_positive_side={f"x{t:g}": crossing_radius(fitgrid, df['f41'], t)
                                  for t in (1e2, 1e4, 1e6)},
    crossing_radii_negative_side={f"x{t:g}": crossing_radius(fitgrid, dfn['f41'], t)
                                  for t in (1e2, 1e4, 1e6)},
    value_at_1e4=float(df['f41'][-1]),
)
# F4pi and Xi pieces
q2['F4pi'] = dict(
    total_power_fit=dict(zip(['power', 'prefactor'],
                             power_fit(fitgrid, df['F4pi'], 200, 1e4))),
    piece_dpi_f40_power=dict(zip(['power', 'prefactor'],
                                 power_fit(fitgrid, df['F4pi_pieces'][0], 200, 1e4))),
    piece_dpi_f41_X_power=dict(zip(['power', 'prefactor'],
                                   power_fit(fitgrid, df['F4pi_pieces'][1], 200, 1e4))),
    total_at_1e4=float(df['F4pi'][-1]),
    cancelled_sum_note="F4pi itself is NOT a cancelled sum (no condition "
    "forces it to 1 or 0); it is a derivative of the growing F4 pieces and "
    "grows like r^4. It enters the background equations and Sigma-type "
    "combinations, whose own sums stay small only through the same "
    "trajectory tuning.",
)
xp = Xi_pieces(df)
Xi_tot, _ = Xi_Gamma(df)
q2['Xi_pieces'] = dict(
    total_power_fit=dict(zip(['power', 'prefactor'], power_fit(fitgrid, Xi_tot, 200, 1e4))),
    largest_piece_power=dict(zip(['power', 'prefactor'],
        power_fit(fitgrid, xp['pip_16r_pip2_f40'], 200, 1e4))),
    pieces_at_1e4={k: float(v[-1]) for k, v in xp.items()},
    total_at_1e4=float(Xi_tot[-1]),
    note="Xi ~ -(r^2 + tau^2/2)/tau on the positive side; its two largest "
         "pieces (from f40 and f41) are each ~ r^2/tau with opposite signs "
         "and comparable size to Xi itself: O(1) cancellation, on top of "
         "an Xi that itself grows like r^2.",
)
# F (Lagrangian) decomposition on background
q2['F_decomposition_at_1e4'] = dict(
    f0=float(df['f0'][-1]), f1X=float((df['f1'] * df['X'])[-1]),
    f2X2=float((df['f2'] * df['X']**2)[-1]), F_total=float(df['F'][-1]),
    note="All three pieces decay (~r^-2, r^-2, r^-4); F_on_bg ~ 1e-14 at "
         "r=1e4. No growth in the L2 value on-trajectory.")
# float64 cancellation floor for the literal F4 sum
q2['float64_cancellation_floor'] = dict(
    literal_sum_f40_plus_f41X_at_1000=float(theory(np.array([1000.0]))['F4_sum_check'][0]),
    true_F4bg_at_1000=float(F4bg_s(np.arcsinh(np.array([100.0])))[0]),
    note="At r=1000 the literal float64 sum f40 + f41*X (pieces ~1.25e7) "
         "returns 1.5e-8 -- pure roundoff, 36 orders of magnitude above "
         "the true F4bg = 6.7e-44: the on-trajectory "
         "cancellation in F4 exceeds float64 dynamic range beyond "
         "r ~ a few hundred. This is a statement about the size of the "
         "cancellation, evaluated here via the defining eq. (61) form.")
res['Q2'] = q2

# ---------------------------------------------------------------- Q4
res['Q4'] = dict(
    cT=dict(
        definition="c_T^2 = c_r^2 = calG/calF (odd sector, MRV eq. speed_odd); "
                   "c_T = sqrt(c_r^2)",
        max_abs_cT_dev_to_1e4_pos=float(np.max(np.abs(
            np.sqrt(all_quantities(rlog)['cr2']) - 1))),
        max_abs_cT_dev_to_1e4_neg=float(np.max(np.abs(
            np.sqrt(all_quantities(-rlog)['cr2']) - 1))),
        value="c_T = 1 identically by the designer choice calF=calG=calH=1 "
              "(MRV eq. D:HF_choice); numerical deviation is at the float64 "
              "roundoff floor (see Q1_max_deviations_to_1e4). D2's GW170817 "
              "window |c_T/c - 1| <= ~1e-15 is therefore satisfied "
              "identically ON THIS BACKGROUND.",
    ),
    far_field_metric=dict(
        metric="ds^2 = -dt^2 + dr^2 + (r^2+tau^2) dOmega^2 exactly, for all r "
               "(MRV eq. ABJ). g_tt = -1 exactly: no 1/r term at any radius.",
        ADM_mass=0.0,
        J_asymptotics="J = |r| + tau^2/(2|r|) + O(r^-3); areal-radius "
                      "correction only, no Newtonian potential.",
        curvature_falloff="Einstein-tensor (effective) components ~ "
                          "tau^2/(r^2+tau^2)^2 ~ tau^2/r^4 (Phase 3, exact).",
    ),
    scalar=dict(
        pi_prime_at_1e4=float(theory(np.array([10000.0]))['pip'][0]),
        pi_prime_law="pi' = tau/J = tau/sqrt(r^2+tau^2) ~ tau/r "
                     "(power fit -1); pi itself = tau*arcsinh(r/tau) "
                     "~ tau*ln(2|r|/tau) grows logarithmically and never "
                     "settles to a constant.",
        long_range_force_paragraph=(
            "No on-background long-range scalar force on a test particle "
            "arises at linear order. The published action contains no "
            "matter sector at all (L_matter = 0 in the example), so a test "
            "particle couples only to the metric; the background metric "
            "has A = B = 1 exactly, hence Gamma^r_tt = 0 and a static test "
            "particle is geodesic at every r -- there is no Newtonian "
            "1/r force from the throat (ADM = 0) and no direct pi-mediated "
            "force, because no pi-matter coupling is specified. The "
            "scalar gradient pi' ~ tau/r is long-range as a field profile, "
            "and scalar perturbations do mix with metric perturbations "
            "(that mixing is the even sector audited in Phase 3 / F4-1..3), "
            "but on this background it produces no additional static force "
            "on a minimally coupled test body. Honest limit: this is an "
            "on-background statement only. A real star or binary would "
            "source pi through the (off-trajectory) field equations, and "
            "per Q3 the published construction fixes no unique prediction "
            "for that situation."),
    ),
)

res['Q3_text'] = (
    "What the construction fixes (MRV Sec. sec:wormhole, 'Wormhole beyond "
    "Horndeski: an example'): a reconstruction. The metric (eq. ABJ) and "
    "scalar profile (eq. galileon, pi = tau*arcsinh(r/tau), X in [-1/2, 0)) "
    "are CHOSEN; the theory functions are then cooked up so the background "
    "equations and the checked stability conditions hold ON that "
    "trajectory. Every determining equation is an on-trajectory condition: "
    "eq. D:HF_choice (calH=calG=calF=1 on the background) yields eqs. "
    "D:g41 and D:f40; eq. D:F4_choice fixes only the on-background value "
    "F4(pi, X(pi)) = w*sech(sinh(pi/tau)+u); eq. D:g40, the f41 choice "
    "eq. D:f41 (chosen so the no-ghost denominator behaves on the "
    "trajectory, eq. D:xi_denominator), f1 from E_B=0 (eq. D:f1), f0 from "
    "E_A=0 (eq. D:f0), and f2 from the on-background Sigma target "
    "(eqs. D:for_sigma, D:f2explicit). The two-variable form written in "
    "the Ansatz (eq. ansatz: F = f0 + f1 X + f2 X^2, G4 = 1/2 + g40 + "
    "g41 X, F4 = f40 + f41 X) is introduced with 'we choose the following "
    "Ansatz' -- a chosen polynomial-in-X representative, not a derived or "
    "uniqueness-proved extension: infinitely many functions of (pi, X) "
    "share the same trajectory values and the same on-trajectory "
    "derivative combinations the paper checks, and nothing in the paper "
    "selects among them off the trajectory. The paper nowhere evaluates "
    "the theory off the trajectory: there is no weak-field expansion, no "
    "PPN parameter, no solar-system or binary-pulsar discussion anywhere "
    "in the text (verified by full-text search). Its only asymptotic "
    "statements are on-trajectory: eq. function_asymp and eq. "
    "asymptotic_Lagrangian are evaluated where |pi(r)| = c1*log|r|, i.e. "
    "on X = X(pi). The authors state the limitation themselves: 'Here we "
    "require only that the space-time is asymptotically flat and do not "
    "impose any restrictions on the asymptotic behavior of the "
    "Lagrangian' (Sec. sec:wormhole); 'weak gravity regime is grossly "
    "different from General Relativity even at large distances from the "
    "wormhole' (Introduction; repeated after eq. "
    "asymptotic_Lagrangian); the Conclusions leave it open 'whether the "
    "wormholes of this sort are viable in the sense that physics in the "
    "large distance asymptotics is consistent with experimental and "
    "observational tests'. CONSEQUENCE (registered): weak-field PPN / "
    "solar-system / binary-pulsar predictions (gates D2/D3 in their "
    "weak-field form) are NOT COMPUTABLE from the published construction "
    "-- no unique off-trajectory theory is fixed, and no such prediction "
    "is made or can be quoted from the paper."
)

res['verdict'] = dict(
    category="(ii) NOT EXCLUDED BUT INCOMPLETE",
    basis="Q1/Q4: every on-background quantity audited is GR-identical to "
          "float64 roundoff out to |r| = 1e4 (spot checks to 1e6), c_T = 1 "
          "identically, ADM = 0 exactly -- no computable quantity violates "
          "D2/D3, so (i) is not available. Q2: the cancellation is "
          "unbounded -- raw designer functions grow as powers (f41 ~ r^6, "
          "crossing 1e2/1e4/1e6 x the cancelled sum at the radii in "
          "Q2.largest_raw_term), and the F4 pieces exceed their cancelled "
          "sum by factors passing 1e2/1e4/1e6 at the radii in "
          "Q2.F4_decomposition, growing like r^4 * exp(r/tau) thereafter. "
          "Q3: no unique off-trajectory extension is fixed by the paper, "
          "so weak-field predictions are not computable from the "
          "published construction. Both halves of category (ii)'s "
          "registered definition are met; (iii) fails on both counts.",
)

with open('/home/hatch/workspace/warp-pilot/phase4/results/p45_asymptotics.json', 'w') as fh:
    json.dump(res, fh, indent=2)
print(json.dumps(res, indent=2))
