#!/usr/bin/python3

def no_c(my_string):
    no_c_in_str = ""
    for letter in my_string:
        if letter not in 'cC':
            no_c_in_str += letter
    return no_c_in_str
