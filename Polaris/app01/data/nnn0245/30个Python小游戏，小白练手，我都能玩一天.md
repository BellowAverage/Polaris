
--- 
title:  30个Python小游戏，小白练手，我都能玩一天 
tags: []
categories: [] 

---
大家好，我是雨雨~

今天给大家带来30个py小游戏，一定要收藏！**全部源码都整理好了**

### 有手就行

#### **1、吃金币**

**【有手就行系列不介绍玩法了+附源码】**

 <img alt="" height="303" src="https://img-blog.csdnimg.cn/fa923f2f737949d3a64af3709d299656.png" width="569">

**源码分享：**

```
import os
import cfg
import sys
import pygame
import random
from modules import *
 
 
'''游戏初始化'''
def initGame():
    # 初始化pygame, 设置展示窗口
    pygame.init()
    screen = pygame.display.set_mode(cfg.SCREENSIZE)
    pygame.display.set_caption('catch coins —— 九歌')
    # 加载必要的游戏素材
    game_images = {}
    for key, value in cfg.IMAGE_PATHS.items():
        if isinstance(value, list):
            images = []
            for item in value: images.append(pygame.image.load(item))
            game_images[key] = images
        else:
            game_images[key] = pygame.image.load(value)
    game_sounds = {}
    for key, value in cfg.AUDIO_PATHS.items():
        if key == 'bgm': continue
        game_sounds[key] = pygame.mixer.Sound(value)
    # 返回初始化数据
    return screen, game_images, game_sounds
 
 
'''主函数'''
def main():
    # 初始化
    screen, game_images, game_sounds = initGame()
    # 播放背景音乐
    pygame.mixer.music.load(cfg.AUDIO_PATHS['bgm'])
    pygame.mixer.music.play(-1, 0.0)
    # 字体加载
    font = pygame.font.Font(cfg.FONT_PATH, 40)
    # 定义hero
    hero = Hero(game_images['hero'], position=(375, 520))
    # 定义食物组
    food_sprites_group = pygame.sprite.Group()
    generate_food_freq = random.randint(10, 20)
    generate_food_count = 0
    # 当前分数/历史最高分
    score = 0
    highest_score = 0 if not os.path.exists(cfg.HIGHEST_SCORE_RECORD_FILEPATH) else int(open(cfg.HIGHEST_SCORE_RECORD_FILEPATH).read())
    # 游戏主循环
    clock = pygame.time.Clock()
    while True:
        # --填充背景
        screen.fill(0)
        screen.blit(game_images['background'], (0, 0))
        # --倒计时信息
        countdown_t
```
