from math import atan2, radians, sin, cos, sqrt

# import livmap


def distance_between_coords(lat1: float, long1: float, lat2: float, long2: float):
    radius = 6371
    lat1 = radians(lat1)
    long1 = radians(long1)
    lat2 = radians(lat2)
    long2 = radians(long2)
    dlat = abs(lat2 - lat1)
    dlong = abs(long2 - long1)
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlong / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = radius * c
    return distance


print(distance_between_coords(37.7749, -122.4194, 34.0522, -118.2437))
