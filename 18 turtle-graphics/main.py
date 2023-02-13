import turtle
from turtle import Turtle, Screen
import random

#tim = Turtle()
turtle.colormode(255)
directions = [0, 90, 180, 270]

#for _ in range(4):
#    tim.forward(100)
#    tim.left(90)

#for _ in range(6):
#    tim.pendown()
#    tim.forward(10)
#    tim.penup()
#    tim.forward(10)

#for i in range(8):
#    for _ in range(i + 3):
#        tim.forward(100)
#        tim.right(360/(i + 3))

#tim.pensize(15)
#tim.speed("fastest")
#for _ in range(200):
#    tim.color(random.choice(colors))
#    tim.forward(30)
#    tim.setheading(random.choice(directions))

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color



def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

#draw_spirograph(10)
#screen = Screen()
#screen.exitonclick()
"""
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)
"""
color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim = turtle.Turtle()
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
tim.speed("fastest")

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle.Screen()
screen.exitonclick()