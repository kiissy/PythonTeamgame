from bangtal import *

class Button(Object):
    def __init__(self, file, scene, x, y, nextScene = None, scale = 1, show = True):
        super().__init__(file)
        self.locate(scene, x, y)
        self.nextScene = nextScene
        self.setScale(scale)
        if show:
            self.show()

    def setNextScene(self, nextScene):
        self.nextScene = nextScene
        
    def onMouseAction(self, x, y, action):
        if self.nextScene == None:
            endGame()
        else:
            self.nextScene.enter()
