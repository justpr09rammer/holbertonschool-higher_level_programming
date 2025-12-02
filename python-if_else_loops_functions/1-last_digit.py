#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)
if number != 0:
    last_digit = int(abs(number) / 10**int(math.log10(abs(number)))) % 10
    if number < 0:
        last_digit *= -1
else:
    last_digit = 0
if last_digit > 5:
    msg = f'Last digit of {number} is {last_digit} and is greater than 5'
elif last_digit < 6 and last_digit != 0:
    msg = f'Last digit of {number} is {last_digit} and is less than 6 and not 0'
else:  # last_digit == 0
    msg = f'Last digit of {number} is {last_digit} and is 0'
print(msg)
