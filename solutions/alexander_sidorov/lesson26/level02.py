def rotate_left(lst, revs):
    result = lst[:]

    if len(result) < 2:
        return result

    for _ in range(revs):
        result.append(result[0])
        result.pop(0)

    return result
