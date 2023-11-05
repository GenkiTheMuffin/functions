def rectangle(width: int, symbol="*"):
    print(symbol * width)
    print(symbol + " " * (width - 2) + symbol)
    print(symbol * width)


rectangle(5, "x")
rectangle(10)
