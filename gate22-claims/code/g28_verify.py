#!/usr/bin/env python3
"""GATE-28 independent verification.

Pure arithmetic on Phase 270's STORED refit table
(phase270/results/p270_results.json). No refit is re-run,
no engine is imported, no march is touched. Every deciding
number of Phase 270's memo/checkpoint that the reworded
fence (i) will carry is re-derived here from the stored
rows: the 60-refit distribution, the band-membership count
and its window anatomy, the Leg-3 Tier-1 divisor range,
the cross-product total, the linearised crossing range,
and the two ordering checks. Gate-27's stability band and
linearised slope are taken from gate27's own record
(g27_verify_results.json / GATE27.md SS2) as the priced
instrument the fence applies -- this gate verifies the
application, not the instrument (the instrument's own
status is attack line (1) of GATE28.md, priced there).
"""
import json
import statistics

WP = "/home/hatch/workspace/warp-pilot"
p270 = json.load(open(f"{WP}/phase270/results/p270_results.json"))

C_TRIM_STORED = 5.253378225339471
SBAR_REG = 1.1540830919809508
BAND = (-0.11264, 0.10352)          # Gate-27 stability band, delta c_trim
T_STAR = 0.6782280511877113         # Gate-27 linearised crossing
SLOPE = 0.0289                      # Gate-27: t per unit delta c_trim
WOUND = (0.55625, 0.5625)
CLAMPED = (0.65625, 0.6625)

out = {}

# --- 1. The 60-refit distribution, recomputed from stored rows ----------
refits = p270["leg2"]["refits"]
assert len(refits) == 60, len(refits)
cts = [r["c_trim_at_registered_divisor"] for r in refits]
out["n_refits"] = len(refits)
out["c_trim_min"] = min(cts)
out["c_trim_max"] = max(cts)
out["c_trim_median"] = statistics.median(cts)
out["leg2_delta_range"] = [min(cts) - C_TRIM_STORED, max(cts) - C_TRIM_STORED]
out["stored_distribution_matches"] = (
    abs(min(cts) - p270["leg2"]["distribution_c_trim"]["min"]) < 1e-12
    and abs(max(cts) - p270["leg2"]["distribution_c_trim"]["max"]) < 1e-12
    and abs(statistics.median(cts) - p270["leg2"]["distribution_c_trim"]["median"]) < 1e-12
)
# internal consistency of each stored row: c_trim == -c2 / sbar_registered
out["row_identity_max_dev"] = max(
    abs(r["c_trim_at_registered_divisor"] - (-r["c2"]) / SBAR_REG) for r in refits
)

# --- 2. Band membership: count and window anatomy -----------------------
band_lo = C_TRIM_STORED + BAND[0]
band_hi = C_TRIM_STORED + BAND[1]
in_band = [r for r in refits if band_lo <= r["c_trim_at_registered_divisor"] <= band_hi]
out["n_in_band"] = len(in_band)
out["in_band_rows"] = [
    {
        "window": [r["window_start"], r["window_end"]],
        "subsetting": r["subsetting"],
        "weighting": r["weighting"],
        "c_trim": r["c_trim_at_registered_divisor"],
    }
    for r in in_band
]
out["in_band_all_maximal_corner"] = all(
    r["window_end"] == 0.475 or (r["window_end"] == 0.45 and r["window_start"] > 0.0)
    for r in in_band
)
# the stored coefficient IS the registered-baseline refit row:
base_rows = [
    r for r in refits
    if r["window_start"] == 0.0 and r["window_end"] == 0.475
    and r["subsetting"] == "full_lattice_step0.025" and r["weighting"] == "OLS"
]
out["baseline_row_is_stored_coefficient"] = (
    len(base_rows) == 1 and abs(base_rows[0]["c_trim_at_registered_divisor"] - C_TRIM_STORED) < 1e-12
)
# window-end marginal anatomy (baseline start/subsetting/weighting):
ends = {}
for e in (0.375, 0.40, 0.425, 0.45, 0.475):
    rows = [
        r for r in refits
        if r["window_start"] == 0.0 and r["window_end"] == e
        and r["subsetting"] == "full_lattice_step0.025" and r["weighting"] == "OLS"
    ]
    if rows:
        v = rows[0]["c_trim_at_registered_divisor"]
        ends[str(e)] = {"c_trim": v, "pct_vs_stored": 100.0 * (v - C_TRIM_STORED) / C_TRIM_STORED}
out["end_marginals_baseline"] = ends

# --- 3. Leg-3 Tier-1 divisor range, from stored tier rows ---------------
t1 = p270["leg3"]["tier1"]
out["leg3_tier1_raw"] = t1
# extract the three summary divisors and their implied c_trim at baseline q2
q2 = p270["baseline"]["q2"]

# --- 4. Cross-product total, recomputed from the two marginals ----------
c2_abs_min = -p270["leg2"]["distribution_c2"]["max"]   # 4.751315536043338
c2_abs_max = -p270["leg2"]["distribution_c2"]["min"]   # 6.526176061254181
out["c2_abs_range"] = [c2_abs_min, c2_abs_max]

# --- 5. Leg-1 +-1 SE band ------------------------------------------------
se_ct = p270["leg1"]["SE_c_trim"]
out["leg1_pm1SE_band"] = [C_TRIM_STORED - se_ct, C_TRIM_STORED + se_ct]
out["leg1_band_exits_both_sides"] = (
    C_TRIM_STORED - se_ct < band_lo and C_TRIM_STORED + se_ct > band_hi
)
out["leg1_diagnostics"] = {
    "SE_q2": p270["leg1"]["SE_q2"],
    "SE_c_trim": se_ct,
    "sign_runs": p270["leg1"]["sign_runs"],
    "durbin_watson": p270["leg1"]["durbin_watson"],
    "declaration": p270["leg1"]["declaration"],
    "enters_total": p270["leg1"]["enters_total"],
}

# --- 6. Cross-product total, from the two marginal ranges ---------------
sbar_lo = min(v["divisor"] for v in t1.values() if isinstance(v, dict) and "divisor" in v)
sbar_hi = max(v["divisor"] for v in t1.values() if isinstance(v, dict) and "divisor" in v)
out["tier1_divisor_range"] = [sbar_lo, sbar_hi]
total_lo = c2_abs_min / sbar_hi     # smallest |q2| over largest divisor
total_hi = c2_abs_max / sbar_lo     # largest |q2| over smallest divisor
out["cross_product_total_c_trim"] = [total_lo, total_hi]
out["cross_product_total_delta"] = [total_lo - C_TRIM_STORED, total_hi - C_TRIM_STORED]
stored_total = p270["total"]["total_interval_c_trim"]
out["cross_product_matches_stored_total"] = (
    abs(total_lo - stored_total[0]) < 1e-9 and abs(total_hi - stored_total[1]) < 1e-9
)
out["exit_lo_by"] = BAND[0] - out["cross_product_total_delta"][0]
out["exit_hi_by"] = out["cross_product_total_delta"][1] - BAND[1]
out["leg2_alone_exits_both_sides"] = (
    out["leg2_delta_range"][0] < BAND[0] and out["leg2_delta_range"][1] > BAND[1]
)
out["tier1_delta_range"] = [
    p270["total"]["marginals"]["leg3_tier1_c_trim_range_at_baseline_q2"][0] - C_TRIM_STORED,
    p270["total"]["marginals"]["leg3_tier1_c_trim_range_at_baseline_q2"][1] - C_TRIM_STORED,
]
out["tier1_alone_inside_band"] = (
    out["tier1_delta_range"][0] >= BAND[0] and out["tier1_delta_range"][1] <= BAND[1]
)

# --- 7. Linearised crossing range (Gate-27's instrument, applied) -------
d_lo, d_hi = out["cross_product_total_delta"]
cross_lo = T_STAR + SLOPE * d_lo    # negative delta -> earlier crossing
cross_hi = T_STAR + SLOPE * d_hi
out["crossing_range"] = [cross_lo, cross_hi]
out["crossing_range_matches_stored"] = (
    abs(cross_lo - p270["verdict"]["linearised_crossing"]["crossing_range"][0]) < 1e-9
    and abs(cross_hi - p270["verdict"]["linearised_crossing"]["crossing_range"][1]) < 1e-9
)

# --- 8. Ordering checks ---------------------------------------------------
out["wound_survives_full_range"] = cross_lo > WOUND[1]
out["wound_clearance_at_min_crossing"] = cross_lo - WOUND[1]
out["clamped_ordering_survives"] = cross_lo > CLAMPED[1]
out["crossing_range_straddles_clamped"] = cross_lo < CLAMPED[0] and cross_hi > CLAMPED[1]
out["straddle_amounts"] = {
    "range_begins_below_clamped_lo_by": CLAMPED[0] - cross_lo,
    "range_ends_above_clamped_hi_by": cross_hi - CLAMPED[1],
}
# crossing shifts about t* at the total-range ends (memo SS-verdict figures)
out["crossing_shifts_about_tstar"] = [SLOPE * d_lo, SLOPE * d_hi]
# in band-percentage terms: the total uncertainty vs the band half-widths
out["uncertainty_vs_band"] = {
    "lo_ratio_to_band_lo": d_lo / BAND[0],
    "hi_ratio_to_band_hi": d_hi / BAND[1],
    "pct_of_coefficient": [100.0 * d_lo / C_TRIM_STORED, 100.0 * d_hi / C_TRIM_STORED],
}

# --- 9. Stored-coefficient percentile in the defensible set -------------
out["stored_coefficient_rank_ascending"] = 1 + sum(1 for c in cts if c < C_TRIM_STORED)
out["refits_above_stored_all_start_dropped"] = all(
    r["window_start"] > 0.0 for r in refits if r["c_trim_at_registered_divisor"] > C_TRIM_STORED
)

# --- 10. Curve-based cross-check of the linearised crossing range -------
# Attack line (1) instrument: Gate-27's linearisation holds BOTH the
# amplitude response (~1.0/unit, t^2 law) and the crossing slope
# (-15.8985/unit t, the tangent across the certified bracket) constant.
# The certificate's own stored per-instant limits (Phase 266) give the
# TRUE margin curve L(t); applying the same measured amplitude response
# to that curve -- M_delta(t) = L(t) + t^2 * delta, sensitivity 1.0 --
# removes the tangent assumption and prices what it costs. Piecewise-
# linear interpolation on the stored limits; sensitivity taken as 1.0
# (Gate-27 measured 1.009839 / 1.006338 / 0.999345 at the three sites).
p266 = json.load(open(f"{WP}/phase266/results/p2661_results.json"))
per = p266["certificate"]["per_instant"]
ts = sorted(float(t) for t in per.keys())
Ls = [per[f"{t:.5g}" if f"{t:.5g}" in per else str(t)]["NEC_ph"]["L"] for t in ts]
# rebuild robustly: keys are decimal strings of the instants
Ls = []
for t in ts:
    key = next(k for k in per.keys() if abs(float(k) - t) < 1e-12)
    Ls.append(per[key]["NEC_ph"]["L"])
out["window_instants"] = ts
out["window_limits"] = Ls
slopes = [(Ls[i + 1] - Ls[i]) / (ts[i + 1] - ts[i]) for i in range(len(ts) - 1)]
out["margin_curve_local_slopes"] = slopes

def interp(t):
    if t <= ts[0]:
        return Ls[0] + slopes[0] * (t - ts[0])
    for i in range(len(ts) - 1):
        if ts[i] <= t <= ts[i + 1]:
            return Ls[i] + slopes[i] * (t - ts[i])
    return Ls[-1] + slopes[-1] * (t - ts[-1])

def curve_crossing(delta, sens=1.0):
    # solve L(t) + sens * t^2 * delta = 0 by bisection on [0.60, 0.75]
    lo, hi = 0.60, 0.75
    f = lambda t: interp(t) + sens * t * t * delta
    flo = f(lo)
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if (f(mid) > 0) == (flo > 0):
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)

cc_lo = curve_crossing(d_lo)
cc_hi = curve_crossing(d_hi)
out["curve_based_crossing_range"] = [cc_lo, cc_hi]
out["curve_vs_linearised"] = {
    "lo_shift": cc_lo - cross_lo,
    "hi_shift": cc_hi - cross_hi,
}
out["curve_wound_clearance"] = cc_lo - WOUND[1]
out["curve_straddle"] = {
    "below_clamped_lo_by": CLAMPED[0] - cc_lo,
    "above_clamped_hi_by": cc_hi - CLAMPED[1],
}
# consistency: Gate-27's endpoint band under the same instrument --
# delta at which the t=0.675 margin flips: -L(0.675)/0.675^2
i675 = ts.index(0.675)
out["endpoint_band_rederived"] = [
    -Ls[i675] / (0.675 ** 2),
    -per["0.68125"]["NEC_ph"]["L"] / (0.68125 ** 2),
]
# amplitude excursion at the crossing implied by the total delta range
out["amplitude_excursion_at_crossing"] = [abs(d_lo) * T_STAR ** 2, abs(d_hi) * T_STAR ** 2]
out["bracket_end_margins"] = [Ls[i675], per["0.68125"]["NEC_ph"]["L"]]

json.dump(out, open(f"{WP}/gate28/work/g28_verify_results.json", "w"), indent=1)
print(json.dumps(out, indent=1))
