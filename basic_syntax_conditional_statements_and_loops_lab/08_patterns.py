number = int(input())

for first_half in range(1, number + 1):
    print(first_half * "*")
for second_half in range(number - 1, 0, -1):
    print(second_half * "*")
