
--- 
title:  用Python写了一个空洞机甲小游戏 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/img_convert/7acca40e9f317a5c4beb64f23f643bbf.png">

来源：http://nxw.so/4WSng

**先来看看效果图：**

<img src="https://img-blog.csdnimg.cn/img_convert/d9fef74eb37cb840769cd778d9251e9e.png">

<img src="https://img-blog.csdnimg.cn/img_convert/3ec69d145e12adcd4f0698dec89d0f53.png"><img src="https://img-blog.csdnimg.cn/img_convert/39e824dd3f51c504e787344ed8eed329.png">

<img src="https://img-blog.csdnimg.cn/img_convert/49dbb72b84db2e4a433b7c97b68d13e1.png">

**由于项目代码过多，这里只给出部分代码。**

**图片素材和源码的下载链接在文章结尾，大家自行下载即可。**

```
import pygame,sys
import time


import random
pygame.init()
pygame.mixer.init()
FRAM_PER_SECONDS=7
clock =pygame.time.Clock()
WIDTH=1290
HEIGHT=715
load_img_x=1290/2-376/2
load_img_y=715/2-224/2
load_animate=False
check=1 #关卡--标志
pause=False
#加载动画及音效
font = pygame.font.SysFont(None,50,True)# 字体  True 打开抗锯齿
load_music=pygame.mixer.Sound("music/11046.wav")
start_music=pygame.mixer.Sound("music/战斗背景音效.wav")
back_music=pygame.mixer.Sound("music/BGM_1 (1)_02.wav")
green_jn=pygame.mixer.Sound("music/敌人技能.wav")
green_attack_music=pygame.mixer.Sound("music/怪叫.wav")
player_hit_music=pygame.mixer.Sound("music/机甲受伤.wav")
walk_music=pygame.mixer.Sound("music/机器走路.wav")
jump_music=pygame.mixer.Sound("music/弹跳.wav")
diren_die_music=pygame.mixer.Sound("music/坦克爆炸.wav")
jn_music=pygame.mixer.Sound("music/激光声游戏喷射_1_3.wav")
attack_music=pygame.mixer.Sound("music/敌人普攻_01_1.wav")
check_music=pygame.mixer.Sound("music/升级或者获得奖励.wav")
feiti_music=pygame.mixer.Sound("music/机器故障.wav")
game_over_music=pygame.mixer.Sound("music/我一定会回来的.wav")
life_add_music=pygame.mixer.Sound("music/加血.wav")


player_hit_music.set_volume(0.5)
check_music.set_volume(0.2)
green_attack_music.set_volume(0.1)
back_music.set_volume(0)
jn_music.set_volume(1)
start_music.set_volume(0.5)
load_music.set_volume(1)




#出始地图
map_img=pygame.image.load("map_img/left.jpg")
start_back=pygame.image.load("load_img/start_back2.png")
set_font = pygame.font.SysFont("KaiTi", 47)


# load_music.play()


screen=pygame.display.set_mode((WIDTH,HEIGHT),pygame.FULLSCREEN)
# screen=pygame.display.set_mode((WIDTH,HEIGHT))
# screen.fill((16,16,16))
screen.blit(start_back,(0,0))


pygame.display.set_caption("空 洞 机 甲   -   -   -   -   -  （ 河软空洞传奇工作室  版权所有  Copyright @  2020 ）                                                  感                        谢                        支                        持")
pygame.display.set_icon(start_back)
#
load_image=() #开始动画列表
load_count=1 #开始动画加载
start_flag=False#是否开始
start_music.play(-1)#游戏开始音效
for pic_num in range(1,30):
    if pic_num&lt;10:
        load_image+=(pygame.image.load("./load_img/jz00"+str(pic_num)+".png"),)
    elif pic_num&gt;9:
        load_image+=(pygame.image.load("./load_img/jz0"+str(pic_num)+".png"),)


class walk_sound():
    def __init__(self,src):
        self.sound=pygame.mixer.Sound(src)
        self.sound.set_volume(1)
    def music_play(self):
        self.sound.play()
    def music_stop(self):
        self.sound.stop()


#关卡动画
class check_fun(object):
    check_list = []
    for pic_num in range(1, 13):
        check_list+=(pygame.image.load("./right_check/箭头" + str(pic_num) + ".png"),)
    def __init__(self):
        self.check_count=1
    def draw(self,screen):
        if self.check_count&gt;=12:
            self.check_count=1
        if self.check_count:
            screen.blit(self.check_list[self.check_count],(1100,290))
            self.check_count+=1


#机甲玩家角色
class Player(object):
    flc_list=()                            #机甲o技能列表
    lizi_list = ()                         #粒子特效1 列表
    lizi2_list = ()                        #粒子特效2 列表
    lizi3_list =()                         #粒子特效3 列表
    walk_right = ()                        #机甲 向左走列表
    walk_left = ()                         #机甲 向左走列表
    jn_list = ()                           #机甲i技能列表
    jump_list = ()                         #机甲跳跃技能列表
    hit_list = ()                          #机甲受伤列表
    attack_list_one=()                     #近攻 第一段 列表
    attack_list_two = ()                   #近攻 第二段列表
    attack_list_three = ()                 #近攻 第三段列表
    life_list=()                           #机甲受伤 列表
    die_list=()                             #机甲 血量 列表
    all_tuple=()
    stand_list = ()
    HP_tuple=()
    cd_tuple=()
    level_tuple=()
    for pic_num in range(1,13):
        level_tuple+=(pygame.image.load("./Update/"+str(pic_num)+".png"),)
    for pic_num in range(1,17):
        all_tuple+=(pygame.image.load("./jn/BIG/1 ("+str(pic_num)+").png"),)
    for pic_num in range(1,12):
        cd_tuple+=(pygame.image.load("./cd/cd"+str(pic_num)+".png"),)
    for pic_num in range(1,17):
        HP_tuple+=(pygame.image.load("./HP/"+str(pic_num)+".png"),)
    for pic_num in range(1,65):
        die_list+=(pygame.image.load("./die/die ("+str(pic_num)+").png"),)
    for pic_num in range(1,33):
        flc_list+=(pygame.image.load("./jn/flc ("+str(pic_num)+").png"),)
    for pic_num in range(1,49):
        lizi_list+=(pygame.image.load("./fire/"+str(pic_num)+".png"),)
    for pic_num in range(1,34):
        lizi2_list+=(pygame.image.load("./huohua/"+str(pic_num)+".png"),)
    for pic_num in range(1,81):
        lizi3_list+=(pygame.image.load("./huohua2/"+str(pic_num)+".png"),)
    for pic_num in range(1,5):
        life_list+=(pygame.image.load("./hit/ss (1).png"),)
        life_list+=(pygame.image.load("./hit/ss (2).png"),)
    for pic_num in range(1,13):
        walk_right+=(pygame.image.load("./walk/walk ("+str(pic_num)+").png"),)
    for pic_num in range(12,0,-1):
        walk_left+=(pygame.image.load("./walk/walk ("+str(pic_num)+").png"),)
    for pic_num in range(1, 25):
        stand_list+=(pygame.image.load("./stand/stand (" + str(pic_num) + ").png"),)
    for pic_num in range(1,41):
        jn_list+=(pygame.image.load("./jn/jn ("+str(pic_num)+").png"),)
    for pic_num in range(1,39):
        jump_list+=(pygame.image.load("./jump/jump ("+str(pic_num)+").png"),)
    for pic_num in range(1,48):
        hit_list+=(pygame.image.load("./hit/jd ("+str(pic_num)+").png"),)
    for pic_num in range(1,14):
        attack_list_one+=(pygame.image.load("./attack/1attack ("+str(pic_num)+").png"),)
    for pic_num in range(1,7):
        attack_list_two+=(pygame.image.load("./attack/2attack ("+str(pic_num)+").png"),)
    for pic_num in range(1,12):
        attack_list_three+=(pygame.image.load("./attack/3attack ("+str(pic_num)+").png"),)
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.speed=1
        self.left=False
        self.right=True
        self.stand=True
        self.jump=False
        self.i=False
        self.hit=False
        self.attack=0
        self.stand_count=1#站立的图片索引
        self.walk_count=1#步行的图片索引
        self.jump_count=1#跳跃的图片索引
        self.jn_count=1#技能i的图片索引
        self.hit_count=1#受伤的图片索引
        self.attack_Bool=False
        self.attack_one_count = 1#一段普攻的图片索引
        self.attack_two_count = 1  # 二段普攻的图片索引
        self.attack_three_count = 1  # 三段普攻的图片索引
        self.life=100
        self.t=10
        self.hit_box = (self.x, self.y, self.width, self.height)  # 碰撞框的位置 大小变量
        self.kill_enemy=0
        self.life_remove_bool=False
        self.life_count=0
        self.lizi_count=1
        self.lizi2_count = 1
        self.flc_count=0
        self.lizi3_count=1
        self.HP_count=0
        self.cd_count=0
        self.all_count=0
        self.cd=False
        self.levelAdd=False
        self.level=1
        self.flc=False
        self.die=False
        self.all=False
        self.die_count=0
        self.level_count=0
        self.HP_img=pygame.image.load("./HP/电池.png")
        self.skill_img = pygame.image.load("./HP/skill_num.png")
        self.player_img = pygame.image.load("./HP/head.png")
        self.win_bool=False
        self.lifeAdd=False
        self.all_lenth=50
    def draw(self,screen):
        if self.all_count&gt;=16:
            self.all_count=0
            self.all=False
            self.all_lenth=50


        if player.all_count&gt;14:
            U_Testing(enemylist)
            U_Testing(enemylist2)
            U_Testing(enemylist3)
            U_Testing(enemylist4)


        if self.cd_count&gt;=11:
            self.cd_count=0
            self.cd=False
        if self.HP_count == 2:
            life_add_music.play()
        if self.HP_count&gt;=16:
            life_add_music.stop()
            self.HP_count=0
            self.lifeAdd = False


        if self.level_count==2:
            life_add_music.play()
        if self.level_count&gt;=12:
            life_add_music.stop()
        if self.level_count&gt;=12:
            self.level_count=0
            self.levelAdd = False


        if self.lizi_count&gt;=48:
            self.lizi_count=1
        if self.lizi2_count&gt;=33:
            self.lizi2_count=1
        if self.lizi3_count&gt;=80:
            self.lizi3_count=1
        if self.lizi2_count:


            screen.blit(self.lizi2_list[self.lizi2_count], (-100, 500))
            screen.blit(self.lizi2_list[self.lizi2_count], (200, 500))
            screen.blit(self.lizi2_list[self.lizi2_count], (500, 500))
            screen.blit(self.lizi2_list[self.lizi2_count], (800, 500))
            screen.blit(self.lizi2_list[self.lizi2_count], (1100, 500))
            self.lizi2_count += 1
        # if self.lizi3_count:
        #     screen.blit(self.lizi3_list[self.lizi3_count], (-100, -120))
        #     screen.blit(self.lizi3_list[self.lizi3_count], (200, -200))
        #     screen.blit(self.lizi3_list[self.lizi3_count], (500, -120))
        #     screen.blit(self.lizi3_list[self.lizi3_count], (800, -200))
        #     screen.blit(self.lizi3_list[self.lizi3_count], (1100, -120))
        #     self.lizi3_count += 1


        if self.lizi_count:
            screen.blit(self.lizi_list[self.lizi_count], (-100, 600))
            screen.blit(self.lizi_list[self.lizi_count], (200, 550))
            screen.blit(self.lizi_list[self.lizi_count], (500, 600))
            screen.blit(self.lizi_list[self.lizi_count], (800, 550))
            screen.blit(self.lizi_list[self.lizi_count], (1100, 600))
            self.lizi_count+=1
        if self.die_count &gt;=64:
            self.die_count=0
            self.life=100
            self.kill_enemy=0
            self.die = False
            self.stand = True
            return


        if self.stand_count&gt;=24:
            self.stand_count=1


        if self.flc_count&gt;=32:
            self.flc_count=0
            self.flc=False


        if self.life_count&gt;=8:
            self.life_count=0
            self.life_remove_bool=False


        if self.attack_one_count&gt;=13:
            self.attack_one_count=1
            self.stand=True
            self.attack_Bool = False


        if self.attack_two_count&gt;=6:
            self.attack_two_count=1
            self.stand = True
            self.attack_Bool = False


        if self.attack_three_count&gt;=11:
            self.attack_three_count=1
            self.stand = True
            self.attack_Bool = False


        if self.walk_count&gt;=12:
            self.walk_count=1


        if self.jump_count&gt;=38:
            self.jump_count=1
        if self.jn_count&gt;=40:
            self.jn_count=1
        if self.hit_count&gt;=47:
            self.hit_count=1


        if self.die_count==20:
            diren_die_music.play()








        if self.life_remove_bool and not self.die:
            screen.blit(self.life_list[self.life_count],(self.x,self.y))
            if self.life_count==0:
                player_hit_music.play()
            elif self.life_count==5:
                player_hit_music.stop()
            self.stand=False
            self.i = False
            self.j = False
            self.left=False
            self.right=False
            self.jump = False
            self.flc = False
            self.life_count+=1
        elif self.stand and not self.jump and not self.i and not self.flc  and not self.hit and not self.attack_Bool and not self.life_remove_bool and not self.die:
            screen.blit(self.stand_list[self.stand_count],(self.x,self.y))
            self.stand_count+=1
        elif self.right and not self.stand and not self.jump and not self.i and not self.flc  and not self.hit and not self.attack_Bool and not self.life_remove_bool and not self.die:  # 如果没有站立中 并且left=True,
            screen.blit(self.walk_right[self.walk_count], (self.x,self.y))  # 绘制马里奥
            self.walk_count += 1
            if self.walk_count==2:
                walk_music.play()
            elif self.walk_count==1:
                walk_music.stop()
        elif self.left and not self.stand and not self.jump and not self.i and not self.flc and not self.hit and not self.attack_Bool and not self.life_remove_bool and not self.die:  # 如果没有站立中 并且left=True,
            screen.blit(self.walk_left[self.walk_count], (self.x,self.y))  # 绘制马里奥
            self.walk_count += 1
            if self.walk_count==2:
                walk_music.play()
            elif self.walk_count==1:
                walk_music.stop()
        elif self.flc  and not self.die:
            if self.flc_count==1:
                feiti_music.play()
            if self.flc_count==20:
                feiti_music.stop()
            screen.blit(self.flc_list[self.flc_count], (self.x, self.y-120))
            self.flc_count += 1
        elif self.i  and not self.die:
            screen.blit(self.jn_list[self.jn_count],(self.x,self.y-75))
            self.jn_count+=1
            if self.jn_count == 2:
                jn_music.play()
            elif self.jn_count == 1:
                jn_music.stop()
        elif self.jump and not self.attack_Bool and not self.die:
            screen.blit(self.jump_list[self.jump_count],(self.x,self.y-75))
            self.jump_count+=1
            if self.jump_count == 2:
                jump_music.play()
            elif self.jump_count == 1:
                jump_music.stop()
        elif self.attack==1 and self.attack_Bool and not self.die:
            screen.blit(self.attack_list_one[self.attack_one_count],(self.x,self.y))
            self.attack_one_count += 1
            if self.attack_one_count==2:
                attack_music.play()
            elif self.attack_one_count==1:
                attack_music.stop()
        elif self.attack==2 and self.attack_Bool and not self.die:
            screen.blit(self.attack_list_two[self.attack_two_count],(self.x,self.y))
            self.attack_two_count += 1
            if self.attack_two_count == 2:
                attack_music.play()
            elif self.attack_two_count == 1:
                attack_music.stop()
        elif self.attack==3 and self.attack_Bool and not self.die:
            screen.blit(self.attack_list_three[self.attack_three_count],(self.x,self.y))
            self.attack_three_count += 1
            if self.attack_three_count == 2:
                attack_music.play()
            elif self.attack_three_count == 1:
                attack_music.stop()


        elif self.hit and not self.die:
            screen.blit(self.hit_list[self.hit_count],(self.x,self.y))
            self.hit_count+=1


        elif self.die:
            self.life = 0
            self.skill = False
            self.attack = False
            screen.blit(self.die_list[self.die_count],(self.x-100,self.y-20))
            self.die_count+=1


        self.hit_box = (self.x, self.y, self.width, self.height)








        if self.levelAdd:
            LEVAdd = font.render("LEVEL UP ", True, (255, 0, 0))
            screen.blit(LEVAdd, (player.x - 50, player.y - 50))
            screen.blit(self.level_tuple[self.level_count],(self.x-40,self.y-90))
            self.level_count+=1


        if self.lifeAdd:
            screen.blit(self.HP_tuple[self.HP_count],(self.x,self.y-40))
            self.HP_count+=1


        if self.all:
            self.all_lenth+=50
            screen.blit(self.all_tuple[self.all_count],(self.x+self.all_lenth,self.y+(self.height/2)-210))
            self.all_count+=1


        #是否胜利
        if self.kill_enemy&gt;=7:
            self.win_bool=True
        else:
            self.win_bool=False






#敌人死亡删除
def die_enemy_green():
    enemylist.pop()
def die_enemy_grey():
    enemylist2.pop()
def die_enemy_pink():
    enemylist3.pop()
def die_enemy_Boss():
    enemylist4.pop()






#BIG   BOSS
class Boss(object):
    walk_tuple = ()         #走路元组
    skill_tuple = ()        #远攻元组
    attack_tuple = ()       #近攻元组
    life_remove_tuple = ()          #受伤元组
    die_tuple = ()          #死亡元组
    arm_tuple = ()          #胳膊元组
    for pic_num in range(1,13):
        walk_tuple += (pygame.image.load("./yellow/walk1/1 ("+str(pic_num)+").png"),)
    for pic_num in range(1,34):
        skill_tuple += (pygame.image.load("./yellow/skill/skill ("+str(pic_num)+").png"),)
    for pic_num in range(1,30):
        attack_tuple += (pygame.image.load("./yellow/attack/attack ("+str(pic_num)+").png"),)
    for pic_num in range(1,40):
        life_remove_tuple += (pygame.image.load("./yellow/hit/hit ("+str(pic_num)+").png"),)
    for pic_num in range(1,13):
        die_tuple += (pygame.image.load("./yellow/die/die ("+str(pic_num)+").png"),)
    for pic_num in range(1,13):
        die_tuple += (pygame.image.load("./yellow/die/die ("+str(pic_num)+").png"),)
    for pic_num in range(1,13):
        die_tuple += (pygame.image.load("./yellow/die/die ("+str(pic_num)+").png"),)
    for pic_num in range(1,13):
        die_tuple += (pygame.image.load("./yellow/die/die ("+str(pic_num)+").png"),)
    for pic_num in range(1,13):
        die_tuple += (pygame.image.load("./yellow/die/die ("+str(pic_num)+").png"),)
    for pic_num in range(1,7):
        arm_tuple += (pygame.image.load("./yellow/arm/arm ("+str(pic_num)+").png"),)
    def __init__(self,x,y,start,end):
        self.x = x
        self.y = y
        self.width = 149
        self.height = 122
        self.area = [start,end]
        self.Yarea = [390-self.height,640-self.height]
        self.walk_count = 0             #走路图片索引
        self.skill_count = 0            #远攻图片索引
        self.attack_count = 0           #近攻图片索引
        self.life_count = 0              #倒地图片索引
        self.die_count = 0              #逃跑图片索引
        self.arm_count = 0              #胳膊图片索引
        self.life = 0                  #boss生命值
        self.speed = 1.5                #x轴移动速度
        self.speed_Y = 1.9              #y轴移动速度
        self.hit_box = (self.x,self.y,self.width,self.height)       #碰撞检测
        self.die = False
        self.walk = True
        self.skill=False
        self.attack=False
        self.life_remove_bool=False
        self.Enemy_Y = 0                #保留受伤 Y轴 位置
        self.enemy_img = pygame.image.load("./HP/enemy_yellow.png")      #生命值图标
        self.game_start_Bool = True                 #加载血条长度
    def draw(self,screen):
        global HP_img_boss
        global HP_bool_boss
        if self.game_start_Bool:
            self.life+=0.5
            if self.life&gt;15:
                self.life=15
                self.game_start_Bool=False
        self.move()


        if self.life &lt;= 0:
            self.life_remove_bool = False
            self.die = True
            self.walk = False


        if self.arm_count&gt;=6:
            self.arm_count=0


        if self.life_count&gt;=39:
            # self.y=self.Enemy_Y
            self.life_count=0
            self.life_remove_bool=False
            self.walk=True
        # 敌方走路
        if self.walk_count&gt;=12:
            self.walk_count=0


        #敌方远程攻击
        if self.skill_count==20 and not self.life_remove_bool and not self.die:
            if collision_check_tanke(player, enemylist4[0]):
                player.life -= 8
                player.life_remove_bool = True
                if player.life&lt;=0:
                    player.die=True
        # 敌方近程攻击
        if self.attack_count == 17 and not self.life_remove_bool and not self.die:
            if collision_check_tanke_yellow(player, enemylist4[0]):
                player.life -= 8
                player.life_remove_bool = True
                if player.life&lt;=0:
                    player.die=True


        #敌方 远程 技能
        if self.skill_count &gt;= 33:
            self.skill_count = 0
            self.skill=False
            self.walk=True


        # 敌方 近程 技能
        if self.attack_count &gt;= 29:
            self.attack_count = 0
            self.attack = False
            self.walk = True


            #坦克死亡
        if self.die_count &gt;= 60:
            HP_img_boss = Prop_Hp(random.randint(int(self.x), int(self.x + self.width)), random.randint(int(self.y), int(self.y + self.height)))
            HP_bool_boss=True
            player.kill_enemy+=1
            self.die_count=0
            self.skill_count=0
            self.die=False
            self.walk=True
            self.speed_Y*=2.5
            self.speed*=2.5
            self.life=0
            self.game_start_Bool = True
            self.y=500
            game_over_music.stop()
            die_enemy_Boss()
            return
        #死亡音效
        if self.die_count==20:
            game_over_music.play()


        if self.life_remove_bool:
            self.walk=False
            self.skill = False
            self.attack = False
            screen.blit(self.life_remove_tuple[self.life_count], (self.x, self.y))
            self.life_count += 1
            # self.y = player.y + player.height - enemylist4[0].height - 10


        elif self.skill and not  self.life_remove_bool:
            if self.skill_count==15:
                green_jn.play()
            if self.skill_count==1:
                green_jn.stop()


            screen.blit(self.skill_tuple[self.skill_count], (self.x-150, self.y-50))
            self.skill_count+=1
        elif self.attack and not  self.life_remove_bool:
            screen.blit(self.attack_tuple[self.attack_count],(self.x-250,self.y))
            self.attack_count+=1
        if self.attack_count == 10 and self.attack:
            green_attack_music.play()
        if self.attack_count == 29 or not self.attack:
            green_attack_music.stop()


        if self.speed&gt;0 and self.walk and not self.die:
            self.skill = False
            screen.blit(self.walk_tuple[self.walk_count],(self.x,self.y))
            self.walk_count+=1
        elif  self.speed&lt;0 and self.walk:
            screen.blit(self.walk_tuple[self.walk_count],(self.x,self.y))
            self.walk_count+=1
        elif self.die:
            self.life = 0
            self.skill = False
            self.attack = False
            if self.die_count%2==0 and self.die_count&lt;20:
                pygame.time.delay(10)
                screen.fill([0, 0, 0])# 敌人 死亡特效
            elif  self.die_count%2==1 and self.die_count&lt;20:
                pygame.time.delay(10)
                screen.fill([255, 0, 0])# 敌人 死亡特效


            self.x += 11
            screen.blit(self.arm_tuple[self.arm_count],(700,500))
            self.arm_count+=1
            screen.blit(self.die_tuple[self.die_count],(self.x,self.y))
            self.die_count+=1
        # 绘制血条
        screen.blit(self.enemy_img, (1160, 0))
        pygame.draw.rect(screen, (218, 234, 87), (600 + (15 - self.life) * (540 / 15), 40, (540 / 15) * self.life, 30))
        if self.game_start_Bool == False and self.life &lt; 15:
            pygame.draw.rect(screen, (102, 115, 44), (600, 40, 540 - (540 / 15 * self.life), 30))


    # 敌人移动类
    def move(self):


        #遇敌人反向
        if collision_check_fanxiang(player, enemylist4[0]) or collision_check_fanxiang( enemylist4[0], player) :
            enemylist4[0].speed = enemylist4[0].speed * -1
        # 当机甲没有进行攻击时
        if player.walk_right  or player.stand:
        #敌人远程技能
            if collision_check_tanke(player, enemylist4[0])  and not self.life_remove_bool and not self.die  and not self.attack and ( player.stand or player.left or player.right ) and not player.die :
                self.skill=True
                self.walk = False
            # 敌人近程技能
            if collision_check_tanke_yellow(player, enemylist4[0]) and not self.life_remove_bool and not self.die  and not self.skill and ( player.stand or player.left or player.right ) and not player.die:
                self.attack = True
                self.walk = False


        if self.die_count &gt;= 60:
            return


        if self.walk:
            # y移动
            if self.speed_Y&gt;0  and not self.die:
                if self.y&lt;self.Yarea[1]+self.speed_Y:
                    self.y += self.speed_Y
                else:
                    self.speed_Y=self.speed_Y*(-1)
                    self.y+=self.speed_Y
                    self.walk_count=0
            elif  self.speed_Y&lt;0  and not self.die:
                if self.y&gt;self.Yarea[0]-self.speed_Y:
                    self.y+=self.speed_Y
                else:
                    self.speed_Y = self.speed_Y * (-1)
                    self.y += self.speed_Y
                    self.walk_count = 0


            if self.speed&gt;0 and not self.die:
                # X移动
                if self.x&lt;self.area[1]+self.speed:
                    self.x+=self.speed
                else:
                    self.speed=self.speed*(-1)
                    self.x+=self.speed
                    self.walk_count=0
            elif self.speed&lt;0  and not self.die:
                # X移动
                if self.x&gt;self.area[0]-self.speed:
                    self.x+=self.speed
                else:
                    self.speed=self.speed*(-1)
                    self.x+=self.speed
                    self.walk_count=0


#敌人  BOSS 章鱼
class Enemy_pink(object):
    walk_left=()
    walk_right=()
    die_list = ()
    life_remove_list = ()
    falsh_list=()
    skill_list=()
    attack_list = ()
    for pic_num in range(1,83):
        attack_list+=(pygame.image.load("./pink/attack/attack1 ("+str(pic_num)+").png"),)
    for pic_num in range(1,17):
        walk_left+=(pygame.image.load("./pink/walk/"+str(pic_num)+".png"),)
    for pic_num in range(16,0,-1):
        walk_right+=(pygame.image.load("./pink/walk/"+str(pic_num)+".png"),)
    for pic_num in range(1,51):
        skill_list+=(pygame.image.load("./pink/skill2/"+str(pic_num)+".png"),)
    #敌人 先起飞 再死亡
    for pic_num in range(1,58):
        die_list+=(pygame.image.load("./pink/die/die ("+str(pic_num)+").png"),)
    # 减血
    for pic_num in range(1,29):
        life_remove_list+=(pygame.image.load("./pink/hit/hit ("+str(pic_num)+").png"),)


    def __init__(self,x,y,start,end):
        self.x=x
        self.y=y
        self.width=361
        self.height=179
        self.area=[start,end]
        self.Yarea = [440, 500] # Y轴 运动 区间
        self.walk_count=1
        self.speed=-2
        self.speed_Y=1.9
        self.life=0
        self.hit_box = (self.x, self.y, self.width, self.height)
        self.die=False
        self.walk=True
        self.die_count=1
        self.life_count=1
        self.skill_count=1
        self.attack_count=0
        self.life_remove_bool=False
        self.skill=False
        self.attack = False
        self.Enemy_Y=0  #保留受伤 Y轴 位置
        self.enemy_img = pygame.image.load("./HP/enemy_pink.png")
        self.HP_img = pygame.image.load("./HP/电池.png")
        self.game_start_Bool=True
    def draw(self,screen):
        global HP_img_pink
        global HP_bool_pink
        if self.game_start_Bool:
            self.life+=0.17
            if self.life&gt;3:
                self.life=3
                self.game_start_Bool=False


        self.move()


        if self.life &lt;= 0:
            self.life_remove_bool = False
            self.die = True
            self.walk = False


        if self.life_count&gt;=28:
            # self.y=self.Enemy_Y
            self.life_count=0
            self.life_remove_bool=False
            self.walk=True
        # 敌方走路
        if self.walk_count&gt;=16:
            self.walk_count=0


        #敌方远程攻击
        if self.skill_count==30 and not self.life_remove_bool and not self.die:
            if collision_check_tanke_jincheng(player, enemylist3[0]):
                player.life -= 8
                player.life_remove_bool = True
                if player.life&lt;=0:
                    player.die=True
        # 敌方近程攻击
        if self.attack_count == 50 and not self.life_remove_bool and not self.die:
            if collision_check_tanke(player, enemylist3[0]):
                player.life -= 8
                player.life_remove_bool = True
                if player.life&lt;=0:
                    player.die=True


        #敌方 远程 技能
        if self.skill_count &gt;= 50:
            self.skill_count = 0
            self.skill=False
            self.walk=True


        # 敌方 近程 技能
        if self.attack_count &gt;= 82:
            self.attack_count = 0
            self.attack = False
            self.walk = True


            #坦克死亡
        if self.die_count &gt;= 57:
            HP_img_pink = Prop_Hp(random.randint(int(self.x), int(self.x + self.width)), random.randint(int(self.y), int(self.y + self.height)))
            HP_bool_pink=True
            player.kill_enemy+=1
            self.die_count=0
            self.skill_count=0
            self.die=False
            self.walk=True
            self.speed_Y*=2.5
            self.speed*=2.5
            self.life=0
            self.game_start_Bool=True
            diren_die_music.stop()
            die_enemy_pink()
            return
        #死亡音效
        if self.die_count==20:
            diren_die_music.play()


        if self.life_remove_bool:
            # if player.jump or player.i:
            #     self.y = player.y + player.height - enemylist3[0].height - 10
            self.walk=False
            self.skill = False
            self.attack = False
            screen.blit(self.life_remove_list[self.life_count], (self.x, self.y))
            self.life_count += 1
            # self.y = player.y + player.height - enemylist3[0].height - 10


        elif self.skill and not  self.life_remove_bool:
            if self.skill_count==15:
                green_jn.play()
            if self.skill_count==1:
                green_jn.stop()
            screen.blit(self.skill_list[self.skill_count], (self.x-150, self.y-50))
            self.skill_count+=1
        elif self.attack and not  self.life_remove_bool:
            screen.blit(self.attack_list[self.attack_count],(self.x-250,self.y-100))
            self.attack_count+=1
        if self.attack_count == 10 and self.attack:
            green_attack_music.play()
        if self.attack_count == 55 or not self.attack:
            green_attack_music.stop()


        if self.speed&gt;0 and self.walk and not self.die:
            self.skill = False
            screen.blit(self.walk_left[self.walk_count],(self.x,self.y))
            self.walk_count+=1
        elif  self.speed&lt;0 and self.walk:
            screen.blit(self.walk_left[self.walk_count],(self.x,self.y))
            self.walk_count+=1
        elif self.die:
            self.life = 0
            self.skill = False
            self.attack = False
            if self.die_count%2==0 and self.die_count&lt;20:
                pygame.time.delay(20)
                screen.fill([0, 0, 0])# 敌人 死亡特效
            elif  self.die_count%2==1 and self.die_count&lt;20:
                pygame.time.delay(20)
                screen.fill([255, 0, 0])# 敌人 死亡特效


            # if self.die_count&lt;13:
            #     self.y = player.y + player.height - self.height - 10
            screen.blit(self.die_list[self.die_count],(self.x,self.y))
            self.die_count+=1
        # 绘制血条
        screen.blit(self.enemy_img, (1040, -45))
        pygame.draw.rect(screen, (235, 35, 200), (600 + (3 - self.life) * (540 / 3), 40, (540 / 3) * self.life, 30))
        if self.game_start_Bool == False and self.life &lt; 3:
            pygame.draw.rect(screen, (80, 0, 100), (600, 40, 540 - (540 / 3 * self.life), 30))




    # 敌人移动类
    def move(self):


        #遇敌人反向
        if collision_check_fanxiang(player, enemylist3[0]) or collision_check_fanxiang( enemylist3[0], player) :
            enemylist3[0].speed = enemylist3[0].speed * -1
        # 当机甲没有进行攻击时
        if player.walk_right  or player.stand:
        #敌人远程技能
            if collision_check_tanke_jincheng(player, enemylist3[0])  and not self.life_remove_bool and not self.die  and not self.attack and ( player.stand or player.left or player.right ):
                self.skill=True
                self.walk = False
            # 敌人近程技能
            if collision_check_tanke(player, enemylist3[0]) and not self.life_remove_bool and not self.die  and not self.skill and ( player.stand or player.left or player.right ):
                self.attack = True
                self.walk = False


        if self.die_count &gt;= 57:
            return


        if self.walk:
            # y移动
            if self.speed_Y&gt;0  and not self.die:
                if self.y&lt;self.Yarea[1]+self.speed_Y:
                    self.y += self.speed_Y
                else:
                    self.speed_Y=self.speed_Y*(-1)
                    self.y+=self.speed_Y
                    self.walk_count=0
            elif  self.speed_Y&lt;0  and not self.die:
                if self.y&gt;self.Yarea[0]-self.speed_Y:
                    self.y+=self.speed_Y
                else:
                    self.speed_Y = self.speed_Y * (-1)
                    self.y += self.speed_Y
                    self.walk_count = 0


            if self.speed&gt;0 and not self.die:
                # X移动
                if self.x&lt;self.area[1]+self.speed:
                    self.x+=self.speed
                else:
                    self.speed=self.speed*(-1)
                    self.x+=self.speed
                    self.walk_count=0
            elif self.speed&lt;0  and not self.die:
                # X移动
                if self.x&gt;self.area[0]-self.speed:
                    self.x+=self.speed
                else:
                    self.speed=self.speed*(-1)
                    self.x+=self.speed
                    self.walk_count=0


#灰色敌人
class Enemy_grey(object):  # 声明灰色敌人类
    walk_left=()
    walk_right=()
    die_list = ()
    life_remove_list = ()
    falsh_list=()
    skill_list=()
    # attack_list=()


    for pic_num in range(2, 0, -1):  # 循环敌人向右行走的图片
        walk_right+=(pygame.image.load("./grey/walk/walk (" + str(pic_num) + ").png"),)
        # 加载向右行走的图片
    for pic_num in range(1, 3):  # 循环敌人向左行走的图片
        walk_left+=(pygame.image.load("./grey/walk/walk (" + str(pic_num) + ").png"),)
        # 加载向左行走的图片
    for pic_num in range(1,22):
        skill_list+=(pygame.image.load("./grey/skill/skill ("+str(pic_num)+").png"),)


    #敌人 先起飞 再死亡
    for pic_num in range(1,36):
        die_list+=(pygame.image.load("./grey/hit/hit ("+str(pic_num)+").png"),)
    for pic_num in range(1,45):
        die_list+=(pygame.image.load("./grey/die/die ("+str(pic_num)+").png"),)
    # 减血
    for pic_num in range(1,24):
        life_remove_list+=(pygame.image.load("./grey/hit/hit ("+str(pic_num)+").png"),)


    def __init__(self,x,y,start,end):
        self.x=x
        self.y=y
        self.width=124
        self.height=100
        self.area=[start,end]
        self.Yarea = [370, 430] # Y轴 运动 区间
        self.walk_count=0
        self.speed=-1.9
        self.speed_Y=1.9
        self.life=0
        self.hit_box = (self.x, self.y, self.width, self.height)
        self.die=False
        self.walk=True
        self.die_count=1
        self.life_count=1
        self.skill_count=1
        self.attack_count = 0
        self.life_remove_bool=False
        self.attack=False
        self.skill=False
        self.Enemy_Y=0  #保留受伤 Y轴 位置
        self.enemy_img = pygame.image.load("./HP/enemy_grey.png")
        self.HP_img = pygame.image.load("./HP/电池.png")
        self.game_start_Bool=True
    def draw(self,screen):
        global HP_img_grey
        global HP_bool_grey
        if self.game_start_Bool:
            self.life+=0.145
            if self.life &gt; 3:
                self.life = 3
                self.game_start_Bool = False


        self.move()
        # 敌方受击
        #检测生命
        if self.life &lt;= 0:
            self.life_remove_bool = False
            self.die = True
            self.walk = False


        # if self.life_count==2:
        #     self.Enemy_Y=self.y


        if self.life_count&gt;=23:
            # self.y=self.Enemy_Y
            self.life_count=1
            self.life_remove_bool=False
            self.walk=True


        # 敌方走路
        if self.walk_count==2:
            self.walk_count=0


        #机甲掉血
        if self.skill_count==12 and not self.life_remove_bool and not self.die:
            if collision_check_tanke_green(player, enemylist2[0]):
                player.life -= 8
                player.life_remove_bool = True
                if player.life&lt;=0:
                    player.die=True


        #敌方技能
        if self.skill_count &gt;= 21:
            self.skill_count = 1
            self.skill=False
            self.walk=True


            #坦克死亡
        if self.die_count &gt;= 78:
            HP_img_grey = Prop_Hp(random.randint(int(self.x), int(self.x + self.width)), random.randint(int(self.y), int(self.y + self.height)))
            HP_bool_grey=True
            player.kill_enemy += 1
            self.die_count=1
            self.skill_count = 1
            self.die=False
            self.walk=True
            self.speed_Y*=2.4
            self.speed*=2.4
            self.life=0
            self.game_start_Bool=True
            diren_die_music.stop()
            die_enemy_grey()
            return
        # 死亡音效
        if self.die_count==35:
            diren_die_music.play()


        if self.life_remove_bool:
            self.skill = False
            self.walk = False
            self.attack = False
            if player.jump or player.i:
                self.y = player.y + player.height - enemylist2[0].height - 10
            screen.blit(self.life_remove_list[self.life_count], (self.x-20, self.y-80))
            self.life_count += 1


        elif self.skill and not  self.life_remove_bool:
            screen.blit(self.skill_list[self.skill_count], (self.x-120, self.y))
            self.skill_count+=1


        if self.speed&gt;0 and self.walk and not self.die:
            self.skill = False
            screen.blit(self.walk_left[self.walk_count],(self.x,self.y))
            self.walk_count+=1
        elif  self.speed&lt;0 and self.walk and not self.die:
            screen.blit(self.walk_left[self.walk_count],(self.x,self.y))
            self.walk_count+=1
        elif self.die:
            self.life = 0
            self.skill = False
            self.attack = False
            if self.die_count%2==0 and self.die_count&lt;20:
                pygame.time.delay(20)
                screen.fill([0, 0, 0])# 敌人 死亡特效
            elif  self.die_count%2==1 and self.die_count&lt;20:
                pygame.time.delay(20)
                screen.fill([255, 0, 0])# 敌人 死亡特效


            # if self.die_count&lt;20:
            #     self.y=player.y+player.height-self.height-10-120
            # else:
            #     self.y = self.Enemy_Y
            self.die_count+=1


            screen.blit(self.die_list[self.die_count], (self.x, self.y))
        # 绘制血条
        screen.blit(self.enemy_img, (1150, 63))
        pygame.draw.rect(screen, (130, 200, 200), (600 + (3 - self.life) * (540 / 3), 100, (540 / 3) * self.life, 30))
        if self.game_start_Bool == False and self.life &lt; 3:
            pygame.draw.rect(screen, (50, 75, 75), (600, 100, 540 - (540 / 3 * self.life), 30))


    # 敌人移动类
    def move(self):
        #遇敌人反向
        if collision_check_fanxiang(player, enemylist2[0]) or collision_check_fanxiang( enemylist2[0], player) :
            enemylist2[0].speed = enemylist2[0].speed * -1
        # 当机甲没有进行攻击时
        if player.walk_right or player.walk_right or player.stand:
            #远攻
            if collision_check_tanke(player, enemylist2[0])  and not self.life_remove_bool and not self.die:
                self.skill=True
                self.walk = False


        if self.walk:
            # y移动
            if self.speed_Y&gt;0  and not self.die:
                if self.y&lt;self.Yarea[1]+self.speed_Y:
                    self.y += self.speed_Y
                else:
                    self.speed_Y=self.speed_Y*(-1)
                    self.y+=self.speed_Y
                    self.walk_count=0
            elif  self.speed_Y&lt;0  and not self.die:
                if self.y&gt;self.Yarea[0]-self.speed_Y:
                    self.y+=self.speed_Y
                else:
                    self.speed_Y = self.speed_Y * (-1)
                    self.y += self.speed_Y
                    self.walk_count = 0


            if self.speed&gt;0 and not self.die:
                # X移动
                if self.x&lt;self.area[1]+self.speed:
                    self.x+=self.speed
                else:
                    self.speed=self.speed*(-1)
                    self.x+=self.speed
                    self.walk_count=0
            elif self.speed&lt;0  and not self.die:
                # X移动
                if self.x&gt;self.area[0]-self.speed:
                    self.x+=self.speed
                else:
                    self.speed=self.speed*(-1)
                    self.x+=self.speed
                    self.walk_count=0


#敌人 绿色坦克
class Enemy(object):
    walk_left=()
    walk_right=()
    die_list = ()
    life_remove_list = ()
    falsh_list=()
    skill_list=()
    attack_list = ()


    for pic_num in range(1,24):
        attack_list+=(pygame.image.load("./green/attack/attack ("+str(pic_num)+").png"),)
    for pic_num in range(1,9):
        walk_left+=(pygame.image.load("./green/walk/walk ("+str(pic_num)+").png"),)
    for pic_num in range(8,0,-1):
        walk_right+=(pygame.image.load("./green/walk/walk ("+str(pic_num)+").png"),)
    for pic_num in range(1,38):
        skill_list+=(pygame.image.load("./green/skill/skill ("+str(pic_num)+").png"),)


    #敌人 先起飞 再死亡
    for pic_num in range(1,40):
        die_list+=(pygame.image.load("./green/die/hit ("+str(pic_num)+").png"),)
    for pic_num in range(1,65):
        die_list+=(pygame.image.load("./green/die/die ("+str(pic_num)+").png"),)
    # 减血
    for pic_num in range(1,24):
        life_remove_list+=(pygame.image.load("./green/die/hit ("+str(pic_num)+").png"),)


    def __init__(self,x,y,start,end):
        self.x=x
        self.y=y
        self.width=133
        self.height=95
        self.area=[start,end]
        self.Yarea = [300, 360] # Y轴 运动 区间
        self.walk_count=1
        self.speed=-1.5
        self.speed_Y=1.9
        self.life=0
        self.hit_box = (self.x, self.y, self.width, self.height)
        self.die=False
        self.walk=True
        self.die_count=1
        self.life_count=1
        self.skill_count=1
        self.attack_count=0
        self.life_remove_bool=False
        self.skill=False
        self.attack = False
        self.Enemy_Y=0  #保留受伤 Y轴 位置
        self.enemy_img=pygame.image.load("./HP/enemy_green.png")
        self.game_start_Bool=True
    def draw(self,screen):
        global HP_img_green
        global HP_bool_green
        if self.game_start_Bool:
            self.life+=0.12
            if self.life &gt; 3:
                self.life = 3
                self.game_start_Bool = False


        self.move()


        if self.life &lt;= 0:
            self.life_remove_bool = False
            self.die = True
            self.walk = False


        # 敌方受击
        # if self.life_count==2:
        #     self.Enemy_Y=self.y




        if self.life_count&gt;=23:
            # self.y=self.Enemy_Y
            self.life_count=0
            self.life_remove_bool=False
            self.walk=True


        # 敌方走路
        if self.walk_count&gt;=8:
            self.walk_count=0


        #敌方远程攻击
        if self.skill_count==25 and not self.life_remove_bool and not self.die:
            if collision_check_tanke(player, enemylist[0]):
                player.life -= 8
                player.life_remove_bool = True
                if player.life&lt;=0:
                    player.die=True
        # 敌方近程攻击
        if self.attack_count == 14 and not self.life_remove_bool and not self.die:
            if collision_check_tanke_jincheng(player, enemylist[0]):
                player.life -= 8
                player.life_remove_bool = True
                if player.life&lt;=0:
                    player.die=True


        #敌方 远程 技能
        if self.skill_count &gt;= 37:
            self.skill_count = 0
            self.skill=False
            self.walk=True


        # 敌方 近程 技能
        if self.attack_count &gt;= 23:
            self.attack_count = 0
            self.attack = False
            self.walk = True


            #坦克死亡
        if self.die_count &gt;= 103:
            HP_img_green = Prop_Hp(random.randint(int(self.x), int(self.x + self.width)), random.randint(int(self.y), int(self.y + self.height)))
            HP_bool_green=True
            player.kill_enemy+=1
            self.die_count=0
            self.skill_count=0
            self.die=False
            self.walk=True
            self.speed_Y*=2.2
            self.speed*=2.2
            self.life=0
            self.game_start_Bool=True
            diren_die_music.stop()
            die_enemy_green()
            return


        #死亡音效
        if self.die_count==40:
            diren_die_music.play()


        if self.life_remove_bool:
            if player.jump or player.i:
                self.y = player.y + player.height - enemylist[0].height - 10
            self.walk=False
            self.skill = False
            self.attack = False
            screen.blit(self.life_remove_list[self.life_count], (self.x, self.y))
            self.life_count += 1
            # self.y = player.y + player.height - enemylist[0].height - 10


        if self.skill and not  self.life_remove_bool:
            if self.skill_count==20:
                green_jn.play()
            if self.skill_count==1:
                green_jn.stop()
            screen.blit(self.skill_list[self.skill_count], (self.x-150, self.y-90))
            self.skill_count+=1


        if self.attack_count == 1 and self.attack :
            green_attack_music.play()
        if self.attack_count == 15 or not self.attack:
            green_attack_music.stop()


        if self.attack and not  self.life_remove_bool:
            screen.blit(self.attack_list[self.attack_count],(self.x-50,self.y))
            self.attack_count+=1






        if self.speed&gt;0 and self.walk and not self.die:
            self.skill = False
            screen.blit(self.walk_left[self.walk_count],(self.x,self.y))
            self.walk_count+=1
        elif  self.speed&lt;0 and self.walk:
            screen.blit(self.walk_left[self.walk_count],(self.x,self.y))
            self.walk_count+=1
        elif self.die:
            self.skill = False
            self.attack = False
            self.life = 0




            if self.die_count%2==0 and self.die_count&lt;20:
                pygame.time.delay(20)
                screen.fill([0, 0, 0])# 敌人 死亡特效
            elif  self.die_count%2==1 and self.die_count&lt;20:
                pygame.time.delay(20)
                screen.fill([255, 0, 0])# 敌人 死亡特效


            screen.blit(self.die_list[self.die_count],(self.x,self.y))
            self.die_count+=1
        # 绘制血条
        screen.blit(self.enemy_img, (1125, 120))
        pygame.draw.rect(screen, (0, 200, 115), (600 + (3 - self.life) * (540 / 3), 160, (540 / 3) * self.life, 30))
        if self.game_start_Bool == False and self.life &lt; 3:
            pygame.draw.rect(screen, (0, 65, 20), (600, 160, 540 - (540 / 3 * self.life), 30))


    # 敌人移动类
    def move(self):


        #遇敌人反向
        if collision_check_fanxiang(player, enemylist[0]) or collision_check_fanxiang( enemylist[0], player) :
            enemylist[0].speed = enemylist[0].speed * -1
        #当机甲没有进行攻击时
        if player.walk_right or player.walk_right or player.stand:
        #敌人远程技能
            if collision_check_tanke(player, enemylist[0])  and not self.life_remove_bool and not self.die  and not self.attack:
                self.skill=True
                self.walk = False
            # 敌人近程技能
            if collision_check_tanke_jincheng(player, enemylist[0]) and not self.life_remove_bool and not self.die  and not self.skill:
                self.attack = True
                self.walk = False


        if self.die_count &gt;= 63:
            return


        if self.walk:
            # y移动
            if self.speed_Y&gt;0  and not self.die:
                if self.y&lt;self.Yarea[1]+self.speed_Y:
                    self.y += self.speed_Y
                else:
                    self.speed_Y=self.speed_Y*(-1)
                    self.y+=self.speed_Y
                    self.walk_count=0
            elif  self.speed_Y&lt;0  and not self.die:
                if self.y&gt;self.Yarea[0]-self.speed_Y:
                    self.y+=self.speed_Y
                else:
                    self.speed_Y = self.speed_Y * (-1)
                    self.y += self.speed_Y
                    self.walk_count = 0


            if self.speed&gt;0 and not self.die:
                # X移动
                if self.x&lt;self.area[1]+self.speed:
                    self.x+=self.speed
                else:
                    self.speed=self.speed*(-1)
                    self.x+=self.speed
                    self.walk_count=0
            elif self.speed&lt;0  and not self.die:
                # X移动
                if self.x&gt;self.area[0]-self.speed:
                    self.x+=self.speed
                else:
                    self.speed=self.speed*(-1)
                    self.x+=self.speed
                    self.walk_count=0


#血瓶
class Prop_Hp(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.width=64
        self.height=64
        self.HP=2
        self.imglist=[pygame.image.load("./HP/HP.png"),pygame.image.load("./HP/HP2.png"),pygame.image.load("./HP/HP3.png"),pygame.image.load("./HP/gun.png"),pygame.image.load("./HP/gun2.png"),pygame.image.load("./HP/gun3.png"),pygame.image.load("./HP/gun4.png")]
        self.ran=random.randint(0,6)
        self.img=self.imglist[self.ran]
    def draw(self,screen):
        global HP_bool_green
        global HP_bool_grey
        global HP_bool_pink
        screen.blit(self.img,(self.x,self.y))
        if HP_bool_grey:
            if HP_img_grey.imglist.index(HP_img_grey.img)&gt;2:
                if collision_check_tanke_HP(player, HP_img_grey):
                    player.levelAdd = True
                    player.level += 1
                    player.life += 5




                    if player.life &gt; 100:
                        player.life = 100
                    HP_bool_grey = False
            else:
                if collision_check_tanke_HP(player, HP_img_grey):
                    player.lifeAdd=True
                    player.life += 5
                    if player.life &gt;= 100:
                       player.life=100
                    HP_bool_grey=False


        if HP_bool_green:
            if HP_img_green.imglist.index(HP_img_green.img) &gt; 2:
                if collision_check_tanke_HP(player, HP_img_green):
                    player.levelAdd = True
                    player.level += 1
                    player.life += 5


                    if player.life &gt; 100:
                        player.life = 100
                    HP_bool_green = False
            else:
                if collision_check_tanke_HP(player, HP_img_green):
                    player.lifeAdd = True
                    player.life += 5
                    if player.life &gt;= 100:
                       player.life=100
                    HP_bool_green=False


        if HP_bool_pink:
            if HP_img_pink.imglist.index(HP_img_pink.img) &gt; 2:
                if collision_check_tanke_HP(player, HP_img_pink):
                    player.levelAdd = True
                    player.level += 1
                    player.life += 5


                    if player.life&gt;100:
                        player.life=100
                    HP_bool_pink = False
            else:
                if collision_check_tanke_HP(player, HP_img_pink):
                    player.lifeAdd = True
                    player.life += 5
                    if player.life &gt;= 100:
                       player.life=100
                    HP_bool_pink=False


back_music.play(-1)


#主要绘制函数
def draw_img():
    global load_count
    global FRAM_PER_SECONDS
    global set_img
    if load_count&gt;=29:
        load_count=30
        load_music.stop()
        screen.blit(map_img, (0, 0))
        #打开  游戏 战斗背景 音乐
        back_music.set_volume(0.06)
        set_img=pygame.image.load("./load_img/setbig.png")
        screen.blit(set_img,(10,10))
        if HP_bool_green==True:
            HP_img_green.draw(screen)


        if HP_bool_grey==True:
            HP_img_grey.draw(screen)
        if HP_bool_pink==True:
            HP_img_pink.draw(screen)




        if len(enemylist) and  len(enemylist2) and  len(enemylist3):
            if  player.y+player.height &lt; enemylist[0].y+enemylist[0].height &lt; enemylist2[0].y+enemylist2[0].height &lt; enemylist3[0].y+enemylist3[0].height and not player.jump and not enemylist[0].die  and not enemylist2[0].die  and not enemylist3[0].die:
                player.draw(screen)
                enemylist[0].draw(screen)
                enemylist2[0].draw(screen)
                enemylist3[0].draw(screen)
            elif  enemylist[0].y+enemylist[0].height &lt;   player.y+player.height &lt; enemylist2[0].y+enemylist2[0].height &lt; enemylist3[0].y+enemylist3[0].height and not player.jump and not enemylist[0].die  and not enemylist2[0].die  and not enemylist3[0].die:
                enemylist[0].draw(screen)
                player.draw(screen)
                enemylist2[0].draw(screen)
                enemylist3[0].draw(screen)
            elif  enemylist[0].y+enemylist[0].height &lt; enemylist2[0].y+enemylist2[0].height &lt;  player.y+player.height &lt; enemylist3[0].y+enemylist3[0].height and not player.jump and not enemylist[0].die  and not enemylist2[0].die  and not enemylist3[0].die:
                enemylist[0].draw(screen)
                enemylist2[0].draw(screen)
                player.draw(screen)
                enemylist3[0].draw(screen)
            elif enemylist[0].y+enemylist[0].height &lt; enemylist2[0].y+enemylist2[0].height &lt; enemylist3[0].y+enemylist3[0].height &lt;  player.y+player.height and not player.jump and not enemylist[0].die  and not enemylist2[0].die  and not enemylist3[0].die:
                enemylist[0].draw(screen)
                enemylist2[0].draw(screen)
                enemylist3[0].draw(screen)
                player.draw(screen)
            elif player.jump :
                enemylist[0].draw(screen)
                enemylist2[0].draw(screen)
                enemylist3[0].draw(screen)
                player.draw(screen)
                #敌人受攻击时 先后绘制
            elif enemylist[0].life_remove_bool or enemylist[0].die:
                enemylist[0].draw(screen)
                enemylist3[0].draw(screen)
                enemylist2[0].draw(screen)
                player.draw(screen)
            elif enemylist2[0].life_remove_bool or enemylist2[0].die:
                enemylist[0].draw(screen)
                enemylist3[0].draw(screen)
                enemylist2[0].draw(screen)
                player.draw(screen)
            elif enemylist3[0].life_remove_bool or enemylist3[0].die:
                enemylist[0].draw(screen)
                enemylist2[0].draw(screen)
                enemylist3[0].draw(screen)
                player.draw(screen)
            elif enemylist[0].life_remove_bool and enemylist2[0].life_remove_bool or enemylist[0].die or enemylist2[0].die:
                enemylist3[0].draw(screen)
                enemylist[0].draw(screen)
                enemylist2[0].draw(screen)
                player.draw(screen)
            elif enemylist[0].life_remove_bool and enemylist3[0].life_remove_bool or enemylist[0].die or enemylist3[0].die:
                enemylist2[0].draw(screen)
                enemylist[0].draw(screen)
                enemylist3[0].draw(screen)
                player.draw(screen)
            elif enemylist2[0].life_remove_bool and enemylist3[0].life_remove_bool or enemylist2[0].die or enemylist3[0].die:
                enemylist[0].draw(screen)
                enemylist2[0].draw(screen)
                enemylist3[0].draw(screen)
                player.draw(screen)
            else:
                enemylist[0].draw(screen)
                enemylist2[0].draw(screen)
                enemylist3[0].draw(screen)
                player.draw(screen)






        elif  len(enemylist) and  len(enemylist2): #绿色和灰色


            if  player.y+player.height &lt; enemylist[0].y+enemylist[0].height &lt; enemylist2[0].y+enemylist2[0].height  and not player.jump  and not enemylist[0].die  and not enemylist2[0].die:
                player.draw(screen)
                enemylist[0].draw(screen)
                enemylist2[0].draw(screen)


            elif enemylist[0].y+enemylist[0].height &lt; player.y+player.height &lt; enemylist2[0].y+enemylist2[0].height  and not player.jump and not enemylist[0].die  and not enemylist2[0].die:


                enemylist[0].draw(screen)
                player.draw(screen)
                enemylist2[0].draw(screen)


            elif enemylist[0].y + enemylist[0].height &lt; enemylist2[0].y + enemylist2[0].height &lt; player.y + player.height and not player.jump and not enemylist[0].die  and not enemylist2[0].die:
                enemylist[0].draw(screen)
                enemylist2[0].draw(screen)
                player.draw(screen)
            elif player.jump :
                player.draw(screen)
                enemylist[0].draw(screen)
                enemylist2[0].draw(screen)
            # 敌人受攻击时 先后绘制
            elif enemylist[0].life_remove_bool or enemylist[0].die:#绿色
                enemylist[0].draw(screen)
                enemylist2[0].draw(screen)
                player.draw(screen)
            elif enemylist2[0].life_remove_bool or enemylist2[0].die:#灰色
                enemylist[0].draw(screen)
                enemylist2[0].draw(screen)
                player.draw(screen)
            elif enemylist[0].life_remove_bool and enemylist2[0].life_remove_bool or enemylist[0].die or enemylist2[0].die:#绿色和灰色
                enemylist[0].draw(screen)
                enemylist2[0].draw(screen)
                player.draw(screen)


        elif len(enemylist) and len(enemylist3): #绿色和粉色


            if  player.y+player.height &lt; enemylist[0].y+enemylist[0].height &lt; enemylist3[0].y+enemylist3[0].height  and not player.jump and not enemylist[0].die  and not enemylist3[0].die:
                player.draw(screen)
                enemylist[0].draw(screen)
                enemylist3[0].draw(screen)
            elif enemylist[0].y+enemylist[0].height &lt; player.y+player.height &lt; enemylist3[0].y+enemylist3[0].height  and not player.jump and not enemylist[0].die  and not enemylist3[0].die:
                enemylist[0].draw(screen)
                player.draw(screen)
                enemylist3[0].draw(screen)
            elif enemylist[0].y + enemylist[0].height &lt; enemylist3[0].y + enemylist3[0].height &lt; player.y + player.height and not player.jump and not enemylist[0].die  and not enemylist3[0].die:
                enemylist[0].draw(screen)
                enemylist3[0].draw(screen)
                player.draw(screen)
            elif player.jump :
                player.draw(screen)
                enemylist[0].draw(screen)
                enemylist3[0].draw(screen)
            # 敌人受攻击时 先后绘制
            elif enemylist[0].life_remove_bool or enemylist[0].die:  # 绿色
                enemylist[0].draw(screen)
                enemylist3[0].draw(screen)
                player.draw(screen)
            elif enemylist3[0].life_remove_bool or enemylist3[0].die:  # 粉色
                enemylist[0].draw(screen)
                enemylist3[0].draw(screen)
                player.draw(screen)
            elif enemylist[0].life_remove_bool and enemylist3[0].life_remove_bool or enemylist[0].die  or enemylist3[0].die:  # 绿色和灰色
                enemylist[0].draw(screen)
                enemylist3[0].draw(screen)
                player.draw(screen)


        elif len(enemylist2) and len(enemylist3): #粉色和灰色


            if  player.y+player.height &lt; enemylist2[0].y+enemylist2[0].height &lt; enemylist3[0].y+enemylist3[0].height  and not player.jump and not enemylist2[0].die  and not enemylist3[0].die:
                player.draw(screen)
                enemylist2[0].draw(screen)
                enemylist3[0].draw(screen)


            elif enemylist2[0].y+enemylist2[0].height &lt; player.y+player.height &lt; enemylist3[0].y+enemylist3[0].height  and not player.jump and not enemylist2[0].die  and not enemylist3[0].die:


                enemylist2[0].draw(screen)
                player.draw(screen)
                enemylist3[0].draw(screen)


            elif enemylist2[0].y + enemylist2[0].height &lt; enemylist3[0].y + enemylist3[0].height &lt; player.y + player.height and not player.jump and not enemylist2[0].die  and not enemylist3[0].die:


                enemylist2[0].draw(screen)
                enemylist3[0].draw(screen)
                player.draw(screen)
            elif player.jump :
                player.draw(screen)
                enemylist2[0].draw(screen)
                enemylist3[0].draw(screen)
            # 敌人受攻击时 先后绘制
            elif enemylist3[0].life_remove_bool or enemylist3[0].die:  # 粉色
                enemylist2[0].draw(screen)
                enemylist3[0].draw(screen)
                player.draw(screen)
            elif enemylist2[0].life_remove_bool or enemylist2[0].die:  # 灰色
                enemylist2[0].draw(screen)
                enemylist3[0].draw(screen)
                player.draw(screen)
            elif enemylist[0].life_remove_bool and enemylist2[0].life_remove_bool or enemylist2[0].die or enemylist3[0].die:  # 绿色和灰色
                enemylist2[0].draw(screen)
                enemylist3[0].draw(screen)
                player.draw(screen)


        elif len(enemylist): #绿色
            if player.y + player.height &lt; enemylist[0].y + enemylist[0].height and not player.jump and not enemylist[0].die :
                player.draw(screen)
                enemylist[0].draw(screen)
            else:
                enemylist[0].draw(screen)
                player.draw(screen)
        elif len(enemylist2): #灰色
            if player.y + player.height &lt; enemylist2[0].y + enemylist2[0].height and not player.jump and not enemylist2[0].die:
                player.draw(screen)
                enemylist2[0].draw(screen)
            else:
                enemylist2[0].draw(screen)
                player.draw(screen)
        elif len(enemylist3): #灰色
            if player.y + player.height &lt; enemylist3[0].y + enemylist3[0].height and not player.jump and not enemylist3[0].die:
                player.draw(screen)
                enemylist3[0].draw(screen)
            else:
                enemylist3[0].draw(screen)
                player.draw(screen)


        if len(enemylist)+ len(enemylist2) +len(enemylist4)+ len(enemylist3)==0 and check==1 and player.kill_enemy&lt;3:
            print(check)
            enemylist.append(green)
            enemylist2.append(grey)
            enemylist3.append(pink)
            player.draw(screen)
            # enemylist4.append(boss)
        elif len(enemylist)+ len(enemylist2) +len(enemylist4)+ len(enemylist3)==0 and check==2 and player.kill_enemy&lt;6:
            print(check)
            enemylist.append(green)
            enemylist2.append(grey)
            enemylist3.append(pink)
            player.draw(screen)
            # enemylist4.append(boss)
        elif len(enemylist)+ len(enemylist2) +len(enemylist4)+ len(enemylist3)==0 and check==3 and player.kill_enemy&lt;7:
            print(check)
            # enemylist.append(green)
            # enemylist2.append(grey)
            # enemylist3.append(pink)
            enemylist4.append(boss)
            player.draw(screen)
        elif len(enemylist) + len(enemylist2) +len(enemylist4) + len(enemylist3) == 0 and  player.kill_enemy==7 and check==3:
            player.draw(screen)
            Check_fun.draw(screen)#箭头 -- 动态
            check_music.play()
        elif len(enemylist) + len(enemylist2) +len(enemylist4) + len(enemylist3) == 0 and  player.kill_enemy==6 and check==2:
            player.draw(screen)
            Check_fun.draw(screen)#箭头 -- 动态
            check_music.play()
        elif len(enemylist) + len(enemylist2) +len(enemylist4) + len(enemylist3) == 0 and  player.kill_enemy==3 and check==1:
            player.draw(screen)
            Check_fun.draw(screen)#箭头 -- 动态
            check_music.play()


        if len(enemylist4) and  len(enemylist) + len(enemylist2) + len(enemylist3) &gt;0:
            enemylist4[0].draw(screen)
        elif len(enemylist4) and  len(enemylist) + len(enemylist2) + len(enemylist3) == 0:
            player.draw(screen)
            enemylist4[0].draw(screen)


        jn = pygame.image.load("./cd/Equipmentbarl.png")
        screen.blit(jn, (200, 565))
        if player.cd and player.i:
            screen.blit(player.cd_tuple[player.cd_count], (210, 575))
            player.cd_count += 1
        elif player.cd and player.flc:
            screen.blit(player.cd_tuple[player.cd_count], (280, 575))
            player.cd_count += 1
        elif player.cd and player.attack_Bool:
            screen.blit(player.cd_tuple[player.cd_count], (350, 575))
            player.cd_count += 1
        elif player.cd and player.all:
            screen.blit(player.cd_tuple[player.cd_count], (420, 575))
            player.cd_count += 1




        LEVEL = font.render("LEVEL : " + str(player.level), True, (60, 200, 200))
        screen.blit(LEVEL, (210, 530))
        # 绘制血条
        screen.blit(player.player_img, (10, 520))
        pygame.draw.rect(screen, (72, 32, 38), (200, 650, 750, 35))
        pygame.draw.rect(screen, (230, 65, 92), (200, 650, (750 / 100) * player.life, 35))


        FRAM_PER_SECONDS = 16


    elif load_count&lt;=28:
        screen.blit(load_image[load_count],(load_img_x,load_img_y))
        load_count+=1


def game_load():
    # load_music.play()
    global game_start
    global game_end
    screen.blit(start_back, (0, 0))
    game_start=pygame.image.load("./load_img/开始游戏1.png")
    game_end=pygame.image.load("./load_img/退出游戏2.png")


    screen.blit(game_start, (446,300))
    screen.blit(game_end,(446,500))
    if start_flag==True:
        screen.fill((16,16,16))
        draw_img()


def start_button():
    global start_flag
    global pause
    for event in pygame.event.get():
        if load_animate == True:
            pass
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if start_flag == False and (406 &lt;= pygame.mouse.get_pos()[0] &lt;= 406 + game_start.get_width()) and (300 &lt;= pygame.mouse.get_pos()[1] &lt;= 300 + game_start.get_height()):
                start_flag=True
                start_music.stop()  # 游戏开始音效
                load_music.play(-1)


            if start_flag == False and (406 &lt;= pygame.mouse.get_pos()[0] &lt;= 406 + game_end.get_width()) and (500 &lt;= pygame.mouse.get_pos()[1] &lt;= 500 + game_end.get_height()):
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (10 &lt;= event.pos[0] &lt;= 10 + 121) and (10 &lt;= event.pos[1] &lt;= 10 + 95) and pause == False:
                pause = True
                paused()


#拾取血包
def collision_check_tanke_HP(a,b):
    temp1= (b.x+b.width&gt;a.x+a.width-30&gt;b.x)
    #角色的攻击区间  容错区间
    temp2= (-40&lt;(b.y+b.height)-(a.y+a.height)&lt;=45)
    return temp1 and  temp2




#敌人技能  近程技能
def collision_check_tanke_yellow(a,b):
    temp1= (b.x+b.width&gt;a.x+a.width+210&gt;b.x)
    #角色的攻击区间  容错区间
    temp2= (-40&lt;(b.y+b.height)-(a.y+a.height)&lt;=45)
    return temp1 and  temp2


#敌人技能  近程技能
def collision_check_tanke_jincheng(a,b):
    temp1= (b.x+b.width&gt;a.x+a.width+50&gt;b.x)
    #角色的攻击区间  容错区间
    temp2= (-40&lt;(b.y+b.height)-(a.y+a.height)&lt;=45)
    return temp1 and  temp2


#绿色敌人技能  近程技能
def collision_check_tanke_green(a,b):
    temp1= (b.x+b.width&gt;a.x+a.width+150&gt;b.x)
    #角色的攻击区间  容错区间
    temp2= (-40&lt;(b.y+b.height)-(a.y+a.height)&lt;=45)
    return temp1 and  temp2


#敌人技能  远攻技能
def collision_check_tanke(a,b):
    temp1= (b.x+b.width&gt;a.x+a.width+170&gt;b.x)
    #角色的攻击区间  容错区间
    temp2= (-40&lt;(b.y+b.height)-(a.y+a.height)&lt;=45)
    return temp1 and  temp2


#敌人 遇我 进行反向
def collision_check_fanxiang(a,b):
    temp1= (b.x+b.width&gt;=a.x+a.width&gt;=b.x)
    #角色的攻击区间  容错区间
    temp2= (-19&lt;(b.y+b.height)-(a.y+a.height)&lt;=35)
    return temp1 and  temp2


#基本技能 碰撞检测 类
def collision_check(a,b):
    temp1= (b.x+b.width&gt;a.x+a.width+150&gt;b.x)
    #角色的攻击区间  容错区间
    temp2= (-60&lt;(b.y+b.height)-(a.y+a.height)&lt;=60)
    return temp1 and  temp2
#机甲飞踢 碰撞检测 类
def collision_check_foot(a,b):
    temp1= (b.x+b.width&gt;a.x+a.width+150&gt;b.x)
    #角色的攻击区间  容错区间
    temp2= (-60&lt;(b.y+b.height)-(a.y+a.height)&lt;=60)
    return temp1 and  temp2


#碰撞检测函数
def collision_check_HP(a,b):
    temp1 = (b.x&lt;=a.x+a.width&lt;=b.x+b.width)
    temp2 = (b.y&lt;=a.y+a.height&lt;=b.y+b.height)
    return temp1 and temp2


#all 技能
def U_Testing(enemy_obj):
    if len(enemy_obj):
        if  not enemy_obj[0].die:
            enemy_obj[0].x+=100
            enemy_obj[0].life -= 3
            enemy_obj[0].life_remove_bool = True
            enemy_obj[0].walk = False
            enemy_obj[0].skill = False
            enemy_obj[0].attack = False
            enemy_obj[0].x += 20
            if enemy_obj[0].life &lt;= 0:
                enemy_obj[0].life_remove_bool = False
                enemy_obj[0].die = True
                enemy_obj[0].walk = False




#三段普攻
def J_Testing(enemy_obj):
    if len(enemy_obj):
        if collision_check(player, enemy_obj[0]) and not enemy_obj[0].die:
            enemy_obj[0].life -= 3
            enemy_obj[0].life_remove_bool = True
            enemy_obj[0].walk = False
            enemy_obj[0].skill = False
            enemy_obj[0].attack = False
            enemy_obj[0].x += 20


            if enemy_obj[0].life &lt;= 0:




                enemy_obj[0].life_remove_bool = False
                enemy_obj[0].die = True
                enemy_obj[0].walk = False


#跳跃检测
def Jump_Testing(enemy_obj):
    if len(enemy_obj):
        if enemy_obj[0].x + enemy_obj[0].width &gt; player.x &gt; enemy_obj[0].x and player.y + player.height &gt; enemy_obj[0].y + enemy_obj[0].height - 40 and player.y + player.height &lt; enemy_obj[0].y + enemy_obj[0].height + 40:
            player.x = enemy_obj[0].width + enemy_obj[0].x + 15
            player.right = True  # 设置进行禁止穿模 位移到两侧
            # player.walk=True
        if player.x &lt; enemy_obj[0].x &lt; player.x + player.width and player.y + player.height &gt; enemy_obj[0].y + enemy_obj[0].height - 40 and player.y + player.height &lt; enemy_obj[0].y + enemy_obj[0].height + 40:
            player.x = enemy_obj[0].x - player.width - 15
            player.left = True  # 设置进行禁止穿模 位移到两侧
            # player.walk=True
#I技能检测
def I_Testing(enemy_obj):
    if len(enemy_obj):
        enemy_obj[0].Enemy_Y = enemy_obj[0].y
        if collision_check(player, enemy_obj[0]):
            enemy_obj[0].Enemy_Y = enemy_obj[0].y
            enemy_obj[0].life_remove_bool = True
            enemy_obj[0].y = player.y + player.height - enemy_obj[0].height - 100
            enemy_obj[0].skill = False
            enemy_obj[0].attack = False
            enemy_obj[0].walk = False
            enemy_obj[0].life -= 4
            enemy_obj[0].x += 20
            if enemy_obj[0].life &lt;= 0:




                enemy_obj[0].life_remove_bool = False
                enemy_obj[0].die = True
                enemy_obj[0].walk = False
        return enemy_obj




#暂停
def unpause():
    global pause
    back_music.set_volume(0.06)
    pause=False


#设置
def paused():
    global flag
    global check
    global pause
    zanting=pygame.image.load("./load_img/返回游戏.png")         #图片按钮
    quit_img=pygame.image.load("./load_img/退出游戏.png")        #图片按钮
    restart_img = pygame.image.load("./load_img/重新开始.png")   #图片按钮
    logo_img=pygame.image.load("./load_img/logo.png")            #图片按钮
    screen.blit(zanting, (185,190))
    screen.blit(restart_img, (185, 280))
    screen.blit(quit_img, (185, 370))
    screen.blit(logo_img,(595,150))
    back_music.set_volume(0)                                      #背景音乐暂停
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # quit()
            if load_count&gt;=29 and pause==True:
                if event.type == pygame.MOUSEBUTTONDOWN :                #继续游戏-- 点击屏幕 MENU 按钮 第一种继续游戏
                    if (10 &lt;= event.pos[0] &lt;= 10 + set_img.get_width()) and (10 &lt;= event.pos[1] &lt;= 10 + set_img.get_height()):
                        unpause()
                if event.type == pygame.MOUSEBUTTONDOWN:                #继续游戏-- 点击屏幕 继续游戏 菜单 第二种继续游戏
                    if (185 &lt;= event.pos[0] &lt;= 185 + zanting.get_width()) and (190 &lt;= event.pos[1] &lt;= 190 + zanting.get_height()):
                        unpause()
                if event.type == pygame.MOUSEBUTTONDOWN:                #退出游戏--按钮
                    if (185 &lt;= event.pos[0] &lt;= 185 + zanting.get_width()) and (370 &lt;= event.pos[1] &lt;= 370 + zanting.get_height()):
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:                #重新开始--按钮
                    if (185 &lt;= event.pos[0] &lt;= 185 + zanting.get_width()) and (280 &lt;= event.pos[1] &lt;= 280 + zanting.get_height()):
                        check=5
                        unpause()


        pygame.display.update()


y=100
HP_bool_green=False
HP_bool_grey=False
HP_bool_pink=False
def start():
    global load_animate
    global check
    global map_img
    global enemylist
    global enemylist2
    global enemylist3
    global enemylist4
    global HP_bool_green
    global HP_bool_grey
    global HP_bool_pink
    global player
    global Check_fun
    global green
    global grey
    global boss
    global pause
    global pink
    global keys
    enemylist = []
    enemylist2 = []
    enemylist3 = []
    enemylist4 = []
    player = Player(160, 410, 100, 100)


    Check_fun = check_fun()
    green = Enemy(random.randint(500, WIDTH - 133), 420, 500, WIDTH - 153)
    grey = Enemy_grey(random.randint(500, WIDTH - 133), 430, 500, WIDTH - 203)
    pink = Enemy_pink(random.randint(500, WIDTH - 133), 440, 500, WIDTH - 401)
    boss = Boss(random.randint(500, WIDTH - 133), 440, 500, WIDTH -400)
    enemylist.append(green)
    enemylist2.append(grey)
    enemylist3.append(pink)
    # enemylist4.append(boss)


    while True:
        clock.tick(FRAM_PER_SECONDS)  #可以说是循环执行的次数  #我认为只是设置游戏运行的速度，或者设置while循环更新自身、运行自身的频率
        game_load()
        start_button()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


            if event.type == pygame.MOUSEBUTTONDOWN:
                if load_animate:
                    load_animate=False
                    screen.fill((16,16,16))


        keys = pygame.key.get_pressed()  # 获取所有键盘事件


        if  pause==False and start_flag:
            if keys[pygame.K_ESCAPE]:
                pause=True
                paused()


        if player.life&lt;=0:
            player.die=True
            if player.die_count&gt;=64:
                player.die=False
                return ""


        #全局速度
        if keys[pygame.K_LSHIFT] :
            player.speed = 4
            if keys[pygame.K_LSHIFT] and pygame.key.get_mods() &amp; keys[pygame.K_k]:
                player.speed=6
        else:
            if  len(enemylist)+ len(enemylist2) +len(enemylist3) +len(enemylist4) ==4:


                player.speed = 1
            elif  len(enemylist)+ len(enemylist2) +len(enemylist3) +len(enemylist4) ==3:


                player.speed = 3
            elif len(enemylist) + len(enemylist2) + len(enemylist3) +len(enemylist4) == 2:


                player.speed = 5
            elif len(enemylist) + len(enemylist2) + len(enemylist3) +len(enemylist4) == 1:
                player.speed = 10
            else:
                player.speed = 15




        # 敌人绿色  穿模设置


        if len(enemylist) and  keys[pygame.K_d]  and player.x &lt; WIDTH-player.height :
            # D 键走动  禁止与敌人穿模
           #当敌人死亡时 直线行走
            if keys[pygame.K_d] and player.x &lt; WIDTH and not player.attack_Bool  and enemylist[0].die :
                player.x += player.speed
                player.right = True
                player.stand = False
            # 当与敌人不在一个 视觉水平时 直线行走
            elif keys[pygame.K_d] and ((player.y+player.height&lt;=enemylist[0].y+enemylist[0].height-40) or (player.y+player.height&gt;=enemylist[0].y+enemylist[0].height+20 )):
                player.x+=player.speed
                player.right = True
                player.stand = False
                # player.jump = False
            # 设置行走区间 敌人起点是终点 动态区间
            elif not enemylist[0].die and keys[pygame.K_d] and (player.x+player.width &lt;= enemylist[0].x-10 or player.x&gt;=enemylist[0].x+enemylist[0].width):
                player.x+=player.speed
                player.right = True
                player.stand = False
            # 设置行走区间与敌人接触时 将机甲 停止
            elif not enemylist[0].die and keys[pygame.K_d] and player.x+player.width &gt; enemylist[0].x :
                player.stand=True
                player.left=False
                player.right=True
        #左键
        if len(enemylist) and keys[pygame.K_a] and player.x &gt;0:
            # 当敌人死亡时 直线行走
            if keys[pygame.K_a] and player.x &gt; 0  and not player.attack_Bool and enemylist[0].die:
                player.x -= player.speed
                player.left = True
                player.stand = False
            # 当与敌人不在一个 视觉水平时 直线行走
            elif keys[pygame.K_a] and (player.y + player.height &lt;= enemylist[0].y + enemylist[0].height - 40 or player.y + player.height &gt;= enemylist[0].y + enemylist[0].height + 20):
                player.x -= player.speed
                player.left = True
                player.stand = False
            # 设置行走区间 敌人起点是终点 动态区间
            elif not enemylist[0].die and keys[pygame.K_a] and (( player.x &gt;= enemylist[0].x+enemylist[0].width+10) or (player.x+player.width &lt;enemylist[0].x)):
                player.x -= player.speed
                player.left = True
                player.stand = False
            # 设置行走区间与敌人接触时 将机甲 停止
            elif not enemylist[0].die and keys[pygame.K_a] and player.x &lt; enemylist[0].x+enemylist[0].width :
                player.stand = True
                player.left = True
                player.right = False
        #w 键 上 禁止穿模
        if len(enemylist) and keys[pygame.K_w] and player.y+player.height &gt;390 and not player.jump  and not player.i:
            # 当敌人死亡时 直线行走
            if keys[pygame.K_w] and player.y &gt; 390  and not player.attack_Bool and not player.jump and enemylist[0].die:
                player.y -= player.speed
                player.left = True
                player.stand = False
            # 当与敌人不在一个 视觉水平时 直线行走
            elif keys[pygame.K_w] and ((player.x + player.width &lt; enemylist[0].x) or (player.x  &gt; enemylist[0].x + enemylist[0].width )):
                player.y -= player.speed
                player.left = True
                player.stand = False
            # 设置行走区间 敌人起点是终点 动态区间
            elif not enemylist[0].die and keys[pygame.K_w] and ( player.y+player.height &gt;= enemylist[0].y+enemylist[0].height+20 or player.y+player.height &lt;= enemylist[0].y+enemylist[0].height-40):
                player.y -= player.speed
                player.left = True
                player.stand = False
                if player.y+player.height&gt;enemylist[0].y+enemylist[0].height and  player.y+player.height-enemylist[0].y-enemylist[0].height&lt;20:
                    player.y=enemylist[0].y+enemylist[0].height+20-player.height
            # 设置行走区间与敌人接触时 将机甲 停止
            elif not enemylist[0].die and keys[pygame.K_w] and player.y+player.height &lt; enemylist[0].y+enemylist[0].height+20  and  player.y+player.height &gt; enemylist[0].y+enemylist[0].height-40 :
                player.y = enemylist[0].y + enemylist[0].height+20-player.height
                if player.y&gt;640:
                    player.y=640
                player.stand=True
                player.right=False
                player.left=True
        # s 键 上 禁止穿模
        if len(enemylist) and keys[pygame.K_s] and player.y + player.height &lt; 640 and not player.jump  and not player.i:
            # 当敌人死亡时 直线行走
            if keys[pygame.K_s] and player.y &lt; 640 and not player.attack_Bool and not player.jump and enemylist[0].die:
                player.y += player.speed
                player.right = True
                player.stand = False
            # 当与敌人不在一个 视觉水平时 直线行走
            elif keys[pygame.K_s] and ((player.x + player.width &lt; enemylist[0].x) or (player.x &gt; enemylist[0].x + enemylist[0].width)):
                player.y += player.speed
                player.right = True
                player.stand = False
            # 设置行走区间 敌人起点是终点 动态区间
            elif not enemylist[0].die and keys[pygame.K_s] and (player.y + player.height &gt;= enemylist[0].y + enemylist[0].height + 20 or player.y + player.height &lt;=enemylist[0].y + enemylist[0].height - 40):
                player.y += player.speed
                player.right = True
                player.stand = False
                if player.y+player.height&lt;enemylist[0].y+enemylist[0].height and player.y + player.height - enemylist[0].y - enemylist[0].height &gt; -40:
                    player.y = enemylist[0].y + enemylist[0].height -40 - player.height
            # 设置行走区间与敌人接触时 将机甲 停止
            elif not enemylist[0].die and keys[pygame.K_s] and player.y + player.height &gt; enemylist[0].y + enemylist[0].height - 40 and  player.y + player.height &lt; enemylist[0].y + enemylist[0].height + 20  :
                player.y = enemylist[0].y + enemylist[0].height-40-player.height
                if player.y&lt;390:
                    player.y=390
                player.left = False
                player.right = True
                player.stand = True




        # 敌人灰色  穿模设置


        if len(enemylist2) and keys[pygame.K_d] and player.x &lt; WIDTH - player.height:
            # D 键走动  禁止与敌人穿模
            # 当敌人死亡时 直线行走
            if keys[pygame.K_d] and player.x &lt; WIDTH and not player.attack_Bool and enemylist2[0].die:
                player.x += player.speed
                player.right = True
                player.stand = False
            # 当与敌人不在一个 视觉水平时 直线行走
            elif keys[pygame.K_d] and ((player.y + player.height &lt;= enemylist2[0].y + enemylist2[0].height - 40) or (player.y + player.height &gt;= enemylist2[0].y + enemylist2[0].height + 20)):
                player.x += player.speed
                player.right = True
                player.stand = False
                # player.jump = False
            # 设置行走区间 敌人起点是终点 动态区间
            elif not enemylist2[0].die and keys[pygame.K_d] and (player.x + player.width &lt;= enemylist2[0].x - 10 or player.x &gt;= enemylist2[0].x + enemylist2[0].width):
                player.x += player.speed
                player.right = True
                player.stand = False
            # 设置行走区间与敌人接触时 将机甲 停止
            elif not enemylist2[0].die and keys[pygame.K_d] and player.x + player.width &gt; enemylist2[0].x:
                player.stand = True
                player.left = False
                player.right = True
        # 左键
        if len(enemylist2) and keys[pygame.K_a] and player.x &gt; 0:
            # 当敌人死亡时 直线行走
            if keys[pygame.K_a] and player.x &gt; 0 and not player.attack_Bool and enemylist2[0].die:
                player.x -= player.speed
                player.left = True
                player.stand = False
            # 当与敌人不在一个 视觉水平时 直线行走
            elif keys[pygame.K_a] and (player.y + player.height &lt;= enemylist2[0].y + enemylist2[0].height - 40 or player.y + player.height &gt;= enemylist2[0].y + enemylist2[0].height + 20):
                player.x -= player.speed
                player.left = True
                player.stand = False
            # 设置行走区间 敌人起点是终点 动态区间
            elif not enemylist2[0].die and keys[pygame.K_a] and ((player.x &gt;= enemylist2[0].x + enemylist2[0].width + 10) or (player.x + player.width &lt; enemylist2[0].x)):
                player.x -= player.speed
                player.left = True
                player.stand = False
            # 设置行走区间与敌人接触时 将机甲 停止
            elif not enemylist2[0].die and keys[pygame.K_a] and player.x &lt; enemylist2[0].x + enemylist2[0].width:
                player.stand = True
                player.left = True
                player.right = False
        # w 键 上 禁止穿模
        if len(enemylist2) and keys[pygame.K_w] and player.y + player.height &gt; 390 and not player.jump and not player.i:
            # 当敌人死亡时 直线行走
            if keys[pygame.K_w] and player.y &gt; 390 and not player.attack_Bool and not player.jump and enemylist2[0].die:
                player.y -= player.speed
                player.left = True
                player.stand = False
            # 当与敌人不在一个 视觉水平时 直线行走
            elif keys[pygame.K_w] and ((player.x + player.width &lt; enemylist2[0].x) or (player.x &gt; enemylist2[0].x + enemylist2[0].width)):
                player.y -= player.speed
                player.left = True
                player.stand = False
            # 设置行走区间 敌人起点是终点 动态区间
            elif not enemylist2[0].die and keys[pygame.K_w] and (player.y + player.height &gt;= enemylist2[0].y + enemylist2[0].height + 20 or player.y + player.height &lt;= enemylist2[0].y + enemylist2[0].height - 40):
                player.y -= player.speed
                player.left = True
                player.stand = False
                if player.y + player.height &gt; enemylist2[0].y + enemylist2[0].height and player.y + player.height - enemylist2[0].y - enemylist2[0].height &lt; 20:
                    player.y = enemylist2[0].y + enemylist2[0].height + 20 - player.height
            # 设置行走区间与敌人接触时 将机甲 停止
            elif not enemylist2[0].die and keys[pygame.K_w] and player.y + player.height &lt; enemylist2[0].y + enemylist2[0].height + 20 and player.y + player.height &gt; enemylist2[0].y + enemylist2[0].height - 40:
                player.y = enemylist2[0].y + enemylist2[0].height + 20 - player.height
                if player.y &gt; 640:
                    player.y = 640
                player.stand = True
                player.right = False
                player.left = True
        # s 键 上 禁止穿模
        if len(enemylist2) and keys[pygame.K_s] and player.y + player.height &lt; 640 and not player.jump and not player.i:
            # 当敌人死亡时 直线行走
            if keys[pygame.K_s] and player.y &lt; 640 and not player.attack_Bool and not player.jump and enemylist2[0].die:
                player.y += player.speed
                player.right = True
                player.stand = False
            # 当与敌人不在一个 视觉水平时 直线行走
            elif keys[pygame.K_s] and ((player.x + player.width &lt; enemylist2[0].x) or (player.x &gt; enemylist2[0].x + enemylist2[0].width)):
                player.y += player.speed
                player.right = True
                player.stand = False
            # 设置行走区间 敌人起点是终点 动态区间
            elif not enemylist2[0].die and keys[pygame.K_s] and (player.y + player.height &gt;= enemylist2[0].y + enemylist2[0].height + 20 or player.y + player.height &lt;= enemylist2[0].y + enemylist2[0].height - 40):
                player.y += player.speed
                player.right = True
                player.stand = False
                if player.y + player.height &lt; enemylist2[0].y + enemylist2[0].height and player.y + player.height - enemylist2[0].y - enemylist2[0].height &gt; -40:
                    player.y = enemylist2[0].y + enemylist2[0].height - 40 - player.height
            # 设置行走区间与敌人接触时 将机甲 停止
            elif not enemylist2[0].die and keys[pygame.K_s] and player.y + player.height &gt; enemylist2[0].y + enemylist2[0].height - 40 and player.y + player.height &lt; enemylist2[0].y + enemylist2[0].height + 20:
                player.y = enemylist2[0].y + enemylist2[0].height - 40 - player.height
                if player.y &lt; 390:
                    player.y = 390
                player.left = False
                player.right = True
                player.stand = True


        # 敌人灰色  穿模设置


        if len(enemylist3) and keys[pygame.K_d] and player.x &lt; WIDTH - player.height:
            # D 键走动  禁止与敌人穿模
            # 当敌人死亡时 直线行走
            if keys[pygame.K_d] and player.x &lt; WIDTH and not player.attack_Bool and enemylist3[0].die:
                player.x += player.speed
                player.right = True
                player.stand = False
            # 当与敌人不在一个 视觉水平时 直线行走
            elif keys[pygame.K_d] and ((player.y + player.height &lt;= enemylist3[0].y + enemylist3[0].height - 40) or (player.y + player.height &gt;= enemylist3[0].y + enemylist3[0].height + 20)):
                player.x += player.speed
                player.right = True
                player.stand = False
                # player.jump = False
            # 设置行走区间 敌人起点是终点 动态区间
            elif not enemylist3[0].die and keys[pygame.K_d] and (player.x + player.width &lt;= enemylist3[0].x - 10 or player.x &gt;= enemylist3[0].x + enemylist3[0].width):
                player.x += player.speed
                player.right = True
                player.stand = False
            # 设置行走区间与敌人接触时 将机甲 停止
            elif not enemylist3[0].die and keys[pygame.K_d] and player.x + player.width &gt; enemylist3[0].x:
                player.stand = True
                player.left = False
                player.right = True
        # 左键
        if len(enemylist3) and keys[pygame.K_a] and player.x &gt; 0:
            # 当敌人死亡时 直线行走
            if keys[pygame.K_a] and player.x &gt; 0 and not player.attack_Bool and enemylist3[0].die:
                player.x -= player.speed
                player.left = True
                player.stand = False
            # 当与敌人不在一个 视觉水平时 直线行走
            elif keys[pygame.K_a] and (player.y + player.height &lt;= enemylist3[0].y + enemylist3[0].height - 40 or player.y + player.height &gt;= enemylist3[0].y + enemylist3[0].height + 20):
                player.x -= player.speed
                player.left = True
                player.stand = False
            # 设置行走区间 敌人起点是终点 动态区间
            elif not enemylist3[0].die and keys[pygame.K_a] and ((player.x &gt;= enemylist3[0].x + enemylist3[0].width + 10) or (player.x + player.width &lt; enemylist3[0].x)):
                player.x -= player.speed
                player.left = True
                player.stand = False
            # 设置行走区间与敌人接触时 将机甲 停止
            elif not enemylist3[0].die and keys[pygame.K_a] and player.x &lt; enemylist3[0].x + enemylist3[0].width:
                player.stand = True
                player.left = True
                player.right = False
        # w 键 上 禁止穿模
        if len(enemylist3) and keys[pygame.K_w] and player.y + player.height &gt; 390 and not player.jump and not player.i:
            # 当敌人死亡时 直线行走
            if keys[pygame.K_w] and player.y &gt; 390 and not player.attack_Bool and not player.jump and enemylist3[0].die:
                player.y -= player.speed
                player.left = True
                player.stand = False
            # 当与敌人不在一个 视觉水平时 直线行走
            elif keys[pygame.K_w] and ((player.x + player.width &lt; enemylist3[0].x) or (player.x &gt; enemylist3[0].x + enemylist3[0].width)):
                player.y -= player.speed
                player.left = True
                player.stand = False
            # 设置行走区间 敌人起点是终点 动态区间
            elif not enemylist3[0].die and keys[pygame.K_w] and (player.y + player.height &gt;= enemylist3[0].y + enemylist3[0].height + 20 or player.y + player.height &lt;= enemylist3[0].y + enemylist3[0].height - 40):
                player.y -= player.speed
                player.left = True
                player.stand = False
                if player.y + player.height &gt; enemylist3[0].y + enemylist3[0].height and player.y + player.height - enemylist3[0].y - enemylist3[0].height &lt; 20:
                    player.y = enemylist3[0].y + enemylist3[0].height + 20 - player.height
            # 设置行走区间与敌人接触时 将机甲 停止
            elif not enemylist3[0].die and keys[pygame.K_w] and player.y + player.height &lt; enemylist3[0].y + enemylist3[0].height + 20 and player.y + player.height &gt; enemylist3[0].y + enemylist3[0].height - 40:
                player.y = enemylist3[0].y + enemylist3[0].height + 20 - player.height
                if player.y &gt; 640:
                    player.y = 640
                player.stand = True
                player.right = False
                player.left = True
        # s 键 上 禁止穿模
        if len(enemylist3) and keys[pygame.K_s] and player.y + player.height &lt; 640 and not player.jump and not player.i:
            # 当敌人死亡时 直线行走
            if keys[pygame.K_s] and player.y &lt; 640 and not player.attack_Bool and not player.jump and enemylist3[0].die:
                player.y += player.speed
                player.right = True
                player.stand = False
            # 当与敌人不在一个 视觉水平时 直线行走
            elif keys[pygame.K_s] and ((player.x + player.width &lt; enemylist3[0].x) or (player.x &gt; enemylist3[0].x + enemylist3[0].width)):
                player.y += player.speed
                player.right = True
                player.stand = False
            # 设置行走区间 敌人起点是终点 动态区间
            elif not enemylist3[0].die and keys[pygame.K_s] and (player.y + player.height &gt;= enemylist3[0].y + enemylist3[0].height + 20 or player.y + player.height &lt;= enemylist3[0].y + enemylist3[0].height - 40):
                player.y += player.speed
                player.right = True
                player.stand = False
                if player.y + player.height &lt; enemylist3[0].y + enemylist3[0].height and player.y + player.height - enemylist3[0].y - enemylist3[0].height &gt; -40:
                    player.y = enemylist3[0].y + enemylist3[0].height - 40 - player.height
            # 设置行走区间与敌人接触时 将机甲 停止
            elif not enemylist3[0].die and keys[pygame.K_s] and player.y + player.height &gt; enemylist3[0].y + enemylist3[0].height - 40 and player.y + player.height &lt; enemylist3[0].y + enemylist3[0].height + 20:
                player.y = enemylist3[0].y + enemylist3[0].height - 40 - player.height
                if player.y &lt; 390:
                    player.y = 390
                player.left = False
                player.right = True
                player.stand = True


        #切换地图  关卡结束
        if keys[pygame.K_d]  and player.x &gt; WIDTH-player.width and len(enemylist)+ len(enemylist2)+ len(enemylist3) + len(enemylist4)==0  and check==3:
            check+=1
            HP_bool_green=False
            HP_bool_grey=False
            HP_bool_pink=False
        # 切换 游戏第三场景
        elif keys[pygame.K_d] and player.x &gt; WIDTH-player.width and len(enemylist)+ len(enemylist2)+ len(enemylist3) + len(enemylist4)==0  and check==2:
            HP_bool_green = False
            HP_bool_grey = False
            HP_bool_pink = False
            player.x = 0
            map_img=pygame.image.load("map_img/right.jpg")
            check+= 1
        #切换 游戏第二场景
        elif keys[pygame.K_d] and player.x &gt; WIDTH-player.width and len(enemylist)+ len(enemylist2)+ len(enemylist3) + len(enemylist4)==0  and check==1:
            HP_bool_green = False
            HP_bool_grey = False
            HP_bool_pink = False
            player.x = 0
            map_img=pygame.image.load("map_img/center.jpg")
            check+=1
        elif check==1 and player.kill_enemy==0:
            HP_bool_green = False
            HP_bool_grey = False
            HP_bool_pink = False
            map_img=pygame.image.load("map_img/left.jpg")
            #游戏 结束  选择重新开始 和退出
        if check==4:
            return ""
        if check==5:
            return ""


        if len(enemylist)+ len(enemylist2) +len(enemylist3) +len(enemylist4) &lt;4:
            if keys[pygame.K_d] and player.x &lt; WIDTH  and player.x &gt; -20:
                player.x+=player.speed
                player.left=False
                player.right = True
                player.stand = False
                # player.jump = False


            if keys[pygame.K_a] and player.x &lt; WIDTH  and player.x &gt; 0:
                player.x -= player.speed
                player.left = True
                player.right = False
                player.stand = False
                # player.jump = False
            if keys[pygame.K_w] and player.y+player.height &gt;390  and not player.jump:
                player.y-=player.speed
                player.left = True
                player.right = False
                player.stand = False
                # player.jump = False
            if keys[pygame.K_s] and player.y + player.height &lt; 640  and not player.jump:
                player.y+=player.speed
                player.left = True
                player.right = False
                player.stand = False
                player.jump = False


        if not keys[pygame.K_d] and  not keys[pygame.K_w] and  not keys[pygame.K_s] and  not keys[pygame.K_a] :
            walk_music.stop()
            player.stand=True


        #三段普攻
        if keys[pygame.K_j]   and not player.attack_Bool and not player.life_remove_bool:
            player.cd = True
            J_Testing(enemylist)
            J_Testing(enemylist2)
            J_Testing(enemylist3)
            J_Testing(enemylist4)
            player.stand = False
            player.attack_Bool = True
            player.attack += 1
            if player.attack &gt; 3:
                player.attack = 0
                player.attack_Bool = False
                player.stand = True


        if keys[pygame.K_u]:
            player.all=True
            player.cd = True




        #flc o 键技能
        if not player.flc and keys[pygame.K_o]   and not keys[pygame.K_w] and not keys[pygame.K_s] and not player.life_remove_bool:
            if keys[pygame.K_o] and not player.jump and not player.i :
                J_Testing(enemylist)
                J_Testing(enemylist2)
                J_Testing(enemylist3)
                J_Testing(enemylist4)
                player.cd = True
                player.flc=True
                player.stand = False
                player.attack_Bool = True
                player.attack += 1
                if player.attack &gt; 3:
                    player.attack = 0
                    player.attack_Bool = False
                    player.stand = True


        if not player.i  and not keys[pygame.K_w] and not keys[pygame.K_s]  :
            if keys[pygame.K_i] and not player.jump and  not player.flc and not player.life_remove_bool:
                player.cd=True
                global en1
                global en2
                global en3
                en1=I_Testing(enemylist)
                en2=I_Testing(enemylist2)
                en3=I_Testing(enemylist3)
                en4=I_Testing(enemylist4)




                player.i=True
                player.jn_count = 1
        elif player.i:
            if player.t&gt;=-10:#开始向上升
                a=1
                if player.t&lt;0:#向下落的时候
                    a=-1
                player.y-=0.5*a*(player.t**2)
                player.t-=1
            else:#落地后
                if len(enemylist):
                    en1[0].y = en1[0].Enemy_Y
                if len(enemylist2):
                    en2[0].y = en2[0].Enemy_Y
                if len(enemylist3):
                    en3[0].y = en3[0].Enemy_Y
                if len(enemylist4):
                    en4[0].y = en4[0].Enemy_Y


                player.i =False
                player.stand=True
                player.t=10
                player.jn_count=1




        if not player.jump:
            if keys[pygame.K_k] and not keys[pygame.K_w] and not keys[pygame.K_s]  and not player.i:
                player.jump=True#设置跳跃
        else:
            # 三段普攻
            if keys[pygame.K_j] and not player.attack_Bool and not player.life_remove_bool:
                player.cd = True
                J_Testing(enemylist)
                J_Testing(enemylist2)
                J_Testing(enemylist3)
                J_Testing(enemylist4)
                player.stand = False
                player.attack_Bool = True
                player.attack += 1
                if player.attack &gt; 3:
                    player.attack = 0
                    player.attack_Bool = False
                    player.stand = True
                player.stand = False
                player.attack_Bool = True
                player.attack += 1
                if player.attack &gt; 3:
                    player.attack = 0
                    player.attack_Bool = False
                    player.stand = True
            if player.t&gt;=-10:#开始向上升
                a=1
                if player.t&lt;0:#向下落的时候
                    a=-1
                player.y-=0.5*a*(player.t**2)
                player.t-=1
            else:#落地后
                player.jump = False
                player.t = 10
                player.jump_count = 1
                #跳跃检测
                Jump_Testing(enemylist)
                Jump_Testing(enemylist2)
                Jump_Testing(enemylist3)
                Jump_Testing(enemylist4)
        pygame.display.update()


    # 结束类 增加图片
def game_over():
    global check
    start_btn=pygame.image.load("./load_img/重新开始.png")
    end_btn=pygame.image.load("./load_img/退出游戏.png")
    failed=pygame.image.load("./load_img/失败.png")
    win_img=pygame.image.load("./load_img/胜利.png")
    bg=pygame.image.load("./map_img/right.jpg")
    back_music.stop()
    while True:
        if check==5:
            back_music.play(-1)
            player.life = 100
            player.x = 0
            player.kill_enemy = 0
            check = 1
            return True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                                    #鼠标事件
            if event.type==pygame.MOUSEBUTTONDOWN:
                            # 鼠标位置
                if (495&lt;=event.pos[0]&lt;=495+start_btn.get_width()) and (450&lt;=event.pos[1]&lt;450+start_btn.get_height()):
                    back_music.play(-1)
                    player.life = 100
                    player.x = 0
                    player.kill_enemy = 0
                    check = 1
                    return True
                if (495&lt;=event.pos[0]&lt;=495+start_btn.get_width()) and (320&lt;=event.pos[1]&lt;320+start_btn.get_height()):
                    sys.exit()
        player.kill_enemy=0
        screen.blit(bg,(0,0))
        screen.blit(start_btn,(495,450))
        screen.blit(end_btn,(495,320))
        if player.win_bool==False :   #失败
            screen.blit(failed, (395, 120))
        if player.win_bool :  #胜利
            screen.blit(win_img, (425, 120))
        pygame.display.update()


run=True
if __name__ == '__main__':
    flag=True
    while flag:
        game_result=start()
        if game_result=="":
            flag=game_over()

```

**<strong>图片素材以及源码下载**</strong>

****1.******** ******长按识别****下方二维码加我个人微信**

****2. ******备注机甲****免费获取**

<img src="https://img-blog.csdnimg.cn/img_convert/67bd9c35ebc4d486b113663f4ec38226.png">

```
长按????二维码+我个人微信

备注机甲获取

```
