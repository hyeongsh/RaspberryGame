from PIL import Image, ImageDraw, ImageFont
from colorsys import hsv_to_rgb
import time

from Joystick import Joystick
from Character import Character
from BlockManager import BlockManager
from GameManager import GameManager

def main():
	joystick = Joystick()
	my_image = Image.new("RGB", (joystick.width, joystick.height))
	my_draw = ImageDraw.Draw(my_image)
	my_pos = Character()
	blockManager = BlockManager()
	gameManager = GameManager()
	
	flag = 0
	while True:
		my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 255, 255, 100))	
		match flag:
			case 0:
				flag = draw_main(my_draw, joystick, gameManager, blockManager, my_pos)
			case 1:
				flag = draw_game(my_draw, joystick, gameManager, blockManager, my_pos)
			case 2:
				flag = draw_menu(my_draw, joystick, gameManager)
			case 3:
				flag = draw_finish(my_draw, joystick, gameManager)
			case 4:
				break
		joystick.disp.image(my_image)
	my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (0, 0, 0, 0))	
	joystick.disp.image(my_image)
	


def draw_main(my_draw, joystick, gameManager, blockManager, my_pos):
	font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
	font_size = 30
	font = ImageFont.truetype(font_path, font_size)
	my_draw.rectangle(tuple([40, 30, 200, 70]), fill="white", width=1, outline='#000000')
	my_draw.text((60, 35), "Level 1", fill="black", font=font)
	my_draw.rectangle(tuple([40, 75, 200, 115]), fill="white", width=1, outline='#000000')
	my_draw.text((60, 80), "Level 2", fill="black", font=font)
	my_draw.rectangle(tuple([40, 120, 200, 160]), fill="white", width=1, outline='#000000')
	my_draw.text((60, 125), "Level 3", fill="black", font=font)
	my_draw.rectangle(tuple([40, 165, 200, 205]), fill="white", width=1, outline='#000000')
	my_draw.text((80, 170), "EXIT", fill="black", font=font)

	if joystick.check_button_U() and gameManager.level > 1:  # up pressed
		gameManager.level -= 1
	if joystick.check_button_D() and gameManager.level < 4:  # down pressed
		gameManager.level += 1
	if joystick.check_button_A():
		if gameManager.level != 4:
			gameManager.start_game(blockManager, my_pos)
			return 1
		else:
			return 4
	
	my_draw.rectangle(tuple([40, 30 + ((gameManager.level - 1) * 45), 200, 70 + ((gameManager.level - 1) * 45)]), width=3, outline='red')
	return 0

def draw_game(my_draw, joystick, gameManager, blockManager, my_pos):
	if gameManager.is_ending():
		return 3
	if joystick.check_button_U() and my_pos.y != 0:
		my_pos.y -= 1
	if joystick.check_button_D() and my_pos.y != 9:
		my_pos.y += 1
	if joystick.check_button_L() and my_pos.x != 0:
		my_pos.x -= 1
	if joystick.check_button_R() and my_pos.x != 12:
		my_pos.x += 1
	if joystick.check_button_A():
		blockManager.click_blocks(my_pos.x, my_pos.y, gameManager)
	if joystick.check_button_B():
		gameManager.stop_time = time.time()
		return 2
	
	my_pos.change_position()

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
					my_draw.polygon([((x1 + x2) / 2, y1), (x2, (y1 + y2) / 2), 
									 ((x1 + x2) / 2, y2), (x1, (y1 + y2) / 2)], fill=block.adjust_fill(), outline='#000000')
				if block.fill == "orange":
					x1, y1, x2, y2 = block.pattern
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
	return 1

def draw_menu(my_draw, joystick, gameManager):
	gameManager.time_stop()
	if joystick.check_button_A():
		gameManager.level = 1
		return 0
	if joystick.check_button_B():
		return 1
		
	my_draw.rectangle(tuple([40, 80, 200, 160]), fill="white", width=1, outline='#000000')
	font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
	font = ImageFont.truetype(font_path, 20)
	my_draw.text((80, 90), f"HOME?", fill="black", font=font)
	my_draw.text((50, 130), f"A: Yes, B: No", fill="black", font=font)
	return 2

def draw_finish(my_draw, joystick, gameManager):
	if joystick.check_button_A():
		return 0
	if gameManager.finish == 0:
		gameManager.finish = 90 - gameManager.time_check()
	font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
	font_size = 30
	font = ImageFont.truetype(font_path, font_size)
	if gameManager.block_check() == 100 - ((3 - gameManager.level) * 30):
		my_draw.text((70, 80), f"CLEAR", fill="black", font=font)
		my_draw.text((30, 120), f"{gameManager.finish} Second", fill="black", font=font)
	else:
		my_draw.text((20, 80), f"GAME OVER", fill="black", font=font)
		if gameManager.block_check() < 10:
			my_draw.text((110, 120), f"{gameManager.block_check()}", fill="black", font=font)
		elif gameManager.block_check() < 100:
			my_draw.text((100, 120), f"{gameManager.block_check()}", fill="black", font=font)
	return 3
	
if __name__ == '__main__':
	main()