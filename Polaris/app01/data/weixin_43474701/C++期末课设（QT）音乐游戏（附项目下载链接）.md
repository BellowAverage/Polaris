
--- 
title:  C++期末课设（QT）音乐游戏（附项目下载链接） 
tags: []
categories: [] 

---
### C++期末课设（QT）音乐游戏（含程序设计报告）



### 一. 作业题目

音乐游戏（Rhythm Game）的开发

### 二. 开发软件

Qt 6.5.0

### 三. 课题要求

1)面向对象 2)单元测试 3)模型部分 4)验证

### 四. 主要流程

1．整体流程 实现思路： (1)定义了GameDefine类，负责游戏主要参数的定义 (2)定义了GameControl类，负责游戏主要进程的初始化、运行和控制 (3)定义抽象的虚基类GameScene，成员方法为

```
virtual void LoadScene() = 0;//加载场景
    virtual void LoadPos() = 0;//加载位置
    virtual void AddItem() = 0;//将元素添加到场景中去
    virtual void AddEffect() = 0;//添加效果
    virtual void AddPicture() = 0;//添加图片
    virtual void LoadPushButton() = 0;//加载按钮
    QGraphicsScene *mScene;//游戏场景
    QGraphicsPixmapItem *mBackground;//游戏背景

```

虚析构函数： virtual ~GameScene(){}。 其他类继承关系 <img src="https://img-blog.csdnimg.cn/89ce9be8524a49779adac3af98fb7831.png" alt="在这里插入图片描述">

### 2．主要的场景逻辑和计算算法

（1）场景切换 ①总述： 游戏中一共存在四个场景：开始场景（Start Scene）、主场景（Main Scene）、暂停场景（Stop Scene）、结算场景（End Scene）。场景之间的逻辑关系如下图所示： <img src="https://img-blog.csdnimg.cn/23fc4d69df9c4f4abd5624290d5330f2.png" alt="在这里插入图片描述"> ②开始场景（Start Scene）： 游戏开始时会弹出开始场景： <img src="https://img-blog.csdnimg.cn/72f91f565bff44ae8e125098b9785a0e.png" alt="在这里插入图片描述"> 点击场景中间的开始按钮就会跳转至主场景。 ③主场景（Main Scene）： 主场景是游戏进行的主要场景，在主场景中，会播放谱面，玩家需要根据节奏接住落下的音符。其中四个轨道从左到右分别对应着键盘上的S、D、J、K四个键。玩家需要在音符落到判定线是击打轨道对应的键位，经过判定算法，得出相应的判定。 <img src="https://img-blog.csdnimg.cn/afc5046b96aa4bbf94d7ff11a6134db3.png" alt="在这里插入图片描述"> 按下主场景中的暂停按钮，会跳转到暂停场景；当谱面结束之后，会自动跳转至结算场景。 ④暂停场景（Stop Scene）： 暂停界面中有两个按钮，左侧按钮按下继续游戏，跳转回主场景，中间会给3秒的缓冲时间；右侧按钮按下会直接退出游戏。 <img src="https://img-blog.csdnimg.cn/9eaa0e580c1f47a09e0c7c5880d59931.png" alt="在这里插入图片描述"> 结算场景（End Scene）： <img src="https://img-blog.csdnimg.cn/fa9c08f8c3c14379900d9e3dbcac7357.png" alt="在这里插入图片描述"> 当谱面结束时会自动跳转至结算界面，结算场景包括谱名、分数、最大连击数、准度等信息。

剩下的就不多说啦~ 
