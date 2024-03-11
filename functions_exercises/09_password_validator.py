def valid_password(password):
    result = ""

    if not 6 <= len(password) <= 10:
        result += "Password must be between 6 and 10 characters\n"
    elif not password.isalnum():
        result += "Password must consist only of letters and digits\n"
    elif sum(char.isdigit() for char in password) < 2:
        result += "Password must have at least 2 digits\n"
    else:
        result += "Password is valid\n"

    return result


user_password = input()
print(valid_password(user_password))
