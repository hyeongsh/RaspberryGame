import numpy as np
import copy

class Block:
    def __init__(self, x, y, color):
        self.appearance = 'rectangle'
        self.state = None
        self.x = x
        self.y = y
        self.position = np.array([x * 16 + 16, y * 16 + 48, (x + 1) * 16 + 16, (y + 1) * 16 + 48])
        self.pattern = np.array([x * 16 + 21, y * 16 + 53, (x + 1) * 16 + 11, (y + 1) * 16 + 43])
        self.fill = color
    
    def to_string(self):
        return f"x = {self.x}, y = {self.y}, color = {self.fill}"
    
    def adjust_fill(self):
        if self.fill == "red":
            return (255, 153, 153)
        if self.fill == "green":
            return (102, 205, 102)
        if self.fill == "blue":
            return (153, 153, 255)
        if self.fill == "orange":
            return (255, 204, 153)
        if self.fill == "pink":
            return (255, 182, 215)
        return (255, 255, 255, 255)

    def remove_block(self):
        self.position[0] += 2
        self.position[1] += 2
        self.position[2] -= 2
        self.position[3] -= 2