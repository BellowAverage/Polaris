
--- 
title:  如何用 Python 实现手机远程控制电脑 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/img_convert/894ad9b6a8c3ba828850b2b781e7c110.png">

来源：https://zacksock.blog.csdn.net

## 

## 一、前言

很多时候，我们都有远程控制电脑的需求。比如正在下载某样东西，需要让电脑在下载完后关机。或者你需要监控一个程序的运行状况等。

今天我们就来用Python实现一个远程监控并控制电脑的小程序。

## 二、实现原理

听起来远程控制电脑好像很高级的样子，但是实现起来其实非常简单。实现原理如下：
1. 运行程序，让程序不停地读取邮件1. 用手机给电脑发送邮件1. 判断是否读取到指定主题的邮件，如果有，则获取邮件内容1. 根据邮件内容，执行预设的函数
与其说是学习如何远程控制电脑，还不如说是学习如何读取邮件。当然，上面的的流程只实现了远程控制电脑，而没实现对电脑的监控。而监控的操作可以以截图的方式来进行。

我们可以预设一个指令，当读取到邮件内容为grab时，我们就发送电脑截图。如何将电脑截图发送给手机邮箱，这样就达到了监控的效果。

关于如何发送邮件可以参考博客：

https://blog.csdn.net/ZackSock/article/details/112278615?spm=1001.2014.3001.5501

这里就不再详细说了。下面我们看看如何读取邮件。

## 三、读取邮件

读取邮件需要使用到imbox模块，安装语句如下：

```
pip install imbox

```

读取邮件的代码如下：

```
from imbox import Imbox


def read_mail(username, password):
    with Imbox('imap.163.com', username, password, ssl=True) as box:
        all_msg = box.messages(unread=True)
        for uid, message in all_msg:
            # 如果是手机端发来的远程控制邮件
            if message.subject == 'Remote Control':
                # 标记为已读
                box.mark_seen(uid)
                return message.body['plain'][0]



```

首先我们用with语句，打开邮箱。然后通过下面语句获取所有的未读邮件：

```
all_msg = box.messages(unread=True)

```

获取未读邮件后，对邮件进行遍历。将主题为“Reomte Control”的邮件标记为已读，并返回文本内容。

这里需要注意，因为我们筛选出了主题为“Remote Control”的邮件，因此我们在用手机发邮件的时候需要将主题设置为“Remote Control”，这样可以避免其它邮件的干扰。

## 四、截图

截图需要使用到PIL模块，安装如下：

```
pip install pillow

```

截图的代码很简单：

```
from PIL import ImageGrab


def grab(sender, to):
     # 截取电脑全屏
    surface = ImageGrab.grab()
    # 将截屏保存为surface.jpg
    surface.save('surface.jpg')
    # 将截屏发送给手机
    send_mail(sender, to, ['surface.jpg'])

```

其中send_mail的代码如下：

```
import yagmail


def send_mail(sender, to, contents):
    smtp = yagmail.SMTP(user=sender, host='smtp.163.com')
    smtp.send(to, subject='Remote Control', contents=contents)

```

关于发送邮件的介绍可以参考上面提到的博客。

## 五、关机

关机的操作非常简单，我们可以用python来执行命令行语句即可。代码如下：

```
import os


def shutdown():
  # 关机
    os.system('shutdown -s -t 0')

```

除了关机，我们还可以执行很多操作。对于一些复杂的操作，我们可以预编写一些bat文件，这里就不演示了。

## 六、完整代码

上面我们编写了各个部分的代码，然后再来看看主体部分的代码：

```
def main():
  # 电脑用来发送邮件已经电脑读取的邮箱
    username = 'sockwz@163.com'
    password = '********'
  
  # 手机端的邮箱
    receiver = '2930777518@qq.com'
  
  # 读取邮件的时间间隔
    time_space = 5
  
  # 注册账户
    yagmail.register(username, password)
    
    # 循环读取
    while True:
        # 读取未读邮件
        msg = read_mail(username, password)
        if msg:
          # 根据不同的内容执行不同操作
            if msg == 'shutdown':
                shutdown()
            elif msg == 'grab':
                grab(username, receiver)
        time.sleep(time_space)

```

我们可以根据自己的需求编写一些其它功能。下面是完整的代码：

```
import os
import time
import yagmail
from imbox import Imbox
from PIL import ImageGrab




def send_mail(sender, to, contents):
    smtp = yagmail.SMTP(user=sender, host='smtp.163.com')
    smtp.send(to, subject='Remote Control', contents=contents)




def read_mail(username, password):
    with Imbox('imap.163.com', username, password, ssl=True) as box:
        all_msg = box.messages(unread=True)
        for uid, message in all_msg:
            # 如果是手机端发来的远程控制邮件
            if message.subject == 'Remote Control':
                # 标记为已读
                box.mark_seen(uid)
                return message.body['plain'][0]




def shutdown():
    os.system('shutdown -s -t 0')




def grab(sender, to):
    surface = ImageGrab.grab()
    surface.save('surface.jpg')
    send_mail(sender, to, ['surface.jpg'])




def main():
    username = 'sockwz@163.com'
    password = '你的授权码'
    receiver = '2930777518@qq.com'
    time_space = 5
    yagmail.register(username, password)
    while True:
        # 读取未读邮件
        msg = read_mail(username, password)
        if msg:
            if msg == 'shutdown':
                shutdown()
            elif msg == 'grab':
                grab(username, receiver)
        time.sleep(time_space)




if __name__ == '__main__':
    main()



```

## ``





&lt; END &gt;

<img src="https://img-blog.csdnimg.cn/img_convert/12c9c7a22fbff4320d40757c6efacad3.gif">

微信扫码关注，了解更多内容
