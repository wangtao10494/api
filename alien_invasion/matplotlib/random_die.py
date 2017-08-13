from random import choice
from random import randint

class Random_die():
	
	def __init__(self,num_points=2,num_sides=6):
		self.num_points = num_points
		self.num_sides = num_sides
		"""开始时没有坐标"""
		self.x_values=[]
		self.y_values=[]
		
	def roll(self):
		return randint(1,self.num_sides)
		
	def fill_walk(self):
		for value in range(self.num_points):
			x_step = self.roll()
			
			self.x_values.append(x_step)
			self.y_values.append(x_step)
	
