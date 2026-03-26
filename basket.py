from turtle import Turtle
from fruit import DISTANCE

LEFT = -180
RIGHT = 0 

class Basket(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("basket")
        self.penup()
        self.speed('fastest')
        self.goto(0,-280)

    def Left(self):
        self.setheading(LEFT)
        self.move()

    def Right(self):
        self.setheading(RIGHT)
        self.move()

    def move(self):
        self.forward(DISTANCE)

