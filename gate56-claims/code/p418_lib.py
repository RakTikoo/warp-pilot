#!/usr/bin/env python3
"""
p418_lib.py -- Phase 418 machinery: THE
CARRYING-AWARE HUNT. Registration:
p418_registration.md (filed before any
computation).

The assembly and reads are Phase 414's
verbatim (p414_lib: profiles_at414 /
set_read414 / nec_at414 / adversary_polish414
/ worst_null_at414 / phys_row414 -- the 398
base assembly with the base PARAMETERISED and
405's free S spline on a zero base). This lib
adds only: the seed bases (400's winner,
native K_B = 17; B1 from
phase414/results/p414_base.json, native
K_B = 9), the stored seed shapes (405's G50
winner, 412's P* winner, B1's Part-2 T1
winner), the joint PEN400 pricing PEN418
(SS4), the K-resampling representation move
for base corrections, and the stored bars.
float64. Programme venv. WP root from env
P418_WP.
"""
import json
import os
import sys

import numpy as np
from scipy.interpolate import CubicSpline

WP = os.environ.get('P418_WP', '/home/hatch/workspace/warp-pilot')
for _v in ('P414_WP', 'P406_WP', 'P405_WP', 'P400_WP',
           'P398_WP', 'P395_WP', 'P394_WP', 'P389_WP'):
    os.environ.setdefault(_v, WP)
for _p in (f'{WP}/phase418/work', f'{WP}/phase414/work',
           f'{WP}/phase406/work', f'{WP}/phase405/work',
           f'{WP}/phase404/work', f'{WP}/phase398/work',
           f'{WP}/phase395/work', f'{WP}/phase394/work',
           f'{WP}/phase389/work', f'{WP}/phase341/work',
           f'{WP}/phase381/work'):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import p414_lib as L414  # noqa: E402
import p405_lib as L405  # noqa: E402
import p400_lib as L400  # noqa: E402
import p398_lib as L398  # noqa: E402

DTYPE = L398.DTYPE
BETA = L398.BETA
FINE_R = L398.FINE_R
L316 = L398.L316
knots = L405.knots

LAM400 = L400.LAM400                      # 1.0e-5
LAM_REG = L400.LAM_REG                    # 1.0e-2
VN_BOUND, VM_BOUND = L400.VN_BOUND, L400.VM_BOUND   # 0.35, 1.0
N_FLOOR, M_FLOOR = L400.N_FLOOR, L400.M_FLOOR       # 0.55, 1.0
MU_BOUNDS = (0.1, 6.0, 0.1, 30.0)         # muN lo/hi, muM lo/hi (406 SS4)

CRIT = L405.SS7_BAR                       # 0.4426742490267404
H2_PEAK = L405.H2_PEAK                    # 0.8853484980534808

# --------------------------------- stored bars (SS1)
M0_400 = 1.3977194851281464e-06
J1_400 = 1.2273852081052888e-06           # THE CRITERION BAR
J2_400 = 6.699288757141148e-07            # THE 2x BAR
G50_TG = dict(L414.G50_TG)
G50_NEC_R = L414.G50_NEC_R
G50_WORST_NULL = L414.G50_WORST_NULL
PSTAR_SEC = L414.PSTAR_SEC
PSTAR_WORST_NULL = L414.PSTAR_WORST_NULL
PSTAR_NEC_R = L414.PSTAR_NEC_R

L1_B1 = 6.257021665543401e-06
B1_T1_JOINT = -4.60458433226168e-06
B1_T1_WORST_NULL = -4.666009738694515e-06
B1_T1_NEC_R = 16.21951219512195
B1_T1_SEC = -0.000728237917620445
B1_SEED_SHAPE_JOINT = -5.503912e-05       # 414's record (S-C datum)
B1_T2_JOINT = -2.047771471716486e-05

SPEND_400 = {1: M0_400 - J1_400, 2: M0_400 - J2_400}
SPEND_B1 = {1: L1_B1 - B1_T1_JOINT, 2: L1_B1 - B1_T2_JOINT}

# --------------------------------- the seed bases
BASE400 = {'muN': L405.WIN_MUN, 'muM': L405.WIN_MUM,
           'K': L405.WIN_K,
           'vN': np.array(L405.WIN_VN, dtype=DTYPE),
           'vM': np.array(L405.WIN_VM, dtype=DTYPE),
           'joint': M0_400, 'sec_min': L405.WIN_TG['sec']}
BASEB1 = L414.load_base()                 # p414_base.json verbatim

# --------------------------------- the seed shapes
G50_KNOTS = np.array(L414.G50_KNOTS, dtype=DTYPE)      # K_S = 9


def _load_json(path):
    with open(path) as f:
        return json.load(f)


_rungs = _load_json(f'{WP}/phase412/results/p412_rungs.json')
PSTAR_KNOTS = np.array(_rungs['m2']['winner']['vS_scaled'],
                       dtype=DTYPE)                    # K_S = 9
_state2 = _load_json(f'{WP}/phase414/results/p414_state2.json')
B1T1_KNOTS = np.array(
    _state2['targets']['T1']['winner']['vS_scaled'],
    dtype=DTYPE)                                       # K_S = 17
B1T2_KNOTS = np.array(
    _state2['targets']['T2']['winner']['vS_scaled'],
    dtype=DTYPE)
B1T2_K = int(_state2['targets']['T2']['winner_K'])

# --------------------------------- verbatim reads (414 form)
profiles_at = L414.profiles_at414
T_at = L414.T_at414
set_read = L414.set_read414
nec_at = L414.nec_at414
adversary_polish = L414.adversary_polish414
worst_null_at = L414.worst_null_at414
phys_row = L414.phys_row414
positivity_ok = L398.positivity_ok398
joint_of_read = L405.joint_of_read
peak_of_shape = L405.peak_of_shape
scale_to_peak = L405.scale_to_peak
h2_seed = L405.h2_seed
rough = L400.rough


def pen418(vN, vM, vS_scaled):
    """PEN418 (registration SS4): LAM400 x
    [rough(vN) + rough(vM) + rough(vS_scaled)]
    -- 400's penalty400 on the base sectors
    plus 405's pen400 on the scaled shape."""
    tot = rough(vN) + rough(vS_scaled)
    if vM is not None:
        tot += rough(vM)
    return LAM400 * tot


def box_for_peak(P):
    """412 SS5's per-rung amplitude box on the
    scaled knot vector."""
    return max(1.0, 2.0 * P / BETA)


def step_scale(P):
    return max(1.0, P / CRIT)


def cd_steps(P):
    s = step_scale(P)
    return (0.05 * s, 0.02 * s, 0.008 * s)


def shape_at_knots(v_from, K_from, K_to):
    """Sample a spline's knot vector at another
    K's knots (the lineage's representation
    move; used for shapes AND base corrections,
    which are the same spline form)."""
    cs = CubicSpline(knots(K_from),
                     np.asarray(v_from, dtype=DTYPE),
                     bc_type='not-a-knot')
    return np.array(cs(knots(K_to)), dtype=DTYPE)


def base_at_K(base, K_to):
    """The base with its corrections resampled
    to K_to knots (spline sampling; SS4's
    representation move). muN/muM unchanged."""
    if int(base['K']) == int(K_to):
        return {'muN': float(base['muN']),
                'muM': float(base['muM']), 'K': int(K_to),
                'vN': np.array(base['vN'], dtype=DTYPE),
                'vM': np.array(base['vM'], dtype=DTYPE)}
    return {'muN': float(base['muN']),
            'muM': float(base['muM']), 'K': int(K_to),
            'vN': shape_at_knots(base['vN'], base['K'], K_to),
            'vM': shape_at_knots(base['vM'], base['K'], K_to)}


BASE400_K9 = base_at_K(BASE400, 9)


def base_dict(muN, muM, K, vN, vM):
    return {'muN': float(muN), 'muM': float(muM),
            'K': int(K),
            'vN': np.array(vN, dtype=DTYPE),
            'vM': np.array(vM, dtype=DTYPE)}


def guards_ok(muN, muM, vN, vM):
    """SS4's guards/box on the base sectors
    (the shape box is checked separately)."""
    lo_n, hi_n, lo_m, hi_m = MU_BOUNDS
    if not (lo_n <= muN <= hi_n and lo_m <= muM <= hi_m):
        return False
    if np.max(np.abs(vN)) > VN_BOUND:
        return False
    if np.max(np.abs(vM)) > VM_BOUND:
        return False
    return True


def peak_radius(vS, K):
    """Peak |beta*S| and its FINE_R attainment
    radius (412's form)."""
    cs = CubicSpline(knots(K), np.asarray(vS, dtype=DTYPE),
                     bc_type='not-a-knot')
    vals = np.abs(BETA * cs(FINE_R))
    i = int(np.argmax(vals))
    return float(vals[i]), float(FINE_R[i])
