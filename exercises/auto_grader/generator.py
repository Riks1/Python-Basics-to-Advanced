# exercises/auto_grader/generator.py
import os
from pathlib import Path
from textwrap import dedent

PROBLEM_TEMPLATE = dedent("""\
# {title}

Difficulty: {difficulty}

## Problem
{description}

## Example
Input:
{example_input}

Output:
{example_output}
""")

SOLUTION_TEMPLATE = dedent("""\
# Hidden/reference solution for {title}
def solve(x: str) -> str:
    \"\"\"Reference implementation.\"\"\"
    return x[::-1]
""")

TEST_TEMPLATE = dedent("""\
import importlib.util
from pathlib import Path

def import_solution(path):
    spec = importlib.util.spec_from_file_location("solution", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def test_examples():
    sol = import_solution(Path(__file__).parent / "solution.py")
    assert sol.solve({example_input!r}) == {example_output!r}
""")

def create_reverse_string(dirpath):
    dirpath = Path(dirpath)
    dirpath.mkdir(parents=True, exist_ok=True)

    (dirpath / "problem.md").write_text(PROBLEM_TEMPLATE.format(
        title="Reverse a String",
        difficulty="Beginner",
        description="Given a string, return the reverse of the string.",
        example_input="hello",
        example_output="olleh"
    ))

    (dirpath / "solution.py").write_text(SOLUTION_TEMPLATE.format(title="Reverse a String"))

    (dirpath / "test_solution.py").write_text(TEST_TEMPLATE.format(example_input="hello", example_output="olleh"))

if __name__ == "__main__":
    create_reverse_string("exercises/auto_grader/sample_exercises/reverse_string")
    print("Sample exercise created.")
