from tkinter import *       #导入tkinter库，是python的内置库，导入即可使用
from random import randint  #导入random模块中的randint函数，用于生成随机整数
import tkinter.messagebox   #导入弹窗库，用于信息提示

class Grid(object):   #定义一个网格（Gird）类，用于设置游戏总界面，蛇轨迹绘画等
    #初始化函数，__init__()方法,被称为类的构造函数或初始化方法，当创建了类的实例时就会调用该方法
    def __init__(self, master=None,height=16, width=24, offset=10, grid_width=30, grid_height=30,bg="#B0E2FF"):   #采用__init__()构造方法初始化Gird类的宽和高、背景颜色(浅蓝)
        self.height = height    #把参数height赋值给对象变量height，值为16，用于设置canvas纵坐标中网格的个数
        self.width = width      #把参数width 赋值给对象变量width ，值为24，用于设置canvas横坐标中网格的个数
        self.offset = offset    #把参数offset 赋值给对象变量offset，为允许发生的偏移量
        self.grid_width = grid_width   #把参数grid_width赋值给对象变量grid_width，单个网格的宽度为50
        self.grid_height=grid_height   #把参数grid_height赋值给对象变量grid_height，单个网格的高度为50
        self.bg = bg                   #把参数bg赋值给对象变量bg，设置背景色
        self.canvas = Canvas(master, width=self.width*self.grid_width+2*self.offset, height=self.height*self.grid_height+   #设置画布(蛇活动范围)的大小和背景颜色
                                                                                          2*self.offset, bg=self.bg)
        self.canvas.pack(side=RIGHT,fill=Y)     #用pack()函数对画布进行布局，side=RIGHT设置得分栏位于canvas的右侧，fill=Y填充Y方向的空间
 
    def draw(self, pos, color):    #定义一个draw函数，作用是绘制小蛇的行进路径、形状实物的形状
        #pos位置坐标参数
        x = pos[0] * self.grid_width + self.offset
        y = pos[1] * self.grid_width + self.offset
        #outline属性要与网格的背景色（self.bg）相同，更加美观
        self.canvas.create_oval(x, y, x + self.grid_width, y + self.grid_width, fill=color, outline=self.bg)
        #绘制一个圆形((a,b,c,d),值为左上角和右下角的坐标)，路径及小蛇、实物的形状，轮廓outline属性设置为网格的背景色
        
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

class Snake(object):      #定义一个蛇类，用于定义蛇的各种参数
    def __init__(self, grid, color = "#000000"):    #采用__init__()构造方法对蛇进行初始化
        self.grid = grid     #引用grid类为蛇的网格
        self.color = color   #蛇的初始化颜色
        self.body = [(8, 11), (8, 12), (8, 13)]  #蛇的初始化长度
        self.direction = "Up"   #定义蛇的初始行进方向向上
        for i in self.body:     #用for循环遍历蛇
            self.grid.draw(i, self.color)

    #定义initial()方法用于游戏重新开始时初始化贪吃蛇的位置
    def initial(self):
        while not len(self.body) == 0:   #进行while循环，知道蛇的长度为0，退出while循环
            pop = self.body.pop()
            self.grid.draw(pop, self.grid.bg)
        self.body = [(8, 11), (8, 12), (8, 13)]  #初始化蛇的大小
        self.direction = "Up"   #游戏重新开始初始化蛇的方向
        self.color = "blue"   #游戏重新开始初始化蛇的颜色
        for i in self.body:   #用for循环遍历蛇
            self.grid.draw(i, self.color)

    #蛇向一个指定点移动  
    def move(self, new):    #定义move()方法使蛇发生移动
        self.body.insert(0, new)    
        pop = self.body.pop()
        self.grid.draw(pop, self.grid.bg)
        self.grid.draw(new, self.color)

    #蛇向一个指定点移动，并增加长度
    def add(self ,new):    #定义一个add()方法,用于增加蛇的长度
        self.body.insert(0, new)    #更新后蛇的长度
        self.grid.draw(new, self.color)  #显示更新后的蛇

    #蛇吃到了特殊食物1，减短自身的长度
    def cut_down(self,new):   #定义一个cut_down()方法，用于减短蛇的长度
        self.body.insert(0, new)   #更新后蛇的长度
        self.grid.draw(new, self.color)  #显示更新后的蛇
        for i in range(0,3):     #遍历for循环，将蛇的长度减少3个格
            pop = self.body.pop()
            self.grid.draw(pop, self.grid.bg)

    #蛇吃到了特殊食物2，回到最初长度
    def init(self, new):    #定义init()方法用于返回蛇最初的长度
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
