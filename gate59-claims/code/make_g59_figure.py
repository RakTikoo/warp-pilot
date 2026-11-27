#!/usr/bin/env python
"""make_g59_figure.py -- written for the Gate-59 bundle.

Reads only the bundled records (sources/g59_relax2.json)
and writes figures/g59_relaxation.png: the gate's
per-site dictionary-relaxation evidence for the
Arm A / T_req negative (GATE59.md S5).

Left: the relaxation floor at the peak site A3 vs the
shell energy E (log scale), with the joint fit's A3
residual and the 428 F1 bar (1e-9) as references.
Right: per-site floors -- joint fit residual vs
relaxation floor at the stored energy, all three sites.
"""
import json
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', 'sources', 'g59_relax2.json')
OUT = os.path.join(HERE, '..', 'figures', 'g59_relaxation.png')

r = json.load(open(SRC))
scan = r['A3_peak_scan']
Es = [x['E'] for x in scan]
fl = [x['polished_frob'] for x in scan]
joint = r['joint_fit_site_residuals']
others = {}
for x in r['other_sites']:
    others[x['site']] = x['polished_frob']
relax = {'A1_joint_argmin': others['A1_joint_argmin'],
         'A2_sec_argmin': others['A2_sec_argmin'],
         'A3_peak': fl[0]}

fig, ax = plt.subplots(1, 2, figsize=(10.5, 4.2))
a = ax[0]
a.plot(Es, fl, 'o-', color='#2456a6', lw=1.6, ms=6,
       label='relaxation floor at A3 (192 modes, free amplitudes)')
a.axhline(joint['A3_peak'], color='#c0392b', ls='--', lw=1.3,
          label="joint fit's A3 residual (1.2754e-3)")
a.axhline(1e-9, color='grey', ls=':', lw=1.3,
          label='428 F1 bar (1e-9)')
a.set_yscale('log')
a.set_xlabel('shell energy E')
a.set_ylabel('Frobenius residual at A3')
a.set_title('Single-shell floor at the peak site vs E')
a.legend(fontsize=7.5, loc='lower right')
a.grid(alpha=0.3, which='both')

b = ax[1]
sites = ['A1_joint_argmin', 'A2_sec_argmin', 'A3_peak']
labels = ['A1\n(joint argmin)', 'A2\n(SEC argmin)', 'A3\n(peak)']
x = np.arange(3)
w = 0.38
b.bar(x - w / 2, [joint[s] for s in sites], w,
      color='#c0392b', label='joint fit residual')
b.bar(x + w / 2, [relax[s] for s in sites], w,
      color='#2456a6', label='per-site relaxation floor')
b.axhline(1e-9, color='grey', ls=':', lw=1.3,
          label='428 F1 bar (1e-9)')
b.set_yscale('log')
b.set_xticks(x)
b.set_xticklabels(labels, fontsize=8.5)
b.set_ylabel('residual (Frobenius, per site)')
b.set_title('The relaxation floors where the joint fit floors')
b.legend(fontsize=7.5)
b.grid(alpha=0.3, which='both', axis='y')

fig.tight_layout()
os.makedirs(os.path.dirname(OUT), exist_ok=True)
fig.savefig(OUT, dpi=150)
print('wrote', OUT)
