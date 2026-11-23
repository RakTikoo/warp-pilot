"""W-A run 2: caveat settlement ladder + instrument claims + boundaries."""
import json, sys, time
import numpy as np
sys.path.insert(0,'/home/hatch/workspace/warp-pilot')
sys.path.insert(0,'/home/hatch/workspace/warp-pilot/phase41')
sys.path.insert(0,'/home/hatch/workspace/warp-pilot/gate8')
import shell as sh
from p413_audit import build_composed, composed_gfunc, audit_points, region_of, fib_dirs
from wa_lib import audit

out={}; t0=time.time()
po = sh.build_shell(5.0,10.0,1.9125,kind='edgepeaked',params={'wd':1.0,'floor':0.1},s_rho=1.0,s_P=0.58,Nr=4001)
pi = sh.build_shell(2.0,4.0,0.765,kind='edgepeaked',params={'wd':0.4,'floor':0.1},s_rho=0.4,s_P=0.232,Nr=4001)
comp0 = build_composed(po,pi,0.0,0.0)
bi = float(0.05*np.exp(float(np.interp(3.0,comp0['r'],comp0['a']))-float(np.interp(3.0,pi['r'],pi['a']))))
bo_dual = float(0.05*np.exp(float(np.interp(7.5,comp0['r'],comp0['a']))-float(np.interp(7.5,po['r'],po['a']))))
def gf_for(payload_coord):
    comp = build_composed(po,pi,payload_coord-bi,bi); return comp, composed_gfunc(comp)

comp08, gf08 = gf_for(0.08)
dirs = fib_dirs(26,23)
radii = np.linspace(0.8,5.4,24)
pts_pc = np.concatenate([dirs*rr for rr in radii])
rr_pc = np.sqrt(np.sum(pts_pc**2,axis=1))

def dec_scan(gf, pts, h, order):
    That,m = audit(gf, pts, h, order)
    scale = np.max(np.abs(That),axis=(1,2))
    thr = max(1e-11, 1e-3*abs(float(np.max(That[:,0,0]))))
    return m, scale>thr

# --- 1. Locate the caveat site on MY machinery (o4, h=0.075, focused set)
m, sig = dec_scan(gf08, pts_pc, 0.075, 4)
cav = sig & (rr_pc>4.0) & (rr_pc<5.0)
i_worst = np.where(cav)[0][np.nanargmin(m['dec'][cav])]
site = pts_pc[i_worst]
out['caveat_site'] = {'point':site.tolist(),'r':float(rr_pc[i_worst]),
    'dec_o4_h0.075':float(m['dec'][i_worst]),'typeI':bool(m['typeI'][i_worst])}
print('site', out['caveat_site'], flush=True)

# --- 2. h-ladder at the FIXED site point, both discretisations
ladder={}
for order in (2,4):
    ladder[f'o{order}']={}
    for h in (0.15,0.075,0.0375,0.01875):
        That,mm = audit(gf08, site[None,:], h, order)
        ladder[f'o{order}'][str(h)] = {'dec':float(mm['dec'][0]),'nec':float(mm['nec'][0]),
            'sec':float(mm['sec'][0]),'typeI':bool(mm['typeI'][0])}
        print('ladder',order,h,ladder[f'o{order}'][str(h)], flush=True)
out['caveat_ladder_site']=ladder
# Richardson on o4 (assume 4th order) and o2 (2nd order)
for order,p in ((4,4),(2,2)):
    hs=[0.15,0.075,0.0375,0.01875]; vs=[ladder[f'o{order}'][str(h)]['dec'] for h in hs]
    rich=[]
    for a,b in zip(vs[:-1],vs[1:]):
        rich.append(b+(b-a)/(2**p-1))
    out[f'richardson_o{order}']={'dec_series':vs,'extrap_pairwise':rich}

# --- 3. Whole focused-set cavity DEC min per h (does the dip persist anywhere?)
scan={}
for order in (4,):
    scan[f'o{order}']={}
    for h in (0.15,0.075,0.0375):
        m,sig = dec_scan(gf08, pts_pc, h, order)
        cavm = sig & (rr_pc>4.0) & (rr_pc<5.0)
        clear = sig & (rr_pc<=4.6) & (rr_pc>=2.0)  # cavity stencil-clear band (region cavity is 4<r<5; use 4.0-4.6)
        clear = sig & (rr_pc>4.0) & (rr_pc<=4.6)
        scan[f'o{order}'][str(h)]={'cavity_dec_min':float(np.nanmin(m['dec'][cavm])),
            'cavity_dec_min_r':float(rr_pc[cavm][np.nanargmin(m['dec'][cavm])]),
            'cavity_clear_dec_min':float(np.nanmin(m['dec'][clear])) if clear.sum() else None,
            'payload_dec_min':float(np.nanmin(m['dec'][sig & (rr_pc<2.0)])),
            'payload_worst_all':float(np.nanmin([np.nanmin(m[k][sig & (rr_pc<2.0)]) for k in ('nec','wec','sec','dec')]))}
        print('scan',order,h,scan[f'o{order}'][str(h)], flush=True)
out['focused_scan']=scan

# --- 4. h=0.3 payload artefact site: payload-region worst on main bed, h ladder o4
pts_main,_ = audit_points(10.0, seed=11)
rr_m = np.sqrt(np.sum(pts_main**2,axis=1))
pay={}
for h in (0.3,0.15,0.075):
    That,mm = audit(gf08, pts_main, h, 4)
    scale=np.max(np.abs(That),axis=(1,2)); thr=max(1e-11,1e-3*abs(float(np.max(That[:,0,0]))))
    sel=(scale>thr)&(rr_m<2.0)
    pay[str(h)]={'payload_worst':float(np.nanmin([np.nanmin(mm[k][sel]) for k in ('nec','wec','sec','dec')])),
                 'payload_dec_min':float(np.nanmin(mm['dec'][sel]))}
    print('payload ladder',h,pay[str(h)], flush=True)
out['payload_h_ladder_o4']=pay

# --- 5. Boundary: 0.0998 outer-wall SEC, focused_ow set
comp10, gf10 = gf_for(0.10)
pts_ow = np.concatenate([dirs*rr for rr in np.linspace(4.8,10.8,24)])
rr_ow = np.sqrt(np.sum(pts_ow**2,axis=1))
ow={}
for h in (0.15,0.075):
    That,mm = audit(gf10, pts_ow, h, 4)
    scale=np.max(np.abs(That),axis=(1,2)); thr=max(1e-11,1e-3*abs(float(np.max(That[:,0,0]))))
    sel=(scale>thr)&(rr_ow>=5.0)&(rr_ow<=10.0)
    ow[str(h)]={'outer_sec_min':float(np.nanmin(mm['sec'][sel])),
        'outer_worst':float(np.nanmin([np.nanmin(mm[k][sel]) for k in ('nec','wec','sec','dec')])),
        'sec_worst_r':float(rr_ow[sel][np.nanargmin(mm['sec'][sel])]),
        'typeI_outer':float(np.mean(mm['typeI'][sel]))}
    print('ow',h,ow[str(h)], flush=True)
out['boundary_00998_focused_ow_o4']=ow

# --- 6. Follow-up row: beta_o capped 0.05 -> payload 0.0821, full volume o4 h=0.15
comp_cap = build_composed(po,pi,0.05,bi); gf_cap = composed_gfunc(comp_cap)
That,mm = audit(gf_cap, pts_main, 0.15, 4)
scale=np.max(np.abs(That),axis=(1,2)); thr=max(1e-11,1e-3*abs(float(np.max(That[:,0,0]))))
sig=scale>thr
regs={}
for reg in ('payload','inner_wall','cavity','outer_wall','exterior'):
    sel=sig & np.array([region_of(x,comp_cap)==reg for x in rr_m])
    regs[reg]={'worst':float(np.nanmin([np.nanmin(mm[k][sel]) for k in ('nec','wec','sec','dec')])),
               'typeI':float(np.mean(mm['typeI'][sel]))}
out['followup_capped0821_o4_h0.15']={'regions':regs,'typeI_frac_sig':float(np.mean(mm['typeI'][sig]))}
print('capped', out['followup_capped0821_o4_h0.15'], flush=True)

out['elapsed']=time.time()-t0
json.dump(out, open('/home/hatch/workspace/warp-pilot/gate8/results/wa_run2.json','w'), indent=1)
print('DONE', out['elapsed'], flush=True)
