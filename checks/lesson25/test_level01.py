# pylint: disable=C0103

import pytest


def verify_class_structure(user_class):
    assert isinstance(user_class, type)
    assert user_class.mro() == [user_class, object]
    assert len(user_class.__dict__) == 4
    assert hasattr(user_class, "__init__")
    assert "__init__" not in user_class.__dict__


def verify_class_init(user_class):
    with pytest.raises(TypeError):
        user_class(1)
    with pytest.raises(TypeError):
        user_class(1, 2)
    with pytest.raises(TypeError):
        user_class(name=1)
    with pytest.raises(TypeError):
        user_class(email=1)

    user = user_class()
    assert user.__dict__ == {}


def verify_class(klass):
    verify_class_structure(klass)
    verify_class_init(klass)


def verify_module(module):
    class_name = "User"
    assert hasattr(module, class_name)

    User = getattr(module, class_name)
    verify_class(User)


def test(modules_level01):
    for module in modules_level01.values():
        verify_module(module)
