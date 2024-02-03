groups_size = int(input())
days = int(input())

coins = 0

for current_day in range(1, days + 1):
    if current_day % 10 == 0:
        groups_size -= 2
    if current_day % 15 == 0:
        groups_size += 5
    if current_day % 3 == 0:
        coins -= 3 * groups_size
    if current_day % 5 == 0:
        coins += 20 * groups_size
        if current_day % 3 == 0:
            coins -= 2 * groups_size
    coins += 50
    coins -= 2 * groups_size
coins_per_person = coins // groups_size
print(f"{groups_size} companions received {coins_per_person} coins each.")
