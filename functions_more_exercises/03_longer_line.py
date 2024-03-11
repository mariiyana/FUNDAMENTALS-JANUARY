import math


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    if abs(x1) + abs(y1) + abs(x2) + abs(y2) > abs(x3) + abs(y3) + abs(x4) + abs(y4):
        first = abs(x1) + abs(y1)
        second = abs(x2) + abs(y2)
        if first <= second:
            return f"({math.floor(x1)}, {math.floor(y1)})({math.floor(x2)}, {math.floor(y2)})"
        else:
            return f"({math.floor(x2)}, {math.floor(y2)})({math.floor(x1)}, {math.floor(y1)})"
    elif abs(x1) + abs(y1) + abs(x2) + abs(y2) < abs(x3) + abs(y3) + abs(x4) + abs(y4):
        first = abs(x3) + abs(y3)
        second = abs(x4) + abs(y4)
        if first <= second:
            return f"({math.floor(x3)}, {math.floor(y3)})({math.floor(x4)}, {math.floor(y4)})"
        else:
            return f"({math.floor(x4)}, {math.floor(y4)})({math.floor(x3)}, {math.floor(y3)})"
    elif abs(x1) + abs(y1) + abs(x2) + abs(y2) == abs(x3) + abs(y3) + abs(x4) + abs(y4):
        return f"({math.floor(x1)}, {math.floor(y1)})({math.floor(x2)}, {math.floor(y2)})"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())
print(longer_line(x1, y1, x2, y2, x3, y3, x4, y4))
