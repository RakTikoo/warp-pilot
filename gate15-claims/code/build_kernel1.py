"""Builder for g15_wb2_kernel.py (Gate-15, W-B2 completion kernel).
Assembles: header + embedded gate data (zlib/base85) + Gate-15's own
W-B2 modules (path prefix rewritten, counts asserted) + driver_wb2.py.
Text processing only — runs no gate computation.
"""
import base64, hashlib, json, os, zlib

G15 = os.path.expanduser("~/workspace/warp-pilot/gate15")
WB2 = os.path.join(G15, "work_b2")
KAG = os.path.join(G15, "kaggle")
PREFIX = "/home/hatch/workspace/warp-pilot/gate15/work_b2/"

def b85_of_bytes(b):
    return base64.b85encode(zlib.compress(b, 9)).decode()

def b85_of_json(path):
    with open(path, "rb") as fh:
        return b85_of_bytes(fh.read())

def sha(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()

modules = {}
rewrite_counts = {}
for fname in ("wb2_kernels.py", "wb2_functionals.py", "wb2_a1_patch.py",
              "wb2_source.py", "wb2_second.py"):
    with open(os.path.join(WB2, fname)) as fh:
        src = fh.read()
    n = src.count(PREFIX)
    src = src.replace(PREFIX, "g15_home/")
    rewrite_counts[fname] = n
    modules[fname] = b85_of_bytes(src.encode())
assert rewrite_counts == {"wb2_kernels.py": 0, "wb2_functionals.py": 1,
                          "wb2_a1_patch.py": 1, "wb2_source.py": 1,
                          "wb2_second.py": 1}, rewrite_counts

build_info = {
    "built": "2026-11-23",
    "builder": "gate15/kaggle/build_kernel1.py",
    "path_rewrite": f"{PREFIX} -> g15_home/ (relative), counts per module asserted",
    "rewrite_counts": rewrite_counts,
    "module_sha256_home_originals": {f: sha(os.path.join(WB2, f)) for f in modules},
    "data_sha256": {
        "wb1_basis_jets.json": sha(os.path.join(G15, "results/wb1_basis_jets.json")),
        "wb2_functionals_home.json": sha(os.path.join(WB2, "wb2_functionals.json")),
        "wb2_source_home.json": sha(os.path.join(WB2, "wb2_source.json")),
    },
    "pins": {"mpmath": "1.3.0", "sympy": "1.14.0", "numpy": "2.5.5", "scipy": "1.18.1"},
}

header = '''# GATE-15 KERNEL 1 — W-B2 COMPLETION (see driver docstring below).
# Self-contained Kaggle kernel (CPU session, Internet OFF). Launch is
# the parent agent's action; results are provisional until re-judged
# at home in a fresh process. pip pins (home venv versions):
#   mpmath==1.3.0 sympy==1.14.0 numpy==2.5.5 scipy==1.18.1
import base64, json, os, zlib

def _load(lit):
    return json.loads(zlib.decompress(base64.b85decode(lit.encode())).decode())

def _text(lit):
    return zlib.decompress(base64.b85decode(lit.encode())).decode()

FUNC_HOME = _load("""FUNC_LIT""")
SRC_HOME = _load("""SRC_LIT""")
BASIS_JETS = _load("""BASIS_LIT""")
BUILD_INFO = json.loads("""BUILD_JSON""")
_MODULES = {
'''
for fname, lit in modules.items():
    header += f'    "{fname}": """{lit}""",\n'
header += '''}
os.makedirs("g15_home", exist_ok=True)
for _n, _lit in _MODULES.items():
    with open(os.path.join("g15_home", _n), "w") as _fh:
        _fh.write(_text(_lit))

'''

header = (header
          .replace("FUNC_LIT", b85_of_json(os.path.join(WB2, "wb2_functionals.json")))
          .replace("SRC_LIT", b85_of_json(os.path.join(WB2, "wb2_source.json")))
          .replace("BASIS_LIT", b85_of_json(os.path.join(G15, "results/wb1_basis_jets.json")))
          .replace("BUILD_JSON", json.dumps(build_info).replace("\\", "\\\\").replace('"""', '\\"\\"\\"')))

with open(os.path.join(KAG, "driver_wb2.py")) as fh:
    driver = fh.read()

out = os.path.join(KAG, "g15_wb2_kernel.py")
with open(out, "w") as fh:
    fh.write(header + driver)
print("wrote", out, os.path.getsize(out), "bytes")
print("rewrite counts:", rewrite_counts)
