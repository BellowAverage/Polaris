
--- 
title:  用 Python 送上特殊的母亲节祝福 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/20200510103334507.gif#pic_center" alt=""> 今天是母亲节，做儿女的自然要为母亲送上节日的祝福，如果自己在母亲身边的话，可以直接说几句祝福的话以及送一些小礼物什么的，要是不在母亲身边的话，可以打个电话问候一下。

当然了，作为一个程序员，除了上面的祝福方式，我们还可以编写一个小程序为母亲送上特殊的节日祝福，本文我们使用 Python 来为自己的母亲制作一个特殊的节日祝福。

代码实现如下所示：

```
colorama.init(convert=True)  
RED = colorama.Fore.RED + colorama.Style.BRIGHT  
CYAN = colorama.Fore.CYAN + colorama.Style.BRIGHT  
GREEN = colorama.Fore.GREEN + colorama.Style.BRIGHT  
YELLOW = colorama.Fore.YELLOW + colorama.Style.BRIGHT  
MAGENTA = colorama.Fore.MAGENTA + colorama.Style.BRIGHT  
  
# 打印抬头  
for i in range(1, 35):  
    print('')  
# \*的位置  
heartStars = \[2, 4, 8, 10, 14, 20, 26, 28, 40, 44, 52, 60, 64, 76\]  
# 空格的位置  
heartBreakLines = \[13, 27, 41, 55, 69, 77\]  
# 玫瑰的空列位置  
flowerBreakLines = \[7, 15, 23, 31, 39, 46\]  
  
# 添加空列  
def addSpaces(a):  
    count = a  
while count &gt; 0:  
        print(' ', end='')  
        count -= 1  
  
# 添加空行  
def newLineWithSleep():  
    time.sleep(0.3)  
    print('\\n', end='')  
  
play = 0  
while play == 0:  
    Left\_Spaces = randint(8, 80)  
    addSpaces(Left\_Spaces)  
# 画心  
for i in range(0, 78):  
if i in heartBreakLines:  
            newLineWithSleep()  
            addSpaces(Left\_Spaces)  
elif i in heartStars:  
            print(RED + '\*', end='')  
elif i in (32, 36):  
            print(GREEN + 'M', end='')  
elif i == 34:  
            print(GREEN + 'O', end='')  
else:  
            print(' ', end='')  
    newLineWithSleep()  
    addSpaces(randint(8, 80))  
    print(CYAN + "H a p p y  M o t h e r ' s   D a y !", end='')  
    newLineWithSleep()  
    newLineWithSleep()  
    Left\_Spaces = randint(8, 80)  
    addSpaces(Left\_Spaces)  
# 画花  
for i in range(0, 47):  
if i in flowerBreakLines:  
            newLineWithSleep()  
            addSpaces(Left\_Spaces)  
elif i in (2, 8, 12, 18):  
            print(MAGENTA + '{', end='')  
elif i in (3, 9, 13, 19):  
            print(MAGENTA + '\_', end='')  
elif i in (4, 10, 14, 20):  
            print(MAGENTA + '}', end='')  
elif i in (27, 35, 43):  
            print(GREEN + '|', end='')  
elif i in (34, 44):  
            print(GREEN + '~', end='')  
elif i == 11:  
            print(YELLOW + 'o', end='')  
else:  
            print(' ', end='')  
    print('\\n', end='')

```

看一下效果： <img src="https://img-blog.csdnimg.cn/20200510103401867.gif" alt="">

<img src="https://img-blog.csdnimg.cn/20200424064031758.PNG?#pic_center" alt="" width="500">
