
--- 
title:  女朋友让我深夜十二点催她睡觉，我用Python轻松搞定 
tags: []
categories: [] 

---
## 事情是这样的：昨天晚上，女朋友让我十二点催她睡觉。

<img src="https://img-blog.csdnimg.cn/img_convert/da45a643845b24397f22813a408e6840.png" alt="da45a643845b24397f22813a408e6840.png">不过，可是我实在太困了，熬不下去…… 是吧？女朋友哪有睡觉重要？<img src="https://img-blog.csdnimg.cn/img_convert/fa68f1aef45efee7c6a787902d3aa230.png" alt="fa68f1aef45efee7c6a787902d3aa230.png">但，女朋友的命令，我是不敢违抗的……<img src="https://img-blog.csdnimg.cn/img_convert/5088907a44ef1dfda32ca9ffcec270ab.png" alt="5088907a44ef1dfda32ca9ffcec270ab.png">但是睡觉也不能缺！

这时候我们该怎么办呢？是时候让Python登场了！

## **Python登场**

这次我们来做一个自动发送微信的程序，在深夜十二点的时候给女朋友发去消息，也算是尽了一个男朋友的义务了。

### 安装和导入

我们需要两个模块：apscheduler，pyautogui

快捷键 Windows+r 打开运行控制框，输入 cmd，进入命令行，输入：

```
pip install apscheduler
pip install pyautogui
```

导入：

```
import pyautogui
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler # 阻塞当前进程的调度器
# blocking类型调度器会阻塞当前进程，若你想要后台运行的调度器，可以使用以下代码：
# from apscheduler.schedulers.background import BackgroundScheduler
```

## **pyautogui**

首先我们来实现自动发送消息

pyautogui 是一个非常强大的库，可以操作鼠标和键盘。我们将用它来完成自动操作电脑。

先来做一些基本设置：

```
pyautogui.PAUSE = 1 # 设置每一步操作的间隔（秒），可防止操作太快
```

然后我们登录微信，最小化。

接下来我们把鼠标放到微信的任务栏图标上，运行以下语句，获取此时光标的坐标，返回一个Point对象：

```
print(pyautogui.position()) # 打印坐标，Point(x=148, y=879)
icon_position = pyautogui.position() # Point(x=148, y=879)
```

打开微信，选择女朋友的回话窗口，将鼠标放在输入框上，同样获取光标坐标，为了将焦点锁定到输入框以方便待会的输入。<img src="https://img-blog.csdnimg.cn/img_convert/bb95ebc0542219ab13a5d6a4bd2a7cac.png" alt="bb95ebc0542219ab13a5d6a4bd2a7cac.png">

```
print(pyautogui.position()) # 打印坐标，Point(x=174, y=751)
entry_position = pyautogui.position() # Point(x=174, y=751)
```

接下来，控制程序依次点击这两个点：

```
pyautogui.click(icon_position) # 默认左键单击
# pyautogui.click(148, 879)
pyautogui.click(entry_position)
# pyautogui.click(174, 751)
```

打开微信并锁定焦点后，我们开始输入文本。

输入文本可以有两种方式：
- `pyautogui.typewrite(['o', 'n', 'e', 'enter'])`
在方法中传入一个列表，里面每一元素都是单个字母或特殊按键
- `pyautogui.typewrite('You can type multiple letters in this way')`
传入字符串，但不能同时打印字母和特殊按键。

这两种方式都不能直接输入中文，所以只能依靠你的输入法来输入中文了。

```
pyautogui.typewrite([*list('zhengzai '), *list('jinxing '), 'shift', *list('pyautogui'), 'shift', *list('shiyan '), 'enter'], 0.1) # 第一个参数是输入文本，第二个是输入每个字符的间隔时间
```

为了使我们的操作更加 人模狗样 像人的操作，我么来加上移动鼠标的代码：

```
pyautogui.moveTo(icon_position, duration=2) # duration为执行时长，可选
pyautogui.click(icon_position)
pyautogui.moveTo(entry_position, duration=2)
pyautogui.click(entry_position)
pyautogui.typewrite([*list('zhengzai '), *list('jinxing '), 'shift', *list('pyautogui'), 'shift', *list('shiyan '), 'enter'], 0.1) # 第二个参数为按下每一个字母的间隔，可选
```

看看效果：<img src="https://img-blog.csdnimg.cn/img_convert/5aa9c49f4beb94f61a36c5d60870f9d9.gif" alt="5aa9c49f4beb94f61a36c5d60870f9d9.gif">当然，若是你要输入的内容实在很多，又嫌麻烦，可以通过复制粘贴来实现：

```
import pyperclip


pyperclip.copy('正在进行发中文试验，看到请忽略，更不要骂傻逼') # 复制
pyautogui.hotkey('ctrl', 'v') # 按下组合键的方法，ctrl+v粘贴
pyautogui.press('enter') # 按下按键
```

<img src="https://img-blog.csdnimg.cn/img_convert/fdabbef55056560873201e002e7f05b5.gif" alt="fdabbef55056560873201e002e7f05b5.gif">这样，我们便完成了自动发送微信消息的功能了。

## **apscheduler**

APScheduler 是一个Python库，可实现延迟调度要执行Python代码的功能，可以只执行一次，也可以定期执行。可以随时添加新任务或删除旧任务。能够十分方便地进行定时任务。

```
scheduler = BlockingScheduler() # 实例化一个调度器
scheduler.add_job(main, 'date', run_date=datetime(2021, 8, 18, 24, 00, 00)) # 添加任务
scheduler.start()
```

add_job 方法在这里传了 3 个参数，第一个为到时间后要执行的函数，第二个为触发器的类型。这里选用的是 date 触发器，特定的时间点触发，作业任务只会执行一次。第三个参数 run_date 就是执行的时间。在这前我已经把自动发送消息的代码封装为了 main 函数，只需到时后调用即可。

## **完整代码**

```
import pyautogui
import pyperclip
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


def main():
  pyautogui.PAUSE = 0


  icon_position = pyautogui.Point(x=148, y=879) # 任务栏图标位置
  entry_position = pyautogui.Point(x=174, y=751) # 输入框位置


  pyautogui.moveTo(icon_position, duration=1) # duration为执行时长，可选
  pyautogui.click(icon_position)
  pyautogui.moveTo(entry_position, duration=0.7)
  pyautogui.click(entry_position)
  pyperclip.copy('快去睡觉')
  pyautogui.hotkey('ctrl', 'v')
  pyautogui.press('enter')
    pyperclip.copy('笨猪')
  pyautogui.hotkey('ctrl', 'v')
  pyautogui.press('enter')


scheduler = BlockingScheduler() # 实例化
scheduler.add_job(main, 'date', run_date=datetime(2021, 8, 18, 24, 00, 00)) # 添加任务
scheduler.start()
```

完成啦！现在可以去睡觉了。

## **结果**

第二天早上起床，我被我妈妈骂了一顿，问我为什么午夜12点的时候电脑还亮着，而且还在自己发微信！

不过，好在女朋友没丢，我成功完成了女朋友的任务！<img src="https://img-blog.csdnimg.cn/img_convert/906cfe16c1743d74a1cab417566957ce.gif" alt="906cfe16c1743d74a1cab417566957ce.gif">

好啦，这篇文章就到这里了。以上就是我分享的全部内容，感谢阅读！

## 版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。本文链接：

https://blog.csdn.net/weixin_52132159/article/details/119785717

别忘了**点赞**，**在看**哈~
