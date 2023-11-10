def watch_hand_angle(h: int, m: int):
    minute_hand_angle = m * 6
    hour_hand_angle = 30 * h + 0.5 * m
    return abs(hour_hand_angle - minute_hand_angle)


print(watch_hand_angle(3, 45))
