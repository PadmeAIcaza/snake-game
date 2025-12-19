from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(600, 600) # 300 per -ve and +ve axis
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0) # turn off the tracer

snake = Snake()
screen.listen() # captures user's inputs
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_on = True
while game_on:
    screen.update() # updates the screen once all squares have move forward
    time.sleep(0.1) # adds a 0.1 second delay after all squares have moved

    snake.move()













screen.exitonclick()