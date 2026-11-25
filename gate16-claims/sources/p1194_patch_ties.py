#!/usr/bin/env python3
"""Add max-residual tie sets (from the independent checker's
recomputation, p1194_checker_output.json run of record) to
p1194_results.json. Values transcribed from the checker
output: A best start 7 ties [44,50,51,52]; B best start 6
ties [14..44]; B projected seed ties [14..44]."""
import json
import subprocess

W = '/home/hatch/workspace/warp-pilot'
res = json.load(open(W + '/phase119/results/p1194_results.json'))
res['half_A']['best']['max_resid_ties_within_1e-9'] = [44, 50, 51, 52]
res['half_B']['best']['max_resid_ties_within_1e-9'] = list(range(14, 45))
res['half_B']['hinge_projected_seed']['max_resid_ties_within_1e-9'] = \
    list(range(14, 45))
res['tie_note'] = (
    'At candidates whose worst point is a plateau pin, the '
    'maximum residual is tied within 1e-9 across many subset '
    'points (the independent checker lists the tie set for '
    'every read). The stored max_resid_point is the primary '
    'path\'s argmax; every tied point carries the same '
    'decomposition pattern (half (b): t_FB share ~1; half (a) '
    'best: all-sign pin). Verdicts do not depend on which '
    'tied point is named.')
data = json.dumps(res, indent=1)
p = subprocess.run(['perl', W + '/phase119/work/p1194_writefile.pl',
                    W + '/phase119/results/p1194_results.json'],
                   input=data.encode(), capture_output=True)
print(p.stderr.decode(), 'rc', p.returncode)
