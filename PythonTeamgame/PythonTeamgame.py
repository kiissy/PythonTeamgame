from bangtal import *
import random

setGameOption(GameOption.ROOM_TITLE, False)
setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

start_scene = Scene("Runaway", "images/startbg.png")

startButton = Object('images/start.png')
startButton.locate(start_scene, 600, 270)
startButton.show()

endButton = Object('images/end.png')
endButton.locate(start_scene, 600, 230)
endButton.show()

def endButton_onMouse(x, y, action):
    endGame()
endButton.onMouseAction = endButton_onMouse

class chara(Object):
    def __init__(self, file, scene, x, y, i, j):
        super().__init__(file)
        self.locate(scene, x, y)
        self.show()
        self.life = 3
        self.i = i
        self.j = j

    # move funciton
    def move(self):
        pass

    def is_die(self):
        if self.life == 0:
            return True
        else:
            return False



startGame(start_scene)