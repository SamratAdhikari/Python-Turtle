
#Looping a circle through a square

print("Circle")

import turtle
hey = turtle.Turtle()
hey.speed(0)

def circle(le, ag):
    for i in range(4):
        hey.forward(le)
        hey.left(ag)

for s in range(30):
    circle(100, 90)
    hey.left(10)

turtle.done()



