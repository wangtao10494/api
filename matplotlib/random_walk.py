from random import choice

class RandomWalk():
	"""生成随机数据的类"""
	
	def __init__(self,num_points = 100):
		"""初始化随机漫步的属性"""
		self.num_points = num_points
		
		#所有漫步都始于（0,0）
		self.x_values = [0]
		self.y_values = [0]
		
	def get_step(self):
		"""前进方向和前进距离"""
		direction = choice([1,-1])
		distance = choice([0,1,2,3,4])
		return direction * distance
		
	def fill_walk(self):
		"""计算随机漫步包含的所有点"""
		#不断漫步，直到列表达到指定的长度
		while len(self.x_values) < self.num_points:
			x_step = self.get_step()
			y_step = self.get_step()
			
			if x_step == 0 and y_step == 0 :
				continue
			
		#计算下一个点的x和y值
		next_x = self.x_values[-1] + x_step
		next_y = self.y_values[-1] + y_step
		
		self.x_values.append(next_x)
		self.y_values.append(next_y)
			
		
		
