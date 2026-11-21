from verify_finalist import main
cfgB = {'M': 2.4, 'kind': 'edgepeaked', 'params': {'wd': 3.0, 'floor': 0.2},
        'sr': 2.0, 'sp': 1.16, 'beta_w': 0.03, 'shift_kind': 'cos', 'ws': [10.0, 20.0]}
main(cfgB, 'B_M2.4_b0.03')
