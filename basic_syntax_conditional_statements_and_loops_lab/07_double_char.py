command = input()

while command != "End":
    if command != "SoftUni":
        string = ""
        for char in command:
            string += char * 2
        print(string)
    command = input()
    