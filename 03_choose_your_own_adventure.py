"""
## Check if a number is even or odd
##
number = int( input("Which number do you want to check? "))

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
## Print out BMI and weight status of patient
##
height = float( input("Enter your height in m: ") )
weight = float( input("Enter your weight in Kg: "))

BMI = round( weight / (height**2) )

if BMI < 18.5:
    print(f"Your BMI is {BMI}. You are underweight")
elif BMI < 25:
    print(f"Your BMI is {BMI}. You have a normal weight")
elif BMI < 30:
    print(f"Your BMI is {BMI}. You are overweight")
elif BMI < 35:
    print(f"Your BMI is {BMI}. You are obese")
else:
    print(f"Your BMI is {BMI}. You are clinically obese")

## Leap year checking program
##
year = int(input("Which year do you want to check? "))

if year % 400 == 0:
    print(f"The year {year} is a leap year")
elif year % 100 == 0:
    print(f"The year {year} is not a leap year")
elif year % 4 == 0:
    print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is not a leap year")

##  Rollercoaster pricing agent
##
print("Welcome to the rollercoaster")
height = int( input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int( input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        bill = bill + 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you are not tall enough to ride this rollercoaster.")

## Pizza pricing agent
##
print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M, or L.")
add_pepperoni = input("Do you want pepperoni? Y or N.")
extra_cheese = input("Do you want extra cheese? Y or N.")

bill = 0

if size == "S":
    bill = 15
if size == "M":
    bill = 20
if size == "L":
    bill = 25
else:
    print("You entered a wrong order")
if add_pepperoni == "Y":
    if size == "S":
        bill = bill + 2
    else:
        bill = bill + 3
if extra_cheese == "Y":
    bill = bill + 1
print(f"Your bill is ${bill}")

## Love calculator
##
print("Welcome to the love calculator")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_score = 0
name2_score = 0

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int( str(true) + str(love) )
print(love_score)

if (love_score < 10) or (love_score > 90)
    print(f"Your love score is {love_score}, you go together like mentos and coke")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")
"""
## Tresure island
##
print("Welcome to Tresure Island")
print("Your mission is to find the treasure.")
direction = input("You're at a cross road. Do you want to go left or right?")

if direction == "left":
    direction = input("You reach a river crossing. Do you want to 'swim' or 'wait' for a boat?")
else:
    print("you are attacked by chimpanzees. Game over.")
if direction == "wait":
    direction = input("You crossed the river and see three doors. There is a red, blue, and a yellow door. Choose a colour 'red', 'blue', or 'yellow'")
else:
    print("You drown in the river. Game over")
if direction == "yellow"
    print("You win")
elif direction == "red":
    print("You fall into a hole. Game over")
else:
    print("You are attacked by an alligator. Game Over")