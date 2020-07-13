def compare_triplets(triplet1, triplet2):
    points1 = sum(i > j for i, j in zip(triplet1, triplet2))
    points2 = sum(i < j for i, j in zip(triplet1, triplet2))

    return points1, points2
