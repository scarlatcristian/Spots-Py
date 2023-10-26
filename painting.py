# import colorgram
from turtle import Turtle, Screen, colormode
import random

# rgb_colors = []
# colors = colorgram.extract('paint.jpeg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

# print(rgb_colors)

colormode(255)
turtle = Turtle()
turtle.speed('fastest')
turtle.penup()
turtle.hideturtle()


color_list = [
    (208, 151, 103), (58, 105, 133), (148, 87, 58), (128, 163, 185), (196, 137, 157), (138, 71, 95), (210, 91, 67), (130, 177, 155), (60, 120, 89), (162, 149, 54), (191, 91, 118), (224, 201, 126), (25, 48,
                                                                                                                                                                                                      75), (78, 157, 122), (55, 41, 27), (232, 166, 185), (40, 56, 105), (238, 170, 159), (56, 33, 47), (58, 155, 172), (115, 37, 58), (105, 121, 164), (27, 51, 39), (160, 210, 190), (17, 95, 71), (117, 42, 33)
]

turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    turtle.dot(20, random.choice(color_list))
    turtle.forward(50)

    if dot_count % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)

screen = Screen()
screen.exitonclick()
