
--- 
title:  用python实现背单词的功能（python3经典编程案例） 
tags: []
categories: [] 

---
1、新建文件：words.txt，内容如下：

```
a copy of				一份，一本
account		[ə'kaʊnt]		n. 账户；账单
age		[eɪdʒ]		n. 年龄
Anaconda	[ˌænəˈkɒndə]	n. 水蟒；蟒蛇
args				n. [计算机]参数
arguments	['ɑːgjʊm(ə)nts]	n. 参数
array		[əˈreɪ]		n. 数组，阵列；排列，列阵
attributes	['ætrə,bjʊt]	n. 属性（attribute的复数）
audience		['ɔːdɪəns]		n. 观众；听众
available		[əˈveɪləbl]	adj. 可获得的；可购得的
axis		[ˈæksɪs]		n. 轴；轴线；轴心国
centers				n. 中心，中央
coef				abbr. 系数；折算率
columns		[ˈkɒləms]		列
ctrl		[kən'trəʊl]	n. 计算机的Ctrl按键（控制键）

```

2、同目录下新建python文件：

```
# -*- encoding: utf-8 -*-
import tkinter as tk
import time
import threading
import random

window = tk.Tk()
window.title('06_轻松背单词')
window.geometry('640x765')
window.flag = True

# 设置label1背景为图片
# image_file = tk.PhotoImage(file='bg.png')
# label1 = tk.Label(window, text='', font=("黑体", 60, "normal"), compound='center', image=image_file)

label1 = tk.Label(window, text='', font=("黑体", 60, "normal"), compound='center')
label2 = tk.Label(window, text='', font=("黑体", 15, "normal"))
label1.pack()
label2.place(x=230, y=430)
words = []
with open('words.txt', 'r', encoding='utf-8') as f:
    for s in f.readlines():
        words.append(s)


def autoChange():
    """定义自动切换单词的方法"""
    window.flag = True
    while window.flag:
        i = random.randint(0, len(words) - 1)  # 随机显示单词
        a = words[i].split()  # 文本分割为列表
        b1 = a[0:1]  # 第1列单词
        b2 = a[2:4]  # 第2、3列音标和解释
        # label组件显示文本
        label1['text'] = b1
        label2['text'] = b2
        time.sleep(1)


if __name__ == '__main__':
    # 用线程控制自动切换单词
    t = threading.Thread(target=autoChange)
    t.start()
    window.mainloop()
    window.flag = False


```
