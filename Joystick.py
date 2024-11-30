from digitalio import DigitalInOut, Direction
from adafruit_rgb_display import st7789
import board

class Joystick:
    def __init__(self):
        self.cs_pin = DigitalInOut(board.CE0)
        self.dc_pin = DigitalInOut(board.D25)
        self.reset_pin = DigitalInOut(board.D24)
        self.BAUDRATE = 24000000

        self.spi = board.SPI()
        self.disp = st7789.ST7789(
                    self.spi,
                    height=240,
                    y_offset=80,
                    rotation=180,
                    cs=self.cs_pin,
                    dc=self.dc_pin,
                    rst=self.reset_pin,
                    baudrate=self.BAUDRATE,
                    )

        # Input pins:
        self.button_A = DigitalInOut(board.D5)
        self.button_A.direction = Direction.INPUT

        self.button_B = DigitalInOut(board.D6)
        self.button_B.direction = Direction.INPUT

        self.button_L = DigitalInOut(board.D27)
        self.button_L.direction = Direction.INPUT

        self.button_R = DigitalInOut(board.D23)
        self.button_R.direction = Direction.INPUT

        self.button_U = DigitalInOut(board.D17)
        self.button_U.direction = Direction.INPUT

        self.button_D = DigitalInOut(board.D22)
        self.button_D.direction = Direction.INPUT

        self.button_C = DigitalInOut(board.D4)
        self.button_C.direction = Direction.INPUT

        # Turn on the Backlight
        self.backlight = DigitalInOut(board.D26)
        self.backlight.switch_to_output()
        self.backlight.value = True

        # Create blank image for drawing.
        # Make sure to create image with mode 'RGB' for color.
        self.width = self.disp.width
        self.height = self.disp.height

        self.stack_U = False
        self.stack_D = False
        self.stack_L = False
        self.stack_R = False
        self.stack_A = False
        self.stack_B = False

    def check_button_U(self):
        if self.button_U.value and self.stack_U:
            self.stack_U = False
            return True
        elif not self.button_U.value:
            self.stack_U = True
            self.stack_D = False
            self.stack_L = False
            self.stack_R = False
            self.stack_A = False
            self.stack_B = False
            return False
        else:
            return False 
        
    def check_button_D(self):
        if not self.button_D.value:
            self.stack_U = False
            self.stack_D = True
            self.stack_L = False
            self.stack_R = False
            self.stack_A = False
            self.stack_B = False
            return False
        elif self.button_D.value and self.stack_D:
            self.stack_D = False
            return True
        else:
            return False 
        
    def check_button_L(self):
        if self.button_L.value and self.stack_L:
            self.stack_L = False
            return True
        elif not self.button_L.value:
            self.stack_U = False
            self.stack_D = False
            self.stack_L = True
            self.stack_R = False
            self.stack_A = False
            self.stack_B = False
            return False
        else:
            return False 
        
    def check_button_R(self):
        if self.button_R.value and self.stack_R:
            self.stack_R = False
            return True
        elif not self.button_R.value:
            self.stack_U = False
            self.stack_D = False
            self.stack_L = False
            self.stack_R = True
            self.stack_A = False
            self.stack_B = False
            return False
        else:
            return False 
        
    def check_button_A(self):
        if self.button_A.value and self.stack_A:
            self.stack_A = False
            return True
        elif not self.button_A.value:
            self.stack_U = False
            self.stack_D = False
            self.stack_L = False
            self.stack_R = False
            self.stack_A = True
            self.stack_B = False
            return False
        else:
            return False 
        
    def check_button_B(self):
        if self.button_B.value and self.stack_B:
            self.stack_B = False
            return True
        elif not self.button_B.value:
            self.stack_U = False
            self.stack_D = False
            self.stack_L = False
            self.stack_R = False
            self.stack_A = False
            self.stack_B = True
            return False
        else:
            return False 