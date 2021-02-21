from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.allCars = []
        self.trains = []
        self.carSpeed = 0.08
        self.reachLevel = False

    def createCars(self):
        randChange = random.randint(1,6)
        if randChange == 1:
            new_car = Turtle('square')
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            randomPosition = random.randint(-250, 250)
            new_car.setheading(0)
            new_car.goto(300, randomPosition)
            self.allCars.append(new_car)

    def moveCars(self):
        for car in self.allCars:
            car.backward(STARTING_MOVE_DISTANCE)
        for train in self.trains:
            train.backward(STARTING_MOVE_DISTANCE)

    def increaseSpeed(self):
        self.carSpeed *= 0.7

    def createTrain(self):
        randForTrain = random.randint(1, 100)
        if randForTrain == 1:
            train = Turtle('square')
            train.color(random.choice(COLORS))
            train.penup()
            # The only difference between train and car is the length value.
            train.shapesize(stretch_wid=1, stretch_len=6)
            randomPosition = random.randint(-250, 250)
            train.setheading(0)
            train.goto(300, randomPosition)
            self.trains.append(train)