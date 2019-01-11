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

class SnakeGame(Frame):    #定义一个SnakeGame类，Frame框架，用于游戏规则的设定和进行游戏控制
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
        self.display_food()    #调用初始化食物的显示颜色
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

    #type1:普通食物  type2:减少3  type3:回到最初状态  type4:吃了会变色
    def display_food(self):   #定义display_food()，用于显示食物的颜色、位置和类型
        self.food.color = "#23D978"   #初始化食物的颜色为绿色
        self.food.type = 1   #初始化食物的类型为第一个类型
        if randint(0, 20) == 5:     #判断出现的（0,20）范围内出现随机数是否为5，对随机数为5的数字设置其食物颜色和类型
            self.food.color = "#FFD700"     
            self.food.type = 3
            while (self.food.pos in self.snake.body):    #判断蛇是否吃到食物，若吃到食物，该类食物随机出现
                self.food.set_pos()
            self.food.display()
        elif randint(0, 4) == 2:    #判断出现的（0,4）范围内出现随机数是否为2，对随机数为2的数字设置其食物颜色和类型
            self.food.color = "#EE82EE"
            self.food.type = 4
            while (self.food.pos in self.snake.body):   #判断蛇是否吃到食物，若吃到食物，该类食物随机出现
                self.food.set_pos()
            self.food.display()
        elif len(self.snake.body) > 10 and randint(0, 16) == 1:    #当蛇的长度>10个格子，且随机数为（0,16）设置其食物颜色和类型
            self.food.color = "#FF0000"
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
                self.i = (self.i+1)%10   #调用color_c(包含颜色)进行食物颜色闪烁
                self.food.color = color
                self.food.display()
                self.move(color)
            else:    #如果游戏不结束、食物类型不为4，调用move()方法
                self.move()
        self.after(self.speed, self.run)   #调用after()方法改变蛇行进速度和游戏进程

    def move(self, color="#EE82EE"):   #定义move()方法，用与判断蛇的移动方向
        # 计算蛇下一次移动的点
        head = self.snake.body[0]   
        if self.snake.direction == 'Up':  #如果蛇向上移动，执行以下操作
            if head[1] - 1 < 0:
                new = (head[0], 16)
            else:
                new = (head[0], head[1] - 1)
        elif self.snake.direction == 'Down':   #如果蛇向上移动，执行以下操作
            new = (head[0], (head[1] + 1) % 16)
        elif self.snake.direction == 'Left':  #如果蛇向左移动，执行下面的操作
            if head[0] - 1 < 0:
                new = (24, head[1])
            else:
                new = (head[0] - 1, head[1])
        else:     #如果蛇不符合上述3个移动方向，执行下面的一行代码
            new = ((head[0] + 1) % 24, head[1])
            #撞到自己，设置游戏结束的标志位，等待下一循环
        if new in self.snake.body:
            self.gameover=True
        #如果吃到食物
        elif new == self.food.pos:
            if self.food.type == 1:   #如果吃到的食物类型是1，则调用add函数，蛇向一个指定点移动，并增加自身函数
                self.snake.add(new)
            elif self.food.type == 2:   #如果吃到的食物类型是2，则调用cut_down函数，剪短自身长度
                self.snake.cut_down(new)
            elif self.food.type == 4:   #如果吃到的食物类型是4，则调用change函数，改变自身颜色
                self.snake.change_color(new, color)
            else:     #如果没有吃到上述类型的食物，执行下面的方法
                self.snake.init(new)    #蛇吃到了黄色食物则回到原始长度。
            self.display_food()       #蛇吃到了食物，则调用display_food函数，随机生成食物
            self.score = self.score+1   #只要蛇吃到了食物，不管什么食物，则分数自动加一
            self.m.set("Score:" + str(self.score))   #更新分数显示区域的分数显示。
        #什么都没撞到，继续前进
        else:  
            self.snake.move(new)    

if __name__ == '__main__':  #__name__就是标识模块的名字的一个系统变量,通过if判断这样就可以执行“__mian__
    root = Tk()         #创建一个窗口
    root.title("贪吃蛇小游戏")
    snakegame = SnakeGame(root)
    snakegame.run()    #游戏开始
    snakegame.mainloop()  #进入消息循环

