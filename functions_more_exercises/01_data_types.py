def data_types(data_type, num):
    if data_type == "int":
        number = int(num)
        return number * 2
    elif data_type == "real":
        result = float(num) * 1.5
        return f"{result:.2f}"
    elif data_type == "string":
        return f"${num}$"


data_type = input()
num = input()
print(data_types(data_type, num))
