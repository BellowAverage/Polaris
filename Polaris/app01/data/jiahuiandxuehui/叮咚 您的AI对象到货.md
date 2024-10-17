
--- 
title:  叮咚 您的AI对象到货 
tags: []
categories: [] 

---


#### 目录标题
- - - <ul><li>- - <ul><li>- - 


## 一年一度的打狗节

今天大家是来看对象的，我就不废话了。不过可以回顾一下往期样例
- - - 还有就是这个死皮赖脸的打法 <img src="https://img-blog.csdnimg.cn/61c4adbda75e49cd8eba497346b6b0d3.gif" alt="请添加图片描述" height="250">
## 今年搞一个AI对象

### 示例

<img src="https://img-blog.csdnimg.cn/4011dd5ba00d48228748eb1fb82a69d8.png" alt="在这里插入图片描述">

### 源码

用到了之前的经验：

#### api

```
import urllib.request
import re

while True:
    x = input("主人：")
    x = urllib.parse.quote(x)
    link = urllib.request.urlopen(
        "http://nlp.xiaoi.com/robot/webrobot?&amp;callback=__webrobot_processMsg&amp;data=%7B%22sessionId%22%3A%22ff725c236e5245a3ac825b2dd88a7501%22%2C%22robotId%22%3A%22webbot%22%2C%22userId%22%3A%227cd29df3450745fbbdcf1a462e6c58e6%22%2C%22body%22%3A%7B%22content%22%3A%22" + x + "%22%7D%2C%22type%22%3A%22txt%22%7D")
    html_doc = link.read().decode()
    reply_list = re.findall(r'\"content\":\"(.+?)\\r\\n\"', html_doc)
    print("小i：" + reply_list[-1])


```

```

from tkinter import *
import tkinter as tk
import urllib.request
import requests




root = Tk()
root.iconphoto(False,tk.PhotoImage(file='photo/1.ioc'))
root.title("我的野蛮女友")
root.minsize(600,400)

# 聊天
frame_1=tk.Frame(root,height=300,width=200)
frame_1.pack(side=TOP)
frame_1.place(x=0,y=0)

w=Scrollbar(frame_1)
w.pack(side=RIGHT,fill=Y)
mylist = Listbox(frame_1, yscrollcommand = w.set,width=50,height=14,bg='#D9FFFF')
mylist.pack( side = LEFT, fill = BOTH )


# 输入

frame_2=tk.Frame(root)
frame_2.place(x=0,y=260)
t=Text(frame_2,bg="#FFFFFF",width=49,height=10,bd=1,highlightcolor='#AAAAFF')
t.pack()




# 署名
frame_4=tk.Frame(root)
frame_4.place(x=410,y=240)
lab_1=tk.Label(frame_4,fg="#F00078",text="@肥学",width=10,height=10,font=('微软雅黑',14))
lab_1.pack(side=LEFT)
# p=PhotoImage(file='photo/1.ioc')
# lab_2=tk.Label(frame_4,image=p,width=90,height=90)
# lab_2.pack(side=RIGHT)


# 图片
frame_5=tk.Frame(root)
frame_5.place(x=380,y=0)
text_image=tk.Text(frame_5,width=30,height=19)
photo=PhotoImage(file='photo/2.png')
text_image.image_create(END,image=photo)
text_image.pack()

def input_text():
    get_text="我："+t.get("0.0",'end')+'\n\n'
    mylist.insert('end',get_text)
    t.delete('1.0','end')
    girl_friend(get_text)

def girl_friend(topic):

    resp = requests.get("http://api.qingyunke.com/api.php", {<!-- -->'key': 'free', 'appid': 0, 'msg': topic})
    resp.encoding = 'utf8'
    resp = resp.json()
    girl_text='小美：'+resp['content']
    mylist.insert('end',girl_text)


# 按键
frame_3=tk.Frame(root)
frame_3.place(x=350,y=260)
button_1=tk.Button(frame_3,command=input_text,text="发送",bg='#C4E1FF',height=1,width=6,bd=0,relief=RIDGE,fg="#000000")
button_1.pack(side=LEFT)
button_2=tk.Button(frame_3,command=root.destroy,text="退出",bg='#ff7575',height=1,width=6,bd=0,relief=RIDGE,fg="#000000")
button_2.pack(side=RIGHT)

root.mainloop()

```

#### 两个主要函数

```
def input_text():
    get_text="我："+t.get("0.0",'end')+'\n\n'
    mylist.insert('end',get_text)
    t.delete('1.0','end')
    girl_friend(get_text)

def girl_friend(topic):

    resp = requests.get("http://api.qingyunke.com/api.php", {<!-- -->'key': 'free', 'appid': 0, 'msg': topic})
    resp.encoding = 'utf8'
    resp = resp.json()
    girl_text='小美：'+resp['content']
    mylist.insert('end',girl_text)

```

也可以封装成可执行文件，这样更方便一点教程我就不写了大家看一下这个：

#### GUI设置

## <font color="red" size="6">点击直接资料领取</font>

**如果你在学习python或者Java哪怕是C遇到问题都可以来给我留言，因为在学习初期新手总会走很多弯路，这个时候如果没有有个人来帮一把的话很容易就放弃了。身边很多这样的例子许多人学着学着就转了专业换了方向，不仅是自身问题还是没有正确的学习。所以作为一个过来人我希望有问题给我留言，说不上是帮助就是顺手敲几行字的事情。**

**这里有python，Java学习资料还有有有趣好玩的编程项目，更有难寻的各种资源。反正看看也不亏。**
