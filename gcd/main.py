#!/usr/bin/env python3


def gcd(a: int, b: int):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


print(gcd(128, 28))
