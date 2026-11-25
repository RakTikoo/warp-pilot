#!/usr/bin/env python3
"""GATE-19 independent reproduction of the fluid_T transposition defect.
Three tests, gate's own code:
 (1) synthetic ADM metric: coded fluid_T vs basis-free (rho+p)n(x)n + p g,
     and vs the A^T That A tetrad form.
 (2) degenerate-plane rotation: rebuild Em with V rotated inside gamma's
     exactly-degenerate plane; coded output must not move if well-defined.
 (3) stored P128-2 bed: coded vs basis-free max diff (subset points).
Run BEFORE and AFTER the source fix; mode from argv: pre|post.
"""
import json, os, sys
import numpy as np
W = '/home/hatch/workspace/warp-pilot'
for p in ('phase128/work', 'phase119/work', 'phase101/work', 'phase76', 'phase18', 'phase48', 'phase15'):
    sys.path.insert(0, os.path.join(W, p))
import p761_lib as L
import p481_lib as PL

mode = sys.argv[1] if len(sys.argv) > 1 else 'pre'
out = {'mode': mode}
rng = np.random.default_rng(19)

# ---- (1) synthetic ADM metric ----
# gamma = R diag(2.0, 1.0, 0.5) R^T (non-degenerate, rotated), beta != 0
th = 0.7
R = np.array([[np.cos(th), -np.sin(th), 0.], [np.sin(th), np.cos(th), 0.], [0., 0., 1.]])
gam1 = R @ np.diag([2.0, 1.0, 0.5]) @ R.T
alpha1, beta1 = 0.83, np.array([0.21, -0.13, 0.05])
g1 = np.zeros((4, 4))
g1[0, 0] = -alpha1**2 + beta1 @ np.linalg.inv(gam1) @ beta1 * 0 + beta1 @ (np.linalg.solve(gam1, beta1)) * 0  # placeholder fixed below
# ADM: g00 = -alpha^2 + beta_i beta^i ; g0i = beta_i ; gij = gamma_ij, beta_i = gamma_ij beta^j
beta_cov1 = gam1 @ beta1
g1[0, 0] = -alpha1**2 + beta1 @ beta_cov1
g1[0, 1:] = beta_cov1; g1[1:, 0] = beta_cov1; g1[1:, 1:] = gam1
pts1 = np.array([[14.75, 0., 0.]])  # r inside window support? window_w peaks plateau; rho scale irrelevant (linear in rho0)
w_, rho0_ = 0.37, 1.3
FT = L.fluid_T(pts1, g1[None], w_, rho0_)[0]
r1 = np.linalg.norm(pts1[0]); rho = rho0_ * float(PL.window_w(np.array([r1]))[0]); p = w_ * rho
ncov = np.array([-alpha1, 0., 0., 0.])
Tbf = (rho + p) * np.outer(ncov, ncov) + p * g1
out['synthetic'] = dict(max_coded_vs_basisfree=float(np.max(np.abs(FT - Tbf))),
                        rho=float(rho), p=float(p))
# tetrad-form check with the lib's own Em construction
gamma = g1[1:, 1:]; beta_cov = g1[0, 1:]
ginv_ = np.linalg.inv(gamma); beta_up = ginv_ @ beta_cov
alpha = np.sqrt(-g1[0, 0] + beta_cov @ beta_up)
lam, V = np.linalg.eigh(gamma)
Em = np.zeros((4, 4)); Em[0, 0] = 1/alpha; Em[1:, 0] = -beta_up/alpha
for i in range(3):
    Em[1:, i+1] = V[:, i]/np.sqrt(lam[i])
A = np.linalg.inv(Em)
That = np.diag([rho, p, p, p])
T_correct = A.T @ That @ A
T_codedform = A @ That @ A.T
out['synthetic']['max_AThatA_vs_basisfree'] = float(np.max(np.abs(T_correct - Tbf)))
out['synthetic']['max_codedform_vs_basisfree'] = float(np.max(np.abs(T_codedform - Tbf)))
out['synthetic']['max_coded_vs_codedform'] = float(np.max(np.abs(FT - 0.5*(T_codedform+T_codedform.T))))

# ---- (2) degenerate-plane rotation ----
gam2 = R @ np.diag([1.5, 1.5, 0.4]) @ R.T   # exactly degenerate 1.5,1.5
beta2 = np.array([0.11, 0.07, -0.03]); alpha2v = 0.91
beta_cov2 = gam2 @ beta2
g2 = np.zeros((4, 4)); g2[0, 0] = -alpha2v**2 + beta2 @ beta_cov2
g2[0, 1:] = beta_cov2; g2[1:, 0] = beta_cov2; g2[1:, 1:] = gam2
def fluid_with_V(gamma, beta_cov, alpha, Vrot):
    lam_, V_ = np.linalg.eigh(gamma)
    # rotate the two degenerate eigenvectors by 0.9 rad inside their plane
    Q = np.eye(3); c, s = np.cos(0.9), np.sin(0.9)
    # eigh sorts ascending: lam = (0.4, 1.5, 1.5); degenerate plane = cols 1,2
    Q[1, 1], Q[1, 2], Q[2, 1], Q[2, 2] = c, -s, s, c
    Vr = V_ @ Q if Vrot else V_
    Em_ = np.zeros((4, 4)); Em_[0, 0] = 1/alpha; Em_[1:, 0] = -(np.linalg.inv(gamma) @ beta_cov)/alpha
    for i in range(3):
        Em_[1:, i+1] = Vr[:, i]/np.sqrt(lam_[i])
    A_ = np.linalg.inv(Em_)
    return A_ @ That @ A_.T, A_.T @ That @ A_
ginv2 = np.linalg.inv(gam2); bup2 = ginv2 @ beta_cov2
alp2 = np.sqrt(-g2[0, 0] + beta_cov2 @ bup2)
rho2 = rho; p2 = p; That = np.diag([rho2, p2, p2, p2])
coded0, corr0 = fluid_with_V(gam2, beta_cov2, alp2, False)
coded1, corr1 = fluid_with_V(gam2, beta_cov2, alp2, True)
out['degenerate'] = dict(coded_rotation_move=float(np.max(np.abs(coded1 - coded0))),
                         correct_rotation_move=float(np.max(np.abs(corr1 - corr0))))

# ---- (3) stored P128-2 bed ----
import p1194_lib as P4
import p1282_lib as B128
rec = json.load(open(os.path.join(W, 'phase128/results/p1282_results.json')))
best = rec['best']
wall = B128.WallBlend(1.1); wall.blend_bp = [float(x) for x in best['blend']]
pts = wall.pts_sub
K = wall.kern(pts); g = K['g']
wB = float(P4.W_B); rho0B = float(best['rho0'])
FTb = L.fluid_T(pts, g, wB, rho0B)
rr = np.linalg.norm(pts, axis=1)
rhob = rho0B * PL.window_w(np.clip(rr, 0, 60)); pb = wB * rhob
gam_b = g[:, 1:, 1:]; bcov_b = g[:, 0, 1:]
ginv_b = np.linalg.inv(gam_b); bup_b = np.einsum('pij,pj->pi', ginv_b, bcov_b)
alp_b = np.sqrt(-g[:, 0, 0] + np.einsum('pi,pi->p', bcov_b, bup_b))
ncov_b = np.zeros((len(pts), 4)); ncov_b[:, 0] = -alp_b
Tbf_b = (rhob + pb)[:, None, None] * np.einsum('pi,pj->pij', ncov_b, ncov_b) + pb[:, None, None] * g
out['p1282_bed'] = dict(max_coded_vs_basisfree=float(np.max(np.abs(FTb - Tbf_b))),
                        mean_abs_diff=float(np.mean(np.abs(FTb - Tbf_b))),
                        fluid_scale_max=float(np.max(np.abs(Tbf_b))))
print(json.dumps(out, indent=1))
json.dump(out, open(os.path.join(W, f'gate19/results/g19_repro_{mode}.json'), 'w'), indent=1)
