from project.consts import COINAGE


def get_change(mon):

    mon *= 100
    res = {}
    for note, val in sorted(COINAGE.items(), key=lambda pair: -pair[1]):
        count = int(mon / val)
        if count:
            res[note] = count
        mon -= count * val
    return res
