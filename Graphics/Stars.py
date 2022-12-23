print("Stars")

import turtle

samrat3 = turtle.Turtle()
samrat3.speed(0)
samrat3.getscreen().bgcolor("#994444")
samrat3.color("white", "cyan")

def star(samrat3, size):

    if size <= 10:
        return
    else:
        samrat3.begin_fill()
        for i in range(5):
            samrat3.forward(size)
            star(samrat3, size/3)
            samrat3.left(216) #216
        samrat3.end_fill()









star(samrat3, 360)






turtle.done()
