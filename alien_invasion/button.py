import pygame.font
from settings import Settings
class Button():
	
	def __init__(self,ai_settings,screen,msg):
		"""初始化按钮属性"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		"""设置按钮的尺寸和其他属性"""
		self.width,self.height = 200,50
		self.button_color = (150,150,150)
		self.text_color = (255,255,255)
		self.font = pygame.font.SysFont('SimHei',24)
		
		"""创建按钮的rect对象，并使其居中"""
		self.begin_rect = pygame.Rect(0,0,self.width,self.height)
		self.begin_rect.center = self.screen_rect.center
		self.over_rect = pygame.Rect(0,0,self.width,self.height)
		self.over_rect.x = self.screen_rect.centerx - 100
		self.over_rect.y = self.screen_rect.centery - 100
		
		"""按钮标签只需创建一次"""
		self.prep_msg(msg)
		self.prep_msg1(msg)

	def prep_msg(self,msg):
		"""将msg渲染为图像，并使其在按钮上居中"""
		self.msg_image = self.font.render(msg,True,self.text_color,
					self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.screen_rect.center
		self.screen.fill(self.button_color,self.begin_rect)
		self.screen.blit(self.msg_image,self.msg_image_rect)
		
	def prep_msg1(self,msg):
		self.msg_image = self.font.render(msg,True,self.text_color,
					self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.over_rect.center
#		self.msg_image_rect.y = self.screen_rect.centery - 100
		self.screen.fill(self.button_color,self.over_rect)
		self.screen.blit(self.msg_image,self.msg_image_rect)
		

		
		
	

