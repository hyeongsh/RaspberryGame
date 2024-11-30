import numpy as np

class Character:
    def __init__(self):
        self.appearance = 'circle'
        self.state = None
        self.start_pos()
        self.outline = "#FFFFFF"

    def start_pos(self):
        self.x = 6
        self.y = 4
        self.position = np.array([self.x * 16 + 19, self.y * 16 + 51, (self.x + 1) * 16 + 13, (self.y + 1) * 16 + 45])

    def change_position(self):
        self.position = np.array([self.x * 16 + 19, self.y * 16 + 51, (self.x + 1) * 16 + 13, (self.y + 1) * 16 + 45])

