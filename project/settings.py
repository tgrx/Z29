from pathlib import Path

Z29 = Path(__file__).parent.parent.resolve()

SOLUTIONS: Path = Z29 / "solutions"
CHECKS: Path = Z29 / "checks"

assert SOLUTIONS.is_dir(), f"SOLUTIONS: {SOLUTIONS.as_posix()} is not a dir"
assert CHECKS.is_dir(), f"CHECKS: {CHECKS.as_posix()} is not a dir"
