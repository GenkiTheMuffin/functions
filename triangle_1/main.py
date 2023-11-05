def triangle(height: int, symbol: str):
    for line in range(0, height):
        for _ in range(0, line + 1):
            print(symbol, end=" ")
        print(" ")


def triangle_psycho(height: int, symbol: str):
    for line in range(0, height):
        print(symbol * (line + 1))


triangle_psycho(10, "x")
