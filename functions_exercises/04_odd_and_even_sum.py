def odd_or_even(number):
    odd = 0
    even = 0

    for digit in str(number):
        if int(digit) % 2 == 0:
            even += int(digit)
        else:
            odd += int(digit)

    return f"Odd sum = {odd}, Even sum = {even}"


number = int(input())
print(odd_or_even(number))
