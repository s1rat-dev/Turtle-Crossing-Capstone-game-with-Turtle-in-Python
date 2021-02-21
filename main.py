import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carManager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(carManager.carSpeed)
    screen.update()
    carManager.createCars()
    carManager.moveCars()

    # Adding train to the game to make the game more diffucult.
    if score.levelName >= 4:
        carManager.createTrain()
        for train in carManager.trains:
            if train.distance(player) < 68 and train.ycor() < player.ycor() + 19.5:
                game_is_on = False
                score.gameOver()

    # Pass to next level that be faster.
    if player.ycor() > 280:
        player.resetPosition()
        carManager.increaseSpeed()
        score.increaseLevel()

    # We check that are they hit each other or not for decide to gameOver function.
    for car in carManager.allCars:
        if car.distance(player) < 26 and car.ycor() < player.ycor() + 19.5:
            game_is_on = False
            score.gameOver()

screen.exitonclick()