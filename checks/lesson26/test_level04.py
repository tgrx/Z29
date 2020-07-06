import string

from scipy.stats import pearsonr


def correlate(collection1, collection2):
    def _conv(_v):
        if isinstance(_v, str):
            return ord(_v)
        return _v

    converted1 = [_conv(_e) for _e in collection1]
    converted2 = [_conv(_e) for _e in collection2]

    _r, _p = pearsonr(converted1, converted2)
    return abs(_r)


def verify(module):
    func_name = "key"
    assert hasattr(
        module, func_name
    ), f"module {module.__name__} has no attribute {func_name}"

    key = getattr(module, func_name)
    assert callable(key), f"entity {module.__name__}.{func_name} is not a function"

    dataset = (
        "".join(_letter * 1000 for _letter in string.ascii_lowercase),
        list(range(100000)),
        range(100000),
        tuple(range(100000)),
    )

    for data in dataset:
        expected = sorted(data)
        got = sorted(data, key=key)
        corr = correlate(expected, got)
        assert corr < 0.1, f"sort mismatch on data `{data[:10]}...`"


def test(modules_level04):
    for module in modules_level04.values():
        verify(module)
