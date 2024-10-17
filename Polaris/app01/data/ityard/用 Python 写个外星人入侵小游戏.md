
--- 
title:  用 Python 写个外星人入侵小游戏 
tags: []
categories: [] 

---
>  
  作者：weixin_wangyanpi  
  https://blog.csdn.net/weixin_44412311/article/details/106590762 
 

历时七天，终于做出来了（因为还要上网课，学习其他的东西，所以做的比较慢，如果每天能拿出五个小时做这个游戏的话，个人觉得三天差不多，当然了，这是对于小白来说）。我是按照买的资料书上来做的，在我代码里面呢，增加了一些资料上没有的功能，比如说外星人是随机产生的（资料书是创建整个外星人群），本来打算让每个外星人随机移动的，但是试了一下发现，外星人移动杂乱无章，然后后就采用了资料书上的做法，让它们作为整体移动；还有就是在射中外星人的时候，可能会产生暴击（emmm,其实是福利吧，bone，不是说伤害有暴击，这个“暴击”得分会更高一些）；再一个就是随着等级增加，飞船发射子弹的宽度以及每次发射子弹的数量都会有所增加，当然，外星人以及飞船移动速度也会增加；再一个就是最高分（High score）、当前分数（score）、飞船剩余生命、等级（level）的布局和资料书有所不同，改动就大致这些吧，以后还会逐渐改善，比如增加声音啊，让外星人也能发射子弹，飞船碰到外星人的子弹也会死亡之类的功能吧。OK，废话少说，下面上代码！

alien_invasion.py:

```
"""该游戏主程序，尽量做到最简单"""
import pygame


from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from score_board import Scoreboard


import game_function as gf


def run_game():
       """初始化背景设置"""
       pygame.init()
       
       """"创建一个Settings实例"""
       ai_settings=Settings()
       
       """创建一个游戏窗口以及标题"""
       screen=pygame.display.set_mode(
              (ai_settings.screen_width,ai_settings.screen_height))
       pygame.display.set_caption('Alien Invasion')
       
       """创建一艘飞船实例"""
       ship=Ship(ai_settings,screen)
       
       """创建一个用于存储子弹和外星人的编组"""
       bullets=Group()
       aliens=Group()


       """创建外星人群"""
       gf.creat_fleet(ai_settings,screen,ship,aliens)


       """创建存储游戏统计信息的实例,并创建记分牌"""
       stats = GameStats(ai_settings)
       sb = Scoreboard(ai_settings,screen,stats)
       
       #创建play按钮
       play_button = Button(ai_settings,screen,"Play")
       
       """进入主循环"""  
       while True:
              """"监视用户的操作，键盘和鼠标"""
              gf.check_events(ai_settings,screen,ship,aliens,bullets,stats,play_button,sb)
              if stats.game_active:
                     """更新飞船"""
                     ship.update()
                     """更新子弹"""
                     gf.update_bullet(ai_settings,screen,ship,aliens,bullets,stats,sb)
                     """更新外星人"""
                     gf.update_aliens(ai_settings,screen,ship,aliens,stats,bullets,sb)
              """刷新屏幕"""
              gf.update_screen(ai_settings,screen,ship,aliens,bullets,
                               stats,play_button,sb)


run_game()

```

game_function.py:如果把这个游戏比作一个人，那么上一段代码是刚接触这个人，他给你留下的第一印象，那么下面这段代码可以说是这个人的灵魂了

```
import sys
import pygame


from random import randint
from bullet import Bullet
from alien import Alien
from time import sleep


def fire_bullet(ai_settings,screen,ship,bullets,stats):
       """开火！"""
       #确保屏幕上的子弹数在限制范围内
       for i in range(int(stats.level/5) + 1):
              if len(bullets) &lt; ai_settings.bullet_allowed:
                     new_bullet=Bullet(ai_settings,screen,ship)
                     bullets.add(new_bullet)


def check_keydown(event,ai_settings,screen,ship,bullets,stats):
       """检查用户按键是否按下以及执行的任务"""
       if event.key  == pygame.K_RIGHT:
              ship.moving_right=True
                            
       elif event.key == pygame.K_LEFT:
              ship.moving_left=True


       elif event.key == pygame.K_UP:
              ship.moving_up=True


       elif event.key == pygame.K_DOWN:
              ship.moving_down=True


       elif event.key == pygame.K_SPACE:
              #发射一颗子弹，并且在限制范围内
              fire_bullet(ai_settings,screen,ship,bullets,stats)
              
def check_keyup(event,ship):
       """检查用户释放按键"""
       if event.key == pygame.K_RIGHT:
              ship.moving_right=False
                            
       elif event.key == pygame.K_LEFT:
              ship.moving_left=False


       elif event.key == pygame.K_UP:
              ship.moving_up=False


       elif event.key == pygame.K_DOWN:
              ship.moving_down=False
    

```

```
def check_events(ai_settings,screen,ship,aliens,bullets,stats,play_button,sb):
       """响应键盘和鼠标事件"""
       for event in pygame.event.get():
              if event.type == pygame.K_q:
                     sys.exit()
              #如果一直按下右键或者左键，空格键，则向右或右移动或者开火       
              elif event.type == pygame.KEYDOWN:
                     check_keydown(event,ai_settings,screen,ship,bullets,stats)
              
              #释放右键或左键，停止移动
              elif event.type == pygame.KEYUP:
                     check_keyup(event,ship)


              #点击Play按钮，开始游戏
              elif event.type == pygame.MOUSEBUTTONDOWN:
                     mouse_x,mouse_y = pygame.mouse.get_pos()
                     check_play_button(ai_settings,screen,ship,aliens,bullets,
                       stats,play_button,mouse_x,mouse_y,sb)
              
def  check_play_button(ai_settings,screen,ship,aliens,bullets,
                       stats,play_button,mouse_x,mouse_y,sb):
       """在玩家单击Play按钮时开始游戏"""
       button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
       if button_clicked and not stats.game_active:
              #重置游戏设置
              ai_settings.init_dynamic_settings()
              #隐藏光标
              pygame.mouse.set_visible(False)
              #重置游戏统计信息
              stats.reset_stats()
              stats.game_active = True


              #重置记分牌图像
              sb.prep_score()
              sb.prep_high_score(screen)
              sb.prep_level()
              sb.prep_ships(screen)


              #清空外星人和子弹列表
              aliens.empty()
              bullets.empty()


              #创建一群新的外星人，并让飞船居中
              creat_fleet(ai_settings,screen,ship,aliens)
              ship.center_ship(ai_settings)
                                                                        
def update_screen(ai_settings,screen,ship,aliens,bullets,stats,play_button,sb):
       """每次循环都重绘屏幕"""
       screen.fill(ai_settings.bg_color)
       for bullet in bullets.sprites():
              bullet.draw_bullet()
       ship.blitme()
       aliens.draw(screen)
       sb.show_score()
       
       #如果游戏处于非活动状态，绘制Play按钮
       if not stats.game_active:
              play_button.draw_button()
              
       """"刷新屏幕，擦去旧屏幕，显示新屏幕"""
       pygame.display.flip()



```

```
def update_bullet(ai_settings,screen,ship,aliens,bullets,stats,sb):
       """更新子弹位置，并删除已经消失的子弹"""
       #更新子弹位置
       bullets.update()
       #删除消失的子弹
       for bullet in bullets.copy():
              if bullet.rect.bottom&lt;=0:
                     bullets.remove(bullet)
       #检查是否有子弹击中外星人
       check_bullet_alien_colide(ai_settings,screen,ship,aliens,bullets,stats,sb)
       
def get_number_aliens_x(ai_settings,alien_width):
       """获得水平方向上外星人个数"""
       available_space_x = ai_settings.screen_width-2 * alien_width
       number_aliens_x = int(available_space_x/(2 * alien_width))
       return number_aliens_x


def get_space_rows(ai_settings,ship_height,alien_height):
       """获得垂直方向上外星人的行数"""
       available_space_y = (ai_settings.screen_height-(3 * alien_height)-
                          ship_height)                            
       number_aliens_rows = int(available_space_y/(2 * alien_height))
       return number_aliens_rows


def creat_alien(ai_settings,screen,aliens,alien_number,row_number):
       """根据传入的数据在某个位置创建一个外星人"""
       alien = Alien(ai_settings,screen)
       alien_width = alien.rect.width
       alien.x = alien_width + 2 * alien_width * alien_number
       alien.rect.x = alien.x
       alien.rect.y = (alien.rect.height +20) + 2 * alien.rect.height * row_number 
       aliens.add(alien)


def creat_random_alien_x(number_aliens_x,ai_settings,screen,aliens,row_number):
       """在第一行随机创建若干个外星人"""
       for i in range(2,number_aliens_x+2):
              random_number_x=randint(2,i)
              for alien_number in range(random_number_x - 1,random_number_x):
                     creat_alien(ai_settings,screen,aliens,alien_number,row_number)
                     

```

```
def creat_fleet(ai_settings,screen,ship,aliens):
       """创建外星人群以及获取屏幕上最大的行数和每行最多个数"""
       alien=Alien(ai_settings,screen)
       number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
       number_rows = get_space_rows(ai_settings,ship.rect.height,
                                    alien.rect.height)
       """随机创建行数"""
       for j in range(0,number_rows):
              random_number_y = randint(0,j)
              for row_number in range(random_number_y):
                     creat_random_alien_x(number_aliens_x,ai_settings,
                                                 screen,aliens,row_number)


def check_fleet_edges(ai_settings,aliens):
       """有外星人到达屏幕边缘"""
       for alien in aliens.sprites():
              if alien.check_edges():
                     change_fleet_direction(ai_settings,aliens)
                     break
              
def change_fleet_direction(ai_settings,aliens):
       """将外星人下移，并改变它们的方向"""
       for alien in aliens.sprites():
              alien.rect.y += ai_settings.fleet_drop_speed
       ai_settings.fleet_direction *= -1
       
def update_aliens(ai_settings,screen,ship,aliens,stats,bullets,sb):
       """检测有外星人位于屏幕边缘或者相撞或者外星人到达底部，更新外星人的位置"""       
       check_fleet_edges(ai_settings,aliens)
       aliens.update()


       #检测飞船与外星人的撞击
       if pygame.sprite.spritecollideany(ship,aliens):
              ship_hit(ai_settings,screen,ship,aliens,stats,bullets,sb)
       #检查是否有外星人到达屏幕底部
       check_aliens_bottom(ai_settings,screen,ship,aliens,stats,bullets,sb)


def check_bullet_alien_colide(ai_settings,screen,ship,aliens,bullets,stats,sb):
       """检测子弹和外星人的碰撞"""
       collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
       #两个True可使得子弹与外星人碰撞后消失，并返回一个字典
       #碰撞之后加分
       if collisions:
              for aliens in collisions.values():
                     i = randint(0,10)
                     if i&gt;8:
                            stats.score += (ai_settings.alien_points + 10) * len(aliens)
                            sb.prep_score()
                     else:
                            stats.score += ai_settings.alien_points * len(aliens)
                            sb.prep_score()
              #检查是否刷新最高分
              check_high_score(stats,sb,screen)
              
       if len(aliens) == 0:
              #删除现有的子弹，加快游戏速度,创建新的外星人
              ship.center_ship(ai_settings)
              bullets.empty()
              ai_settings.increase_speed()
              #提高等级
              stats.level += 1
              ai_settings.increase_bullet_size()
              sb.prep_level()
              
              creat_fleet(ai_settings,screen,ship,aliens)



```

```
def ship_hit(ai_settings,screen,ship,aliens,stats,bullets,sb):
       """飞船与外星人相撞，生命减1，清除外星人和子弹列表
       并创建新的外星人，飞船放在屏幕底部中央位置"""
       if stats.ship_left &gt; 0:
              stats.ship_left -= 1
              sb.prep_ships(screen)
              #清空外星人和子弹列表
              aliens.empty()
              bullets.empty()
              #新建一个飞船和外星人群
              creat_fleet(ai_settings,screen,ship,aliens)
              ship.center_ship(ai_settings)
              #暂停0.5秒
              sleep(0.5)
       else:
              ai_settings.bullet_width = 3 
              stats.game_active = False
              pygame.mouse.set_visible(True)
             
def check_aliens_bottom(ai_settings,screen,ship,aliens,stats,bullets,sb):
       """检查是否有外星人到达底部"""
       screen_rect = screen.get_rect()
       for alien in aliens.sprites():
              if alien.rect.bottom &gt;= screen_rect.bottom:
                   ship_hit(ai_settings,screen,ship,aliens,stats,bullets,sb)
                   break
       
def check_high_score(stats,sb,screen):
       """检查是否产生了新的最高分"""
       if stats.score &gt; stats.high_score:
              stats.high_score = stats.score
              sb.prep_high_score(screen)

```

后面的文件基本是作为分支吧，一些属性还有一些初始化的数据，都是为game_function文件提供资源的

settings.py:

```
class Settings():
       def __init__(self):
              """设置长度和宽度以及背景色属性"""
              self.screen_width = 800
              self.screen_height = 700
              self.bg_color=(255,255,255)
              self.ship_limit = 2


              """子弹设置""" 
              self.bullet_width = 3
              self.bullet_height=15
              self.bullet_color=(60,60,60)
              self.bullet_allowed=8


              """外星人移动设置"""
              self.fleet_drop_speed = 10
              """以什么样的速度加快游戏节奏"""
              self.speed_up_scale = 1.1
              self.init_dynamic_settings()


              """外星人点数的提高"""
              self.score_scale = 1.5


              """子弹大小提高"""
              self.bullet_scale = 10


       def init_dynamic_settings(self):
              self.speed = 1.5
              self.bullet_speed = 3
              self.alien_speed = 0.2
              #fleet_direction为1表示向右移动，-1表示向左移动
              self.fleet_direction = -1


              #计分
              self.alien_points = 10


       def increase_speed(self):
              """提高速度设置和外星人点数设置"""
              self.speed *= self.speed_up_scale
              self.bullet_speed *= self.speed_up_scale
              self.alien_speed *= self.speed_up_scale


              self.alien_points = int(self.alien_points * self.score_scale)


       def increase_bullet_size(self):
              self.bullet_width += self.bullet_scale

```

ship.py:

```
import pygame


from pygame.sprite import Sprite


class Ship(Sprite):
       def __init__(self,ai_settings,screen):
              """初始化飞船并设置其初始位置"""
              super(Ship,self).__init__()
              self.screen=screen


              #加载飞船图像并获取其外接矩形
              self.image=pygame.image.load('images/ship.bmp')
              self.rect=self.image.get_rect()#获取飞船的矩形
              self.screen_rect=screen.get_rect()#获取屏幕矩形


              self.ai_settings=ai_settings


              #将每艘新飞船放在屏幕底部中央位置
              self.rect.centerx=self.screen_rect.centerx
              self.rect.centery=self.screen_rect.centery
              self.rect.bottom=self.screen_rect.bottom


              self.center_x=float(self.rect.centerx)
              self.center_y=float(self.rect.centery)
              """连续检测按键，设置未按下右键为False"""
              self.moving_right=False
              self.moving_left=False
              self.moving_up=False
              self.moving_down=False


       def update(self):
              """如果连续按方向键，则一直移动,并且不超过边界"""
              if self.moving_right and self.rect.right &lt; self.screen_rect.right:
                     self.center_x+=self.ai_settings.speed
                     
             #使用两个if，这样玩家同时按下两个键，
             #将先增大rect.centerx值，再降低，则飞船位置不变       
              if self.moving_left and self.rect.left &gt; 0:
                     self.center_x-=self.ai_settings.speed


              if self.moving_up and self.rect.top &gt; 0:
                     self.center_y-=self.ai_settings.speed
                     
              if self.moving_down and self.rect.bottom &lt; self.screen_rect.bottom:
                     self.center_y+=self.ai_settings.speed


              self.rect.centerx=self.center_x
              self.rect.centery=self.center_y
              
       """在指定位置绘制飞船"""
       def blitme(self):
              self.screen.blit(self.image,self.rect)


       def center_ship(self,ai_settings):
              self.center_x = ai_settings.screen_width/2
              self.center_y = ai_settings.screen_height - 28

```

alien.py:

```
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
       def __init__(self,ai_settings,screen):
              super().__init__()
              """初始化外星人并设置其初始位置"""
              self.screen=screen
              self.ai_settings=ai_settings


              #加载外星人图像并设置rect属性
              self.image=pygame.image.load('images/alien.bmp')
              self.rect=self.image.get_rect()


              #每个外星人都在屏幕左上角附近
              self.rect.x=self.rect.width
              self.rect.y=self.rect.height 


              #存储外星人准确位置
              self.x=float(self.rect.x)


       def check_edges(self):
              """如果外星人碰到屏幕边缘，则返回True"""
              screen_rect = self.screen.get_rect()
              if self.rect.right &gt;= screen_rect.right:
                     return True
              elif self.rect.left &lt;= 0:
                     return True


       def update(self):
              """移动外星人"""
              self.x += (self.ai_settings.alien_speed *
                         (self.ai_settings.fleet_direction))
              self.rect.x=self.x


       def blitme(self):
              """在指定位置绘制飞船"""
              self.screen.blit(self.image,self.rect)

```

bullet.py:

```
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
       def __init__(self,ai_settings,screen,ship):
              #在飞船位置创建一个子弹对象
              super(Bullet,self).__init__()
              self.screen=screen


              self.rect=pygame.Rect(0,0,ai_settings.bullet_width
                                    ,ai_settings.bullet_height)
              self.rect.centerx = ship.rect.centerx
              self.rect.top = ship.rect.top
              self.y=float(self.rect.y)
              self.color=ai_settings.bullet_color
              self.speed=ai_settings.bullet_speed


       def update(self):
              """向上移动子弹"""
              #更新子弹的小数值
              self.y -= self.speed
              self.rect.y=self.y


       def draw_bullet(self):
              """在屏幕上绘制子弹"""
              pygame.draw.rect(self.screen,self.color,self.rect)

```

button.py:

```
import pygame.font


class Button():
       def __init__(self,ai_settings,screen,msg):
              """初始化按钮属性"""
              self.screen = screen
              self.screen_rect = screen.get_rect()


              #设置按钮大小以及其他属性
              self.width,self.height = 200,50
              self.button_color = (0, 255, 0)
              self.text_color = (60,60,60)
              self.font = pygame.font.SysFont(None,48)


              #创建按钮的rect对象，并使其居中
              self.rect = pygame.Rect(0, 0, self.width, self.height)
              self.rect.center = self.screen_rect.center


              #按钮的标签只需要创建一次
              self.prep_msg(msg)


       def prep_msg(self,msg):
              """将msg渲染为图像，并使其在按钮上居中"""
              self.msg_image = self.font.render(msg,True,self.text_color,
                                                 self.button_color)
              self.msg_image_rect = self.msg_image.get_rect()
              self.msg_image_rect.center = self.rect.center


       def draw_button(self):
              #绘制一个用颜色填充的按钮，再绘制文本
              self.screen.fill(self.button_color,self.rect)
              self.screen.blit(self.msg_image,self.msg_image_rect)

```

game_stats.py:

```
class GameStats():
       """跟踪游戏的统计信息"""
       def __init__(self,ai_settings):
              self.ai_settings = ai_settings
              self.game_active = False
              self.reset_stats()


              #任何情况下都不能重置最高分
              self.high_score = 0


       def reset_stats(self):
              """初始化在游戏运行过程中可能变化的统计信息"""
              self.ship_left = self.ai_settings.ship_limit
              self.score = 0
              self.level = 1
              self.bullet_width = 3

```

scord_board.py:

```
import pygame.font


from pygame.sprite import Group
from ship import Ship


class Scoreboard():
       """显示得分的类"""
       def __init__(self,ai_settings,screen,stats):
              """初始化显示得分的属性"""
              self.screen = screen
              self.screen_rect = screen.get_rect()
              self.ai_settings = ai_settings
              self.stats = stats


              #显示得分时的字体设置
              self.text_color = (30,30,30)
              self.font = pygame.font.SysFont(None,48)


              #准备初始得分图像以及当前最高得分
              self.prep_score()
              self.prep_high_score(screen)
              self.prep_level()
              self.prep_ships(screen)


       def prep_score(self):
              """将得分转化为可渲染的图像"""
              rounded_score = int(round(self.stats.score,-1))
              score_str ="Score:"+"{:,}".format(rounded_score)
              self.score_image = self.font.render(score_str,True,self.text_color,
                                                  self.ai_settings.bg_color)


              #将得分放在屏幕右上角
              self.score_rect = self.score_image.get_rect()
              self.score_rect.right = self.screen_rect.right - 20
              self.score_rect.top = 20


       def prep_high_score(self,screen):
              """将最高得分渲染为图片"""
              high_score = int(round(self.stats.high_score,-1))
              high_score_str = "High Score:"+"{:,}".format(high_score)
              self.high_score_image = self.font.render(high_score_str,True,self.text_color,
                                                  self.ai_settings.bg_color)


              """将最高得分放在屏幕左上角"""
              self.high_score_rect = self.high_score_image.get_rect()
              self.high_score_rect.left = self.screen_rect.left + 20
              self.high_score_rect.top = 20


       def prep_level(self):
              """将等级渲染为图像"""
              self.level_image = self.font.render("Level:"+str(self.stats.level),True,
                                                  self.text_color,self.ai_settings.bg_color)


              #将等级放在右下角
              self.level_rect = self.level_image.get_rect()
              self.level_rect.right = self.score_rect.right
              self.level_rect.bottom = self.score_rect.bottom + 650


       def show_score(self):
              """在屏幕上显示得分,最高分，等级"""
              self.screen.blit(self.score_image,self.score_rect)
              self.screen.blit(self.high_score_image,self.high_score_rect)
              self.screen.blit(self.level_image,self.level_rect)
              #绘制剩余飞船
              self.ships.draw(self.screen)


       def prep_ships(self,screen):
              """显示剩余的飞机"""
              self.ships = Group()
              for ship_number in range(self.stats.ship_left + 1):
                     ship =Ship(self.ai_settings,self.screen)
                     ship.rect.x = 10 + ship_number * ship.rect.width
                     ship.rect.y = self.screen_rect.top + 640
                     self.ships.add(ship)

```

代码的话，我觉得注释已经比较清楚了，然后就没有多费口舌去解释

下面是运行之后的截图：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanlMTmE5R2ljZ0kzZzVyVDZpYmlhcFZoTWZFNUN4YUZMaWNWc2JrRHIxbTQzUFdIV21xdmJDQTBuaFRYdU1ZbFdSYkFnRlBCMVJBNG5pYmlhakEvNjQw?x-oss-process=image/format,png">当三艘飞船用光后，结束游戏<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanlMTmE5R2ljZ0kzZzVyVDZpYmlhcFZoTWZJZnhpYVRPczJ5Z2xEMWtodjNCaEJYTVR4OWpsblhaQ3hGMXJTamxBaWN1VnhDMWdGZ29ReFE0dy82NDA?x-oss-process=image/format,png">再次点击“Play”按钮，再次开始<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanlMTmE5R2ljZ0kzZzVyVDZpYmlhcFZoTWZMUTliM2ljaWNvUFJJSG9MaWJtSEFaOUtub08xYkNEVFE4SUJvQmlhaWFCYmN5NkczYVIwNFpwZVVaUS82NDA?x-oss-process=image/format,png">上面就是代码还有运行之后的照片了，虽然游戏到目前为止还不是很完善，但是这七天我真的学会了很多东西，我觉得对我最有益的还是学会了模块化思维，这种思维就是将复杂的问题分解成小的模块，如果这些小的模块仍然比较麻烦，那就继续分解，说实话，短短七天，这种思想已经开始渗透到其他的学科，甚至我的日常生活，想到这我还是非常开心的。还有的话就是学会了类，学会了类的属性以及方法，还有大范围的使用函数（在game_function文件中可以看到，单这个文件就大概用了15到20个函数），大大提高了我使用函数的熟练度。

emmm，在大一开始学习C语言，那时候也不听课，上C语言就看那些游戏主播，然后做题也不会，考试的时候背了几段代码就去考试了，结果还做出来了8个（总共11个，没有选择填空这些理论题目），那时候就暗下发誓，这辈子永远不会去学这些编程语言！！！现在，嚯~！真香啊！我再次接触C语言是因为要学习单片机，要参加比赛，然后不得不去复习，然后慢慢的发现，C语言是这么的简单啊（当然，学到指针那地方也是让我头疼了好几个周，还有后面的数据结构也是），然后慢慢的又开始接触上了Python，一开始是看B站小甲鱼的视频学习，但是慢慢地，感觉没有资料完全听不懂，所以呢，又买了以恶不能资料书去学习，本来打算看视频然后配合视频学习的，但是后来发现，小甲鱼的视频其实更偏向于python进阶，所以就放弃了视频，主攻资料书了。

总的来说吧，对于自己现在的状态非常满意，嘿嘿！

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9RQjZHNFpvRTE4NGliejlNc2N3YXE5OHcwNXVHQWljMXh0UXZqNWhzTEQ1eFdmcjlIYlhsTDVSTnFRcU1wcnVnNlhqRDdtSTRVY1F2Y3U2NEdHZTI3VDdBLzY0MA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb24walFiZjlpYVdGcTBMaWJaSVQ0WXJCNGlhd0ZmZE5lQjFJcks0eXhrWVplbnFvWWY2dHc3dElpY0EyMUxNWEFSVzN6bkk5ajU0NmliMzFRLzY0MA?x-oss-process=image/format,png">

分享或在看是对我最大的支持 
