def compare_triplets(first_triple, second_triple):
    counter_first = 0
    counter_second = 0
    for i in range(3):
        if first_triple[i] > second_triple[i]:
            counter_first += 1
        elif first_triple[i] < second_triple[i]:
            counter_second += 1
    return counter_first, counter_second
