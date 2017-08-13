import pygame
from alien import Alien
from pygame.sprite import Sprite

class Abullet(Sprite):
	"""对外星人发射的子弹进行管理的类"""
	
	def __init__(self,ai_settings,screen,aliens):
		"""在飞船所处的位置创建一个子弹对象"""
		super(Abullet,self).__init__()
		self.screen = screen
		
		"""在（0,0）处创建一个表示子弹的矩形，在设置正确的位置"""
		self.rect = pygame.Rect(0,0,ai_settings.abullet_width,
			ai_settings.abullet_height)
		for alien in aliens:
			self.rect.centerx = alien.rect.x
			self.rect.top = alien.rect.y
		
		"""存储用小数表示的子弹位置"""
		self.y = float(self.rect.y)
		
		self.color = ai_settings.abullet_color
		self.speed_factor = ai_settings.abullet_speed_factor
		
	def update(self):
		"""向上移动子弹"""
		"""更新表示子弹位置的小数值"""
		self.y += self.speed_factor
		"""更新表示子弹的rect的位置"""
		self.rect.y = self.y
		
	def draw_abullet(self):
		"""在屏幕上绘制子弹"""
		pygame.draw.rect(self.screen,self.color,self.rect)
