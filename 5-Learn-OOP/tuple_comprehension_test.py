SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]
card_list = []
temp_tuple = ()
# Not quite
'''
for symbol in SUITS:
    card_list.append(tuple(i for i in RANKS))
# [('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'), 
# ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'), 
# ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'), 
# ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')]
'''
for symbol in SUITS:
    for card in RANKS:
        item = (card, symbol)
        print(item)

for symbol in SUITS:
    for card in RANKS:
        card_list.append((card, symbol))

print(card_list)
print(card_list.pop())