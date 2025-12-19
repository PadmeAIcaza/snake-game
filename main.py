from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(600, 600) # 300 per -ve and +ve axis
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0) # turn off the tracer

# starting positions the three starting squares
starting_positions = [(0, 0), (-20, 0), (-40, 0)] # tuples

# all the new positions of the squares will be stored here
segments = []

# loops to create all 3 squares
for position in starting_positions:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.penup() # it won't draw the default line
    new_segment.goto(position)
    segments.append(new_segment)

game_on = True
while game_on:
    screen.update() # updates the screen once all squares have move forward
    time.sleep(0.1) # adds a 0.1 second delay after all squares have moved
                            # start  stop  step
    for seg_num in range(len(segments) - 1, 0, -1): # this for loop will make the snake move continuously without disconnecting
        new_x = segments[seg_num - 1].xcor() # grabs the previous square's xcoord
        new_y = segments[seg_num - 1].ycor() # grabs the previous square's ycoord
        segments[seg_num].goto(new_x, new_y) # sets the previous square's x and y coords into next square
    segments[0].forward(20)
    segments[0].left(90)













screen.exitonclick()