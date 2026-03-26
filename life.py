from turtle import Turtle
from scoreboard import ALIGNMENT,FONT

class Life(Turtle):
    def __init__(self):
        super().__init__()
        self.life_count = 5
        self.color("black")
        self.penup()
        self.goto(250,260)
        self.update_life_count()

    def decrease_life_count(self):
        self.life_count -= 1
        self.update_life_count()
        

    def update_life_count(self):
        self.clear()
        self.write(f"Life : {self.life_count}",align=ALIGNMENT,font=FONT)
    
