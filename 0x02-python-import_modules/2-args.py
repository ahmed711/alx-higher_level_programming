#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    if len(argv) > 1:
        if len(argv) > 2:
            print("{:d} arguments:".format(len(argv) - 1))
        else:
            print("{:d} argument:".format(len(argv) - 1))
    else:
        print("{:d} arguments.".format(len(argv) - 1))
    for i, arg in enumerate(argv[1:]):
        print("{}: {}".format(i + 1, arg))
