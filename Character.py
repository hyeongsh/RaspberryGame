import numpy as np

class Character:
    def __init__(self, width, height):
        self.appearance = 'rectangle'
        self.state = None
        self.position = np.array([width/2 - 21, height/2 - 21, width/2 + 1, height/2 + 1])
        self.outline = "#FFFFFF"

    def move(self, command = [False, False, False, False]):
        if command == [False, False, False, False]:
            self.state = None
            self.outline = "#0000FF" #검정색상 코드!
        
        else:
            self.state = 'move'
            self.outline = "#FF0000" #빨강색상 코드!

            if command[0]:
                self.position[1] -= 20
                self.position[3] -= 20

            elif command[1]:
                self.position[1] += 20
                self.position[3] += 20

            elif command[2]:
                self.position[0] -= 20
                self.position[2] -= 20
                
            elif command[3]:
                self.position[0] += 20
                self.position[2] += 20