
--- 
title:  用python实现无限弹窗-五一劳动节快乐 
tags: []
categories: [] 

---
脚本如下，安装好`tkinter`模块可以直接运行。

```
# -*- encoding: utf-8 -*-
"""
@File: 弹窗_五一节快乐.py
@Description: 
"""
import tkinter as tk
import random
import threading
import time


def dow():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    window.title('五一劳动节快乐！    ')
    window.geometry("100x25" + "+" + str(a) + "+" + str(b))
    tk.Label(window,
             text='五一劳动节快乐！',  # 标签的文字
             bg='Red',  # 背景颜色
             font=('楷体', 17),  # 字体和字体大小
             width=15, height=2  # 标签长宽
             ).pack()  # 固定窗口位置
    window.mainloop()


# threads = []
# for i in range(3):  # 需要的弹框数量
#     t = threading.Thread(target=dow)
#     threads.append(t)
#     time.sleep(0.5)
#     threads[i].start()
dow()


# try:
#     run_thread(Store, "tb_store")
# except Exception as e:
#     logger.error(f"出现重大问题:{e}")
#



```
