import importlib.util
from pathlib import Path

def import_solution(path):
    spec = importlib.util.spec_from_file_location("solution", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def test_examples():
    sol = import_solution(Path(__file__).parent / "solution.py")
    assert sol.solve("hello") == "olleh"
