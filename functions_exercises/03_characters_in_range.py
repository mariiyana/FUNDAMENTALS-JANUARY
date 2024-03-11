def chars_range(char1, char2):
    result = ""

    for index in range(ord(char1) + 1, ord(char2)):
        result += chr(index) + " "

    return result


first_char = input()
second_char = input()
print(chars_range(first_char, second_char))
