import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_values,squares,linewidth = 5)
plt.rcParams['font.sans-serif'] = ['SimHei']
				
"""设置图表标题并给坐标轴加上标签"""
plt.title("这是一张图表",fontsize = 24)
plt.xlabel('Value',fontsize = 14)
plt.ylabel('Square of value',fontsize = 14)

"""设置刻度标记的大小"""
plt.tick_params(axis='both',labelsize = 14)

plt.show()
				
