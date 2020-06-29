import ast
import importlib.util
from collections import defaultdict
from pathlib import Path
from typing import Collection


def import_by_path(module_path: Path):
    package_name = ".".join(module_path.parts[-4:-1])
    module_name = module_path.name[:-3]

    spec = importlib.util.spec_from_file_location(
        f"{package_name}.{module_name}", module_path.as_posix()
    )
    module = importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)

    return module


class NameDetector(ast.NodeVisitor):
    def __init__(self, banned_names: Collection):
        self.__banned_names = frozenset(banned_names)
        if not self.__banned_names:
            raise TypeError("no banned names provided")

        self.__found_names = defaultdict(list)

    def visit_Name(self, node: ast.Name):
        if node.id in self.__banned_names:
            self.__found_names[node.id].append(node.lineno)

    @property
    def detected_violations(self):
        return bool(self.__found_names)

    def report(self, module=""):
        if module:
            module = f"({module}) "

        if not self.detected_violations:
            return f"{module}ok"

        msg = "; ".join(
            f"`{name}` at line{'s' if len(lines) > 1 else ''} {','.join(map(str, lines))}"
            for name, lines in sorted(self.__found_names.items())
        )

        return f"{module}detected usage of prohibited names: {msg}"


def verify_names(module, *names):
    loader = module.__loader__
    py_file = Path(loader.path)
    py_file.resolve()

    with py_file.open() as src:
        tree = ast.parse(src.read())

    detector = NameDetector(names)
    detector.visit(tree)

    assert not detector.detected_violations, detector.report(py_file.as_posix())
