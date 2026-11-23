"""
W-A GATE-9 fresh Bach engine (wa_engine.py)

Fresh symbolic derivation of the Bach tensor for the static spherical
ansatz
    ds^2 = -exp(2 Phi(r)) dt^2 + (1 - b(r)/r)^{-1} dr^2 + r^2 dOmega^2
from the metric, from first principles (Christoffel -> Riemann -> Ricci
-> Weyl -> double covariant divergence), following the standard
definition
    B_{mn} = nabla^a nabla^b C_{m a n b} + (1/2) R^{ab} C_{m a n b}
(conventions -+++).  Written from scratch for Gate 9; no phase script
is imported or copied.

CONVENTION IDENTIFICATION (anchor-verified, Gate 9): the registered
Bach tensor of the programme (Mannheim's B, i.e. Varieschi-Ault's W,
W_{mn} = 2 C^a_{m n}{}^{b}{}_{;b;a} + C^a_{m n}{}^{b} R_{ba}) is TWICE
the bracket above.  The raw bracket was computed first; against the
Phase-32 T-b closed forms it gave ratio exactly 0.5 at every point
and component, so the components returned here are multiplied by 2
to land on the registered convention.  Bach-flatness anchors are
insensitive to this overall factor; the T-b anchor fixes it.

Sparse targeted computation: only the Weyl components and their first
covariant derivatives are stored (dicts keyed by index tuples, zeros
dropped); the second covariant derivative is formed only for the
index patterns the contraction B^t_t, B^r_r, B^th_th actually needs.

Usage: build_bach(b_expr, phi_expr) -> dict with mixed components
'Bt','Br','Bth' as sympy expressions in r (theta cancels), plus
'trace' (sum of mixed diagonal, B^ph_ph = B^th_th by symmetry).
b_expr / phi_expr are sympy expressions in r (may contain parameters).
"""
import sympy as sp

t, r, th, ph = sp.symbols('t r theta phi')
COORDS = [t, r, th, ph]


def _add(d, key, val):
    if val == 0:
        return
    if key in d:
        v = d[key] + val
        if v == 0:
            del d[key]
        else:
            d[key] = v
    else:
        d[key] = val


def build_bach(b_expr, phi_expr, want=('Bt', 'Br', 'Bth'), debug=False,
               final_simplify=True):
    # ---- metric (diagonal) -------------------------------------------
    F = 1 - b_expr / r
    g = [None] * 4
    g[0] = -sp.exp(2 * phi_expr)
    g[1] = 1 / F
    g[2] = r**2
    g[3] = r**2 * sp.sin(th)**2
    gi = [1 / x for x in g]

    # partial derivatives of the diagonal metric: dg[i][d]
    dg = [[sp.diff(g[i], COORDS[d]) for d in range(4)] for i in range(4)]

    # ---- Christoffel Gamma^a_{bc} (sparse) ---------------------------
    # diagonal metric: Gamma^a_{bc} = (1/2) g^{aa} (d_b g_{ac} + d_c g_{ab}
    #                                               - d_a g_{bc})
    Gam = {}
    for a in range(4):
        for b in range(4):
            for c in range(4):
                val = 0
                if a == c:
                    val += dg[a][b]
                if a == b:
                    val += dg[a][c]
                if b == c:
                    val -= dg[b][a]
                if val != 0:
                    Gam[(a, b, c)] = sp.Rational(1, 2) * gi[a] * val

    def d_of(expr, d):
        return sp.diff(expr, COORDS[d])

    # ---- Riemann R^a_{bcd} (sparse) ----------------------------------
    # R^a_{bcd} = d_c Gam^a_{bd} - d_d Gam^a_{bc}
    #             + Gam^a_{ce} Gam^e_{bd} - Gam^a_{de} Gam^e_{bc}
    Riem = {}
    todo = [(a, b, c, d) for a in range(4) for b in range(4)
            for c in range(4) for d in range(4)]
    for (a, b, c, d) in todo:
        val = 0
        if (a, b, d) in Gam:
            val += d_of(Gam[(a, b, d)], c)
        if (a, b, c) in Gam:
            val -= d_of(Gam[(a, b, c)], d)
        for e in range(4):
            if (a, c, e) in Gam and (e, b, d) in Gam:
                val += Gam[(a, c, e)] * Gam[(e, b, d)]
            if (a, d, e) in Gam and (e, b, c) in Gam:
                val -= Gam[(a, d, e)] * Gam[(e, b, c)]
        if val != 0:
            Riem[(a, b, c, d)] = val

    # ---- Ricci R_{bd} = R^a_{b a d}, scalar --------------------------
    Ric = {}
    for (a, b, c, d), v in Riem.items():
        if c == a:
            _add(Ric, (b, d), v)
    Rscalar = sum(gi[i] * Ric.get((i, i), 0) for i in range(4))

    # ---- Weyl C_{abcd} (lower) ---------------------------------------
    # C_{abcd} = R_{abcd}
    #   - (1/2)(g_{ac} R_{bd} - g_{ad} R_{bc} - g_{bc} R_{ad} + g_{bd} R_{ac})
    #   + (R/6)(g_{ac} g_{bd} - g_{ad} g_{bc})
    Rlow = {}
    for (a, b, c, d), v in Riem.items():
        Rlow[(a, b, c, d)] = g[a] * v

    def gd(i, j):
        return g[i] if i == j else 0

    Weyl = {}
    idx = [(a, b, c, d) for a in range(4) for b in range(4)
           for c in range(4) for d in range(4)]
    for (a, b, c, d) in idx:
        val = Rlow.get((a, b, c, d), 0)
        val -= sp.Rational(1, 2) * (
            gd(a, c) * Ric.get((b, d), 0) - gd(a, d) * Ric.get((b, c), 0)
            - gd(b, c) * Ric.get((a, d), 0) + gd(b, d) * Ric.get((a, c), 0))
        val += (Rscalar / 6) * (gd(a, c) * gd(b, d) - gd(a, d) * gd(b, c))
        if val != 0:
            Weyl[(a, b, c, d)] = val

    # ---- first covariant derivative F_{e abcd} = nabla_e C_{abcd} ----
    # NOTE: nabla_e C_{abcd} is generally NONZERO even where C_{abcd} = 0
    # (connection terms mix in other components), so F is formed for
    # every index pattern, not only the nonzero Weyl patterns.
    GamEI = {}
    for (m, e, i), gv in Gam.items():
        GamEI.setdefault((e, i), []).append((m, gv))
    Fcov = {}
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    v = Weyl.get((a, b, c, d), 0)
                    for e in range(4):
                        val = d_of(v, e) if v != 0 else 0
                        for slot, idxv in enumerate((a, b, c, d)):
                            for (m, gam) in GamEI.get((e, idxv), ()):
                                key = [a, b, c, d]
                                key[slot] = m
                                cv = Weyl.get(tuple(key), 0)
                                if cv != 0:
                                    val -= gam * cv
                        if val != 0:
                            Fcov[(e, a, b, c, d)] = val

    # ---- Bach: B_{mn} = nabla^a nabla^b C_{m a n b}
    #                     + (1/2) R^{ab} C_{m a n b} --------------------
    # second derivative G_{f e abcd} = nabla_f (nabla_e C_{abcd}),
    # formed only for patterns (f,e,m,a,n,b) with the contraction
    # a = second slot, b = fourth slot.
    def second_cov(f, e, a, b, c, d):
        val = 0
        base = Fcov.get((e, a, b, c, d), 0)
        if base != 0:
            val += d_of(base, f)
        slots = (e, a, b, c, d)
        for slot, idxv in enumerate(slots):
            for m in range(4):
                gam = Gam.get((m, f, idxv), 0)
                if gam == 0:
                    continue
                key = [e, a, b, c, d]
                key[slot] = m
                fv = Fcov.get(tuple(key), 0)
                if fv != 0:
                    val -= gam * fv
        return val

    if debug:
        return {'Gam': Gam, 'Riem': Riem, 'Ric': Ric, 'Rscalar': Rscalar,
                'Weyl': Weyl, 'Fcov': Fcov, 'g': g, 'gi': gi}
    comp_index = {'Bt': 0, 'Br': 1, 'Bth': 2}
    out = {}
    for name in want:
        m = comp_index[name]
        n = m
        val = 0
        for a in range(4):
            for b in range(4):
                g2 = second_cov(a, b, m, a, n, b)
                if g2 != 0:
                    val += gi[a] * gi[b] * g2
                cv = Weyl.get((m, a, n, b), 0)
                if cv != 0:
                    # R^{ab}: Ricci is diagonal for this ansatz
                    if a == b:
                        val += sp.Rational(1, 2) * gi[a] * gi[b] * \
                            Ric.get((a, b), 0) * cv
        if final_simplify:
            out[name] = sp.simplify(sp.together(2 * val * gi[m]))
        else:
            out[name] = 2 * val * gi[m]
    out['trace_raw'] = None  # filled by caller if all components wanted
    return out


def simplify_expr(e):
    return sp.simplify(sp.together(e))
