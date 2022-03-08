import random


#Creating a function to contain random cards


def start_game():
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
            return f"Draw {computer_score}"

        elif computer_score == 0:
            return f"Lose, Computer has a blck Jack {computer_score}"

        elif user_score == 0:
            return  f"Win with Blacjack {computer_score}"

        elif user_score > 21:
            return f"You went over. You lose {computer_score}"

        elif computer_score > 21:
            return f"You won, computer went over {computer_score}"

        elif computer_score < user_score:
            return f"You won {computer_score}"

        else:
            return f"You lost {computer_score}"


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


    print(compare(user_score, computer_score))


start_game()


start_new_game = True

while start_new_game:
    command = input("Would you like to play Again:\n")

    if command == 'y':
        start_game()

    else:
        start_new_game = False