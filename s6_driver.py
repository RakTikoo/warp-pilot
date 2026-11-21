"""
s6_driver.py — S6: free-form superluminal ladder. Track P's
adversarial DE (PCHIP density/shift genes, re-randomised arbiters
at h and h/2 built in) at v in {1.1, 1.5, 2.0} on the best
geometry so far ((10,30) thick shell), M in {10, 20}.
Usage: python3 s6_driver.py BETA M
"""
import sys
import trackP

if __name__ == '__main__':
    beta = float(sys.argv[1]); M = float(sys.argv[2])
    rounds = int(sys.argv[3]) if len(sys.argv) > 3 else 2
    trackP.run_adversarial(beta, M, R1=10.0, R2=30.0, rounds=rounds,
                           maxiter=12, seed=5, tag='S6')
