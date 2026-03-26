from turtle import Screen
from fruit import Fruit
from basket import Basket
from scoreboard import Scoreboard
from life import Life

import time

screen = Screen()
screen.setup(width=600,height=500)
screen.title("Fruit Catch")
screen.bgpic('bgpic.png')
screen.register_shape("apple", "fruit.png")
screen.register_shape("basket", "basket.png")
screen.tracer(0)
screen.listen()



# print(screen.getshapes())
game_is_on = True

fruit1 = Fruit()
# fruit2 = Fruit()

basket = Basket()
scoreboard = Scoreboard()

life = Life()

screen.onkeypress(basket.Left,"Left")
screen.onkeypress(basket.Right,"Right")

while game_is_on:
    fruit1.move()
    # fruit2.move()
    time.sleep(0.1)
    screen.update()
    

    # If No Life Left
    if life.life_count ==  0:
            game_is_on = False
            scoreboard.game_over()


    # On Ground Collision
    if fruit1.ycor() < -260:
        if scoreboard.isScoreInc == True:
                scoreboard.isScoreInc=False
                fruit1.refresh()
        else:
            life.decrease_life_count()
            fruit1.refresh()

    # elif fruit2.ycor() < -260:
        
    #     if scoreboard.isScoreInc == True:
    #             scoreboard.isScoreInc=False
    #             fruit2.refresh()
    #     else:
    #         life.decrease_life_count()
    #         fruit2.refresh()

    
    # print(basket.position())
    # On Collision with Basket
    # fruit2.distance(basket.position()) < 70
    
    if fruit1.distance(basket.position()) < 70 and scoreboard.isScoreInc == False: 
        scoreboard.increase_score()




screen.exitonclick()