# pylint: disable=C0103,C0122


def verify_class_structure(klass):
    assert isinstance(klass, type)
    assert klass.mro() == [klass, object]
    class_attrs = {
        "__init__",
        "__str__",
        "__truediv__",
    }
    for class_attr in class_attrs:
        assert hasattr(
            klass, class_attr
        ), f'class {klass} does not have an attr "{class_attr}"'


def verify_class_logic(klass):
    p1 = klass("")
    assert "" == str(p1)

    p2 = klass(".")
    assert "." == str(p2)

    p3 = klass("x")
    assert "x" == str(p3)

    p4 = p2 / p3
    assert "./x" == str(p4)

    p5 = p3 / p1 / p2
    assert "x/." == str(p5)


def verify_class(klass):
    verify_class_structure(klass)
    verify_class_logic(klass)


def verify_module(module):
    class_name = "Path"
    assert hasattr(module, class_name)

    klass = getattr(module, class_name)
    verify_class(klass)


def test(modules_level04):
    for module in modules_level04.values():
        verify_module(module)
