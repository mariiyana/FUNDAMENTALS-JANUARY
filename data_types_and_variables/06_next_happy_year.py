current_year = int(input())

while True:
    current_year += 1
    year_as_string = str(current_year)
    if len(year_as_string) == len(set(year_as_string)):
        break
print(current_year)
