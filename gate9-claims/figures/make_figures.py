# Figure generator for the Gate-9 claims bundle (release v1.11.0).
# Reads ONLY the bundle's own stored result files (../results/*.json);
# every plotted value traces to those files (see MANIFEST.md).
# Plain-text labels throughout (no mathtext), programme venv python.
import json
import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = pathlib.Path(__file__).resolve().parent
RES = HERE.parent / "results"


def load(name):
    return json.loads((RES / name).read_text())


# ---------------------------------------------------------------- G9-1
wa = load("wa_g91_numbers.json")
combos = ["rho", "NEC1", "NEC2", "DEC_r", "DEC_t", "SEC"]
grid_min = [wa["grid_float64"]["minima"][c]["value"] for c in combos]
tail = [float(wa["probes_mp50"]["tail_1000"][c]) for c in combos]
throat_labels = ["NEC1", "DEC_t"]
throat_gate = [wa["comparisons"]["throat_NEC1_mine_limit"],
               wa["comparisons"]["throat_DEC_t_mine_limit"]]
throat_stored = [wa["stored"]["throat_NEC1"], wa["stored"]["throat_DEC_t"]]

fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))
x = range(len(combos))
w = 0.38
axes[0].bar([i - w / 2 for i in x], grid_min, w,
            label="float64 grid minimum (2500 pts, at r = 1000)")
axes[0].bar([i + w / 2 for i in x], tail, w,
            label="50-digit probe at r = 1000")
axes[0].set_yscale("log")
axes[0].set_xticks(list(x))
axes[0].set_xticklabels(combos)
axes[0].set_ylabel("B-combination value (all > 0)")
axes[0].set_title("G9-1: whole-domain minima of the six EC combinations")
axes[0].legend(fontsize=7)
axes[0].grid(True, axis="y", alpha=0.3)

x2 = range(len(throat_labels))
axes[1].bar([i - w / 2 for i in x2], throat_gate, w, label="Gate-9 limit (fresh engine)")
axes[1].bar([i + w / 2 for i in x2], throat_stored, w, label="stored (Phases 61/71)")
axes[1].set_xticks(list(x2))
axes[1].set_xticklabels(throat_labels)
axes[1].set_ylabel("throat value")
axes[1].set_title("G9-1: throat NEC1 / DEC_t - gate vs stored")
axes[1].legend(fontsize=7)
axes[1].grid(True, axis="y", alpha=0.3)
fig.tight_layout()
fig.savefig(HERE / "fig_g91_legality.png", dpi=150)
plt.close(fig)

# ---------------------------------------------------------------- G9-2
wb = load("wb_g92_numbers.json")
radii = [10, 100, 1000]
member_jump = [abs(float(wb["primary_radii_audited_interior"]["10"]["jump"])),
               abs(float(wb["primary_radii_audited_interior"]["100"]["jump"])),
               abs(float(wb["deciding"]["jump_Rtilde_at_my_a_zero"]))]
slice_jump = [wb["anchor_phi0_jump_numeric_examples"][f"p=0.1,Sig={r}"] for r in radii]

fig, ax = plt.subplots(figsize=(6.4, 4.2))
ax.plot(radii, member_jump, "o-", label="joining member (Phi2, p = 0.1): |[R~]|")
ax.plot(radii, slice_jump, "s--",
        label="Phi = 0 slice identity (1+p)(r0/rS)^(1-p), p = 0.1: never zero")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("junction radius r_Sigma / r0")
ax.set_ylabel("|[R~]|")
ax.set_title("G9-2: [R~] vanishes only for the member at 10^3 r0\n"
             "(shell S00 = +0.0204229 alpha0; stored +0.020291; LEGAL)")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(HERE / "fig_g92_join.png", dpi=150)
plt.close(fig)

# ---------------------------------------------------------------- G9-3
wc = load("wc_g93_numbers.json")
Rs = [10, 20, 30]


def block_series(blocks, profile):
    return [blocks[f"{profile}_R{r}"]["averaged_fit"]["min_phys"] for r in Rs]


fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))
axes[0].plot(Rs, block_series(wc["dynamic_member"]["blocks"], "P1"), "o-",
             label="member P1 (averaged)")
axes[0].plot(Rs, block_series(wc["dynamic_member"]["blocks"], "P2"), "o-",
             label="member P2 (averaged)")
axes[0].plot(Rs, block_series(wc["regate_Tb"]["blocks"], "P1"), "s--",
             label="T-b re-gate P1 (averaged)")
axes[0].plot(Rs, block_series(wc["regate_Tb"]["blocks"], "P2"), "s--",
             label="T-b re-gate P2 (averaged)")
axes[0].axhline(0.0, color="k", lw=0.8)
axes[0].set_xlabel("quotient domain R / r0")
axes[0].set_ylabel("smallest physical eigenvalue (omega^2)")
axes[0].set_title("G9-3: dynamic spectrum - no zero crossing, all minima > 0")
axes[0].legend(fontsize=7)
axes[0].grid(True, alpha=0.3)

tr = wc["static_member"]["mp40_traces"]
tr_r = [float(k) for k in tr.keys()]
tr_b = [abs(float(tr[k]["delta_b"])) for k in tr.keys()]
tr_p = [abs(float(tr[k]["delta_P"])) for k in tr.keys()]
axes[1].plot(tr_r, tr_b, "o-", label="|trace, delta_b| (40-digit)")
axes[1].plot(tr_r, tr_p, "s-", label="|trace, delta_P| (40-digit)")
axes[1].axhline(1e-25, color="r", lw=0.9, label="registered bar 1e-25")
axes[1].set_xscale("log")
axes[1].set_yscale("log")
axes[1].set_xlabel("radius r / r0")
axes[1].set_ylabel("|linearised-Bach trace|")
axes[1].set_title("G9-3: static traces at 40 digits (max 3.13e-34)")
axes[1].legend(fontsize=7)
axes[1].grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(HERE / "fig_g93_stability.png", dpi=150)
plt.close(fig)

# ---------------------------------------------------------------- G9-4
wd = load("wd_g94_numbers.json")
fit = wd["clause_c_pole"]["pole_fit_points_|NEC1|_vs_delta"]
deltas = sorted(float(k) for k in fit.keys())
nec = [fit[k if k in fit else str(k)] for k in
       [next(kk for kk in fit if float(kk) == d) for d in deltas]]
eps = [0.01, 0.001, 0.0001]
bounds = [wd["clause_c_pole"]["shell_price_lower_bounds"][f"eps={e}"]["ratio_lower_bound"]
          for e in ["0.01", "0.001", "0.0001"]]

fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))
axes[0].plot(deltas, nec, "o", label="|NEC1| at e^-1 (1 - delta), 40-digit probes")
order = wd["clause_c_pole"]["pole_order_loglog_fit"]
ref = [nec[2] * (deltas[2] / d) ** order for d in deltas]
axes[0].plot(deltas, ref, "--", label=f"log-log fit, pole order {order:.2f} (stored 7)")
axes[0].set_xscale("log")
axes[0].set_yscale("log")
axes[0].set_xlabel("delta (distance from the pole at x_b = e^-1)")
axes[0].set_ylabel("|NEC1|")
axes[0].set_title("G9-4: the grown shell is singular - NEC1 pole at x_b = e^-1")
axes[0].legend(fontsize=7)
axes[0].grid(True, alpha=0.3)

axes[1].plot(eps, bounds, "o-", label="shell price lower bound (x E_legal per decade)")
axes[1].axhline(2.216e73, color="r", lw=0.9,
                label="T-b finite price 2.216e73 x E_legal")
axes[1].set_xscale("log")
axes[1].set_yscale("log")
axes[1].set_xlabel("pole exclusion epsilon")
axes[1].set_ylabel("price lower bound (x E_legal)")
axes[1].set_title("G9-4: shell price is UNBOUNDED as epsilon -> 0")
axes[1].set_ylim(1e70, 1e98)
axes[1].legend(fontsize=7)
axes[1].grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(HERE / "fig_g94_formation.png", dpi=150)
plt.close(fig)

print("figures written")
