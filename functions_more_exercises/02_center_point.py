import math


def center_point(x1, y1, x2, y2):
    first_distance = abs(x1) + abs(y1)
    second_distance = abs(x2) + abs(y2)

    if first_distance <= second_distance:
        return f"({math.floor(x1)}, {math.floor(y1)})"
    else:
        return f"({int(x2)}, {int(y2)})"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(center_point(x1, y1, x2, y2))
