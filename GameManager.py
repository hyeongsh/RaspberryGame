import time
from BlockManager import BlockManager
from Character import Character

class GameManager:
	def __init__(self):
		self.start_time = time.time()
		self.stop_time = 0
		self.offset = 0
		self.end_time = self.start_time + 90
		self.finish = 0
		self.block_count = 0

	def restart_game(self, blockManager, my_pos):
		self.start_time = time.time()
		self.end_time = self.start_time + 90
		self.finish = 0
		self.block_count = 0
		my_pos.start_pos()
		blockManager.make_map()
	
	def time_stop(self):
		cur_time = time.time()
		self.offset = int(cur_time - self.stop_time)

	def time_check(self):
		cur_time = time.time()
		return int(self.end_time - cur_time + self.offset)
	
	def is_ending(self):
		cur_time = time.time()
		if int(self.end_time - cur_time + self.offset) <= 0 or self.block_count == 100:
			return True
		return False

	def block_check(self):
		return self.block_count