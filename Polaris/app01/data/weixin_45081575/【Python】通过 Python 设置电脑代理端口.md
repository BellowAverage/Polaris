
--- 
title:  【Python】通过 Python 设置电脑代理端口 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/6c9fab8202af48ccadd30ea43c60b41a.png" alt="在这里插入图片描述">

## 前言

>  
 前段时间帮朋友做某视频号的视频采集，需要设置电脑的代理端口去拦截指定数据。所以在每次运行程序时候都需要手动开启电脑的代理端口，朋友跟我吐槽说程序运行起来很麻烦。遂有此文。 


## 念念碎

无论`百度`还是`必应`搜索：**`Python 设置电脑代理端口`**，出来的结果，都是牛头不搭马嘴。
- 上图为百度搜索，下图为必应搜索
<img src="https://img-blog.csdnimg.cn/e73bddd978764763bed4a6b7a72190e0.png" alt="在这里插入图片描述">

<mark>手动分割</mark>

<img src="https://img-blog.csdnimg.cn/3c6d199b97db49849e514443b7394e92.png" alt="在这里插入图片描述">

## 准备工作

看简介，需要修改系统代理，可通过Python模块函数和命令行编程来实现。这个模块可谓是不大不小刚刚好~ 细心的你可能还会发现，它的发布时间是在7年前。 <img src="https://img-blog.csdnimg.cn/42243a511fd449e0bdeb99dfd07697cb.png" alt="在这里插入图片描述">

### **安装模块**

```
pip install winproxy

```

### **食用方法**

#### 命令行编程

<img src="https://img-blog.csdnimg.cn/5776968ac5794b0ebe39f472d4a2378f.png" alt="在这里插入图片描述">

看起来很多东西，但用在修改系统代理上，只需要用到三行命令，如下
- 以下命令在`cmd`命令行执行即可。
```
# 开启电脑代理
winproxy on
# 设置电脑代理 ip:port
winproxy set --all 127.0.0.1:9527
# 关闭电脑代理
winproxy off

```

#### Python API

<img src="https://img-blog.csdnimg.cn/443c4c0fd58b41abb4ab497b7c18fd85.png" alt="在这里插入图片描述">

看起来很多东西，但用在修改系统代理上，只需要用到四行命令，如下
- 以下命令用在`python`行。
```
# 导入模块
from winproxy import ProxySetting

# 实例化类
p = ProxySetting()

# 打开 or 关闭 系统代理
p.enable = True or False

# 设置指定的ip:port
p.server = '0.0.0.0:9527'

# 写入到注册表，可理解为 令修改系统代理生效
p.registry_write()

```

## 代码

**cmd**

```
winproxy on
# 设置电脑代理 ip:port
winproxy set --all 127.0.0.1:9527
# 关闭电脑代理
winproxy off

```

**Python**

```
from winproxy import ProxySetting

p = ProxySetting()


def set_proxy():
    """设置系统代理"""
    p.enable = True
    p.server = '127.0.0.1:9527'
    p.registry_write()


def close_proxy():
    """关闭系统代理"""
    p.enable = False
    p.registry_write()


```

## 后话

经过`winproxy`的点缀，某视频号的视频采集一步到位。朋友赞不绝口！！！ 本次到此结束，有问题请利用强大的搜索引擎，自行解决。
