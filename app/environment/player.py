import pyxel
from game_config import JUMP_FORCE, GRAVITY, MAX_JUMPS

class Player:
    def __init__(self, image_path, total_frames, player_width, initial_pos_x, initial_pos_y, floor_ref):
        pyxel.image(1).load(0, 0, image_path)
        self.player_size = player_width
        self.frame_count = total_frames
        self.x = initial_pos_x
        self.y = initial_pos_y
        self.frame = 0
        self.frame_counter = 0
        self.floor_ref = floor_ref
        #gravity
        self.vertical_velocity = 0  # initial vertical velocity
        self.gravity = GRAVITY  # gravity constant
        self.jumps = MAX_JUMPS

    def update(self):
        # change frame every tot frame for animation
        self.frame_counter += 1
        if self.frame_counter % 3 == 0:
            self.frame = (self.frame + 1) % self.frame_count

        # gravity
        self.y += self.vertical_velocity
        self.vertical_velocity += self.gravity

        #check collisions
        self.handle_floor_collisions(self.floor_ref.floors)

        #jump
        if pyxel.btnp(pyxel.KEY_SPACE):
            if self.jumps < MAX_JUMPS:
                self.vertical_velocity -= JUMP_FORCE
                self.jumps += 1

    def handle_floor_collisions(self, floors):
        for floor in floors:
            if (
                self.x < floor.x + floor.width
                and self.x + self.player_size > floor.x
                and self.y < floor.y + floor.height
                and self.y + self.player_size > floor.y
            ):
                # collision found, rest player pos and vertical_velocity
                self.y = floor.y - self.player_size
                self.vertical_velocity = 0
                self.jumps = 0

    def draw(self):
        pyxel.blt(self.x, self.y, 1, self.frame * self.player_size, 0, self.player_size, self.player_size, 0)
