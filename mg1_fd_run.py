import json
import numpy as np
import mg1_fr as mg
import mg1_fd_check as fdc
import verify_metric as vm

rows = json.load(open('results/mg1_stage1.json'))
def Rstar(aA, aC, v):
    for r in rows:
        if r['aA'] == aA and r['aC'] == aC and r['v_s'] == v and r.get('ahat') == 0.0:
            return r['R_absmax']
    raise KeyError((aA, aC, v))

cases = [
    dict(v_s=1.5, R=1.0, Delta=0.25, aA=0.0, aC=0.0, eta=0.0, ahat=1.0),
    dict(v_s=1.0, R=1.0, Delta=0.25, aA=0.3, aC=0.0, eta=0.0, ahat=0.1),
]
out = []
for c in cases:
    Rs = Rstar(c['aA'], c['aC'], c['v_s'])
    alpha = c['ahat'] / Rs
    gf_jax = mg.make_metric(c['v_s'], c['R'], c['Delta'], c['aA'], c['aC'], c['eta'])
    def gf_np(pts):
        pts = np.asarray(pts, dtype=float)
        if pts.ndim == 2:
            return np.stack([np.asarray(gf_jax(p)) for p in pts])
        return np.asarray(gf_jax(pts))
    pts = [np.array([0.0, 1.0, 0.0]), np.array([0.35, 0.85, 0.4])]
    for pt in pts:
        Tm_ad, Te_ad, R_ad, F_ad = mg.tensors_at_point(gf_jax, pt, alpha)
        Tm_fd, err = fdc.Tm_FD_richardson(gf_np, pt, alpha)
        d = float(np.max(np.abs(np.asarray(Tm_ad) - Tm_fd)))
        scale = float(np.max(np.abs(Tm_fd)))
        _ma = vm.hawking_ellis_margins(vm.eulerian_that(gf_np(pt[None]), np.asarray(Tm_ad)[None]))
        _mf = vm.hawking_ellis_margins(vm.eulerian_that(gf_np(pt[None]), Tm_fd[None]))
        m_ad = {k: float(_ma[k][0]) for k in ('nec', 'wec', 'sec', 'dec')}
        m_fd = {k: float(_mf[k][0]) for k in ('nec', 'wec', 'sec', 'dec')}
        print(f"aA={c['aA']} v={c['v_s']} ahat={c['ahat']} pt={pt}: maxdiff={d:.3e} rich_err={err:.3e} scale={scale:.3e}")
        print(f"   margins AD: nec={m_ad['nec']:+.4e} | FD: nec={m_fd['nec']:+.4e} sec={m_fd['sec']:+.4e}")
        out.append(dict(case={k: c[k] for k in c}, pt=pt.tolist(), maxdiff=d,
                        rich_err=float(err), scale=scale,
                        nec_ad=float(m_ad['nec']), nec_fd=float(m_fd['nec'])))
json.dump(out, open('results/mg1_fd_check.json', 'w'), indent=1)
print('saved')
