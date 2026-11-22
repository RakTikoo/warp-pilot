"""MRV wormhole audit -- the CERTIFIED even-sector (l=2) ghost sign
structure (Gate-3 certification follow-up, 2026-11-22).

Source data: gate3/results/v_g3_1_cert.json -- the branch-independent
action-level certification of the sign of det K for the even-parity
kinetic matrix of the Mironov-Rubakov-Volkova designer
beyond-Horndeski wormhole (arXiv:1811.05832; tau = 10).  The
certification eliminates the auxiliary field b by a block Schur
complement of the action/EOM symbol and restricts the (i*om)^2
coefficient to the Hamiltonian-constraint surface -- a congruence, so
the determinant SIGN is basis-independent; no equation-of-motion row
operation is performed at any step.

(a) Designer theory: det K_phys at the four settled radii
    r = -20, -5, +5, +20.  Signs (+, -, -, +): negative at |r| = 5
    (the ghost band, bracketed by the settled points) and positive
    at |r| = 20.  At r = 0 det K degenerates in every presentation
    and carries no sign.
(b) Eigenvalues of K_phys at r = -5 and r = +5: the designer theory
    has mixed signs at both radii (a ghost), while the GR +
    canonical-scalar control on the same substrate is positive
    definite (both eigenvalues positive; det = +7661.64 at both
    radii) -- the healthy answer, on the same machinery on which an
    earlier row-elimination route flipped the control's sign by
    branch (+6717.02 / -6817.65).

Values are in the certification route's normalisation; magnitudes
are presentation-dependent and the SIGN is the invariant content.
All plotted values are read from the result file at render time and
asserted against the gate record.  All arithmetic float64.
"""
import json
import os

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

WP = os.path.expanduser("~/workspace/warp-pilot")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "mrv_ghost_certified.png")

cert = json.load(open(os.path.join(WP, "gate3/results/v_g3_1_cert.json")))
assert cert["verdict"] == "CERTIFIED"
assert cert["parametrisations_all_invariant"] is True
assert cert["congruence_all_invariant"] is True
assert cert["h_all_invariant"] is True

RADII = [-20, -5, 5, 20]
dets = np.array([cert["radii"][str(r)]["det"] for r in RADII],
                dtype=np.float64)
expected = {  # GATE3.md certification section, this route's normalisation
    -20: (+137.96, "positive"), -5: (-67.26, "negative"),
    5: (-17.20, "negative"), 20: (+127.28, "positive"),
}
for r, d in zip(RADII, dets):
    assert cert["radii"][str(r)]["sign"] == expected[r][1]
    assert abs(d - expected[r][0]) < 0.01, (r, d)

eigs_des = {r: np.array(cert["radii"][str(r)]["K_phys_eigs"],
                        dtype=np.float64) for r in (-5, 5)}
eigs_gr = {r: np.array(cert["GR_control"][str(r)]["K_phys_eigs"],
                       dtype=np.float64) for r in (-5, 5)}
for r in (-5, 5):
    assert np.any(eigs_des[r] < 0) and np.any(eigs_des[r] > 0)  # ghost
    assert np.all(eigs_gr[r] > 0)                               # healthy
    assert abs(cert["GR_control"][str(r)]["det"] - 7661.64) < 0.01

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.2))

# (a) det K_phys at the settled radii
colors = ["#2166ac" if d > 0 else "#b2182b" for d in dets]
ax1.bar([str(r) for r in RADII], dets, color=colors, width=0.58)
ax1.axhline(0.0, color="black", lw=0.9)
for r, d in zip(RADII, dets):
    ax1.annotate(f"{d:+.2f}", (str(r), d),
                 ha="center", va="bottom" if d > 0 else "top",
                 fontsize=9, xytext=(0, 2 if d > 0 else -2),
                 textcoords="offset points")
ax1.set_xlabel("radius r  (settled points; r = 0 is degenerate, no sign)")
ax1.set_ylabel(r"det $\mathcal{K}_{\mathrm{phys}}$  (certification normalisation)")
ax1.set_title("(a) Designer theory: det $\\mathcal{K}$ sign at $\\ell=2$\n"
              "negative at $|r|=5$, positive at $|r|=20$", fontsize=10.5)

# (b) eigenvalues at r = -5, +5: designer vs GR control
x = np.arange(4)
labels = [r"designer, $r=-5$", r"designer, $r=+5$",
          r"GR control, $r=-5$", r"GR control, $r=+5$"]
evals = np.array([eigs_des[-5], eigs_des[5], eigs_gr[-5], eigs_gr[5]])
for i, ev in enumerate(evals):
    for j, e in enumerate(ev):
        ax2.scatter(i + (j - 0.5) * 0.22, e,
                    s=64, color="#b2182b" if e < 0 else "#2166ac",
                    zorder=3)
ax2.axhline(0.0, color="black", lw=0.9)
ax2.set_xticks(x)
ax2.set_xticklabels(labels, fontsize=8.3)
ax2.set_ylabel(r"eigenvalues of $\mathcal{K}_{\mathrm{phys}}$")
ax2.set_title("(b) Eigenvalues at the band radii\n"
              "designer: mixed signs (ghost); GR control: positive definite",
              fontsize=10.5)

fig.tight_layout()
fig.savefig(OUT, dpi=200)
print("wrote", OUT)
print("dets:", dict(zip(RADII, dets.tolist())))
print("designer eigs:", {r: v.tolist() for r, v in eigs_des.items()})
print("GR eigs:", {r: v.tolist() for r, v in eigs_gr.items()})
