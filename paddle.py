# THIS FILE CONTAINS PADDLE CLASS DEFINITION WHICH CAN BE SEEN ON BOTH SIDES OF THE GAME SCREEN.
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, paddle_position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(paddle_position)

    def go_up(self):
        new_y = self.ycor() + 20
        if new_y < 260:
            self.sety(new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        if new_y > -260:
            self.sety(new_y)
