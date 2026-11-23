"""Checker over wb_g92_numbers.json against GATE9.md G9-2 bars."""
import json
from decimal import Decimal
d = json.load(open('/home/hatch/workspace/warp-pilot/gate9/results/wb_g92_numbers.json'))
res = {}
res['anchor_flat_eq_-2'] = Decimal(d['anchor_flat_Rtilde']) == Decimal(-2)
for s in ['10', '100']:
    res[f'anchor_Tb_{s}_within_0.1pct'] = Decimal(d['anchor_Tb'][s]['rel_err']) < Decimal('0.001')
res['anchor_phi0_identity_residual_zero'] = d['anchor_phi0_identity_residual'] == '0'
res['anchor_phi0_jump_formula'] = d['anchor_phi0_jump'] == 'Sigma**(p - 1)*(p + 1)'
dec = d['deciding']
res['beta_within_1pct'] = Decimal(dec['beta_rel_err_vs_stored']) < Decimal('0.01')
res['k_within_2pct'] = Decimal(dec['k_rel_err_vs_stored']) < Decimal('0.02')
res['jump_zero_40digit'] = abs(Decimal(dec['jump_Rtilde_at_my_a_zero'])) < Decimal('1e-20')
res['Rn_within_2pct'] = Decimal(dec['Rn_rel_err']) < Decimal('0.02')
res['S00_within_2pct'] = Decimal(dec['S00_rel_err']) < Decimal('0.02')
res['S00_sign_positive'] = dec['S00_sign_positive'] is True
res['primary_radii_no_join'] = all(Decimal(v['jump']) > 0 for v in d['primary_radii_audited_interior'].values())
res['ALL_PASS'] = all(res.values())
print(json.dumps(res, indent=1))
json.dump(res, open('/home/hatch/workspace/warp-pilot/gate9/results/wb_checker.json', 'w'), indent=1)
