import numpy as np

class Character:
    def __init__(self):
        self.appearance = 'circle'
        self.movement = [False, False, False, False]
        self.state = None
        self.start_pos()
        self.outline = "#FFFFFF"

    def start_pos(self):
        self.x = 6
        self.y = 4
        self.position = np.array([self.x * 16 + 19, self.y * 16 + 51, (self.x + 1) * 16 + 13, (self.y + 1) * 16 + 45])

    def change_position(self):
        self.position = np.array([self.x * 16 + 19, self.y * 16 + 51, (self.x + 1) * 16 + 13, (self.y + 1) * 16 + 45])

    def move(self, command = [False, False, False, False]):
        if command != [False, False, False, False] and self.movement == [False, False, False, False]:
            self.movement = command
            self.state = None
            self.outline = "#0000FF" #검정색상 코드!
            return
        elif command == [False, False, False, False] and self.movement != [False, False, False, False]:
            self.state = 'move'
            self.outline = "#FF0000" #빨강색상 코드!

            if self.movement[0] and self.y != 0:
                self.y -= 1
                self.change_position()

            elif self.movement[1] and self.y != 9:
                self.y += 1
                self.change_position()

            elif self.movement[2] and self.x != 0:
                self.x -= 1
                self.change_position()
                
            elif self.movement[3] and self.x != 12:
                self.x += 1
                self.change_position()
            
            self.movement = [False, False, False, False]

