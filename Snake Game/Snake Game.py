# Snake Game
# Author: Samrat Adhikari
# Date: 18 October
# Purpose: Educational Purpose

# Modules
import turtle
import time
import random
import os
import tkinter


# Get high score
with open('Score.txt') as f:
	HIGH_SCORE = f.read()

# Game Variables
WIDTH = 600
HEIGHT = 600
BG = 'green'
HEAD_COLOR = 'black'
BODY_COLOR = 'grey'
FOOD_COLOR = 'red'
DELAY = 0.1
SPEED = 20
SCORE = 0


# Setup the screen
win = turtle.Screen()
win.title('Snake Game')
win.bgcolor(BG)
win.setup(width=WIDTH, height=HEIGHT)
win.cv._rootwindow.resizable(False, False)
win.tracer(0) # Turns off the screen updates
# Set Favicon
img = tkinter.Image('photo', file="icon.png")
turtle._Screen._root.iconphoto(True, img)


# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color(HEAD_COLOR)
head.penup()
head.goto(0, 0)
head.direction = 'stop'

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color(FOOD_COLOR)
food.penup()
food.goto(0, 100)

# Segments for body
segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f'Score: {SCORE} \tHigh Score: {HIGH_SCORE}', align='center', font='Courier 22 normal')


# Functions
def go_up():
	if head.direction != 'down':
		head.direction = 'up'

def go_down():
	if head.direction != 'up':
		head.direction = 'down'

def go_left():
	if head.direction != 'right':
		head.direction = 'left'

def go_right():
	if head.direction != 'left':
		head.direction = 'right'

def game_over():
	time.sleep(0.5)
	head.goto(0, 0)
	head.direction = 'stop'
	DELAY = 0.1

	# Remove the segments
	for segment in segments:
		segment.goto(1000, 1000)

	# Clear the segments list
	segments.clear()


def move():
	if head.direction == 'up':
		y = head.ycor()
		head.sety(y + SPEED)

	if head.direction == 'down':
		y = head.ycor()
		head.sety(y - SPEED)

	if head.direction == 'left':
		x = head.xcor()
		head.setx(x - SPEED)

	if head.direction == 'right':
		x = head.xcor()
		head.setx(x + SPEED)

# Keyboard bindings
win.listen()
win.onkeypress(go_up, 'Up')
win.onkeypress(go_down, 'Down')
win.onkeypress(go_left, 'Left')
win.onkeypress(go_right, 'Right')

# Gameloop
while True:
	win.update()

	# Check for a collision with the border
	if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
		game_over()

	# Move food to random coordinate
	if head.distance(food) < 30:
		x = random.randint(-270, 270)
		y = random.randint(-270, 260)
		food.goto(x, y)

		# Add a segment
		segment = turtle.Turtle()
		segment.speed(0)
		segment.shape('square')
		segment.color(BODY_COLOR)
		segment.penup()
		segments.append(segment)

		# Increase game speed
		DELAY -= 0.01

		# Increase the score
		SCORE += 10

		if SCORE > int(HIGH_SCORE):
			HIGH_SCORE = SCORE

			with open('Score.txt' ,'w') as f:
				f.write(str(HIGH_SCORE))

		pen.clear()
		pen.write(f'Score: {SCORE} \tHigh Score: {HIGH_SCORE}', align='center', font='Courier 22 normal')

	# Move the end segments first in reverse order
	for index in range(len(segments)-1, 0, -1):
		x = segments[index - 1].xcor()
		y = segments[index - 1].ycor()

		segments[index].goto(x, y)

	# Move segment 0 to where the head is
	if len(segments) > 0:
		x = head.xcor()
		y = head.ycor()
		segments[0].goto(x, y)

	move()

	# Check for head collision with the body segments
	for segment in segments:
		if segment.distance(head) < 20:
			game_over()

	time.sleep(0.1)

win.mainloop()
