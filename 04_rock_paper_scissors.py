"""
## simple coin flip
##
import random

random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")

## Banker roulette
##
import random
names_string = input("Give me everybody's names, separated by a comma. ")

names = names_string.split(", ")
random_choice = random.randint(0, len(names) - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to pay for the meal today.")

## Treasure map
##
row1 = ["■", "■", "■"]
row2 = ["■", "■", "■"]
row3 = ["■", "■", "■"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0]) - 1
vertical = int(position[1]) - 1

selected_row = map[vertical]
selected_row[horizontal] = "X"

print(f"{row1}\n{row2}\n{row3}")
"""
## Rock, paper, scissors
##
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))
if user_choice != 0 or user_choice != 1 or user_choice != 2:
    print("Invalid entry")
else:
    print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("Computer chose:")
print(game_images[computer_choice])

if computer_choice == 0:
    if user_choice == 0:
        print("You tied with Rock.")
    elif user_choice == 1:
        print("You lose")
    elif user_choice == 2:
        print("You win")

if computer_choice == 1:
    if user_choice == 0:
        print("You win")
    elif user_choice == 1:
        print("You tied with Paper.")
    elif user_choice == 2:
        print("You lose")

if computer_choice == 2:
    if user_choice == 0:
        print("You lose")
    elif user_choice == 1:
        print("You win")
    elif user_choice == 2:
        print("You tied with Scissors.")