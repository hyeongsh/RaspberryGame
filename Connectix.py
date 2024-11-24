from PIL import Image, ImageDraw, ImageFont
from colorsys import hsv_to_rgb
import time

from Character import Character
from Joystick import Joystick
from BlockManager import BlockManager
from GameManager import GameManager

def main():
    joystick = Joystick()
    my_image = Image.new("RGB", (joystick.width, joystick.height))
    my_draw = ImageDraw.Draw(my_image)
    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(255, 0, 0, 100))
    joystick.disp.image(my_image)
    my_pos = Character()
    blockManager = BlockManager()
    gameManager = GameManager()

    click_button = False
    restart_button = False
    restart = False
    is_finish = False
    while True:
        if restart:
            gameManager.time_stop()
            if not joystick.button_A.value:
                restart_button = True
                gameManager.restart_game(blockManager, my_pos)
            if not joystick.button_B.value:
                restart_button = True
            if joystick.button_B.value and restart_button:
                restart_button = False
                restart = False
        command = [False, False, False, False]
        if not joystick.button_U.value:  # up pressed
            command[0] = True
        if not joystick.button_D.value:  # down pressed
            command[1] = True
        if not joystick.button_L.value:  # left pressed
            command[2] = True
        if not joystick.button_R.value:  # right pressed
            command[3] = True
        if not joystick.button_A.value:
            click_button = True
        if not joystick.button_B.value:
            restart_button = True

        if joystick.button_A.value and click_button:
            click_button = False
            blockManager.click_blocks(my_pos.x, my_pos.y, gameManager)
        
        if joystick.button_B.value and restart_button:
            restart_button = False
            restart = True
            gameManager.stop_time = time.time()
        
        my_pos.move(command)

        # 전체 그림
        my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 255, 255, 100))
        if restart:
            my_draw.rectangle(tuple([40, 80, 200, 160]), fill="white", width=1, outline='#000000')
            font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
            font = ImageFont.truetype(font_path, 20)
            my_draw.text((70, 90), f"RESTART?", fill="black", font=font)
            my_draw.text((50, 130), f"A: Yes, B: No", fill="black", font=font)
        elif not gameManager.is_ending():
            draw_game(my_draw, gameManager, my_pos, blockManager)
        else:
            is_finish = draw_finish(my_draw, gameManager, is_finish)
        joystick.disp.image(my_image)


def draw_game(my_draw, gameManager, my_pos, blockManager):
    # 라인 그리기
    for x in range(0, 240, 16):
        my_draw.line((x, 0, x, 240), fill="gray", width=1)
    for y in range(0, 240, 16):
        my_draw.line((0, y, 240, y), fill="gray", width=1)
    # 외부 라인 (점수, 시간 표시)
    my_draw.rectangle(tuple([0, 0, 16, 240]), fill="white", width=1, outline='#000000')
    my_draw.rectangle(tuple([224, 0, 240, 240]), fill="white", width=1, outline='#000000')
    my_draw.rectangle(tuple([0, 0, 240, 48]), fill="white", width=1, outline='#000000')
    my_draw.rectangle(tuple([0, 208, 240, 240]), fill="white", width=1, outline='#000000')
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    font_size = 30
    font = ImageFont.truetype(font_path, font_size)
    my_draw.text((10, 10), f"Time: {gameManager.time_check()}", fill="black", font=font)
    my_draw.text((10, 210), f"Block: {gameManager.block_check()}", fill="black", font=font)
    # 블록 그리기
    for row in blockManager.blocks:
        for block in row:
            if block:
                my_draw.rectangle(tuple(block.position), fill=block.fill, outline='#000000')
                if block.fill == "red":
                    my_draw.ellipse(tuple(block.pattern), fill=block.adjust_fill(), outline='#000000')
                if block.fill == "green":
                    my_draw.rectangle(tuple(block.pattern), fill=block.adjust_fill(), outline='#000000')
                if block.fill == "blue":
                    x1, y1, x2, y2 = block.pattern
                    my_draw.polygon([((x1 + x2) // 2, y1), (x2, (y1 + y2) // 2), 
                                     ((x1 + x2) // 2, y2), (x1, (y1 + y2) // 2)], fill=block.adjust_fill(), outline='#000000')
                if block.fill == "orange":
                    x1, y1, x2, y2 = block.pattern
                    mid_x = (x1 + x2) / 2
                    mid_y = (y1 + y2) / 2
                    my_draw.polygon([(x1, y1), ((x1 + x2) // 2, y2), (x2, y1)], fill=block.adjust_fill(), outline='#000000')
                if block.fill == "pink":
                    x1, y1, x2, y2 = block.pattern
                    my_draw.polygon([(x1, y2), ((x1 + x2) / 2, y1), (x2, y2)], fill=block.adjust_fill(), outline='#000000')
    my_draw.ellipse(tuple(my_pos.position), fill="black", outline=my_pos.outline)
    for block in blockManager.break_block:
        my_draw.line(((my_pos.position[0] + my_pos.position[2]) / 2,
                      (my_pos.position[1] + my_pos.position[3]) / 2,
                      (block.position[0] + block.position[2]) / 2,
                      (block.position[1] + block.position[3]) / 2
                      ), fill="black", width=5)
        my_draw.rectangle(tuple(block.position), fill=block.fill, outline='#000000')
        block.remove_block()
        if block.position[0] >= block.position[2]:
            blockManager.break_block.clear()

def draw_finish(my_draw, gameManager, is_finish):
    if not is_finish:
        gameManager.finish = 90 - gameManager.time_check()
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    font_size = 30
    font = ImageFont.truetype(font_path, font_size)
    if gameManager.block_check() == 100:
        my_draw.text((70, 100), f"CLEAR", fill="black", font=font)
        my_draw.text((30, 140), f"{gameManager.finish} Second", fill="black", font=font)
    else:
        my_draw.text((20, 100), f"GAME OVER", fill="black", font=font)
        if gameManager.block_check() < 10:
            my_draw.text((110, 140), f"{gameManager.block_check()}", fill="black", font=font)
        elif gameManager.block_check() < 100:
            my_draw.text((100, 140), f"{gameManager.block_check()}", fill="black", font=font)
    return True

if __name__ == '__main__':
    main()