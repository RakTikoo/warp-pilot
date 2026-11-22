#!/usr/bin/env python
"""Gate-5 G5-5 FRESH verification. All formulas transcribed by THIS worker
from arXiv:2106.02476 LaTeX source (WormAssympSafe01-07.tex):
 general improved eqs (Phi=0), simplified IEQ-tt/rr/ll-s, fKretsch,
 rhoellis/prellis/plellis, regionsr. float64. Planck units lP=1."""
import numpy as np, json
from scipy.optimize import brentq

out={}
xi=1.0; r0=1.0
# Paper printed simplified rho, pr (rhoellis, prellis) for f1: f=2 xi r0^2/r^4
def rho_paper(r,r0=r0,xi=xi): return -r0**2/r**8*(-30*xi*r0**2+24*xi*r**2+r**4)
def pr_paper(r,r0=r0,xi=xi):  return -r0**2/r**8*(-14*xi*r0**2+16*xi*r**2+r**4)
# General eqs with generic f (my transcription of the general system, Phi=0, b=r0^2/r)
def general(r,f,fp,fpp,r0=r0):
    b=r0**2/r; bp=-r0**2/r**2
    rho=(1+f)*bp/r**2-(1-b/r)*(fpp+2*fp/r)+(bp*r-b)*fp/(2*r**2)
    pr=-(1+f)*b/r**3+(1-b/r)*(2/r)*fp
    pl=-(1+f)*((bp*r-b)/(2*r**2)*(1/r))+(1-b/r)*(fp/r+fpp)-(bp*r-b)*fp/(2*r**2)
    return rho,pr,pl
def f1(r,r0=r0,xi=xi): return 2*xi*r0**2/r**4
def f1p(r,r0=r0,xi=xi): return -8*xi*r0**2/r**5
def f1pp(r,r0=r0,xi=xi): return 40*xi*r0**2/r**6
rs=np.linspace(1.0,50,2000)
g=np.array([general(r,f1(r),f1p(r),f1pp(r)) for r in rs])
out['general_vs_printed_rho_maxdiff']=float(np.max(np.abs(g[:,0]-rho_paper(rs))))
out['general_vs_printed_pr_maxdiff']=float(np.max(np.abs(g[:,1]-pr_paper(rs))))
# Corrected pl closed form (phase claim) vs my general pl
pl_corr=lambda r: r0**2*(r**4+32*xi*r**2-38*xi*r0**2)/r**8
out['general_pl_vs_corrected_maxdiff']=float(np.max(np.abs(g[:,2]-pl_corr(rs))))
# Printed IEQ-ll-s: (1+f) r0^2/r^4 * f' + (1-r0^2/r^2)(f'/r+f'') + r0^2/r^3 f'
def pl_printed(r):
    f,fp,fpp=f1(r),f1p(r),f1pp(r)
    return (1+f)*r0**2/r**4*fp+(1-r0**2/r**2)*(fp/r+fpp)+r0**2/r**3*fp
out['printed_pl_minus_general_at_r2']=float(pl_printed(2.0)-general(2.0,f1(2.0),f1p(2.0),f1pp(2.0))[2])
out['printed_pl_at_throat']=float(pl_printed(1.0)); out['correct_pl_at_throat']=float(pl_corr(1.0))
# Throat values analytic check
rt=np.array([general(1.0,f1(1.0),f1p(1.0),f1pp(1.0))])[0]
out['throat_rho_pr_pl']=[float(x) for x in rt]
out['throat_rho_plus_pr']=float(rt[0]+rt[1]); out['throat_SEC']=float(rt[0]+rt[1]+2*rt[2])
out['throat_rho_plus_pl']=float(rt[0]+rt[2])
# window: rho+pr throat = 2(2xi-r0^2)/r0^4 -> edge sqrt(2)=1.41421; f3 edge sqrt(2*sqrt3)
out['window_edge_f1']=float(np.sqrt(2)); out['window_edge_f3_correct_sqrt3']=float(np.sqrt(2*np.sqrt(3)))
out['window_edge_f3_if_sqrt4']=float(np.sqrt(2*2.0))
# Roots at xi=r0=1: NEC1 root and rho root (fine scan+brentq)
nec=lambda r: rho_paper(r)+pr_paper(r)
out['NEC1_root']=float(brentq(nec,1.0,1.2))
out['rho_root']=float(brentq(rho_paper,1.0,1.3))
# omega bands at xi=r0=1: find where omega crosses -1 (nec root) and rho root
out['omega_at_1.05']=float(pr_paper(1.05)/rho_paper(1.05))
out['omega_at_1.2']=float(pr_paper(1.2)/rho_paper(1.2))
# paper regionsr bounds at xi=1
out['regionsr_lower']=float(np.sqrt(2)); out['regionsr_upper']=float(np.sqrt(2)*np.sqrt(np.sqrt(51)-3))
# rootrho formula evaluated at window edge r0^2=2xi (phase provenance claim for upper bound)
def rootrho(r0v,xi=1.0): return np.sqrt(np.sqrt(6)*np.sqrt(xi*(5*r0v**2+24*xi))-12*xi)
def rootpl(r0v,xi=1.0): return np.sqrt(np.sqrt(2)*np.sqrt(xi*(11*r0v**2+50*xi))-10*xi)
out['rootrho_at_edge_r0sq2']=float(rootrho(np.sqrt(2))); out['rootpl_at_edge_r0sq2']=float(rootpl(np.sqrt(2)))
out['rootpl_at_r0_1']=float(rootpl(1.0)); out['rootrho_at_r0_1']=float(rootrho(1.0))
# Effective sector (GR tensor): rho_eff=b'/r^2, pr_eff=-b/r^3
out['eff_rho_plus_pr_at_throat']=float(-r0**2/1.0**4 - r0**2/1.0**4)  # -2 r0^2/r^4 at r=r0=1
# Conservation: div T for anisotropic MT, Phi=0: div = pr' + (2/r)(pr-pl)  [nabla_mu T^mu_r with sign conv: use magnitude]
def divT(r):
    h=1e-6
    prp=(pr_paper(r+h)-pr_paper(r-h))/(2*h)
    return prp+(2/r)*(pr_paper(r)-pl_corr(r))
for rr in [1.0043282259895108]:
    scale=(abs(rho_paper(rr))+abs(pr_paper(rr))+abs(pl_corr(rr)))/rr
    out['divT_at_1.0043']=float(divT(rr)); out['divT_ratio']=float(abs(divT(rr))/scale)
rr_grid=np.linspace(1.001,3,4000); ratios=[abs(divT(r))/((abs(rho_paper(r))+abs(pr_paper(r))+abs(pl_corr(r)))/r) for r in rr_grid]
out['divT_max_ratio_1_to_3']=float(np.max(ratios))

# ---- (b) Origination: general f-profile throat formula, derived fresh ----
# kappa(rho+pr)(r0) = (b'(r0)-1)*[(1+f0)/r0^2 + f'(r0)/(2 r0)]  (throat: 1-b/r=0)
omega=4/np.pi*(1-np.pi**2/144); out['omega_BR']=float(omega)
def throat_nec(r0v,bp,f0,fp):
    return (bp-1)*((1+f0)/r0v**2+fp/(2*r0v))
res={}
for shape,bp in [('ellis',-1.0),('sqrt',0.5)]:
    for xic in [1,10]:
        C=omega*xic**2  # f = C/r^2 (lP=1)
        grid=np.logspace(0,np.log10(1/1.616e-35),400)  # r0 in lP: 1 .. ~6.19e34 (1 m)
        corrs=[]
        terms=[]
        for r0v in grid:
            f0=C/r0v**2; fp=-2*C/r0v**3
            nec=throat_nec(r0v,bp,f0,fp); gr=(bp-1)/r0v**2
            corrs.append(nec-gr)
            # separate pieces: prefactor piece (bp-1)*f0/r0^2 ; X piece (bp-1)*fp/(2r0)
            terms.append(((bp-1)*f0/r0v**2,(bp-1)*fp/(2*r0v)))
        res[f'{shape}_xi{xic}']={'max_abs_corr':float(np.max(np.abs(corrs))),
            'nec_at_1lP':float(throat_nec(1.0,bp,C,-2*C)),
            'pieces_at_1lP':[float(terms[0][0]),float(terms[0][1])]}
out['origination_k_xi_over_r']=res
# NOTE checkpoint quoted -237.19/+237.19: that is (1+f0)-form pieces? check alternate split:
# full nec pieces at xi=10,ellis,r0=1: prefactor term (b'-1)(1+f0)/r0^2 and X term separately:
C=omega*100
out['alt_split_xi10_ellis']={'prefactor_incl_GR':float(-2*(1+C)),'X_term':float(-2*(-2*C/2)),'naive_nec':float(-2*(1+C))}
# curvature id: f=2 xi r0^2/r^4, n=4: bracket=(1-f0)/r0^2, f0=2/r0^2 (xi=1)
# switch: f0=0.01 -> r0=sqrt(200)
out['curv_switch_analytic']=float(np.sqrt(200))
grid=np.logspace(0,3,20001); f0=2/grid**2
idx=np.argmin(np.abs(f0-0.01)); out['curv_switch_grid']=float(grid[idx])
out['curv_window_edge']=float(np.sqrt(2))
print(json.dumps(out,indent=1))
with open('/tmp/g55/out.json','w') as fh: json.dump(out,fh,indent=1)
