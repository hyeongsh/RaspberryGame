import numpy as np

class Block:
    def __init__(self, x, y):
        self.appearance = 'rectangle'
        self.state = None
        self.position = np.array([x * 20, y * 20, (x + 1) * 20, (y + 1) * 20])
        self.outline = "#FFFFFF"
