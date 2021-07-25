import random


# function ask for how many times to pick and whos deck to put it in

def deal(pick_amount, who_deck, who_num_deck):
    for i in range(pick_amount):
        card = deck.pop()
        who_deck.append(card)
        if card == "J" or card == "Q" or card == "K":
            who_num_deck.append(10)
        else:
            who_num_deck.append(card)


def counter(add):
    count = sum(add)
    return count




deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "K", "Q"]*4
random.shuffle(deck)

user_deck = []
user_num_deck = []
user_total = 0


dealer_total = 0
dd = []

deal(2, user_deck, user_num_deck)
print(user_deck)
print(user_num_deck)
user_total += counter(user_num_deck)
print(user_total)
