from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color('white')
        self.penup() # removes the movement line
        self.goto(0, 270) # positioning of the text
        self.hideturtle() # removes the turtle
        self.update_scoreboard()


    def update_scoreboard(self): # is called everytime the snake eats food
        self.clear() # removes the previous text and score to avoid overlaps
        self.write(f'Score: {self.score} High Score: {self.high_score}', False,ALIGNMENT, FONT)


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write('GAME OVER', False, ALIGNMENT, FONT)


