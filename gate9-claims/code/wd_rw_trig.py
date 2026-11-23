#!/usr/bin/env python3
"""W-D follow-up to wd_rw.py: the 4 Weyl components sympy's simplify left
unreduced in the general-RW computation share the single trig factor
(-sin(2th)tan(th) - cos(2th) + 1) (times a(t)-dependent factors).
This script shows that factor is identically zero (sympy fu reduction),
so C = 0 identically on the general RW metric, as B = 0 already showed."""
import sympy as sp, json
th = sp.symbols('th')
e = -sp.sin(2*th)*sp.tan(th) - sp.cos(2*th) + 1
out = {"trig_factor": str(e), "fu_reduction": str(sp.fu(e)),
       "numeric_at_0.7": float(e.subs(th, 0.7)), "identically_zero": bool(sp.fu(e) == 0)}
json.dump(out, open('/home/hatch/workspace/warp-pilot/gate9/wd_rw_trig.json', 'w'), indent=1)
print(out)
