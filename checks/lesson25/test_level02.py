# pylint: disable=C0103

import pytest

from . import test_level01 as regression01


def verify_class_structure(klass):
    assert isinstance(klass, type)

    mro = klass.mro()
    assert len(mro) == 3
    assert mro[0] is klass
    regression01.verify_class(mro[1])
    assert mro[2] is object

    assert len(klass.__dict__) == 3
    assert "__init__" in klass.__dict__


def verify_class_init(klass):
    with pytest.raises(TypeError):
        klass()
    with pytest.raises(TypeError):
        klass(1)
    with pytest.raises(TypeError):
        klass(name=1)
    with pytest.raises(TypeError):
        klass(email=1)
    with pytest.raises(TypeError):
        klass(1, name=1, email=2)
    with pytest.raises(TypeError):
        klass(1, 2, name=1, email=2)
    with pytest.raises(TypeError):
        klass(1, 2, 3)
    with pytest.raises(TypeError):
        klass(1, 2, phone=3)
    with pytest.raises(TypeError):
        klass(name=1, email=2, phone=3)

    user1 = klass(name=1, email=2)
    assert user1.__dict__ == {"name": 1, "email": 2}

    user2 = klass(name=2, email=2)
    assert user2.__dict__ == {"name": 2, "email": 2}

    user3 = klass(name=2, email=3)
    assert user3.__dict__ == {"name": 2, "email": 3}

    user = klass(name=False, email=None)
    assert user.__dict__ == {"name": False, "email": None}

    user = klass(name="ok", email="ok@ok.ok")
    assert user.__dict__ == {"name": "ok", "email": "ok@ok.ok"}


def verify_class(klass):
    verify_class_structure(klass)
    verify_class_init(klass)


def verify_module(module):
    class_name = "User"
    assert hasattr(module, class_name)

    User = getattr(module, class_name)
    verify_class(User)


def test(modules_level02):
    for module in modules_level02.values():
        verify_module(module)
