from turtle import Turtle

# starting positions the three starting squares
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)] # tuples
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        # all the new positions of the squares will be stored here
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        '''creates snake's body'''
        for position in STARTING_POSITIONS:
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.penup()  # it won't draw the default line
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        # start  stop  step
        for seg_num in range(len(self.segments) - 1, 0,
                             -1):  # this for loop will make the snake move continuously without disconnecting
            new_x = self.segments[seg_num - 1].xcor()  # grabs the previous square's xcoord
            new_y = self.segments[seg_num - 1].ycor()  # grabs the previous square's ycoord
            self.segments[seg_num].goto(new_x, new_y)  # sets the previous square's x and y coords into next square
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)