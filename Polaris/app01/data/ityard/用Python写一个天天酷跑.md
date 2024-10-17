
--- 
title:  用Python写一个天天酷跑 
tags: []
categories: [] 

---
写出来的效果图就是这样了:

下面就更新一下全部的代码吧

还是老样子先定义

```
import pygame,sys
import random
```

写一下游戏配置

```
width = 1200            #窗口宽度
height = 508            #窗口高度
size = width, height   
score=None              #分数
myFont=myFont1=None     #字体
surObject=None          #障碍物图片         
surGameOver=None        #游戏结束图片
bg=None                 #背景对象
role=None               #人物对象
object=None             #障碍物对象        
objectList=[]           #障碍物对象数组
clock=None              #时钟
gameState=None          #游戏状态（0，1）表示（游戏中，游戏结束）
```

写人物

```
class Role: #人物
    def __init__(self,surface=None,y=None):
        self.surface=surface
        self.y=y
        self.w=(surface.get_width())/12
        self.h=surface.get_height()/2
        self.currentFrame=-1
        self.state=0        #0代表跑步状态，1代表跳跃状态,2代表连续跳跃
        self.g=1            #重力加速度
        self.vy=0           #y轴速度       
        self.vy_start=-20   #起跳开始速度
    def getRect(self):
        return (0,self.y+12,self.w,self.h)
```

写障碍物

```
class Object:  #障碍物
    def __init__(self,surface,x=0,y=0):
        self.surface=surface
        self.x=x
        self.y=y
        self.w=surface.get_width()
        self.h=surface.get_height()
        self.currentFrame=random.randint(0,6)
        self.w = 100
        self.h = 100
    def getRect(self):
        return (self.x,self.y,self.w,self.h)
    def collision(self,rect1,rect2):
        #碰撞检测
        if (rect2[0]&gt;=rect1[2]-20) or (rect1[0]+40&gt;=rect2[2])or (rect1[1]+rect1[3]&lt;rect2[1]+20) or (rect2[1]+rect2[3]&lt;rect1[1]+20):
            return False
        return True
```

写背景

```
class Bg:   #背景
    def __init__(self,surface):
        self.surface=surface
        self.dx=-10
        self.w=surface.get_width()
        self.rect=surface.get_rect()
```

```
def initGame():
        
    global bg,role,clock,gameState,surObject,surGameOver,score,myFont,myFont1,objectList
    #分数初始化
    score=0
    #初始化
    objectList=[]
    #加载字体
    myFont=pygame.font.Font("./freesansbold.ttf",32)
    myFont1=pygame.font.Font("./freesansbold.ttf",64)   
    # 创建时钟对象 (可以控制游戏循环频率)
    clock = pygame.time.Clock()
    #初始化游戏状态
    gameState=0
    #游戏背景
    surBg=pygame.image.load("image/bg.bmp").convert_alpha()
    bg=Bg(surBg)
    #结束画面
    surGameOver=pygame.image.load("image/gameover.bmp").convert_alpha()
    #人物图片
    surRole=pygame.image.load("image/role.png").convert_alpha()  
    role=Role(surRole,508-85)
    #障碍物图片
    surObject=pygame.image.load("image/object.png").convert_alpha()  


def addObject():
    global surObject,object,objectList,object
    rate=4
    #是否生成障碍物
    if not random.randint(0,300)&lt;rate:
        return
    y=random.choice([height-100,height-200,height-300,height-400])
    object=Object(surObject,width+40,y)
    objectList.append(object)


def updateLogic():
    global gameState,score
    #键盘事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             sys.exit()
        elif event.type==pygame.KEYDOWN:
            #空格键跳跃
            if gameState==0:
                if event.key==pygame.K_SPACE:
                    if role.state==0:
                        role.state=1
                        role.vy=role.vy_start
                    elif role.state==1:
                        role.state=2
                        role.vy=role.vy_start
            elif gameState==1:
                if event.key==pygame.K_SPACE:
                    #重新开始游戏
                    initGame()
                    
    if gameState==0:
        #背景的移动   
        bg.dx+=10
        if bg.dx==1200:
            bg.dx=0 
            
        #人物的移动  
        if role.state==0:    
            role.currentFrame+=1
            if role.currentFrame==12:
                role.currentFrame=0  
        else:
            role.y+=role.vy
            role.vy+=role.g 
            if role.y&gt;=508-85:
                role.y=508-85
                role.state=0
        #障碍物的移动
        addObject()
        
        for object in objectList:
            object.x-=10     #障碍物移动
            # 障碍物超出屏幕，移除障碍物
            if object.x+object.w&lt;=0:
                objectList.remove(object)
                score+=10    #避开障碍物，加10分
                print("移除了一个目标")   
            #碰撞检测
            if object.collision(role.getRect(),object.getRect()):
                if(object.currentFrame==6):
                    objectList.remove(object)
                    score+=100  #吃金币加100分
                    print(score)
                    print("吃了一个金币")
                else: 
                    gameState=1   #游戏失败
                    print("发生了碰撞！")
```

ok啦，这就是这个天天酷跑的全部代码啦，有问题可以留言，我看到都会回的。

如果本文对你有帮助的话，欢迎点赞&amp;在看&amp;分享，这对我继续分享&amp;创作优质文章非常重要。感谢🙏🏻
