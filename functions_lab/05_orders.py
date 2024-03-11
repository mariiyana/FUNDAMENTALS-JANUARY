product = input()
quantity = int(input())

products = {"coffee": 1.50, "water": 1.00, "coke": 1.40, "snacks": 2.00}


def calculations(product, quantity):
    if product == "coffee"\
            or product == "water"\
            or product == "coke"\
            or product == "snacks":
        return f"{products[product] * quantity:.2f}"


print(calculations(product, quantity))


# product = input()
# quantity = int(input())
#
# coffee = 1.50
# water = 1.00
# coke = 1.40
# snacks = 2.00
#
# price = 0
#
# if product == "coffee":
#     price = quantity * coffee
# elif product == "water":
#     price = quantity * water
# elif product == "coke":
#     price = quantity * coke
# elif product == "snacks":
#     price = quantity * snacks
#
# print(f"{price:.2f}")
