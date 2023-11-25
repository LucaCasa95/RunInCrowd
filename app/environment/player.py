import pyxel

class Player:
    def __init__(self, image_path, total_frames, player_width, initial_pos_x, initial_pos_y):
        pyxel.image(1).load(0, 0, image_path)
        self.player_size = player_width
        self.FRAME_COUNT = total_frames
        self.x = initial_pos_x
        self.y = initial_pos_y
        self.frame = 0
        self.frame_counter = 0
        #gravity
        self.dy = 0  # initial vertical velocity
        self.gravity = 0.5  # gravità constant

    def update(self):
        self.frame_counter += 1
        # change frame every tot frame
        if self.frame_counter % 3 == 0:
            self.frame = (self.frame + 1) % self.FRAME_COUNT
         # Aggiorna la posizione y con la velocità verticale
        self.y += self.dy
        # Aggiungi la gravità alla velocità verticale
        self.dy += self.gravity

    def draw(self):
        pyxel.blt(self.x, self.y, 1, self.frame * self.player_size, 0, self.player_size, self.player_size, 0)
