#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = '-' if number < 0 else ''
if abs(number % 10) == 0:
    num_cond = "and is 0"
elif abs(number % 10) < 6:
    num_cond = "and is less than 6 and not 0"
else:
    num_cond = "and is greater than 5"
print(f"Last digit of {number:d} is {sign}{abs(number) % 10:d} and is {num_cond}") 
