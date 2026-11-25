import sympy as sp, json, sys
sys.path.insert(0, 'work')
from p721_lib import derive_G
G = derive_G()
out = {str(k): str(v) for k, v in G.items()}
with open('work/p721_G_exprs.json', 'w') as f:
    json.dump(out, f, indent=1)
print('done')
for k, v in G.items():
    print(k, '=', v)
