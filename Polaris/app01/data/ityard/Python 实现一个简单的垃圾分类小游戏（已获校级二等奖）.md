
--- 
title:  Python 实现一个简单的垃圾分类小游戏（已获校级二等奖） 
tags: []
categories: [] 

---
>  
  作者：Vincentish 
  https://blog.csdn.net/Vincentish/article/details/107495432 
 

## 项目简介

本项目报名参加了“兖州中材杯”武汉理工大学第十一届环保创意作品大赛艺术理念组比赛。组员共三名，本人负责代码实现部分，其余两人分别负责项目策划与场景人物绘制。

### 项目背景

小组中负责策划的同学经过一定的调研之后发现，我校在校学生普遍缺乏垃圾分类方面的知识。经过讨论后，我们把游戏方向定位于“垃圾分类”，游戏类型定位于像素风游戏，由于本人水平和时间有限，只能将玩法设计得尽量简单。**感谢另外两位组员，他们的努力掩盖了我水平上的不足。**

### 玩法介绍

家控制一名角色在操场背景上移动，垃圾桶在操场边上。捡起垃圾丢进相应的垃圾桶内，若全部正确投放则游戏成功，否则游戏失败。游戏期间，若有不清楚该作何分类的垃圾，则可以点击图书馆的按钮，进入图书馆查询。图书馆提供垃圾图鉴和分类标准两种信息。垃圾图鉴帮助玩家分辨自己捡到的垃圾，而分类标准指每种垃圾的定义及举例。

### 项目成果

本项目在“兖州中材杯”武汉理工大学第十一届环保创意作品大赛艺术理念组比赛中最终获得了第五名、二等奖的成绩，距第四名仅差0.5分。

## 项目实现

**写项目时本人仅自学了一个月的Python，且本人是大一新生，对计算机科学的基础知识了解甚少，若代码风格幼稚、愚蠢，还望读者见谅。**

### 模块划分

游戏按场景分为以下几个模块：**开始游戏界面**、**游戏说明界面**、**人物选择界面**、**操场界面**（主要游戏场地）、**图书馆外界面**、**图书馆内界面**、**游戏结束界面**。
1. 开始游戏界面：背景（像素化的学校建筑），游戏标题，三个按钮（开始、游戏说明、退出）。<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcU1SMmQwTkZZR01DTzFoa25LdmNBNnliaWFRYVJsaWN2RmVmT3VYT01saWFPdk5veU12aWNlaDZyb2R0Q0ZiOWw3bmVnMUJSQTlTWDVhWUEvNjQw?x-oss-process=image/format,png">1. 游戏说明界面：背景（与开始界面相同），游戏说明文字，返回按钮。<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcU1SMmQwTkZZR01DTzFoa25LdmNBNnFiREI4dHh3bEFuNDR0M2F4RE9uZFFON3N6OTNxZFBMTTFpYWliSXNURHZXa1h3OUJleDhkekR3LzY0MA?x-oss-process=image/format,png">1. 人物选择界面：背景，提示（选择人物），两个可选人物。<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcU1SMmQwTkZZR01DTzFoa25LdmNBNkFqNWY5Zll5QnVRZUd5OThGc2hhWnQ5WDk3UlhDbkpzUFlzaWNFRmRUZ3RhWkxNQmJKczlZa0EvNjQw?x-oss-process=image/format,png">1. 操场界面：背景，人物，垃圾桶，随机产生的垃圾，图书馆按钮。<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9QdlA2cWpVcHZJcU1SMmQwTkZZR01DTzFoa25LdmNBNjR4UGpDYk9aR3JtazMzclhSTjhDMWliNFY0OGFCa29vU1lxa2pnQ0R4RTZLTmxkcHp0aDVFOEEvNjQw?x-oss-process=image/format,png"><img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcU1SMmQwTkZZR01DTzFoa25LdmNBNmNpYzA3OEhNQWhSWHZlUzJVcUFIM2dJMTFNTE5EYUcyYjFrZTFpYlFRdllnTHU5YlZFd0tNMmJnLzY0MA?x-oss-process=image/format,png">1. 图书馆外界面：背景（我校图书馆的像素风绘制）、操场按钮（会到操场）、进入按钮（进入图书馆内部）。<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcU1SMmQwTkZZR01DTzFoa25LdmNBNjdUeHN4TWg5OWN1aWFCWkpZWU80cm5MQ2JjaHpCd1VHZTFCVk4zMWc4SjNuRlkyMG1UNWlidWVBLzY0MA?x-oss-process=image/format,png">1. 图书馆内界面：背景（我校图书馆内部），各类垃圾图标按钮（厨余垃圾、可回收垃圾、有害垃圾、其他垃圾），垃圾图鉴按钮，返回按钮。子界面：各类垃圾信息界面，垃圾图鉴界面，返回按钮。<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcU1SMmQwTkZZR01DTzFoa25LdmNBNjBsajJuSU91eHFRZUI1cWZodENCQmRIaE5HRWNINjZvcUFWakREbkRqakNCMzg4dHpISlhnUS82NDA?x-oss-process=image/format,png"><img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcU1SMmQwTkZZR01DTzFoa25LdmNBNnVrQ1lPSldld3V2cVlLamY0YXh1b2VNUGpsVm1nbDBjaWJKQnAyUG1jY25xM055SW83Q2ZYalEvNjQw?x-oss-process=image/format,png"><img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcU1SMmQwTkZZR01DTzFoa25LdmNBNktwTHBNUHBDTEVmZTllVEdJR3lEREJQOHNiSVh1TmMwTWFyY2JpY3hpY0lrOHBzaWNFc2xDOUhDZy82NDA?x-oss-process=image/format,png"><img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcU1SMmQwTkZZR01DTzFoa25LdmNBNnpJZGRpYmFrSG5HaWFjYmppYzdCRGVOYnpHaWFhMlR3VGNQNXRZNEQzSDhUcEl3em1tRDQ2aWIyRzF3LzY0MA?x-oss-process=image/format,png"><img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcU1SMmQwTkZZR01DTzFoa25LdmNBNnZMWG5JZDVxaWFEbGN1TUx3UHRlWkZzV2ZyTFMxejJuRlpwckw3RkxBNFVJUzdEaWJlWVFLbHRRLzY0MA?x-oss-process=image/format,png"><img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcU1SMmQwTkZZR01DTzFoa25LdmNBNklpYmhkYWhZUU5pY3E0blFLa2ZGQUxhdnZwMW1xRnN0dzAxQklwekE1bUIycVFpYjRIbGR0RlRUdy82NDA?x-oss-process=image/format,png">1. 游戏结束界面：胜利界面，失败界面。<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcU1SMmQwTkZZR01DTzFoa25LdmNBNlZ5cld5OVpvajI0YXZGR2p3NVhsNGoycDZ1R0RRWEdqVFl6MGFDbXQzbXF4WEFWVjZZUE9XZy82NDA?x-oss-process=image/format,png"><img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcU1SMmQwTkZZR01DTzFoa25LdmNBNnhqYjRvWWlheWlhY3pNVVJwOUNDQkpld2hpYmw3Wk0zd2ljb2ZKb3lobWtlRUdXODBUMGxOUzBPcUEvNjQw?x-oss-process=image/format,png">
### 代码实现

直接上代码：

```
import pygame as py
import sys
import random
from pygame.locals import *
#===========================================================
#========================前期准备===========================
py.init()
#注：游戏需要的所有文件（图片等）都放在同游戏目录的"Files"目录下。
#定义一个按钮类
class Button(py.rect.Rect):
    def __init__(self, obj):
        super().__init__(obj)
    def has(self, pos):
        if self.right &gt;= pos[0] &gt;= self.left and self.bottom &gt;= pos[1] &gt;= self.top:
            return True
        else:
            return False

screen = py.display.set_mode((1000, 650))
#===========================================================
#=========================图书馆内==========================

def knowledge(selection):
    path = 'Files\\inside_liberary\\knowledge' + str(selection) + '.jpg'
    know = py.image.load(path)
    know = py.transform.smoothscale(know,(1000,650))
    screen.blit(know,(0,0))
    exits = py.image.load('Files\\inside_liberary\\back.png')
    exits = py.transform.smoothscale(exits,(72,72))
    exit_button = screen.blit(exits,(918, 570))
    exit_button = Button(exit_button)
    py.display.flip()
    #进入事件循环
    while True:
        for event in py.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pos = py.mouse.get_pos()
                #点击离开该页面
                if exit_button.has(pos):
                    selection = 0
                    break
        if not selection:
            break

def inside_Liberary():
    ilib = py.image.load('Files\\inside_liberary\\Inside.jpg')
    ilib = py.transform.smoothscale(ilib,(1000,650))
    screen.blit(ilib,(0,0))
    #退出图书馆的按钮
    exits = py.image.load('Files\\inside_liberary\\exit.png')
    exits = py.transform.smoothscale(exits,(72,81))
    exit_button = screen.blit(exits,(5, 560))
    exit_button = Button(exit_button)
    #厨余垃圾按钮
    rubbish1 = py.image.load('Files\\inside_liberary\\rubbish1.png')
    rubbish1 = py.transform.smoothscale(rubbish1,(150,298))
    rubbish1_button = screen.blit(rubbish1, (80,150))
    rubbish1_button = Button(rubbish1_button)
    #可回收垃圾按钮
    rubbish2 = py.image.load('Files\\inside_liberary\\rubbish2.png')
    rubbish2 = py.transform.smoothscale(rubbish2,(150,298))
    rubbish2_button = screen.blit(rubbish2, (310,150))
    rubbish2_button = Button(rubbish2_button)
    #有害垃圾按钮
    rubbish3 = py.image.load('Files\\inside_liberary\\rubbish3.png')
    rubbish3 = py.transform.smoothscale(rubbish3,(150,298))
    rubbish3_button = screen.blit(rubbish3, (540,150))
    rubbish3_button = Button(rubbish3_button)
    #不可回收垃圾按钮
    rubbish4 = py.image.load('Files\\inside_liberary\\rubbish4.png')
    rubbish4 = py.transform.smoothscale(rubbish4,(150,298))
    rubbish4_button = screen.blit(rubbish4, (770,150))
    rubbish4_button = Button(rubbish4_button)
    #图鉴按钮
    rubbish5 = py.image.load('Files\\inside_liberary\\rubbish5.png')
    rubbish5 = py.transform.smoothscale(rubbish5,(82, 72))
    rubbish5_button = screen.blit(rubbish5, (903,560))
    rubbish5_button = Button(rubbish5_button)
    
    py.display.flip()
    selection = -1
    #进入事件循环
    while True:
        for event in py.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pos = py.mouse.get_pos()
                #点击离开图书馆
                if exit_button.has(pos):
                    selection = 0
                    break
                #点击厨余垃圾
                if rubbish1_button.has(pos):
                    selection = 1
                    break
                #点击可回收垃圾
                if rubbish2_button.has(pos):
                    selection = 2
                    break
                #点击有害垃圾
                if rubbish3_button.has(pos):
                    selection = 3
                    break
                #点击不可回收垃圾
                if rubbish4_button.has(pos):
                    selection = 4
                    break
                #点击图鉴
                if rubbish5_button.has(pos):
                    selection = 5
                    break
        if selection != -1:
            break
    if selection:
        knowledge(selection)
        inside_Liberary()
#===========================================================
#=========================图书馆外==========================

def outside_Liberary():
    olib = py.image.load('Files\\outside_liberary\\Outside.jpg')
    olib = py.transform.smoothscale(olib,(1000,650))
    screen.blit(olib,(0,0))
    #进入图书馆的按钮
    enter = py.image.load('Files\\outside_liberary\\enter_lib.png')
    enter = py.transform.smoothscale(enter,(72, 72))
    enter_button = screen.blit(enter,(470,550))
    enter_button = Button(enter_button)
    #退出图书馆的按钮
    exits = py.image.load('Files\\outside_liberary\\playground.png')
    exits = py.transform.smoothscale(exits,(72, 51))
    exit_button = screen.blit(exits,(5, 590))
    exit_button = Button(exit_button)
    py.display.flip()
    selection = -1
    #进入事件循环
    while True:
        for event in py.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pos = py.mouse.get_pos()
                #点击返回操场
                if exit_button.has(pos):
                    selection = 0
                    break
                #点击进入图书馆
                if enter_button.has(pos):
                    selection = 1
                    break
        if selection != -1:
            break
    if selection:
        inside_Liberary()
        outside_Liberary()

#===========================================================
#==========================游戏帮助=========================

def help_page():
    background = py.image.load('Files\\help\\background.jpg')
    background = py.transform.smoothscale(background,(1000,650))
    screen.blit(background,(0,0))
    #返回按钮
    exits = py.image.load('Files\\help\\back.png')
    exits = py.transform.smoothscale(exits,(72,57))
    exit_button = screen.blit(exits,(5, 585))
    exit_button = Button(exit_button)
    py.display.flip()
    back = 0
    while True:
        for event in py.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pos = py.mouse.get_pos()
                if exit_button.has(pos):
                    back = 1
                    break
        if back:
            break
                
#===========================================================
#==========================游戏结束=========================

def game_over(result):
    path = 'Files\\game_over\\result' + str(result) + '.png'
    background = py.image.load(path)
    background = py.transform.smoothscale(background,(1000,650))
    screen.blit(background,(0,0))
    py.display.flip()
    temp = 0
    while True:
        for event in py.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                temp = 1
                break
        if temp:
            break

#===========================================================
#==========================操场环节=========================

choices = ['01', '02', '11', '12', '21', '22', '31']
class Rubbish():
    def __init__(self, sort):
        self.sort = sort
        self.img = py.image.load('Files\\playground\\' + sort + '.png')
        x = random.randint(100, 1400)
        y = random.randint(110, 900)
        self.position = self.img.get_rect()
        self.position = self.position.move((x, y))
        screen.blit(self.img, self.position)
class Role():
    def __init__(self, role):
        self.r_side = py.image.load('Files\\playground\\' + role + '1.png')
        self.r_walk = py.image.load('Files\\playground\\' + role + '2.png')
        self.l_side = py.transform.flip(self.r_side, True, False)
        self.l_walk = py.transform.flip(self.r_walk, True, False)
        self.img = self. r_side
        self.position = self.img.get_rect()
        screen.blit(self.img, self.position)
        self.rubbish = None
    def move(self, key):
        if key == K_UP:
            if self.position.top &lt;= 200:
                return (0, 2)
            else:
                self.position = self.position.move(0, -2)
                return 0
        if key == K_DOWN:
            if self.position.bottom &gt;= 450:
                return (0, -2)
            else:
                self.position = self.position.move(0, 2)
                return 0
        if key == K_RIGHT:
            if self.position.right &gt;= 800:
                return (-2, 0)
            else:
                self.position = self.position.move(2, 0)
                return 0
        if key == K_LEFT:
            if self.position.left &lt;= 200:
                return (2, 0)
            else:
                self.position = self.position.move(-2, 0)
                return 0
        
class Trash_can():
    def __init__(self, num):
        self. num = num
        self.img = py.image.load('Files\\playground\\' + str(num) + '.png')
        self.img = py.transform.smoothscale(self.img,(100, 92))
        self.position = self.img.get_rect()
        self.position = self.position.move((100 + num*200, 0))
        screen.blit(self.img, self.position)
def playground(selection):
    background = py.image.load('Files\\playground\\Playground.jpg')
    screen.blit(background, [0, 0])
    lib = py.image.load('Files\\playground\\liberary.png')
    lib = py.transform.smoothscale(lib, (78, 72))
    lib_button = screen.blit(lib, (900, 10))
    lib_button = Button(lib_button)
    trash_can = []
    for num in range(0, 4):
        trash_can.append(Trash_can(num))
    role = Role(selection)
    rubbish = []
    for sort in choices:
        rubbish.append(Rubbish(sort))
    py.display.flip()
    down = 0
    go = None
    move_bg = [0, 0]
    temp = 0
    while True:
        for event in py.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pos = py.mouse.get_pos()
                if lib_button.has(pos):
                    outside_Liberary()
            if event.type == KEYDOWN and\
               event.key in (K_UP, K_DOWN, K_RIGHT, K_LEFT):
                if event.key == K_RIGHT:
                    role.img = role.r_side
                elif event.key == K_LEFT:
                    role.img = role.l_side
                down = 1
                go = event.key
            if event.type == KEYUP and event.key == go:
                if event.key == K_RIGHT:
                    role.img = role.r_side
                elif event.key == K_LEFT:
                    role.img = role.l_side
                down = 0
        take = role.position.collidelist([each.position for each in rubbish])
        if take &gt;= 0 and not role.rubbish:
            role.rubbish = rubbish[take].sort[0]
            del rubbish[take]
        put = role.position.collidelist([each.position for each in trash_can])
        if put &gt;= 0 and role.rubbish:
            if role.rubbish == str(trash_can[put].num):
                role.rubbish = None
                if not len(rubbish):
                    game_over(1)
                    break
            else:
                game_over(2)
                break
        if down:
            moved = role.move(go)
            temp += 1
            if not temp % 20:
                if role.img == role.r_side:
                    role.img = role.r_walk
                elif role.img == role.r_walk:
                    role.img = role.r_side
                elif role.img == role.l_side:
                    role.img = role.l_walk
                else:
                    role.img = role.l_side
            if moved:
                if 0 &gt;= moved[0] + move_bg[0] &gt;= -497 and \
                   0 &gt;= moved[1] + move_bg[1] &gt;= -326:
                    for i in range(2):
                        move_bg[i] += moved[i]
                    for each in rubbish:
                        each.position = each.position.move(moved)
                    for each in trash_can:
                        each.position = each.position.move(moved)
                elif role.position.left - moved[0] &gt;= 0 and\
                     role.position.right - moved[0] &lt;= 1000 and\
                     role.position.top - moved[1] &gt;= 0 and\
                     role.position.bottom - moved[1] &lt;= 650:
                    role. position = role.position.move([-i for i in moved])
        screen.blit(background, move_bg)
        lib = py.image.load('Files\\playground\\liberary.png')
        lib = py.transform.smoothscale(lib, (78, 72))
        lib_button = screen.blit(lib, (900, 10))
        lib_button = Button(lib_button)
        for each in trash_can:
            screen.blit(each.img, each.position)
        for each in rubbish:
            screen.blit(each.img, each.position)
        screen.blit(role.img, role.position)
        py.display.flip()


#===========================================================
#==========================选择人物=========================

def choose_role():
    background = py.image.load('Files\\choose_player\\background.jpg')
    background = py.transform.smoothscale(background,(1000,650))
    screen.blit(background, (0, 0))
    man = py.image.load('Files\\choose_player\\man.png')
    man = py.transform.smoothscale(man,(123, 325))
    man_button = screen.blit(man,(200, 200))
    man_button = Button(man_button)
    woman = py.image.load('Files\\choose_player\\woman.png')
    woman = py.transform.smoothscale(woman,(113, 325))
    woman_button = screen.blit(woman,(687, 200))
    woman_button = Button(woman_button)
    py.display.flip()
    while True:
        for event in py.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pos = py.mouse.get_pos()
                if man_button.has(pos):
                    return 'man'
                if woman_button.has(pos):
                    return 'woman'
                
#===========================================================
#========================开始游戏界面========================

def start():
    background = py.image.load('Files\\start\\background.jpg')
    background = py.transform.smoothscale(background,(1000,650))
    screen.blit(background, (0, 0))
    start_game = py.image.load('Files\\start\\start_game.png')
    start_game = py.transform.smoothscale(start_game,(140, 149))
    start_button = screen.blit(start_game,(150, 330))
    start_button = Button(start_button)
    game_help = py.image.load('Files\\start\\game_help.png')
    game_help = py.transform.smoothscale(game_help,(280, 182))
    help_button = screen.blit(game_help,(380, 320))
    help_button = Button(help_button)
    quit_game = py.image.load('Files\\start\\quit_game.png')
    quit_game = py.transform.smoothscale(quit_game,(200,160))
    quit_button = screen.blit(quit_game,(680, 330))
    quit_button = Button(quit_button)
    py.display.flip()
    while True:
        for event in py.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pos = py.mouse.get_pos()
                if start_button.has(pos):
                    role = choose_role()
                    playground(role)
                    break
                elif help_button.has(pos):
                    help_page()
                    break
                elif quit_button.has(pos):
                    sys.exit()
        break
    start()
start()


```

### 游戏效果

游戏演示如下：



<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9RQjZHNFpvRTE4NGliejlNc2N3YXE5OHcwNXVHQWljMXh0UXZqNWhzTEQ1eFdmcjlIYlhsTDVSTnFRcU1wcnVnNlhqRDdtSTRVY1F2Y3U2NEdHZTI3VDdBLzY0MA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb24walFiZjlpYVdGcTBMaWJaSVQ0WXJCNGlhd0ZmZE5lQjFJcks0eXhrWVplbnFvWWY2dHc3dElpY0EyMUxNWEFSVzN6bkk5ajU0NmliMzFRLzY0MA?x-oss-process=image/format,png">

分享或在看是对我最大的支持 
