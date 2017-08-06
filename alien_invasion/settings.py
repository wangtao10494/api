class Settings():
	"""存储【外星人入侵】的所有设置的类"""
	def __init__(self):
		"""初始化游戏的静态设置"""
		self.screen_width = 600
		self.screen_height = 600
		self.bg_color = (50,50,50)
		
		"""飞船设置"""
		self.ship_limit = 3
		
		"""飞船子弹设置"""
		self.bullet_width = 6
		self.bullet_height = 30
		self.bullet_color = 160,160,160
		self.bullets_allowed = 5
		
		"""外星人子弹设置"""
		self.abullet_width = 6
		self.abullet_height = 20
		self.abullet_color = 160,160,160
		
		
		"""外星人设置"""
		self.fleet_drop_speed = 10
		
		"""以什么样的速度加快游戏节奏"""
		self.speedup_scale = 1.1
		
		"""外星人分数提高速度"""
		self.score_scale = 2
		
		self.initialize_dynamic_settings()
		
		
	def initialize_dynamic_settings(self):
		"""初始化随游戏进行而变化的设置"""
		self.ship_speed_factor = 0.2
		self.bullet_speed_factor = 1
		self.alien_speed_factor = 0.2
		self.abullet_speed_factor = 1
		self.alien_points = 10
		
		"""fleet_direction为1表示向右：为-1表示向左"""
		self.fleet_direction = 1
		
		
	def increase_speed(self):
		"""提高速度设置"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)
		
		
