#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    for i, num in enumerate(my_list):
        new_list.append(my_list[i] if num != search else replace)
    return new_list
