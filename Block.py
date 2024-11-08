import numpy as np

class Block:
    def __init__(self, x, y):
        self.appearance = 'rectangle'
        self.state = None
        self.position = np.array([x * 16, y * 16, (x + 1) * 16, (y + 1) * 16])
        self.outline = "#FFFFFF"
