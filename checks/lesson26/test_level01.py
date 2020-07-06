def verify(module):
    func_name = "compare_triplets"

    assert hasattr(module, func_name)

    compare_triplets = getattr(module, func_name)
    assert callable(compare_triplets)

    assert compare_triplets((1, 0, 1), (0, 1, 0)) == (2, 1)
    assert compare_triplets((1, 1, 1), (0, 1, 0)) == (2, 0)


def test(modules_level01):
    for module in modules_level01.values():
        verify(module)
