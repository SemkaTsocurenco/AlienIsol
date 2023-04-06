import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	
	def __init__(self,ai_game):
		super().__init__()
		self.screen=ai_game.screen
		self.image = pygame.image.load(
			"C:\\Users\\semn-\\PycharmProjects\\AlienIsol\\images\\new_alien.png")
		self.rect = self.image.get_rect()
		
		# каждый новый прешелец появляется в левом верхнем экране
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		self.x = float(self.rect.x)