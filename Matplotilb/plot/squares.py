import matplotlib.pyplot as plt

"""input_values=[1,2,3,4,5]
squares=[1,4,9,16,25]

#绘制线条的粗细
plt.plot(input_values,squares,linewidth=5)
#设置图表标题
plt.title("Square Nubmers",fontsize=24)
#X,Y轴标签
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
#设置刻度标记
plt.tick_params(axis='both',labelsize=14)
plt.show()"""

x_value=list(range(1,1001))
y_value=[x**2 for x in x_value]
#添加颜色
"""plt.scatter(x_value,y_value,c=(102/255,204/255,255/255),s=40)"""
#添加颜色映射,y值越大颜色越深
plt.scatter(x_value,y_value,c=y_value,cmap=plt.cm.Blues,s=40)
#设置图表标题
plt.title("Square Nubmers",fontsize=24) 
#X,Y轴标签
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
#设置刻度标记
plt.tick_params(axis='both',labelsize=10)
#自动保存
#plt.savefig('squares_polt.png',bbox_inches='tight')
plt.show()