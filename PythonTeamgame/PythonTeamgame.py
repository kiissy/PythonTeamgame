from bangtal import *
from button import Button
from mainScene import MainScene
from startScene import StartScene

collision = False

if __name__ == "__main__":
    setGameOption(GameOption.ROOM_TITLE, False)
    setGameOption(GameOption.INVENTORY_BUTTON, False)
    setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)
    
    mainScene = MainScene("Main Game", "images/gamebg.png")
    startScene = StartScene("Runaway", "images/startbg.png", mainScene)

    startGame(startScene)
