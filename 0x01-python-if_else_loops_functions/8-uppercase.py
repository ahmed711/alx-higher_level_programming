#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        asciiVal = ord(letter)
        if 97 <= asciiVal <= 122:
            asciiVal -= 32
        print("{0:c}".format(asciiVal), end="")
    print("")
