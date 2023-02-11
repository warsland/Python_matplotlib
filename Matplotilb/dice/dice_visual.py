from die import Die
import pygal

#创建骰子
die1= Die()
die2= Die()
#保存骰子投掷结果
results=[]
for roll_num in range(1000):
    result=die1.roll()*die2.roll()
    results.append(result)

#分析投掷结果
frequencies=[]
num_results=[]
for num1 in range(1,die1.num_sides+1):
    for num2 in range(1,die2.num_sides+1):
        num_result=num1*num2
        if num_result not in num_results:
            num_results.append(num_result)
num_results.sort()

for value in num_results:
    frequencie=results.count(value)
    frequencies.append(frequencie)

#分析结果可视化
#直方图实例
hist=pygal.Bar()
#标题
hist.title="Results of rolling two D6 1000 times and the result multiply"
#横坐标
x_lable=[]
for num in num_results:
    x_lable.append(str(num))
hist.x_labels=x_lable
hist.x_title='Result'
hist.y_title="Frequency of Result"
#将数据添加入直方图中
hist.add('D6',frequencies)
#将图表渲染为SVG文件，其扩展名必须为.svg
hist.render_to_file('two_D6_dies_result_multiply_visual.svg')