import mpmath as mp
mp.mp.dps=30
lP=mp.mpf('1.616e-35')
for ell in ['1.0','0.1']:
    e=mp.mpf(ell); print('ell',ell,'ell^2/lP^2=', mp.nstr(e**2/lP**2,4))
Nreq=mp.mpf('1.06e72')
for cap in ['3.8e69','3.8e67']:
    c=mp.mpf(cap); print('shortfall vs',cap,'=', mp.nstr(mp.log10(Nreq/c),4),'orders; ratio',mp.nstr(Nreq/c,3))
MP=mp.mpf('1.22e28') # eV
for N in ['1e72','1.06e72','1.06e73']:
    n=mp.mpf(N); print('Lambda N=',N, mp.nstr(MP/mp.sqrt(n),4),'eV')
# La line: Nreq scales x10
print('L=a Nreq =', mp.nstr(Nreq*10,3))
# Planck length check value used: 1.616255e-35 gives?
lP2=mp.mpf('1.616255e-35'); print('with CODATA lP, 1m:', mp.nstr(1/lP2**2,4), ' 0.1m:', mp.nstr(mp.mpf('0.01')/lP2**2,4))
