def compare_triplets(first, second):
    total_first = 0
    total_second = 0
    for i in range(3):
        if first[i] > second[i]:
            total_first += 1
        elif first[i] < second[i]:
            total_second += 1
    return total_first, total_second
