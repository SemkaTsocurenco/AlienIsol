import math

class Settings():
	# настройки игры

	def __init__(self):
		# Инициализация настроек игры
		self.screen_width=1200
		self.screen_height=800
		self.bg_color=(230, 230, 230)
		self.ship_speed=6
		self.ship_limit = 3
		#параметры пули
		self.bullet_color=(60, 60, 60)
		self.bullet_speed = 2
		self.bullet_width = 3
		self.bullet_heigth= 15
		self.bullets_allowed =6
		# Настройка пришельцев
		self.alien_speed = 1.5
		self.fleet_drop =10
		self.fleet_direction = 1 # 1 - вправо -1 - влево
		