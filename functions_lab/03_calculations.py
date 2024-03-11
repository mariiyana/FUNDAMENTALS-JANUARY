in_operator = input()
first_number = int(input())
second_number = int(input())


def calculation(first_num, second_num, operator):
    result = 0
    if operator == "multiply":
        result = first_number * second_number
    elif operator == "divide":
        result = first_number // second_number
    elif operator == "add":
        result = first_number + second_number
    elif operator == "subtract":
        result = first_number - second_number

    return result


print(calculation(first_number, second_number, in_operator))
