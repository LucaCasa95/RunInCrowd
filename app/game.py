from pyxel import init, run, cls
from game_config import WINDOW_WIDTH, WINDOW_HEIGHT, BACKGROUND_SCROLL_SPEED
from game_loop.draw_objects import DrawObjects
from game_loop.update_objects import UpdateObjects

class App:
    def __init__(self):
        init(WINDOW_WIDTH, WINDOW_HEIGHT)
        init_game(self)
        run(self.update, self.draw)

    def update(self):
        UpdateObjects(self.background)
        pass

    def draw(self):
        cls(0)
        DrawObjects(self.background)

def init_game(self):
    from environment.background import Background
    self.background = Background("assets/background.png", BACKGROUND_SCROLL_SPEED)

if __name__ == "__main__":
    App()
    