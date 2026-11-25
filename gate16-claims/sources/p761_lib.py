#!/usr/bin/env python3
"""
p761_lib.py -- P76-1 shared library: the derivative-coupled scalar
theory of P47-2/P52-2 on the Phase-48 wall bed.

THEORY (fixed by CHECKPOINT76 SS P76-1): action
  S = int e [ -(1-xi phi^2) T/2 + (bc/2) V^mu d_mu phi
              + (b2/2) phi^2 div V + P(X,phi) ] d^4x ,
  X = -(1/2) g^mn d_m phi d_n phi,  P(X,phi) = p1 X + p2 X^2
  (the P_phi = 0, two-parameter slice of P52-2's datum space;
   P_X = p1 + 2 p2 X, P_XX = 2 p2, c_r^2 = P_X/(P_X + 2 X P_XX)).

WALL POSE (stated, run record): the derivative couplings are
boundary-equivalent to an (alpha T + gamma R)/2 mixture with
  gamma(phi) = bc phi/2 - b2 phi^2/2            (P36-1/P47-2),
so on the metric bed the theory is read in its boundary-
equivalent metric form with effective coupling function
  H(phi) = 1 - xi phi^2 + gamma(phi)
(the throat demand pattern of P52-2 is -(F - gamma) x
(Ellis pattern), F = xi phi^2 - 1, i.e. exactly -H + 2 - ...
in the programme's demand sign convention; the wall code's
own sign convention is the P48-1 operational one, below).
Wall field-equation LHS (programme convention, p182_engine
F*R form E_R = 2 F G + 2 (Hess F - g Box F) with F = H/2,
plus the sector stress tensor in E-units as in p481_lib):
  E_tot = H G_bed + (Hess H - g Box H) + T_P  [+ T_fluid]
  T_P,ab = P_X d_a phi d_b phi + P g_ab ,
  T_required = E_tot / (8 pi)   (legality read on T_required).
Scalar profile: radial, Bed(beta,'wallwide',pi0,shape)
splines of p182_engine (support [8,22], zero outside --
screening (v) and exterior data (iv) are then exact).
Canonical EoM (P59-3: coupling force DIVIDED by P_X is the
EoM's kinetic structure; the residual read here is the
undivided EL numerator, normalised -- the DIVISION is
exhibited in the throat path, where D_eom = P_X - L^2 P_XX
divides the force, exactly as P52-2/P59-3 registered):
  eom = P_X Box phi - P_XX (v^mu ph_mu_nu v^nu)
        + (1/2) H_,phi R_bed          [P_phi = 0 slice]
  H_,phi = -2 xi phi + bc/2 - b2 phi  (coupling force density;
  its gamma part bc/2 - b2 phi is P52-2's force coefficient).
Family B fluid: isotropic, p_f = w rho_f, rho_f(r) =
rho0 * window_w(r) (P48-1 plateau window), separately
conserved read = its Eulerian-frame divergence companion
(same FD divergence used for T_required).
float64 everywhere.
"""
import sys

import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase18')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase15')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase48')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
import p182_engine as E          # noqa: E402
import p182_basis as B           # noqa: E402
import p152_lib as L15           # noqa: E402
import p481_lib as PL            # noqa: E402
import verify_metric as vm       # noqa: E402

EIGHT_PI = E.EIGHT_PI
PI4 = 4.0 * np.pi
N0 = -0.75   # div V at the Ellis throat (P47-2/P52-2)

# ==================================================================
# THROAT PATH (exact P52-2 algebra; the G-b anchor)
# ==================================================================

def F_(xi, u):
    return xi * u * u - 1.0


def demands(xi, beta, b2, u, L, W):
    """Programme-convention demanded totals (4pi x total matter),
    transcribed verbatim from phase52/p522_main.py."""
    F = F_(xi, u)
    gam = beta * u / 2 - b2 * u * u / 2
    gphi = beta / 2 - b2 * u
    gl = gphi * L
    gll = gphi * W - b2 * L * L
    D = 2 * xi * u * L
    rho = -F / 2 + D + gam / 2 + gll / 2
    pr = -F / 2 + gam / 2 - gl / 4
    pt = 3 * F / 8 - D / 2 - 3 * gam / 8 - gll / 2 - gl / 4
    return rho, pr, pt


def throat_solve_row(xi, beta, b2, w, u, L, P_phi=0.0, P_XX=0.0):
    """P52-2's joint throat solve, transcribed from p522_main.py.
    Unknowns (P, P_X, rho_f, W); canonical EoM: D_eom W =
    P_phi - (beta/2 - b2 u) n0 - P_X L/2, D_eom = P_X - L^2 P_XX
    (the coupling force DIVIDED by the kinetic coefficient --
    P59-3 canonical form)."""
    from scipy.optimize import fsolve
    F = F_(xi, u)
    if F <= 0 or L == 0:
        return None
    gam = beta * u / 2 - b2 * u * u / 2
    gphi = beta / 2 - b2 * u
    coeff = beta / 2 - b2 * u
    D = 2 * xi * u * L

    def eqs(x):
        PX, W = x
        rho_d, pr_d, pt_d = demands(xi, beta, b2, u, L, W)
        Deom = PX - L * L * P_XX
        return [PI4 * L * L * PX - (pr_d - pt_d),
                Deom * W + PX * L / 2 - (P_phi - coeff * N0)]
    PX0 = max(1e-3, (-7 * F / 8 + D / 2 + 7 * gam / 8) / (PI4 * L * L))
    try:
        sol, info, ier, _ = fsolve(eqs, [PX0, 0.0], full_output=True)
    except Exception:
        return None
    if ier != 1 or np.max(np.abs(eqs(sol))) > 1e-9:
        return None
    PX, W = float(sol[0]), float(sol[1])
    rho_d, pr_d, pt_d = demands(xi, beta, b2, u, L, W)
    s = (rho_d + pt_d) / PI4
    rho_f = s / (1 + w)
    P = (pt_d - PI4 * w * rho_f) / PI4
    res = [(-PI4 * P + PI4 * rho_f) - rho_d,
           (PI4 * (P + L * L * PX) + PI4 * w * rho_f) - pr_d,
           (PI4 * P + PI4 * w * rho_f) - pt_d]
    if max(abs(r) for r in res) > 1e-8:
        return None
    return dict(xi=xi, beta=beta, beta2=b2, w=w, phi0=float(u),
                L=float(L), P=float(P), P_X=float(PX),
                rho_f=float(rho_f), F_eff=float(F), W_EoM=float(W),
                channel_residuals=[float(r) for r in res],
                demanded_4pi_rho_plus_pt=float(rho_d + pt_d),
                fluid_share=float(PI4 * (1 + w) * rho_f),
                exchange_throat_l=float(coeff * N0 * L))


# ==================================================================
# WALL PATH
# ==================================================================

def gamma_of(phi, bc, b2):
    return bc * phi / 2.0 - b2 * phi * phi / 2.0


def H_of(phi, xi, bc, b2):
    return 1.0 - xi * phi**2 + gamma_of(phi, bc, b2)


def dH_of(phi, xi, bc, b2):
    return -2.0 * xi * phi + bc / 2.0 - b2 * phi


def fld_derivs(Fld, Gam, h=0.3):
    """Scalar-field partial 1st/2nd derivatives on the 19-pt
    stencil + covariant Hessian - g Box (p182_basis pattern)."""
    P = Fld.shape[0]
    dF = np.zeros((P, 4)); ddF = np.zeros((P, 4, 4))
    for i in range(3):
        ip, im = 1 + 2 * i, 2 + 2 * i
        dF[:, i + 1] = (Fld[:, ip] - Fld[:, im]) / (2 * h)
        ddF[:, i + 1, i + 1] = (Fld[:, ip] - 2 * Fld[:, 0]
                                + Fld[:, im]) / h**2
    cidx = 7
    for (i, j) in ((0, 1), (0, 2), (1, 2)):
        vals = [Fld[:, cidx + k] for k in range(4)]
        cidx += 4
        ddF[:, i + 1, j + 1] = ddF[:, j + 1, i + 1] = \
            (vals[0] - vals[1] - vals[2] + vals[3]) / (4 * h**2)
    Hess = ddF - np.einsum('pabc,pc->pab', Gam, dF)
    return dF, Hess


class PhiProfile:
    """Lightweight radial scalar profile: p182_engine.pi_splines
    ('wallwide') + its pi_jets formula, without E.Bed's shell
    rebuild (the metric comes from bed15)."""

    def __init__(self, pi0, shape):
        self.cs, self.d1, self.d2 = E.pi_splines('wallwide', pi0,
                                                 shape)

    def pi_jets(self, pts):
        pts = np.asarray(pts, dtype=np.float64)
        r = np.linalg.norm(pts, axis=1)
        rs = np.where(r > 0, r, 1.0)
        n = pts / rs[:, None]
        rc = np.clip(r, 0.0, 60.0)
        pip, pipp = self.d1(rc), self.d2(rc)
        P = len(pts)
        v = np.zeros((P, 4))
        v[:, 1:] = pip[:, None] * n
        H = np.zeros((P, 4, 4))
        coef = np.where(r > 0, pip / rs, 0.0)
        for i in range(3):
            for j in range(3):
                H[:, 1 + i, 1 + j] = pipp * n[:, i] * n[:, j] \
                    + coef * ((1.0 if i == j else 0.0)
                              - n[:, i] * n[:, j])
        return v, H



class Wall:
    """Bed + metric kernels for one beta (cached per point set)."""

    def __init__(self, beta):
        self.beta = float(beta)
        self.bed15 = L15.bed(beta)
        import p182_run as R
        self.idx = R.bind_subset(self.bed15)
        self.pts_sub = self.bed15['pts_b'][self.idx]
        self.pts_bind = self.bed15['pts_b']
        vidx = PL.vol300_index(self.bed15)
        self.pts_vol = self.bed15['pts_v'][vidx]
        self._kern = {}

    def kern(self, pts):
        # Phase 166 (2026-11-23) SOURCE FIX: this cache was keyed on
        # the point set alone, so swapping bed15['gf'] on a live Wall
        # (Phase 164's step-2 solver does exactly that) silently
        # served the OLD bed's jets. The cache is now invalidated
        # whenever the bed's metric factory changes identity, and
        # the key carries a point-set fingerprint (count + sum +
        # first/last rows) instead of count + sum alone. Regression:
        # phase166/work/p166_kern_regression.py.
        gf = self.bed15['gf']
        if gf is not getattr(self, '_kern_gf', None):
            self._kern = {}
            self._kern_gf = gf
        pts_a = np.asarray(pts, dtype=np.float64)
        key = (len(pts_a), float(np.sum(pts_a)),
               tuple(pts_a[0]) if len(pts_a) else (),
               tuple(pts_a[-1]) if len(pts_a) else ())
        if key in self._kern:
            return self._kern[key]
        pts = np.asarray(pts, dtype=np.float64)
        g, dg, ddg = E.metric_jets(self.bed15['gf'], pts, 0.3)
        v0 = np.zeros((len(pts), 4)); H0 = np.zeros((len(pts), 4, 4))
        sg, basis, aux = E.lag_basis(g, dg, ddg, v0, H0)
        Ric = aux['Ric']; Rsc = basis[:, 0]
        G = Ric - 0.5 * Rsc[:, None, None] * g
        out = dict(g=g, dg=dg, ddg=ddg, ginv=aux['ginv'],
                   Gam=aux['Gam'], G=G, Rsc=Rsc, sqrtg=sg)
        self._kern[key] = out
        return out

    def phi_jets(self, pts, pi0, shape):
        if not hasattr(self, '_beds'):
            self._beds = {}
        key = (round(float(pi0), 10), round(float(shape), 10))
        if key not in self._beds:
            self._beds[key] = PhiProfile(float(pi0), float(shape))
        bed = self._beds[key]
        v, H = bed.pi_jets(pts)
        return bed, v, H


    def E_total(self, pts, z, fluid=None):
        """z = (xi, bc, b2, pi0, shape, p1, p2).
        fluid = None or (w, rho0). Returns (Ecov, aux dict)."""
        xi, bc, b2, pi0, shape, p1, p2 = [float(q) for q in z]
        K = self.kern(pts)
        g, ginv, Gam = K['g'], K['ginv'], K['Gam']
        bed, v, H = self.phi_jets(pts, pi0, shape)
        sg, basis, aux = E.lag_basis(g, K['dg'], K['ddg'], v, H)
        XL = aux['XL']; X = -0.5 * XL
        ph = aux['ph']
        phi = bed.cs(np.clip(np.linalg.norm(pts, axis=1), 0, 60))
        Hf = H_of(phi, xi, bc, b2)
        # Hess H - g Box H via stencil values of H(phi(r))
        st = B.stencil(pts, 0.3).reshape(-1, 3)
        phis = bed.cs(np.clip(np.linalg.norm(st, axis=1), 0, 60))
        Hs = H_of(phis, xi, bc, b2).reshape(len(pts), 19)
        _, HessH = fld_derivs(Hs, Gam)
        BoxH = np.einsum('pab,pab->p', ginv, HessH)
        ER = Hf[:, None, None] * K['G'] + HessH \
            - g * BoxH[:, None, None]
        Pval = p1 * X + p2 * X**2
        PX = p1 + 2.0 * p2 * X
        TP = PX[:, None, None] * np.einsum('pa,pb->pab', v, v) \
            + Pval[:, None, None] * g
        Ecov = ER + TP
        if fluid is not None:
            w, rho0 = fluid
            Ecov = Ecov + fluid_T(pts, g, w, rho0)
        # canonical EoM numerator at pts
        box = np.einsum('pab,pab->p', ginv, ph)
        vup = np.einsum('pab,pb->pa', ginv, v)
        hv = np.einsum('pab,pb->pa', ph, vup)
        vhv = np.einsum('pa,pa->p', vup, hv)
        PXX = 2.0 * p2
        eom = PX * box - PXX * vhv \
            + 0.5 * dH_of(phi, xi, bc, b2) * K['Rsc']
        denom = np.abs(PX * box) + np.abs(PXX * vhv) \
            + np.abs(0.5 * dH_of(phi, xi, bc, b2) * K['Rsc']) + 1e-12
        cr2 = PX / np.where(np.abs(PX + 2 * X * PXX) > 0,
                            PX + 2 * X * PXX, np.nan)
        auxo = dict(phi=phi, X=X, PX=PX, H=Hf, eom=eom,
                    eom_denom=denom, cr2=cr2, Rsc=K['Rsc'],
                    F_eff=xi * phi**2 - 1.0)
        return Ecov, auxo

    def _jets(self, pts, bed):
        return E.metric_jets(self.bed15['gf'], pts, 0.3)[1:]


def fluid_T(pts, g, w, rho0):
    """Covariant isotropic-fluid tensor with Eulerian-frame
    diag(rho, w rho, w rho, w rho), rho = rho0 * window_w(r)."""
    r = np.linalg.norm(pts, axis=1)
    rho = rho0 * PL.window_w(np.clip(r, 0, 60))
    P = len(pts)
    That = np.zeros((P, 4, 4))
    That[:, 0, 0] = rho
    for i in range(1, 4):
        That[:, i, i] = w * rho
    # invert eulerian_that: That = E^T Tcov E (E^mu_a columns)
    gamma = g[:, 1:, 1:]
    beta_cov = g[:, 0, 1:]
    gamma_inv = np.linalg.inv(gamma)
    beta_up = np.einsum('pij,pj->pi', gamma_inv, beta_cov)
    alpha2 = -g[:, 0, 0] + np.einsum('pi,pi->p', beta_cov, beta_up)
    alpha = np.sqrt(np.maximum(alpha2, 1e-300))
    lam, V = np.linalg.eigh(gamma)
    Em = np.zeros((P, 4, 4))
    Em[:, 0, 0] = 1.0 / alpha
    Em[:, 1:, 0] = -beta_up / alpha[:, None]
    for i in range(3):
        Em[:, 1:, i + 1] = V[:, :, i] / np.sqrt(lam[:, i])[:, None]
    Einv = np.linalg.inv(Em)
    # GATE-19 SOURCE FIX (2026-11-23): the tetrad identity is
    # That = E^T Tcov E (E^mu_a columns), so Tcov = A^T That A with
    # A = Einv. The original line formed A That A^T (einsum
    # 'pma,pab,pnb') -- the transposed congruence. Invisible for
    # diagonal metrics / axis-aligned eigenbases; with a shift it
    # adds a spurious term depending on LAPACK's arbitrary
    # eigenbasis inside gamma's degenerate plane, so the coded
    # tensor was not a well-defined function of the geometry.
    # Proven in phase166/CHECKPOINT166.md P166-4 and independently
    # reproduced in gate19/work/g19_repro.py (synthetic ADM metric:
    # A^T That A matches the basis-free (rho+p) n(x)n + p g to
    # 3.3e-16, coded form missed by 0.737; degenerate-plane
    # rotation moved the coded output 0.140, the corrected form
    # 1.1e-16; P128-2 bed coded-vs-basis-free up to 0.114).
    # Regression: gate19/work/g19_repro.py (post mode). Every
    # fluid-consuming stored read (R_E, E_total legality) predates
    # this fix and encodes the defective tensor; see
    # gate19/GATE19.md for the re-audit map.
    Tcov = np.einsum('pam,pab,pbn->pmn', Einv, That, Einv)
    return 0.5 * (Tcov + np.swapaxes(Tcov, -1, -2))


def margins(Ecov, g, fast=False):
    if not fast:
        return PL.margins_from_E(g, Ecov)
    That = vm.eulerian_that(g, Ecov / EIGHT_PI)
    m = vm.hawking_ellis_margins(That, do_fallback=False)
    out = {}
    for k in ('nec', 'wec', 'sec', 'dec'):
        out[k] = np.where(np.isnan(m[k]), -1.0, m[k])
    out['That'] = That
    return out


def legal_frac(m):
    ok = (m['nec'] >= 0) & (m['wec'] >= 0) & (m['sec'] >= 0) \
        & (m['dec'] >= 0)
    return float(np.mean(ok)), ok


def divergence_companion(wall, pts, z, fluid=None, h=0.3):
    """Covariant divergence of T_required at pts (spatial FD on
    the 19-pt stencil, centre Gamma from kern). Returns
    relative-magnitude array (|div T| / (|T|_F + tiny))."""
    K = wall.kern(pts)
    Gam = K['Gam']; ginv = K['ginv']   # Gam[p,a,b,c] = Gamma^c_{ab}
    st = B.stencil(pts, h)
    P = len(pts)
    Tall = np.zeros((P, 19, 4, 4))
    for s in range(19):
        Es, _ = wall.E_total(st[:, s], z, fluid)
        Tall[:, s] = Es / EIGHT_PI
    dT = np.zeros((P, 3, 4, 4))        # dT[:,i] = d_{i+1} T_cov
    for i in range(3):
        ip, im = 1 + 2 * i, 2 + 2 * i
        dT[:, i] = (Tall[:, ip] - Tall[:, im]) / (2 * h)
    T0 = Tall[:, 0]
    Tmix = np.einsum('pab,pbc->pac', ginv, T0)        # T^a_c
    # nabla_a T^a_c = d_a T^a_c + Gam^a_{a d} T^d_c - Gam^d_{a c} T^a_d
    div = np.zeros((P, 4))
    for i in range(3):
        a = i + 1
        div += np.einsum('pb,pbc->pc', ginv[:, :, a], dT[:, i])
    # Gam^a_{a d}: sum over a of Gam[p,a,d,a]
    Gad = np.einsum('pada->pd', Gam)
    div += np.einsum('pd,pdc->pc', Gad, Tmix)
    div -= np.einsum('pacd,pad->pc', Gam, Tmix)
    scale = np.linalg.norm(T0.reshape(P, -1), axis=1) + 1e-12
    return np.abs(div).max(axis=1) / scale, div
