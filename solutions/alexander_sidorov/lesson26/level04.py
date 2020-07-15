from random import randint


def key(_arg):
    """
    Returns a random integer in [0, 2**64)
    Outgoing correlation between original and sorted ~ 2%
    Also have tried:
    * `hash(arg)`   17% correlation
    * `id(arg)`     98% correlation
    """
    return randint(0, 2 ** 64 - 1)


if __name__ == "__main__":
    print(key(1))
