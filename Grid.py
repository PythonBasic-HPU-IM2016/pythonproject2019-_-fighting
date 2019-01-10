
from tkinter import *            #导入tkinter库，为python的内置库，导入即可使用 
from random import randint       #导入random模块中的randint函数，用于生成随机整数
import tkinter.messagebox        #导入弹窗库，用于信息提示

class Grid(object):     
#使用class类的继承，实现代码的重用，Grid为通过继承创建的新类（子类或派生类），object为被继承的类（基类、父类或超类）
    def __init__(self, master=None, height=16, width=24, offset=10, grid_width=48, grid_height=50, bg="#808080"):
    #__init__()方法,被称为类的构造函数或初始化方法，当创建了类的实例时就会调用该方法
    #self 代表类的实例,即Grid对象本身。self 在定义类的方法时是必须有的，在调用时不必传入相应的参数。
        self.height = height              #一个变量，值为16，用于设置canvas纵坐标中网格的个数
        self.width = width                #一个变量，值为24，用于设置canvas横坐标中网格的个数
        self.offset = offset              #offset为允许发生的偏移量
        self.grid_width = grid_width      #单个网格的宽度为50
        self.grid_height = grid_height    #单个网格的高度为50
        self.bg = bg                      #设置背景色
        self.canvas = Canvas(master, width=self.width*self.grid_width+2*self.offset, height=self.height*self.grid_height+
                                                                                           2*self.offset, bg=self.bg)
        #设置canvas的宽度、高度、背景色。
        self.canvas.pack(side=RIGHT, fill=Y)    
        #用pack()函数对画布进行布局，side=RIGHT设置得分框位于canvas的右侧，fill=Y填充Y方向的空间
    def draw(self, pos, color):
        x = pos[0] * self.grid_width + self.offset    #设置x坐标轴位置
        y = pos[1] * self.grid_height + self.offset   #设置y坐标轴位置   
        self.canvas.create_rectangle(x, y, x + self.grid_width, y + self.grid_width, fill=color, outline=self.bg)
        #绘制一个矩形，坐标为（X,Y, , ,），outline属性设置网格的背景色（self.bg）相同
