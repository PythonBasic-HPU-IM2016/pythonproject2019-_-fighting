class Snake(object):        #定义一个蛇类
    #蛇向一个指定点移动
    def __init__(self, grid, color = "#000000"): #采用__init__()构造方法对蛇进行初始化
        self.grid = grid      #蛇的形状为网格
        self.color = color    #蛇的初始化颜色
        self.body = [(8, 11), (8, 12), (8, 13)]   #蛇的初始化长度
        self.direction = "Up"        #定义蛇的初始行进方向向上
        for i in self.body:       ##用for循环遍历蛇
            self.grid.draw(i, self.color)

    #这个方法用于游戏重新开始时初始化贪吃蛇的位置
    def initial(self):
        while not len(self.body) == 0:
            pop = self.body.pop()
            self.grid.draw(pop, self.grid.bg)
        self.body = [(8, 11), (8, 12), (8, 13)]
        self.direction = "Up"
        self.color = "#000000"
        for i in self.body:
            self.grid.draw(i, self.color)
            
    def move(self, new):    #定义move()方法使蛇发生移动
        self.body.insert(0, new)
        pop = self.body.pop()
        self.grid.draw(pop, self.grid.bg)
        self.grid.draw(new, self.color)

    #蛇向一个指定点移动，并增加长度
    def add(self ,new):    #定义一个add()方法,用于增加蛇的长度
        self.body.insert(0, new)    #更新后蛇的长度
        self.grid.draw(new, self.color)  #显示更新后的蛇

    #蛇吃到了特殊食物1，剪短自身的长度
    def cut_down(self,new):   #定义一个cut_down()方法，用于减短蛇的长度
        self.body.insert(0, new)   #更新后蛇的长度
        self.grid.draw(new, self.color)  #显示更新后的蛇
        for i in range(0,3):     #遍历for循环，将蛇的长度减少3个格
            pop = self.body.pop()
            self.grid.draw(pop, self.grid.bg)

    #蛇吃到了特殊食物2，回到最初长度
    def init(self, new):
        self.body.insert(0, new)
        self.grid.draw(new, self.color)
        while len(self.body) > 3:   #判断蛇的长度，如果大于3个格，则用while循环返回蛇的初始长度
            pop = self.body.pop()
            self.grid.draw(pop, self.grid.bg)

     #蛇吃到了特殊食物3，改变了自身的颜色
    def change_color(self, new, color):     #定义change_color()方法，改变蛇的颜色
        self.color = color   #蛇改变为特殊食物的颜色
        self.body.insert(0, new)   #显示更新后的蛇
        for item in self.body:   #遍历蛇的身体，全部改变为改变之后的颜色
            self.grid.draw(item, self.color)


