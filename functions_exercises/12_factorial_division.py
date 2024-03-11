import math


def factorial_number(a, b):
    a = math.factorial(a)
    b = math.factorial(b)
    return f"{(a / b):.2f}"


first_number = int(input())
second_number = int(input())
print(factorial_number(first_number, second_number))
