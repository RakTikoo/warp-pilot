"""W-B2: exact monomial algebra for the source kernels and their r-derivatives.

Kernels are polynomials in w = r - D*mu, q = s^2 = r^2 - 2rDmu + D^2 (with
half-integer powers), and r, with coefficients sympy expressions in (D, mu).
The r-derivative acts as: d(w)=1, d(q)=2w, d(r)=1, d(D)=d(mu)=0.
Monomial (a,b,c) = w^a q^b r^c:
  d/dr -> a w^(a-1) q^b r^c + 2b w^(a+1) q^(b-1) r^c + c w^a q^b r^(c-1).
Coefficients are lambdified to mpmath functions at the end.
"""
from fractions import Fraction
import sympy as sp
from mpmath import mpf

Dsym, musym = sp.symbols("D mu")

def dmonomials(terms):
    out = {}
    for (a, b, c), coeff in terms.items():
        if a > 0:
            key = (a - 1, b, c)
            out[key] = out.get(key, 0) + a * coeff
        if b != 0:
            key = (a + 1, b - 1, c)
            out[key] = out.get(key, 0) + 2 * b * coeff
        if c > 0:
            key = (a, b, c - 1)
            out[key] = out.get(key, 0) + c * coeff
    return out

def deriv_list(terms, nmax):
    out = [terms]
    for _ in range(nmax):
        out.append(dmonomials(out[-1]))
    return [{k: sp.lambdify((Dsym, musym), v, "mpmath") for k, v in t.items()} for t in out]

KV = deriv_list({(2, Fraction(-3, 2), 0): sp.Integer(1)}, 2)                    # w^2 q^-3/2
KW = deriv_list({(1, Fraction(-3, 2), 1): Dsym}, 3)                             # D r w q^-3/2
KA = deriv_list({(0, Fraction(-3, 2), 0): Dsym**2 * (1 - musym**2)}, 4)         # D^2(1-mu^2) q^-3/2

def eval_terms(terms, r, mu, D):
    w = r - D * mu
    q = w * w + D * D * (1 - mu * mu)  # = r^2 - 2rDmu + D^2, stable form
    tot = mpf(0)
    for (a, b, c), coeff in terms.items():
        tot += coeff(D, mu) * (w**a) * (q**mpf(float(b))) * (r**c)  # b half-integer: exact
    return tot
