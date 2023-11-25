import pyxel
from game_config import WINDOW_HEIGHT, INITIAL_FLOOR_WIDTH, FLOOR_HEIGHT, FLOOR_VELOCITY
from random import randint

class Floor:
    def __init__(self):
        self.first = True
        self.floors = []
        self.max_floors_to_draw = 1

    def update(self):
        if len(self.floors) < self.max_floors_to_draw:
            #floor creation
            if self.first == True:
                #first floor of the game
                self.x_pos = 0
                self.y_pos = WINDOW_HEIGHT - FLOOR_HEIGHT
                self.floor_width = INITIAL_FLOOR_WIDTH
                self.floor_height = FLOOR_HEIGHT
                self.first = False
            else:
                #randomic generated floor
                pass
            self.floors.append(FloorElem(self.x_pos, self.y_pos, self.floor_width, self.floor_height, randint(1, 16)))
        
        #update floors x
        for floor in self.floors:
            floor.x -= FLOOR_VELOCITY

    def draw(self):
        for floor in self.floors:
            pyxel.rect(floor.x, floor.y, floor.width, floor.height, floor.color)

class FloorElem:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
