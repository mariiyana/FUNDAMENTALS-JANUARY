number_of_lines = int(input())

string = ""

for bracket in range(number_of_lines):
    line = input()

    if line == ")" or line == "(":
        string += line
string = string.replace("()", "")

if not string:
    print("BALANCED")
else:
    print("UNBALANCED")
