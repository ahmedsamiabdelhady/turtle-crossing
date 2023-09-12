from turtle import Turtle
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()

        self.score = 1

    def scorebar(self):
        self.setpos(-280,260)
        self.write(f"Level: {self.score}", align= "left", font= FONT)

    
    def score_up(self):
        self.clear()
        self.score += 1
        self.scorebar()
    
    def game_over(self):
        self.home()
        self.write("Game Over", align= "center", font= FONT)
    
