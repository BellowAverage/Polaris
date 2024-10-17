
--- 
title:  用 Python 写个扫雷小游戏 
tags: []
categories: [] 

---
扫雷是一款益智类小游戏，最早于 1992 年由微软在 Windows 上发行，游戏适合于全年龄段，规则简单，即在最短的时间内找出所有非雷格子且在中间过程中不能踩到雷， 踩到雷则失败，需重新开始。

本文我们使用 Python 来实现扫雷游戏，主要用的 Python 库是 pygame。

### 实现

游戏组成比较简单，主要包括：小方格、计时器、地雷等。

首先，我们初始化一些常量，比如：横竖方块数、地雷数、鼠标点击情况等，如下所示：

```
BLOCK_WIDTH = 30
BLOCK_HEIGHT = 16
# 块大小
SIZE = 20
# 地雷数
MINE_COUNT = 66
# 未点击
normal = 1
# 已点击
opened = 2
# 地雷
mine = 3
# 标记为地雷
flag = 4
# 标记为问号
ask = 5
# 踩中地雷
bomb = 6
# 被双击的周围
hint = 7
# 正被鼠标左右键双击
double = 8
readied = 1,
started = 2,
over = 3,
win = 4

```

接着定义一个地雷类，类中定义一些基本属性（如：坐标、状态等）及 get、set 方法，代码实现如下：

```
class Mine:
    def __init__(self, x, y, value=0):
        self._x = x
        self._y = y
        self._value = 0
        self._around_mine_count = -1
        self._status = normal
        self.set_value(value)
    def __repr__(self):
        return str(self._value)
    def get_x(self):
        return self._x
    def set_x(self, x):
        self._x = x
    x = property(fget=get_x, fset=set_x)
    def get_y(self):
        return self._y
    def set_y(self, y):
        self._y = y
    y = property(fget=get_y, fset=set_y)
    def get_value(self):
        return self._value
    def set_value(self, value):
        if value:
            self._value = 1
        else:
            self._value = 0
    value = property(fget=get_value, fset=set_value, doc='0:非地雷 1:雷')
    def get_around_mine_count(self):
        return self._around_mine_count
    def set_around_mine_count(self, around_mine_count):
        self._around_mine_count = around_mine_count
    around_mine_count = property(fget=get_around_mine_count, fset=set_around_mine_count, doc='四周地雷数量')
    def get_status(self):
        return self._status
    def set_status(self, value):
        self._status = value
    status = property(fget=get_status, fset=set_status, doc='BlockStatus')

```

再接着定义一个 MineBlock 类，用来处理扫雷的基本逻辑，代码实现如下：

```
class MineBlock:
    def __init__(self):
        self._block = [[Mine(i, j) for i in range(BLOCK_WIDTH)] for j in range(BLOCK_HEIGHT)]
        # 埋雷
        for i in random.sample(range(BLOCK_WIDTH * BLOCK_HEIGHT), MINE_COUNT):
            self._block[i // BLOCK_WIDTH][i % BLOCK_WIDTH].value = 1
    def get_block(self):
        return self._block
    block = property(fget=get_block)
    def getmine(self, x, y):
        return self._block[y][x]
    def open_mine(self, x, y):
        # 踩到雷了
        if self._block[y][x].value:
            self._block[y][x].status = bomb
            return False
        # 先把状态改为 opened
        self._block[y][x].status = opened
        around = _get_around(x, y)
        _sum = 0
        for i, j in around:
            if self._block[j][i].value:
                _sum += 1
        self._block[y][x].around_mine_count = _sum
        # 如果周围没有雷，那么将周围 8 个未中未点开的递归算一遍
        if _sum == 0:
            for i, j in around:
                if self._block[j][i].around_mine_count == -1:
                    self.open_mine(i, j)
        return True
    def double_mouse_button_down(self, x, y):
        if self._block[y][x].around_mine_count == 0:
            return True
        self._block[y][x].status = double
        around = _get_around(x, y)
        # 周围被标记的雷数量
        sumflag = 0
        for i, j in _get_around(x, y):
            if self._block[j][i].status == flag:
                sumflag += 1
        # 周边的雷已经全部被标记
        result = True
        if sumflag == self._block[y][x].around_mine_count:
            for i, j in around:
                if self._block[j][i].status == normal:
                    if not self.open_mine(i, j):
                        result = False
        else:
            for i, j in around:
                if self._block[j][i].status == normal:
                    self._block[j][i].status = hint
        return result
    def double_mouse_button_up(self, x, y):
        self._block[y][x].status = opened
        for i, j in _get_around(x, y):
            if self._block[j][i].status == hint:
                self._block[j][i].status = normal

```

我们接下来初始化界面，首先生成由小方格组成的面板，主要代码实现如下：

```
for row in block.block:
	for mine in row:
		pos = (mine.x * SIZE, (mine.y + 2) * SIZE)
		if mine.status == opened:
			screen.blit(img_dict[mine.around_mine_count], pos)
			opened_count += 1
		elif mine.status == double:
			screen.blit(img_dict[mine.around_mine_count], pos)
		elif mine.status == bomb:
			screen.blit(img_blood, pos)
		elif mine.status == flag:
			screen.blit(img_flag, pos)
			flag_count += 1
		elif mine.status == ask:
			screen.blit(img_ask, pos)
		elif mine.status == hint:
			screen.blit(img0, pos)
		elif game_status == over and mine.value:
			screen.blit(img_mine, pos)
		elif mine.value == 0 and mine.status == flag:
			screen.blit(img_error, pos)
		elif mine.status == normal:
			screen.blit(img_blank, pos)

```

看一下效果： <img src="https://img-blog.csdnimg.cn/img_convert/95b2afe1ef911ee1e83ffd4cb24ba044.png" alt=""> 再接着添加面板的 head 部分，包括：显示雷数、重新开始按钮（笑脸）、显示耗时，主要代码实现如下：

```
print_text(screen, font1, 30, (SIZE * 2 - fheight) // 2 - 2, '%02d' % (MINE_COUNT - flag_count), red)
if game_status == started:
	elapsed_time = int(time.time() - start_time)
print_text(screen, font1, SCREEN_WIDTH - fwidth - 30, (SIZE * 2 - fheight) // 2 - 2, '%03d' % elapsed_time, red)
if flag_count + opened_count == BLOCK_WIDTH * BLOCK_HEIGHT:
	game_status = win
if game_status == over:
	screen.blit(img_face_fail, (face_pos_x, face_pos_y))
elif game_status == win:
	screen.blit(img_face_success, (face_pos_x, face_pos_y))
else:
	screen.blit(img_face_normal, (face_pos_x, face_pos_y))

```

看一下效果： <img src="https://img-blog.csdnimg.cn/img_convert/ad5b350f03e86bdf7f48b6a800d6ae87.png" alt=""> 再接着添加各种点击事件，代码实现如下：

```
for event in pygame.event.get():
	if event.type == QUIT:
		sys.exit()
	elif event.type == MOUSEBUTTONDOWN:
		mouse_x, mouse_y = event.pos
		x = mouse_x // SIZE
		y = mouse_y // SIZE - 2
		b1, b2, b3 = pygame.mouse.get_pressed()
		if game_status == started:
			# 鼠标左右键同时按下，如果已经标记了所有雷，则打开周围一圈；如果还未标记完所有雷，则有一个周围一圈被同时按下的效果
			if b1 and b3:
				mine = block.getmine(x, y)
				if mine.status == opened:
					if not block.double_mouse_button_down(x, y):
						game_status = over
	elif event.type == MOUSEBUTTONUP:
		if y &lt; 0:
			if face_pos_x &lt;= mouse_x &lt;= face_pos_x + face_size \
					and face_pos_y &lt;= mouse_y &lt;= face_pos_y + face_size:
				game_status = readied
				block = MineBlock()
				start_time = time.time()
				elapsed_time = 0
				continue
		if game_status == readied:
			game_status = started
			start_time = time.time()
			elapsed_time = 0
		if game_status == started:
			mine = block.getmine(x, y)
			# 按鼠标左键
			if b1 and not b3:
				if mine.status == normal:
					if not block.open_mine(x, y):
						game_status = over
			# 按鼠标右键
			elif not b1 and b3:
				if mine.status == normal:
					mine.status = flag
				elif mine.status == flag:
					mine.status = ask
				elif mine.status == ask:
					mine.status = normal
			elif b1 and b3:
				if mine.status == double:
					block.double_mouse_button_up(x, y)

```

我们来看一下最终实现效果： <img src="https://img-blog.csdnimg.cn/img_convert/646ea1e990b44c374ad9d0a69c291dd3.gif" alt="">

### 总结

本文我们通过 Python 简单的实现了扫雷游戏，大家有兴趣的话，可以实际操作一下，看看自己能否排除全部的雷。

源码在公号 **Python小二** 后台回复 **201019** 获取。

>  
 本文非首发于个人号 

