def rotate_left(lis, elem):
    if elem > len(lis):
        elem = elem % len(lis)
    return lis[elem:] + lis[:elem]
