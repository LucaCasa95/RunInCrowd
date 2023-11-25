import pyxel
from game_config import WINDOW_HEIGHT, PLAYER_POS_Y, PLAYER_WIDTH, INITIAL_FLOOR_WIDTH, FLOOR_MARGIN

class Floor:
    def __init__(self):
        self.first = True
        self.x_pos = 0
        self.y_pos = PLAYER_POS_Y + PLAYER_WIDTH - FLOOR_MARGIN
        self.rect_width = INITIAL_FLOOR_WIDTH
        self.rect_height = WINDOW_HEIGHT - self.y_pos

    def update(self):
        pass

    def draw(self):
        if self.first == True:
            self.first = False
        pyxel.rect(self.x_pos, self.y_pos, self.rect_width, self.rect_height, 2)
