"""P108-5 second path (from scratch, dense Kronecker matrices).
Independent of p1085_eval.py: builds H, projectors, unitary as explicit
matrices; ground state by eigendecomposition (not the printed analytic
state); E_out, E_prep^(marg), E_in, S(t), tau by dense spectral evolution.
Usage: python p1085_secondpath.py N m r [N m r ...]  -> JSON lines."""
import numpy as np, itertools, json, sys
import numpy.linalg as la
from scipy.optimize import brentq
COEFF = 3/(32*np.pi**2)

def run(N,m,r):
    h=1.0; k=r*h; dim=2**N
    D=np.sqrt(N**2*h**2+4*k**2)
    sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]],complex)
    sz=np.diag([1.,-1.]).astype(complex); I2=np.eye(2,dtype=complex)
    def op(p,site):
        ops=[I2]*N; ops[site]=p; M=ops[0]
        for o in ops[1:]: M=np.kron(M,o)
        return M
    Hi=[h*op(sz,i)+(N*h**2/D)*np.eye(dim) for i in range(N)]
    Pall=op(sx,0)
    for i in range(1,N): Pall=Pall@op(sx,i)
    V=2*k*Pall+(4*k**2/D)*np.eye(dim)
    H=sum(Hi)+V
    w,Uh=la.eigh(H)
    assert abs(w[0])<1e-9, w[0]           # ground energy 0 (printed constants)
    g=Uh[:,0]
    n_in=N-m; outs=list(range(n_in,N))
    A=N*m*h**2+4*k**2; B=2*(N-m)*h*k
    theta=0.5*np.arccos(A/np.sqrt(A**2+B**2))
    G=op(sy,outs[0])
    for i in outs[1:]: G=G@op(sx,i)
    rho=np.zeros((dim,dim),complex); Ein=0.0
    Hin=sum(Hi[i] for i in range(n_in))
    for alpha in itertools.product([1,-1],repeat=n_in):
        psi=g.copy()
        for j,al in enumerate(alpha):
            Pj=0.5*(np.eye(dim)+al*op(sx,j)); psi=Pj@psi
        # E_in: expectation of input-sector H in post-measurement (pre-unitary) state, summed over outcomes
        Ein+=float(np.vdot(psi,Hin@psi).real)
        ap=int(np.prod(alpha))
        U=np.cos(theta)*np.eye(dim)-1j*ap*np.sin(theta)*G
        psi=U@psi; rho+=np.outer(psi,psi.conj())
    sector=sum(Hi[i] for i in outs)+V
    Eout=-float(np.trace(rho@sector).real)
    # marginals from eigvec ground state
    rho_g=np.outer(g,g.conj()); marg=[]
    for i in range(N):
        t=rho_g.reshape([2]*(2*N))
        keep=[i]+[N+j for j in range(N) if j!=i]
        # trace out all except qubit i: move axes
        axes=list(range(2*N))
        others=[j for j in range(N) if j!=i]+[N+j for j in range(N) if j!=i]
        tt=np.transpose(t,axes[:0]+[i]+others[:N-1]+[N+i]+others[N-1:]) if False else None
        # simpler: partial trace via reshape loop
        red=np.zeros((2,2),complex)
        idx=np.arange(dim)
        bi=(idx>>(N-1-i))&1
        rest=idx & ~(1<<(N-1-i))
        for x in range(dim):
            for y in range(dim):
                if rest[x]==rest[y]: red[bi[x],bi[y]]+=rho_g[x,y]
        marg.append(red)
    rho_marg=marg[0]
    for i in range(1,N): rho_marg=np.kron(rho_marg,marg[i])
    Eprep=float(np.trace(rho_marg@sector).real)-float(np.trace(rho_g@sector).real)
    # spectral S(t)
    rho_e=Uh.conj().T@rho@Uh; sec_e=Uh.conj().T@sector@Uh
    M=rho_e*sec_e.T
    gaps_all=(w[:,None]-w[None,:]).ravel(); vals_all=M.ravel()
    keep=np.abs(vals_all)>1e-12
    gaps_r=np.round(gaps_all[keep],9)
    ug,inv=np.unique(gaps_r,return_inverse=True)
    coeffs=np.zeros(len(ug),complex); np.add.at(coeffs,inv,vals_all[keep])
    def S(t): return float(np.sum(coeffs*np.exp(-1j*ug*t)).real)
    assert abs(S(0)+Eout)<1e-7
    ts=np.linspace(0,30,6001); vv=np.array([S(t) for t in ts])
    def cross(level):
        idx=np.where((vv[:-1]<level)&(vv[1:]>=level))[0]
        if len(idx)==0: return None
        i=int(idx[0]); return float(brentq(lambda t:S(t)-level,ts[i],ts[i+1],xtol=1e-12))
    t0=cross(0.0); tm=cross(Eprep)
    net=Eprep-Eout; neg=max(0.0,-net)
    return dict(N=N,m=m,r=r,E_out=Eout,E_prep_marg=Eprep,E_in=Ein,E_net_B=net,
                tau0=t0,tau_marg=tm,
                R_tau0=(neg*t0/COEFF if t0 else None), R_tau_marg=(neg*tm/COEFF if tm else None),
                ground_energy=float(w[0]))

if __name__=="__main__":
    args=sys.argv[1:]; triples=[tuple(map(float,args[i:i+3])) for i in range(0,len(args),3)]
    for (N,m,r) in triples:
        print(json.dumps(run(int(N),int(m),r)),flush=True)
