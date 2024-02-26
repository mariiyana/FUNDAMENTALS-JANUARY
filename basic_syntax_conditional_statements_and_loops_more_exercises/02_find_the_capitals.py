string = input()
capital_letters = []

for index in range(len(string)):
    if string[index].isupper():
        capital_letters.append(index)
print(capital_letters)
