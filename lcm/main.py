#!/usr/bin/env python3

def lcm(a: int, b: int):
    product = a * b
    while b != 0:
        a, b = b, a % b
    return product // a


print(lcm(12, 10))
