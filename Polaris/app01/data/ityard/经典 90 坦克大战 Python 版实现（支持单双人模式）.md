
--- 
title:  经典 90 坦克大战 Python 版实现（支持单双人模式） 
tags: []
categories: [] 

---
坦克大战是一个比较经典的小游戏，而 90 坦克大战是一个比较经典的版本，我们来看一下如何利用 Python 实现坦克大战，先睹为快。 <img src="https://img-blog.csdnimg.cn/20200106200951816.gif" alt="">

### 游戏设定

➢ **基本组成**
- 场景- 坦克- 子弹- 食物- 大本营
➢ **操作规则**

玩家一
- 移动：WASD- 射击：J
玩家二
- 移动：←→↑↓- 射击：0
### 主要实现

➢ **场景实现代码**

```
# 场景类
import pygame
import random

# 石头墙
class Brick(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.brick = pygame.image.load('images/scene/brick.png')
		self.rect = self.brick.get_rect()
		self.being = False
# 钢墙
class Iron(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.iron = pygame.image.load('images/scene/iron.png')
		self.rect = self.iron.get_rect()
		self.being = False
# 冰
class Ice(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.ice = pygame.image.load('images/scene/ice.png')
		self.rect = self.ice.get_rect()
		self.being = False
# 河流
class River(pygame.sprite.Sprite):
	def __init__(self, kind=None):
		pygame.sprite.Sprite.__init__(self)
		if kind is None:
			self.kind = random.randint(0, 1)
		self.rivers = ['images/scene/river1.png', 'images/scene/river2.png']
		self.river = pygame.image.load(self.rivers[self.kind])
		self.rect = self.river.get_rect()
		self.being = False
# 树
class Tree(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.tree = pygame.image.load('images/scene/tree.png')
		self.rect = self.tree.get_rect()
		self.being = False
# 地图
class Map():
	def __init__(self, stage):
		self.brickGroup = pygame.sprite.Group()
		self.ironGroup  = pygame.sprite.Group()
		self.iceGroup = pygame.sprite.Group()
		self.riverGroup = pygame.sprite.Group()
		self.treeGroup = pygame.sprite.Group()
		if stage == 1:
			self.stage1()
		elif stage == 2:
			self.stage2()
	# 关卡一
	def stage1(self):
		for x in [2, 3, 6, 7, 18, 19, 22, 23]:
			for y in [2, 3, 4, 5, 6, 7, 8, 9, 10, 17, 18, 19, 20, 21, 22, 23]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
				self.brick.being = True
				self.brickGroup.add(self.brick)
		for x in [10, 11, 14, 15]:
			for y in [2, 3, 4, 5, 6, 7, 8, 11, 12, 15, 16, 17, 18, 19, 20]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
				self.brick.being = True
				self.brickGroup.add(self.brick)
		for x in [4, 5, 6, 7, 18, 19, 20, 21]:
			for y in [13, 14]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
				self.brick.being = True
				self.brickGroup.add(self.brick)
		for x in [12, 13]:
			for y in [16, 17]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
				self.brick.being = True
				self.brickGroup.add(self.brick)
		for x, y in [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25), (14, 25)]:
			self.brick = Brick()
			self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
			self.brick.being = True
			self.brickGroup.add(self.brick)
		for x, y in [(0, 14), (1, 14), (12, 6), (13, 6), (12, 7), (13, 7), (24, 14), (25, 14)]:
			self.iron = Iron()
			self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24
			self.iron.being = True
			self.ironGroup.add(self.iron)
	# 关卡二
	def stage2(self):
		for x in [2, 3, 6, 7, 18, 19, 22, 23]:
			for y in [2, 3, 4, 5, 6, 7, 8, 9, 10, 17, 18, 19, 20, 21, 22, 23]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
				self.brick.being = True
				self.brickGroup.add(self.brick)
		for x in [10, 11, 14, 15]:
			for y in [2, 3, 4, 5, 6, 7, 8, 11, 12, 15, 16, 17, 18, 19, 20]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
				self.brick.being = True
				self.brickGroup.add(self.brick)
		for x in [4, 5, 6, 7, 18, 19, 20, 21]:
			for y in [13, 14]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
				self.brick.being = True
				self.brickGroup.add(self.brick)
		for x in [12, 13]:
			for y in [16, 17]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
				self.brick.being = True
				self.brickGroup.add(self.brick)
		for x, y in [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25), (14, 25)]:
			self.brick = Brick()
			self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
			self.brick.being = True
			self.brickGroup.add(self.brick)
		for x, y in [(0, 14), (1, 14), (12, 6), (13, 6), (12, 7), (13, 7), (24, 14), (25, 14)]:
			self.iron = Iron()
			self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24
			self.iron.being = True
			self.ironGroup.add(self.iron)
	def protect_home(self):
		for x, y in [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25), (14, 25)]:
			self.iron = Iron()
			self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24
			self.iron.being = True
			self.ironGroup.add(self.iron)

```

➢ **坦克实现代码**

```
# 坦克类
import pygame
import random
from BattleCity.bullet import Bullet

# 我方坦克类
class myTank(pygame.sprite.Sprite):
	def __init__(self, player):
		pygame.sprite.Sprite.__init__(self)
		# 玩家编号(1/2)
		self.player = player
		# 不同玩家用不同的坦克(不同等级对应不同的图)
		if player == 1:
			self.tanks = ['images/myTank/tank_T1_0.png', 'images/myTank/tank_T1_1.png', 'images/myTank/tank_T1_2.png']
		elif player == 2:
			self.tanks = ['images/myTank/tank_T2_0.png', 'images/myTank/tank_T2_1.png', 'images/myTank/tank_T2_2.png']
		else:
			raise ValueError('myTank class -&gt; player value error.')
		# 坦克等级(初始0)
		self.level = 0
		# 载入(两个tank是为了轮子特效)
		self.tank = pygame.image.load(self.tanks[self.level]).convert_alpha()
		self.tank_0 = self.tank.subsurface((0, 0), (48, 48))
		self.tank_1 = self.tank.subsurface((48, 0), (48, 48))
		self.rect = self.tank_0.get_rect()
		# 保护罩
		self.protected_mask = pygame.image.load('images/others/protect.png').convert_alpha()
		self.protected_mask1 = self.protected_mask.subsurface((0, 0), (48, 48))
		self.protected_mask2 = self.protected_mask.subsurface((48, 0), (48, 48))
		# 坦克方向
		self.direction_x, self.direction_y = 0, -1
		# 不同玩家的出生位置不同
		if player == 1:
			self.rect.left, self.rect.top = 3 + 24 * 8, 3 + 24 * 24
		elif player == 2:
			self.rect.left, self.rect.top = 3 + 24 * 16, 3 + 24 * 24
		else:
			raise ValueError('myTank class -&gt; player value error.')
		# 坦克速度
		self.speed = 3
		# 是否存活
		self.being = True
		# 有几条命
		self.life = 3
		# 是否处于保护状态
		self.protected = False
		# 子弹
		self.bullet = Bullet()
	# 射击
	def shoot(self):
		self.bullet.being = True
		self.bullet.turn(self.direction_x, self.direction_y)
		if self.direction_x == 0 and self.direction_y == -1:
			self.bullet.rect.left = self.rect.left + 20
			self.bullet.rect.bottom = self.rect.top - 1
		elif self.direction_x == 0 and self.direction_y == 1:
			self.bullet.rect.left = self.rect.left + 20
			self.bullet.rect.top = self.rect.bottom + 1
		elif self.direction_x == -1 and self.direction_y == 0:
			self.bullet.rect.right = self.rect.left - 1
			self.bullet.rect.top = self.rect.top + 20
		elif self.direction_x == 1 and self.direction_y == 0:
			self.bullet.rect.left = self.rect.right + 1
			self.bullet.rect.top = self.rect.top + 20
		else:
			raise ValueError('myTank class -&gt; direction value error.')
		if self.level == 0:
			self.bullet.speed = 8
			self.bullet.stronger = False
		elif self.level == 1:
			self.bullet.speed = 12
			self.bullet.stronger = False
		elif self.level == 2:
			self.bullet.speed = 12
			self.bullet.stronger = True
		elif self.level == 3:
			self.bullet.speed = 16
			self.bullet.stronger = True
		else:
			raise ValueError('myTank class -&gt; level value error.')
	# 等级提升
	def up_level(self):
		if self.level &lt; 3:
			self.level += 1
		try:
			self.tank = pygame.image.load(self.tanks[self.level]).convert_alpha()
		except:
			self.tank = pygame.image.load(self.tanks[-1]).convert_alpha()
	# 等级降低
	def down_level(self):
		if self.level &gt; 0:
			self.level -= 1
		self.tank = pygame.image.load(self.tanks[self.level]).convert_alpha()
	# 向上
	def move_up(self, tankGroup, brickGroup, ironGroup, myhome):
		self.direction_x, self.direction_y = 0, -1
		# 先移动后判断
		self.rect = self.rect.move(self.speed*self.direction_x, self.speed*self.direction_y)
		self.tank_0 = self.tank.subsurface((0, 0), (48, 48))
		self.tank_1 = self.tank.subsurface((48, 0), (48, 48))
		# 是否可以移动
		is_move = True
		# 地图顶端
		if self.rect.top &lt; 3:
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			is_move = False
		# 撞石头/钢墙
		if pygame.sprite.spritecollide(self, brickGroup, False, None) or \
			pygame.sprite.spritecollide(self, ironGroup, False, None):
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			is_move = False
		# 撞其他坦克
		if pygame.sprite.spritecollide(self, tankGroup, False, None):
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			is_move = False
		# 大本营
		if pygame.sprite.collide_rect(self, myhome):
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			is_move = False
		return is_move
	# 向下
	def move_down(self, tankGroup, brickGroup, ironGroup, myhome):
		self.direction_x, self.direction_y = 0, 1
		# 先移动后判断
		self.rect = self.rect.move(self.speed*self.direction_x, self.speed*self.direction_y)
		self.tank_0 = self.tank.subsurface((0, 48), (48, 48))
		self.tank_1 = self.tank.subsurface((48, 48), (48, 48))
		# 是否可以移动
		is_move = True
		# 地图底端
		if self.rect.bottom &gt; 630 - 3:
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			is_move = False
		# 撞石头/钢墙
		if pygame.sprite.spritecollide(self, brickGroup, False, None) or \
			pygame.sprite.spritecollide(self, ironGroup, False, None):
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			is_move = False
		# 撞其他坦克
		if pygame.sprite.spritecollide(self, tankGroup, False, None):
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			is_move = False
		# 大本营
		if pygame.sprite.collide_rect(self, myhome):
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			is_move = False
		return is_move
	# 向左
	def move_left(self, tankGroup, brickGroup, ironGroup, myhome):
		self.direction_x, self.direction_y = -1, 0
		# 先移动后判断
		self.rect = self.rect.move(self.speed*self.direction_x, self.speed*self.direction_y)
		self.tank_0 = self.tank.subsurface((0, 96), (48, 48))
		self.tank_1 = self.tank.subsurface((48, 96), (48, 48))
		# 是否可以移动
		is_move = True
		# 地图左端
		if self.rect.left &lt; 3:
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			is_move = False
		# 撞石头/钢墙
		if pygame.sprite.spritecollide(self, brickGroup, False, None) or \
			pygame.sprite.spritecollide(self, ironGroup, False, None):
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			is_move = False
		# 撞其他坦克
		if pygame.sprite.spritecollide(self, tankGroup, False, None):
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			is_move = False		
		# 大本营
		if pygame.sprite.collide_rect(self, myhome):
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			is_move = False
		return is_move
	# 向右
	def move_right(self, tankGroup, brickGroup, ironGroup, myhome):
		self.direction_x, self.direction_y = 1, 0
		# 先移动后判断
		self.rect = self.rect.move(self.speed*self.direction_x, self.speed*self.direction_y)
		self.tank_0 = self.tank.subsurface((0, 144), (48, 48))
		self.tank_1 = self.tank.subsurface((48, 144), (48, 48))
		# 是否可以移动
		is_move = True
		# 地图右端
		if self.rect.right &gt; 630 - 3:
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			is_move = False
		# 撞石头/钢墙
		if pygame.sprite.spritecollide(self, brickGroup, False, None) or \
			pygame.sprite.spritecollide(self, ironGroup, False, None):
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			is_move = False
		# 撞其他坦克
		if pygame.sprite.spritecollide(self, tankGroup, False, None):
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			is_move = False
		# 大本营
		if pygame.sprite.collide_rect(self, myhome):
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			is_move = False
		return is_move
	# 死后重置
	def reset(self):
		self.level = 0
		self.protected = False
		self.tank = pygame.image.load(self.tanks[self.level]).convert_alpha()
		self.tank_0 = self.tank.subsurface((0, 0), (48, 48))
		self.tank_1 = self.tank.subsurface((48, 0), (48, 48))
		self.rect = self.tank_0.get_rect()
		self.direction_x, self.direction_y = 0, -1
		if self.player == 1:
			self.rect.left, self.rect.top = 3 + 24 * 8, 3 + 24 * 24
		elif self.player == 2:
			self.rect.left, self.rect.top = 3 + 24 * 16, 3 + 24 * 24
		else:
			raise ValueError('myTank class -&gt; player value error.')
		self.speed = 3
# 敌方坦克类
class enemyTank(pygame.sprite.Sprite):
	def __init__(self, x=None, kind=None, is_red=None):
		pygame.sprite.Sprite.__init__(self)
		# 用于给刚生成的坦克播放出生特效
		self.born = True
		self.times = 90
		# 坦克的种类编号
		if kind is None:
			self.kind = random.randint(0, 3)
		else:
			self.kind = kind
		# 所有坦克
		self.tanks1 = ['images/enemyTank/enemy_1_0.png', 'images/enemyTank/enemy_1_1.png', 'images/enemyTank/enemy_1_2.png', 'images/enemyTank/enemy_1_3.png']
		self.tanks2 = ['images/enemyTank/enemy_2_0.png', 'images/enemyTank/enemy_2_1.png', 'images/enemyTank/enemy_2_2.png', 'images/enemyTank/enemy_2_3.png']
		self.tanks3 = ['images/enemyTank/enemy_3_0.png', 'images/enemyTank/enemy_3_1.png', 'images/enemyTank/enemy_3_2.png', 'images/enemyTank/enemy_3_3.png']
		self.tanks4 = ['images/enemyTank/enemy_4_0.png', 'images/enemyTank/enemy_4_1.png', 'images/enemyTank/enemy_4_2.png', 'images/enemyTank/enemy_4_3.png']
		self.tanks = [self.tanks1, self.tanks2, self.tanks3, self.tanks4]
		# 是否携带食物(红色的坦克携带食物)
		if is_red is None:
			self.is_red = random.choice((True, False, False, False, False))
		else:
			self.is_red = is_red
		# 同一种类的坦克具有不同的颜色, 红色的坦克比同类坦克多一点血量
		if self.is_red:
			self.color = 3
		else:
			self.color = random.randint(0, 2)
		# 血量
		self.blood = self.color
		# 载入(两个tank是为了轮子特效)
		self.tank = pygame.image.load(self.tanks[self.kind][self.color]).convert_alpha()
		self.tank_0 = self.tank.subsurface((0, 48), (48, 48))
		self.tank_1 = self.tank.subsurface((48, 48), (48, 48))
		self.rect = self.tank_0.get_rect()
		# 坦克位置
		if x is None:
			self.x = random.randint(0, 2)
		else:
			self.x = x
		self.rect.left, self.rect.top = 3 + self.x * 12 * 24, 3
		# 坦克是否可以行动
		self.can_move = True
		# 坦克速度
		self.speed = max(3 - self.kind, 1)
		# 方向
		self.direction_x, self.direction_y = 0, 1
		# 是否存活
		self.being = True
		# 子弹
		self.bullet = Bullet()
	# 射击
	def shoot(self):
		self.bullet.being = True
		self.bullet.turn(self.direction_x, self.direction_y)
		if self.direction_x == 0 and self.direction_y == -1:
			self.bullet.rect.left = self.rect.left + 20
			self.bullet.rect.bottom = self.rect.top - 1
		elif self.direction_x == 0 and self.direction_y == 1:
			self.bullet.rect.left = self.rect.left + 20
			self.bullet.rect.top = self.rect.bottom + 1
		elif self.direction_x == -1 and self.direction_y == 0:
			self.bullet.rect.right = self.rect.left - 1
			self.bullet.rect.top = self.rect.top + 20
		elif self.direction_x == 1 and self.direction_y == 0:
			self.bullet.rect.left = self.rect.right + 1
			self.bullet.rect.top = self.rect.top + 20
		else:
			raise ValueError('enemyTank class -&gt; direction value error.')
	# 随机移动
	def move(self, tankGroup, brickGroup, ironGroup, myhome):
		self.rect = self.rect.move(self.speed*self.direction_x, self.speed*self.direction_y)
		is_move = True
		if self.direction_x == 0 and self.direction_y == -1:
			self.tank_0 = self.tank.subsurface((0, 0), (48, 48))
			self.tank_1 = self.tank.subsurface((48, 0), (48, 48))
			if self.rect.top &lt; 3:
				self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
				self.direction_x, self.direction_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
				is_move = False
		elif self.direction_x == 0 and self.direction_y == 1:
			self.tank_0 = self.tank.subsurface((0, 48), (48, 48))
			self.tank_1 = self.tank.subsurface((48, 48), (48, 48))
			if self.rect.bottom &gt; 630 - 3:
				self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
				self.direction_x, self.direction_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
				is_move = False
		elif self.direction_x == -1 and self.direction_y == 0:
			self.tank_0 = self.tank.subsurface((0, 96), (48, 48))
			self.tank_1 = self.tank.subsurface((48, 96), (48, 48))
			if self.rect.left &lt; 3:
				self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
				self.direction_x, self.direction_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
				is_move = False
		elif self.direction_x == 1 and self.direction_y == 0:
			self.tank_0 = self.tank.subsurface((0, 144), (48, 48))
			self.tank_1 = self.tank.subsurface((48, 144), (48, 48))
			if self.rect.right &gt; 630 - 3:
				self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
				self.direction_x, self.direction_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
				is_move = False
		else:
			raise ValueError('enemyTank class -&gt; direction value error.')
		if pygame.sprite.spritecollide(self, brickGroup, False, None) \
			or pygame.sprite.spritecollide(self, ironGroup, False, None) \
			or pygame.sprite.spritecollide(self, tankGroup, False, None):
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			self.direction_x, self.direction_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
			is_move = False
		if pygame.sprite.collide_rect(self, myhome):
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			self.direction_x, self.direction_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
			is_move = False
		return is_move
	# 重新载入坦克
	def reload(self):
		self.tank = pygame.image.load(self.tanks[self.kind][self.color]).convert_alpha()
		self.tank_0 = self.tank.subsurface((0, 48), (48, 48))
		self.tank_1 = self.tank.subsurface((48, 48), (48, 48))

```

➢ **子弹实现代码**

```
# 子弹类
import pygame

# 子弹类
class Bullet(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		# 子弹四个方向(上下左右)
		self.bullets = ['images/bullet/bullet_up.png', 'images/bullet/bullet_down.png', 'images/bullet/bullet_left.png', 'images/bullet/bullet_right.png']
		# 子弹方向(默认向上)
		self.direction_x, self.direction_y = 0, -1
		self.bullet = pygame.image.load(self.bullets[0])
		self.rect = self.bullet.get_rect()
		# 在坦克类中再赋实际值
		self.rect.left, self.rect.right = 0, 0
		# 速度
		self.speed = 6
		# 是否存活
		self.being = False
		# 是否为加强版子弹(可碎钢板)
		self.stronger = False
	# 改变子弹方向
	def turn(self, direction_x, direction_y):
		self.direction_x, self.direction_y = direction_x, direction_y
		if self.direction_x == 0 and self.direction_y == -1:
			self.bullet = pygame.image.load(self.bullets[0])
		elif self.direction_x == 0 and self.direction_y == 1:
			self.bullet = pygame.image.load(self.bullets[1])
		elif self.direction_x == -1 and self.direction_y == 0:
			self.bullet = pygame.image.load(self.bullets[2])
		elif self.direction_x == 1 and self.direction_y == 0:
			self.bullet = pygame.image.load(self.bullets[3])
		else:
			raise ValueError('Bullet class -&gt; direction value error.')
	# 移动
	def move(self):
		self.rect = self.rect.move(self.speed*self.direction_x, self.speed*self.direction_y)
		# 到地图边缘后消失
		if (self.rect.top &lt; 3) or (self.rect.bottom &gt; 630 - 3) or (self.rect.left &lt; 3) or (self.rect.right &gt; 630 - 3):
			self.being = False

```

➢ **食物实现代码**

```
# 食物类
import pygame
import random

# 食物类, 用于提升坦克能力
class Food(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		# 消灭当前所有敌人
		self.food_boom = 'images/food/food_boom.png'
		# 当前所有敌人静止一段时间
		self.food_clock = 'images/food/food_clock.png'
		# 使得坦克子弹可碎钢板
		self.food_gun = 'images/food/food_gun.png'
		# 使得大本营的墙变为钢板
		self.food_iron = 'images/food/food_gun.png'
		# 坦克获得一段时间的保护罩
		self.food_protect = 'images/food/food_protect.png'
		# 坦克升级
		self.food_star = 'images/food/food_star.png'
		# 坦克生命+1
		self.food_tank = 'images/food/food_tank.png'
		# 所有食物
		self.foods = [self.food_boom, self.food_clock, self.food_gun, self.food_iron, self.food_protect, self.food_star, self.food_tank]
		self.kind = None
		self.food = None
		self.rect = None
		# 是否存在
		self.being = False
		# 存在时间
		self.time = 1000
	# 生成食物
	def generate(self):
		self.kind = random.randint(0, 6)
		self.food = pygame.image.load(self.foods[self.kind]).convert_alpha()
		self.rect = self.food.get_rect()
		self.rect.left, self.rect.top = random.randint(100, 500), random.randint(100, 500)
		self.being = True

```

➢ **大本营实现代码**

```
# 大本营类
import pygame

# 大本营类
class Home(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.homes = ['images/home/home1.png', 'images/home/home2.png', 'images/home/home_destroyed.png']
		self.home = pygame.image.load(self.homes[0])
		self.rect = self.home.get_rect()
		self.rect.left, self.rect.top = (3 + 12 * 24, 3 + 24 * 24)
		self.alive = True
	# 大本营置为摧毁状态
	def set_dead(self):
		self.home = pygame.image.load(self.homes[-1])
		self.alive = False

```

➢ **启动类实现代码**

```
import sys
import pygame
from BattleCity import scene, tank, home, food

def show_start_interface(screen, width, height):
	tfont = pygame.font.Font('font/simkai.ttf', width//5)
	cfont = pygame.font.Font('font/simkai.ttf', width//20)
	title = tfont.render(u'TANK', True, (255, 0, 0))
	content1 = cfont.render(u'1 PLAYER（按1）', True, (0, 0, 255))
	content2 = cfont.render(u'2 PLAYER（按2）', True, (0, 0, 255))
	trect = title.get_rect()
	trect.midtop = (width/2, height/5)
	crect1 = content1.get_rect()
	crect1.midtop = (width/2, height/1.8)
	crect2 = content2.get_rect()
	crect2.midtop = (width/2, height/1.6)
	screen.blit(title, trect)
	screen.blit(content1, crect1)
	screen.blit(content2, crect2)
	pygame.display.update()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					return 1
				if event.key == pygame.K_2:
					return 2
# 结束界面显示
def show_end_interface(screen, width, height, is_win):
	bg_img = pygame.image.load("images/others/background.png")
	screen.blit(bg_img, (0, 0))
	if is_win:
		font = pygame.font.Font('font/simkai.ttf', width//10)
		content = font.render(u'恭喜通关！', True, (255, 0, 0))
		rect = content.get_rect()
		rect.midtop = (width/2, height/2)
		screen.blit(content, rect)
	else:
		fail_img = pygame.image.load("images/others/gameover.png")
		rect = fail_img.get_rect()
		rect.midtop = (width/2, height/2)
		screen.blit(fail_img, rect)
	pygame.display.update()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
# 关卡切换
def show_switch_stage(screen, width, height, stage):
	bg_img = pygame.image.load("images/others/background.png")
	screen.blit(bg_img, (0, 0))
	font = pygame.font.Font('font/simkai.ttf', width//10)
	content = font.render(u'第%d关' % stage, True, (0, 255, 0))
	rect = content.get_rect()
	rect.midtop = (width/2, height/2)
	screen.blit(content, rect)
	pygame.display.update()
	delay_event = pygame.constants.USEREVENT
	pygame.time.set_timer(delay_event, 1000)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == delay_event:
				return
def main():
	# 初始化
	pygame.init()
	pygame.mixer.init()
	screen = pygame.display.set_mode((630, 630))
	pygame.display.set_caption("TANK")
	# 加载图片
	bg_img = pygame.image.load("images/others/background.png")
	# 加载音效
	add_sound = pygame.mixer.Sound("audios/add.wav")
	add_sound.set_volume(1)
	bang_sound = pygame.mixer.Sound("audios/bang.wav")
	bang_sound.set_volume(1)
	blast_sound = pygame.mixer.Sound("audios/blast.wav")
	blast_sound.set_volume(1)
	fire_sound = pygame.mixer.Sound("audios/fire.wav")
	fire_sound.set_volume(1)
	Gunfire_sound = pygame.mixer.Sound("audios/Gunfire.wav")
	Gunfire_sound.set_volume(1)
	hit_sound = pygame.mixer.Sound("audios/hit.wav")
	hit_sound.set_volume(1)
	start_sound = pygame.mixer.Sound("audios/start.wav")
	start_sound.set_volume(1)
	# 开始界面
	num_player = show_start_interface(screen, 630, 630)
	# 播放游戏开始的音乐
	start_sound.play()
	# 关卡
	stage = 0
	num_stage = 2
	# 游戏是否结束
	is_gameover = False
	# 时钟
	clock = pygame.time.Clock()
	# 主循环
	while not is_gameover:
		# 关卡
		stage += 1
		if stage &gt; num_stage:
			break
		show_switch_stage(screen, 630, 630, stage)
		# 该关卡坦克总数量
		enemytanks_total = min(stage * 12, 60)
		# 场上存在的敌方坦克总数量
		enemytanks_now = 0
		# 场上可以存在的敌方坦克总数量
		enemytanks_now_max = min(max(stage * 2, 4), 8)
		# 精灵组
		tanksGroup = pygame.sprite.Group()
		mytanksGroup = pygame.sprite.Group()
		enemytanksGroup = pygame.sprite.Group()
		bulletsGroup = pygame.sprite.Group()
		mybulletsGroup = pygame.sprite.Group()
		enemybulletsGroup = pygame.sprite.Group()
		myfoodsGroup = pygame.sprite.Group()
		# 自定义事件
		# 	-生成敌方坦克事件
		genEnemyEvent = pygame.constants.USEREVENT + 0
		pygame.time.set_timer(genEnemyEvent, 100)
		# 	-敌方坦克静止恢复事件
		recoverEnemyEvent = pygame.constants.USEREVENT + 1
		pygame.time.set_timer(recoverEnemyEvent, 8000)
		# 	-我方坦克无敌恢复事件
		noprotectMytankEvent = pygame.constants.USEREVENT + 2
		pygame.time.set_timer(noprotectMytankEvent, 8000)
		# 关卡地图
		map_stage = scene.Map(stage)
		# 我方坦克
		tank_player1 = tank.myTank(1)
		tanksGroup.add(tank_player1)
		mytanksGroup.add(tank_player1)
		if num_player &gt; 1:
			tank_player2 = tank.myTank(2)
			tanksGroup.add(tank_player2)
			mytanksGroup.add(tank_player2)
		is_switch_tank = True
		player1_moving = False
		player2_moving = False
		# 为了轮胎的动画效果
		time = 0
		# 敌方坦克
		for i in range(0, 3):
			if enemytanks_total &gt; 0:
				enemytank = tank.enemyTank(i)
				tanksGroup.add(enemytank)
				enemytanksGroup.add(enemytank)
				enemytanks_now += 1
				enemytanks_total -= 1
		# 大本营
		myhome = home.Home()
		# 出场特效
		appearance_img = pygame.image.load("images/others/appear.png").convert_alpha()
		appearances = []
		appearances.append(appearance_img.subsurface((0, 0), (48, 48)))
		appearances.append(appearance_img.subsurface((48, 0), (48, 48)))
		appearances.append(appearance_img.subsurface((96, 0), (48, 48)))
		# 关卡主循环
		while True:
			if is_gameover is True:
				break
			if enemytanks_total &lt; 1 and enemytanks_now &lt; 1:
				is_gameover = False
				break
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == genEnemyEvent:
					if enemytanks_total &gt; 0:
						if enemytanks_now &lt; enemytanks_now_max:
							enemytank = tank.enemyTank()
							if not pygame.sprite.spritecollide(enemytank, tanksGroup, False, None):
								tanksGroup.add(enemytank)
								enemytanksGroup.add(enemytank)
								enemytanks_now += 1
								enemytanks_total -= 1
				if event.type == recoverEnemyEvent:
					for each in enemytanksGroup:
						each.can_move = True
				if event.type == noprotectMytankEvent:
					for each in mytanksGroup:
						mytanksGroup.protected = False
			# 检查用户键盘操作
			key_pressed = pygame.key.get_pressed()
			# 玩家一
			if key_pressed[pygame.K_w]:
				tanksGroup.remove(tank_player1)
				tank_player1.move_up(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myhome)
				tanksGroup.add(tank_player1)
				player1_moving = True
			elif key_pressed[pygame.K_s]:
				tanksGroup.remove(tank_player1)
				tank_player1.move_down(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myhome)
				tanksGroup.add(tank_player1)
				player1_moving = True
			elif key_pressed[pygame.K_a]:
				tanksGroup.remove(tank_player1)
				tank_player1.move_left(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myhome)
				tanksGroup.add(tank_player1)
				player1_moving = True
			elif key_pressed[pygame.K_d]:
				tanksGroup.remove(tank_player1)
				tank_player1.move_right(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myhome)
				tanksGroup.add(tank_player1)
				player1_moving = True
			elif key_pressed[pygame.K_j]:
				if not tank_player1.bullet.being:
					fire_sound.play()
					tank_player1.shoot()
			# 玩家二
			if num_player &gt; 1:
				if key_pressed[pygame.K_UP]:
					tanksGroup.remove(tank_player2)
					tank_player2.move_up(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myhome)
					tanksGroup.add(tank_player2)
					player2_moving = True
				elif key_pressed[pygame.K_DOWN]:
					tanksGroup.remove(tank_player2)
					tank_player2.move_down(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myhome)
					tanksGroup.add(tank_player2)
					player2_moving = True
				elif key_pressed[pygame.K_LEFT]:
					tanksGroup.remove(tank_player2)
					tank_player2.move_left(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myhome)
					tanksGroup.add(tank_player2)
					player2_moving = True
				elif key_pressed[pygame.K_RIGHT]:
					tanksGroup.remove(tank_player2)
					tank_player2.move_right(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myhome)
					tanksGroup.add(tank_player2)
					player2_moving = True
				elif key_pressed[pygame.K_0]:
					if not tank_player2.bullet.being:
						fire_sound.play()
						tank_player2.shoot()
			# 背景
			screen.blit(bg_img, (0, 0))
			# 石头墙
			for each in map_stage.brickGroup:
				screen.blit(each.brick, each.rect)
			# 钢墙
			for each in map_stage.ironGroup:
				screen.blit(each.iron, each.rect)
			# 冰
			for each in map_stage.iceGroup:
				screen.blit(each.ice, each.rect)
			# 河流
			for each in map_stage.riverGroup:
				screen.blit(each.river, each.rect)
			# 树
			for each in map_stage.treeGroup:
				screen.blit(each.tree, each.rect)
			time += 1
			if time == 5:
				time = 0
				is_switch_tank = not is_switch_tank
			# 我方坦克
			if tank_player1 in mytanksGroup:
				if is_switch_tank and player1_moving:
					screen.blit(tank_player1.tank_0, (tank_player1.rect.left, tank_player1.rect.top))
					player1_moving = False
				else:
					screen.blit(tank_player1.tank_1, (tank_player1.rect.left, tank_player1.rect.top))
				if tank_player1.protected:
					screen.blit(tank_player1.protected_mask1, (tank_player1.rect.left, tank_player1.rect.top))
			if num_player &gt; 1:
				if tank_player2 in mytanksGroup:
					if is_switch_tank and player2_moving:
						screen.blit(tank_player2.tank_0, (tank_player2.rect.left, tank_player2.rect.top))
						player1_moving = False
					else:
						screen.blit(tank_player2.tank_1, (tank_player2.rect.left, tank_player2.rect.top))
					if tank_player2.protected:
						screen.blit(tank_player1.protected_mask1, (tank_player2.rect.left, tank_player2.rect.top))
			# 敌方坦克
			for each in enemytanksGroup:
				# 出生特效
				if each.born:
					if each.times &gt; 0:
						each.times -= 1
						if each.times &lt;= 10:
							screen.blit(appearances[2], (3+each.x*12*24, 3))
						elif each.times &lt;= 20:
							screen.blit(appearances[1], (3+each.x*12*24, 3))
						elif each.times &lt;= 30:
							screen.blit(appearances[0], (3+each.x*12*24, 3))
						elif each.times &lt;= 40:
							screen.blit(appearances[2], (3+each.x*12*24, 3))
						elif each.times &lt;= 50:
							screen.blit(appearances[1], (3+each.x*12*24, 3))
						elif each.times &lt;= 60:
							screen.blit(appearances[0], (3+each.x*12*24, 3))
						elif each.times &lt;= 70:
							screen.blit(appearances[2], (3+each.x*12*24, 3))
						elif each.times &lt;= 80:
							screen.blit(appearances[1], (3+each.x*12*24, 3))
						elif each.times &lt;= 90:
							screen.blit(appearances[0], (3+each.x*12*24, 3))
					else:
						each.born = False
				else:
					if is_switch_tank:
						screen.blit(each.tank_0, (each.rect.left, each.rect.top))
					else:
						screen.blit(each.tank_1, (each.rect.left, each.rect.top))
					if each.can_move:
						tanksGroup.remove(each)
						each.move(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myhome)
						tanksGroup.add(each)
			# 我方子弹
			for tank_player in mytanksGroup:
				if tank_player.bullet.being:
					tank_player.bullet.move()
					screen.blit(tank_player.bullet.bullet, tank_player.bullet.rect)
					# 子弹碰撞敌方子弹
					for each in enemybulletsGroup:
						if each.being:
							if pygame.sprite.collide_rect(tank_player.bullet, each):
								tank_player.bullet.being = False
								each.being = False
								enemybulletsGroup.remove(each)
								break
						else:
							enemybulletsGroup.remove(each)	
					# 子弹碰撞敌方坦克
					for each in enemytanksGroup:
						if each.being:
							if pygame.sprite.collide_rect(tank_player.bullet, each):
								if each.is_red == True:
									myfood = food.Food()
									myfood.generate()
									myfoodsGroup.add(myfood)
									each.is_red = False
								each.blood -= 1
								each.color -= 1
								if each.blood &lt; 0:
									bang_sound.play()
									each.being = False
									enemytanksGroup.remove(each)
									enemytanks_now -= 1
									tanksGroup.remove(each)
								else:
									each.reload()
								tank_player.bullet.being = False
								break
						else:
							enemytanksGroup.remove(each)
							tanksGroup.remove(each)
					# 子弹碰撞石头墙
					if pygame.sprite.spritecollide(tank_player.bullet, map_stage.brickGroup, True, None):
						tank_player.bullet.being = False
					'''
					# 等价方案(更科学点)
					for each in map_stage.brickGroup:
						if pygame.sprite.collide_rect(tank_player.bullet, each):
							tank_player.bullet.being = False
							each.being = False
							map_stage.brickGroup.remove(each)
							break
					'''
					# 子弹碰钢墙
					if tank_player.bullet.stronger:
						if pygame.sprite.spritecollide(tank_player.bullet, map_stage.ironGroup, True, None):
							tank_player.bullet.being = False
					else:
						if pygame.sprite.spritecollide(tank_player.bullet, map_stage.ironGroup, False, None):
							tank_player.bullet.being = False
					'''
					# 等价方案(更科学点)
					for each in map_stage.ironGroup:
						if pygame.sprite.collide_rect(tank_player.bullet, each):
							tank_player.bullet.being = False
							if tank_player.bullet.stronger:
								each.being = False
								map_stage.ironGroup.remove(each)
							break
					'''
					# 子弹碰大本营
					if pygame.sprite.collide_rect(tank_player.bullet, myhome):
						tank_player.bullet.being = False
						myhome.set_dead()
						is_gameover = True
			# 敌方子弹
			for each in enemytanksGroup:
				if each.being:
					if each.can_move and not each.bullet.being:
						enemybulletsGroup.remove(each.bullet)
						each.shoot()
						enemybulletsGroup.add(each.bullet)
					if not each.born:
						if each.bullet.being:
							each.bullet.move()
							screen.blit(each.bullet.bullet, each.bullet.rect)
							# 子弹碰撞我方坦克
							for tank_player in mytanksGroup:
								if pygame.sprite.collide_rect(each.bullet, tank_player):
									if not tank_player.protected:
										bang_sound.play()
										tank_player.life -= 1
										if tank_player.life &lt; 0:
											mytanksGroup.remove(tank_player)
											tanksGroup.remove(tank_player)
											if len(mytanksGroup) &lt; 1:
												is_gameover = True
										else:
											tank_player.reset()
									each.bullet.being = False
									enemybulletsGroup.remove(each.bullet)
									break
							# 子弹碰撞石头墙
							if pygame.sprite.spritecollide(each.bullet, map_stage.brickGroup, True, None):
								each.bullet.being = False
								enemybulletsGroup.remove(each.bullet)
							'''
							# 等价方案(更科学点)
							for one in map_stage.brickGroup:
								if pygame.sprite.collide_rect(each.bullet, one):
									each.bullet.being = False
									one.being = False
									enemybulletsGroup.remove(one)
									break
							'''
							# 子弹碰钢墙
							if each.bullet.stronger:
								if pygame.sprite.spritecollide(each.bullet, map_stage.ironGroup, True, None):
									each.bullet.being = False
							else:
								if pygame.sprite.spritecollide(each.bullet, map_stage.ironGroup, False, None):
									each.bullet.being = False
							'''
							# 等价方案(更科学点)
							for one in map_stage.ironGroup:
								if pygame.sprite.collide_rect(each.bullet, one):
									each.bullet.being = False
									if each.bullet.stronger:
										one.being = False
										map_stage.ironGroup.remove(one)
									break
							'''
							# 子弹碰大本营
							if pygame.sprite.collide_rect(each.bullet, myhome):
								each.bullet.being = False
								myhome.set_dead()
								is_gameover = True
				else:
					enemytanksGroup.remove(each)
					tanksGroup.remove(each)
			# 家
			screen.blit(myhome.home, myhome.rect)
			# 食物
			for myfood in myfoodsGroup:
				if myfood.being and myfood.time &gt; 0:
					screen.blit(myfood.food, myfood.rect)
					myfood.time -= 1
					for tank_player in mytanksGroup:
						if pygame.sprite.collide_rect(tank_player, myfood):
							# 消灭当前所有敌人
							if myfood.kind == 0:
								for _ in enemytanksGroup:
									bang_sound.play()
								enemytanksGroup = pygame.sprite.Group()
								enemytanks_total -= enemytanks_now
								enemytanks_now = 0
							# 敌人静止
							if myfood.kind == 1:
								for each in enemytanksGroup:
									each.can_move = False
							# 子弹增强
							if myfood.kind == 2:
								add_sound.play()
								tank_player.bullet.stronger = True
							# 使得大本营的墙变为钢板
							if myfood.kind == 3:
								map_stage.protect_home()
							# 坦克获得一段时间的保护罩
							if myfood.kind == 4:
								add_sound.play()
								for tank_player in mytanksGroup:
									tank_player.protected = True
							# 坦克升级
							if myfood.kind == 5:
								add_sound.play()
								tank_player.up_level()
							# 坦克生命+1
							if myfood.kind == 6:
								add_sound.play()
								tank_player.life += 1
							myfood.being = False
							myfoodsGroup.remove(myfood)
							break
				else:
					myfood.being = False
					myfoodsGroup.remove(myfood)
			pygame.display.flip()
			clock.tick(60)
	if not is_gameover:
		show_end_interface(screen, 630, 630, True)
	else:
		show_end_interface(screen, 630, 630, False)

if __name__ == '__main__':
	main()

```

以上就是坦克大战实现的主要代码，当然还涉及到一些图片等素材，如果需要**完整实现**，可以关注文末公众号，后台回复 **tank** 免费领取。

<img src="https://img-blog.csdnimg.cn/20191212073821865.png#pic_center" alt="" width="600">
