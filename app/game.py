import pyxel
import game_config
from game_loop.draw_objects import DrawObjects
from game_loop.update_objects import UpdateObjects

class App:
    def __init__(self):
        init_game()
        pyxel.init(game_config.WINDOW_WIDTH, game_config.WINDOW_HEIGHT)
        pyxel.run(self.update, self.draw)

    def update(self):
        #UpdateObjects(self.player1)
        pass

    def draw(self):
        pyxel.cls(0)
        #DrawObjects(self.player)

def init_game():
    #create gamne objects
    pass

if __name__ == "__main__":
    App()
    