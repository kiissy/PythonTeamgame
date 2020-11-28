from bangtal import *
import random

setGameOption(GameOption.ROOM_TITLE, False)
setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

start_scene = Scene("Runaway", "images/startbg.png")
scene = Scene("game", "images/gamebg.png")

startButton = Object('images/start.png')
startButton.locate(start_scene, 600, 270)
startButton.show()
def startButton_onMouse(x, y, action):
    pass
startButton.onMouseAction = startButton_onMouse

endButton = Object('images/end.png')
endButton.locate(start_scene, 600, 230)
endButton.show()

def endButton_onMouse(x, y, action):
    endGame()
endButton.onMouseAction = endButton_onMouse

class Player(Object):
    def __init__(self, file, scene, x, y, i, j):
        super().__init__(file)
        self.locate(scene, x, y)
        self.show()
        self.life = 3
        self.i = i
        self.j = j

    # move funciton
    def move(self, dir):
        pass

    def is_die(self):
        if self.life == 0:
            return True
        else:
            return False

player = Player("images/player.png", scene, )

class Arrow(Object):
    def __init__(self, file, scene, x, y, dir):
        super().__init__(file)
        self.locate(scene, x, y)
        self.show()
        self.dir = dir

    def onMouseAction(self, x, y, aciton):
        pass

startGame(start_scene)