# Создадим класс для окна в pygame

import sys
import pygame as py
from settings import Settings
from ship import Ship
class AlienInvasion():
	
	def __init__(self):
		# инициализирует работу класса
		py.init()
		self.settings=Settings()
		
		self.screen = py.display.set_mode((self.settings.screen_width,self.settings.screen_height))
		py.display.set_caption("Alien Invasion")
		# Прописовка корабля
		self.ship = Ship(self)
		
	
	def run_game(self):
		# начинает игру
		while True:
			#Отслеживает события на клавиатуре и мышке
			self._check_ivents()  # проверка на ивенты
			self._update_screen() #при каждом проходе цикла прописовывается экран
			self.ship.Update() # обновляет положение корабля
			
	def _check_ivents(self):   #вспомогательный класс для run game
		# ждёт нажатия клавиш и события мышки
		for event in py.event.get():
			if event.type == py.QUIT:
				sys.exit()
				
			elif event.type == py.KEYDOWN:
				if event.key == py.K_d:
					self.ship.moving_right = True
				elif event.key == py.K_a:
					self.ship.moving_left = True
					
			elif event.type == py.KEYUP:
				if event.key == py.K_d:
					self.ship.moving_right = False
				elif event.key == py.K_a:
					self.ship.moving_left = False
				
		
	def _update_screen(self):  #вспомогательный класс для run game
		# обновляет экран
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		# последний прорисованный экран
		py.display.flip()

	
	
if __name__ == '__main__':
	# создать экземпляр
	ai=AlienInvasion()
	ai.run_game()
