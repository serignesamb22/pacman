import turtle
import time
import random

# Step 1: Setting Up the Game Environment
screen = turtle.Screen()
screen.title("PacMan")
screen.bgcolor("black")
screen.setup(width=600, height=600)

#Create PacMan
pacman = turtle.Turtle()
pacman.shape("circle")
pacman.color("yellow")
pacman.penup()
pacman.goto(0,0)
pacman.direction= "stop"

#Key Bindings
def go_up():
   pacman.direction = "up"
  
def go_down():
  pacman.direction = "down"

def go_left():
  pacman.direction = "left"

def go_right():
  pacman.direction = "right"

#Use keys to move pacman
def move():
  if pacman.direction == "up":
    y = pacman.ycor()
    pacman.sety(y+20)
  elif pacman.direction == "down":
    y = pacman.ycor()
    pacman.sety(y-20)
  elif pacman.direction == "left":
    x = pacman.xcor()
    pacman.setx(x-20)
  elif pacman.direction == "right":
    x = pacman.xcor()
    pacman.setx(x+20)

#make the game read our inputs
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

ghosts = []
colors = ["purple", "cyen", "orange", "green"]
start_pos = [(100,0), (-100,0), (0,100), (0,-100)]

for color, position in zip(colors, start_pos):
  ghost = turtle.Turtle()
  ghost.shape("square")
  ghost.color(color)
  ghost.penup()
  ghost.goto(position)
  ghosts.append(ghost)
  

#Main Loop
while True:
  screen.update()
  move()
  time.sleep(0.1)
