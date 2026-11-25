"""
p803_compose.py — P80-3 stage 2: composed source-modulated rows.
ORDER OF OPERATIONS (registered economics discipline): the held-W
payload sum of EVERY candidate row is computed and written to
results/p803_economics.json BEFORE any composed legality read.
Then composed gate-standard audits (h=0.3/0.15, regions, conservation)
for rows whose shells are both alone-legal at their alone betas,
in descending payload order. Candidate passes get the DEC ladder +
second paths in p803_verify.py.
float64, venv python. Resumable via results/p803_composed.json.
"""
import json, os, sys, time
import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase80')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase52')
import p803_lib as P
sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate6')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase41')
from p413_audit import build_composed, composed_gfunc, audit_points, region_of
import p523_lib as G

RES = '/home/hatch/workspace/warp-pilot/phase80/results'
STATE = RES + '/p803_alone_state.json'
ECON = RES + '/p803_economics.json'
OUT = RES + '/p803_composed.json'
BETAS = [0.05, 0.06, 0.07, 0.08]


def load(path, default):
    if os.path.exists(path):
        try:
            return json.load(open(path))
        except Exception:
            pass
    return default


def save(obj, path):
    json.dump(obj, open(path, 'w'), indent=1)


def alone_legal(rec):
    """Alone legality, gate standard, with the programme's artefact
    pattern made explicit (P46-2/P52-3): Type-I 1.000 at h=0.3/0.15;
    payload + wall regions' worst > 0 at h=0.3 AND 0.15 with
    sampled-null > 0 there; the exterior (smoothed density tail)
    must be > 0 at h=0.15, OR negative only at h=0.3/0.15 with the
    h=0.075 ladder rung positive (the demonstrated stencil-artefact
    signature: magnitude shrinking with h, sign flipping)."""
    if 'audit' not in rec:
        return False
    for h in ('0.3', '0.15'):
        a = rec['audit'][h]
        for reg in ('payload', 'inner_wall'):
            e = a['regions'].get(reg)
            if e is None or e['worst'] is None or e['worst'] <= 0:
                return False
            if e['typeI_frac'] != 1.0:
                return False
            if e['min_sampled_nec_all'] is None or e['min_sampled_nec_all'] <= 0:
                return False
    # exterior: clean at h=0.15, or the switch/fringe artefact
    # signature (P50-1 pattern): failures confined to the exterior,
    # worst magnitude strictly shrinking across h = 0.3/0.15/0.075,
    # Type-I 1.000 at h=0.075, and the h=0.075 exterior worst within
    # 3e-5 of zero (its Richardson limit is then positive; the
    # deciding composed row's fringe ladder to h=0.0375 is run in
    # p803_verify.py before any verdict rests on such a shell).
    ext15 = rec['audit']['0.15']['regions']['exterior']
    if ext15['worst'] is not None and ext15['worst'] > 0 and ext15['typeI_frac'] == 1.0:
        return True
    a075 = rec['audit'].get('0.075')
    if not a075:
        return False
    e03 = rec['audit']['0.3']['regions']['exterior']
    e075 = a075['regions'].get('exterior')
    if e075 is None or e075['typeI_frac'] != 1.0 or e075['worst'] is None:
        return False
    w03, w15, w075 = e03['worst'], ext15['worst'], e075['worst']
    if None in (w03, w15, w075):
        return False
    if w075 > 0:
        return True  # ladder rung clean: the artefact has flipped away
    return abs(w075) < abs(w15) < abs(w03) and w075 > -3e-5


def main():
    t0 = time.time()
    state = json.load(open(STATE))
    prof_o, prof_i = P.frontier_outer(), P.frontier_inner()

    # ---------- ECONOMICS FIRST (no legality read above this line) ----
    econ = {'item': 'P80-3 economics (held-W payload sums, stated BEFORE '
                     'any composed legality read)',
            'rows': {}}
    xs = {}
    for bo in BETAS:
        for bi in BETAS:
            ro = state['shells']['outer'].get(f'b{bo}')
            ri = state['shells']['inner'].get(f'b{bi}')
            if not ro or not ri:
                continue
            if 'x' not in ro or 'x' not in ri:
                continue
            beta_o, beta_i, anat, _ = P.held_betas(prof_o, prof_i, bo, bi)
            name = f'o{bo}_i{bi}'
            econ['rows'][name] = {
                'beta_o_alone': bo, 'beta_i_alone': bi,
                'anatomy': anat,
                'alone_legal_outer': alone_legal(ro),
                'alone_legal_inner': alone_legal(ri),
                'x_outer': ro['x'], 'x_inner': ri['x'],
            }
            xs[name] = (np.array(ro['x']), np.array(ri['x']),
                        beta_o, beta_i)
    save(econ, ECON)
    print('ECONOMICS written:', {k: round(v['anatomy']['payload_relat'], 5)
                                 for k, v in econ['rows'].items()}, flush=True)

    out = load(OUT, {'item': 'P80-3 composed', 'float': 'float64', 'rows': {}})

    # ---------- machinery gate: cosine P46-2 0.0799 row, gate-standard --
    if 'cosine_control' not in out:
        comp0 = build_composed(prof_o, prof_i, 0.0, 0.0)
        rmi = 0.5 * (prof_i['R1'] + prof_i['R2'])
        ac = float(np.interp(rmi, comp0['r'], comp0['a']))
        aa = float(np.interp(rmi, prof_i['r'], prof_i['a']))
        bi_c = float(0.05 * np.exp(ac - aa))
        bo_c = float(0.08 - bi_c)
        comp = build_composed(prof_o, prof_i, bo_c, bi_c)
        gf = composed_gfunc(comp)
        pts, _ = audit_points(prof_o['R2'], seed=11)
        out['cosine_control'] = {
            'note': 'P46-2 verdict row (payload coord 0.08, relat 0.0799), '
                    'single inner re-equilibration, cosine windows, read '
                    'with the GATE-STANDARD auditor (P46-2 record used the '
                    'Phase-1 judge: inner +9.79e-04, outer +4.05e-05, '
                    'payload +1.09e-04 at h=0.15)',
            'beta_o': bo_c, 'beta_i': bi_c,
            'payload_relat': float((bo_c + bi_c) / (1 + bo_c * bi_c)),
            'audit': {str(h): P.summarise_gs(gf, pts, h,
                                             region_fn=lambda r: region_of(r, comp))
                      for h in (0.3, 0.15)},
        }
        save(out, OUT)
        a = out['cosine_control']['audit']['0.15']
        print('cosine control h0.15 worst', a['worst'], 'regions',
              {k: v['worst'] for k, v in a['regions'].items()}, flush=True)

    # ---------- composed audits, descending payload, alone-legal only --
    order = sorted(econ['rows'].items(),
                   key=lambda kv: -kv[1]['anatomy']['payload_relat'])
    for name, erow in order:
        if not (erow['alone_legal_outer'] and erow['alone_legal_inner']):
            continue
        if name in out['rows'] and 'audit' in out['rows'][name]:
            continue
        x_o, x_i, beta_o, beta_i = xs[name]
        comp = build_composed(prof_o, prof_i, beta_o, beta_i)
        gf = P.composed_gfunc_src(comp, prof_o, prof_i, x_o, x_i)
        pts, _ = audit_points(prof_o['R2'], seed=11)
        row = {'anatomy': erow['anatomy'], 'audit': {}}
        for h in (0.3, 0.15):
            row['audit'][str(h)] = P.summarise_gs(
                gf, pts, h, region_fn=lambda r: region_of(r, comp))
        rr = np.sqrt(np.sum(pts ** 2, axis=1))
        wsel = np.array([region_of(x, comp) in ('inner_wall', 'outer_wall')
                         for x in rr])
        wpts = pts[wsel][::max(1, int(np.sum(wsel)) // 28)][:28]
        row['conservation'] = G.divergence_read_gs(gf, wpts)
        row['chains'] = [{k: c[k] for k in ('lam', 'k', 'S_lo_minus1', 'S_hi',
                                            'balance_rel', 'monotone_violation')}
                         for c in gf.chains]
        out['rows'][name] = row
        save(out, OUT)
        a = row['audit']['0.15']
        print(f'{name} payload={erow["anatomy"]["payload_relat"]:.5f} '
              f'h0.15 worst={a["worst"]:+.3e} typeI={a["typeI_frac_sig"]} '
              f'regions={ {k: (round(v["worst"], 9) if v["worst"] is not None else None) for k, v in a["regions"].items()} } '
              f'cons={row["conservation"]["rel_med"]:.4f} '
              f'({time.time()-t0:.0f}s)', flush=True)
    out['elapsed_s'] = time.time() - t0
    save(out, OUT)
    print(f'DONE {out["elapsed_s"]:.0f}s -> {OUT}', flush=True)


if __name__ == '__main__':
    main()
