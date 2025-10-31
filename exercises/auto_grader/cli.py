# exercises/auto_grader/cli.py
import sys
from pathlib import Path
from generator import create_reverse_string

USAGE = "Usage: python cli.py new <exercise-name>"

def main(args):
    if len(args) < 2:
        print(USAGE); return
    cmd = args[0]
    name = args[1]
    if cmd == "new":
        target = Path("exercises/auto_grader/sample_exercises") / name
        create_reverse_string(target)
        print(f"Created exercise: {target}")
    else:
        print(USAGE)

if __name__ == "__main__":
    main(sys.argv[1:])
