from Block import Block
import random

class BlockManager:
    def __init__(self):
        self.blocks = []
        red = 20
        green = 20
        blue = 20
        yellow = 20
        gray = 20
        blank = 30
        for i in range(0, 13):
            for j in range(0, 10):
                while True:
                    random_number = random.randint(0, 5)
                    if random_number == 0 and red != 0:
                        red -= 1
                        self.blocks.append(Block(i, j, "red"))
                        break
                    elif random_number == 1 and green != 0:
                        green -= 1
                        self.blocks.append(Block(i, j, "green"))
                        break
                    elif random_number == 2 and blue != 0:
                        blue -= 1
                        self.blocks.append(Block(i, j, "blue"))
                        break
                    elif random_number == 3 and yellow != 0:
                        yellow -= 1
                        self.blocks.append(Block(i, j, "yellow"))
                        break
                    elif random_number == 4 and gray != 0:
                        gray -= 1
                        self.blocks.append(Block(i, j, "pink"))
                        break
                    elif random_number == 5 and blank != 0:
                        blank -= 1
                        break
