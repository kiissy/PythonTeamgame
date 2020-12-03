from bangtal import *
import threading
import random

class Obstacle(Object):
    def __init__(self, scene, player):
        super().__init__(random.choice(['images/cat1.png', 'images/cat2.png',\
            'images/cat3.png', 'images/cat4.png', 'images/dog1.png',\
            'images/dog2.png','images/dog3.png', 'images/dog4.png']))
        self.scene = scene
        self.x = 1000
        
        self.y = random.choice([150, 300, 450])

        self.locate(scene, self.x, self.y)
        self.setScale(0.45)
        self.show()
        self.end = False
        self.speed =2.0
        self.player = player

    def start(self):
        t = threading.Thread(target=self.move)
        t.start()
    
    def move(self):
        self.timer1 = Timer(int(10 / self.speed))
        self.timer1.onTimeout = self.onTimeOut
        self.timer1.start()
        currentTime = self.timer1.get()
        while not self.scene.isCollision:
            time2 = self.timer1.get()
            if (currentTime - time2) > (1 / (self.speed * 10)):
                currentTime = time2
                self.x -= (10 * self.speed)
                self.locate(self.scene, int(self.x), self.y)
                if self.x < 100:
                    if self.player.y == self.y:
                        print("collision")
                        self.scene.isCollision = True
                        self.timer1.onTimeout()
                if self.x < 0:
                    self.timer1.onTimeout()
        self.timer1.onTimeout()
    def onTimeOut(self):
        self.y = -1
        self.hide()
        del self