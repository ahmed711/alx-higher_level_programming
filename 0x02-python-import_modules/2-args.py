#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    print("{:d} argument{}".format(len(argv) - 1, 's:' if len(argv) - 1 else '.')) 
    for i, arg in enumerate(argv[1:]):
        print("{}: {}".format(i + 1, arg))
