
--- 
title:  【uiautomation】获取微信好友名单，可指定标签 & 全部 
tags: []
categories: [] 

---
## 前言

>  
 接到了一个需求：现微信有8000+好友，需要给所有好友发送一则一样的消息。网上搜索一番后，发现`uiautomation` 可以解决该需求，遂有此文。这是第一篇，获取全部好友 


代码在文章末尾，自取~ 更多功能的微信群发消息代码链接 ：

## 知识点📖

|知识点|链接
|------
|Microsoft 的 **uiautomation**|
|Python 的 **uiautomation**|
|微信群发消息 GitHub链接|

## 代码实现

>  
 Windows系统微信客户端 


这里使用了一个测试的微信，全部好友为 `354`，标签为`高中同学`的好友为 `68`，下面用代码去获取它们！

<img src="https://img-blog.csdnimg.cn/cc781736506244b2bccdfd0349e3beb7.png" alt="在这里插入图片描述">

代码运行如下：

获取标签为`高中同学`的名单如下
- <img src="https://img-blog.csdnimg.cn/e763b901eabe4d96bd84f0d87abea353.png" alt="在这里插入图片描述">
获取全部好友：
- 有两个好友是重名的，去重后就会了一个人（后面再优化重名这个问题 <img src="https://img-blog.csdnimg.cn/196dcdd824e54e1581879067f11d04ad.png" alt="在这里插入图片描述">
## 完整代码

```
# -*- coding: utf-8 -*-
# @Author : Frica01
# @Time   : 2022-09-10 15:39
# @Name   : wechat_operation.py

import time
import uiautomation as auto

wx_window = auto.WindowControl(Name='微信', ClassName='WeChatMainWndForPC')


def get_friend_list(tag: str = None, num: int = 10) -&gt; list:
    """
    获取微好友名称.

    Args:
        tag(str): 可选参数，如不指定，则获取所有好友
        num(int): 可选参数，如不指定，只获取10页好友

    Returns:
        list
    """

    def click_tag():
        """点击标签"""
        contacts_window.ButtonControl(Name="标签").Click()

    auto.SendKeys(text='{Alt}{Ctrl}w')  # 快捷键唤醒微信
    # 点击 通讯录管理
    wx_window.ButtonControl(Name="通讯录").Click()
    wx_window.ListControl(Name="联系人").ButtonControl(Name="通讯录管理").Click()
    contacts_window = auto.GetForegroundControl()  # 切换到通讯录管理，相当于切换到弹出来的页面

    if tag:
        click_tag()  # 点击标签
        contacts_window.PaneControl(Name=tag).Click()
        time.sleep(0.3)
        click_tag()  # 关闭标签

    # 获取滑动模式
    scroll = contacts_window.ListControl().GetScrollPattern()
    assert scroll, "没有可滑动对象"
    name_list = list()
    rate: int = int(float(102000 / num))  # 根据输入的num计算滑动的步长
    for pct in range(0, 102000, rate):  # range不支持float，不导入numpy库，采取迂回这的方式
        # 每次滑动一点点，-1代表不用滑动
        scroll.SetScrollPercent(horizontalPercent=-1, verticalPercent=pct / 100000)
        for name_node in contacts_window.ListControl().GetChildren():  # 获取当前页面的 列表 -&gt; 子节点
            nick_name = name_node.TextControl().Name  # 用户名
            remark_name = name_node.ButtonControl(foundIndex=2).Name  # 用户备注名，索引1会错位，索引2是备注名，索引3是标签名
            name_list.append(remark_name if remark_name else nick_name)
    contacts_window.SendKey(auto.SpecialKeyNames['ESC'])  # 结束时候关闭 "通讯录管理" 窗口
    return list(set(name_list))  # 简单去重，但是存在误判（如果存在同名的好友


```

## 后话

如果看不懂代码，可以在下方留言~ see you.🎈🎈
