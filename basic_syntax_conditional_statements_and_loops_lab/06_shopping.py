budget = int(input())
command_prices = input()

while command_prices != "End":
    current_prices = int(command_prices)
    budget -= current_prices

    if budget < 0:
        print("You went in overdraft!")
        exit()
    command_prices = input()
else:
    print("You bought everything needed.")
