from Block import Block
import random

class BlockManager:
    def __init__(self):
        self.blocks = [[None for _ in range(10)] for _ in range(13)]
        self.break_block = []
        self.block_count = 0

    def make_map(self, level):
        self.blocks = [[None for _ in range(10)] for _ in range(13)]
        level_block = 20 - ((3 - level) * 6)
        red = level_block
        green = level_block
        blue = level_block
        orange = level_block
        pink = level_block
        blank = 130 - (level_block * 5)
        tmp = [0, 0, 0, 0, 0, 0]
        for i in range(0, 13):
            for j in range(0, 10):
                while True:
                    random_number = random.randint(0, 130)
                    if random_number < level_block and red != 0:
                        red -= 1
                        self.blocks[i][j] = Block(i, j, "red")
                        break
                    elif random_number < level_block * 2 and green != 0:
                        green -= 1
                        self.blocks[i][j] = Block(i, j, "green")
                        break
                    elif random_number < level_block * 3 and blue != 0:
                        blue -= 1
                        self.blocks[i][j] = Block(i, j, "blue")
                        break
                    elif random_number < level_block * 4 and orange != 0:
                        orange -= 1
                        self.blocks[i][j] = Block(i, j, "orange")
                        break
                    elif random_number < level_block * 5 and pink != 0:
                        pink -= 1
                        self.blocks[i][j] = Block(i, j, "pink")
                        break
                    elif random_number >= level_block * 5 and blank != 0:
                        blank -= 1
                        self.blocks[i][j] = Block(i, j, "white")
                        break

    def click_blocks(self, x, y, gameManager):
        colors = [0, 0, 0, 0, 0, 0]
        directions = []
        if self.blocks[x][y].fill != "white":
            return
        directions.append(self.check_direction(x, y, 0))
        colors[self.check_colors(directions[0].x, directions[0].y)] += 1
        directions.append(self.check_direction(x, y, 1))
        colors[self.check_colors(directions[1].x, directions[1].y)] += 1
        directions.append(self.check_direction(x, y, 2))
        colors[self.check_colors(directions[2].x, directions[2].y)] += 1
        directions.append(self.check_direction(x, y, 3))
        colors[self.check_colors(directions[3].x, directions[3].y)] += 1

        print(f"top: {directions[3].to_string()}")
        print(f"bot: {directions[2].to_string()}")
        print(f"left: {directions[1].to_string()}")
        print(f"right: {directions[0].to_string()}")
        print(f"r: {colors[0]} g: {colors[1]} b: {colors[2]} o: {colors[3]} p: {colors[4]} x: {colors[5]}")
        print("")

        check = True
        if colors[0] >= 2:
            for i in range(0, 4):
                if directions[i].fill == "red":
                    self.blocks[directions[i].x][directions[i].y].fill = "white"
                    directions[i].fill = "black"
                    self.break_block.append(directions[i])
                    gameManager.block_count += 1
                    check = False
        if colors[1] >= 2:
            for i in range(0, 4):
                if directions[i].fill == "green":
                    self.blocks[directions[i].x][directions[i].y].fill = "white"
                    directions[i].fill = "black"
                    self.break_block.append(directions[i])
                    gameManager.block_count += 1
                    check = False
        if colors[2] >= 2:
            for i in range(0, 4):
                if directions[i].fill == "blue":
                    self.blocks[directions[i].x][directions[i].y].fill = "white"
                    directions[i].fill = "black"
                    self.break_block.append(directions[i])
                    gameManager.block_count += 1
                    check = False
        if colors[3] >= 2:
            for i in range(0, 4):
                if directions[i].fill == "orange":
                    self.blocks[directions[i].x][directions[i].y].fill = "white"
                    directions[i].fill = "black"
                    self.break_block.append(directions[i])
                    gameManager.block_count += 1
                    check = False
        if colors[4] >= 2:
            for i in range(0, 4):
                if directions[i].fill == "pink":
                    self.blocks[directions[i].x][directions[i].y].fill = "white"
                    directions[i].fill = "black"
                    self.break_block.append(directions[i])
                    gameManager.block_count += 1
                    check = False
        if check:
            gameManager.end_time -= 3
        
    def check_direction(self, x, y, flag):
        offset = 0
        if flag == 0 or flag == 1:
            if flag == 0:
                offset = 1
            else:
                offset = -1
            cur = x
            while cur >= 0 and cur <= 12:
                if self.blocks[cur][y].fill != "white":
                    return Block(cur, y, self.blocks[cur][y].fill)
                else:
                    cur += offset
        else:
            if flag == 2:
                offset = 1
            else:
                offset = -1
            cur = y
            while cur >= 0 and cur <= 9:
                if self.blocks[x][cur].fill != "white":
                    return Block(x, cur, self.blocks[x][cur].fill)
                else:
                    cur += offset
        return Block(-1, -1, "blank")
        

    def check_colors(self, x, y):
        if (x == -1 and y == -1):
            return 5
        elif self.blocks[x][y].fill == "red":
            return 0
        elif self.blocks[x][y].fill == "green":
            return 1
        elif self.blocks[x][y].fill == "blue":
            return 2
        elif self.blocks[x][y].fill == "orange":
            return 3
        elif self.blocks[x][y].fill == "pink":
            return 4
        else:
            return 5