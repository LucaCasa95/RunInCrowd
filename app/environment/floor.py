import pyxel
from game_config import WINDOW_HEIGHT, INITIAL_FLOOR_WIDTH, FLOOR_HEIGHT

class Floor:
    def __init__(self):
        self.first = True
        self.x_pos = 0
        self.y_pos = WINDOW_HEIGHT - FLOOR_HEIGHT
        self.rect_width = INITIAL_FLOOR_WIDTH
        self.rect_height = FLOOR_HEIGHT

    def update(self):
        pass

    def draw(self):
        if self.first == True:
            self.first = False
        pyxel.rect(self.x_pos, self.y_pos, self.rect_width, self.rect_height, 2)
