#!/usr/bin/env python3


def gcd(a: int, b: int):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def lcm(a: int, b: int):
    result = abs(a * b) // gcd(a, b)
    return result


print(lcm(12, 10))
