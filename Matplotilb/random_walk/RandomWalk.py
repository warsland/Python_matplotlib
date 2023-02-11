from random import choice

class RandomWalk():
    """生成一个随机漫步数据的类"""
    def __init__(self,num_points=5000) -> None:
        self.num_points=num_points

        """漫步初始位置"""
        self.x_values=[0]
        self.y_values=[0]
    
    def get_step(self):
        """计算前进步骤"""
         #决定前进方向，-1表示左，1表示右
        direction=choice([-1,1])
        #决定前进距离
        distance=choice(list(range(0,6)))
        #计算前进步数
        step=distance*direction
        return step
    
    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        #不断漫步直至列表达到指定长度
        while len(self.x_values)<self.num_points:
            #决定前进方向，-1表示左，1表示右
            #x_direction=choice([-1,1])
            #决定前进距离
            #x_distance=choice(list(range(0,6)))
            #x_step=x_distance*x_direction
            #决定前进方向，-1表示下，1表示上
            #y_direction=choice([-1,1])
            #决定前进距离
            #y_distance=choice(list(range(0,6)))
            #y_step=y_direction*y_distance

            x_step=self.get_step()
            y_step=self.get_step()

            #防止随机漫步中出现原地踏步现象
            if x_step==0 and y_step==0:
                continue
            
            #计算下一个点的位置
            next_x=self.x_values[-1]+x_step
            next_y=self.y_values[-1]+y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

            



            