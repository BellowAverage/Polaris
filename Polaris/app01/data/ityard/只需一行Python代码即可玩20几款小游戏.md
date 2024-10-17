
--- 
title:  只需一行Python代码即可玩20几款小游戏 
tags: []
categories: [] 

---
今天分享一个有趣的 github 项目：`https://github.com/kingser/free-python-games`，通过该项目，我们只需一行代码即可玩 20 几款小游戏，下面具体来看一下。

### 安装

首先，我们进行安装，安装很简单，只需一行命令即可：`pip install freegames`。

### 使用

安装完成之后，我们使用命令：`python -m freegames list`查看一下可玩的游戏列表，如下所示：

```
ant
bagels
bounce
cannon
connect
crypto
fidget
flappy
guess
life
madlibs
maze
memory
minesweeper
pacman
paint
pong
simonsays
snake
tictactoe
tiles
tron

```

小游戏的运行(启动)使用命令：`python -m freegames.游戏名`，下面通过示例具体看一下。

```
python -m freegames.snake

```

<img src="https://img-blog.csdnimg.cn/img_convert/44da77b5e036bcbf1cbe1bf2eda96a18.gif" alt="">

```
python -m freegames.pacman

```

<img src="https://img-blog.csdnimg.cn/img_convert/a183fc152f91ccfeb0140ac6b68e265c.gif" alt="">

```
python -m freegames.flappy

```

[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-JQf84Noc-1653304382849)(https://files.mdnice.com/user/4201/6978795a-d0b0-468a-9dea-a26bd513b311.gif)]

```
python -m freegames.connect

```

<img src="https://img-blog.csdnimg.cn/img_convert/d4855d6cc08c5f04672f6c7c2950482a.gif" alt="">

```
python -m freegames.cannon

```

<img src="https://img-blog.csdnimg.cn/img_convert/857c42e9f85100a71faf6096f487fafe.gif" alt="">

```
python -m freegames.memory

```

[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-ceYzZkBS-1653304382852)(https://files.mdnice.com/user/4201/5345ac91-ee32-48f7-8710-f65186890ce7.gif)]

```
python -m freegames.pong

```

<img src="https://img-blog.csdnimg.cn/img_convert/d13bb4a3d24474b078a8d6cd22f6efb3.gif" alt="">

```
python -m freegames.simonsays

```

<img src="https://img-blog.csdnimg.cn/img_convert/1fd2b0cabfee8b69e3ac972ee59d7d9a.gif" alt="">

```
python -m freegames.tictactoe

```

<img src="https://img-blog.csdnimg.cn/img_convert/a43d6c1a50ee9bb49f7fbce0c698e741.gif" alt="">

```
python -m freegames.tiles

```

<img src="https://img-blog.csdnimg.cn/img_convert/5418a41edd32f62b9d4614499b32a33e.gif" alt="">

```
python -m freegames.tron

```

<img src="https://img-blog.csdnimg.cn/img_convert/f4d9f594bd97c995a825d2e59de0169d.gif" alt="">

```
python -m freegames.life

```

<img src="https://img-blog.csdnimg.cn/img_convert/393b389a21e18966d3a03c10fb696aa8.gif" alt="">

```
python -m freegames.maze

```

<img src="https://img-blog.csdnimg.cn/img_convert/884a9c49607ca83e4c77faf249ca4f96.gif" alt="">

```
python -m freegames.fidget

```

<img src="https://img-blog.csdnimg.cn/img_convert/4856817216806bc1651f52ee57cb7e44.gif" alt="">

好了，这里就不一一列举了，有兴趣的小伙伴可以自己动手试试。
