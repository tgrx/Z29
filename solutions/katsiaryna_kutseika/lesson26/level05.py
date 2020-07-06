from project.consts import COINAGE


def get_change(valuee):
    result = {}
    new_value = valuee * 100
    for note, value in sorted(COINAGE.items(), reverse=True, key=lambda i: i[1]):
        count = int(new_value / value)
        if count:
            result[note] = count
        new_value -= count * value
    return result
