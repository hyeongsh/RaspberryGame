import numpy as np

class Character:
    def __init__(self, width, height):
        self.appearance = 'rectangle'
        self.state = None
        self.x = 6
        self.y = 4
        self.position = np.array([self.x * 16 + 16, self.y * 16 + 48, (self.x + 1) * 16 + 16, (self.y + 1) * 16 + 48])
        self.outline = "#FFFFFF"

    def change_position(self):
        self.position = np.array([self.x * 16 + 16, self.y * 16 + 48, (self.x + 1) * 16 + 16, (self.y + 1) * 16 + 48])

    def move(self, command = [False, False, False, False]):
        if command == [False, False, False, False]:
            self.state = None
            self.outline = "#0000FF" #검정색상 코드!
        
        else:
            self.state = 'move'
            self.outline = "#FF0000" #빨강색상 코드!

            if command[0]:
                if self.y == 0:
                    return
                self.y -= 1
                self.change_position()

            elif command[1]:
                if self.y == 9:
                    return
                self.y += 1
                self.change_position()

            elif command[2]:
                if self.x == 0:
                    return
                self.x -= 1
                self.change_position()
                
            elif command[3]:
                if self.x == 12:
                    return
                self.x += 1
                self.change_position()

