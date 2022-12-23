# Pong Game

# Modules
import turtle

# GUI
root = turtle.Screen()
root.title("Pong Game")
root.bgcolor("black")
root.setup(width=800, height=600)
root.tracer(0)

# Game Objects
# Paddle A
tabA = turtle.Turtle()
tabA.speed(0)
tabA.shape("square")
tabA.color("pink")
tabA.penup()
tabA.goto(-380, 0)
tabA.shapesize(stretch_wid=5,stretch_len=1)

# Paddle B
tabB = turtle.Turtle()
tabB.speed(0)
tabB.shape("square")
tabB.color("light blue")
tabB.penup()
tabB.goto(370, 0)
tabB.shapesize(stretch_wid=5,stretch_len=1)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("light green")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = -0.5


# Functions
# TabA
def tabA_up():
	y = tabA.ycor()
	y += 20
	tabA.sety(y)
def tabA_down():
	y = tabA.ycor()
	y -= 20
	tabA.sety(y)

# TabB
def tabB_up():
	y = tabB.ycor()
	y += 20
	tabB.sety(y)
def tabB_down():
	y = tabB.ycor()
	y -= 20
	tabB.sety(y)


# Keyboard Binding
root.listen()
# Key Binding for TabA
root.onkeypress(tabA_up, "w")
root.onkeypress(tabA_down, "s")
root.onkeypress(tabB_up, "Up")
root.onkeypress(tabB_down, "Down")

# Game Loop
while True:
	root.update()

	# Move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	# Border Checking
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1

	if ball.ycor() < -290:
		ball.sety(-260)
		ball.dy *= -1

	if ball.xcor() > 390:
		ball.goto(0, 0)
		ball.dx *= -1

	if ball.xcor() < -390:
		ball.goto(0, 0)
		ball.dx *= -1

	if (ball.xcor() > 340) and (ball.ycor() < tabB.ycor() + 40) and (ball.ycor() > tabB.ycor() - 40):
		ball.dx *= -1



