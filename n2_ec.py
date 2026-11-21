"""
n2_ec.py — N2: Einstein-Cartan torsion (Weyssenhoff spin fluid).

Structure (Hehl-Datta): in EC gravity the Riemannian Einstein
tensor is sourced by an EFFECTIVE tensor
    Sigma = T_fluid + DeltaT_spin,
where the spin-spin contact term for a spin-aligned Weyssenhoff
fluid has, in the fluid rest frame with spin along z, the
anisotropic form (up to the O(1) factor conventions of the
literature, stated openly):
    DeltaT ~ -delta * diag(1, -1, -1, +1)   (eigenvalue form)
i.e. NEC along the spin axis: Delta(rho + p_z) = -2 delta < 0 —
the ONE classical contact term with the right sign to help a warp
wall — while NEC transverse saturates. Sign audit below is done on
the actual superluminal shell tensor (beta=1.5, S7 point): how
large must delta be for Sigma's fluid part (= T_req - DeltaT) to
be EC-legal?

Magnitude ledger (the kill): the contact term's size relative to
the fluid's own density is set by the CARTAN density scale,
rho_Cartan ~ 1e54 kg/m^3 (literature scale at which spin-torsion
terms rival matter terms for nucleon-like matter; labelled
literature value, case 2/3 boundary — no experiment probes EC
torsion at these densities). In geometric units:
    delta / T_fluid ~ T_fluid / T_Cartan.
Supplying a deficit D therefore needs a fluid of density
T_f ~ sqrt(D * T_Cartan). Numbers in the output: required T_f in
geom, J/m^3 and kg/m^3 vs nuclear density 1e18 kg/m^3 (densest
ordinary matter, before even asking for polarisation).
Assumption (named): torsion couples only to intrinsic spin
(standard EC). Constraint: spin-density required vs torsion
bounds from spin-precession / Hughes-Drever class experiments —
orders of magnitude weaker than the density kill; the density
ledger is the binding gate. c_T gate (D2): EC propagates tensors
at c (literature) — inside the GW170817 window.
float64 everywhere.
"""
import json, time
import numpy as np

import shell as sh
import verify_metric as vm
from verify_finalist import dense_points

DTYPE = np.float64
C_SI = 2.99792458e8
G_SI = 6.674e-11
GEOM_PER_JM3 = G_SI / C_SI ** 4        # J/m^3 -> 1/m^2
RHO_CARTAN_KGM3 = 1e54                 # literature scale, labelled
T_CARTAN_GEOM = RHO_CARTAN_KGM3 * C_SI ** 2 * GEOM_PER_JM3


def main():
    t0 = time.time()
    beta = 1.5
    prof = sh.build_shell(10.0, 20.0, 2.0, kind='edgepeaked',
                          params={'wd': 3.0, 'floor': 0.2},
                          s_rho=2.0, s_P=1.16, Nr=4001)
    gf = sh.shell_point_factory(prof, beta, 'cos', 1.0, [10.0, 20.0])
    pts = dense_points()
    _, That, m = vm.einstein_at_points(gf, pts, h=0.3)
    scale = np.max(np.abs(That), axis=(1, 2))
    sig = scale > 1e-6
    nec = m['nec'][sig]
    D = float(-np.min(nec))
    # spin axis = shift axis (x). In the eigenframe of each point we
    # cannot target the axis exactly; the generous bound: delta
    # must cover D/2 (NEC_z supply = 2 delta).
    delta_star = D / 2.0
    T_f_req = float(np.sqrt(delta_star * T_CARTAN_GEOM))
    out = {'beta': beta, 'D_nec_deficit': D,
           'delta_star': delta_star,
           'T_cartan_geom': float(T_CARTAN_GEOM),
           'T_fluid_required_geom': T_f_req,
           'T_fluid_required_Jm3': float(T_f_req / GEOM_PER_JM3),
           'T_fluid_required_kgm3': float(T_f_req / GEOM_PER_JM3
                                          / C_SI ** 2),
           'nuclear_kgm3': 1e18,
           'orders_above_nuclear': float(np.log10(
               T_f_req / GEOM_PER_JM3 / C_SI ** 2 / 1e18)),
           'wall_density_geom': float(np.max(That[:, 0, 0])),
           'elapsed_s': time.time() - t0,
           'verdict': ('Sign: the spin contact term CAN enter NEC '
                       'with the helping sign along the spin axis. '
                       'Magnitude: supplying the beta=1.5 deficit '
                       'needs a spin-polarised fluid ~10^'
                       + f"{float(np.log10(T_f_req / GEOM_PER_JM3 / C_SI ** 2 / 1e18)):.0f}"
                       ' orders of magnitude above nuclear density '
                       '— the term is real and irrelevant at warp '
                       'scales. Bounded exclusion by magnitude (F3: '
                       'structural — the coupling is fixed by GR '
                       'constants, no free parameter to tune). '
                       'REOPENING: a torsion coupling >> EC '
                       'standard (non-minimal torsion-matter '
                       'coupling) — a different theory, gated by '
                       'D2/D3 spin-precession bounds.')}
    print(json.dumps({k: out[k] for k in
                      ('beta', 'D_nec_deficit', 'delta_star',
                       'T_fluid_required_kgm3',
                       'orders_above_nuclear')}, indent=1))
    json.dump(out, open('results/n2_ec.json', 'w'), indent=1, default=float)
    print('N2 DONE', flush=True)


if __name__ == '__main__':
    main()
