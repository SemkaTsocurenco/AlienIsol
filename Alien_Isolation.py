# Создадим класс для окна в pygame

import sys
import pygame as py
from settings import Settings
from ship import Ship
from bullet import Bullet
from Alien import Alien
class AlienInvasion():
	
	def __init__(self):
		# инициализирует работу класса
		py.init()
		self.settings=Settings()
		# размер экрана из настроек
		self.screen = py.display.set_mode((0, 0), py.FULLSCREEN)
		self.buff_wigth = self.settings.screen_width
		self.buff_heigth = self.settings.screen_height
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		py.display.set_caption("Alien Invasion")
		# Прописовка корабля
		self.ship = Ship(self)
		self.bullets = py.sprite.Group()
		self.alien = py.sprite.Group()
		self._create_fleet()
	
	def run_game(self):
		# начинает игру
		while True:
			#Отслеживает события на клавиатуре и мышке
			self._check_ivents()  # проверка на ивенты
			self._update_screen() #при каждом проходе цикла прописовывается экран
			self.ship.Update() # обновляет положение корабля
			self.bullets.update()#обновляет положение пули
			self._del_bullets() # удаляет патроны за экраном
			
	def _check_ivents(self):   #вспомогательный класс для run game
		# ждёт нажатия клавиш и события мышки
		for event in py.event.get():
			if event.type == py.QUIT:
				sys.exit()
			elif event.type == py.KEYDOWN:
				self._check_keydown(event)   # события для нажатой клавиши
			elif event.type == py.KEYUP:
				self._check_keyup(event)  # события для отпущенной клавиши
				
	def _check_keydown(self,event):    # вспомогательный для check_ivents
		# для ивентов нажатой клавиши
		if event.key == py.K_d:
			self.ship.moving_right = True
		elif event.key == py.K_a:
			self.ship.moving_left = True
		elif event.key == py.K_ESCAPE:
			sys.exit()
		elif event.key == py.K_o:
			self.switch_fullscreen()
		elif event.key == py.K_SPACE:
			self._fire_bullet()
			
	
	def _check_keyup(self,event):  # вспомогательный для check_ivents
		# для ивентов отпущенной клавиши
		if event.key == py.K_d:
			self.ship.moving_right = False
		elif event.key == py.K_a:
			self.ship.moving_left = False
			
			
	def _update_screen(self):  #вспомогательный класс для run game
		# обновляет экран
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.alien.draw(self.screen)
		# последний прорисованный экран
		py.display.flip()
		

	def switch_fullscreen(self):
		if py.display.get_window_size() == (self.buff_wigth,self.buff_heigth):
			# полноэкранный режим
			self.screen = py.display.set_mode((0, 0), py.FULLSCREEN)
			self.settings.screen_width = self.screen.get_rect().width
			self.settings.screen_height = self.screen.get_rect().height
			
			self.ship.rect.midbottom = self.screen.get_rect().midbottom
		else:
			self.settings.screen_width = self.buff_wigth
			self.settings.screen_height = self.buff_heigth
			self.screen = py.display.set_mode((self.settings.screen_width, self.settings.screen_height))
			self.ship.rect.midbottom = self.screen.get_rect().midbottom
		self._update_screen()

	def _fire_bullet(self):
		# создаю новый снаряд
		if len(self.bullets) < self.settings.bullets_allowed:  # ограниченное кол-во зарядов
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)
	
	def _del_bullets(self):
		for bullet in self.bullets.copy():  # copy для того, чтобы можно было изменять bullets
			if bullet.rect.bottom <=0:
				self.bullets.remove(bullet)
				
	def _create_fleet(self):
		# создание флота
		# создаём пришельца и вычислим количество пришельцев в ряду
		#интервал между пришельцами равен одному пришельцу
		alien = Alien(self)
		alien_width = alien.rect.width
		available_space_x = self.settings.screen_width - (2 * alien_width)
		num_aliens_x = available_space_x // (2 * alien_width)
		
		#Создадим первый ряд пришельцев
		for alien_num in range(num_aliens_x):
			alien = Alien(self)
			alien.x = alien_width + 2 * alien_width * alien_num
			alien.rect.x = alien.x
			self.alien.add(alien)
			
			
	

if __name__ == '__main__':
	# создать экземпляр
	ai=AlienInvasion()
	ai.run_game()