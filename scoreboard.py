from turtle import Turtle
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.color('black')
        self.hideturtle()
        self.levelName = 1
        self.writeAgain()


    def writeAgain(self):
        self.clear()
        self.goto(-240,260)
        self.write('Level: {0}'.format(self.levelName),align='center',font=FONT)

    def increaseLevel(self):
        self.levelName += 1
        self.writeAgain()

    def gameOver(self):
        self.goto(0,0)
        self.write('GAME OVER',align='center',font=FONT)