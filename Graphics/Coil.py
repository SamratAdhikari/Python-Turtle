print("Coil")

import turtle
import math

samrat2 = turtle.Turtle()
samrat2.speed(0)
samrat2.color("purple", "blue")

for i in range(2000):
    samrat2.forward(10)
    samrat2.left(math.sin(i/10)*25)
    samrat2.left(20)




turtle.done()