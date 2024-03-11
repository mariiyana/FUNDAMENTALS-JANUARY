def get_sorted_num(num):
    numbers = list(map(int, num.split()))
    sorted_num = list(sorted(numbers))
    return sorted_num


number = input()
print(get_sorted_num(number))
