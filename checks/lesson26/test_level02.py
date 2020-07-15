def verify(module):
    func_name = "rotate_left"

    assert hasattr(module, func_name)

    rotate_left = getattr(module, func_name)
    assert callable(rotate_left)

    lst0 = [1, 2, 3, 4, 5]
    lst1 = rotate_left(lst0, 8)
    assert lst1 == [4, 5, 1, 2, 3]
    assert lst0 is not lst1

    lst0 = [1, 2, 3, 4, 5]
    lst1 = rotate_left(lst0, 2)
    assert lst1 == [3, 4, 5, 1, 2]
    assert lst0 is not lst1

    lst1 = rotate_left(lst0, 1000 * len(lst0))
    assert lst1 == lst0
    assert lst1 is not lst0


def test(modules_level02):
    for module in modules_level02.values():
        verify(module)
