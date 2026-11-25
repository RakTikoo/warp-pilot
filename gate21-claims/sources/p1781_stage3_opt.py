#!/usr/bin/env python3
"""P178-1 Stage 3+4 -- SPECULATIVE.
CONSTRAINED OPTIMUM (a-priori selection rule): minimise linearised
coupled closure ||res0 + J.d|| subject to |g41.d|<=5e-4, |g44.d|<=5e-4,
count-preserving linearised sign(D0+GD.d)=sign(D0) at all 56 points.
Method: scipy SLSQP (analytic Jacobians), multi-start; cross-checked by
a min-max-|dq| feasibility solve at caps 0.63/0.625/0.62.
EXACT VERIFICATION: exact-read optimum (pose_E_coupledIa +
residual_frame closure; reads() for q/Type-I/count). If a clause
misses, iterate: correction steps against EXACT reads (secant form:
q/D gradients and coupled J carried from d=0, residual vector re-read
exactly at each candidate), each iteration exact-read and logged.
"""
import json, sys, time
import numpy as np
from scipy.optimize import minimize
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase176/work')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase171/work')
import p1763_common as X
import p1711_common as C

t0=time.time()
WRK='/home/hatch/workspace/warp-pilot/phase178/work'
RES='/home/hatch/workspace/warp-pilot/phase178/results'
S=np.load('/home/hatch/workspace/warp-pilot/phase176/work/p1763_state.npz')
res0, scales, J = S['res0'], S['scales'], S['J_coupled_Ea']
G=np.load(WRK+'/p1781_grad.npz')
g41,g44,GD,D0 = G['g41'],G['g44'],G['GD'],G['D0']
basis=X.BASES['Ea']
CAP,TOL=0.63,5e-4
sgnD=np.sign(D0); assert np.all(sgnD!=0)
U,sv,Vt=np.linalg.svd(J,full_matrices=False); V=Vt.T
d_ls=-V@((U.T@res0)/np.maximum(sv,1e-300))
def lin_closure(d): return float(np.sqrt(np.mean((res0+J@d)**2)))
Cu,Ca,Cb=X.field_value_contribs(basis)
SIG_CUT=23.491427444171965
def stats(d):
    y=Vt@d
    return dict(norm=float(np.linalg.norm(d)),max_coeff=float(np.max(np.abs(d))),
        max_field_value=float(max(np.abs(Cu@d).max(),np.abs(Ca@d).max(),np.abs(Cb@d).max())),
        frac_below_sigcut=float(np.sum(y[sv<SIG_CUT]**2)/np.sum(y**2)) if np.sum(y**2)>0 else 0.0,
        lin_closure=lin_closure(d),lin_dq41=float(g41@d),lin_dq44=float(g44@d),
        lin_count_ok=bool(np.all(np.sign(D0+GD@d)==sgnD)),
        lin_count_min_margin=float(np.min(sgnD*(D0+GD@d))))

# ---------- linearised optimum (min closure s.t. q + count) ----------
def solve_minclosure(d_start):
    cons=[dict(type='ineq',fun=lambda d: TOL-g41@d,jac=lambda d:-g41),
          dict(type='ineq',fun=lambda d: TOL+g41@d,jac=lambda d: g41),
          dict(type='ineq',fun=lambda d: TOL-g44@d,jac=lambda d:-g44),
          dict(type='ineq',fun=lambda d: TOL+g44@d,jac=lambda d: g44),
          dict(type='ineq',fun=lambda d: sgnD*(D0+GD@d),
              jac=lambda d: sgnD[:,None]*GD)]
    def obj(d): r=res0+J@d; return float(r@r)
    def jac(d): return 2*J.T@(res0+J@d)
    return minimize(obj,d_start,jac=jac,constraints=cons,method='SLSQP',
                    options=dict(maxiter=1000,ftol=1e-16))
# equality-constrained LS start: min closure s.t. g41.d=0,g44.d=0
Aeq=np.stack([g41,g44])
KKT=np.zeros((74,74)); KKT[:72,:72]=J.T@J; KKT[:72,72:]=Aeq.T; KKT[72:,:72]=Aeq
rhs=np.concatenate([-J.T@res0,[0.0,0.0]])
try:
    sol_eq=np.linalg.solve(KKT,rhs)[:72]
except np.linalg.LinAlgError:
    sol_eq=np.linalg.lstsq(KKT,rhs,rcond=None)[0][:72]
cands={}
for nm,st in (('from_ls',d_ls),('from_eqLS',sol_eq),('from_zero',np.zeros(72))):
    r=solve_minclosure(st.copy())
    cands[nm]=dict(success=bool(r.success),message=str(r.message),d=r.x,**stats(r.x))
    print('minclosure',nm,'success',r.success,'lin_closure',cands[nm]['lin_closure'],
          'dq',cands[nm]['lin_dq41'],cands[nm]['lin_dq44'],'count_ok',cands[nm]['lin_count_ok'],flush=True)
feas={k:v for k,v in cands.items() if abs(v['lin_dq41'])<=TOL+1e-9 and abs(v['lin_dq44'])<=TOL+1e-9 and v['lin_count_ok']}
best_name=min(feas,key=lambda k:feas[k]['lin_closure']) if feas else None
print('BEST linearised:',best_name, flush=True)

# min-max-|dq| at fixed caps (obstruction pricing if infeasible / margin check)
def solve_min_t(cap):
    R=cap*np.sqrt(224.0)
    cons=[dict(type='ineq',fun=lambda x: R**2-np.sum((res0+J@x[:72])**2),
               jac=lambda x: np.concatenate([-2*J.T@(res0+J@x[:72]),[0.0]])),
          dict(type='ineq',fun=lambda x: x[-1]-g41@x[:72],jac=lambda x: np.concatenate([-g41,[1.0]])),
          dict(type='ineq',fun=lambda x: x[-1]+g41@x[:72],jac=lambda x: np.concatenate([g41,[1.0]])),
          dict(type='ineq',fun=lambda x: x[-1]-g44@x[:72],jac=lambda x: np.concatenate([-g44,[1.0]])),
          dict(type='ineq',fun=lambda x: x[-1]+g44@x[:72],jac=lambda x: np.concatenate([g44,[1.0]])),
          dict(type='ineq',fun=lambda x: sgnD*(D0+GD@x[:72]),
              jac=lambda x: np.hstack([sgnD[:,None]*GD,np.zeros((56,1))]))]
    x0=np.concatenate([d_ls,[max(abs(g41@d_ls),abs(g44@d_ls))]])
    if np.sum((res0+J@d_ls)**2)>R**2: x0[:72]=0.0; x0[-1]=max(abs(g41@np.zeros(72)),0.0)
    r=minimize(lambda x: x[-1],x0,jac=lambda x: np.array([0.0]*72+[1.0]),
               constraints=cons,method='SLSQP',options=dict(maxiter=1000,ftol=1e-16))
    return dict(success=bool(r.success),t=float(r.fun),d=r.x[:72],**stats(r.x[:72]))
mint={}
for cap in (0.63,0.625,0.62):
    mint[str(cap)]=solve_min_t(cap)
    print('min_t at cap',cap,'t=',mint[str(cap)]['t'],'success',mint[str(cap)]['success'],flush=True)

# ---------- exact reads ----------
def exact_reads(d):
    gf=X.make_gf_enriched(d,basis)
    Et,_=C.pose_E_coupledIa(gf)
    dR,_,_=C.residual_frame(gf,Et)
    rv=X.resvec(dR,scales)
    cl=float(np.sqrt(np.mean(rv**2)))
    fr=C.reads(gf)
    return dict(closure=cl,q41=float(fr['q_r'][41]),q44=float(fr['q_r'][44]),
                dq41=float(fr['q_r'][41]-X.STORED_Q[0]),dq44=float(fr['q_r'][44]-X.STORED_Q[1]),
                typeI=[bool(fr['typeI'][i]) for i in (41,44)],count=int(np.sum(fr['typeI'])),
                D=np.array(fr['D_r'],dtype=np.float64),resvec=rv)
def clauses(e):
    return dict(closure_ok=bool(e['closure']<=CAP),dq_ok=bool(abs(e['dq41'])<=TOL and abs(e['dq44'])<=TOL),
                typeI_ok=bool(e['typeI']==[False,False]),count_ok=bool(e['count']==52))
def all_ok(e):
    c=clauses(e); return all(c.values()),c

iters=[]
d_cur = np.array((feas[best_name]['d'] if best_name else mint['0.63']['d']),dtype=np.float64)
for it in range(13):
    e=exact_reads(d_cur)
    ok,c=clauses(e),None
    ok,c=all_ok(e)
    rec=dict(iteration=it,closure=e['closure'],q41=e['q41'],q44=e['q44'],dq41=e['dq41'],dq44=e['dq44'],
             typeI=e['typeI'],count=e['count'],clauses=c,all_ok=bool(ok),**stats(d_cur))
    iters.append(rec); print('EXACT iter',it,json.dumps({k:rec[k] for k in ('closure','dq41','dq44','typeI','count','all_ok')}),flush=True)
    np.savez(WRK+'/p1781_iter_partial.npz',d=d_cur,iteration=it)
    json.dump(dict(iters=iters),open(WRK+'/p1781_iters.json','w'),indent=1)
    if ok: break
    # correction: minimise ||res_exact + J.delta||^2 + 1e-6||delta||^2 s.t.
    # g.delta = -dq_exact (both), and sgnD0*(D_exact + GD.delta) >= target
    # margins: 0 where sign already right, +|D| restoration where flipped;
    # plus keep closure linearised-around-candidate <= 0.628
    res_e=e['resvec']; D_e=e['D']
    tgt=np.where(sgnD*D_e>=0, 0.0, -sgnD*D_e+1e-6)  # required sgnD*GD.delta >= tgt - sgnD*D_e... form below
    # constraint: sgnD*(D_e + GD delta) >= m_i, m_i = 0 if sgnD*D_e>=0 else 0 (restore to >=0)
    cons=[dict(type='eq',fun=lambda dl: g41@dl+e['dq41'],jac=lambda dl: g41),
          dict(type='eq',fun=lambda dl: g44@dl+e['dq44'],jac=lambda dl: g44),
          dict(type='ineq',fun=lambda dl: sgnD*(D_e+GD@dl),jac=lambda dl: sgnD[:,None]*GD),
          dict(type='ineq',fun=lambda dl: (0.628*np.sqrt(224.0))**2-np.sum((res_e+J@dl)**2),
              jac=lambda dl: -2*J.T@(res_e+J@dl))]
    def obj(dl): r=res_e+J@dl; return float(r@r)+1e-6*float(dl@dl)
    def jac(dl): return 2*J.T@(res_e+J@dl)+2e-6*dl
    r=minimize(obj,np.zeros(72),jac=jac,constraints=cons,method='SLSQP',
               options=dict(maxiter=1000,ftol=1e-16))
    print(' correction success',r.success,'|delta|',float(np.linalg.norm(r.x)),flush=True)
    if not r.success and np.linalg.norm(r.x)==0: break
    d_cur=d_cur+r.x
final=iters[-1]
witness_found=bool(final['all_ok'])
out=dict(label='SPECULATIVE',method='SLSQP analytic Jacobians, multi-start (LS / equality-LS / zero); '
         'selection rule: minimum linearised coupled closure subject to |dq|<=5e-4 both sites and '
         'linearised count-preserving sign constraints; target closure margin: optimum sought <=0.625 '
         'when the min-closure optimum allows (it is the unconstrained-by-cap minimum)',
         H_grad=1e-3,
         linearised_candidates={k:{kk:vv for kk,vv in v.items() if kk!='d'} for k,v in cands.items()},
         linearised_best=best_name,
         min_t_at_caps={k:{kk:vv for kk,vv in v.items() if kk!='d'} for k,v in mint.items()},
         iterations=iters,witness_found=witness_found,seconds=time.time()-t0)
json.dump(out,open(WRK+'/p1781_stage3.json','w'),indent=1)
np.savez(WRK+'/p1781_state.npz',d_final=d_cur,
         d_lin_best=np.array(feas[best_name]['d']) if best_name else np.array(mint['0.63']['d']),
         d_mint_063=np.array(mint['0.63']['d']),d_ls=d_ls)
print('WITNESS_FOUND',witness_found,f'[{time.time()-t0:.0f}s]',flush=True)
print('STAGE3 DONE',flush=True)
