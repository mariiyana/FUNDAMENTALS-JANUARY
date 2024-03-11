def palindrome_integers(num):
    result = ""

    for index in num:
        if str(index) == str(index)[::-1]:
            result += "True\n"
        else:
            result += "False\n"
    return result


number = list(map(int, input().split(", ")))
print(palindrome_integers(number))
