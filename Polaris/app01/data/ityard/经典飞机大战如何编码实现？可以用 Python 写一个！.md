
--- 
title:  经典飞机大战如何编码实现？可以用 Python 写一个！ 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/20200523084742897.jpg#pic_center" alt=""> 当年微信 5.0 发布时，首页被设置成了一款新推出的小游戏，它就是微信版飞机大战，游戏一经推出便是火爆异常，铅笔画风格的游戏界面也受到了很多人的喜欢。

最近重温了一下这款小游戏，尽管时隔多年，但无论是游戏的画质还是风格，时至今日依然都不过时。本文我们使用 Python 来实现一下这款小游戏，游戏的实现主要用到第三方模块 pygame，安装使用 `pip install pygame` 即可。

### 环境

操作系统：Windows Python 版本：3.6 涉及模块：pygame、sys、random

### 实现

飞机大战的构成相对比较简单，主要包括：主界面、玩家、敌人、子弹、计分板等，下面来看一下具体实现。

首先我们来绘制一个主界面，主要实现代码如下所示：

```
# 设置屏幕的宽度
SCREEN_WIDTH = 450
# 设置屏幕的高度
SCREEN_HEIGHT = 600
# 初始化窗口
pygame.init()
# 设置窗口标题
pygame.display.set_caption("飞机大战")
# 设置屏幕大小
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
# 隐藏光标
pygame.mouse.set_visible(False)
# 设置背景
bg = pygame.image.load("resources/image/bg.png")
# 绘制屏幕
screen.fill(0)
# 加入背景图片
screen.blit(bg, (0, 0))
# 设置游戏结束的图片
bg_game_over = pygame.image.load("resources/image/bg_game_over.png")
# 加载飞机资源图片
img_plane = pygame.image.load("resources/image/shoot.png")
img_start = pygame.image.load("resources/image/start.png")
img_pause = pygame.image.load("resources/image/pause.png")
img_icon = pygame.image.load("resources/image/plane.png").convert_alpha()
# 顺便设置窗口
pygame.display.set_icon(img_icon)
# 初始化位置
player_pos = [200, 450]

```

看一下效果： <img src="https://img-blog.csdnimg.cn/20200530092115239.PNG#pic_" alt="" width="400"> 接着，我们再来定义玩家的属性和方法，主要实现代码如下所示：

```
class Player(pygame.sprite.Sprite):
    def __init__(self, img, rect, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = []
        # 将飞机图片部分分隔
        for i in range(len(rect)):
            self.image.append(img.subsurface(rect[i]).convert_alpha())
        # 获取飞机的区域
        self.rect = rect[0]
        self.rect.topleft = pos
        self.speed = 8
        # 生成精灵组实例
        self.bullets = pygame.sprite.Group()
        self.img_index = 0
        # 判断飞机是否被打中
        self.is_hit = False
    def shoot(self, img):
        bullet = Bullet(img, self.rect.midtop)
        # 添加子弹实例到玩家的子弹组
        self.bullets.add(bullet)
    def moveUp(self):
        # 当遇到顶部时,设置上顶部为0
        if self.rect.top &lt;= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed
    def moveDown(self):
        # 当遇到底部时,设置一直为常值
        if self.rect.top &gt;= SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.top += self.speed
    def moveLeft(self):
        # 当遇到左边时,一直停靠在左边
        if self.rect.left &lt;= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed
    def moveRight(self):
        # 当遇到右边时, 停靠右边
        if self.rect.left &gt;= SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left += self.speed

```

看一下玩家的飞机样式： <img src="https://img-blog.csdnimg.cn/2020053009293817.PNG" alt=""> 我们再接着定义子弹的属性和方法，主要实现代码如下所示：

```
class Bullet(pygame.sprite.Sprite):
    def __init__(self, img, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        # 设置图片的区域
        self.rect = self.image.get_rect()
        self.rect.midbottom = pos
        self.speed = 10
    def move(self):
        self.rect.top -= self.speed

```

看一下子弹的样式： <img src="https://img-blog.csdnimg.cn/20200530093151928.PNG" alt=""> 定义完玩家，我们再来定义敌机的属性和方法，主要实现代码如下所示：

```
class Enemy(pygame.sprite.Sprite):
    def __init__(self, img, explosion_img, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.explosion_img = explosion_img
        self.speed = 2
        # 设置击毁序列
        self.explosion_index = 0
    def move(self):
        # 敌人的子弹只能一直向下
        self.rect.top += self.speed

```

最后，我们来定义一下游戏运行的相应逻辑，比如：击中敌机、玩家与敌机碰撞、生成分数等，主要实现代码如下所示：

```
while running:
    # 设置游戏帧率为 60
    clock.tick(60)
    if not is_pause and not is_game_over:
        if not player.is_hit:
            # 设置连续射击,因为每秒 60 帧,15/60=0.25 秒发一次子弹
            if shoot_frequency % 15 == 0:
                player.shoot(bullet_img)
            shoot_frequency += 1
            # 当设置的射击频率大于 15，置零
            if shoot_frequency &gt;= 15:
                shoot_frequency = 0
        # 控制生成敌机的频率
        if enemy_frequency % 50 == 0:
            # 设置敌机的出现的位置
            enemy_pos = [random.randint(0, SCREEN_WIDTH - enemy_rect.width), 0]
            enemy = Enemy(enemy_img, enemy_explosion_imgs, enemy_pos)
            enemies.add(enemy)
        enemy_frequency += 1
        if enemy_frequency &gt;= 100:
            enemy_frequency = 0
        # 控制子弹的显示运行
        for bullet in player.bullets:
            bullet.move()
            if bullet.rect.bottom &lt; 0:
                player.bullets.remove(bullet)
        # 控制敌机的运行
        for enemy in enemies:
            enemy.move()
            # 判断敌机是否与玩家飞机碰撞
            if pygame.sprite.collide_circle(enemy, player):
                enemies_explosion.add(enemy)
                enemies.remove(enemy)
                player.is_hit = True
                # 设置玩家的飞机被毁
                is_game_over = True
            # 判断敌机是否在界面
            if enemy.rect.top &lt; 0:
                enemies.remove(enemy)
        # 设置敌机与玩家的飞机子弹相碰时，返回被击的敌机实例
        enemy_explosion = pygame.sprite.groupcollide(enemies, player.bullets, 1, 1)
        for enemy in enemy_explosion:
            enemies_explosion.add(enemy)
    # 绘制屏幕
    screen.fill(0)
    # 加入背景图片
    screen.blit(bg, (0, 0))
    # 添加玩家飞机图片到屏幕
    if not player.is_hit:
        screen.blit(player.image[int(player.img_index)], player.rect)
        player.img_index = shoot_frequency / 8
    else:
        if player_explosion_index &gt; 47:
            is_game_over = True
        else:
            player.img_index = player_explosion_index / 8
            screen.blit(player.image[int(player.img_index)], player.rect)
            player_explosion_index += 1
    # 敌机被子弹击中的效果显示
    for enemy in enemies_explosion:
        if enemy.explosion_index == 0:
            pass
        if enemy.explosion_index &gt; 7:
            enemies_explosion.remove(enemy)
            score += 100
            continue
        # 敌机被击时显示图片
        screen.blit(enemy.explosion_img[int(enemy.explosion_index / 2)], enemy.rect)
        enemy.explosion_index += 1
    # 显示子弹
    player.bullets.draw(screen)
    # 显示敌机
    enemies.draw(screen)
    # 分数的显示效果
    score_font = pygame.font.Font(None, 36)
    score_text = score_font.render(str(score), True, (128, 128, 128))
    # 设置文字框
    text_rect = score_text.get_rect()
    # 放置文字的位置
    text_rect.topleft = [20, 10]
    # 显示出分数
    screen.blit(score_text, text_rect)
    left, middle, right = pygame.mouse.get_pressed()
    # 暂停游戏
    if right == True and not is_game_over:
        is_pause = True
    if left == True:
        # 重置游戏
        if is_game_over:
            is_game_over = False
            player_rect = []
            player_rect.append(pygame.Rect(0, 99, 102, 126))
            player_rect.append(pygame.Rect(165, 360, 102, 126))
            player_rect.append(pygame.Rect(165, 234, 102, 126))
            player_rect.append(pygame.Rect(330, 624, 102, 126))
            player_rect.append(pygame.Rect(330, 498, 102, 126))
            player_rect.append(pygame.Rect(432, 624, 102, 126))
            player = Player(img_plane, player_rect, player_pos)
            bullet_rect = pygame.Rect(1004, 987, 9, 21)
            bullet_img = img_plane.subsurface(bullet_rect)
            enemy_rect = pygame.Rect(534, 612, 57, 43)
            enemy_img = img_plane.subsurface(enemy_rect)
            enemy_explosion_imgs = []
            enemy_explosion_imgs.append(img_plane.subsurface(pygame.Rect(267, 347, 57, 43)))
            enemy_explosion_imgs.append(img_plane.subsurface(pygame.Rect(873, 697, 57, 43)))
            enemy_explosion_imgs.append(img_plane.subsurface(pygame.Rect(267, 296, 57, 43)))
            enemy_explosion_imgs.append(img_plane.subsurface(pygame.Rect(930, 697, 57, 43)))
            enemies = pygame.sprite.Group()
            enemies_explosion = pygame.sprite.Group()
            score = 0
            shoot_frequency = 0
            enemy_frequency = 0
            player_explosion_index = 16
        # 继续游戏
        if is_pause:
            is_pause = False
    # 游戏结束
    if is_game_over:
        font = pygame.font.SysFont("微软雅黑", 48)
        text = font.render("Score: " + str(score), True, (255, 0, 0))
        text_rect = text.get_rect()
        text_rect.centerx = screen.get_rect().centerx
        text_rect.centery = screen.get_rect().centery + 70
        # 显示游戏结束画面
        screen.blit(bg_game_over, (0, 0))
        # 显示分数
        screen.blit(text, text_rect)
        font = pygame.font.SysFont("微软雅黑", 40)
        text = font.render("Press Left Mouse to Restart", True, (255, 0, 0))
        text_rect = text.get_rect()
        text_rect.centerx = screen.get_rect().centerx
        text_rect.centery = screen.get_rect().centery + 150
        screen.blit(text, text_rect)
    # 刷新屏幕
    pygame.display.update()
    # 处理游戏退出
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if not is_pause and not is_game_over:
        key = pygame.key.get_pressed()
        if key[K_w] or key[K_UP]:
            player.moveUp()
        if key[K_s] or key[K_DOWN]:
            player.moveDown()
        if key[K_a] or key[K_LEFT]:
            player.moveLeft()
        if key[K_d] or key[K_RIGHT]:
            player.moveRight()

```

我们来看一下最终实现效果： <img src="https://img-blog.csdnimg.cn/20200530095146111.gif#pic_" alt="" width="400">

>  
 作者：程序员野客 公号：Python小二 链接： 

