"""W-A run 1: anchors (Minkowski, Finalist-A calibration) + verdict row 0.0799
full volume, my direct-d2 machinery, order=2 primary, order=4 cross-check."""
import json, sys, time
import numpy as np
sys.path.insert(0,'/home/hatch/workspace/warp-pilot')
sys.path.insert(0,'/home/hatch/workspace/warp-pilot/phase41')
sys.path.insert(0,'/home/hatch/workspace/warp-pilot/gate8')
import shell as sh
from p413_audit import build_composed, composed_gfunc, audit_points, region_of, flat_gfunc
from wa_lib import audit, einstein_direct
import verify_metric as vm  # ONLY for the flat-control comparison + locating phase site; not deciding machinery

out = {}
t0=time.time()
# ---- Anchor 1: Minkowski exact zero (my path)
rng = np.random.default_rng(7)
fpts = rng.normal(size=(120,3))*6.0
for h in (0.3,0.15):
    for order in (2,4):
        G,g = einstein_direct(flat_gfunc, fpts, h, order)
        out[f'minkowski_h{h}_o{order}'] = float(np.max(np.abs(G))/(8*np.pi))
print('minkowski', {k:v for k,v in out.items()}, flush=True)

def summarise_mine(gf, pts, h, order, comp):
    That, m = audit(gf, pts, h, order)
    scale = np.max(np.abs(That),axis=(1,2))
    thr = max(1e-11, 1e-3*abs(float(np.max(That[:,0,0]))))
    sig = scale > thr
    rr = np.sqrt(np.sum(pts**2,axis=1))
    res = {'h':h,'order':order,'n_sig':int(sig.sum()),
           'worst':float(np.nanmin([np.nanmin(m[k][sig]) for k in ('nec','wec','sec','dec')])),
           'typeI_frac_sig':float(np.mean(m['typeI'][sig])), 'regions':{}}
    for reg in ('payload','inner_wall','cavity','outer_wall','exterior'):
        sel = sig & np.array([region_of(x,comp)==reg for x in rr])
        if sel.sum():
            vals = {k: float(np.nanmin(m[k][sel])) for k in ('nec','wec','sec','dec')}
            res['regions'][reg] = {'worst':min(vals.values()), 'mins':vals,
                'typeI':float(np.mean(m['typeI'][sel])),
                'worst_r':float(rr[sel][np.nanargmin(np.minimum.reduce([m[k][sel] for k in ('nec','wec','sec','dec')]))])}
    return res

def build(cls, payload):
    if cls=='frontier':
        po = sh.build_shell(5.0,10.0,1.9125,kind='edgepeaked',params={'wd':1.0,'floor':0.1},s_rho=1.0,s_P=0.58,Nr=4001)
        pi = sh.build_shell(2.0,4.0,0.765,kind='edgepeaked',params={'wd':0.4,'floor':0.1},s_rho=0.4,s_P=0.232,Nr=4001)
        bia=0.05
    else:
        po = sh.build_shell(10.0,20.0,2.0,kind='edgepeaked',params={'wd':3.0,'floor':0.2},s_rho=2.0,s_P=1.16,Nr=4001)
        pi = sh.build_shell(4.0,8.0,0.8,kind='edgepeaked',params={'wd':1.2,'floor':0.2},s_rho=0.8,s_P=0.464,Nr=4001)
        bia=0.02
    comp0 = build_composed(po,pi,0.0,0.0)
    rmid = 0.5*(pi['R1']+pi['R2'])
    ac = float(np.interp(rmid, comp0['r'], comp0['a'])); aa = float(np.interp(rmid, pi['r'], pi['a']))
    bi = float(bia*np.exp(ac-aa)); bo = float(payload-bi)
    comp = build_composed(po,pi,bo,bi)
    anat = {'a_comp_mid_i':ac,'a_alone_mid_i':aa,'ratio':float(np.exp(ac-aa)),
            'W':float(bi*np.exp(-ac)),'W_alone':float(bia*np.exp(-aa)),'beta_i':bi,'beta_o':bo}
    return comp, composed_gfunc(comp), anat

# ---- Anchor 2: Finalist-A calibration, payload 0.04
comp, gf, anat = build('finalistA', 0.04)
print('cal anatomy', anat, flush=True)
out['cal_anatomy']=anat
pts,_ = audit_points(20.0, seed=11)
for h in (0.3,0.15):
    out[f'cal_h{h}'] = summarise_mine(gf, pts, h, 2, comp)
    print('cal', h, out[f'cal_h{h}']['worst'], out[f'cal_h{h}']['typeI_frac_sig'], flush=True)

# ---- Verdict row: frontier payload 0.08 (relat 0.0799)
comp, gf, anat = build('frontier', 0.08)
print('verdict anatomy', anat, flush=True)
out['verdict_anatomy']=anat
pts,_ = audit_points(10.0, seed=11)
for h in (0.3,0.15):
    out[f'verdict_h{h}_o2'] = summarise_mine(gf, pts, h, 2, comp)
    print('verdict o2', h, out[f'verdict_h{h}_o2']['worst'], {k:round(v['worst'],8) for k,v in out[f'verdict_h{h}_o2']['regions'].items()}, flush=True)
out['verdict_h0.15_o4'] = summarise_mine(gf, pts, 0.15, 4, comp)
print('verdict o4 h0.15', out['verdict_h0.15_o4']['worst'], {k:round(v['worst'],8) for k,v in out['verdict_h0.15_o4']['regions'].items()}, flush=True)
out['elapsed']=time.time()-t0
json.dump(out, open('/home/hatch/workspace/warp-pilot/gate8/results/wa_run1.json','w'), indent=1)
print('DONE', out['elapsed'], flush=True)
