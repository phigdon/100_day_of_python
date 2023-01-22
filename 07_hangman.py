"""
#Steps 1-3
import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

display = []
for letter in chosen_word:
    display.append("_")
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for index in range(len(chosen_word)):
        if chosen_word[index] == guess:
            display[index] = guess
    print(display)
    if "_" not in display:
        end_of_game = True
print("You win.")
"""
## Step 4
##
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"{guess} is not in the word")
        lives = lives - 1

    #Join all the elements in the list and turn it into a String.

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
    print(f"You have {lives} wrong guesses remaining")
    if lives == 0:
        print("You lose")
        end_of_game = True
    print(f"{' '.join(display)}")
