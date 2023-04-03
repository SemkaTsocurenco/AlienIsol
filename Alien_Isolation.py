# Создадим класс для окна в pygame

import sys
import pygame as py

class AlienInvasion:
	
	def __init__(self):
		# инициализирует работу класса
		py.init()
		self.screen = py.display.set_mode((1200 , 800))
		py.display.set_caption("Alien Invasion")
		# Цвет фона
		self.bg_color = (230, 230, 230)
		
		
	
	def run_game(self):
		# начинает игру
		while True:
			#Отслеживает события на клавиатуре и мышке
			for event in py.event.get():
				if event.type == py.QUIT:
					sys.exit()
			#при каждом проходе цикла прописовывается экран
			self.screen.fill(self.bg_color)
			#последний прорисованный экран
			py.display.flip()
			


if __name__ == '__main__':
	# создать экземпляр
	ai=AlienInvasion()
	ai.run_game()
