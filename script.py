import random


#Creating a function to contain random cards

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

    card = random.choice(cards)
    return card 