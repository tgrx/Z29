def verify(module):
    func_name = "key"
    assert hasattr(
        module, func_name
    ), f"module {module.__name__} has no attribute {func_name}"

    key = getattr(module, func_name)
    assert callable(key), f"entity {module.__name__}.{func_name} is not a function"

    dataset = (
        "yxz",
        [1, 2, 3, 4, 5],
        range(0, 100, 3),
        {1, 2, 3, 4, 5},
        {1: 5, 2: 4, 3: 3, 4: 2, 5: 1},
    )

    for data in dataset:
        expected = sorted(data)
        got = sorted(data, key=key)

        assert expected == got, f"sort mismatch on data `{data}`"


def test(modules_level03):
    for module in modules_level03.values():
        verify(module)
