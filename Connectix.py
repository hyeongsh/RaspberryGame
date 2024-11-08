from PIL import Image, ImageDraw, ImageFont
import time
import random
from colorsys import hsv_to_rgb

from Character import Character
from Joystick import Joystick
from Block import Block

def main():
    joystick = Joystick()
    my_image = Image.new("RGB", (joystick.width, joystick.height))
    my_draw = ImageDraw.Draw(my_image)
    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(255, 0, 0, 100))
    joystick.disp.image(my_image)
    # 잔상이 남지 않는 코드
    my_pos = Character(joystick.width, joystick.height)
    while True:
        time.sleep(0.05)
        command = [False, False, False, False]
        if not joystick.button_U.value:  # up pressed
            command[0] = True

        if not joystick.button_D.value:  # down pressed
            command[1] = True

        if not joystick.button_L.value:  # left pressed
            command[2] = True

        if not joystick.button_R.value:  # right pressed
            command[3] = True
        
        my_pos.move(command)

        my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 255, 255, 100))
        for x in range(0, joystick.width, 16):
            my_draw.line((x, 0, x, joystick.height), fill="gray", width=1)
        for y in range(0, joystick.height, 16):
            my_draw.line((0, y, joystick.width, y), fill="gray", width=1)
        my_draw.rectangle(tuple([0, 0, 16, 240]), fill="white", width=1, outline='#000000')
        my_draw.rectangle(tuple([224, 0, 240, 240]), fill="white", width=1, outline='#000000')
        my_draw.rectangle(tuple([0, 0, 240, 48]), fill="white", width=1, outline='#000000')
        my_draw.rectangle(tuple([0, 208, 240, 240]), fill="white", width=1, outline='#000000')

        my_draw.rectangle(tuple(my_pos.position), outline = my_pos.outline)

        joystick.disp.image(my_image)


if __name__ == '__main__':
    main()