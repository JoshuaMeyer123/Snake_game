from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 16, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())

        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.color("white")
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.score}  High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.score_update()

    def score_increase(self):
        self.score += 1
        self.score_update()
