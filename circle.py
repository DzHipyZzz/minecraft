from turtle import *

bgcolor('black')
speed(0)
hideturtle()
for i in range(200):
    color('green')
    circle(i)
    color('purple')
    circle(i*1.3)
    right(3)
    forward(3)

