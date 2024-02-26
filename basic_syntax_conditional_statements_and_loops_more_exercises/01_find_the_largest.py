number = input()
digits = []

for digit in str(number):
    digits.append(int(digit))
digits.sort(reverse=True)
largest_number = "".join(str(digit) for digit in digits)
print(largest_number)
