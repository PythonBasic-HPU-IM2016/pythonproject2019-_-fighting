#该模块调用到的其它函数由其他同学进行编写
class SnakeGame(Frame):
    def move(self, color="#EE82EE"):
    # 计算蛇下一次移动的点
    head = self.snake.body[0]
    if self.snake.direction == 'Up':
        if head[1] - 1 < 0:
            new = (head[0], 16)
        else:
            new = (head[0], head[1] - 1)
    elif self.snake.direction == 'Down':
        new = (head[0], (head[1] + 1) % 16)
    elif self.snake.direction == 'Left':
        if head[0] - 1 < 0:
            new = (24, head[1])
        else:
            new = (head[0] - 1, head[1])
    else:
        new = ((head[0] + 1) % 24, head[1])
        #撞到自己，设置游戏结束的标志位，等待下一循环
    if new in self.snake.body:
        self.gameover=True
    #吃到食物
    elif new == self.food.pos:
        if self.food.type == 1:
            self.snake.add(new)#如果吃到的食物类型是1，则调用add函数，蛇向一个指定点移动，并增加自身函数
        elif self.food.type == 2:
            self.snake.cut_down(new)#如果吃到的食物类型是2，则调用cut_down函数，剪短自身长度
        elif self.food.type == 4:
            self.snake.change(new, color)#如果吃到的食物类型是4，则调用change函数，改变自身颜色
        else:
            self.snake.init(new)#蛇吃到了黄色食物则回到原始长度。
        self.display_food()#蛇吃到了食物，则调用display_food函数，随机生成食物
        self.score = self.score+1#只要蛇吃到了食物，不管什么食物，则分数自动加一
        self.m.set("Score:" + str(self.score))#更新分数显示区域的分数显示。
        #什么都没撞到，继续前进
    else:
        self.snake.move(new)
