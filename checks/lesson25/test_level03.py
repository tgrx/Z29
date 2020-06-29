# pylint: disable=C0103,R0124

from collections import namedtuple

from . import test_level01 as regression01
from . import test_level02 as regression02


def verify_class_structure(klass):
    assert isinstance(klass, type)

    mro = klass.mro()
    assert len(mro) == 4
    assert mro[0] is klass
    regression02.verify_class_structure(mro[1])
    regression01.verify_class_structure(mro[2])
    assert mro[3] is object

    assert len(klass.__dict__) == 4
    assert "__init__" not in klass.__dict__
    assert "__eq__" in klass.__dict__


def verify_class_comparison(klass, **kwargs):
    user1 = klass(name=1, email=2, **kwargs)
    user2 = klass(name=2, email=2, **kwargs)
    user3 = klass(name=2, email=3, **kwargs)
    user4 = klass(name="ok", email=f"{'ok' * 10000}@ok.ok", **kwargs)
    user5 = klass(name="ok1", email=f"{'ok' * 10000}@ok.ok", **kwargs)

    assert user1 == user1
    assert user1 == user2

    assert user2 == user1
    assert user2 == user2

    assert user3 == user3

    assert user4 == user4
    assert user4 == user5

    assert user5 == user4
    assert user5 == user5

    assert not user1 == user3
    assert not user1 == user4
    assert not user1 == user5

    assert not user2 == user3
    assert not user2 == user4
    assert not user2 == user5

    assert not user3 == user1
    assert not user3 == user2
    assert not user3 == user4
    assert not user3 == user5

    assert not user4 == user1
    assert not user4 == user2
    assert not user4 == user3

    assert not user5 == user1
    assert not user5 == user2
    assert not user5 == user3

    assert not user1 == 2
    assert not 2 == user2  # pylint: disable=C0122
    assert not 3 == user3  # pylint: disable=C0122

    c = namedtuple("C", ["email"])(2)
    assert not user1 == c


def verify_class(klass):
    verify_class_structure(klass)
    regression02.verify_class_init(klass)
    verify_class_comparison(klass)


def verify_module(module):
    class_name = "User"
    assert hasattr(module, class_name)

    User = getattr(module, class_name)
    verify_class(User)


def test(modules_level03):
    for module in modules_level03.values():
        verify_module(module)
