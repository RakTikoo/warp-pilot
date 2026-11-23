"""
Gate-8 W-A independent evaluator for G8-1.

DIFFERENT IN KIND from the Phase-1 judge (verify_metric.einstein_at_points):
the judge builds Gamma on offset points by FD of the metric and then takes a
SECOND finite difference OF GAMMA (nested FD4-of-FD4). This evaluator never
differentiates Gamma numerically: it takes DIRECT finite differences of the
metric's first AND second partial derivatives, then forms dGamma ALGEBRAICALLY
from dg, d2g and dginv = -ginv dg ginv. Two flavours:
  order=2: 2nd-order central direct differences.
  order=4: 4th-order direct differences (diagonal 2nd deriv via the standard
           5-point formula; mixed 2nd deriv via composition of 4th-order
           first-derivative operators applied to g itself -- still direct
           d2g, never dGamma by FD).
Only shared material: the stored composed-metric DEFINITION (shell profiles,
build_composed, composed_gfunc from phase41) whose audit is the claim, and
the audit point sets. float64 everywhere.
"""
import numpy as np
DTYPE = np.float64
EIGHT_PI = 8.0*np.pi

def _shift(pts, axis, k, h):
    p = pts.copy(); p[:, axis] += k*h; return p

def metric_derivs(gfunc, pts, h, order=2):
    """Returns g, dg[e] (e=1..3 spatial; dg[0]=0), d2g[e][f] symmetric."""
    P = len(pts)
    g0 = gfunc(pts)
    dg = [np.zeros_like(g0) for _ in range(4)]
    d2 = [[np.zeros_like(g0) for _ in range(4)] for _ in range(4)]
    if order == 2:
        gp = [gfunc(_shift(pts,i,1,h)) for i in range(3)]
        gm = [gfunc(_shift(pts,i,-1,h)) for i in range(3)]
        for i in range(3):
            dg[i+1] = (gp[i]-gm[i])/(2*h)
            d2[i+1][i+1] = (gp[i]-2*g0+gm[i])/h**2
        for i in range(3):
            for j in range(i+1,3):
                gpp = gfunc(_shift(_shift(pts,i,1,h),j,1,h))
                gpm = gfunc(_shift(_shift(pts,i,1,h),j,-1,h))
                gmp = gfunc(_shift(_shift(pts,i,-1,h),j,1,h))
                gmm = gfunc(_shift(_shift(pts,i,-1,h),j,-1,h))
                d2[i+1][j+1] = d2[j+1][i+1] = (gpp-gpm-gmp+gmm)/(4*h*h)
    elif order == 4:
        offs = {}
        for i in range(3):
            for k in (-2,-1,1,2):
                offs[(i,k)] = gfunc(_shift(pts,i,k,h))
            dg[i+1] = (offs[(i,-2)]-8*offs[(i,-1)]+8*offs[(i,1)]-offs[(i,2)])/(12*h)
            d2[i+1][i+1] = (-offs[(i,2)]+16*offs[(i,1)]-30*g0+16*offs[(i,-1)]-offs[(i,-2)])/(12*h*h)
        for i in range(3):
            for j in range(i+1,3):
                # mixed: apply 4th-order first-deriv operator in j to the
                # 4th-order first-deriv field in i (evaluated from g directly)
                acc = np.zeros_like(g0)
                for kj,wj in ((-2,1.0),(-1,-8.0),(1,8.0),(2,-1.0)):
                    base = _shift(pts,j,kj,h)
                    vals = []
                    for ki in (-2,-1,1,2):
                        vals.append(gfunc(_shift(base,i,ki,h)))
                    dgi = (vals[0]-8*vals[1]+8*vals[2]-vals[3])/(12*h)
                    acc += wj*dgi
                d2[i+1][j+1] = d2[j+1][i+1] = acc/(12*h)
    else:
        raise ValueError(order)
    return g0, dg, d2

def einstein_direct(gfunc, pts, h, order=2):
    pts = np.asarray(pts, dtype=DTYPE)
    g, dg, d2 = metric_derivs(gfunc, pts, h, order)
    ginv = np.linalg.inv(g)
    P = len(pts)
    # Gamma^a_bc = .5 ginv^ad (dg_b g_dc + dg_c g_db - dg_d g_bc)
    Gamma = np.zeros((P,4,4,4), dtype=DTYPE)
    for a in range(4):
        for b in range(4):
            for c in range(4):
                term = np.stack([dg[b][...,d,c]+dg[c][...,d,b]-dg[d][...,b,c] for d in range(4)], axis=-1)
                Gamma[...,a,b,c] = 0.5*np.einsum('...d,...d->...', ginv[...,a,:], term)
    # dginv_e = -ginv dg_e ginv  (e spatial; e=0 zero)
    dginv = [np.zeros_like(g) for _ in range(4)]
    for e in range(1,4):
        dginv[e] = -np.einsum('...ad,...de,...eb->...ab', ginv, dg[e], ginv)
    # dGamma_e^a_bc algebraic
    Ricci = np.zeros((P,4,4), dtype=DTYPE)
    for e in range(1,4):  # derivative direction (spatial index e, coord idx e)
        # d_e Gamma^a_bd for all a,b,d
        dG = np.zeros((P,4,4,4), dtype=DTYPE)
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    t1 = np.stack([d2[e][b][...,d,c]+d2[e][c][...,d,b]-d2[e][d][...,b,c] for d in range(4)], axis=-1)
                    term1 = 0.5*np.einsum('...d,...d->...', ginv[...,a,:], t1)
                    t2 = np.stack([dg[b][...,d,c]+dg[c][...,d,b]-dg[d][...,b,c] for d in range(4)], axis=-1)
                    term2 = 0.5*np.einsum('...d,...d->...', dginv[e][...,a,:], t2)
                    dG[...,a,b,c] = term1+term2
        a_idx = e  # coordinate index equals spatial e (coords 1..3)
        for b_ in range(4):
            for d_ in range(4):
                Ricci[...,b_,d_] += dG[...,a_idx,b_,d_]
                if d_ == a_idx:
                    for a in range(4):
                        Ricci[...,b_,d_] -= dG[...,a,b_,a]
    for b_ in range(4):
        for d_ in range(4):
            for a in range(4):
                for e in range(4):
                    Ricci[...,b_,d_] += (Gamma[...,a,a,e]*Gamma[...,e,b_,d_]
                                         - Gamma[...,a,d_,e]*Gamma[...,e,b_,a])
    Rsc = np.einsum('...ab,...ab->...', ginv, Ricci)
    G = Ricci - 0.5*Rsc[...,None,None]*g
    return G, g

def eulerian_that(g, Tcov):
    gamma = g[...,1:,1:]; beta_cov = g[...,0,1:]
    gamma_inv = np.linalg.inv(gamma)
    beta_up = np.einsum('...ij,...j->...i', gamma_inv, beta_cov)
    alpha2 = -g[...,0,0] + np.einsum('...i,...i->...', beta_cov, beta_up)
    alpha = np.sqrt(np.maximum(alpha2, 1e-300))
    lam, V = np.linalg.eigh(gamma)
    E = np.zeros(g.shape[:-2]+(4,4), dtype=DTYPE)
    E[...,0,0] = 1.0/alpha
    E[...,1:,0] = -beta_up/alpha[...,None]
    for i in range(3):
        E[...,1:,i+1] = V[...,:,i]/np.sqrt(lam[...,i])[...,None]
    That = np.einsum('...ma,...nb,...mn->...ab', E, E, Tcov)
    return 0.5*(That+np.swapaxes(That,-1,-2))

def margins_from_that(That):
    flat = That.reshape(-1,4,4); Np = flat.shape[0]
    M = flat.copy(); M[:,0,:] *= -1.0
    evals, evecs = np.linalg.eig(M)
    scale = np.maximum(np.max(np.abs(evals.real),axis=1),1e-300)
    real_ok = np.max(np.abs(evals.imag),axis=1) < 1e-8*scale
    ev2 = np.abs(evecs)**2
    norms = -ev2[:,0,:]+ev2[:,1,:]+ev2[:,2,:]+ev2[:,3,:]
    cand = norms < -1e-6
    typeI = real_ok & (cand.sum(axis=1)==1)
    k = np.argmax(cand,axis=1); ar = np.arange(Np)
    rho = np.where(typeI, -evals[ar,k].real, np.nan)
    mask = np.ones((Np,4),bool); mask[ar,k]=False
    ps = np.where(typeI[:,None], evals.real[mask].reshape(Np,3), np.nan)
    with np.errstate(invalid='ignore'):
        nec = np.where(typeI, np.min(rho[:,None]+ps,axis=1), np.nan)
        wec = np.where(typeI, np.minimum(rho, np.min(rho[:,None]+ps,axis=1)), np.nan)
        sec = np.where(typeI, np.minimum(np.min(rho[:,None]+ps,axis=1), rho+np.sum(ps,axis=1)), np.nan)
        dec = np.where(typeI, np.minimum(rho, rho-np.max(np.abs(ps),axis=1)), np.nan)
    return dict(rho=rho, p=ps, typeI=typeI, nec=nec, wec=wec, sec=sec, dec=dec,
                rho_euler=That[:,0,0])

def audit(gfunc, pts, h, order=2):
    G, g = einstein_direct(gfunc, pts, h, order)
    That = eulerian_that(g, G/EIGHT_PI)
    return That, margins_from_that(That)
