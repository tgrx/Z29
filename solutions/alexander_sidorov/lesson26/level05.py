from project.consts import COINAGE

_coinage_reversed = {_value: _coin for _coin, _value in COINAGE.items()}


def get_change(amount):
    rest = int(amount * 100)
    coinage = {}

    while rest:
        nominal, name = max(
            (value, name) for value, name in _coinage_reversed.items() if value <= rest
        )
        items, rest = divmod(rest, nominal)
        coinage[name] = items

    return coinage
