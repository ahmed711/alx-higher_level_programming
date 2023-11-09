#!/usr/bin/python3

def common_elements(set_1, set_2):
    comman_set = set()
    for item in set_1:
        if item in set_2:
            comman_set.add(item)
    for item in set_2:
        if item in set_1 and item not in comman_set:
            comman_set.add(item)
    return comman_set
