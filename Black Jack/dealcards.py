import random


# function ask for how many times to pick and whos deck to put it in

def deal(pick_amount, who_deck):

    for i in range(pick_amount):
        who_deck.append(deck.pop())

deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, "J", "K", "Q"]*4
random.shuffle(deck)
user_deck = []
dd = []
deal(5, user_deck)
print("the user has {}".format(user_deck))
deal(5, dd)
print("the dealer has{}".format(dd))
