import json

from project.consts import COINAGE


def verify(module):
    func_name = "get_change"
    assert hasattr(
        module, func_name
    ), f"module {module.__name__} has no attribute {func_name}"

    get_change = getattr(module, func_name)
    assert callable(
        get_change
    ), f"entity {module.__name__}.{func_name} is not a function"

    dataset = (
        0,
        0.01,
        0.02,
        0.05,
        0.1,
        0.5,
        0.07,
        0.13,
        0.19,
        0.25,
        0.33,
        0.33,
        0.37,
        0.59,
        1,
        2,
        5,
        10,
        12.37,
        14.29,
        20,
        34.57,
        42.41,
        50,
        85.97,
        88.03,
        100,
        2454.37,
    )

    for expected in dataset:
        coinage = get_change(expected)
        pretty_coinage = pretty(coinage)
        verify_coinage(coinage, pretty_coinage)
        got = sum(amount * COINAGE[nominal] for nominal, amount in coinage.items())
        got /= 100
        assert (
            expected == got
        ), f"mismatch: {expected:.2f} decomposes to {pretty_coinage}"


def verify_coinage(coinage, pretty_coinage=None):
    if not pretty_coinage:
        pretty_coinage = pretty(coinage)
    for nominal, amount in coinage.items():
        assert isinstance(
            amount, int
        ), f"key '{nominal}' contains non-int value {amount} at {pretty_coinage}"


def pretty(coinage):
    return json.dumps(coinage, indent=4, sort_keys=True)


def test(modules_level05):
    for module in modules_level05.values():
        verify(module)
