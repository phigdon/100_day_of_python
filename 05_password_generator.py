"""
## Height average
##
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
number_students = 0
for height in student_heights:
    total_height = total_height + height
    number_students = number_students + 1
average_height = total_height / number_students
print(average_height)

## High score
## 78 65 89 86 55 91 64 89
student_scores = input("Input a list of student scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
max_score = 0
for score in student_scores:
    if score >= max_score:
        max_score = score
print(f"The highest score in the class is {max_score}")

## Adding even numbers
##
total = 0
for number in range(2, 101, 2):
    total = total + number
print(total)

##
##
for number in range(1,101):
    if number %3 == 0 and number %5 == 0:
        print("FizzBuzz")
    elif number %3 == 0:
        print("Fizz")
    elif number %5 == 0:
        print("Buzz")
    else:
        print(number)

## Password generator
##
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

## simple
password = ""
for char in range(1, nr_letters +1):
    password = password + random.choice(letters)
for char in range(1, nr_symbols +1):
    password = password + random.choice(numbers)
for char in range(1, nr_numbers +1):
    password = password + random.choice(symbols)
print(password)
"""
# finished
password_list =[]
for char in range(1, nr_letters +1):
    password_list.append(random.choice(letters))
for char in range(1, nr_symbols +1):
    password_list.append(random.choice(symbols))
for char in range(1, nr_numbers +1):
    password_list.append(random.choice(numbers))
print(password_list)
random.shuffle(password_list)
print(password_list)