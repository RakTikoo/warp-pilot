"""W-A run 4: resolve the 0.0998 outer-wall SEC disagreement at the judge's
worst point: both machineries, both orders, h ladder."""
import json, sys
import numpy as np
sys.path.insert(0,'/home/hatch/workspace/warp-pilot')
sys.path.insert(0,'/home/hatch/workspace/warp-pilot/phase41')
sys.path.insert(0,'/home/hatch/workspace/warp-pilot/gate8')
import shell as sh
import verify_metric as vm
from p413_audit import build_composed, composed_gfunc, audit_points, region_of
from wa_lib import audit

po = sh.build_shell(5.0,10.0,1.9125,kind='edgepeaked',params={'wd':1.0,'floor':0.1},s_rho=1.0,s_P=0.58,Nr=4001)
pi = sh.build_shell(2.0,4.0,0.765,kind='edgepeaked',params={'wd':0.4,'floor':0.1},s_rho=0.4,s_P=0.232,Nr=4001)
comp0 = build_composed(po,pi,0.0,0.0)
bi = float(0.05*np.exp(float(np.interp(3.0,comp0['r'],comp0['a']))-float(np.interp(3.0,pi['r'],pi['a']))))
comp10 = build_composed(po,pi,0.10-bi,bi); gf10 = composed_gfunc(comp10)
pts,_ = audit_points(10.0, seed=11)
rr = np.sqrt(np.sum(pts**2,axis=1))
G,That,m = vm.einstein_at_points(gf10, pts, h=0.15)
scale=np.max(np.abs(That),axis=(1,2)); thr=max(1e-11,1e-3*abs(float(np.max(That[:,0,0]))))
ow = np.where((scale>thr)&(rr>=5.0)&(rr<=10.0))[0]
iw = ow[np.argmin(m['sec'][ow])]
site = pts[iw]
out={'judge_worst_point':site.tolist(),'r':float(rr[iw]),'judge_sec_h0.15':float(m['sec'][iw])}
print('site',out,flush=True)
for h in (0.3,0.15,0.075,0.0375):
    G,That,m = vm.einstein_at_points(gf10, site[None,:], h=h)
    out[f'judge_h{h}']={'sec':float(m['sec'][0]),'nec':float(m['nec'][0]),'dec':float(m['dec'][0]),'typeI':bool(m['typeI'][0])}
    print('judge',h,out[f'judge_h{h}'],flush=True)
for order in (2,4):
    for h in (0.3,0.15,0.075,0.0375):
        That,mm = audit(gf10, site[None,:], h, order)
        out[f'mine_o{order}_h{h}']={'sec':float(mm['sec'][0]),'nec':float(mm['nec'][0]),'dec':float(mm['dec'][0]),'typeI':bool(mm['typeI'][0])}
        print('mine',order,h,out[f'mine_o{order}_h{h}'],flush=True)
# neighbourhood: 26 dirs at r=7.278049, mine o4 vs judge, h=0.15/0.075
from p413_audit import fib_dirs
dirs = fib_dirs(26,11)
shell_pts = dirs*7.278049
for h in (0.15,0.075):
    G,That,mj = vm.einstein_at_points(gf10, shell_pts, h=h)
    That,mm = audit(gf10, shell_pts, h, 4)
    out[f'shell_h{h}']={'judge_sec_min':float(np.nanmin(mj['sec'])),'mine_sec_min':float(np.nanmin(mm['sec'])),
                        'judge_worst':float(np.nanmin([np.nanmin(mj[k]) for k in ('nec','wec','sec','dec')])),
                        'mine_worst':float(np.nanmin([np.nanmin(mm[k]) for k in ('nec','wec','sec','dec')]))}
    print('shell',h,out[f'shell_h{h}'],flush=True)
json.dump(out, open('/home/hatch/workspace/warp-pilot/gate8/results/wa_run4.json','w'), indent=1)
print('DONE',flush=True)
