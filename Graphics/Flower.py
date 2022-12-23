print("Flower")


import turtle

samrat1 = turtle.Turtle()
samrat1.speed(0)
samrat1.color("green", "orange")
samrat1.begin_fill()
for i in range(100):
    samrat1.forward(200)
    samrat1.left(168.5)
    samrat1.forward(200)

samrat1.end_fill()

turtle.done()
