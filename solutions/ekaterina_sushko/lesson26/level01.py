def compare_triplets(first_triplet, second_triplet):
    total_first = 0
    total_second = 0
    for i in range(3):
        if first_triplet[i] > second_triplet[i]:
            total_first += 1
        elif first_triplet[i] < second_triplet[i]:
            total_second += 1
    return (
        total_first,
        total_second,
    )
