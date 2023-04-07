import pygame


class stat():
	
	def __init__(self,ai_game):
		
		self.set = ai_game.settings
		self.reset_stat()
		
	def reset_stat(self):
		# инициализация статистки
		self.ships_left = self.set.ship_limit
		