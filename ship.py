import pygame as py
from PIL import Image
import os
class Ship():
	# управление кораблём
	def __init__(self,ai_game):
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		
		#Загрузим изображение корабля
		self.Image = py.image.load(
			"C:\\Users\\semn-\\PycharmProjects\\AlienIsol\\images\\new_space_ship.png")
		self.rect = self.Image.get_rect()
		# Появление корабля снизу экрана
		self.rect.midbottom = self.screen_rect.midbottom
		
	def blitme(self):
		#корабль в текущей позиции
		self.screen.blit(self.Image, self.rect)
	
def resize_im(path):
	img=Image.open(path)
	img=img.resize((75,75))
	img.save(f'{os.path.dirname(path)}\\new_{os.path.basename(path)}')
	
resize_im("C:\\Users\\semn-\\PycharmProjects\\AlienIsol\\images\\space_ship.png")