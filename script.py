import random


#Creating a function to contain random cards

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

    card = random.choice(cards)
    return card 

user_card = []
computer_card = []
game_over = False

for _ in range(2):
    user_card.append(deal_card())

    computer_card.append(deal_card())


def calculate_score(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


user_score = calculate_score(user_card)
computer_score = calculate_score(computer_card)


