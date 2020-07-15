def rotate_left(lvl, num):
    num = num % len(lvl)
    return lvl[num:] + lvl[:num]
