class Food(object):     #Food类
    def __init__(self, grid, color = "#23D978"):
        #初始化函数，包含网格grid和颜色color参数 
        self.grid = grid     #把参数grid赋值给对象变量grid  
        self.color = color   #把参数color赋值给对象变量color 
        self.set_pos()       #食物Food的位置
        self.type = 1        #食物Food类型1

    def set_pos(self):       #定义食物出现位置的set_pos()方法
        x = randint(0, self.grid.width - 1)   #调用randint随机出现食物横坐标的位置
        y = randint(0, self.grid.height - 1)  #调用randint随机出现食物纵坐标的位置
        self.pos = (x, y)
        #返回食物出现的位置坐标
    def display(self):       #定义display方法显示食物和蛇
        self.grid.draw(self.pos, self.color)