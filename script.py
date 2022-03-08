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

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"

    elif computer_score == 0:
        return "Lose, Computer has a blck Jack"

    elif user_score == 0:
        return  "Win with Blacjack"  

    elif user_score > 21:
        return "You went over. You lose"   

    elif computer_score > 21: 
        return "You won, computer went over"  


while not game_over:

    user_score = calculate_score(user_card)
    computer_score = calculate_score(computer_card)

    print(f"Your cards: {user_card}, current score: {user_score}")
    print(f"Computer's first card: {computer_card[0]}")


    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True

    else:
        last_deal = input("Type 'y' to get another card, type 'n' to pass:\n")

        if last_deal == 'y':
            user_card.append(deal_card())

        else:
            game_over = True        


while computer_score != 0 and computer_score < 17:
    computer_card.append(deal_card())      
    computer_score = calculate_score(computer_card)      