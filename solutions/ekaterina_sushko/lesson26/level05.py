from project.consts import COINAGE


def get_change(sum_for_billing):
    result = {}
    right_sum = sum_for_billing * 100
    for note, value in sorted(COINAGE.items(), key=lambda two: -two[1]):
        count = int(right_sum / value)
        if count:
            result[note] = count
        right_sum -= count * value

    return result
