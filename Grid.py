
from tkinter import *            #导入tkinter库，为python的内置库，导入即可使用 
from random import randint       #导入random模块中的randint函数，用于生成随机整数
import tkinter.messagebox        #导入弹窗库，用于信息提示

class Grid(object):     
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
