from turtle import Turtle
PADDLE_POSITION = 350
MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, side):
        super().__init__()
        self.paddle = Turtle(shape="square")
        self.paddle.resizemode("user")
        self.paddle.turtlesize(stretch_len=5)
        self.paddle.color("white")
        self.paddle.penup()
        if side == "left":
            self.paddle.goto(-PADDLE_POSITION, 0)
        elif side == 'right':
            self.paddle.goto(PADDLE_POSITION, 0)
        self.paddle.setheading(UP)

    def move_up(self):
        self.paddle.forward(MOVE_DISTANCE)

    def move_down(self):
        self.paddle.backward(MOVE_DISTANCE)
