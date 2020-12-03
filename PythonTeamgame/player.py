from bangtal import *


class Player(Object):
    centerY = 300
    upY = 450
    downY = 150
    def __init__(self, file, scene, show = True):
        super().__init__(file)
        self.y = self.centerY
        self.scene = scene
        self.locate(scene, 0, self.y)
        self.setScale(0.2)
        
        if show:
            self.show()
    
    def onCombine(self):
        print("test")
    
    def goDown(self):
        self.y -= 150
        if self.y < self.downY:
            self.y = self.downY
        self.locate(self.scene, 0, self.y)
    
    def goUp(self):
        self.y += 150
        if self.y > self.upY:
            self.y = self.upY
        self.locate(self.scene, 0, self.y)
    