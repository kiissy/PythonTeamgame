from bangtal import *
from button import Button

class StartScene(Scene):
    def __init__(self, name, file, nextScene = None):
        super().__init__(name, file)

        startBtn = Button("images/start.png", self, 600, 270, nextScene, scale=1)
        endBtn = Button("images/end.png", self, 600, 230, scale = 1)
