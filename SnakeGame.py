#该模块调用到的其它函数由其他同学进行编写
class SnakeGame(Frame):
    def __init__(self, master):       #采用__init__()构造方法对SnakeGame进行初始化
        Frame.__init__(self, master)  #调用用__init__()构造方法对框架进行初始化
        self.grid = Grid(master)     
        self.snake = Snake(self.grid)
        self.food = Food(self.grid)
        self.gameover = False   #设置游戏结束的初始状态为False
        self.score = 0      #设置游戏的初始得分为0
        self.status = ['run', 'stop']    #设置蛇的状态有run和stop
        self.speed = 300   #设置蛇的初始速度为300
        self.grid.canvas.bind_all("<KeyRelease>", self.key_release)
        self.display_food()    #初始化食物的显示颜色
        #用于设置变色食物
        self.color_c = ("#FFB6C1","#6A5ACD","#0000FF","#F0FFF0","#FFFFE0","#F0F8FF","#EE82EE","#000000","#5FA8D9","#32CD32")
        self.i = 0   
        #界面左侧显示分数   
        self.m = StringVar()
        self.ft1 = ('Fixdsys', 40, "bold")
        self.m1 = Message(master, textvariable=self.m, aspect=5000, font=self.ft1, bg="#FFB5C5")
        self.m1.pack(side=LEFT, fill=Y)
        self.m.set("Score:"+str(self.score))
    #这个方法用于游戏重新开始时初始化游戏
    def initial(self):  #定义一个initial()方法，用于游戏重新开始进行游戏
        self.gameover = False   #初始化游戏结束时游戏重新开始初始的状态
        self.score = 0   #初始化游戏结束时游戏重新开始初始时游戏的得分
        self.m.set("Score:"+str(self.score))
        self.snake.initial()    #调用上面的initial()方法回到游戏重新开始时蛇的状态

    #type1:普通食物  type2:减少2  type3:回到最初状态  type4:吃了会变色
    def display_food(self):   #定义display_food()，用于显示食物的颜色、位置和类型
        self.food.color = "#23D978"   #初始化食物的颜色为绿色
        self.food.type = 1   #初始化食物的类型为第一个类型
        if randint(0, 20) == 5:     #判断出现的（0,20）范围内出现随机数是否为5，对随机数为5的数字设置其食物颜色和类型
            self.food.color = "#FFD700"     
            self.food.type = 3
            while (self.food.pos in self.snake.body):    #判断蛇是否吃到食物，若吃到食物，该类食物随机出现
                self.food.set_pos()
            self.food.display()
        elif randint(0, 10) == 2:    #判断出现的（0,10）范围内出现随机数是否为2，对随机数为2的数字设置其食物颜色和类型
            self.food.color = "#EE82EE"
            self.food.type = 4
            while (self.food.pos in self.snake.body):   #判断蛇是否吃到食物，若吃到食物，该类食物随机出现
                self.food.set_pos()
            self.food.display()
        elif len(self.snake.body) > 10 and randint(0, 16) == 8:    #当蛇的长度>10个格子，且随机数为（0,16）设置其食物颜色和类型
            self.food.color = "#BC8F8F"
            self.food.type = 2
            while (self.food.pos in self.snake.body):   #判断蛇是否吃到食物，若吃到食物，该类食物随机出现
                self.food.set_pos()
            self.food.display()
        else:      #若以上均不满足，当蛇吃到食物时，新食物随机出现
            while (self.food.pos in self.snake.body):  
                self.food.set_pos()
            self.food.display()

    def key_release(self, event):    #定义一个key_release()方法，用于监听键盘事件
        key = event.keysym     #获取一个键盘事件
        key_dict = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}   #定义一个字典，后续进行蛇是否向自己的反方向走进行判断
        #蛇不可以向自己的反方向走
        if key in key_dict and not key == key_dict[self.snake.direction]:   #判断蛇是否是向自己的反方向走，如果不是则蛇前进
            self.snake.direction = key
            self.move()
        elif key == 'p':
            self.status.reverse()
    def run(self):   #定义一个run()方法判断游戏进程
        #首先判断游戏是否暂停
        if not self.status[0] == 'stop':
            #判断游戏是否结束   
            if self.gameover == True:  #如果游戏结束，则显示界面Game Over,your score是多少分
                message = tkinter.messagebox.showinfo("Game Over", "your score: %d" % self.score)
                if message == 'ok':   #点击确定按钮，则调用initial函数游戏重新开始，初始化游戏。
                    self.initial()
            if self.food.type == 4:    #判断食物类型是否为4,是的话执行以下操作，令变色食物闪烁
                color = self.color_c[self.i]   
                self.i = (self.i+1)%10
                self.food.color = color
                self.food.display()
                self.move(color)
            else:    #如果游戏不结束、食物类型不为4，调用move()方法
                self.move()
        self.after(self.speed, self.run)   #调用after()方法改变蛇行进速度和游戏进程
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
