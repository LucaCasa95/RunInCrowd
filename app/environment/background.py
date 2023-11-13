import pyxel

class Background:
    def __init__(self, image_path, scroll_speed):
        pyxel.image(0).load(0, 0, image_path)
        # get image size
        self.image_width = pyxel.image(0).width
        self.image_height = pyxel.image(0).height
        # background initial position
        self.bg_x_1 = 0
        self.bg_x_2 = self.image_width
        # scroll speed
        self.scroll_speed = scroll_speed

    def update(self):
        # scroll left
        self.bg_x_1 -= self.scroll_speed
        self.bg_x_2 -= self.scroll_speed
        # if first background passes entire width, reset
        if self.bg_x_1 <= -self.image_width:
            self.bg_x_1 = self.image_width
        # if second background passes entire width, reset
        if self.bg_x_2 <= -self.image_width:
            self.bg_x_2 = self.image_width

    def draw(self):
        pyxel.blt(self.bg_x_1, 0, 0, 0, 0, self.image_width, self.image_height, 0)
        pyxel.blt(self.bg_x_2, 0, 0, 0, 0, self.image_width, self.image_height, 0)