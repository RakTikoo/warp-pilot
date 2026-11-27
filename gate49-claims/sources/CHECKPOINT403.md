# PHASE 403 — THE POSE SEARCH

**VERDICT: POSE SEARCH RAISES — GATE REFERRAL.
Step 1 (extend the width trend): the trend does
NOT turn. C395's transported joint rises
monotonically through widths 16, 18, 20, 24 to
the registered cap W28 [1, 29] (−9.384899×10⁻⁶),
stopped by the cap (SS4(c)), not by a turn or
an infeasibility; the per-unit-width increments
decay (2.54 → 0.48 ×10⁻⁶) but stay positive.
Step 2 (re-optimise at W28): the scaling search
(334 reads, all feasible, zero DEC-saturated)
finds the centre pose [1, 29], (μ_S, μ_N, μ_M)
= (0.5000090643041506, 1.8999807308424006,
4.892092241322827) at joint −3.676112×10⁻⁶
(SET-244, band pose [1, 29] under transport),
worst-null −5.242074×10⁻⁶, clamped
−3.811020×10⁻⁶ — +2.613374×10⁻⁵ over C395's
home level, worst-null improving alongside
(+2.565414×10⁻⁵, no disagreement flag). RIDERS:
the centre presses the registered box's μ_S
edge (9.1×10⁻⁶ above 0.50) and μ_N edge
(1.9×10⁻⁵ below 1.90) — the optimum OF THE
REGISTERED BOX at this pose; its SS7 peak
|β·S| = 0.442682 clears the half-of-H2 bar
(0.442674) by only 8.0×10⁻⁶; and it is a band
read at its pose under transport, quotable
only as such until a full-extent audit at W28
runs. The level remains NEGATIVE: no EC pass,
no member.**

Charged at ledger entry 1039 (402's named
successor). Registration filed before any
computation: `phase403/work/p403_registration.md`
(SS0–SS9; SS5 notes the polish-method
resolution). Frame of record: the VM (laptop
admission run and followed — §2).

## 1. The act

402's transport (the affine argument map
φ(r) = 10 + (r − a′)·(10/W′), λ = 10/W′;
profile values unrescaled, β = 1.1 unchanged)
composed with the lineage's per-profile scaling
assembly (p394_lib.profiles_at394). Step 1:
transported reads of C395 at widths 16, 18, 20,
24, 28 (centre-15 poses; cap geometric, a′ ≥ 1).
Step 2: the 394/395 search pattern (RAY, DIAG,
G1, G2, G3, G4/G5 Nelder-Mead polishes) over
(μ_S, μ_N, μ_M) at the best width, in the
registered box μ_S ∈ [0.50, 1.10], μ_N ∈
[0.95, 1.90], μ_M ∈ [1.60, 6.50], with the SS7
physicality criterion (peak |β·S| ≥
0.4426742490267404 = 0.5 × H2's 0.8853484980534808)
recorded on every read. JOINT = min(nec, dec)
(402 Amendment 1 semantics); feasibility = C1
ρ_min ≥ 0 AND the pose floors (transported
scaled totals' min N ≥ 0.55, min M ≥ 1.0 on the
2001-point fine band grid).

## 2. Controls

All SS3 controls pass at diff 0.0 (VM, 32 s;
`results/p403_controls.json`): CTL-403-C395-HOME
(lineage read at C395: all five minima, the
worst-null −3.0896210095678075×10⁻⁵, Type-I
count 4067), CTL-403-POSE-HOME (the composed
machinery at [10, 20] reproduces it on every
field), CTL-403-W12 / CTL-403-W14 (402's
transported rows: joints −2.4728052267161693×10⁻⁵
/ −2.050976956715771×10⁻⁵, worst-nulls, DEC, ρ,
Type-I 4093 / 4097), CTL-403-H2 ((1,1,1) →
L_stat(H2) = −1.942246×10⁻⁴).

LAPTOP ADMISSION (CTL-403-ADM): NOT ADMITTED —
the C-10 signature, as in 402 (frame-invariants
at roundoff: dec 2.2×10⁻¹⁹, ρ 0.0; Type-I count
exact; sampled NEC/WEC drift 1.61×10⁻⁷ /
1.77×10⁻⁶, laptop argmin on the sibling shell
15.488 vs VM 15.732). Deciding reads all VM.
Record: `results/p403_controls_laptop.json`.

## 3. Step 1 — the width response curve

Full table in the memo. Joints by width:
10 → −2.980985×10⁻⁵; 12 → −2.472805×10⁻⁵;
14 → −2.050977×10⁻⁵; 16 → −1.792647×10⁻⁵;
18 → −1.571427×10⁻⁵; 20 → −1.393772×10⁻⁵;
24 → −1.128452×10⁻⁵; 28 → −9.384899×10⁻⁶.
Monotone; every row C1- and floor-feasible;
worst-null improves at every step in the same
direction (no disagreement flag); DEC recedes
(−1.777×10⁻⁶ → −3.879×10⁻⁷); ρ_min falls
(+9.781×10⁻⁵ → +4.705×10⁻⁵) — widening spends
density margin to buy pressure level. Stop =
the registered cap; best width 28, pose
[1, 29], λ = 5/14. Record:
`results/p403_step1.json`.

## 4. Step 2 — the search at [1, 29]

334 stored reads (cap 400), all feasible, zero
DEC-saturated (worst DEC over reads
−4.327×10⁻⁷), 334 beat C395's home level, 329
beat the transported seed (−9.384899×10⁻⁶).
RAY: peaks at μ_M = 5.75 (−8.998×10⁻⁶), then
10⁻⁸-scale wiggle — the axis buys ≈ +3.9×10⁻⁷.
DIAG: rises at every step, increments growing
(−8.149, −7.185, −6.192, −5.221 ×10⁻⁶). G1
found the (μ_S ↓, μ_N ↑) slope at fixed μ_M;
G3 walked it to the corner (0.50, 1.90, A_M)
at −3.787147×10⁻⁶; G4 polish settled at the
winner; G5 (from the DIAG endpoint) converged
to the same basin (−3.861226×10⁻⁶), no beat.
Records: `results/p403_screens.jsonl`,
`results/parts/`, `results/p403_search_summary.json`.

## 5. The winner, confirmed

Full re-read reproduces its screen at diff 0.0
on all five minima (`results/p403_confirmation.json`):

- pose [1, 29]; triple (0.5000090643041506,
  1.8999807308424006, 4.892092241322827)
- joint −3.676112×10⁻⁶ (NEC-bound; NEC min
  −3.676112×10⁻⁶ @ r = 17.049)
- worst-null at the argmin −5.242074×10⁻⁶
- adversary depth (Type-I) −3.928911×10⁻⁷
- DEC −3.809243×10⁻⁷ @ r = 25.927; ρ_min
  +4.705527×10⁻⁵; Type-I 4603 (0.693)
- end-clamped −3.811020×10⁻⁶ (cost 1.349×10⁻⁷);
  the transported seed at the pose clamps to
  −9.384854×10⁻⁶ (cost ≈ 0). Record:
  `results/p403_clamp.json`.

ANATOMY (`results/p403_anatomy.json`): the
joint binds at a NON-Type-I point (r = 17.049
= φ⁻¹ of C395's home argmin 15.732 — the site
tracks the transport); over Type-I points the
configuration is within 3.93×10⁻⁷ of legal.
Locals at the site: S = 0.14855, S′′ = +0.00136,
N = 2.33544, M = 25.679, M′ = +1.71308 (vs
transported H2 at the same radius: S = 0.29710,
N = 1.22919, M = 6.04464). Band ranges:
S [−0.00395, 0.40244], N [2.185, 2.351],
M [1.610, 34.756].

PHYSICALITY (SS7): peak |β·S| =
0.44268227409480604 ≥ bar 0.4426742490267404 —
CLEARS by 8.03×10⁻⁶; ratio to H2 = 0.500009
(= μ_S, per Gate-47's measurement). Not an
artefact candidate under the registered
criterion; the margin is the polish's hair
above the box edge the criterion itself set.

GAIN DECOMPOSITION: transport +2.042495×10⁻⁵;
re-optimisation +5.708787×10⁻⁶ (beyond the
band); total +2.613374×10⁻⁵. The winner's
level is 1.9% of |L_stat(H2)| and twice C396's
flagged level while clearing the bar C396
failed (C396's G47-F rider untouched).

## 6. Fences and what's owed

Band reads under transport only (356): the
winner is quotable solely as a band read at
pose [1, 29] until a full-extent audit at that
pose runs; home full-extent restatements
stand. C-10 naming throughout; deciding values
are diff-0.0 reproductions and the
frame-invariant worst-null. No EC pass, no
member, no sustainment/front/transport
content. DESK: NO DATA CONTACT.

Owed / named for the parent (not launched):
the gate referral for the winner's claim set;
a full-extent audit at pose [1, 29]; the width
direction past the cap (the cap was geometric
— a′ ≥ 1 at centre 15 — so further widening
means moving the centre or the band's inner
edge rule, a new registration, not a
continuation of this one).

Spend: VM ≈ 35 min (controls 32 s, Step 1
32 s, search ≈ 31 min, confirmation 87 s);
laptop: the admission read + mirror sync only.
