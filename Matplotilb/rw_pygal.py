import pygal
from  random_walk.RandomWalk import RandomWalk

rw=RandomWalk()
rw.fill_walk()

results=[]
for num in range(0,rw.num_points):
    result=(rw.x_values[num],rw.y_values[num])
    results.append(result)

scatter=pygal.XY(stroke=False)
scatter.title='Random Work'
scatter.x_title='X'
scatter.y_title='Y'
scatter.add("random point",results)

scatter.render_to_file('Random_Walk.svg')