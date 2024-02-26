number = int(input())

for prime_number in range(2, number):
    if number % prime_number == 0:
        print("False")
        break
else:
    print("True")
