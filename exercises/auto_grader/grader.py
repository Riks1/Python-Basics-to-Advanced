# exercises/auto_grader/grader.py
import subprocess
import sys
from pathlib import Path

def run_tests(exercise_path: Path):
    print(f"Running pytest in {exercise_path}")
    cmd = [sys.executable, "-m", "pytest", "-q", str(exercise_path)]
    proc = subprocess.run(cmd)
    return proc.returncode

if __name__ == "__main__":
    path = Path("exercises/auto_grader/sample_exercises/reverse_string")
    rc = run_tests(path)
    if rc == 0:
        print("All tests passed ✅")
    else:
        print("Some tests failed ❌")
    sys.exit(rc)
