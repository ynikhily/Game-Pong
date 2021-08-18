# --------------------------------------IMPORT ALL CLASSES---------------------------------------
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# ----------------------------------GLOBAL VARIABLES FOR OUR GAME ---------------------------------------
GAME_TITLE = 'My Pong Game'
SCREEN_COLOR = 'black'
USER_PADDLE_POS = (-390, 0)
OPPONENT_PADDLE_POS = (380, 0)

# -----------------------------------------SCREEN SETUP---------------------------------------------------
game_screen = Screen()
game_screen.setup(width=800, height=600)
game_screen.title(GAME_TITLE)
game_screen.bgcolor(SCREEN_COLOR)
game_screen.tracer(0)

# ---------------------------INITIALISATION OF BASIC GAME OBJECTS----------------------------------------
user_paddle = Paddle(USER_PADDLE_POS)
opponent_paddle = Paddle(OPPONENT_PADDLE_POS)
pong_ball = Ball()
pong_score = ScoreBoard()

# ----------------------------BINDING KEY TO THE PADDLE FUNCTIONS---------------------------------------
game_screen.listen()
game_screen.onkeypress(fun=user_paddle.go_up, key='w')
game_screen.onkeypress(fun=user_paddle.go_down, key='s')
game_screen.onkeypress(fun=opponent_paddle.go_up, key='Up')
game_screen.onkeypress(fun=opponent_paddle.go_down, key='Down')

# -------------------------------------GAME FLOW BEGINS------------------------------------------------
game_on = True
while game_on:
    time.sleep(pong_ball.move_speed)
    pong_ball.move()

    # CONDITION FOR BALL BOUNCING OFF HORIZONTAL BORDER
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.bounce()

    # CONDITION FOR BALL BOUNCING OFF THE PADDLE
    if pong_ball.xcor() < -360 or pong_ball.xcor() > 350:
        if pong_ball.distance(user_paddle) < 50 or pong_ball.distance(opponent_paddle) < 50:
            pong_ball.paddle_bounce()

    # CONDITION FOR GAME OVER.
        elif pong_ball.xcor() < -360:
            pong_ball.refresh()
            pong_score.opponent_scored()

        elif pong_ball.xcor() > 350:
            pong_ball.refresh()
            pong_score.user_scored()

    game_screen.update()

game_screen.exitonclick()
