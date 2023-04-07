# Создадим класс для окна в pygame

import sys
from time import sleep
import pygame as py
from settings import Settings
from game_stat import stat
from ship import Ship
from bullet import Bullet
from Alien import Alien
class AlienInvasion():
	
	def __init__(self):
		# инициализирует работу класса
		py.init()
		self.settings=Settings()
		self.stat = stat(self)
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
		self.aliens = py.sprite.Group()
		self._create_fleet()
		
		
	
	def run_game(self):
		# начинает игру
		while True:
			#Отслеживает события на клавиатуре и мышке
			self._check_ivents()  # проверка на ивенты
			if self.stat.game_active:
				self.ship.Update() # обновляет положение корабля
				self.update_bullets()#обновляет положение пули
				self._update_aliens() # урпавляет флотом пришельцев
			self._update_screen() #при каждом проходе цикла прописовывается экран

			
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
		self.aliens.draw(self.screen)
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


	def update_bullets(self):
		self.bullets.update()
		self._del_bullets()
		# проверика попадания в пришельцев и их уничтожение
		self._check_bullet_alien_collide()
		
	def _check_bullet_alien_collide(self):
		collisions = py.sprite.groupcollide(
			self.bullets, self.aliens, True, True)
		# первый Т показывает надо ли уничтожать пулю, второй-пришельца
		if not self.aliens:
			# удаление существующих снарядов и добавление нового флота
			self.bullets.empty()
			self._create_fleet()
			self.settings.alien_speed += 0.5
			
		
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
		alien_width, alien_height = alien.rect.size
		available_space_x = self.settings.screen_width - (2 * alien_width)
		num_aliens_x = available_space_x // (2 * alien_width)
		
		# определим количество рядов на экране
		ship_height = self.ship.rect.height
		available_space_y = self.settings.screen_height - (7 * alien_height) - ship_height
		number_rows = available_space_y // (2 * alien_height)
		
		# Создадим первый ряд пришельцев
		for row_num in range(number_rows):
			for alien_num in range(num_aliens_x):
				self._create_alien(alien_num , row_num)
	def _create_alien(self, alien_num, row_num):
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x= alien_width + 2 * alien_width * alien_num
		alien.y= alien_height + 2 * alien_height * row_num
		alien.rect.x = alien_width + 2 * alien_width * alien_num
		alien.rect.y = alien_height + 2 * alien_height * row_num
		self.aliens.add(alien)
		
	
	def _update_aliens(self):
		self._check_fleet_edges()
		self.aliens.update()
		# колизия пришелец - корабль
		if py.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()
		self._check_aliens_bottom()
		
			
	def _ship_hit(self):
		if self.stat.ships_left > 0:
			self.stat.ships_left -= 1
			#очистка
			self.aliens.empty()
			self.bullets.empty()
			#новый флот
			self._create_fleet()
			self.ship.center_ship()
			# небольшая пауза
			sleep(0.5)
		else:
			self.stat.game_active = False
		
	def _check_aliens_bottom(self):
		# добрались ли пришельцы до низа экрана
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
				self._ship_hit()
				break
	def _check_fleet_edges(self):
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break
		
	
	def _change_fleet_direction(self):
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop
		self.settings.fleet_direction *= -1
	

		

if __name__ == '__main__':
	# создать экземпляр
	ai=AlienInvasion()
	ai.run_game()
	