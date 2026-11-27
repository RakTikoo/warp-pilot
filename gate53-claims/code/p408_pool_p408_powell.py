"""
p408_pool_p408_powell.py - Phase 392: one scipy Powell run on -beta_crit
(SCREENING ONLY, never a verdict), generalised from p386_stage2x_powell.py.
Usage: python p408_pool_p408_powell.py <spec.json>
spec: {"tag": str, "name": str, "lib": "p391_12"|"p392_16",
       "start_y": [n], "lo": [n], "hi": [n], "maxfev": int (default 1500)}
CPU screening on the EXTENDED per-candidate-r_m set (JointScreenX for
p386 lib; Screen12 for the 12-mode lib). Incumbent checkpointed to
~/work/p408/state/<tag>_powell_<name>_inc.json; final to
<tag>_powell_<name>.json.
"""
import os, sys, time, json
import numpy as np

POOL = '/home/spark/work/p386/warp-pilot'
P408 = POOL + '/phase408/work'
for p in [P408, POOL, POOL + '/phase386/work', POOL + '/phase251/work',
          POOL + '/phase50', POOL + '/gate6', POOL + '/phase63']:
    sys.path.insert(0, p)
os.environ.setdefault('OMP_NUM_THREADS', '1')
os.environ.setdefault('P386_CONSTR_DR', '2.5e-4')
os.environ.setdefault('P408_CONSTR_DR', '2.5e-4')
from scipy.optimize import minimize

spec = json.load(open(sys.argv[1]))
TAG, name, LIB = spec['tag'], spec['name'], spec.get('lib', 'p386')
lo = np.array(spec['lo'], dtype=np.float64)
hi = np.array(spec['hi'], dtype=np.float64)
ND = len(lo)
y0 = np.array(spec['start_y'], dtype=np.float64)
MAXFEV = int(spec.get('maxfev', 1500))
STATE = '/home/spark/work/p408/state'
os.makedirs(STATE, exist_ok=True)

if LIB == 'p391_12':
    import p408_pool_p391_screen12 as S12
    scr = S12.make_screen12()
elif LIB == 'p392_16':
    import p408_pool_p408_screen16 as S16
    scr = S16.make_screen16()
else:
    import p386_stage2x_common as C
    scr = C.make_screen()


def clip_box(y):
    return np.minimum(np.maximum(np.asarray(y, dtype=np.float64), lo), hi)


st = {'best_y': None, 'best_f': -np.inf, 'nfev': 0, 't0': time.time(),
      'last_write': 0.0}
inc_path = os.path.join(STATE, f'{TAG}_powell_{name}_inc.json')
res_path = os.path.join(STATE, f'{TAG}_powell_{name}.json')


def write_inc(done=False, extra=None):
    rec = {'start': name, 'tag': TAG, 'lib': LIB,
           'start_y': [float(v) for v in y0],
           'best_y': None if st['best_y'] is None else [float(v) for v in st['best_y']],
           'best_beta_crit_screening': None if st['best_y'] is None else float(st['best_f']),
           'best_record': None if st['best_y'] is None else scr.record(st['best_y']),
           'nfev_obj': st['nfev'], 'elapsed_s': time.time() - st['t0'],
           'done': done, 'note': 'SCREENING ONLY'}
    if extra:
        rec.update(extra)
    tmp = inc_path + '.tmp'
    json.dump(rec, open(tmp, 'w'), indent=1)
    os.replace(tmp, inc_path)
    st['last_write'] = time.time()


def obj(y):
    yy = clip_box(y)
    bc = scr.beta_crit(yy)
    st['nfev'] += 1
    if bc > st['best_f']:
        st['best_f'] = float(bc)
        st['best_y'] = yy.copy()
        write_inc()
    elif time.time() - st['last_write'] > 60:
        write_inc()
    return -float(bc)


bc0 = scr.beta_crit(clip_box(y0))
print(f'[{TAG}/{name}] start beta_crit_screening={bc0} '
      f'record={scr.record(clip_box(y0))}', flush=True)
r = minimize(obj, clip_box(y0), method='Powell',
             bounds=[(float(lo[i]), float(hi[i])) for i in range(ND)],
             options={'maxfev': MAXFEV, 'xtol': 1e-3, 'ftol': 1e-5})
xret = clip_box(r.x)
bc_ret = scr.beta_crit(xret)
if st['best_f'] >= bc_ret:
    xopt, bcopt, src = st['best_y'], st['best_f'], 'incumbent'
else:
    xopt, bcopt, src = xret, float(bc_ret), 'powell_return'
write_inc(done=True, extra={'powell_nfev': int(r.nfev),
                            'powell_success': bool(r.success),
                            'source': src,
                            'y_opt': [float(v) for v in xopt],
                            'beta_crit_screening': float(bcopt),
                            'record': scr.record(xopt)})
json.dump(json.load(open(inc_path)), open(res_path, 'w'), indent=1)
print(f'[{TAG}/{name}] POWELL DONE bc_screening={bcopt} '
      f'record={scr.record(xopt)} nfev_obj={st["nfev"]} '
      f'powell_nfev={r.nfev} wall={time.time()-st["t0"]:.0f}s src={src}',
      flush=True)
print(f'[{TAG}/{name}] y_opt={json.dumps([float(v) for v in xopt])}', flush=True)
