#!/usr/bin/python3
"""
a function that prints file content
"""


def read_file(filename=""):
    """ read file content """
    with open(filename, encoding="UTF-8") as f:
        read_data = f.read()
    print(read_data, end="")
