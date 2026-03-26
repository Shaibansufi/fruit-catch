from turtle import Turtle
import random

FRUIT_COUNT  = 3
DISTANCE = 20
DOWN = 270

class Fruit(Turtle):
    def __init__(self):
        super().__init__()
        self.create_fruit()

    def create_fruit(self):
            self.shape("apple")
            self.penup()
            self.speed("fastest")
            self.refresh()
            
                

    def refresh(self):
        x_position = random.randint(-280,280)
        self.goto(x_position,270)
        

    
    def move(self):
        self.setheading(DOWN)
        self.forward(DISTANCE)
        