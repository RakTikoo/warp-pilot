import numpy as np, time
from scipy.optimize import minimize

rng = np.random.default_rng(7)

def Ered_grad(theta, N, k, h=1.0):
    D = np.sqrt(N**2*h**2+4*k**2)
    s = np.sin(theta); c = np.cos(theta)
    P = np.prod(s)
    f = -h*np.sum(c) - 2*k*P + D
    # dP/dtheta_j = c_j * prod_{i!=j} s_i ; guard zeros
    with np.errstate(divide='ignore', invalid='ignore'):
        ratio = np.where(np.abs(s)>1e-300, P/np.where(s==0,1,s), 0.0)
    g = h*s - 2*k*c*ratio
    return f, g

for N,r in [(2,0.5),(2,1.0),(2,2.0),(5,0.5),(6,0.5),(6,1.0),(8,0.5),(8,1.0),(10,0.5),(10,1.0),(10,2.0)]:
    t0=time.time()
    k=r; h=1.0
    D=np.sqrt(N**2+4*k**2)
    ths=np.linspace(0,np.pi/2,400001)
    vals=-N*np.cos(ths)-2*k*np.sin(ths)**N + D
    i=np.argmin(vals)
    best=(vals[i], np.full(N, ths[i]))
    for s_ in range(300):
        x0 = rng.uniform(0, np.pi/2, N)
        res = minimize(Ered_grad, x0, args=(N,k), jac=True, method='L-BFGS-B',
                       bounds=[(0,np.pi/2)]*N, options={'ftol':1e-18,'gtol':1e-14,'maxiter':500})
        if res.fun < best[0]-1e-12:
            best=(res.fun, res.x)
    print(f"N={N} r={r} sym={vals[i]:.12f} th_sym={ths[i]:.5f} multistart={best[0]:.12f} theta={np.round(np.sort(best[1]),5)} marg={4*k*k/D:.10f} ({time.time()-t0:.1f}s)", flush=True)
