from turtle import Turtle

ALIGNMENT = "Center"
FONT = ("Courier",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_count = 0
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(0,200)
        self.update_score()
        self.isScoreInc = False

    def update_score(self):
        self.clear()
        self.write(f"score : {self.score_count}",align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score_count +=1
        self.update_score()
        self.isScoreInc = True


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!")

    
    