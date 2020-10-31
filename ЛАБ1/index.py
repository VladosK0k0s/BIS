#!/usr/bin/env python3

import time


def addTwoNumbers(a, b):
    return a + b


def multiplyTwoNumbers(a, b):
    return a * b


def subtractTwoNumbers(a, b):
    return a - b


def getSquare(a):
    return a**2


def getMod(a, b):
    return a % b


before = time.time()

print(addTwoNumbers(1111111111111111111111111111111111111111111111111111111111111111,
                    22222222222222222222222222222222222222222222222222222))
print(multiplyTwoNumbers(1111111111111111111111111111111111111111111111111111,
                         2222222222222222222222222222222222222222222222222))
# print(subtractTwoNumbers(1111111111111111111111111111111111111111111,
#                          2222222222222222222222222222222))
print(getSquare(1111111111111111111111111111111))
print(getMod(1000, 3))

after = time.time()

print(subtractTwoNumbers(after, before))
