#!/usr/bin/python3
low = list(range(122, 96, -2))
up = list(range(89, 64, -2))
for c_low, c_up in zip(low, up):
    print("{0:c}{1:c}".format(c_low, c_up), end="")
