class Food(object):     #定义一个食物类，用于设置食物的各种参数
    def __init__(self, grid,color="#23D978"):    #采用__init__()构造方法定义一个食物
        self.grid = grid       #引用grid类为食物网格
        self.color = color     #食物的颜色
        self.set_pos()         #食物的位置
        self.type = 1          #第一次游戏开始时食物的类型

    def set_pos(self):        #定义食物出现位置的set_pos()方法
        x = randint(0, self.grid.width - 1)    #调用randint随机出现食物横坐标的位置
        y = randint(0, self.grid.height - 1)   #调用randint随机出现食物纵坐标的位置
        self.pos = (x, y)        #返回食物出现的位置坐标

    def display(self):       #定义display方法显示食物和蛇
        self.grid.draw(self.pos, self.color)
