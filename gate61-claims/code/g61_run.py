#!/usr/bin/env python
"""Gate-61 driver — INDEPENDENT RE-JUDGEMENT OF PHASE 478'S TWO
SHADOW DATA (ledger entry 1243). Registration:
gate61/work/g61_registration.md (written BEFORE this computation).

The gate's own driver: the two builds are imported from their
defining modules (p1621_engine = the datum build per P226-1
registration SS2; p167_engine = the compensated build;
lateral_tide = the record's tide sampler). Everything downstream
of the channel arrays is the gate's own code: CH-COMB posing,
director addition, clause arithmetic (implemented here from the
clause definitions), scale reads, rescue/beta-ceiling arithmetic,
E_shell quadrature (scipy Simpson base; gate fine-Simpson +
mpmath director cross-check), FD-Riemann second tide path,
D-identity perturbation and symbolic gradient tests, and the
documentary evidence pack (own counts, own text extraction, own
absence scan). Controls asserted before any deciding read.
Frame: Phase 166 pin, Gate-19-corrected tensor, venv python,
float64 (+ mpmath 50-digit where registered). INTERNAL only;
writes only in gate61/."""
import json, math, os, re, sys, time
import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase254/work')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase162/work')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase167/work')
import lateral_tide as LT          # noqa: E402
import p1621_engine as B           # noqa: E402
import p167_engine as E            # noqa: E402

ROOT = '/home/hatch/workspace/warp-pilot'
T0 = time.time()
C_LIGHT = 299792458.0
G_NEWTON = 6.67430e-11
BAR = 4.905
A_THROAT = 0.8
TH = B.AUDIT_TH.copy()
CK = list(B.CLAUSE_KEYS)
KAP_PREMIUM = 0.254873
I_STAR = 90
assert abs(TH[I_STAR] - np.pi / 2) < 1e-12

res = {'gate': 'Gate-61 — independent re-judgement of Phase 478',
       'charge': 'ledger entry 1243',
       'claim': 'ledger entry 1242 (Phase 478 verdict: A SECOND '
                'DATUM; identity decided for the home object)',
       'registration': 'gate61/work/g61_registration.md (pre-run)',
       'frame': 'Phase 166 pin, Gate-19-corrected tensor, venv '
                'python, float64; mpmath 50-digit where registered',
       'desk': 'NO DATA CONTACT'}

# =====================================================================
# THE GATE'S OWN downstream arithmetic
# =====================================================================
def gate_clauses(rho, pr, pt, pp):
    """The seven clauses from their definitions (entry 1243 SS(b)
    machinery): NEC = rho + p_i, WEC = rho, DEC = rho - |p_i|.
    Implemented here; cross-checked against the engine's
    clauses_of under CTL-CLAUSE, not used from it."""
    return {'NEC_rho': rho + pr, 'NEC_th': rho + pt,
            'NEC_ph': rho + pp, 'WEC': rho,
            'DEC_rho': rho - np.abs(pr), 'DEC_th': rho - np.abs(pt),
            'DEC_ph': rho - np.abs(pp)}


CLAUSE_DIFF_MAX = [0.0]


def gate_clauses_checked(rho, pr, pt, pp):
    mine = gate_clauses(rho, pr, pt, pp)
    eng = B.clauses_of(rho, pr, pt, pp)
    for k in CK:
        d = float(np.max(np.abs(mine[k] - eng[k])))
        if d > CLAUSE_DIFF_MAX[0]:
            CLAUSE_DIFF_MAX[0] = d
    return mine


C1_GATE = (1.0 - np.cos(TH))**2 / (np.sin(TH)**2 * B.R00**2)


def gate_director(ch, kap):
    """The director channel addition of P226-1 registration SS2,
    recomputed by the gate (c1 from the registered formula)."""
    return {'rho8': ch['rho8'] + 0.5 * kap * C1_GATE,
            'prho8': ch['prho8'] - 0.5 * kap * C1_GATE,
            'pth8': ch['pth8'] - 0.5 * kap * C1_GATE,
            'pph8': ch['pph8'] + 0.5 * kap * C1_GATE,
            'S': ch['S']}


def gate_pose_chcomb(Jbase, a=+0.10):
    """CH-COMB flat (P226-1 SS2 primary arm): M += a, Mhh -= a."""
    J = dict(Jbase)
    J['M'] = Jbase['M'] + a * np.ones_like(TH)
    J['Mhh'] = Jbase['Mhh'] - a * np.ones_like(TH)
    return J


def gate_composition(Jbase):
    """The gate's composition read: pose, channels (defining
    module), gate director, gate clauses. Returns minima,
    argmins, clause arrays, S(theta*), posed jets, total and
    pre-director channels."""
    Jp = gate_pose_chcomb(Jbase)
    ch = B.channels(Jp, TH)
    cht = gate_director(ch, KAP_PREMIUM)
    cl = gate_clauses_checked(cht['rho8'], cht['prho8'],
                               cht['pth8'], cht['pph8'])
    mins = {k: float(np.min(cl[k])) for k in CK}
    argmins = {k: float(TH[int(np.argmin(cl[k]))]) for k in CK}
    return {'minima': mins, 'argmins': argmins, 'arrays': cl,
            'S_star': float(cht['S'][I_STAR]), 'Jp': Jp,
            'ch_tot': cht, 'ch_pre': ch}


def worst_of(arr):
    i = int(np.argmax(np.abs(arr)))
    return float(np.abs(arr[i])), float(TH[i])

# =====================================================================
# Datum machinery (the build as P226-1 SS2 defines it)
# =====================================================================
th_f = np.linspace(0.0, np.pi, 2881)
h_f = th_f[1] - th_f[0]
rhs_tru = B.att(th_f) * B.phi0_h(th_f) / B.R00 - B.att_h(th_f) / B.R00
u_tru_f = np.exp(B.phi0(th_f)) * B.cum_simpson(
    np.exp(-B.phi0(th_f)) * rhs_tru, h_f)
ut_a = B.interp_fine(th_f, u_tru_f, TH)
z = np.zeros_like(TH)
J0 = B.instant_jets(0.0, z, z, z, z, ut_a)

# =====================================================================
# CTL-H — the datum reproduced on the home path (gate clauses)
# =====================================================================
P2261 = json.load(open(f'{ROOT}/phase226/results/p2261_results.json'))
ch0 = B.channels(J0, TH)
cl0 = gate_clauses_checked(ch0['rho8'], ch0['prho8'], ch0['pth8'],
                           ch0['pph8'])
base_mins = {k: float(np.min(cl0[k])) for k in CK}
stored_base = {k: P2261['datum']['base_read'][k + '_min'] for k in CK}
base_diff = max(abs(base_mins[k] - stored_base[k]) for k in CK)
comp_H = gate_composition(J0)
stored_comb = {k: P2261['primary_point']['combined_read'][k + '_min']
               for k in CK}
comb_diff = max(abs(comp_H['minima'][k] - stored_comb[k]) for k in CK)
s_diff = abs(comp_H['S_star']
             - P2261['primary_point']['combined_read']['S_star'])
ut_star = float(ut_a[I_STAR])
ctl_h = {'base_minima': base_mins, 'base_max_abs_diff_vs_stored':
         base_diff, 'combined_minima': comp_H['minima'],
         'combined_max_abs_diff_vs_stored': comb_diff,
         'S_star': comp_H['S_star'], 'S_star_abs_diff': s_diff,
         'utilde_true_theta_star': ut_star,
         'pass': bool(base_diff == 0.0 and comb_diff == 0.0
                      and s_diff == 0.0
                      and abs(ut_star - 1.1412482021558361) <= 1e-15)}
res['controls'] = {'CTL-H': ctl_h}
print('CTL-H pass:', ctl_h['pass'], '| base diff', base_diff,
      '| combined diff', comb_diff, flush=True)
assert ctl_h['pass'], 'CONTROL CTL-H FAILED'

# =====================================================================
# X build — the compensated path (defining modules)
# =====================================================================
th_f2, times2, MU2, U2 = B.march(2881, 0.0025)
h_f2 = th_f2[1] - th_f2[0]
MTT2 = E.mtt_field(U2, 0.0025)


def base_J0_X(mtt_override=None):
    m = 0
    mu_a = B.interp_fine(th_f2, MU2[m], TH)
    mu_h_a = B.interp_fine(th_f2, B.fd4_deriv(MU2[m], h_f2), TH)
    mu_hh_a = B.interp_fine(th_f2, B.fd4_deriv2(MU2[m], h_f2), TH)
    u_a = B.interp_fine(th_f2, U2[m], TH)
    mtt_a = (B.interp_fine(th_f2, MTT2[m], TH)
             if mtt_override is None else mtt_override)
    return E.comp_jets(float(times2[m]), mu_a, mu_h_a, mu_hh_a, u_a,
                       mtt_a)


Jb_X = base_J0_X()

# =====================================================================
# CTL-X — the compensated path on its home ground
# =====================================================================
P2542 = json.load(open(f'{ROOT}/phase254/results/p2542_results.json'))
Jwound_X = dict(Jb_X)
Jwound_X['M'] = Jb_X['M'] + 0.10 * np.ones_like(TH)
Jwound_X['Mhh'] = Jb_X['Mhh'] - 0.10 * np.ones_like(TH)
Jwound_X['Auu'] = Jwound_X['Auu'] - 0.5 * np.ones_like(TH)
comps_wound = LT.lateral_tide_from_jets(Jwound_X, TH)
sw = P2542['datum_reads']['certified_wound']
wound_worsts = {c: float(np.max(np.abs(comps_wound[c])))
                for c in ('R_lthlth', 'R_tthtth', 'R_tltl')}
wound_diffs = {
    'R_lthlth': abs(wound_worsts['R_lthlth']
                    - sw['R_lthlth_worst_abs_pose^-2']),
    'R_tthtth': abs(wound_worsts['R_tthtth']
                    - sw['R_tthtth_worst_abs_pose^-2']),
    'R_tltl': abs(wound_worsts['R_tltl'] - sw['R_tltl_worst_abs_pose^-2'])}
lims = LT.mt_throat_symbolic()
anchors = LT.mt_throat()
ok_fb = (abs(abs(lims['R_lthlth']) - 0.45) <= 1e-9
         and abs(lims['R_tthtth']) <= 1e-12
         and abs(abs(lims['R_tltl']) - anchors['R_tltl'])
         / anchors['R_tltl'] <= 1e-6)
for beta, tgt in ((0.5, 5.8880), (0.9, 75.3046)):
    got = abs((1.0 / (1 - beta**2)) * (lims['R_tthtth']
              + beta**2 * lims['R_lthlth'])) * (C_LIGHT**2 / 4.785e7**2)
    cf = (1.0 / (1 - beta**2)) * beta**2 * 0.45 * (C_LIGHT**2 / 4.785e7**2)
    ok_fb &= abs(got - tgt) / tgt <= 1e-3 and abs(got - cf) / cf <= 1e-6
ctl_x = {'wound_worsts': wound_worsts, 'wound_diffs_vs_stored':
         wound_diffs, 'fallback_anchors_pass': bool(ok_fb),
         'pass': bool(all(v == 0.0 for v in wound_diffs.values())
                      and ok_fb)}
res['controls']['CTL-X'] = ctl_x
print('CTL-X pass:', ctl_x['pass'], '| wound diffs', wound_diffs,
      flush=True)
assert ctl_x['pass'], 'CONTROL CTL-X FAILED'

# =====================================================================
# CTL-467 — 467's CTL-3 comparison on gate posing
# =====================================================================
J467_H = gate_pose_chcomb(J0)
J467_X = gate_pose_chcomb(Jb_X)
jet_diff = {k: float(np.max(np.abs(np.asarray(J467_H[k], float)
                                   - np.asarray(J467_X[k], float))))
            for k in B.JET_ORDER}
comps_H = LT.lateral_tide_from_jets(J467_H, TH)
comps_X = LT.lateral_tide_from_jets(J467_X, TH)
comp_diff = {c: float(np.max(np.abs(comps_H[c] - comps_X[c])))
             for c in ('R_tltl', 'R_tthtth', 'R_lthlth')}
ctl467 = {
    'jet_diff_Fuu': jet_diff['Fuu'], 'jet_diff_Mtt': jet_diff['Mtt'],
    'jet_fields_differing_gt_1e-12':
        [k for k, v in jet_diff.items() if v > 1e-12],
    'tide_diff': comp_diff,
    'home_radial_worst': worst_of(comps_H['R_tltl']),
    'X_radial_worst': worst_of(comps_X['R_tltl']),
    'pass': bool(abs(jet_diff['Fuu'] - 0.9343747896249985) <= 1e-9
                 and abs(jet_diff['Mtt'] - 2.569525345830215e-07) <= 1e-9
                 and abs(comp_diff['R_tltl'] - 0.765001585541698) <= 1e-9
                 and comp_diff['R_tthtth'] == 0.0
                 and comp_diff['R_lthlth'] == 0.0
                 and abs(worst_of(comps_H['R_tltl'])[0]
                         - 1.5202791951713714) <= 1e-9
                 and abs(worst_of(comps_X['R_tltl'])[0]
                         - 0.9718746251967629) <= 1e-9)}
res['controls']['CTL-467'] = ctl467
print('CTL-467 pass:', ctl467['pass'], flush=True)
assert ctl467['pass'], 'CONTROL CTL-467 FAILED'

# =====================================================================
# The five 477 variants + CTL-477X (gate clauses)
# =====================================================================
variants = {
    'H_utilde_true': J0,
    'H_0': B.instant_jets(0.0, z, z, z, z, z),
    'X_mtt_field': Jb_X,
    'X_utilde_true': base_J0_X(mtt_override=ut_a),
    'X_0': base_J0_X(mtt_override=z),
}
P477 = json.load(open(f'{ROOT}/phase477/results/p477_results.json'))
stored_var_mins = P477['T3_legality_reach']['variant_minima']
var_reads = {}
ctl477x_diff = 0.0
for name, Jb in variants.items():
    vr = gate_composition(Jb)
    var_reads[name] = vr
    ctl477x_diff = max(ctl477x_diff,
                       max(abs(vr['minima'][k]
                               - stored_var_mins[name][k])
                           for k in CK))
res['controls']['CTL-477X'] = {
    'max_abs_diff_vs_p477_T3_variant_minima': ctl477x_diff,
    'pass': bool(ctl477x_diff == 0.0)}
print('CTL-477X pass:', res['controls']['CTL-477X']['pass'],
      '| diff', ctl477x_diff, flush=True)
assert res['controls']['CTL-477X']['pass'], 'CONTROL CTL-477X FAILED'

res['controls']['CTL-CLAUSE'] = {
    'gate_clause_arithmetic_vs_engine_clauses_of_max_abs_diff':
        CLAUSE_DIFF_MAX[0],
    'pass': bool(CLAUSE_DIFF_MAX[0] == 0.0)}
print('CTL-CLAUSE pass:', res['controls']['CTL-CLAUSE']['pass'],
      '| max diff', CLAUSE_DIFF_MAX[0], flush=True)
assert res['controls']['CTL-CLAUSE']['pass'], 'CONTROL CTL-CLAUSE FAILED'
print('ALL CONTROLS PASS', flush=True)

# =====================================================================
# (a) DOCUMENTARY EVIDENCE PACK — the gate's own reading
# =====================================================================
def read_text(p):
    return open(p, encoding='utf-8').read()


def count_in(path, needle):
    return read_text(path).count(needle)


# ---- G1: P226-1 registration SS2, quoted from the file itself
reg2261 = read_text(f'{ROOT}/phase226/work/p2261_registration.md')
i2 = reg2261.find('## 2.')
i3 = reg2261.find('## 3.')
sec2 = reg2261[i2:i3]
g1 = {
    'section2_names_instant_jets': 'instant_jets' in sec2,
    'section2_says_datum_build_verbatim':
        'Datum build verbatim from' in sec2,
    'section2_names_p2242_run': 'p2242_run.py' in sec2,
    'comp_jets_in_registration_total':
        count_in(f'{ROOT}/phase226/work/p2261_registration.md',
                 'comp_jets'),
    'counts': {
        'p2261_run.py': {'comp_jets': count_in(
            f'{ROOT}/phase226/work/p2261_run.py', 'comp_jets'),
            'instant_jets': count_in(
                f'{ROOT}/phase226/work/p2261_run.py', 'instant_jets')},
        'p2242_run.py': {'comp_jets': count_in(
            f'{ROOT}/phase224/work/p2242_run.py', 'comp_jets'),
            'instant_jets': count_in(
                f'{ROOT}/phase224/work/p2242_run.py', 'instant_jets')}},
    'stored_vector_reproduced_at_0.0': bool(ctl_h['pass'])}
g1['holds'] = bool(g1['section2_names_instant_jets']
                   and g1['section2_says_datum_build_verbatim']
                   and g1['counts']['p2261_run.py']['comp_jets'] == 0
                   and g1['counts']['p2242_run.py']['comp_jets'] == 0
                   and g1['stored_vector_reproduced_at_0.0'])
res['identity_G1'] = g1
print('G1 holds:', g1['holds'], '| counts:', g1['counts'], flush=True)

# ---- G2: Phase 169 (A1) set, extracted from the run record itself
rec169 = read_text(f'{ROOT}/phase169/results/p1691_run_record.md')
j = rec169.find('lock-carrying clause set')
seg = rec169[j:j + 500].replace('−', '-').replace('**', ' ')
nums = [float(x) for x in re.findall(r'[+-]?\d+\.\d+(?:e[+-]?\d+)?',
                                     seg)]
A1_SET = {'NEC_rho': nums[0], 'DEC_rho': nums[0], 'NEC_th': nums[1],
          'DEC_th': nums[1], 'NEC_ph': nums[2], 'DEC_ph': nums[2],
          'WEC': nums[3]}
a1_diff = max(abs(base_mins[k] - A1_SET[k]) for k in CK)
g2 = {'extracted_A1_set': A1_SET,
      'gate_home_base_minima': base_mins,
      'max_abs_diff': a1_diff,
      'holds': bool(a1_diff == 0.0)}
res['identity_G2'] = g2
print('G2 holds:', g2['holds'], '| A1 diff:', a1_diff, flush=True)

# ---- G3: Phase 167 (R1) text + the gate's absence scan
ck167 = read_text(f'{ROOT}/phase167/CHECKPOINT167.md')
flat167 = re.sub(r'\s+', ' ', ck167)
r1_present = ('NOT an extension of the datum\'s' in flat167
              and 'what is restored is the audit\'s channel values, '
                  'not the datum\'s jets' in flat167)
scan_files = []
for d in sorted(os.listdir(ROOT)):
    full = os.path.join(ROOT, d)
    if not (os.path.isdir(full)
            and (d.startswith('phase') or d.startswith('gate'))):
        continue
    for dirpath, dirnames, filenames in os.walk(full):
        dirnames[:] = [x for x in dirnames
                       if x not in ('__pycache__', 'kaggle')]
        for fn in filenames:
            if fn.endswith('.md') and ('registration' in fn
                                       or 'CHECKPOINT' in fn
                                       or 'run_record' in fn):
                scan_files.append(os.path.join(dirpath, fn))
both_marker = []
comp_population = []
for p in scan_files:
    try:
        t = read_text(p)
    except Exception:
        continue
    comp = ('comp_jets' in t) or ('compensated' in t)
    if comp:
        comp_population.append(os.path.relpath(p, ROOT))
    if comp and ('0.254873' in t or 'CH-COMB' in t):
        both_marker.append(os.path.relpath(p, ROOT))
g3 = {'R1_text_present_verbatim': bool(r1_present),
      'scan_set_size': len(scan_files),
      'compensated_population_size': len(comp_population),
      'both_marker_files': sorted(both_marker),
      'coordinator_classification': {
          'phase203/work/p2034_registration.md':
              'OTHER-DATUM — the compensated march with the wound '
              'director sector alone (no CH-COMB, no combined '
              'datum); 0.254873 cited as the director-alone '
              'premium price',
          'phase221/work/p2212_registration.md':
              'OTHER-DATUM — director-alone life-extension item; '
              'compensated machinery as a control; 0.254873 in a '
              'Phase-203 closure control',
          'phase229/work/p2291_registration.md':
              'OTHER-OBJECT — FU-P226-1, THE COMBINED MARCH: a '
              'sustainment registration. Its C0 control fixes the '
              'datum on the HOME build verbatim (max abs diff '
              '<= 1e-9) and its marched pose is posed on comp_jets '
              'by its own definition; its recorded t = 0 '
              'march-slice NEC_ph is +0.903081, quoted in '
              'CHECKPOINT229 as a MARCH-SLICE value, never as '
              'the datum vector',
          'phase233/work/p2331_registration.md':
              'OTHER-OBJECT — FU-P229-1, the march-priced combined '
              'pose (kappa moved off the premium point); a march '
              'object',
          'phase233/work/p2331_registration_addendum.md':
              'OTHER-OBJECT — addendum to the same march item',
          'phase233/CHECKPOINT233.md':
              'OTHER-OBJECT — checkpoint of the same march line',
          'phase234/work/p2341_registration.md':
              'OTHER-OBJECT — FU-P233-1, a march-slice channel on '
              'the march-priced combined pose (the Gate-27 '
              'certified pose family: kappa = 0.3 + CH-PHI-Auu — '
              'a different composition)',
          'phase246/work/p2462_registration.md':
              'OTHER-DATUM — ports the phi-channel to the '
              'combined-class SOS throat datum (Phase 245 object), '
              'not the P226-1 datum',
          'phase249/work/p2493_registration.md':
              'OTHER-OBJECT — GAP-2 item on the certified '
              'three-channel throat datum (Phase 234 pose)',
          'phase254/work/p2542_registration.md':
              'OTHER-DATUM — the wound datum tide scan (Phase 167 '
              'line); CH-COMB enters as Phase 249 context only',
          'phase260/work/p2601_registration.md':
              'OTHER-OBJECT — rebuild/extension problem for the '
              'Phase 234 certified datum (NEC_rho +1.7015 line)',
          'phase260/work/p2602_registration.md':
              'OTHER-OBJECT — tide-constrained design on the '
              'Phase 234 certified datum',
          'phase264/CHECKPOINT264.md':
              'OTHER-OBJECT — GAP-2 joint pose / coupled solve on '
              'the Phase 249 three-channel spec',
          'phase467/work/p467_registration.md':
              'COMPARISON — 467 CTL-3 poses the compensated build '
              'as a comparison against the datum, expressly not '
              'as the datum',
          'phase467/CHECKPOINT467.md': 'COMPARISON — as above',
          'phase477/work/p477_registration.md':
              'ARBITRATION — the Fuu arbitration itself',
          'phase477/CHECKPOINT477.md': 'ARBITRATION — as above',
          'phase478/work/p478_registration.md':
              'ARBITRATION — the re-registered arbitration under '
              'judgement here',
          'phase478/CHECKPOINT478.md': 'ARBITRATION — as above',
          'gate61/work/g61_registration.md':
              'SELF — this gate\'s registration'},
      'posing_class_files': []}
g3['holds'] = bool(r1_present and g3['posing_class_files'] == [])
res['identity_G3'] = g3
print('G3 holds:', g3['holds'], '| scan set:', len(scan_files),
      '| both-marker:', len(both_marker), flush=True)

# =====================================================================
# (b) THE SHADOW VECTORS vs the charge (entry 1243)
# =====================================================================
CHARGE_VECTORS = {
    'X_m': {'NEC_rho': 0.6781346234610093, 'DEC_rho': 0.6781346234610093,
            'NEC_th': 1.4790316944454176, 'NEC_ph': 0.9030810951057349,
            'WEC': 1.3094045367416725, 'DEC_th': 1.1394910646834866,
            'DEC_ph': 0.9030810951057349},
    'H_0': {'NEC_rho': 0.6781346234610093, 'DEC_rho': 0.6781346234610093,
            'NEC_th': 1.479198706005177, 'NEC_ph': 1.0541767526056953,
            'WEC': 1.3094045367416725, 'DEC_th': 1.0279422865525754,
            'DEC_ph': 1.0541767526056953}}
SHADOW_VARIANT = {'X_m': 'X_mtt_field', 'H_0': 'H_0'}
shadow_vec = {}
for sname, vname in SHADOW_VARIANT.items():
    vr = var_reads[vname]
    dv = max(abs(vr['minima'][k] - CHARGE_VECTORS[sname][k])
             for k in CK)
    shadow_vec[sname] = {
        'minima': vr['minima'], 'argmin_theta': vr['argmins'],
        'max_abs_diff_vs_charge': dv,
        'all_seven_strictly_positive':
            bool(all(vr['minima'][k] > 0 for k in CK)),
        'binding_clause': min(CK, key=lambda k: vr['minima'][k])}
    print('Shadow', sname, '| diff vs charge:', dv,
          '| positive:', shadow_vec[sname]
          ['all_seven_strictly_positive'], flush=True)
res['shadow_vectors'] = shadow_vec

# =====================================================================
# (c) THE D-IDENTITY — (i) perturbation on the shadow paths,
#     (ii) symbolic gradient identity from the stored expressions
# =====================================================================
d_pert = {}
for sname, vname in SHADOW_VARIANT.items():
    Jp = var_reads[vname]['Jp']
    Marr = np.asarray(Jp['M'], float)
    Farr = np.asarray(Jp['F'], float)
    fac = np.exp(2.0 * (Marr - Farr))
    ch_base = B.channels(Jp, TH)
    ti_base = LT.lateral_tide_from_jets(Jp, TH)
    entry = {}
    for delta in (-0.05, 0.03):
        JD = dict(Jp)
        JD['Fuu'] = np.asarray(Jp['Fuu'], float) + fac * delta
        JD['Mtt'] = np.asarray(Jp['Mtt'], float) + delta
        JC = dict(Jp)
        JC['Fuu'] = np.asarray(Jp['Fuu'], float) + delta
        chD = B.channels(JD, TH)
        chC = B.channels(JC, TH)
        tiD = LT.lateral_tide_from_jets(JD, TH)
        tiC = LT.lateral_tide_from_jets(JC, TH)
        entry[str(delta)] = {
            'D_preserving_max_change_channels_pth8_pph8':
                float(max(np.max(np.abs(chD[k] - ch_base[k]))
                          for k in ('pth8', 'pph8'))),
            'D_preserving_max_change_R_tltl':
                float(np.max(np.abs(tiD['R_tltl'] - ti_base['R_tltl']))),
            'D_changing_max_change_channels_pth8_pph8':
                float(max(np.max(np.abs(chC[k] - ch_base[k]))
                          for k in ('pth8', 'pph8'))),
            'D_changing_max_change_R_tltl':
                float(np.max(np.abs(tiC['R_tltl'] - ti_base['R_tltl'])))}
    d_pert[sname] = entry
res['D_identity_perturbation'] = d_pert

import sympy as sp  # noqa: E402
_SUF = ['', 'u', 'h', 't', 'uu', 'uh', 'ut', 'hh', 'ht', 'tt']
_BASES = ['F', 'M', 'A', 'W']
_th = sp.Symbol('th')
_SYMS = [sp.Symbol(b + sf) for b in _BASES for sf in _SUF]
_SYMD = {str(s): s for s in _SYMS}
_FUU = _SYMD['Fuu']
_MTT = _SYMD['Mtt']
_MSY = _SYMD['M']
_FSY = _SYMD['F']
raw129 = json.load(open(f'{ROOT}/phase129/work/p1296_derive_raw.json'))
raw254 = json.load(open(f'{ROOT}/phase254/work/p2542_riemann_jets.json'))
EXPR_SETS = {}
for k in ('rho8', 'prho8', 'pth8', 'pph8', 'mom_rho', 'mom_th',
          'mom_ph', 'S'):
    EXPR_SETS['ch:' + k] = sp.sympify(raw129[k])
for k in ('R_lthlth', 'R_tthtth_ZAMO', 'R_tltl_ZAMO'):
    EXPR_SETS['tide:' + k] = sp.sympify(raw254[k])
CARRYING = {'ch:pth8', 'ch:pph8', 'tide:R_tltl_ZAMO'}
jet_points = {vn: var_reads[vn]['Jp'] for vn in
              ('H_utilde_true', 'H_0', 'X_mtt_field', 'X_utilde_true',
               'X_0')}
sym_rows = {}
for name, expr in EXPR_SETS.items():
    dF = sp.diff(expr, _FUU)
    dM = sp.diff(expr, _MTT)
    ident = dM + sp.exp(2 * (_MSY - _FSY)) * dF
    f_id = sp.lambdify(_SYMS + [_th], ident, 'numpy')
    f_dF = sp.lambdify(_SYMS + [_th], dF, 'numpy')
    f_dM = sp.lambdify(_SYMS + [_th], dM, 'numpy')
    worst_rel = 0.0
    carries = False
    for vn, Jp in jet_points.items():
        args = [np.broadcast_to(np.asarray(Jp[b + sf], float),
                                TH.shape)
                for b in _BASES for sf in _SUF]
        iv = np.asarray(f_id(*args, TH), float)
        a = np.asarray(f_dF(*args, TH), float)
        b_ = np.asarray(f_dM(*args, TH), float)
        scale = np.maximum(np.maximum(np.abs(a), np.abs(b_)), 1e-300)
        if float(np.max(scale)) > 1e-12:
            carries = True
        worst_rel = max(worst_rel,
                        float(np.max(np.abs(iv) / scale)))
    sym_rows[name] = {'carries_Fuu_Mtt': bool(carries),
                      'expected_carrying': bool(name in CARRYING),
                      'gradient_identity_worst_rel_residual':
                          worst_rel}
sym_ok = all(r['carries_Fuu_Mtt'] == r['expected_carrying']
             and r['gradient_identity_worst_rel_residual'] <= 1e-12
             for r in sym_rows.values())
res['D_identity_symbolic'] = {'rows': sym_rows, 'pass': bool(sym_ok)}
print('D-identity symbolic pass:', sym_ok, flush=True)

# =====================================================================
# (d) SCALE INVARIANCE — premise audit + computed check (gate reads)
# =====================================================================
STRESS_PREFACTOR = C_LIGHT**4 / (8.0 * math.pi * G_NEWTON)


def stress_factor(R_phys):
    L = R_phys / A_THROAT
    return STRESS_PREFACTOR / L**2


def legality_at_radius(ch_tot, vec, R_phys):
    s = stress_factor(R_phys)
    cl_phys = gate_clauses_checked(ch_tot['rho8'] * s,
                                   ch_tot['prho8'] * s,
                                   ch_tot['pth8'] * s,
                                   ch_tot['pph8'] * s)
    phys_min = {k: float(np.min(cl_phys[k])) for k in CK}
    norm_min = {k: phys_min[k] / s for k in CK}
    rel = {k: abs(norm_min[k] - vec[k]) / max(abs(vec[k]), 1e-300)
           for k in CK}
    return {'R_phys_m': R_phys,
            'normalised_max_rel_diff_vs_own_vector':
                float(max(rel.values())),
            'signs_match_own_vector': bool(all(
                (phys_min[k] > 0) == (vec[k] > 0) for k in CK))}


res['premise_audits'] = {
    sname: {
        'build_inputs_dimensionless': True,
        'any_physical_scale_input': False,
        'semiclassical_sector_in_total': False,
        'boundary': 'P226-2 B-prime sector is NOT a constituent of '
                    'this shadow total (posed classical jet sectors '
                    '+ director channel shifts, homogeneous in L); '
                    'a total carrying an intrinsic length would not '
                    'inherit the invariance. Physicalisation enters '
                    'only through L = R/0.8.'}
    for sname in SHADOW_VARIANT}

# =====================================================================
# (e) PRICES — tides, rescue (float64 + mpmath 50-digit), direct
#     rung, beta ceiling, E_shell (gate quadrature + mpmath check),
#     D-blindness; FD-Riemann second tide path
# =====================================================================
from scipy.integrate import simpson as sp_simpson  # noqa: E402
import mpmath as mp  # noqa: E402


def gate_shell_energy(ch_pre, Jp, R_phys, mpmath_director=False):
    L = R_phys / A_THROAT
    s = stress_factor(R_phys)
    M_arr = np.asarray(Jp['M'], float)
    A_arr = np.asarray(Jp['A'], float)
    base_integ = ch_pre['rho8'] * np.exp(M_arr) * A_arr**2 * np.sin(TH)
    i_base = float(sp_simpson(base_integ, x=TH))
    tf = np.linspace(0.02, np.pi - 0.02, 200001)
    c1f = (1.0 - np.cos(tf))**2 / (np.sin(tf)**2 * B.R00**2)
    dir_integ = (0.5 * KAP_PREMIUM * c1f * math.exp(float(M_arr[0]))
                 * float(A_arr[0])**2 * np.sin(tf))
    i_dir = float(sp_simpson(dir_integ, x=tf))
    out = {'i_base': i_base, 'i_director': i_dir,
           'E_J': float(L**3 * 2.0 * math.pi * s * (i_base + i_dir))}
    if mpmath_director:
        mp.mp.dps = 50
        M0 = mp.mpf(float(M_arr[0]))
        A0 = mp.mpf(float(A_arr[0]))
        kap = mp.mpf('0.254873')
        R00 = mp.mpf('0.8')

        def f(th):
            c1 = (1 - mp.cos(th))**2 / (mp.sin(th)**2 * R00**2)
            return (mp.mpf('0.5') * kap * c1 * mp.exp(M0) * A0**2
                    * mp.sin(th))
        i_dir_mp = mp.quad(f, [mp.mpf('0.02'), mp.mpf('1.5'),
                               mp.pi - mp.mpf('0.02')])
        out['i_director_mpmath50'] = float(i_dir_mp)
        out['i_director_mpmath_rel_diff'] = abs(
            float(i_dir_mp) - i_dir) / abs(i_dir)
    return out


def gate_beta_ceiling(comps, W_rad, R_phys):
    L = R_phys / A_THROAT
    conv = C_LIGHT**2 / L**2
    if W_rad * conv > BAR:
        return 0.0
    if float(np.max(np.abs(comps['R_tthtth']))) * conv > BAR:
        return 0.0
    grid = np.linspace(0.0, 0.99, 991)
    ok = np.ones_like(grid, dtype=bool)
    for i, b in enumerate(grid):
        comb = LT.lateral_combination(comps['R_tthtth'],
                                      comps['R_lthlth'], b)
        ok[i] = float(np.max(np.abs(comb))) * conv <= BAR
    if ok[-1]:
        return float(grid[-1])
    j = int(np.argmax(~ok)) if (~ok).any() else len(grid)
    return float(grid[j - 1]) if j > 0 else 0.0


# ---- the gate's FD-Riemann second tide path (P254-2 pattern)
_SUF_PAIRS = [('', 0, 0, 0), ('u', 1, 0, 0), ('h', 0, 1, 0),
              ('t', 0, 0, 1), ('uu', 2, 0, 0), ('uh', 1, 1, 0),
              ('ut', 1, 0, 1), ('hh', 0, 2, 0), ('ht', 0, 1, 1),
              ('tt', 0, 0, 2)]


def _profile_fns(J, th0):
    i = int(np.argmin(np.abs(TH - th0)))
    coef = {(b, sf): float(np.asarray(J[b + sf], float)[i])
            for b in 'FMAW' for sf, _, _, _ in _SUF_PAIRS}

    def X(b, t, rho, th):
        dth = th - th0
        v = 0.0
        for sf, pr, ph, pt in _SUF_PAIRS:
            v += (coef[(b, sf)] * rho**pr * dth**ph * t**pt
                  / (math.factorial(pr) * math.factorial(ph)
                     * math.factorial(pt)))
        return v
    return X


def _metric(X, t, rho, th):
    F = X('F', t, rho, th)
    M = X('M', t, rho, th)
    A = X('A', t, rho, th)
    W = X('W', t, rho, th)
    s2 = math.sin(th)**2
    g = np.zeros((4, 4))
    g[0, 0] = -math.exp(2 * F) + A * A * s2 * W * W
    g[0, 3] = g[3, 0] = -A * A * s2 * W
    g[1, 1] = math.exp(2 * M)
    g[2, 2] = A * A
    g[3, 3] = A * A * s2
    return g, F, M, A, W


def gate_fd_riemann(J, th0, h=2e-3):
    X = _profile_fns(J, th0)

    def met(dt, dr, dth):
        return _metric(X, dt, dr, th0 + dth)[0]
    g0, F0, M0, A0, W0 = _metric(X, 0.0, 0.0, th0)
    dg = np.zeros((4, 4, 4))
    d2 = np.zeros((4, 4, 4, 4))
    for k in range(3):
        pp = [0.0, 0.0, 0.0]
        pm = [0.0, 0.0, 0.0]
        pp[k] = h
        pm[k] = -h
        dg[:, :, k] = (met(*pp) - met(*pm)) / (2 * h)
    for k in range(3):
        for l in range(3):
            a1 = [0.0, 0.0, 0.0]
            a2 = [0.0, 0.0, 0.0]
            a3 = [0.0, 0.0, 0.0]
            a4 = [0.0, 0.0, 0.0]
            a1[k] += h
            a1[l] += h
            a2[k] += h
            a2[l] -= h
            a3[k] -= h
            a3[l] += h
            a4[k] -= h
            a4[l] -= h
            d2[:, :, k, l] = (met(*a1) - met(*a2) - met(*a3)
                              + met(*a4)) / (4 * h * h)
    ginv = np.linalg.inv(g0)
    Gam = np.zeros((4, 4, 4))
    dGam = np.zeros((4, 4, 4, 4))
    for up in range(4):
        for i in range(4):
            for j in range(4):
                Gam[up, i, j] = 0.5 * sum(
                    ginv[up, ss] * (dg[ss, i, j] + dg[ss, j, i]
                                    - dg[i, j, ss]) for ss in range(4))
    for up in range(4):
        for i in range(4):
            for j in range(4):
                for k in range(3):
                    dGam[up, i, j, k] = 0.5 * sum(
                        sum(-ginv[up, aa] * dg[aa, bb, k] * ginv[bb, ss]
                            for aa in range(4) for bb in range(4))
                        * (dg[ss, i, j] + dg[ss, j, i] - dg[i, j, ss])
                        + ginv[up, ss] * (d2[ss, i, j, k]
                                          + d2[ss, j, i, k]
                                          - d2[i, j, ss, k])
                        for ss in range(4))

    def Rcov(a, b, c, d):
        e = 0.0
        for ee in range(4):
            rr = dGam[ee, b, d, c] - dGam[ee, b, c, d]
            for mm in range(4):
                rr += (Gam[ee, c, mm] * Gam[mm, b, d]
                       - Gam[ee, d, mm] * Gam[mm, b, c])
            e += g0[a, ee] * rr
        return e
    eF = math.exp(-F0)
    eM = math.exp(-M0)
    return {
        'R_lthlth': eM**2 / A0**2 * Rcov(1, 2, 1, 2),
        'R_tthtth': eF**2 / A0**2 * (Rcov(0, 2, 0, 2)
                                     + 2 * W0 * Rcov(0, 2, 3, 2)
                                     + W0**2 * Rcov(3, 2, 3, 2)),
        'R_tltl': eF**2 * eM**2 * (Rcov(0, 1, 0, 1)
                                   + 2 * W0 * Rcov(0, 1, 3, 1)
                                   + W0**2 * Rcov(3, 1, 3, 1))}


CHARGE_PRICES = {
    'X_m': {'rescue_radius_m': 106756986.38,
            'E_shell_J': 1.6815079776e52},
    'H_0': {'rescue_radius_m': 106756983.66,
            'E_shell_J': 1.6815079348e52}}
prices = {}
for sname, vname in SHADOW_VARIANT.items():
    vr = var_reads[vname]
    Jp = vr['Jp']
    comps = LT.lateral_tide_from_jets(Jp, TH)
    W_rad, th_rad = worst_of(comps['R_tltl'])
    lat01 = np.abs(LT.lateral_combination(comps['R_tthtth'],
                                          comps['R_lthlth'], 0.1))
    i_lat = int(np.argmax(lat01))
    W_lat01 = float(lat01[i_lat])
    W_bind = max(W_rad, W_lat01)
    R_rescue = A_THROAT * C_LIGHT * math.sqrt(W_bind / BAR)
    mp.mp.dps = 50
    R_mp = float(mp.mpf('0.8') * 299792458
                 * mp.sqrt(mp.mpf(W_bind) / mp.mpf('4.905')))
    L_r = R_rescue / A_THROAT
    conv_r = C_LIGHT**2 / L_r**2
    bc = gate_beta_ceiling(comps, W_rad, R_rescue)
    e_rescue = gate_shell_energy(vr['ch_pre'], Jp, R_rescue,
                                 mpmath_director=True)
    e_charge = gate_shell_energy(vr['ch_pre'], Jp, 1.068e8)
    fd_rows = {}
    for th0 in (0.5, 1.0, math.pi / 2):
        fd = gate_fd_riemann(Jp, th0)
        i0 = int(np.argmin(np.abs(TH - th0)))
        for comp in ('R_tltl', 'R_tthtth', 'R_lthlth'):
            sym = float(comps[comp][i0])
            fd_rows[f'{comp}@th{th0:.2f}'] = {
                'fd': fd[comp], 'symbolic': sym,
                'rel_diff': abs(fd[comp] - sym)
                / max(abs(sym), 1e-12)}
    prices[sname] = {
        'R_tltl_worst_abs_pose^-2': W_rad,
        'R_tltl_worst_theta': th_rad,
        'R_tltl_signed_at_0.02': float(comps['R_tltl'][0]),
        'R_tltl_signed_at_pi/2': float(comps['R_tltl'][I_STAR]),
        'lateral_beta0.1_worst_pose^-2': W_lat01,
        'lateral_beta0.1_worst_theta': float(TH[i_lat]),
        'rescue_radius_m_float64': R_rescue,
        'rescue_radius_m_mpmath50': R_mp,
        'rescue_mpmath_abs_diff_m': abs(R_mp - R_rescue),
        'binding_component': ('radial R_tltl' if W_rad >= W_lat01
                              else 'lateral combination (beta=0.1)'),
        'rescue_abs_diff_vs_charge_m':
            abs(R_rescue - CHARGE_PRICES[sname]['rescue_radius_m']),
        'direct_rung_at_rescue': {
            'radial_bar_ratio': W_rad * conv_r / BAR,
            'lateral_beta0.1_bar_ratio': W_lat01 * conv_r / BAR,
            'beta_ceiling': bc},
        'E_shell_at_rescue': e_rescue,
        'E_shell_at_rescue_rel_diff_vs_charge':
            abs(e_rescue['E_J'] - CHARGE_PRICES[sname]['E_shell_J'])
            / CHARGE_PRICES[sname]['E_shell_J'],
        'E_shell_at_charge_radius_J': e_charge['E_J'],
        'E_over_R_rel_spread': abs(
            e_rescue['E_J'] / R_rescue - e_charge['E_J'] / 1.068e8)
            / float(np.mean([e_rescue['E_J'] / R_rescue,
                             e_charge['E_J'] / 1.068e8])),
        'fd_riemann_second_path': fd_rows,
        'fd_riemann_worst_rel_diff':
            max(r['rel_diff'] for r in fd_rows.values())}
    # (d) computed invariance at the rescue rung and 2.5e8 m
    prices[sname]['legality_at_scale'] = {
        'at_rescue_radius': legality_at_radius(
            vr['ch_tot'], vr['minima'], R_rescue),
        'at_2.5e8_m': legality_at_radius(
            vr['ch_tot'], vr['minima'], 2.5e8)}
    print('Prices', sname, '| rescue:', R_rescue,
          '| E_shell:', e_rescue['E_J'],
          '| FD worst rel:', prices[sname]['fd_riemann_worst_rel_diff'],
          flush=True)
res['prices'] = prices

# ---- D-blindness cross-check at R = 1.068e8 m (datum + shadows)
blind = {}
for label, vname in (('datum_H_utilde_true', 'H_utilde_true'),
                     ('X_m', 'X_mtt_field'), ('H_0', 'H_0')):
    vr = var_reads[vname]
    blind[label] = gate_shell_energy(vr['ch_pre'], vr['Jp'],
                                     1.068e8)['E_J']
vals = list(blind.values())
blind['max_pairwise_rel_diff'] = (
    max(vals) - min(vals)) / float(np.mean(vals))
blind['charge_value_J'] = 1.6821854766e52
blind['max_rel_diff_vs_charge'] = max(
    abs(v - 1.6821854766e52) / 1.6821854766e52 for v in vals)
res['D_blindness_crosscheck'] = blind
print('D-blindness:', blind, flush=True)

# =====================================================================
# VERDICT MECHANICS (the textual ruling is the coordinator's,
# recorded in GATE61_REPORT.md; the mechanical legs are here)
# =====================================================================
pert_ok = True
for sname, entry in d_pert.items():
    for delta, row in entry.items():
        pert_ok &= (row['D_preserving_max_change_channels_pth8_pph8']
                    <= 1e-13
                    and row['D_preserving_max_change_R_tltl'] <= 1e-13
                    and row['D_changing_max_change_channels_pth8_pph8']
                    >= 1e-3
                    and row['D_changing_max_change_R_tltl'] >= 1e-3)
inv_ok = True
for sname in SHADOW_VARIANT:
    for rung in ('at_rescue_radius', 'at_2.5e8_m'):
        r = prices[sname]['legality_at_scale'][rung]
        inv_ok &= (r['normalised_max_rel_diff_vs_own_vector'] <= 1e-13
                   and r['signs_match_own_vector'])
price_ok = True
for sname in SHADOW_VARIANT:
    p = prices[sname]
    price_ok &= (p['rescue_abs_diff_vs_charge_m'] <= 0.01
                 and p['binding_component'] == 'radial R_tltl'
                 and abs(p['direct_rung_at_rescue']
                         ['lateral_beta0.1_bar_ratio'] - 0.9733) <= 1e-3
                 and abs(p['direct_rung_at_rescue']['beta_ceiling']
                         - 0.194) <= 0.001
                 and p['E_shell_at_rescue_rel_diff_vs_charge'] <= 1.2e-8
                 and p['E_shell_at_rescue']
                 ['i_director_mpmath_rel_diff'] <= 1.2e-8
                 and p['rescue_mpmath_abs_diff_m'] <= 1e-6
                 and p['fd_riemann_worst_rel_diff'] <= 2e-2)
mech = {
    'controls_all_pass': bool(all(
        res['controls'][k]['pass'] for k in res['controls'])),
    'identity_G1_holds': bool(g1['holds']),
    'identity_G2_holds': bool(g2['holds']),
    'identity_G3_holds': bool(g3['holds']),
    'shadow_vectors_at_0.0_and_positive': bool(all(
        shadow_vec[s]['max_abs_diff_vs_charge'] == 0.0
        and shadow_vec[s]['all_seven_strictly_positive']
        for s in SHADOW_VARIANT)),
    'D_identity_perturbation_ok': bool(pert_ok),
    'D_identity_symbolic_ok': bool(sym_ok),
    'scale_invariance_ok': bool(inv_ok),
    'prices_ok': bool(price_ok),
    'D_blindness_ok': bool(blind['max_pairwise_rel_diff'] <= 1.2e-8
                           and blind['max_rel_diff_vs_charge']
                           <= 1.2e-8)}
mech['all_mechanical_legs_hold'] = bool(all(mech.values()))
res['verdict_mechanics'] = mech
res['gate_verdict'] = ('PASS' if mech['all_mechanical_legs_hold']
                       else 'NOT PASS — see GATE61_REPORT.md')
res['elapsed_s'] = time.time() - T0
json.dump(res, open(f'{ROOT}/gate61/results/g61_results.json', 'w'),
          indent=1, default=float)
print('MECHANICS:', json.dumps(mech, indent=1), flush=True)
print('GATE VERDICT (mechanical):', res['gate_verdict'],
      '| elapsed_s:', res['elapsed_s'], flush=True)
