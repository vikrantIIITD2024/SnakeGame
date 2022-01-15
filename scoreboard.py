from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.score_updates()
        # self.game_over()




    def score_updates(self):
        self.write(f"Score: {self.score} ", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)

        self.write(f"Game  Over", align=ALIGNMENT, font=FONT)





    def score_plus(self):
        self.score += 5
        self.clear()
        self.score_updates()



