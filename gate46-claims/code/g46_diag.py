#!/usr/bin/env python3
"""Diagnostic: batch-vs-single margins at the SEED batch
argmin point (the 7.7e-08 C-10 phenomenon)."""
import numpy as np

import g46_lib as L
import g46_profiles as P

SEED = (0.9323593026620368, 1.1444417317708335, 2.289013671875)
out, R = L.set_read(*SEED)
i = int(np.argmin(R['nec']))
print('batch nec min:', R['nec'][i], 'at flat index', i,
      'typeI(batch):', bool(R['typeI'][i]))
pt = np.array(out['nec_argmin_point'])
print('point:', pt, 'r:', np.linalg.norm(pt))

# single-point read
That1 = L.that_at(*SEED, pt)
m1 = L.margins(That1[None, :, :])
print('single: typeI', bool(m1['typeI'][0]), 'nec', m1['nec'][0])

# shell-batch read restricted to the argmin shell
rr = out['nec_argmin_r']
pts = L.DIRS162 * rr
pr = P.scaled_profiles(*SEED, np.full(len(pts), rr))
T = L.T_cart(pts, pr)
g = L.metric_cart(pts, pr)
That = L.eulerian_that(g, T)
mb = L.margins(That)
i_r, i_d = divmod(i, 162)
print('shell batch: nec at dir', i_d, ':', mb['nec'][i_d],
      'typeI:', bool(mb['typeI'][i_d]))
print('That single vs shell-batch max diff:',
      float(np.max(np.abs(That1 - That[i_d]))))
# is the batch argmin the same direction as the shell argmin?
j = int(np.argmin(mb['nec']))
print('shell argmin dir:', j, 'nec:', mb['nec'][j],
      'typeI:', bool(mb['typeI'][j]))
# eigenvalue NEC at the single point regardless of class:
Mx = That1.copy()
Mx[0, :] *= -1.0
ev = np.linalg.eigvals(Mx)
print('single-point mixed-tensor eigenvalues:', np.sort(ev.real),
      'max imag:', float(np.max(np.abs(ev.imag))))
