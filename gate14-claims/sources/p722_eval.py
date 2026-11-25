#!/usr/bin/env python
"""P72-2 evaluation: ONLY the published formulas fixed in the run record
(Hotta, arXiv:1002.0200, Eqs.(1)-(9) and the printed global max of E_B),
plus expectation values of the printed Hamiltonian (labelled as such).
float64 throughout."""
import json, numpy as np
from scipy.optimize import brentq, minimize

sx = np.array([[0,1],[1,0]], float); sz = np.array([[1,0],[0,-1]], float)
sy = np.array([[0,-1j],[1j,0]], complex); I2 = np.eye(2)
FR_COEF = 3.0/(32*np.pi**2)   # W6: 3/(32 pi^2)

def analyse(h, k):
    S = np.sqrt(h*h + k*k)
    # --- published formulas ---
    EA = h*h/S                                   # Eq.(4), projective (sum l^2 = 1/2)
    EB = (h*h+2*k*k)/S*(np.sqrt(1 + h*h*k*k/(h*h+2*k*k)**2) - 1)  # global max, after Eq.(7)
    cosz, sinz = h/S, k/S
    lam = np.array([(1+cosz)/2, (1-cosz)/2])
    Sground_nats = float(-np.sum(lam*np.log(lam)))
    Sground_ebits = Sground_nats/np.log(2)
    # Eq.(9) check at x=1: post-measurement B eigenvalues (1+-1)/2 -> entropy 0
    dS_nats = Sground_nats  # = sum_mu p f_I(1); verified numerically below via f_I
    def fI(x):
        y = np.sqrt(cosz**2 + x*sinz**2)
        lp, lm = (1+y)/2, (1-y)/2
        ent = lambda p: 0.0 if p<=0 else p*np.log(p)
        return -(ent(lp)+ent(lm)) + (ent((1+cosz)/2)+ent((1-cosz)/2))*0 - (-(ent((1+cosz)/2)+ent((1-cosz)/2))) - (-(ent((1+cosz)/2)+ent((1-cosz)/2)))
    # Direct: f_I(x) = S(rho_B(mu)) - S(rho_B) with sign per Eq.(9) definition
    # Eq.(9): Delta S = sum p f_I, f_I = [entropy terms of post] - [ground terms] negated:
    # f_I(x) = S_ground - S_post(x)  (from the printed expression)
    def fI_printed(x):
        y = np.sqrt(cosz**2 + x*sinz**2)
        def Hbin(p): return 0.0 if p<=0 or p>=1 else -(p*np.log(p)+(1-p)*np.log(1-p))
        return Hbin((1+cosz)/2) - Hbin((1+y)/2)
    dS_check = 0.5*fI_printed(1.0) + 0.5*fI_printed(1.0)
    # --- Hamiltonians (printed Eqs.(1)-(3)) ---
    HA = np.kron(h*sz + (h*h/S)*I2, I2); HB = np.kron(I2, h*sz + (h*h/S)*I2)
    V  = np.kron(2*k*sx, sx) + (2*k*k/S)*np.eye(4)
    H  = HA + HB + V
    evals, evecs = np.linalg.eigh(H)
    g = evecs[:, 0]
    assert abs(evals[0]) < 1e-12, evals[0]
    # ground correlations
    xx = np.kron(sx, sx); corr_xx = float(np.real(g.conj() @ (xx @ g)))
    # --- preparation prices ---
    Eprep_marg = 2*k*k/S                       # = -2k<xx>_g, run record R-marg
    assert abs(Eprep_marg - (-2*k*corr_xx)) < 1e-12
    # separable minimum of <H> over product Bloch vectors (expectation of printed H)
    def Eprod(th):
        a = np.array([np.sin(th[0])*np.cos(th[1]), np.sin(th[0])*np.sin(th[1]), np.cos(th[0])])
        b = np.array([np.sin(th[2])*np.cos(th[3]), np.sin(th[2])*np.sin(th[3]), np.cos(th[2])])
        return h*a[2] + h*b[2] + 2*k*a[0]*b[0] + 2*S  # constants sum to 2S
    best = np.inf
    rng = np.random.default_rng(722)
    for _ in range(200):
        x0 = rng.uniform(0, 2*np.pi, 4)
        r_ = minimize(Eprod, x0, method="Nelder-Mead",
                      options={"maxiter": 4000, "xatol": 1e-12, "fatol": 1e-14})
        best = min(best, r_.fun)
    Esep = float(best); Eprep_sep = Esep  # E_ground = 0
    # --- Bob operation and tau_pulse: direct evaluation of printed H, U_max ---
    # projective sigma_A^x measurement
    Mx = [ (np.eye(4) + np.kron(sx, I2))/2, (np.eye(4) - np.kron(sx, I2))/2 ]
    denom = np.sqrt((h*h+2*k*k)**2 + h*h*k*k)
    rho = np.zeros((4,4), complex)
    for mu in range(2):
        q = (-1)**mu * 0.5; p = 0.5
        cos2 = (h*h+2*k*k)*p/ (denom*np.sqrt(p*p)) * np.sqrt(p)  # use printed forms directly:
        # printed: cos2Omega = (h^2+2k^2) p / sqrt((h^2+2k^2)^2 p^2 + h^2 k^2 q^2)
        cos2 = (h*h+2*k*k)*p/np.sqrt((h*h+2*k*k)**2*p*p + h*h*k*k*q*q)
        sin2 = -h*k*q/np.sqrt((h*h+2*k*k)**2*p*p + h*h*k*k*q*q)
        Om = 0.5*np.arctan2(sin2, cos2)
        UB = np.kron(I2, np.cos(Om)*I2 + 1j*np.sin(Om)*np.array([[0,-1j],[1j,0]], complex))
        psi = Mx[mu] @ g.astype(complex)
        psi = UB @ psi
        rho += np.outer(psi, psi.conj())
    HBV = HB + V
    f0 = float(np.real(np.trace(rho @ HBV)))
    # evolve: rho(t) in eigenbasis of H
    rho_e = evecs.conj().T @ rho @ evecs; HBV_e = evecs.conj().T @ HBV.astype(complex) @ evecs
    def f(t):
        ph = np.exp(-1j*evals*t)
        rt = rho_e * np.outer(ph, ph.conj())
        return float(np.real(np.sum(rt * HBV_e.T)))
    ts = np.linspace(0, 20, 20001); vals = np.array([f(t) for t in ts])
    cross = None
    for i in range(len(ts)-1):
        if vals[i] < 0 <= vals[i+1]:
            cross = float(brentq(f, ts[i], ts[i+1], xtol=1e-14)); break
    tau = cross
    R_raw = EB*tau/FR_COEF if tau else None      # hbar=1 model units: E_B*tau/(coef*hbar)
    E_net_B = Eprep_marg - EB
    R_net = 0.0 if E_net_B >= 0 else abs(E_net_B)*tau/FR_COEF
    return dict(h=h, k=k, r=k/h, EA=EA, EB=EB, EB_over_EA=EB/EA,
                S_ground_nats=Sground_nats, S_ground_ebits=Sground_ebits,
                dS_consumed_nats=float(dS_check), dS_consumed_ebits=float(dS_check)/np.log(2),
                EB_per_ebit_consumed=EB/(float(dS_check)/np.log(2)),
                EB_per_ebit_initial=EB/Sground_ebits,
                corr_xx=corr_xx, E_prep_sep=Eprep_sep, E_sep=Esep,
                E_prep_marg=Eprep_marg, E_net_B_sector=E_net_B,
                total_price_deciding=Eprep_sep+EA, total_per_EB=(Eprep_sep+EA)/EB,
                total_price_marg=Eprep_marg+EA, total_per_EB_marg=(Eprep_marg+EA)/EB,
                f0_HBV=f0, tau_pulse=tau, R_raw=R_raw, R_net=R_net,
                E_legal_at_tau=FR_COEF/tau if tau else None)

out = {"model": "Hotta minimal two-qubit QET, arXiv:1002.0200 Eqs.(1)-(9)",
       "FR_coef_3_over_32pi2": FR_COEF,
       "points": [analyse(1.0, r) for r in (0.5, 1.0, 2.0)]}
print(json.dumps(out, indent=2))
with open("/home/hatch/workspace/warp-pilot/phase72/results/p722_results.json", "w") as fh:
    json.dump(out, fh, indent=2)
