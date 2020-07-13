from project.consts import COINAGE


def get_change(amount):
    bills = {}
    amount *= 100
    for note, cost in sorted(COINAGE.items(), key=lambda i: -i[1]):
        number = int(amount // cost)
        bills[note] = number
        amount -= cost * number

    return bills
