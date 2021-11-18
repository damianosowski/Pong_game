from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(self.score, align="center", font=('Arial', 20, 'normal'))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game over", align="center")

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
