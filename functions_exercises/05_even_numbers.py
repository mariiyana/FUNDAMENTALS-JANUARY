def even_num(num):
    return num % 2 == 0


def get_even_num(num):
    numbers = list(map(int, num.split()))
    even_numbers = list(filter(even_num, numbers))
    return even_numbers


number = input()
print(get_even_num(number))
