from collections import deque


def rotate_left(collection, rotation):
    deque_for_rotation = deque(collection)
    deque_for_rotation.rotate(-rotation)
    final_list = list(deque_for_rotation)
    return final_list
