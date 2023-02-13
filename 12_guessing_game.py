from random import randint
answer = randint(1, 100)
EASY_LEVEL = 10
HARD_LEVEL = 5

turns = 0
def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns remaining"""
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print("You got it")

def set_difficulty():
    level = input("Choose a difficulty. 'easy' or 'hard:")
    if level == 'easy':
        return EASY_LEVEL
    elif level == 'hard':
        return HARD_LEVEL
def game():
    print("Welcome to the guessing game")
    print("I'm thinking of a number between 1 and 100")
    print(f"The acutal answer is {answer}")
    turns = set_difficulty()


    guess = 0
    while guess != answer:
        print(f"You have {turns} remaining to guess the number.")
        guess = int(input("Make a guess:"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses. You lose.")
            return


game()