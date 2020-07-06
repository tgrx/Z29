def compare_triplets(tup_1, tup_2):
    coun_1, coun_2 = 0, 0
    for i, j in zip(tup_1, tup_2):
        if i > j:
            coun_1 += 1
        elif j > i:
            coun_2 += 1
    return coun_1, coun_2
