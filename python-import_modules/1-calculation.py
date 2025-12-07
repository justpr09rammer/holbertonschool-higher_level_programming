#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

def add(a, b):
    return a + b
def sub(a, b):
   return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return int(a / b)

if __name__ == '__main__':
    a = 10
    b = 5
    print('{} + {} = {}'.format(a, b, add(a, b)))
    print('{} - {} = {}'.format(a, b, sub(a, b)))
    print('{} * {} = {}'.format(a, b, mul(a, b)))
    print('{} / {} = {}'.format(a, b, div(a, b)))
