def triangle(height: int, symbol: str):
    for line in range(0, height):
        print((" ") * ((2 * height + 1) - (line * 2 + 1)),
              (symbol + " ") * ((line * 2) + 1))


triangle(3, "x")
