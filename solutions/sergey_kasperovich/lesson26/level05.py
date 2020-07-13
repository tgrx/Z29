from project.consts import COINAGE


def get_change(amount):
    result = {}
    amount *= 100
    for coin_name, coin_value in sorted(COINAGE.items(), key=lambda pair: -pair[1]):
        count = int(amount // coin_value)
        result[coin_name] = count
        amount -= count * coin_value
    return result
