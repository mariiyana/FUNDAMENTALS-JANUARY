string = input()
animal_lst = string.split(", ")

wolf_index = animal_lst.index("wolf")
if wolf_index == len(animal_lst) - 1:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {len(animal_lst) - 1 - wolf_index}! You are about to be eaten by a wolf!")
