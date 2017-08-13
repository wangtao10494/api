import matplotlib.pyplot as plt

x_values = list(range(1,5))
y_values = [x**3 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,
				edgecolor = 'none', s=40)

plt.rcParams['font.sans-serif'] = ['SimHei']
				
"""设置图表标题并给坐标轴加上标签"""
plt.title("这是一张图表",fontsize = 24)
plt.xlabel('Value',fontsize = 14)
plt.ylabel('Square of value',fontsize = 14)

"""设置刻度标记的大小"""
plt.tick_params(axis='both',which='major',labelsize = 14)
plt.show()
#plt.savefig('首次生成的图表.png',bbox_inches = 'tight')
