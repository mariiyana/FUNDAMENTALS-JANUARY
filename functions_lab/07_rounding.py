def rounding():
    numbers = input().split()
    rounded_numbers = []
    for num in numbers:
        rounded_numbers.append(round(float(num)))
    return rounded_numbers


print(rounding())
