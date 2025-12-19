from turtle import Turtle

# starting positions the three starting squares
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)] # tuples
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        # all the new positions of the squares will be stored here
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    '''creates snake's body'''
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()  # it won't draw the default line
        new_segment.goto(position)
        self.segments.append(new_segment)

    '''adds a new segment everytime snake eats'''
    def extend(self):
        # adds a segment to the end of the snake (the tail)
        self.add_segment(self.segments[-1].position()) # position() comes from turtle class


    def move(self):
        # start  stop  step
        for seg_num in range(len(self.segments) - 1, 0,
                             -1):  # this for loop will make the snake move continuously without disconnecting
            new_x = self.segments[seg_num - 1].xcor()  # grabs the previous square's xcoord
            new_y = self.segments[seg_num - 1].ycor()  # grabs the previous square's ycoord
            self.segments[seg_num].goto(new_x, new_y)  # sets the previous square's x and y coords into next square
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN: # if pointing down, is not allowed to go up
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP: # if pointing up, is not allowed to go down
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT: # if pointing right, is not allowed to go left
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT: # if pointing left, is not allowed to go right
            self.head.setheading(RIGHT)