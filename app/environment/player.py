import pyxel

class Player:
    def __init__(self, image_path, total_frames, player_width, initial_pos_x, initial_pos_y):
        # Carica il spritesheet del player
        pyxel.image(1).load(0, 0, image_path)

        # Costanti
        self.PLAYER_SIZE = player_width
        self.FRAME_COUNT = total_frames

        # Posizione e stato iniziali del player
        self.x = initial_pos_x
        self.y = initial_pos_y
        self.frame = 0

         # Variabile per il conteggio dei frame
        self.frame_counter = 0

    def update(self):
        # Incrementa il conteggio dei frame
        self.frame_counter += 1

        # Cambia il frame ogni tot frame (modifica questo valore per regolare la velocità)
        if self.frame_counter % 3 == 0:
            self.frame = (self.frame + 1) % self.FRAME_COUNT

    def draw(self):
        # Disegna il player corrente
        pyxel.blt(self.x, self.y, 1, self.frame * self.PLAYER_SIZE, 0, self.PLAYER_SIZE, self.PLAYER_SIZE, 0)
