def absolute_values():
    numbers = input().split()
    absolute_numbers = []
    for num in numbers:
        absolute_numbers.append(abs(float(num)))
    return absolute_numbers


print(absolute_values())
