#!/usr/bin/env python3
"""Frame-admission probe: the gate's A2 anchor SET read,
run on whatever machine executes this file. Prints the
anchor minima as JSON. Used once, for the laptop-pool
admission control; no deciding read is taken from it."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import g41_lib as G  # noqa: E402

s, _ = G.set_read(1.0, None, None, None, 33)
print(json.dumps({'nec': s['nec']['min'], 'dec': s['dec']['min'],
                  'wec': s['wec']['min'], 'sec': s['sec']['min'],
                  'rho': s['rho']['min'],
                  'typeI_count': s['typeI_count']}))
