#!/usr/bin/env python3.10

#import packages

import turtle

#greet user

print("Buenas, this app will make a simple square to your specifications")

#take user values

c1 = input("Choose your first color..")
c2 = input("Second color..")
c3 = input("Third color..")
c4 = input("Final color..?")

dimen = input("What is the desired length of the sides?")
dimen = float(dimen)

rainbow = [c1, c2, c3, c4]

ssquare = turtle.Turtle()
ssquare.speed(1)
ssquare.width(2)
ssquare.penup()
ssquare.setpos((-dimen/2), (dimen/2))
ssquare.pendown()
for side in rainbow:
    ssquare.color(side)
    ssquare.forward(dimen)
    ssquare.right(90)
ssquare.hideturtle()
