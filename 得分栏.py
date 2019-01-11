class SnakeGame(Frame):    #定义一个SnakeGame类，Frame框架，用于游戏规则的设定和进行游戏控制
    def __init__(self, master): 
    #界面左侧显示分数   
    self.m = StringVar()
    self.ft1 = ('Fixdsys', 40, "bold")
    self.m1 = Message(master, textvariable=self.m, aspect=5000, font=self.ft1, bg="#FFB5C5")
    self.m1.pack(side=LEFT, fill=Y)
    self.m.set("Score:"+str(self.score))
