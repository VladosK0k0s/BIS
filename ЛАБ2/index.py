#!/usr/bin/env python3

import random
from random import randrange
import math


def is_Prime_Miller_Raben(n, k):
    if n != int(n):
        return False
    n = int(n)
    if n == 0 or n == 1 or n == 4 or n == 6 or n == 8 or n == 9:
        return False

    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    s = 0
    d = n-1
    while d % 2 == 0:
        d >>= 1
        s += 1
    assert(2**s * d == n-1)

    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True

    for i in range(k):
        a = random.randrange(2, n)
        if trial_composite(a):
            return False

    return True


def is_Prime_Ferma(p, k):
    if p == 0 or p == 1 or p == 4 or p == 6 or p == 8 or p == 9:
        return False
    if p == 2 or p == 3 or p == 5 or p == 7:
        return True
    for i in range(k):
        if (pow(randrange(2, p-1), p-1, p) != 1):
            return False
    return True


def get_Prime(sign):
    if(sign < 1):
        return 1
    while True:
        n = randrange(10**(sign - 1), 10**(sign))
        k = math.floor(math.log(n, 2) + 1)
        if(is_Prime_Miller_Raben(n, k)):
            return n


def main():
    for i in range(5):
        n = get_Prime(i*10)
        print('Prime number: ', n)
        print('Miller_Raben: ', is_Prime_Miller_Raben(n, 1))
        print('Ferma: ', is_Prime_Ferma(n, 1))

    # for i in range(40):
    #     n = get_Prime(5)
    #     print('Prime number: ', n)
    #     print('Miller_Raben: ', is_Prime_Miller_Raben(n, 1))
    #     print('Ferma: ', is_Prime_Ferma(n, 1))


main()
