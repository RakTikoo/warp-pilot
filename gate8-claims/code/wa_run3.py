"""W-A run 3: head-to-head at the two deciding sites (my o4 vs phase judge,
same points), radial DEC profile at the caveat site, finer ladder."""
import json, sys
import numpy as np
sys.path.insert(0,'/home/hatch/workspace/warp-pilot')
sys.path.insert(0,'/home/hatch/workspace/warp-pilot/phase41')
sys.path.insert(0,'/home/hatch/workspace/warp-pilot/gate8')
import shell as sh
import verify_metric as vm
from p413_audit import build_composed, composed_gfunc, audit_points, region_of, fib_dirs
from wa_lib import audit

po = sh.build_shell(5.0,10.0,1.9125,kind='edgepeaked',params={'wd':1.0,'floor':0.1},s_rho=1.0,s_P=0.58,Nr=4001)
pi = sh.build_shell(2.0,4.0,0.765,kind='edgepeaked',params={'wd':0.4,'floor':0.1},s_rho=0.4,s_P=0.232,Nr=4001)
comp0 = build_composed(po,pi,0.0,0.0)
bi = float(0.05*np.exp(float(np.interp(3.0,comp0['r'],comp0['a']))-float(np.interp(3.0,pi['r'],pi['a']))))
comp08 = build_composed(po,pi,0.08-bi,bi); gf08 = composed_gfunc(comp08)
comp10 = build_composed(po,pi,0.10-bi,bi); gf10 = composed_gfunc(comp10)
out={}

site = np.array([[-2.2447767326898695,-2.3868540162587233,-3.5076923076923086]])
# judge ladder at caveat site
jl={}
for h in (0.15,0.075,0.0375,0.01875):
    G,That,m = vm.einstein_at_points(gf08, site, h=h)
    jl[str(h)]={'dec':float(m['dec'][0]),'nec':float(m['nec'][0]),'typeI':bool(m['typeI'][0])}
    print('judge site',h,jl[str(h)],flush=True)
out['judge_caveat_site']=jl
# my o4 finer ladder
ml={}
for h in (0.075,0.0375,0.01875,0.009375):
    That,m = audit(gf08, site, h, 4)
    ml[str(h)]={'dec':float(m['dec'][0]),'nec':float(m['nec'][0]),'rho':float(m['rho'][0]),'p':m['p'][0].tolist()}
    print('mine site',h,ml[str(h)],flush=True)
out['mine_caveat_site_fine']=ml
# radial profile along site direction, my o4 h=0.01875 and judge h=0.075
d = site[0]/np.linalg.norm(site[0])
prof={}
for rr in (4.4,4.6,4.7,4.8,4.9,4.95):
    p = (d*rr)[None,:]
    That,m = audit(gf08, p, 0.01875, 4)
    G,Thatj,mj = vm.einstein_at_points(gf08, p, h=0.075)
    prof[str(rr)]={'mine_dec':float(m['dec'][0]),'mine_rho':float(m['rho'][0]),
                   'judge_dec_h0.075':float(mj['dec'][0]),'judge_rho':float(mj['rho_eig'][0])}
    print('prof',rr,prof[str(rr)],flush=True)
out['radial_profile']=prof

# 0.0998 main bed head-to-head o4 vs judge h=0.15
pts,_ = audit_points(10.0, seed=11)
rr_m = np.sqrt(np.sum(pts**2,axis=1))
def regions(gf, use_judge, h):
    if use_judge:
        G,That,m = vm.einstein_at_points(gf, pts, h=h)
    else:
        That,m = audit(gf, pts, h, 4)
    scale=np.max(np.abs(That),axis=(1,2)); thr=max(1e-11,1e-3*abs(float(np.max(That[:,0,0]))))
    sig=scale>thr; res={}
    for reg in ('payload','inner_wall','cavity','outer_wall','exterior'):
        sel=sig & np.array([region_of(x,comp10)==reg for x in rr_m])
        res[reg]={'worst':float(np.nanmin([np.nanmin(m[k][sel]) for k in ('nec','wec','sec','dec')])),
                  'sec_min':float(np.nanmin(m['sec'][sel])),'typeI':float(np.mean(m['typeI'][sel]))}
    return res
out['row00998_mainbed_h0.15_mine'] = regions(gf10, False, 0.15)
out['row00998_mainbed_h0.15_judge'] = regions(gf10, True, 0.15)
print('mine 0998', out['row00998_mainbed_h0.15_mine'], flush=True)
print('judge 0998', out['row00998_mainbed_h0.15_judge'], flush=True)
json.dump(out, open('/home/hatch/workspace/warp-pilot/gate8/results/wa_run3.json','w'), indent=1)
print('DONE',flush=True)
