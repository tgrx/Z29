from project.consts import COINAGE


def get_change(amount):
    result = {}
    xxx = amount * 100
    for coin_name, coin_value in sorted(COINAGE.items(), key=lambda pair: -pair[1]):
        count = int(xxx / coin_value)
        if count:
            result[coin_name] = count
        xxx -= count * coin_value
    return result
