import numpy as np

class Block:
    def __init__(self, x, y, color):
        self.appearance = 'rectangle'
        self.state = None
        self.x = x
        self.y = y
        self.position = np.array([x * 16 + 16, y * 16 + 48, (x + 1) * 16 + 16, (y + 1) * 16 + 48])
        self.fill = color
