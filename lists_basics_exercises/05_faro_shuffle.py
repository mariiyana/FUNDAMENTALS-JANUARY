deck_cards = input().split()
shuffles_count = int(input())

for shuffle in range(shuffles_count):
    middle_part = len(deck_cards) // 2
    left_part = deck_cards[:middle_part]
    right_part = deck_cards[middle_part:]
    shuffled_cards = []
    for card in range(len(left_part)):
        shuffled_cards.append(left_part[card])
        shuffled_cards.append(right_part[card])
    deck_cards = shuffled_cards
print(deck_cards)
