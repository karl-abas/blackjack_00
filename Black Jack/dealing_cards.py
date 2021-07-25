import random


def player_deal(pick_amount):

    for i in range(pick_amount):
        players_card.append(deck.pop())


players_card = []

deck = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "K", "Q"]*4
random.shuffle(deck)
player_deal(5)

print(players_card)


def player_deal(pick_amount):

    for i in range(pick_amount):
        user_deck.append(deck.pop())


def dealer_deal(pick_amount):

    for i in range(pick_amount):
        deal_deck.append(deck.pop())
