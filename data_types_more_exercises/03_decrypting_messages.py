key = int(input())
number_of_lines = int(input())

for index in range(number_of_lines):
    message = input()
    x = (ord(message) + key)
    print(chr(x), end="")
