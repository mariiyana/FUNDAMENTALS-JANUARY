def min_max_sum(num):
    numbers = list(map(int, num.split()))
    min_number = min(numbers)
    max_number = max(numbers)
    total_sum = sum(numbers)
    return f"The minimum number is {min_number}"\
           f"\nThe maximum number is {max_number}" \
           f"\nThe sum number is: {total_sum}"


number = input()
print(min_max_sum(number))
