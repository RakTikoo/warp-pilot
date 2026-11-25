"""Gate G2: exact BSKR solution (EPJC App D) vs Einstein (G=2T),
Dirac (3.11), Maxwell (3.12). Symbolic derivatives, numeric eval."""
import sympy as sp
import numpy as np, json

l = sp.symbols('l', real=True)

def build(Qev, c0v, r0v=1.0, kap=1):
    F2 = sp.sqrt(l**2 + r0v**2)
    F0 = 1 - (2 * Qev**2 * r0v / (Qev**2 + r0v**2)) / F2
    F1 = sp.sqrt(1 + r0v / F2) / sp.sqrt(1 - Qev**2 / (r0v * F2))
    sq1 = sp.sqrt(1 - Qev**2 / (r0v * F2)); sq2 = sp.sqrt(1 - r0v / F2)
    U1 = c0v / sp.sqrt(F0) * (sq1 - kap * sq2)**2
    U2 = kap * r0v / (32 * c0v * (Qev**2 + r0v**2) * sp.sqrt(F0)) * (sq1 + kap * sq2)**2
    P = U1 - U2; Q = U1 + U2
    V = (2 * Qev * r0v / (Qev**2 + r0v**2)) * sp.sqrt((1 - Qev**2 / (r0v * F2)) * (1 - r0v / F2))
    exprs = {}
    for nm, f in [('F0', F0), ('F1', F1), ('F2', F2), ('P', P), ('Q', Q), ('V', V)]:
        exprs[nm] = f; exprs[nm + 'd'] = sp.diff(f, l); exprs[nm + 'dd'] = sp.diff(f, l, 2)
    return {k: sp.lambdify(l, v, 'numpy') for k, v in exprs.items()}

def Gcomps(lv, F0v, F1v, F0d, F1d, F0dd, r0=1.0):
    R2 = lv**2 + r0**2
    Gtt = (-2 * lv * R2 * F1d - R2 * F1v**3 + (lv**2 + 2 * r0**2) * F1v) / (R2**2 * F1v**3)
    Gll = (2 * lv * R2 * F0d - R2 * F0v * F1v**2 + lv**2 * F0v) / (R2**2 * F0v * F1v**2)
    num = (lv**4 * F1v * F0dd - lv**4 * F0d * F1d - lv**3 * F0v * F1d + lv**3 * F1v * F0d
           + 2 * lv**2 * r0**2 * F1v * F0dd - 2 * lv**2 * r0**2 * F0d * F1d
           - lv * r0**2 * F0v * F1d + lv * r0**2 * F1v * F0d
           + r0**4 * F1v * F0dd - r0**4 * F0d * F1d + r0**2 * F0v * F1v)
    Gth = num / (R2**2 * F0v * F1v**3)
    return Gtt, Gll, Gth

def audit(Qev, c0v):
    lam = build(Qev, c0v)
    out = []
    for lv in [0.0, 0.05, 0.2, 0.5, 1.0, 2.0, 5.0, 20.0, 100.0]:
        v = {k: float(f(lv)) for k, f in lam.items()}
        R = np.sqrt(lv**2 + 1.0)
        Gtt, Gll, Gth = Gcomps(lv, v['F0'], v['F1'], v['F0d'], v['F1d'], v['F0dd'])
        # Dirac T (w=mu=q=0), kappa=1
        TDtt = 0.0
        TDll = 4 * (v['Pd'] * v['Q'] - v['P'] * v['Qd']) / v['F1']
        TDth = 2 * (v['Q']**2 - v['P']**2) / R
        E2 = (v['Vd'] / (v['F0'] * v['F1']))**2
        TMtt = -0.5 * E2; TMll = -0.5 * E2; TMth = 0.5 * E2
        resE = [Gtt - 2 * (TDtt + TMtt), Gll - 2 * (TDll + TMll), Gth - 2 * (TDth + TMth)]
        # Dirac eqs (3.11), eps_r=+1, eps_t=+1, w=q=mu=0, kappa=1:
        # P' + (F0'/(2F0)+F2'/F2) P + (F1/F2)(1) Q = 0 ; Q' + (...) Q + (F1/F2)(1) P = 0
        br = v['F0d'] / (2 * v['F0']) + v['F2d'] / v['F2']
        resD = [v['Pd'] + br * v['P'] + (v['F1'] / v['F2']) * v['Q'],
                v['Qd'] + br * v['Q'] + (v['F1'] / v['F2']) * v['P']]
        # Maxwell (3.12): (F2^2 V'/(F0 F1))' = 0 (q=0)
        resM = v['F2']**2 * v['Vdd'] / (v['F0'] * v['F1']) + v['Vd'] * (2 * v['F2'] * v['F2d'] / (v['F0'] * v['F1'])
               - v['F2']**2 / (v['F0'] * v['F1']) * (v['F0d'] / v['F0'] + v['F1d'] / v['F1']))
        out.append(dict(l=lv, resE=resE, resD=resD, resM=resM,
                        G=[Gtt, Gll, Gth], TD=[TDtt, TDll, TDth], TM=[TMtt, TMll, TMth]))
    return out

if __name__ == '__main__':
    for Qev, c0v in [(0.5, 1.0), (0.5, 0.5), (0.5, 2.0), (0.25, 1.0)]:
        rows = audit(Qev, c0v)
        mE = max(abs(x) for r in rows for x in r['resE'])
        mD = max(abs(x) for r in rows for x in r['resD'])
        mM = max(abs(r['resM']) for r in rows)
        print(f'Qe={Qev} c0={c0v}: max|Einstein res|={mE:.3e}  max|Dirac res|={mD:.3e}  max|Maxwell res|={mM:.3e}')
        for r in rows[:3]:
            print('   l=', r['l'], 'resE=', ['%.2e' % x for x in r['resE']], 'resD=', ['%.2e' % x for x in r['resD']])
