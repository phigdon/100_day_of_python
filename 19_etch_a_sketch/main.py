import turtle
from turtle import Turtle, Screen
import random

"""
new_turtle = Turtle()
screen = Screen()

def move_forwards():
    new_turtle.forward(10)

def move_backwards():
    new_turtle.back(10)

def turn_right():
    new_turtle.right(10)
def turn_left():
    new_turtle.left(10)

def clear():
    new_turtle.penup()
    new_turtle.home()
    new_turtle.clear()
    new_turtle.pendown()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
"""

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won. The {winning_color} turtle won the race")
            else:
                print(f"You lose. The {winning_color} turtle won the race")


        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()