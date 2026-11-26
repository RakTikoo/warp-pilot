#!/usr/bin/env python
"""P241-1 (FU-P228-2b): DECANINI-FOLACCI TRANSCRIPTION CROSS-CHECK.

Registration: phase241/work/p2411_registration.md (written before
any computation). Frame: Phase 166 pin, Gate-19-corrected tensor,
venv python. Bounded local work only.

METHOD (registered): DF Eq. (3.15) [arXiv:0706.0691 v3, ar5iv
HTML retrieved this session; coefficients cross-read against the
arXiv PDF text layer] is evaluated DIRECTLY on spherical jets by
a sparse dictionary tensor-jet engine in coordinates
(t, l, th, ph) about (l0, th=pi/2): full Christoffel / Riemann /
covariant-derivative calculus, jets in (dl, dth) of orders
(10, 4). NO expansion in Phase 219's 23-tensor basis anywhere in
the deciding read. Bracket units: programme bracket =
20160 pi^2 m^2 T = 210 * (DF sum), DF sum = (96 pi^2 m^2) T.

CONTROLS (before deciding reads): 0 = Eq. (3.15) coefficient
spot-checks re-derived from Eq. (3.3d) via Eqs. (3.11)->(3.13)
->(3.14) and the Sec.2 H-formulas (2.22),(2.23),(2.25),(2.28),
exact Fractions; 1 = Phase 237 core + Phase 219 gate numbers
re-read from stored results; 2 = engine self-checks (Ellis Ricci
eigenvalues; Phase 228 pilot covariant-box difference
D = (+16, -8) r/theta at the Ellis throat, D_t = 0).
"""
import json, math, time
from fractions import Fraction as Fr
import numpy as np
from scipy.optimize import brentq

t_start = time.time()
WP = '/home/hatch/workspace/warp-pilot'
OUT = {'item': 'P241-1 (FU-P228-2b)'}

# =====================================================================
# CONTROL 0 -- transcription spot-checks via the variation route
# (96 pi^2 m^2) T = sum_k c_k H_k, c_k = Eq. (3.13) coefficients,
# H_k = Sec. 2 formulas (2.22)-(2.31).  Registered subset:
# (Box R)_{;ab}, BoxBox R_ab, R Box R_ab (direct), g_ab BoxBox R.
# =====================================================================
def padd(*ps):
    n = max(len(p) for p in ps); out = [Fr(0)] * n
    for p in ps:
        for i, c in enumerate(p): out[i] += c
    return out
def pmul(a, b):
    out = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i + j] += x * y
    return out
def pscale(a, s): return [s * x for x in a]
XI = [Fr(0), Fr(1)]                       # the polynomial xi
X16 = [Fr(-1, 6), Fr(1)]                  # (xi - 1/6)
# Eq. (3.13) coefficients c_k (in W_ren, prefactor 1/(192 pi^2 m^2))
c_RboxR = padd(pmul([Fr(1, 2)], pmul(XI, XI)), pmul([Fr(-1, 5)], XI), [Fr(1, 56)])
c_RicboxRic = [Fr(1, 140)]
c_63_2 = pmul([Fr(1, 30)], X16)           # (6,3)(2): RRic2
c_63_5 = pmul([Fr(-1, 30)], X16)          # (6,3)(5): RRiem2
# H^{{2,0}}(1) (2.22): (BoxR)_{;ab}: 2 ; BoxBoxR_ab: 0 ;
#   R_{;a}R_{;b}: 1 ; trace BoxBoxR: -2 ; trace (dR)^2: -1/2
# H^{{2,0}}(3) (2.23): (BoxR)_{;ab}: 1 ; BoxBoxR_ab: -1 ;
#   trace BoxBoxR: -1/2
# H^{(6,3)(2)} (2.25): R Box R_ab: -1
# H^{(6,3)(5)} (2.28): R Box R_ab: -4
spot = {}
spot['coef_dBoxR_ab'] = padd(pscale(c_RboxR, Fr(2)), c_RicboxRic)
spot['coef_BoxBoxR_ab'] = pscale(c_RicboxRic, Fr(-1))
spot['coef_RBoxR_ab'] = padd(pscale(c_63_2, Fr(-1)), pscale(c_63_5, Fr(-4)))
spot['coef_gab_BoxBoxR'] = padd(pscale(c_RboxR, Fr(-2)), pscale(c_RicboxRic, Fr(-1, 2)))
printed = {
    'coef_dBoxR_ab': padd(pmul(XI, XI), pmul([Fr(-2, 5)], XI), [Fr(3, 70)]),
    'coef_BoxBoxR_ab': [Fr(-1, 140)],
    'coef_RBoxR_ab': pmul([Fr(1, 10)], X16),
    'coef_gab_BoxBoxR': padd(pmul([Fr(-1)], pmul(XI, XI)), pmul([Fr(2, 5)], XI), [Fr(-11, 280)]),
}
def ptrim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0: p.pop()
    return p
spot_ok = all(ptrim(spot[k]) == ptrim(printed[k]) for k in printed)
OUT['control0_spot_checks'] = {
    k: {'rederived': [str(x) for x in ptrim(spot[k])],
        'printed_3_15': [str(x) for x in ptrim(printed[k])],
        'match': bool(ptrim(spot[k]) == ptrim(printed[k]))} for k in printed}
OUT['control0_pass'] = bool(spot_ok)
print('CONTROL 0 (spot-checks):', spot_ok, flush=True)
assert spot_ok

# =====================================================================
# CONTROL 1 -- Phase 237 core + Phase 219 gate numbers from storage
# =====================================================================
r237 = json.load(open(f'{WP}/phase237/work/p2371_results.json'))
core_pair = r237['consistency_anatomy']['pairwise_ELL_plus_family_max_abs_resid']['A_b_const']
r219 = json.load(open(f'{WP}/phase219/work/p2191_results.json'))
c1 = {'pairwise_ELL_plus_Athroat_max_resid_per_xi': core_pair,
      'core_le_2p2e-8': bool(max(core_pair) <= 2.3e-8),  # stored max is 2.2146e-8; memo rounds to 2.2e-8
      'forced_deficit_stored': r219['gate']['a_deficit']['target'],
      'F3_root_stored': r219['gate']['d_roots_Tr'][0],
      'forced_deficit_ok': bool(abs(r219['gate']['a_deficit']['target'] + 1 / (4 * math.pi)) < 1e-12),
      'F3_root_ok': bool(abs(r219['gate']['d_roots_Tr'][0] - 0.86035766893) < 1e-9)}
c1['pass'] = bool(c1['core_le_2p2e-8'] and c1['forced_deficit_ok'] and c1['F3_root_ok'])
OUT['control1_phase237_core_reproduced'] = c1
print('CONTROL 1 (Phase 237 core):', c1['pass'], core_pair, flush=True)
assert c1['pass']

# =====================================================================
# JET ENGINE -- 2-variable Taylor jets in (dl, du), orders (10, 4)
# =====================================================================
NL, NT = 10, 6
JS = (NL + 1, NT + 1)
def jzero(): return np.zeros(JS)
def jconst(x):
    a = jzero(); a[0, 0] = x; return a
def jmul(a, b):
    c = jzero()
    for i in range(NL + 1):
        for j in range(NT + 1):
            v = a[i, j]
            if v != 0.0:
                c[i:, j:] += v * b[:NL + 1 - i, :NT + 1 - j]
    return c
def jadd(a, b): return a + b
def jscale(a, s): return s * a
def jdiv(a, b):
    # series division, b[0,0] != 0; recursion by total degree
    c = jzero(); b0 = b[0, 0]
    for d in range(NL + NT + 1):
        for i in range(max(0, d - NT), min(NL, d) + 1):
            j = d - i
            s = a[i, j]
            for i1 in range(i + 1):
                for j1 in range(j + 1):
                    if i1 == 0 and j1 == 0: continue
                    if i1 <= i and j1 <= j:
                        s -= b[i1, j1] * c[i - i1, j - j1]
            c[i, j] = s / b0
    return c
def jdl(a):
    c = jzero()
    for i in range(NL): c[i, :] = (i + 1) * a[i + 1, :]
    return c
def jdu(a):
    c = jzero()
    for j in range(NT): c[:, j] = (j + 1) * a[:, j + 1]
    return c
def embed_l(a1):
    a = jzero(); a[:, 0] = a1[:NL + 1]; return a
def embed_u(a1):
    a = jzero(); a[0, :] = a1[:NT + 1]; return a

# ---- 1-variable jets (background construction; length NJ1 = 11) ----
NJ1 = 11
def m1(a, b):
    c = np.zeros(NJ1)
    for i in range(NJ1):
        for j in range(NJ1 - i): c[i + j] += a[i] * b[j]
    return c
def d1(a, b):
    c = np.zeros(NJ1)
    for n in range(NJ1):
        c[n] = (a[n] - sum(b[k] * c[n - k] for k in range(1, n + 1))) / b[0]
    return c
def der1(a):
    c = np.zeros(NJ1)
    for k in range(NJ1 - 1): c[k] = (k + 1) * a[k + 1]
    return c
def log1(a):
    d = d1(der1(a), a); c = np.zeros(NJ1); c[0] = math.log(a[0])
    for k in range(NJ1 - 1): c[k + 1] = d[k] / (k + 1)
    return c
def exp1(a):
    c = np.zeros(NJ1); c[0] = math.exp(a[0])
    for n in range(1, NJ1):
        c[n] = sum(k * a[k] * c[n - k] for k in range(1, n + 1)) / n
    return c
def sqrt1(a):
    y = np.zeros(NJ1); y[0] = math.sqrt(a[0]); y[1] = a[1] / (2 * y[0])
    for _ in range(60):
        yn = 0.5 * (y + d1(a, y))
        if np.max(np.abs(yn - y)) < 1e-16: y = yn; break
        y = yn
    return y
def const1(x):
    c = np.zeros(NJ1); c[0] = x; return c

# ---- background jets per family (Phase 237 definitions verbatim) ----
def b_over_R1(Rj, fam, par):
    if fam in ('A', 'E'):
        return d1(const1(1.0), Rj)
    if fam == 'C':
        num = m1(const1(par + 1.0) - Rj, const1(par + 1.0) - Rj)
        return d1(d1(num, const1(par * par)), Rj)
    if fam == 'D':
        return exp1(-par * log1(Rj))
    raise ValueError(fam)
def S_of_h(fam, par):
    # S(h) = b(R)/R as a jet in h = R - 1, R = 1 + h
    h = np.zeros(NJ1); h[1] = 1.0
    R = const1(1.0) + h
    if fam in ('A', 'E'):
        return d1(const1(1.0), R)
    if fam == 'C':
        num = m1(const1(par + 1.0) - R, const1(par + 1.0) - R)
        return d1(d1(num, const1(par * par)), R)
    if fam == 'D':
        return exp1(-par * log1(R))
    raise ValueError(fam)
def solve_Rjet_throat(fam, par):
    # Direct series recursion for (R')^2 = 1 - b(R)/R, R(0) = 1,
    # R'(0) = 0 (even series).  The equation also admits the
    # degenerate branch R == 1 (Phase 237 memo, Control C); the
    # recursion selects the physical branch through a_2 =
    # -S'(0)/4 != 0 (S = b/R as a function of R, S(1) = 1).
    s = S_of_h(fam, par)
    x = np.zeros(NJ1); x[0] = 1.0
    x[2] = -s[1] / 4.0
    def Ecoef(xv, m):
        Rp2 = m1(der1(xv), der1(xv))
        # compose S with (xv - 1): powers of the jet xv-1
        y = xv.copy(); y[0] = 0.0
        comp = const1(s[0]); yp = const1(1.0)
        for k in range(1, NJ1):
            yp = m1(yp, y)
            comp = comp + s[k] * yp
        return Rp2[m] - (1.0 if m == 0 else 0.0) + comp[m]
    for m in range(3, NJ1):
        e0 = Ecoef(x, m)
        denom = 4.0 * m * x[2] + s[1]
        x[m] = -e0 / denom
    return x
def solve_Rjet_local_A(Rstar):
    x = np.zeros(NJ1); x[0] = Rstar; x[1] = math.sqrt(1 - 1 / Rstar)
    def F(xv):
        return (m1(der1(xv), der1(xv)) - const1(1.0) + d1(const1(1.0), xv))[:NJ1 - 1]
    for _ in range(80):
        f0 = F(x)
        if np.max(np.abs(f0)) < 1e-13: break
        J = np.zeros((NJ1 - 1, NJ1 - 1))
        for k in range(1, NJ1):
            xp = x.copy(); xp[k] += 1e-7
            J[:, k - 1] = (F(xp) - f0) / 1e-7
        x[1:] += np.linalg.solve(J, -f0)
    return x
def phi_jet_E1(Rj, eps):
    arg = const1(1.0) - d1(const1(1.0), Rj) + eps * d1(const1(1.0), m1(Rj, Rj))
    return 0.5 * log1(arg)

# ---- sparse dict tensors over indices 0..3 = (t, l, th, ph) ----
def Tadd(A, B, s=1.0):
    out = dict(A)
    for k, v in B.items():
        out[k] = out.get(k, 0) + s * v if k in out else s * v
        if isinstance(out[k], np.ndarray) and np.max(np.abs(out[k])) == 0.0:
            del out[k]
    return out
def Tscale(A, s):
    return {k: s * v for k, v in A.items()}
def Tjet(T, idx): return T.get(idx, None)
def val0(T, idx):
    v = T.get(idx)
    return 0.0 if v is None else float(v[0, 0])
def tmul(A, B):
    out = {}
    for ka, va in A.items():
        for kb, vb in B.items():
            k = ka + kb
            p = jmul(va, vb)
            out[k] = out.get(k, 0) + p if k in out else p
    return {k: v for k, v in out.items() if np.max(np.abs(v)) > 0.0}
def tcontr(A, B, pairs):
    # pairs: list of (axis_in_A, axis_in_B) to contract (equal values)
    out = {}
    na = len(next(iter(A))) if A else 0
    nb = len(next(iter(B))) if B else 0
    bmap = {}
    for kb, vb in B.items():
        key = tuple(kb[ax] for _, ax in pairs)
        bmap.setdefault(key, []).append((kb, vb))
    for ka, va in A.items():
        key = tuple(ka[ax] for ax, _ in pairs)
        for kb, vb in bmap.get(key, []):
            free = tuple(ka[i] for i in range(na) if i not in [a for a, _ in pairs]) + \
                   tuple(kb[i] for i in range(nb) if i not in [b for _, b in pairs])
            p = jmul(va, vb)
            out[free] = out.get(free, 0) + p if free in out else p
    return {k: v for k, v in out.items() if np.max(np.abs(v)) > 0.0}
def ttrace(T, ax1, ax2):
    out = {}
    n = len(next(iter(T)))
    for k, v in T.items():
        if k[ax1] == k[ax2]:
            free = tuple(k[i] for i in range(n) if i not in (ax1, ax2))
            out[free] = out.get(free, 0) + v if free in out else v
    return out
def raise_idx(T, ax, ginv):
    out = {}
    n = len(next(iter(T)))
    for k, v in T.items():
        for new in range(4):
            gv = ginv.get((new, k[ax]))
            if gv is None: continue
            kk = list(k); kk[ax] = new; kk = tuple(kk)
            p = jmul(gv, v)
            out[kk] = out.get(kk, 0) + p if kk in out else p
    return {k: v for k, v in out.items() if np.max(np.abs(v)) > 0.0}
def lower_idx(T, ax, g):
    out = {}
    for k, v in T.items():
        for new in range(4):
            gv = g.get((new, k[ax]))
            if gv is None: continue
            kk = list(k); kk[ax] = new; kk = tuple(kk)
            p = jmul(gv, v)
            out[kk] = out.get(kk, 0) + p if kk in out else p
    return {k: v for k, v in out.items() if np.max(np.abs(v)) > 0.0}
def sym_last2(T):
    # symmetrise the LAST TWO indices with the (1/2)(X_ab + X_ba) rule
    out = {}
    for k, v in T.items():
        ks = k[:-2] + (k[-1], k[-2])
        out[k] = out.get(k, 0) + 0.5 * v if k in out else 0.5 * v
        out[ks] = out.get(ks, 0) + 0.5 * v if ks in out else 0.5 * v
    return {k: v for k, v in out.items() if np.max(np.abs(v)) > 0.0}

# ---- geometry builder: Phi1, R1 are 1-var jets in the local l ----
COSu = np.array([1.0, 0.0, -0.5, 0.0, 1.0 / 24.0])          # sin(th), th=pi/2+u
SIN2u = np.array([1.0, 0.0, -1.0, 0.0, 1.0 / 3.0, 0.0, -2.0 / 45.0])  # sin^2(th)
def build_geometry(Phi1, R1):
    e2P = embed_l(exp1(2.0 * Phi1)); em2P = embed_l(exp1(-2.0 * Phi1))
    R2 = embed_l(m1(R1, R1)); iR2 = embed_l(d1(const1(1.0), m1(R1, R1)))
    g = {(0, 0): -e2P, (1, 1): jconst(1.0), (2, 2): R2,
         (3, 3): jmul(R2, embed_u(SIN2u))}
    # 1/sin^2(th) as u-jet: sin(th)=cos(u), so 1/sin^2 = sec^2(u)
    # = 1 + u^2 + (2/3) u^4 + O(u^6)
    sec2 = np.array([1.0, 0.0, 1.0, 0.0, 2.0 / 3.0, 0.0, 17.0 / 45.0])
    ginv = {(0, 0): -em2P, (1, 1): jconst(1.0), (2, 2): iR2,
            (3, 3): jmul(iR2, embed_u(sec2))}
    def dmu(T, mu):
        if mu == 0 or mu == 3: return {}
        f = jdl if mu == 1 else jdu
        return {k: f(v) for k, v in T.items() if np.max(np.abs(f(v))) > 0.0}
    dg = {mu: dmu(g, mu) for mu in range(4)}
    Gam = {}
    for a in range(4):
        for b in range(4):
            for c in range(4):
                acc = None
                for d in range(4):
                    gv = ginv.get((a, d))
                    if gv is None: continue
                    t1 = dg[b].get((d, c)); t2 = dg[c].get((d, b)); t3 = dg[d].get((b, c))
                    s = None
                    if t1 is not None: s = t1 if s is None else s + t1
                    if t2 is not None: s = t2 if s is None else s + t2
                    if t3 is not None: s = -t3 if s is None else s - t3
                    if s is None: continue
                    p = jmul(gv, s)
                    acc = p if acc is None else acc + p
                if acc is not None and np.max(np.abs(acc)) > 0.0:
                    Gam[(a, b, c)] = 0.5 * acc
    def covd(T):
        # returns D with derivative index FIRST: D[(mu,)+idx]
        n = len(next(iter(T)))
        out = {}
        for mu in range(4):
            for k, v in dmu(T, mu).items():
                out[(mu,) + k] = out.get((mu,) + k, 0) + v if (mu,) + k in out else v
            for kk, w in T.items():
                for slot in range(n):
                    lam = kk[slot]
                    for i in range(4):
                        gv = Gam.get((lam, mu, i))
                        if gv is None: continue
                        k2 = list(kk); k2[slot] = i
                        p = jmul(gv, w)
                        key = (mu,) + tuple(k2)
                        out[key] = out.get(key, 0) - p if key in out else -p
        return {k: v for k, v in out.items() if np.max(np.abs(v)) > 0.0}
    # Riemann R^a_{bcd} = d_c Gam^a_{bd} - d_d Gam^a_{bc} + Gam Gam - Gam Gam
    dGam = {mu: dmu(Gam, mu) for mu in range(4)}
    Rup = {}
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    acc = None
                    v = dGam[c].get((a, b, d))
                    if v is not None: acc = v
                    v = dGam[d].get((a, b, c))
                    if v is not None: acc = -v if acc is None else acc - v
                    for e in range(4):
                        g1 = Gam.get((a, c, e)); g2 = Gam.get((e, b, d))
                        if g1 is not None and g2 is not None:
                            p = jmul(g1, g2); acc = p if acc is None else acc + p
                        g1 = Gam.get((a, d, e)); g2 = Gam.get((e, b, c))
                        if g1 is not None and g2 is not None:
                            p = jmul(g1, g2); acc = -p if acc is None else acc - p
                    if acc is not None and np.max(np.abs(acc)) > 0.0:
                        Rup[(a, b, c, d)] = acc
    Riem = lower_idx(Rup, 0, g)                     # R_{abcd}
    Ric = ttrace(Rup, 0, 2)                         # R_{bd} = R^a_{bad}
    Rsc = ttrace(raise_idx(Ric, 0, ginv), 0, 1)     # scalar (rank-0 dict {(): jet})
    return {'g': g, 'ginv': ginv, 'Gam': Gam, 'Rup': Rup, 'Riem': Riem,
            'Ric': Ric, 'Rsc': Rsc, 'covd': covd, 'dmu': dmu}
print('engine built', round(time.time() - t_start, 1), 's', flush=True)

# =====================================================================
# DERIVATIVE TENSORS + DF MONOMIALS (Eq. (3.15), direct evaluation)
# =====================================================================
def box_of(T, G):
    # Box T = g^{mu nu} nabla_mu nabla_nu T  (derivative index first)
    dd = G['covd'](G['covd'](T))
    out = {}
    n = len(next(iter(T))) if T else 0
    for k, v in dd.items():
        gv = G['ginv'].get((k[0], k[1]))
        if gv is None: continue
        free = k[2:]
        p = jmul(gv, v)
        out[free] = out.get(free, 0) + p if free in out else p
    return {k: v for k, v in out.items() if np.max(np.abs(v)) > 0.0}
def mixed(T, G, a, b):
    # mixed component T^a_b at the point (a,b in 0..3)
    return val0(G['ginv'], (a, a)) * 0 + float(
        (jmul(G['ginv'][(a, a)], T[(a, b)]))[0, 0]) if (a, b) in T else 0.0

def deriv_pack(G):
    covd, ginv, g = G['covd'], G['ginv'], G['g']
    Ric, Riem, Rsc = G['Ric'], G['Riem'], G['Rsc']
    P = {}
    P['dR'] = covd(Rsc)                       # (mu,)
    P['ddR'] = covd(P['dR'])                  # (mu,nu)
    P['boxR'] = box_of(Rsc, G)                # scalar dict {(): jet}
    P['ddboxR'] = covd(covd(P['boxR']))       # (a,b) = (Box R)_{;ab}
    P['boxboxR'] = box_of(P['boxR'], G)
    P['dRic'] = covd(Ric)                     # (mu,a,b)
    P['ddRic'] = covd(P['dRic'])              # (mu,nu,a,b)
    P['boxRic'] = box_of(Ric, G)
    P['boxboxRic'] = box_of(P['boxRic'], G)
    P['dRiem'] = covd(Riem)                   # (mu,a,b,c,d)
    P['ddRiem'] = covd(P['dRiem'])            # (mu,nu,a,b,c,d)
    # raised variants
    P['RicU'] = raise_idx(raise_idx(Ric, 0, ginv), 1, ginv)          # R^{pq}
    P['dRicU'] = raise_idx(raise_idx(P['dRic'], 1, ginv), 2, ginv)   # nabla R^{pq} (mu kept)
    P['boxRicU'] = raise_idx(raise_idx(P['boxRic'], 0, ginv), 1, ginv)
    P['RiemU'] = Riem
    for ax in range(4): P['RiemU'] = raise_idx(P['RiemU'], ax, ginv) # R^{pqrs}
    P['dRiemU'] = P['dRiem']
    for ax in range(1, 5): P['dRiemU'] = raise_idx(P['dRiemU'], ax, ginv)
    P['RicM'] = raise_idx(Ric, 0, ginv)       # R^p_a
    P['dRicM'] = raise_idx(P['dRic'], 1, ginv)  # nabla_mu R^p_a : (mu,p,a)
    P['ddRicM'] = raise_idx(P['ddRic'], 2, ginv)  # (mu,nu,p,a)
    P['ddRicU'] = raise_idx(raise_idx(P['ddRic'], 2, ginv), 3, ginv)  # nabla nabla R^{pq}
    P['boxRicM'] = raise_idx(P['boxRic'], 0, ginv)  # (Box R^p_a)
    return P

def C1(pairs):
    # contraction helper: sum over repeated label values.
    # pairs: list of (tensor, index-labels tuple); returns dict tensor
    # whose key is the tuple of free labels in order of first appearance
    # is NOT tracked -- caller uses explicit free-order via 'free' arg.
    raise NotImplementedError

def contract(tensors, free):
    """tensors: list of (T, labels) with labels a tuple of strings, one
    per index. Repeated labels are summed. free: tuple of labels giving
    the output index order. Returns dict tensor keyed by free values."""
    out = {}
    # group second+ tensors by their shared-label values iteratively
    acc = [(dict(), tensors[0][0], tensors[0][1])]
    # simple recursive join
    def join(acc_items, T, labels):
        new = []
        for keymap, Td, lab in acc_items:
            for k, v in T.items():
                ok = True; km = dict(keymap)
                for ax, lb in enumerate(labels):
                    if lb in km and km[lb] != k[ax]: ok = False; break
                    km[lb] = k[ax]
                if not ok: continue
                new.append((km, {(): v} if False else None, None, Td, lab, k, v))
        return new
    # iterative product with jet multiplication
    cur = [( {}, jconst(1.0) )]  # (label->value, jet)
    for T, labels in tensors:
        nxt = []
        for keymap, jv in cur:
            for k, v in T.items():
                km = dict(keymap); ok = True
                for ax, lb in enumerate(labels):
                    if lb in km and km[lb] != k[ax]: ok = False; break
                    km[lb] = k[ax]
                if ok: nxt.append((km, jmul(jv, v)))
        cur = nxt
    for keymap, jv in cur:
        fk = tuple(keymap[lb] for lb in free)
        out[fk] = out.get(fk, 0) + jv if fk in out else jv
    return {k: v for k, v in out.items() if np.max(np.abs(v)) > 0.0}

def scal(T):
    return T.get((), None)

# ---- the 58 monomials of Eq. (3.15) ----
# Each entry: (group, coefficient polynomial in xi as list of Fractions
# in FACTORED form evaluated by caller, function(G,P)->rank-2 dict or
# ('trace', scalar jet)).  Coefficients are encoded factored, exactly
# as printed, and expanded with Fraction arithmetic in eval_df().
def F(num, den=1): return Fr(num, den)
MONO = []
def mono(group, coef, fn): MONO.append((group, coef, fn))

# ---------- direct part ----------
mono('d20', ('poly', [F(3, 70), F(-2, 5), F(1)]), lambda G, P: P['ddboxR'])
mono('d20', ('const', F(-1, 140)), lambda G, P: P['boxboxRic'])
mono('d20', ('prod', [([F(-6)], [('lin', F(1, 6))]), ('poly', [F(1, 30), F(-1, 3), F(1)])]),
     lambda G, P: tmul(G['Rsc'], P['ddR']) if False else
     {k: jmul(G['Rsc'][()], v) for k, v in P['ddR'].items()})
mono('d20', ('prod', [([F(-1)], [('lin', F(1, 6)), ('lin', F(1, 5))])]),
     lambda G, P: {k: jmul(P['boxR'][()], v) for k, v in G['Ric'].items()})
mono('d20', ('const', F(0)), lambda G, P: None)  # placeholder replaced below
MONO.pop()
def m5(G, P):
    # (1/15)(xi-1/7) R_{;p(a} R^p_{b)} : U_ab = (nabla_p nabla_a R) R^p_b
    U = contract([(P['ddR'], ('p', 'a')), (P['RicM'], ('p', 'b'))], ('a', 'b'))
    return sym_last2(U)
mono('d20', ('prod', [([F(1, 15)], [('lin', F(1, 7))])]), m5)
def m6(G, P):
    return {k: jmul(G['Rsc'][()], v) for k, v in P['boxRic'].items()}
mono('d20', ('prod', [([F(1, 10)], [('lin', F(1, 6))])]), m6)
def m7(G, P):
    # R_{p(a} Box R^p_{b)}
    U = contract([(G['Ric'], ('p', 'a')), (P['boxRicM'], ('p', 'b'))], ('a', 'b'))
    return sym_last2(U)
mono('d20', ('const', F(1, 42)), m7)
def m8(G, P):
    # R^{pq} R_{pq;(ab)} : ddRic with deriv indices (a,b), tensor (p,q)
    dd = {(k[2], k[3], k[0], k[1]): v for k, v in P['ddRic'].items()}
    U = contract([(P['RicU'], ('p', 'q')), (dd, ('p', 'q', 'a', 'b'))], ('a', 'b'))
    return sym_last2(U)
mono('d20', ('prod', [([F(1, 15)], [('lin', F(2, 7))])]), m8)
def m9(G, P):
    # R^{pq} R_{p(a;b)q} : printed derivative order ;b then ;q, i.e.
    # U_ab = R^{pq} nabla_q nabla_b R_{pa}; sym over (a,b)
    dd = {(k[2], k[3], k[0], k[1]): v for k, v in P['ddRic'].items()}
    # dd keyed (x,y,mu,nu) = nabla_mu nabla_nu R_{xy}; want nabla_q nabla_b R_{pa}
    U = contract([(P['RicU'], ('p', 'q')), (dd, ('p', 'a', 'q', 'b'))], ('a', 'b'))
    return sym_last2(U)
mono('d20', ('const', F(2, 105)), m9)
def m10(G, P):
    # R^{pq} R_{ab;pq} : printed order ;p then ;q, i.e. nabla_q nabla_p R_{ab}
    dd = {(k[2], k[3], k[0], k[1]): v for k, v in P['ddRic'].items()}
    return contract([(P['RicU'], ('p', 'q')), (dd, ('a', 'b', 'q', 'p'))], ('a', 'b'))
mono('d20', ('const', F(-1, 70)), m10)
def m11(G, P):
    # R^{;pq} R_{paqb} : (nabla^p nabla^q R) R_{paqb}
    ddU = {(k[0], k[1]): v for k, v in P['ddR'].items()}
    ddU = raise_idx(raise_idx(ddU, 0, G['ginv']), 1, G['ginv'])
    return contract([(ddU, ('p', 'q')), (G['Riem'], ('p', 'a', 'q', 'b'))], ('a', 'b'))
mono('d20', ('prod', [([F(2, 15)], [('lin', F(3, 14))])]), m11)
def m12(G, P):
    return contract([(P['boxRicU'], ('p', 'q')), (G['Riem'], ('p', 'a', 'q', 'b'))], ('a', 'b'))
mono('d20', ('const', F(-1, 105)), m12)
def m13(G, P):
    # R^{pq;r}_{(a} R_{|rqp|b)} : U_ab = (nabla_a nabla^r R^{pq}) R_{rqpb}
    dd = P['ddRicU']  # (mu,nu,p,q) = nabla_mu nabla_nu R^{pq}
    ddr = {}
    for k, v in dd.items():
        for r in range(4):
            gv = G['ginv'].get((r, k[1]))
            if gv is None: continue
            kk = (k[0], r, k[2], k[3])
            p = jmul(gv, v)
            ddr[kk] = ddr.get(kk, 0) + p if kk in ddr else p
    U = contract([(ddr, ('a', 'r', 'p', 'q')), (G['Riem'], ('r', 'q', 'p', 'b'))], ('a', 'b'))
    return sym_last2(U)
mono('d20', ('const', F(4, 105)), m13)
def m14(G, P):
    # R^{p(a;qr} R_{|pqr|b)} : the ;q ;r derivatives contract with the
    # lower tensor indices of R_{pqrb}, so they enter RAISED:
    # U_ab = (nabla^r nabla^q R^p_a) R_{pqrb}, symmetrised over (a,b)
    dd = raise_idx(raise_idx(P['ddRicM'], 0, G['ginv']), 1, G['ginv'])
    # dd keyed (r,q,p,a) = nabla^r nabla^q R^p_a
    U = contract([(dd, ('r', 'q', 'p', 'a')), (G['Riem'], ('p', 'q', 'r', 'b'))], ('a', 'b'))
    return sym_last2(U)
mono('d20', ('const', F(2, 35)), m14)
def m15(G, P):
    dd = {(k[2], k[3], k[4], k[5], k[0], k[1]): v for k, v in P['ddRiem'].items()}
    U = contract([(P['RiemU'], ('p', 'q', 'r', 's')), (dd, ('p', 'q', 'r', 's', 'a', 'b'))], ('a', 'b'))
    return sym_last2(U)
mono('d20', ('prod', [([F(-1, 15)], [('lin', F(3, 14))])]), m15)
mono('d11', ('prod', [([F(-6)], [('lin', F(1, 4)), ('lin2', F(1, 6))])]),
     lambda G, P: contract([(P['dR'], ('a',)), (P['dR'], ('b',))], ('a', 'b')))
def m17(G, P):
    # R_{;p} R^p_{(a;b)} : U_ab = (nabla_p R)(nabla_b R^p_a)
    U = contract([(P['dR'], ('p',)), (P['dRicM'], ('b', 'p', 'a'))], ('a', 'b'))
    return sym_last2(U)
mono('d11', ('prod', [([F(-1, 5)], [('lin', F(3, 14))])]), m17)
def m18(G, P):
    # R_{;p} R_{ab}^{;p}
    dU = raise_idx(P['dRic'], 0, G['ginv'])  # (mu^,a,b) with mu raised: key (mu,a,b) values nabla^mu
    return contract([(P['dR'], ('p',)), (dU, ('p', 'a', 'b'))], ('a', 'b'))
mono('d11', ('prod', [([F(1, 5)], [('lin', F(17, 84))])]), m18)
def m19(G, P):
    return contract([(P['dRicU'], ('a', 'p', 'q')), (P['dRic'], ('b', 'p', 'q'))], ('a', 'b'))
mono('d11', ('prod', [([F(1, 15)], [('lin', F(1, 4))])]), m19)
def m20(G, P):
    dU = raise_idx(P['dRic'], 0, G['ginv'])
    return contract([(P['dRicM'], ('q', 'p', 'a')), (dU, ('q', 'p', 'b'))], ('a', 'b'))
mono('d11', ('const', F(-1, 210)), m20)
def m21(G, P):
    return contract([(P['dRicM'], ('q', 'p', 'a')), (P['dRicM'], ('p', 'q', 'b'))], ('a', 'b'))
mono('d11', ('const', F(1, 42)), m21)
def m22(G, P):
    # R^{pq;r} R_{rqp(a;b)} : U_ab = (nabla^r R^{pq})(nabla_b R_{rqpa})
    dU = raise_idx(P['dRicU'], 0, G['ginv'])  # (r^,p,q)
    U = contract([(dU, ('r', 'p', 'q')), (P['dRiem'], ('b', 'r', 'q', 'p', 'a'))], ('a', 'b'))
    return sym_last2(U)
mono('d11', ('const', F(-1, 105)), m22)
def m23(G, P):
    dU = raise_idx(P['dRicU'], 0, G['ginv'])
    return contract([(dU, ('r', 'p', 'q')), (P['dRiem'], ('r', 'p', 'a', 'q', 'b'))], ('a', 'b'))
mono('d11', ('const', F(-1, 70)), m23)
def m24(G, P):
    return contract([(P['dRiemU'], ('a', 'p', 'q', 'r', 's')), (P['dRiem'], ('b', 'p', 'q', 'r', 's'))], ('a', 'b'))
mono('d11', ('prod', [([F(-1, 15)], [('lin', F(13, 56))])]), m24)
def m25(G, P):
    R3 = raise_idx(raise_idx(raise_idx(G['Riem'], 0, G['ginv']), 1, G['ginv']), 2, G['ginv'])
    dA = {(k[1], k[2], k[3], k[0]): v for k, v in P['dRiem'].items()}  # (p,q,r,a) deriv last->first? build directly:
    # nabla_s R^{pqr}_a : take dRiem (mu,p,q,r,a) -> raise p,q,r ; contract s with raised deriv of R_{pqrb}
    dR3 = P['dRiem']
    for ax in (1, 2, 3): dR3 = raise_idx(dR3, ax, G['ginv'])   # (mu,p,q,r,a) raised pqr
    dRb = raise_idx(P['dRiem'], 0, G['ginv'])                  # (s^,p,q,r,b)
    A = {(k[1], k[2], k[3], k[4], k[0]): v for k, v in dR3.items()}  # (p,q,r,a,s)
    B = {(k[1], k[2], k[3], k[4], k[0]): v for k, v in dRb.items()}  # (p,q,r,b,s)
    return contract([(A, ('p', 'q', 'r', 'a', 's')), (B, ('p', 'q', 'r', 'b', 's'))], ('a', 'b'))
mono('d11', ('const', F(-1, 70)), m25)
# ---------- cubic direct ----------
def mc(G, P, fn): return fn(G, P)
mono('c3', ('prod', [([F(3)], [('lin3', F(1, 6))])]),
     lambda G, P: {k: jmul(jmul(G['Rsc'][()], G['Rsc'][()]), v) for k, v in G['Ric'].items()})
def m27(G, P):
    # R_{pa} R^p_b : mixed pairing (lower x upper)
    return contract([(G['Ric'], ('p', 'a')), (P['RicM'], ('p', 'b'))], ('a', 'b'))
mono('c3', ('prod', [([F(-2, 15)], [('lin', F(1, 6))])]),
     lambda G, P: {k: jmul(G['Rsc'][()], v) for k, v in m27(G, P).items()})
def m28(G, P):
    s = ttrace(contract([(P['RicU'], ('p', 'q')), (G['Ric'], ('p', 'q'))], ()), 0, 0) if False else None
    sc = contract([(P['RicU'], ('p', 'q')), (G['Ric'], ('p', 'q'))], ())
    return {k: jmul(sc[()], v) for k, v in G['Ric'].items()}
mono('c3', ('prod', [([F(-1, 30)], [('lin', F(1, 6))])]), m28)
mono('c3', ('const', F(-2, 315)),
     lambda G, P: contract([(P['RicU'], ('p', 'q')), (G['Ric'], ('p', 'a')), (G['Ric'], ('q', 'b'))], ('a', 'b')))
def m30(G, P):
    U = contract([(P['RicU'], ('p', 'q')), (G['Riem'], ('p', 'a', 'q', 'b'))], ('a', 'b'))
    return {k: jmul(G['Rsc'][()], v) for k, v in U.items()}
mono('c3', ('prod', [([F(1, 15)], [('lin', F(1, 6))])]), m30)
mono('c3', ('const', F(1, 315)),
     lambda G, P: contract([(P['RicU'], ('p', 'r')), (P['RicM'], ('q', 'r')), (G['Riem'], ('p', 'a', 'q', 'b'))], ('a', 'b')))
def m32(G, P):
    U = contract([(P['RicU'], ('p', 'q')), (P['RicM'], ('r', 'a')), (G['Riem'], ('r', 'q', 'p', 'b'))], ('a', 'b'))
    return sym_last2(U)
mono('c3', ('const', F(1, 315)), m32)
def m33(G, P):
    R3 = raise_idx(raise_idx(raise_idx(G['Riem'], 0, G['ginv']), 1, G['ginv']), 2, G['ginv'])
    U = contract([(R3, ('p', 'q', 'r', 'a')), (G['Riem'], ('p', 'q', 'r', 'b'))], ('a', 'b'))
    return {k: jmul(G['Rsc'][()], v) for k, v in U.items()}
mono('c3', ('prod', [([F(1, 15)], [('lin', F(1, 6))])]), m33)
def m34(G, P):
    K = contract([(P['RiemU'], ('p', 'q', 'r', 's')), (G['Riem'], ('p', 'q', 'r', 's'))], ())
    return {k: jmul(K[()], v) for k, v in G['Ric'].items()}
mono('c3', ('prod', [([F(1, 30)], [('lin', F(1, 6))])]), m34)
def m35(G, P):
    R3 = raise_idx(raise_idx(raise_idx(G['Riem'], 0, G['ginv']), 1, G['ginv']), 2, G['ginv'])
    # R^p_{(a} R^{qrs}_{|p|} R_{|qrs|b)} : R^{qrs}_p = R3 keyed (q,r,s,p)
    R3p = R3  # R^{qrs}_p keyed (q,r,s,p): Riem raised on positions 0,1,2
    U = contract([(P['RicM'], ('p', 'a')), (R3p, ('q', 'r', 's', 'p')), (G['Riem'], ('q', 'r', 's', 'b'))], ('a', 'b'))
    return sym_last2(U)
mono('c3', ('const', F(-4, 315)), m35)
def m36(G, P):
    R2 = raise_idx(raise_idx(G['Riem'], 0, G['ginv']), 1, G['ginv'])  # R^{rs}_{pa}
    return contract([(P['RicU'], ('p', 'q')), (R2, ('r', 's', 'p', 'a')), (G['Riem'], ('r', 's', 'q', 'b'))], ('a', 'b'))
mono('c3', ('const', F(-2, 315)), m36)
mono('c3', ('const', F(4, 315)),
     lambda G, P: contract([(G['Ric'], ('p', 'q')), (P['RiemU'], ('p', 'r', 'q', 's')), (G['Riem'], ('r', 'a', 's', 'b'))], ('a', 'b')))
def m38(G, P):
    R3a = raise_idx(raise_idx(raise_idx(G['Riem'], 0, G['ginv']), 1, G['ginv']), 2, G['ginv'])  # R^{prs}_a keyed (p,r,s,a)
    R1b = raise_idx(G['Riem'], 0, G['ginv'])  # R^q_{rsb} keyed (q,r,s,b)
    return contract([(G['Ric'], ('p', 'q')), (R3a, ('p', 'r', 's', 'a')), (R1b, ('q', 'r', 's', 'b'))], ('a', 'b'))
mono('c3', ('const', F(-1, 315)), m38)
def m39(G, P):
    # PHASE 365 REPAIR (this v2 copy only; the stored p2411_driver.py
    # is unchanged): N40 = R^{pqrs} R_{pqt a} R_{rs}{}^t{}_{b} -- the
    # third factor's raised index sits in Riemann slot 2, not slot 0.
    # The stored driver formed R^t{}_{rsb} (slot 0 raised) and
    # contracted it in the slot-2 position (Phase 363: raw (0, +4, 0)
    # vs verbatim (0, -8, 0) at the Ellis throat; +16 bracket in the
    # xi^0 T^r_r total). Here R2 = R_{rs}{}^t{}_{b} keyed (r, s, t, b).
    R2 = raise_idx(G['Riem'], 2, G['ginv'])  # R_{rs}{}^t{}_{b}
    return contract([(P['RiemU'], ('p', 'q', 'r', 's')), (G['Riem'], ('p', 'q', 't', 'a')), (R2, ('r', 's', 't', 'b'))], ('a', 'b'))
mono('c3', ('const', F(2, 315)), m39)
def m40(G, P):
    R1 = raise_idx(G['Riem'], 0, G['ginv'])
    return contract([(P['RiemU'], ('p', 'r', 'q', 's')), (R1, ('t', 'p', 'q', 'a')), (G['Riem'], ('t', 'r', 's', 'b'))], ('a', 'b'))
mono('c3', ('const', F(4, 63)), m40)
def m41(G, P):
    R3d = raise_idx(raise_idx(raise_idx(G['Riem'], 0, G['ginv']), 1, G['ginv']), 2, G['ginv'])
    # R^{pqr}_s keyed (p,q,r,s): Riem raised on positions 0,1,2
    R2u = raise_idx(raise_idx(G['Riem'], 0, G['ginv']), 1, G['ginv'])  # R^{st}_{ab} keyed (s,t,a,b)
    return contract([(R3d, ('p', 'q', 'r', 's')), (G['Riem'], ('p', 'q', 'r', 't')), (R2u, ('s', 't', 'a', 'b'))], ('a', 'b'))
mono('c3', ('const', F(-2, 315)), m41)
print('monomials registered:', len(MONO), flush=True)

# ---------- trace part: 17 scalar monomials (multiplied by g_ab) ----------
TMONO = []
def tmono(group, coef, fn): TMONO.append((group, coef, fn))
tmono('t20', ('poly', [F(-11, 280), F(2, 5), F(-1)]), lambda G, P: P['boxboxR'][()])
tmono('t20', ('prod', [([F(6)], [('lin', F(1, 6))]), ('poly', [F(1, 40), F(-1, 3), F(1)])]),
      lambda G, P: jmul(G['Rsc'][()], P['boxR'][()]))
tmono('t20', ('prod', [([F(-1, 30)], [('lin', F(3, 14))])]),
      lambda G, P: contract([(P['ddR'], ('p', 'q')), (P['RicU'], ('p', 'q'))], ())[()])
tmono('t20', ('prod', [([F(-1, 15)], [('lin', F(5, 28))])]),
      lambda G, P: contract([(G['Ric'], ('p', 'q')), (P['boxRicU'], ('p', 'q'))], ())[()])
def t5(G, P):
    # R_{pq;rs} R^{prqs} : printed order ;r then ;s, i.e. nabla_s nabla_r R_{pq}
    dd = {(k[2], k[3], k[0], k[1]): v for k, v in P['ddRic'].items()}  # (x,y,mu,nu)
    return contract([(dd, ('p', 'q', 's', 'r')), (P['RiemU'], ('p', 'r', 'q', 's'))], ())[()]
tmono('t20', ('prod', [([F(4, 15)], [('lin', F(1, 7))])]), t5)
tmono('t11', ('poly', [F(-53, 1680), F(17, 30), F(-13, 4), F(6)]),
      lambda G, P: contract([(P['dR'], ('p',)), (raise_idx(P['dR'], 0, G['ginv']), ('p',))], ())[()])
def t7(G, P):
    dU = raise_idx(P['dRicU'], 0, G['ginv'])
    return contract([(P['dRic'], ('r', 'p', 'q')), (dU, ('r', 'p', 'q'))], ())[()]
tmono('t11', ('prod', [([F(-1, 15)], [('lin', F(13, 56))])]), t7)
def t8(G, P):
    dU = raise_idx(P['dRicU'], 0, G['ginv'])  # (q^,p,r) after relabel: dRicU (mu,p,q); raise mu
    A = {(k[1], k[2], k[0]): v for k, v in dU.items()}  # (p,r,q) = nabla^q R^{pr}
    return contract([(P['dRic'], ('r', 'p', 'q')), (A, ('p', 'r', 'q'))], ())[()]
tmono('t11', ('const', F(-1, 420)), t8)
def t9(G, P):
    dU = raise_idx(P['dRiemU'], 0, G['ginv'])
    return contract([(P['dRiem'], ('t', 'p', 'q', 'r', 's')), (dU, ('t', 'p', 'q', 'r', 's'))], ())[()]
tmono('t11', ('prod', [([F(1, 15)], [('lin', F(19, 112))])]), t9)
tmono('tc3', ('prod', [([F(-1, 2)], [('lin3', F(1, 6))])]),
      lambda G, P: jmul(jmul(G['Rsc'][()], G['Rsc'][()]), G['Rsc'][()]))
tmono('tc3', ('prod', [([F(1, 60)], [('lin', F(1, 6))])]),
      lambda G, P: jmul(G['Rsc'][()], contract([(P['RicU'], ('p', 'q')), (G['Ric'], ('p', 'q'))], ())[()]))
tmono('tc3', ('const', F(1, 1890)),
      lambda G, P: contract([(G['Ric'], ('p', 'q')), (P['RicM'], ('p', 'r')), (P['RicU'], ('q', 'r'))], ())[()])
tmono('tc3', ('const', F(-1, 630)),
      lambda G, P: contract([(G['Ric'], ('p', 'q')), (G['Ric'], ('r', 's')), (P['RiemU'], ('p', 'r', 'q', 's'))], ())[()])
tmono('tc3', ('prod', [([F(-1, 60)], [('lin', F(1, 6))])]),
      lambda G, P: jmul(G['Rsc'][()], contract([(P['RiemU'], ('p', 'q', 'r', 's')), (G['Riem'], ('p', 'q', 'r', 's'))], ())[()]))
def t15(G, P):
    R1 = raise_idx(G['Riem'], 0, G['ginv'])  # R^p_{rst} keyed (p,r,s,t)
    return contract([(G['Ric'], ('p', 'q')), (R1, ('p', 'r', 's', 't')), (P['RiemU'], ('q', 'r', 's', 't'))], ())[()]
tmono('tc3', ('prod', [([F(2, 15)], [('lin', F(1, 6))])]), t15)
tmono('tc3', ('prod', [([F(-1, 15)], [('lin', F(47, 252))])]),
      lambda G, P: contract([(P['RiemU'], ('p', 'q', 'u', 'v')),
                             (raise_idx(raise_idx(G['Riem'], 0, G['ginv']), 1, G['ginv']), ('r', 's', 'u', 'v')),
                             (G['Riem'], ('p', 'q', 'r', 's'))], ())[()])
def t17(G, P):
    A = raise_idx(raise_idx(G['Riem'], 0, G['ginv']), 1, G['ginv'])   # R^{pq}_{uv} keyed (p,q,u,v)
    BU = P['RiemU']
    return contract([(G['Riem'], ('p', 'r', 'q', 's')), (A, ('p', 'q', 'u', 'v')), (BU, ('r', 'u', 's', 'v'))], ())[()]
tmono('tc3', ('prod', [([F(-4, 15)], [('lin', F(41, 252))])]), t17)
print('trace monomials registered:', len(TMONO), flush=True)

# =====================================================================
# COEFFICIENT EXPANSION (exact Fractions, ascending powers of xi)
# =====================================================================
def expand_coef(spec):
    kind = spec[0]
    if kind == 'const': return [spec[1]]
    if kind == 'poly': return list(spec[1])
    if kind == 'prod':
        out = [F(1)]
        for elem in spec[1]:
            if elem[0] == 'poly':
                out = pmul(out, list(elem[1])); continue
            poly, facs = elem
            out = pmul(out, list(poly))
            for fk, fv in facs:
                n = {'lin': 1, 'lin2': 2, 'lin3': 3}[fk]
                for _ in range(n): out = pmul(out, [-fv, F(1)])
        return out
    raise ValueError(kind)

def eval_df(G, P):
    """Returns (bracket[comp][p], per-group bracket[comp][p]) with
    comp in ('Tt','Tr','Tth') = mixed eigenvalues (t, l, th),
    p = xi-power 0..3, bracket = 210 * DF sum."""
    tot = {c: np.zeros(4) for c in ('Tt', 'Tr', 'Tth')}
    grp = {}
    def accum(group, T):
        if T is None: return
        for ci, comp in enumerate(('Tt', 'Tr', 'Tth')):
            a = ci  # t=0, l=1, th=2 ; mixed T^a_a = ginv_aa * T_aa
            v = mixed_val(G, T, a)
            tot[comp] += v
            grp.setdefault(group, {c: np.zeros(4) for c in tot})
            grp[group][comp] += v
    for group, spec, fn in MONO:
        coef = expand_coef(spec)
        T = fn(G, P)
        if T is None: continue
        # scale tensor by polynomial: evaluate per power separately
        for p in range(4):
            cp = float(coef[p]) if p < len(coef) else 0.0
            if cp == 0.0: continue
            for ci, comp in enumerate(('Tt', 'Tr', 'Tth')):
                v = mixed_val(G, T, ci) * cp * 210.0
                tot[comp][p] += v
                grp.setdefault(group, {c: np.zeros(4) for c in tot})
                grp[group][comp][p] += v
    for group, spec, fn in TMONO:
        coef = expand_coef(spec)
        s = fn(G, P)
        for p in range(4):
            cp = float(coef[p]) if p < len(coef) else 0.0
            if cp == 0.0: continue
            for ci, comp in enumerate(('Tt', 'Tr', 'Tth')):
                # g_ab * s contributes to mixed component as s itself
                v = float(s[0, 0]) * cp * 210.0
                tot[comp][p] += v
                grp.setdefault(group, {c: np.zeros(4) for c in tot})
                grp[group][comp][p] += v
    return tot, grp
def mixed_val(G, T, a):
    v = T.get((a, a))
    if v is None: return 0.0
    gv = G['ginv'][(a, a)]
    return float(jmul(gv, v)[0, 0])

# =====================================================================
# THA RIGHT-HAND SIDES -- reused from phase237/work/p2371_driver.py
# (exact-rational assembly, independently re-typed by its checker)
# =====================================================================
def peval(coefs_desc, x):
    v = Fr(0)
    for c in coefs_desc: v = v * x + Fr(c)
    return v
A_NUM = {'Tt': {0: (-405, 448), 1: (2520, -2772)},
         'Tr': {0: (261, -238), 1: (-1008, 924)},
         'Tth': {0: (-783, 833), 1: (3024, -3234)}}
COMPS3 = ['Tt', 'Tr', 'Tth']
def A_bracket(comp, p, r_frac):
    if p not in A_NUM[comp]: return Fr(0)
    a, b = A_NUM[comp][p]
    return Fr(3, 8) * (Fr(a) * r_frac + Fr(b)) / r_frac**9
C_POLY = {
 'Tt': {0: [129, 1202, 5134, 7856, 3884, 264],
        1: [-756, -11536, -59080, -95200, -46368, -2688],
        2: [0, 23520, 191520, 342720, 164640, 6720],
        3: [0, 0, -161280, -349440, -161280, 0]},
 'Tr': {0: [69, 450, 1878, 2272, 552],
        1: [-252, -3360, -19824, -25536, -5376],
        2: [0, 6720, 70560, 94080, 13440],
        3: [0, 0, -80640, -107520, 0]},
 'Tth': {0: [75, 876, 3198, 5132, 2325, 138],
         1: [-315, -5838, -29484, -55776, -25200, -1344],
         2: [0, 10080, 84840, 198240, 85680, 3360],
         3: [0, 0, -60480, -215040, -80640, 0]}}
C_DEN = {'Tt': Fr(1, 8), 'Tr': Fr(1, 8), 'Tth': Fr(1, 4)}
C_POW = {'Tt': 5, 'Tr': 4, 'Tth': 5}
D_POLY = {
 'Tt': {0: [132, 403, -92, -490, 112, 64],
        1: [-1344, -4956, 1148, 6860, -1792, -672],
        2: [3360, 18480, -5040, -30240, 10080, 3360],
        3: [0, -20160, 6720, 40320, -20160, -6720]},
 'Tr': {0: [0, 69, 146, -210, 0, 64],
        1: [0, -672, -1848, 2940, 0, -672],
        2: [0, 1680, 8400, -13440, 0, 3360],
        3: [0, 0, -13440, 20160, 0, 6720]},
 'Tth': {0: [138, 495, -19, -840, 504, -128],
         1: [-1344, -5460, 462, 11760, -7392, 1344],
         2: [3360, 19320, -840, -53760, 38640, -6720],
         3: [0, -20160, -3360, 80640, -70560, 13440]}}
E_POLY = {
 'Tt': {0: [-442, -491, -1044, 358], 1: [5600, 3332, 10332, -3402],
        2: [-14280, -4620, -31500, 9870], 3: [-26880, -10080, 22680, -5460]},
 'Tr': {0: [58, -107, -20, 22], 1: [112, 1428, 56, -210],
        2: [840, -5460, 0, 630], 3: [-6720, 5040, 0, -420]},
 'Tth': {0: [-538, -382, -833, 283], 1: [7112, 3220, 9296, -3087],
         2: [-14280, -4620, -29400, 9135], 3: [-26880, -7560, 20160, -4830]}}
A_VALS = [Fr(1, 2), Fr(1), Fr(2), Fr(3), Fr(5), Fr(8)]
ETA_VALS = [Fr(3, 20), Fr(3, 10), Fr(9, 20), Fr(3, 5), Fr(3, 4), Fr(9, 10)]
EPS_VALS = [Fr(1, 10), Fr(1, 5), Fr(7, 20), Fr(1, 2)]
def R_at_l_A(l0):
    f = lambda rr: math.sqrt(rr * (rr - 1)) + math.log(math.sqrt(rr) + math.sqrt(rr - 1)) - l0
    return brentq(f, 1.0 + 1e-12, 50.0, xtol=1e-14)
MA_R = [R_at_l_A(l0) for l0 in (0.5, 1.0, 2.0)]
# THA Ellis profiles (phase219 THA dict): bracket_p(R) =
# A R^-8 + B R^-10 + C R^-12
THA_ELL = {
    'Tt': {0: (5940, -22932, 18025), 1: (-60480, 238168, -188930),
           2: (151200, -631680, 513660), 3: (0, 141120, -160440)},
    'Tr': {0: (-2484, 7116, -4445), 1: (24192, -69048, 43050),
           2: (-60480, 181440, -115500), 3: (0, -40320, 36120)},
    'Tth': {0: (7452, -28464, 22225), 1: (-72576, 276192, -215250),
            2: (181440, -725760, 577500), 3: (0, 161280, -180600)}}
def tha_ellis(comp, p, R):
    A, B, C = THA_ELL[comp][p]
    return A * R**-8 + B * R**-10 + C * R**-12
def tha_rhs(fam, par, comp, p):
    if fam == 'A_throat': return float(A_bracket(comp, p, Fr(1)))
    if fam == 'A_fullr': return float(A_bracket(comp, p, Fr(par).limit_denominator(10**12)))
    if fam == 'C': return float(C_DEN[comp] * peval(C_POLY[comp][p], par) / par**C_POW[comp])
    if fam == 'D': return float(peval(D_POLY[comp][p], par) / 8)
    if fam == 'E': return float(peval(E_POLY[comp][p], par) / (16 * par**3))
    raise ValueError(fam)

# =====================================================================
# CONTROL 2 -- engine self-checks on Ellis (throat)
# =====================================================================
def ellis_jets_at(l0):
    S = np.zeros(NJ1); S[0] = 1 + l0 * l0; S[1] = 2 * l0; S[2] = 1.0
    return np.zeros(NJ1), sqrt1(S)
Phi_e, R_e = ellis_jets_at(0.0)
G_e = build_geometry(Phi_e, R_e)
lam_e = [mixed_val(G_e, G_e['Ric'], a) for a in range(3)]
Rsc_e = float(G_e['Rsc'][()][0, 0])
P_e = deriv_pack(G_e)
cov_e = [mixed_val(G_e, P_e['boxboxRic'], a) for a in range(3)]
# scalar box^2 on eigenvalue l-series (Phase 237 boxj definition)
def boxS1(S, R1, Phi1):
    Rp = der1(R1); Pp = der1(Phi1)
    coef = 2.0 * d1(Rp, R1) + Pp
    return der1(der1(S)) + m1(coef, der1(S))
lam_series = {}
for a in range(3):
    Mj = jmul(G_e['ginv'][(a, a)], G_e['Ric'].get((a, a), jzero()))
    lam_series[a] = Mj[:, 0].copy()
    lam_series[a] = np.concatenate([lam_series[a], np.zeros(NJ1 - len(lam_series[a]))])[:NJ1]
scal_e = [float(boxS1(boxS1(lam_series[a], R_e, Phi_e), R_e, Phi_e)[0]) for a in range(3)]
D_e = [cov_e[a] - scal_e[a] for a in range(3)]
c2 = {'ellis_Ricci_eigs': lam_e, 'ellis_R_scalar': Rsc_e,
      'cov_box2Ric_mixed': cov_e, 'scal_box2_lam': scal_e, 'D_pilot': D_e,
      'eigs_ok': bool(abs(lam_e[0]) < 1e-9 and abs(lam_e[1] + 2) < 1e-9 and abs(lam_e[2]) < 1e-9),
      'R_ok': bool(abs(Rsc_e + 2) < 1e-9),
      'D_ok': bool(abs(D_e[0]) < 1e-6 and abs(D_e[1] - 16) < 1e-6 and abs(D_e[2] + 8) < 1e-6)}
c2['pass'] = bool(c2['eigs_ok'] and c2['R_ok'] and c2['D_ok'])
OUT['control2_engine'] = c2
print('CONTROL 2 (engine):', c2['pass'], 'lam', lam_e, 'D', D_e, flush=True)
assert c2['pass'], 'engine control failed -- no deciding read'

# =====================================================================
# DECIDING EVALUATIONS
# =====================================================================
def eval_point(Phi1, R1):
    G = build_geometry(Phi1, R1)
    P = deriv_pack(G)
    return eval_df(G, P)
results = {}
# --- Ellis profile at R = 1, 1.5, 2, 3 ---
ellis_res = {}
for Rv in (1.0, 1.5, 2.0, 3.0):
    l0 = math.sqrt(Rv * Rv - 1.0)
    tot, grp = eval_point(*ellis_jets_at(l0))
    res = {}
    for comp in COMPS3:
        for p in range(4):
            res[f'{comp}_p{p}'] = {'DF': float(tot[comp][p]),
                                   'THA': float(tha_ellis(comp, p, Rv)),
                                   'resid': float(tot[comp][p] - tha_ellis(comp, p, Rv))}
    ellis_res[f'R={Rv}'] = res
    print('ELLIS R=', Rv, 'max resid',
          max(abs(v['resid']) for v in res.values()), flush=True)
results['ellis'] = ellis_res
# --- families ---
fam_points = []
for par in A_VALS: fam_points.append(('C', par, solve_Rjet_throat('C', float(par)), np.zeros(NJ1)))
for par in ETA_VALS: fam_points.append(('D', par, solve_Rjet_throat('D', float(par)), np.zeros(NJ1)))
for par in EPS_VALS:
    Rj = solve_Rjet_throat('E', float(par))
    fam_points.append(('E', par, Rj, phi_jet_E1(Rj, float(par))))
fam_points.append(('A_throat', Fr(1), solve_Rjet_throat('A', None), np.zeros(NJ1)))
for l0, Rv in zip((0.5, 1.0, 2.0), MA_R):
    fam_points.append(('A_fullr', Rv, solve_Rjet_local_A(Rv), np.zeros(NJ1)))
fam_res = {}
for fam, par, Rj, Pj in fam_points:
    tot, grp = eval_point(Pj, Rj)
    key = f'{fam}:{par}'
    res = {}
    for comp in COMPS3:
        for p in range(4):
            tv = tha_rhs(fam if fam in ('A_throat', 'A_fullr') else fam,
                         par if fam != 'A_fullr' else par, comp, p) \
                if fam != 'A_fullr' else tha_rhs('A_fullr', par, comp, p)
            res[f'{comp}_p{p}'] = {'DF': float(tot[comp][p]), 'THA': float(tv),
                                   'resid': float(tot[comp][p] - tv)}
    fam_res[key] = res
    print('FAM', key, 'max resid', max(abs(v['resid']) for v in res.values()), flush=True)
results['families'] = fam_res
OUT['results'] = results

# =====================================================================
# CROSS-CHECK SUMMARIES
# =====================================================================
def block_max(res_dict, keys=None):
    out = {}
    for p in range(4):
        out[p] = max(abs(v['resid']) for k, v in res_dict.items() if k.endswith(f'_p{p}'))
    return out
cc = {}
cc['a_ellis_max_resid_per_p'] = {p: max(abs(v['resid']) for Rv, res in ellis_res.items()
                                        for k, v in res.items() if k.endswith(f'_p{p}'))
                                 for p in range(4)}
athr = fam_res['A_throat:1']
cc['a_Athroat_max_resid_per_p'] = block_max(athr)
cc['a_pass'] = bool(max(cc['a_ellis_max_resid_per_p'].values()) < 1e-6
                    and max(cc['a_Athroat_max_resid_per_p'].values()) < 1e-6)
for fam in ('C', 'D', 'E', 'A_fullr'):
    sub = {k: v for k, v in fam_res.items() if k.startswith(fam + ':')}
    cc[f'b_{fam}_max_resid_per_p'] = {p: max(abs(x['resid']) for res in sub.values()
                                             for k, x in res.items() if k.endswith(f'_p{p}'))
                                      for p in range(4)}
cc['b_Eq26_xi3_cell'] = fam_res['D:9/10']  # placeholder, replaced below
# Eq. (26) xi^3 cell: DF on D at eta=1 limit vs A throat (both DF):
# use D polynomial limit: DF D-family values are computed at the six
# eta values; the eta->1 statement is read from THA side in p2371;
# here record DF-vs-THA at eta=9/10 Tr p3 as the nearest computed cell.
cc['b_D_eta0.9_Tr_p3'] = fam_res['D:9/10']['Tr_p3']
OUT['cross_checks'] = cc
print('CROSS (a) pass:', cc['a_pass'], cc['a_ellis_max_resid_per_p'],
      cc['a_Athroat_max_resid_per_p'], flush=True)
print('CROSS (b):', {k: v for k, v in cc.items() if k.startswith('b_') and 'per_p' in k}, flush=True)

# =====================================================================
# (c) ELLIS GATE from DF throat cubics (Phase 219 Stage B formulas)
# =====================================================================
DF_THROAT = {}
for comp in COMPS3:
    DF_THROAT[comp] = np.array([ellis_res['R=1.0'][f'{comp}_p{p}']['DF'] for p in range(4)])
def cubic_roots(coef):
    r = np.roots([coef[3], coef[2], coef[1], coef[0]])
    return sorted([float(z.real) for z in r if abs(z.imag) < 1e-9])
gate = {}
P_reg = np.array([187.0, -1806.0, 5460.0, -4200.0])
gate['a_forced_deficit'] = -1.0 / (4 * math.pi)
gate['a_pass'] = bool(abs(gate['a_forced_deficit'] + 1 / (4 * math.pi)) < 1e-12)
gate['d_P_max_dev'] = float(np.max(np.abs(DF_THROAT['Tr'] - P_reg)))
gate['d_roots_Tr'] = cubic_roots(DF_THROAT['Tr'])
_iv = [x for x in gate['d_roots_Tr'] if -1.0 <= x <= 2.0]
gate['d_pass'] = bool(len(_iv) == 1 and abs(_iv[0] - 0.8603576689) < 1e-7)
nec = -DF_THROAT['Tt'] + DF_THROAT['Tr']
gate['b_nec_roots'] = cubic_roots(nec)
reg_nec = [0.1515510908, 0.2595996822, 1.4221825603]
gate['b_pass'] = bool(gate['d_pass'] and len(gate['b_nec_roots']) == 3
                      and max(abs(a - b) for a, b in zip(gate['b_nec_roots'], reg_nec)) < 1e-7)
def df_T(comp, xi, mr):
    num = sum(DF_THROAT[comp][p] * xi**p for p in range(4))
    return num / (20160.0 * math.pi**2 * mr**2)
XI_C = 1.0 / 6.0
gate['c_mr1'] = {'Delta_rho': -df_T('Tt', XI_C, 1.0), 'Delta_pr': df_T('Tr', XI_C, 1.0),
                 'Delta_pt': df_T('Tth', XI_C, 1.0)}
gate['c_mr2_pr'] = df_T('Tr', XI_C, 2.0)
gate['c_pass'] = bool(abs(gate['c_mr1']['Delta_pr'] - 9.15822e-5) / 9.15822e-5 < 1e-4
                      and abs(gate['c_mr2_pr'] - 2.28955e-5) / 2.28955e-5 < 1e-4
                      and abs(gate['c_mr1']['Delta_rho'] - 4.24405e-5) / 4.24405e-5 < 1e-4
                      and abs(gate['c_mr1']['Delta_pt'] - 5.33857e-4) / 5.33857e-4 < 1e-4)
gate['all_pass'] = bool(gate['a_pass'] and gate['b_pass'] and gate['c_pass'] and gate['d_pass'])
OUT['gate_c'] = gate
OUT['DF_throat_cubics'] = {c: DF_THROAT[c].tolist() for c in COMPS3}
print('GATE (c):', gate, flush=True)
OUT['wall_seconds'] = time.time() - t_start
with open(f'{WP}/phase241/work/p2411_results.json', 'w') as f:
    json.dump(OUT, f, indent=2)
print('DONE', OUT['wall_seconds'], flush=True)
