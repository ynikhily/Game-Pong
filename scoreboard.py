# THIS FILE CONTAINS THE SCOREBOARD CLASS DEFINITION USED IN OUR PONG GAME
from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 20, "")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.user_score = 0
        self.opponent_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.penup()
        self.color('white')
        self.goto(0, -300)
        self.setheading(90)
        while self.ycor() < 250:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
        self.goto(0, 275)
        self.write(f"Score", align=ALIGNMENT, font=FONT)
        self.goto(0, 250)
        self.write(f"{self.user_score}\t\t{self.opponent_score}", align=ALIGNMENT, font=FONT)

    def user_scored(self):
        self.user_score += 1
        self.update_score()

    def opponent_scored(self):
        self.opponent_score += 1
        self.update_score()
