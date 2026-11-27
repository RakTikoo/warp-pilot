#!/usr/bin/env python3
"""
g56_splines.py -- Gate-56's OWN not-a-knot cubic spline,
written for this gate (second-derivative formulation,
dense linear solve). NOT scipy's CubicSpline and not any
lineage code: the spline layer of every profile in the
claim set is evaluated through this module in the gate's
deciding reads.

Construction: unknowns are the second derivatives M_i at
the knots. Interior rows are the C1-continuity conditions;
the two end rows are the not-a-knot conditions (third
derivative continuous at the second and at the
penultimate knot). Evaluation uses the standard
second-derivative piece formulas. Semantics mirror the
registered _eval_corr: outside [x_0, x_{n-1}] the value
holds the end value and both derivatives are zero.

Two arithmetics: float64 (numpy) and 50-digit mpmath
(the spot-check path). Same construction in both.
"""
import numpy as np

DTYPE = np.float64


class NotAKnotSpline:
    """float64 not-a-knot cubic spline through (x, y)."""

    def __init__(self, x, y):
        x = np.asarray(x, dtype=DTYPE)
        y = np.asarray(y, dtype=DTYPE)
        n = len(x)
        assert n >= 4 and len(y) == n
        self.x, self.y, self.n = x, y, n
        h = np.diff(x)
        self.h = h
        A = np.zeros((n, n), dtype=DTYPE)
        rhs = np.zeros(n, dtype=DTYPE)
        # not-a-knot, left: h1*M0 - (h0+h1)*M1 + h0*M2 = 0
        A[0, 0] = h[1]
        A[0, 1] = -(h[0] + h[1])
        A[0, 2] = h[0]
        # interior C1 rows
        for i in range(1, n - 1):
            A[i, i - 1] = h[i - 1]
            A[i, i] = 2.0 * (h[i - 1] + h[i])
            A[i, i + 1] = h[i]
            rhs[i] = 6.0 * ((y[i + 1] - y[i]) / h[i]
                            - (y[i] - y[i - 1]) / h[i - 1])
        # not-a-knot, right:
        # h_{n-2}*M_{n-3} - (h_{n-3}+h_{n-2})*M_{n-2}
        #     + h_{n-3}*M_{n-1} = 0
        A[n - 1, n - 3] = h[n - 2]
        A[n - 1, n - 2] = -(h[n - 3] + h[n - 2])
        A[n - 1, n - 1] = h[n - 3]
        self.M = np.linalg.solve(A, rhs)

    def _pieces(self, r):
        """Interval index per radius, clipped to the knot
        range (constant-extension semantics handled by the
        caller's derivative zeroing)."""
        rc = np.clip(r, self.x[0], self.x[-1])
        idx = np.searchsorted(self.x, rc, side='right') - 1
        idx = np.clip(idx, 0, self.n - 2)
        return rc, idx

    def eval_all(self, r):
        """(value, d1, d2) at radii r (array-like)."""
        r = np.asarray(r, dtype=DTYPE)
        rc, i = self._pieces(r)
        x, y, M, h = self.x, self.y, self.M, self.h
        hi = h[i]
        a = (x[i + 1] - rc) / hi          # weight of left end
        b = (rc - x[i]) / hi              # weight of right end
        val = (a * y[i] + b * y[i + 1]
               + ((a ** 3 - a) * M[i] + (b ** 3 - b) * M[i + 1])
               * hi ** 2 / 6.0)
        d1 = ((y[i + 1] - y[i]) / hi
              + hi / 6.0 * ((3.0 * b ** 2 - 1.0) * M[i + 1]
                            - (3.0 * a ** 2 - 1.0) * M[i]))
        d2 = a * M[i] + b * M[i + 1]
        outside = (r < self.x[0]) | (r > self.x[-1])
        if np.any(outside):
            d1 = np.where(outside, 0.0, d1)
            d2 = np.where(outside, 0.0, d2)
        return val, d1, d2

    def __call__(self, r):
        return self.eval_all(r)[0]


def eval_corr(spline, r):
    """Registered _eval_corr semantics on the gate spline:
    (d, d', d'') with constant extension outside."""
    return spline.eval_all(r)


# ---------------------------------------------------------------- mpmath
class NotAKnotSplineMP:
    """The same construction in mpmath arithmetic."""

    def __init__(self, mp, x, y):
        self.mp = mp
        n = len(x)
        self.n = n
        self.x = [mp.mpf(v) for v in x]
        self.y = [mp.mpf(v) for v in y]
        h = [self.x[i + 1] - self.x[i] for i in range(n - 1)]
        self.h = h
        A = mp.matrix(n, n)
        rhs = mp.matrix(n, 1)
        A[0, 0] = h[1]
        A[0, 1] = -(h[0] + h[1])
        A[0, 2] = h[0]
        for i in range(1, n - 1):
            A[i, i - 1] = h[i - 1]
            A[i, i] = 2 * (h[i - 1] + h[i])
            A[i, i + 1] = h[i]
            rhs[i] = 6 * ((self.y[i + 1] - self.y[i]) / h[i]
                          - (self.y[i] - self.y[i - 1]) / h[i - 1])
        A[n - 1, n - 3] = h[n - 2]
        A[n - 1, n - 2] = -(h[n - 3] + h[n - 2])
        A[n - 1, n - 1] = h[n - 3]
        sol = mp.lu_solve(A, rhs)
        self.M = [sol[i] for i in range(n)]

    def eval_all(self, r):
        mp = self.mp
        r = mp.mpf(r)
        x, y, M, h = self.x, self.y, self.M, self.h
        rc = min(max(r, x[0]), x[-1])
        i = 0
        while i < self.n - 2 and rc >= x[i + 1]:
            i += 1
        hi = h[i]
        a = (x[i + 1] - rc) / hi
        b = (rc - x[i]) / hi
        val = (a * y[i] + b * y[i + 1]
               + ((a ** 3 - a) * M[i] + (b ** 3 - b) * M[i + 1])
               * hi ** 2 / 6)
        d1 = ((y[i + 1] - y[i]) / hi
              + hi / 6 * ((3 * b ** 2 - 1) * M[i + 1]
                          - (3 * a ** 2 - 1) * M[i]))
        d2 = a * M[i] + b * M[i + 1]
        if r < x[0] or r > x[-1]:
            d1, d2 = mp.mpf(0), mp.mpf(0)
        return val, d1, d2
