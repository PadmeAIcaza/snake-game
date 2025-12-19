from turtle import Turtle
import random

# inheritance
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5) # stretches the lenght and width
        self.color('blue')
        self.speed('fastest')
        '''generates random positions for the food'''
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
