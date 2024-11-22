import numpy as np
import copy

class Block:
    def __init__(self, x, y, color):
        self.appearance = 'rectangle'
        self.state = None
        self.x = x
        self.y = y
        self.position = np.array([x * 16 + 16, y * 16 + 48, (x + 1) * 16 + 16, (y + 1) * 16 + 48])
        self.fill = color
    
    def to_string(self):
        return f"x = {self.x}, y = {self.y}, color = {self.fill}"
    

    def remove_block(self):
        self.position[0] += 2
        self.position[1] += 2
        self.position[2] -= 2
        self.position[3] -= 2