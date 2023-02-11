import matplotlib.pyplot as plt
from RandomWalk import RandomWalk

while True:
    rw=RandomWalk()
    rw.fill_walk()

    #调整绘图尺寸
    #figsize以英寸为单位,dpi：图像分辨率
    plt.figure(dpi=128,figsize=(5,3))

    #隐藏坐标轴
    axes=plt.axes()
    axes.get_xaxis().set_visible(False) 
    axes.get_yaxis().set_visible(False)

    #漫步点着色
    #point_numbers=list(range(rw.num_points))
    #plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,s=1)
    plt.plot(rw.x_values,rw.y_values,c=(102/255,204/255,255/255),linewidth=1)
    #突出起点
    #plt.scatter(0,0,c='green',s=10)
    plt.plot(0,0,'o',c='green',linewidth=10)
    #突出终点
    plt.plot(rw.x_values[-1],rw.y_values[-1],'o',c='red',linewidth=10)
    #plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',s=10)
    plt.show()
    #plt.savefig("one direction.png",bbox_inches='tight')
    KEEP_RUNNING=input("Make another walk? (y/n): ")
    if KEEP_RUNNING=='n':
        break
