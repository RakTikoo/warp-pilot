"""
P21-2 derive: symbolic deciding identities, from p212_lib (action variation).
Writes results/p212_identities.json.  No scan numbers are produced here.
"""
import json, os
import sympy as sp
import p212_lib as lib

out = {}
Tp, Fphys, Gphys, (LF, LG, L0), (E, B) = lib.derive_T()
out['F_phys'] = str(Fphys)          # expect 2*(B^2 - E^2) up to form
out['G_phys'] = str(Gphys)          # expect 4*E*B
rho = -Tp['t']; pr = Tp['r']; pt = Tp['th']
out['rho_expr'] = str(sp.simplify(rho))
out['pr_expr'] = str(sp.simplify(pr))
out['pt_expr'] = str(sp.simplify(pt))
out['Tph_eq_Tth'] = bool(sp.simplify(Tp['ph'] - Tp['th']) == 0)

# IDENTITY I1: T^t_t - T^r_r for GENERAL L(F,G), dyonic ansatz.
diff = sp.simplify(Tp['t'] - Tp['r'])
out['I1_Tt_minus_Tr_general_LFG'] = str(diff)
out['I1_is_zero'] = bool(diff == 0)
# I1b: same for L(F) only (L_G = 0).
out['I1_LFonly_is_zero'] = bool(sp.simplify(diff.subs(LG, 0)) == 0)

# NEC expressions
out['NEC1_expr'] = str(sp.simplify(rho + pr))
out['NEC2_expr'] = str(sp.simplify(rho + pt))

# Maxwell validation: L0 -> F, LF -> 1, LG -> 0, F = 2(B^2 - E^2)
Fexpr = 2*(B**2 - E**2)
mx = {L0: Fexpr, LF: 1, LG: 0}
out['maxwell_rho_ok'] = bool(sp.simplify(rho.subs(mx) - (E**2 + B**2)/(2*sp.pi)) == 0)
out['maxwell_pr_ok'] = bool(sp.simplify(pr.subs(mx) + (E**2 + B**2)/(2*sp.pi)) == 0)
out['maxwell_pt_ok'] = bool(sp.simplify(pt.subs(mx) - (E**2 + B**2)/(2*sp.pi)) == 0)
tr = sp.simplify((-rho + pr + 2*pt).subs(mx))
out['maxwell_traceless'] = bool(tr == 0)

# Magnetic L(F) identities: E=0, LG=0.  F = 2 B^2.
mag = {E: 0, LG: 0}
Fm = 2*B**2
out['mag_NEC2_minus_FLF_over_2pi'] = str(sp.simplify(
    (rho + pt).subs(mag).subs(L0, L0) - Fm*LF/(2*sp.pi)))
# (rho+pt) at E=0 still contains L0; identity NEC2 = F L_F/(2pi) requires
# substituting nothing else: check symbolic difference after expressing
# pt,rho fully (they contain L0 which cancels in rho+pt).
out['mag_NEC2_identity_zero'] = bool(sp.simplify(
    (rho + pt).subs(mag) - Fm*LF/(2*sp.pi)) == 0)
out['mag_rho'] = str(sp.simplify(rho.subs(mag)))     # expect L/(4pi)
out['mag_pr'] = str(sp.simplify(pr.subs(mag)))       # expect -L/(4pi)
out['mag_pt'] = str(sp.simplify(pt.subs(mag)))       # expect (2 F L_F - L)/4pi
out['mag_SEC_expr'] = str(sp.simplify((rho + pr + 2*pt).subs(mag)))
out['mag_DECt_expr'] = str(sp.simplify((rho - pt).subs(mag)))

# Born-Infeld partials + Maxwell limit
Lbi, LFbi, LGbi, Delta = lib.bi_partials()
out['BI_LF'] = str(LFbi)
out['BI_LG'] = str(LGbi)
out['BI_LF_matches_1_over_sqrtDelta'] = bool(
    sp.simplify(LFbi - 1/sp.sqrt(Delta)) == 0)
F, G, bb = sp.symbols('F G b', positive=True)
out['BI_LG_matches'] = bool(sp.simplify(
    LGbi - (-G/(4*bb**2*sp.sqrt(1 + F/(2*bb**2) - G**2/(16*bb**4))))) == 0)
ser = sp.series(Lbi.subs(G, 0), F, 0, 3).removeO()
out['BI_maxwell_series_Fonly'] = str(ser)   # expect F - F^2/(8 b^2) + ...
# Delta factorisation: Delta = (1 + B^2/b^2)(1 - E^2/b^2) on F=2(B^2-E^2), G=4EB
Dfac = sp.simplify(Delta.subs({F: 2*(B**2 - E**2), G: 4*E*B})
                   - (1 + B**2/bb**2)*(1 - E**2/bb**2))
out['BI_Delta_factorises'] = bool(Dfac == 0)

# BI dyonic NEC2 closed form: (rho+pt) with BI partials, F,G physical.
bi_subs = {LF: LFbi.subs({F: Fexpr, G: 4*E*B, bb: bb}),
           LG: LGbi.subs({F: Fexpr, G: 4*E*B, bb: bb}),
           L0: Lbi.subs({F: Fexpr, G: 4*E*B, bb: bb})}
# redo with consistent symbol: lib used 'b' inside bi_partials via symbols
out['BI_NEC2_expr'] = str(sp.simplify((rho + pt).subs(bi_subs)))
out['BI_rho_expr'] = str(sp.simplify(rho.subs(bi_subs)))
out['BI_pt_expr'] = str(sp.simplify(pt.subs(bi_subs)))
out['BI_NEC1_is_zero'] = bool(sp.simplify((rho + pr).subs(bi_subs)) == 0)

# Constitutive / excitation: q_e := sqrt(-g) H^{rt} / sin(th),
# H = L_F F + L_G *F  ->  q_e = r^2 (L_F E - L_G B)  [derived in lib docstring
# algebra; verified numerically in the scan against the closed BI form
# D = E sqrt(1+B^2/b^2)/sqrt(1-E^2/b^2)].
out['constitutive_qe_formula'] = 'q_e = r^2 (L_F * E - L_G * B)'

# Einstein combos: throat values -> DEC identity I3.
r, r0 = sp.symbols('r r0', positive=True)
combo_info = {}
for name, (phi_s, b_s) in lib.COMBOS.items():
    loc = {'r': r, 'r0': r0}
    phi_e = sp.sympify(phi_s, locals=loc); b_e = sp.sympify(b_s, locals=loc)
    rho_c, pr_c, pt_c = lib.einstein_combo(phi_e, b_e)
    bp0 = sp.simplify(sp.diff(b_e, r).subs(r, r0))
    def at_throat(expr):
        v = sp.simplify(expr.subs(r, r0))
        if v.has(sp.nan, sp.zoo):
            v = sp.simplify(sp.limit(expr, r, r0, '+'))
        return v
    rho0 = at_throat(rho_c)
    pr0 = at_throat(pr_c)
    combo_info[name] = {
        'bprime_r0': str(bp0),
        'rho_r0': str(rho0), 'pr_r0': str(pr0),
        'pt_r0': str(at_throat(pt_c)),
        'rho_expr': str(rho_c), 'pr_expr': str(pr_c), 'pt_expr': str(pt_c),
        # I3 check: 8 pi r0^2 rho(r0) == b'(r0) and 8 pi r0^2 pr(r0) == -1
        'I3_rho_matches_bprime': bool(sp.simplify(8*sp.pi*r0**2*rho0 - bp0) == 0),
        'I3_pr_is_minus_1': bool(sp.simplify(8*sp.pi*r0**2*pr0 + 1) == 0),
    }
out['combos'] = combo_info

os.makedirs('results', exist_ok=True)
with open('results/p212_identities.json', 'w') as f:
    json.dump(out, f, indent=1)
for k, v in out.items():
    if k != 'combos':
        print(k, '=', v)
for n, ci in combo_info.items():
    print(n, {k: ci[k] for k in ('bprime_r0', 'rho_r0', 'pr_r0', 'pt_r0',
                                 'I3_rho_matches_bprime', 'I3_pr_is_minus_1')})
