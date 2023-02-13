import random

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return a score on the cards"""
    if sum(cards) == 21 and len(cards) ==2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, dealer_score):
    if user_score == dealer_score:
        return "Tie. You lose"
    elif user_score == 0:
        return "Dealer has blackjack. you lose."
    elif user_score == 0:
        return "You win with a blackjack."
    elif user_score > 21:
        return "You busted. Lose"
    elif dealer_score > 21:
        return "Dealer busted. you win."
    elif user_score > dealer_score:
        return "you win"
    else:
        return "you lose"

def play_game():
    user_cards = []
    dealer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append((deal_card()))

    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)

    while not game_over:
        print(user_cards)
        print(dealer_cards)
        if dealer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card. Type 'n' to pass")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)
    print(compare(user_score, dealer_score))

while input("Do you want to play? Type 'y' or 'n': ") == 'y':
    play_game()