import random


#Creating a function to contain random cards

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

    card = random.choice(cards)
    return card 

user_card = []
computer_card = []

for _ in range(2):
    user_card.append(deal_card())

    computer_card.append(deal_card())


def calculate_score()
