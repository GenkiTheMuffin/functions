def sun_time(h: int, m: int):
    res = 180 / 12 * (h - 6) + (180 / 720 * m)
    return res


print(sun_time(12, 0))
print(sun_time(9, 50))
