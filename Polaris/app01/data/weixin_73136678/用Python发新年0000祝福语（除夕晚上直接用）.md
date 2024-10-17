
--- 
title:  用Python发新年00:00祝福语（除夕晚上直接用） 
tags: []
categories: [] 

---
2023年的新年即将来临,这里用Python写一串简单的代码来实现定点给微信里的所有小伙伴发祝福语！！

#### 环境说明

Python版本: 不限

第三方库:　itchat, schedule

**注:所有祝福语来源于网络,代码运行周期较长,最好跑在服务器上**

#### 代码如下



>  
 <pre>#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-12-9 上午9:08
# @Author  : KainHuck
# @Email   : kainhoo2333@gmail.com
# @File    : 元旦祝福.py
import itchat
import random
import schedule
import datetime
import time
# 登录,并暂存登录状态
itchat.auto_login(hotReload=True)
# 获取所有好友信息friends = itchat.get_friends(update=True)
# 筛选掉没有备注名的好友, 并将要发送祝福语的好友放置在一个字典里
final_friends = {}
for each in friends:
    if len(each['RemarkName']) &gt; 0:
        final_friends[each['RemarkName']] = each['UserName']
# 祝福语列表
greeting = ['元旦到了，在辞旧迎新的日子里，我愿为你送走烦恼迎来开心，送走压力迎来健康，送走失意迎来顺利，送走意外迎来平安，并希望你快快乐乐过个元旦节。',            '圆圆的梦想，七色的花;圆圆的</pre>

