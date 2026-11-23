"""
W-A G9-1 stage 2: 40+ digit probes of the audited member via the fresh
engine, evaluated with mpmath-lambdified expressions at 50-digit
working precision (reported to 40 digits).
Probes: tail r=1000 (the stored tail-minimum radius); throat series
r = 1+1e-9 (the phase record's own probe point) and delta =
1e-6/1e-8/1e-10 for a quadratic-extrapolated throat limit.
"""
import sys, json, time
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate9')
import sympy as sp
import mpmath as mp
from wa_engine import build_bach, r, th

mp.mp.dps = 50
A = sp.Rational(27773424114865775, 10**17)
t0 = time.time()
out = build_bach(r**sp.Rational(1, 10), A * sp.log(r) / (1 + sp.log(r)),
                 final_simplify=False)
print('build_s', time.time() - t0, flush=True)
fns = {k: sp.lambdify(r, out[k].subs(th, 1), modules='mpmath', cse=True)
       for k in ('Bt', 'Br', 'Bth')}
print('lambdify done', time.time() - t0, flush=True)


def probe(rr):
    bt, br, bth = (fns[k](rr) for k in ('Bt', 'Br', 'Bth'))
    rho, pr, pt = -bt, br, bth
    return {
        'rho': mp.nstr(rho, 40), 'pr': mp.nstr(pr, 40), 'pt': mp.nstr(pt, 40),
        'NEC1': mp.nstr(rho + pr, 40), 'NEC2': mp.nstr(rho + pt, 40),
        'DEC_r': mp.nstr(rho - abs(pr), 40), 'DEC_t': mp.nstr(rho - abs(pt), 40),
        'SEC': mp.nstr(rho + pr + 2 * pt, 40),
        'DEC_r_gateform': mp.nstr(rho - pr, 40),
        'DEC_t_gateform': mp.nstr(rho - pt, 40),
        '_raw': {'NEC1': rho + pr, 'DEC_t': rho - abs(pt), 'rho': rho},
    }


pres = {}
for tag, rr in (('tail_1000', mp.mpf(1000)),
                ('throat_1+1e-9', 1 + mp.mpf(10)**-9),
                ('throat_1+1e-6', 1 + mp.mpf(10)**-6),
                ('throat_1+1e-8', 1 + mp.mpf(10)**-8),
                ('throat_1+1e-10', 1 + mp.mpf(10)**-10)):
    p = probe(rr)
    pres[tag] = {k: v for k, v in p.items() if k != '_raw'}
    print('probe', tag, 'NEC1', pres[tag]['NEC1'], 'DEC_t',
          pres[tag]['DEC_t'], flush=True)
    if tag.startswith('throat_1+'):
        pres[tag]['_raw'] = {k: mp.nstr(v, 45) for k, v in p['_raw'].items()}

ds = [mp.mpf(10)**-6, mp.mpf(10)**-8, mp.mpf(10)**-10]
tags = ('throat_1+1e-6', 'throat_1+1e-8', 'throat_1+1e-10')
lim = {}
for key in ('NEC1', 'DEC_t', 'rho'):
    ys = [mp.mpf(pres[t]['_raw'][key]) for t in tags]
    val = mp.mpf(0)
    for i in range(3):
        li = mp.mpf(1)
        for j in range(3):
            if i != j:
                li *= (0 - ds[j]) / (ds[i] - ds[j])
        val += ys[i] * li
    lim[key] = mp.nstr(val, 40)
pres['throat_limit_extrapolated'] = lim
print('limits', lim, flush=True)
for t in tags:
    del pres[t]['_raw']
with open('/home/hatch/workspace/warp-pilot/gate9/results/wa_member_probes.json', 'w') as fh:
    json.dump(pres, fh, indent=1)
print('total_s', time.time() - t0)
