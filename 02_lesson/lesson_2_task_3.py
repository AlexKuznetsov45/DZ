import math


def square(side_length):
    area = side_length**2
    if not isinstance(side_length, int):
        return math.ceil(area)
    else:
        return area


print(square(5))
