def max(a: int, b: int):
    average = (a + b) / 2
    result = average + 0.5 * abs((a - b))
    return result


def min(a: int, b: int):
    average = (a + b) / 2
    result = average - 0.5 * abs((a - b))
    return result


print(max(12, 85))
print(min(12, 85))
