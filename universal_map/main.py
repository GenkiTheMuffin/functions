def universal_map(A: int, B: int, C: int, D: int, x: int):
    y = (D * x - A * D - C * x + B * C) / (B - A)
    return y


print(universal_map(13, 425, 8, 14, 400))
