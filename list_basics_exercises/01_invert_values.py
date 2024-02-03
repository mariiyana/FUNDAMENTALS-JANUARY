number = input().split()
opposite_numbers = []

for opposite in number:
    opposite_num = -int(opposite)
    opposite_numbers.append(opposite_num)
print(opposite_numbers)
