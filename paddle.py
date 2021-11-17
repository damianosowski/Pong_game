from turtle import Turtle
PADDLE_POSITION = 350
MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, side):
        super().__init__()
        self.resizemode("user")
        self.shape("square")
        self.turtlesize(stretch_len=5)
        self.color("white")
        self.penup()
        if side == "left":
            self.goto(-PADDLE_POSITION, 0)
        elif side == 'right':
            self.goto(PADDLE_POSITION, 0)
        self.setheading(UP)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.backward(MOVE_DISTANCE)
