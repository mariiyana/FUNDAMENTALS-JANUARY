
def multiplication(a, b, c):
    sum_three_numbers = a + b + c
    if sum_three_numbers > 0:
        print("positive")
    if sum_three_numbers < 0:
        print("negative")
    if sum_three_numbers == 0:
        print("zero")


first_number = int(input())
second_number = int(input())
third_number = int(input())
multiplication(first_number, second_number, third_number)
