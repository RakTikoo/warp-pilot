#!/usr/bin/env python3
"""
p412_lib.py -- Phase 412 machinery: THE SPEED
LADDER. Registration: p412_registration.md
(filed before any computation).

The assembly and reads are Phase 405's
verbatim (p405_lib: profiles_at405 /
set_read405 / phys_row405 / worst_null_at405 /
adversary_polish405 on Phase 400's winner
base, S a free not-a-knot spline). This lib
adds only the ladder's constants (SS1/SS5):
the Gate-50 winner vector, the rung table,
the per-rung amplitude box and step scaling.
float64. Programme venv. WP root from env
P412_WP.
"""
import os
import sys

import numpy as np

WP = os.environ.get('P412_WP', '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, f'{WP}/phase405/work')

import p405_lib as L  # noqa: E402

DTYPE = L.DTYPE
BETA = L.BETA
FINE_R = L.FINE_R
CRIT = L.SS7_BAR                      # 0.4426742490267404
M0 = L.WIN_JOINT                      # +1.3977194851281464e-06
WIN_TG = L.WIN_TG

# The Gate-50 winner (SS1): K = 9 knots at the
# criterion amplitude (p405_confirmation.json,
# shapeC_knots_at_criterion).
G50_KNOTS = np.array(
    [0.40243113547885484, 0.23237610808870765,
     0.10110504581235646, 0.030274386301308052,
     0.021559512630984955, 0.01297222477301449,
     0.007865452045132022, 0.0035285750792539276,
     -0.00043513901545560714], dtype=DTYPE)
G50_JOINT = 1.2273852081052888e-06
G50_SEC = -2.213556504990559e-04
G50_NEC_R = 17.926829268292682
G50_PEAK = 0.44267424902674035

# Rung multiples (SS5): fixed ladder then
# adaptive x3 in m.
FIXED_MULTS = [2, 5, 10, 25, 100]
CEILING_PEAK = 1.0e6


def rung_targets():
    """The full registered target list
    [(mult, peak), ...] in climb order,
    adaptive continuation included up to the
    ceiling (SS5). The ladder stops earlier
    per the bracket rule."""
    out = [(m, m * CRIT) for m in FIXED_MULTS]
    m = 100
    while True:
        m *= 3
        p = m * CRIT
        if p > CEILING_PEAK:
            break
        out.append((m, p))
    return out


def box_for_peak(P):
    """SS5's per-rung amplitude box on the
    scaled knot vector."""
    return max(1.0, 2.0 * P / BETA)


def step_scale(P):
    return max(1.0, P / CRIT)


def cd_steps(P):
    s = step_scale(P)
    return (0.05 * s, 0.02 * s, 0.008 * s)


# verbatim reads (SS4)
set_read = L.set_read405
phys_row = L.phys_row405
worst_null_at = L.worst_null_at405
adversary_polish = L.adversary_polish405
scale_to_peak = L.scale_to_peak
peak_of_shape = L.peak_of_shape
h2_seed = L.h2_seed
pen400 = L.pen400
joint_of_read = L.joint_of_read
knots = L.knots


def peak_radius(vS, K):
    """Peak |beta*S| and its FINE_R attainment
    radius (SS4)."""
    from scipy.interpolate import CubicSpline
    cs = CubicSpline(knots(K),
                     np.asarray(vS, dtype=DTYPE),
                     bc_type='not-a-knot')
    vals = np.abs(BETA * cs(FINE_R))
    i = int(np.argmax(vals))
    return float(vals[i]), float(FINE_R[i])


def shape_at_knots(vS_from, K_from, K_to):
    """Sample a shape's spline at another K's
    knots (the 405 Stage E warm-start form)."""
    from scipy.interpolate import CubicSpline
    cs = CubicSpline(knots(K_from),
                     np.asarray(vS_from, dtype=DTYPE),
                     bc_type='not-a-knot')
    return np.array(cs(knots(K_to)), dtype=DTYPE)
