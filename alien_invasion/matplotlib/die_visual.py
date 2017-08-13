from die import Die
import pygal

die = Die()


results = []
for roll_num in range(10):
	result = die.roll() * die.roll()
	results.append(result)
	
#分析结果
frequencies = []
for value in results:
	frequency = results.count(value)
	frequencies.append(frequency)

hist = pygal.Bar()
hist.title = '两个不同面骰子投掷1000次数据图'
hist.x_labels = sorted(results)
hist.x_title = 'results'
hist.y_title = 'Frequency of Result'

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')

