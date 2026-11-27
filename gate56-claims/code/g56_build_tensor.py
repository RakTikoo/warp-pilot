#!/usr/bin/env python3
"""
g56_build_tensor.py -- Gate-56 tensor derivation.

Derives ALL first and second spatial derivatives of the
claim family's metric SYMBOLICALLY from the metric itself
(sympy, Cartesian coordinates) and writes g56_tensor.py:
readable generated source (CSE temporaries + assignments)
with numpy and mpmath evaluators.

Metric (the object definition, ledger lineage SS1):
    g_tt = -N(r)^2
    g_tx = g_xt = -beta * S(r)          (beta = 1.1)
    g_ij = delta_ij + (M(r) - 1) n_i n_j,   n = x / r,
    r = sqrt(x^2 + y^2 + z^2), stationary.

The lineage's deciding machinery (p316_lib.T_from_SNM)
carries these derivatives as HAND-derived formulas (its
dv / ddv / dd-gamma expressions). The gate instead lets
sympy differentiate the metric; the Christoffel -> Ricci
-> Einstein contraction is then assembled by the gate's
own code in g56_lib.py from these derivative tensors.

Substitution: after differentiation, N(r) -> N0,
dN/dr -> N1, d^2N/dr^2 -> N2 (likewise M, S). The builder
asserts no Derivative / applied-function term survives.
"""
import sympy as sp
from sympy.printing.pycode import PythonCodePrinter

x, y, z, beta = sp.symbols('x y z beta', real=True)
N0, N1, N2, M0, M1, M2, S0, S1, S2 = sp.symbols(
    'N0 N1 N2 M0 M1 M2 S0 S1 S2', real=True)
r = sp.sqrt(x ** 2 + y ** 2 + z ** 2)
Nf = sp.Function('N')(r)
Mf = sp.Function('M')(r)
Sf = sp.Function('S')(r)
X = [x, y, z]

# ------------------------------------------------ metric
g = sp.zeros(4, 4)
g[0, 0] = -Nf ** 2
g[0, 1] = g[1, 0] = -beta * Sf
for i in range(3):
    for j in range(3):
        g[i + 1, j + 1] = (1 if i == j else 0) \
            + (Mf - 1) * X[i] * X[j] / r ** 2

_PROF_SYMS = {'N': (N0, N1, N2), 'M': (M0, M1, M2),
              'S': (S0, S1, S2)}


def _prof_key(e):
    """('N'|'M'|'S', order) if e is a (possibly Subs-wrapped)
    derivative of a profile function, else None. Sympy's
    chain rule wraps profile derivatives as
    Subs(Derivative(N(_xi), _xi), _xi, r)."""
    d = e
    if isinstance(d, sp.Subs):
        d = d.expr
    if isinstance(d, sp.Derivative):
        f = d.expr
        if isinstance(f, sp.core.function.AppliedUndef):
            return f.func.__name__, sum(
                c for _, c in d.variable_count)
    return None


def clean(expr):
    expr = expr.replace(
        lambda e: _prof_key(e) is not None,
        lambda e: _PROF_SYMS[_prof_key(e)[0]][_prof_key(e)[1]])
    # the bottom-up pass can leave Subs(<profile symbol>, _xi,
    # r) wrappers; a Subs whose expr does not involve its
    # dummy variables is a no-op -- collapse it.
    expr = expr.replace(
        lambda e: isinstance(e, sp.Subs)
        and not (e.expr.atoms() & set(e.variables)),
        lambda e: e.expr)
    expr = expr.subs({Nf: N0, Mf: M0, Sf: S0})
    expr = sp.expand(expr)
    assert not expr.atoms(sp.Derivative), expr
    assert not expr.atoms(sp.Subs), expr
    assert not expr.atoms(sp.Function), expr
    return expr


# --------------------------------------- first derivatives
dg = [[[clean(sp.diff(g[mu, nu], X[a])) if g[mu, nu] != 0
        else sp.Integer(0)
       for nu in range(4)] for mu in range(4)] for a in range(3)]

# -------------------------------------- second derivatives
ddg = [[[[clean(sp.diff(g[mu, nu], X[a], X[b]))
          if g[mu, nu] != 0 else sp.Integer(0)
          for nu in range(4)] for mu in range(4)]
        for b in range(3)] for a in range(3)]

args = (x, y, z, N0, N1, N2, M0, M1, M2, S0, S1, S2, beta)
dg_flat = [dg[a][mu][nu] for a in range(3) for mu in range(4)
           for nu in range(4)]
ddg_flat = [ddg[a][b][mu][nu] for a in range(3) for b in range(3)
            for mu in range(4) for nu in range(4)]


class MPPrinter(PythonCodePrinter):
    """pycode with mpmath-exact numeric literals."""

    def _print_Rational(self, expr):
        return '(mpf(%d)/mpf(%d))' % (expr.p, expr.q)

    def _print_Integer(self, expr):
        return 'mpf(%d)' % int(expr)

    def _print_Float(self, expr):
        return "mpf('%s')" % expr

    def _print_Pow(self, expr):
        base, exp = expr.as_base_exp()
        if exp == sp.Rational(1, 2):
            return 'sqrt(%s)' % self._print(base)
        if exp == sp.Rational(-1, 2):
            return '(mpf(1)/sqrt(%s))' % self._print(base)
        return super()._print_Pow(expr)


def _flat(printer, e):
    """pycode of e with all whitespace collapsed (the printer
    wraps long expressions across lines, which is invalid
    inside an assignment)."""
    s = printer.doprint(e)
    if isinstance(s, tuple):
        s = s[0]
    s = s.replace('math.sqrt(', 'sqrt(')
    assert 'math.' not in s, s
    return ' '.join(s.split())


def emit(flat, shape, printer, fname):
    repl, exprs = sp.cse(flat)
    lines = ['def %s(x, y, z, N0, N1, N2, M0, M1, M2, S0, S1, S2,'
             ' beta):' % fname]
    for sym, e in repl:
        lines.append('    %s = %s' % (sym.name,
                                      _flat(printer, e)))
    body = ', '.join(_flat(printer, e) for e in exprs)
    lines.append('    return [%s]' % body)
    return '\n'.join(lines), len(repl)


np_printer = PythonCodePrinter()
mp_printer = MPPrinter()

dg_np_src, n1 = emit(dg_flat, (3, 4, 4), np_printer, '_dg_list_np')
ddg_np_src, n2 = emit(ddg_flat, (3, 3, 4, 4), np_printer,
                      '_ddg_list_np')
dg_mp_src, n3 = emit(dg_flat, (3, 4, 4), mp_printer, '_dg_list_mp')
ddg_mp_src, n4 = emit(ddg_flat, (3, 3, 4, 4), mp_printer,
                      '_ddg_list_mp')
print('cse temporaries:', n1, n2, n3, n4)

header = '''#!/usr/bin/env python3
"""
g56_tensor.py -- GENERATED by g56_build_tensor.py (sympy
derivation of the Gate-56 metric's first/second spatial
derivatives; see that file). Evaluators return flat lists;
the wrappers reshape to dg (3,4,4) / ddg (3,3,4,4)
[spatial derivative index, mu, nu]. t-derivatives vanish
(stationarity) and are inserted by the caller.
"""
import numpy as _np
from numpy import sqrt
try:
    from mpmath import mp, mpf
except ImportError:  # float path does not need mpmath
    mp = mpf = None


'''
# mpmath functions need sqrt -> mpmath's; emit them in a
# namespace block where sqrt is rebound. The block is
# built only when mpmath is importable (the float64
# evaluators never touch it).
mp_block = ('if mpf is not None:\n'
            '    def _mp_block():\n'
            '        from mpmath import sqrt\n'
            + '\n'.join('        ' + ln if ln.strip() else ln
                        for ln in (dg_mp_src + '\n\n'
                                   + ddg_mp_src).split('\n'))
            + '\n        return _dg_list_mp, _ddg_list_mp\n'
            '    _dg_list_mp, _ddg_list_mp = _mp_block()\n'
            'else:\n'
            '    def _dg_list_mp(*a):\n'
            '        raise ImportError("mpmath unavailable")\n'
            '    def _ddg_list_mp(*a):\n'
            '        raise ImportError("mpmath unavailable")\n')

wrappers = '''

def _stack(out, shp, lead):
    arrs = []
    for o in out:
        a = _np.asarray(o, dtype=_np.float64)
        if a.shape != shp:
            a = _np.broadcast_to(a, shp)
        arrs.append(a)
    A = _np.stack(arrs).reshape(lead + shp)
    if not shp:
        return A
    return A.transpose(
        tuple(range(len(lead), len(lead) + len(shp)))
        + tuple(range(len(lead))))


def dg_np(x, y, z, N0, N1, N2, M0, M1, M2, S0, S1, S2, beta):
    out = _dg_list_np(x, y, z, N0, N1, N2, M0, M1, M2, S0, S1,
                      S2, beta)
    return _stack(out, _np.shape(x), (3, 4, 4))


def ddg_np(x, y, z, N0, N1, N2, M0, M1, M2, S0, S1, S2, beta):
    out = _ddg_list_np(x, y, z, N0, N1, N2, M0, M1, M2, S0, S1,
                       S2, beta)
    return _stack(out, _np.shape(x), (3, 3, 4, 4))


def dg_mp(x, y, z, N0, N1, N2, M0, M1, M2, S0, S1, S2, beta):
    out = _dg_list_mp(x, y, z, N0, N1, N2, M0, M1, M2, S0, S1,
                      S2, beta)
    return _np.array(out, dtype=object).reshape(3, 4, 4)


def ddg_mp(x, y, z, N0, N1, N2, M0, M1, M2, S0, S1, S2, beta):
    out = _ddg_list_mp(x, y, z, N0, N1, N2, M0, M1, M2, S0, S1,
                       S2, beta)
    return _np.array(out, dtype=object).reshape(3, 3, 4, 4)
'''

src = header + dg_np_src + '\n\n' + ddg_np_src + '\n\n' \
    + mp_block + wrappers
out = '/home/hatch/workspace/warp-pilot/gate56/work/g56_tensor.py'
with open(out, 'w') as fh:
    fh.write(src)
print('wrote', out, len(src), 'bytes')
