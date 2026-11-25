"""
p803_verify.py — P80-3 stage 3: independent second paths + DEC ladder
for a composed row (argv: row name; default = best passing row in
p803_composed.json, else the highest-payload audited row).
Second paths (discretisation different in kind from the primary
gate-standard 2nd-order auditor):
  A) wa_diag 4th-order direct-d2 Einstein (einstein4) margins +
     sampled-null, same point set, h=0.3/0.15;
  B) Phase-1 judge (verify_metric, nested-Gamma) summarise, h=0.15.
DEC ladder: p523 focused + stencil-clear point sets at
h in {0.15, 0.075, 0.0375}, gate-standard auditor.
Output: results/p803_verify_<row>.json. float64, venv python.
"""
import json, os, sys, time
import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase80')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase52')
import p803_lib as P
sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate6')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase41')
import wa_auditor as wa
import wa_diag as wd
import verify_metric as vm
from p413_audit import build_composed, audit_points, region_of, summarise as p1_summarise
import p523_lib as G

RES = '/home/hatch/workspace/warp-pilot/phase80/results'
KINDS = ('nec', 'wec', 'sec', 'dec')


def row_passes(audit):
    for h in ('0.3', '0.15'):
        a = audit[h]
        if a['typeI_frac_sig'] != 1.0 or a['worst'] is None or a['worst'] <= 0:
            return False
        if a['min_sampled_nec_all_sig'] is None or a['min_sampled_nec_all_sig'] <= 0:
            return False
        for e in a['regions'].values():
            if e['worst'] is None or e['worst'] <= 0 or e['typeI_frac'] != 1.0:
                return False
    return True


def margins4(gfunc, pts, h):
    G4, g = wd.einstein4(gfunc, pts, h)
    That = wa.eulerian_that(g, G4 / wa.EIGHT_PI)
    m = wa.margins_from_that(That)
    m['sampled_nec'] = wa.sampled_nec_min(That)
    sig, rho_peak, thr = P._sig_mask(That)
    ti = m['typeI']
    out = {'h': h, 'auditor': 'wa_diag_4th_order', 'n_sig': int(np.sum(sig)),
           'typeI_frac_sig': float(np.mean(ti[sig])) if np.any(sig) else None,
           'n_sig_non_typeI': int(np.sum(sig & ~ti))}
    for k in KINDS:
        v = m[k][sig & ti]
        v = v[~np.isnan(v)]
        out['min_' + k] = float(np.min(v)) if v.size else None
    vals = [out['min_' + k] for k in KINDS if out['min_' + k] is not None]
    out['worst'] = float(min(vals)) if vals else None
    sn = m['sampled_nec'][sig]
    out['min_sampled_nec_all_sig'] = float(np.nanmin(sn)) if sn.size else None
    rr = np.sqrt(np.sum(pts ** 2, axis=1))
    regs = {}
    comp_r = {'R1i': 2.0, 'R2i': 4.0, 'R1o': 5.0, 'R2o': 10.0}
    for reg in ('payload', 'inner_wall', 'cavity', 'outer_wall', 'exterior'):
        sel = sig & np.array([region_of(x, comp_r) == reg for x in rr])
        if np.any(sel):
            tisel = sel & ti
            e = {'n_sig': int(np.sum(sel)), 'typeI_frac': float(np.mean(ti[sel]))}
            for k in KINDS:
                v = m[k][tisel]
                v = v[~np.isnan(v)]
                e['min_' + k] = float(np.min(v)) if v.size else None
            vv = [e['min_' + k] for k in KINDS if e['min_' + k] is not None]
            e['worst'] = float(min(vv)) if vv else None
            regs[reg] = e
    out['regions'] = regs
    return out


def main():
    t0 = time.time()
    comp_data = json.load(open(RES + '/p803_composed.json'))
    econ = json.load(open(RES + '/p803_economics.json'))
    rows = comp_data['rows']
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        passing = [n for n, r in rows.items() if row_passes(r['audit'])]
        pool = passing if passing else list(rows)
        name = max(pool, key=lambda n: econ['rows'][n]['anatomy']['payload_relat'])
    erow = econ['rows'][name]
    x_o = np.array(erow['x_outer']); x_i = np.array(erow['x_inner'])
    beta_o, beta_i, anat, _ = P.held_betas(P.frontier_outer(), P.frontier_inner(),
                                           erow['beta_o_alone'], erow['beta_i_alone'])
    prof_o, prof_i = P.frontier_outer(), P.frontier_inner()
    comp = build_composed(prof_o, prof_i, beta_o, beta_i)
    gf = P.composed_gfunc_src(comp, prof_o, prof_i, x_o, x_i)
    pts, _ = audit_points(prof_o['R2'], seed=11)
    out = {'row': name, 'payload_relat': anat['payload_relat'],
           'W_payload_sum': anat['W_payload_sum'],
           'beta_o_comp': beta_o, 'beta_i_comp': beta_i,
           'primary_passes': row_passes(rows[name]['audit'])}
    out['second_path_4th'] = {str(h): margins4(gf, pts, h) for h in (0.3, 0.15)}
    print('4th-order done', time.time() - t0, flush=True)
    out['second_path_phase1'] = p1_summarise(
        gf, pts, 0.15, region_fn=lambda r: region_of(r, comp))
    print('phase1 done', time.time() - t0, flush=True)
    # DEC ladder on focused + stencil-clear sets
    fpts, _ = G.focused_points(comp)
    spts, _ = G.stencil_clear_points(comp)
    out['dec_ladder'] = {}
    for tag, pp in (('focused', fpts), ('stencil_clear', spts)):
        out['dec_ladder'][tag] = {}
        for h in (0.15, 0.075, 0.0375):
            s = P.summarise_gs(gf, pp, h)
            out['dec_ladder'][tag][str(h)] = {
                'worst': s['worst'], 'worst_kind': s['worst_kind'],
                'min_dec': s['min_dec'], 'typeI_frac_sig': s['typeI_frac_sig'],
                'min_sampled_nec_all_sig': s['min_sampled_nec_all_sig'],
                'n_sig': s['n_sig']}
        print(f'ladder {tag} done', time.time() - t0, flush=True)
    out['elapsed_s'] = time.time() - t0
    json.dump(out, open(RES + f'/p803_verify_{name}.json', 'w'), indent=1)
    print(json.dumps({k: out[k] for k in ('row', 'payload_relat', 'primary_passes')}, indent=1))
    print('4th h0.15 worst', out['second_path_4th']['0.15']['worst'],
          'typeI', out['second_path_4th']['0.15']['typeI_frac_sig'])
    print('phase1 h0.15 worst', out['second_path_phase1']['worst'],
          'typeI', out['second_path_phase1']['typeI_frac_sig'])
    print(f'DONE -> p803_verify_{name}.json', flush=True)


if __name__ == '__main__':
    main()
