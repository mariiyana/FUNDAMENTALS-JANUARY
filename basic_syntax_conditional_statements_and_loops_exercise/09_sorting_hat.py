command = input()
house = ""

while command != "Welcome!":
    if command == "Voldemort":
        print("You must not speak of that name!")
        break

    length = len(command)
    if length < 5:
        house = "Gryffindor"
    elif length == 5:
        house = "Slytherin"
    elif length == 6:
        house = "Ravenclaw"
    elif length > 6:
        house = "Hufflepuff"
    print(f"{command} goes to {house}.")
    command = input()

if command == "Welcome!":
    print("Welcome to Hogwarts.")
