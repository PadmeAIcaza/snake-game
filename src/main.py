from turtle import Screen
from snake import Snake
from src.food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600) # 300 per -ve and +ve axis
screen.bgcolor('coral')
screen.title('Snake Game')
screen.tracer(0) # turn off the tracer

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    # if the snake's head is within 15 pixels off the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() < -295 or snake.head.ycor() > 295:
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()