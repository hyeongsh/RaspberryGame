import numpy as np

class Character:
    def __init__(self, width, height):
        self.appearance = 'rectangle'
        self.state = None
        self.position = np.array([width/2 - 9, height/2 - 9, width/2 + 9, height/2 + 9])
        self.outline = "#FFFFFF"

    def move(self, command = [False, False, False, False]):
        if command == [False, False, False, False]:
            self.state = None
            self.outline = "#0000FF" #검정색상 코드!
        
        else:
            self.state = 'move'
            self.outline = "#FF0000" #빨강색상 코드!

            if command[0]:
                if self.position[1] < 48:
                    return
                self.position[1] -= 16
                self.position[3] -= 16

            elif command[1]:
                if self.position[3] > 208:
                    return
                self.position[1] += 16
                self.position[3] += 16

            elif command[2]:
                if self.position[0] < 16:
                    return
                self.position[0] -= 16
                self.position[2] -= 16
                
            elif command[3]:
                if self.position[2] > 224:
                    return
                self.position[0] += 16
                self.position[2] += 16