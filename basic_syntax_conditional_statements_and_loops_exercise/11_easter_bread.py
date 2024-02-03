budget = float(input())
price_for_kg_flour = float(input())

# recipe for one loaf
eggs_needed = 1
flour_needed = 1
milk_needed = 0.250

price_for_pack_of_eggs = price_for_kg_flour * 0.75
price_for_ltr_milk = price_for_kg_flour * 1.25

price_per_loaf = price_for_kg_flour * flour_needed\
                 + price_for_pack_of_eggs * eggs_needed\
                 + price_for_ltr_milk * milk_needed
number_of_loafs = int(budget // price_per_loaf)
money_left = budget - (price_per_loaf * number_of_loafs)

colored_eggs = 0

for loafs in range(1, int(number_of_loafs) + 1):
    colored_eggs += 3
    if loafs % 3 == 0:
        colored_eggs -= (loafs - 2)
print(f"You made {number_of_loafs} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")
