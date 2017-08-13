import matplotlib.pyplot as plt
from random_die import Random_die

while True:
	rd = Random_die()
	rd.fill_walk()
	
	#设置绘图窗口的尺寸
	plt.figure(dpi=128,figsize=(10,6))
	
	point_numbers = list(range(rd.num_points))
	plt.scatter(rd.x_values,rd.y_values,c='red')
					

					
	#隐藏坐标轴
#	plt.axes().get_xaxis().set_visible(False)
#	plt.axes().get_yaxis().set_visible(False)
	
	plt.show()
	
	keep_running = input("Make another walk?(y/n):")
	if keep_running == 'n':
		break
