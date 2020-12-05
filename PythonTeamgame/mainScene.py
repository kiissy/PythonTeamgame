from bangtal import *
from player import Player
from obstacle import Obstacle
from button import Button
import random, threading

class MainScene(Scene):
    keyUp = 84
    keyDown = 85
    
    def __init__(self, name, file, nextScene = None):
        super().__init__(name, file)
        self.startButton = Button("images/start.png", self, 600, 350, scale = 1)
        self.startButton.onMouseAction = self.onStart
        self.mainPlayer = Player("images/player.png", self)
        self.restart = Button("images/restart.png", self, 600, 250)
        self.restart.onMouseAction = self.onRestart
        self.endGame = Button("images/end.png", self, 600, 350)
        self.initialize()

    def initialize(self):
        self.mainPlayer.hide()
        self.restart.hide()
        self.endGame.hide()
        self.startButton.show()
        self.isCollision = False

    def onStart(self, x, y, action):
        self.startButton.hide()
        self.mainPlayer.initLocate()
        self.mainPlayer.show()
        self.t = threading.Thread(target=self.randomGeneration)
        self.t.start()

    def onKeyboard(self, key, pressed):
        if key == self.keyUp and pressed:
            self.mainPlayer.goUp()

        if key == self.keyDown and pressed:
            self.mainPlayer.goDown()

    def randomGeneration(self):
        timer = Timer(100)
        timer.start()
        cTime = timer.get()
        t = random.choice([1, 2, 3])
        while not self.isCollision:
            nTime = timer.get()
            if cTime - nTime > t:
                obstacle = Obstacle(self, self.mainPlayer)
                obstacle.start()
                timer.increase(t)
                cTime = timer.get()
                t = random.choice([0.5, 1.0, 1.5])

        self.gameOver()

    def gameOver(self):
        self.restart.show()
        self.endGame.show()

    def onRestart(self, x, y, action):
        self.initialize()