import random
from game_data import data

# format the account data into printable format
def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr} from {account_country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

score = 0
game_on = True
# generate a random account from the game data
account_b = random.choice(data)

while game_on:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"compare A: {format_data(account_a)}")
    print(f"against B: {format_data(account_b)}")

    # ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # check if user is correct
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score = score + 1
        print(f"You're right. Your current score is {score}")
    else:
        game_on = False
        print(f"Sorry, you're wrong. Final score: {score}")