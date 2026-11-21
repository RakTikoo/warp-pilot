from verify_finalist import main
cfg = {'M': 2.7, 'kind': 'edgepeaked', 'params': {'wd': 3.0, 'floor': 0.2},
       'sr': 2.0, 'sp': 1.16, 'beta_w': 0.03, 'shift_kind': 'cos', 'ws': [10.0, 20.0]}
main(cfg, 'B2_M2.7_b0.03')
