from turtle import Screen, Turtle
from paddle import Paddle

SCREEN_WIDTH = 800
SCREEN_HIGH = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HIGH)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle_left = Paddle((-350, 0))
paddle_right = Paddle((350, 0))

centre_line = Turtle(shape="square")
centre_line.color("white")
centre_line.hideturtle()
centre_line.penup()
centre_line.goto(0, -SCREEN_HIGH / 2 + 30)
centre_line.setheading(90)
centre_line.width(5)

for _ in range(int((SCREEN_HIGH - 60) / 30)):
    centre_line.forward(15)
    centre_line.pendown()
    centre_line.forward(15)
    centre_line.penup()

screen.listen()
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")

is_game_on = True
while is_game_on:
    screen.update()

screen.exitonclick()
