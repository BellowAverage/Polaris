
--- 
title:  在python终端中打印颜色的3中方式（python3经典编程案例） 
tags: []
categories: [] 

---
在 Python 中有几种方法可以将彩色文本输出到终端。 最常见的做法是：

#### 1、使用内置模块：`colorama` 模块

可以使用 Colorama 的 ANSI 转义序列的常量简写来完成彩色文本的跨平台打印： 案例1：

```
from colorama import Fore, Back, Style

print(Fore.RED + 'some red text')
print(Fore.YELLOW + 'some red text')
print(Fore.BLUE + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

```

案例二：

```
# colorama是一个python专门用来在控制台、命令行输出彩色文字的模块，可以跨平台使用。
# 安装colorama模块: pip install colorama
# 常用格式: Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL
from colorama import Fore,Back,Style
print (Fore.RED + "some red text")
print (Fore.GREEN + "some red text")
print (Fore.YELLOW + "some red text")
print (Fore.BLUE + "some red text")
print (Fore.MAGENTA + "some red text")
print (Fore.CYAN + "some red text")
print (Fore.RESET + "some red text")
print (Fore.WHITE + "some red text")
print (Fore.BLACK + "some red text")
print (Back.GREEN + "and with a green background")
print (Style.DIM + "and in dim text")
print (Style.RESET_ALL)
print ("back to normal now!!")

# Init关键字参数: init()接受一些* * kwargs覆盖缺省行为  init(autoreset = False):
# 如果你发现自己一再发送重置序列结束时关闭颜色变化每一个打印,然后init(autoreset = True)将自动化。 示例：
from colorama import init,Fore
init(autoreset=True)
print (Fore.RED + "welcome to python !!")
print ("automatically back to default color again")

```

#### 2、使用`termcolor`模块：

termcolor 是一个 Python 模块，用于在终端中输出 ANSII 颜色格式。

```
# Python program to print
# colored text and background
import sys
from termcolor import colored, cprint
 
text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
print(text)
cprint('Hello, World!', 'green', 'on_red')
 
print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')
print_red_on_cyan('Hello, World!')
print_red_on_cyan('Hello, Universe!')
 
for i in range(10):
    cprint(i, 'magenta', end=' ')
 
cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)


```

#### 3、使用 ANSI 转义码

打印彩色文本最常用的方法是直接打印 ANSI 转义序列。 这可以以不同的格式交付，例如：

构建要调用的函数：我们可以构建函数来调用特定颜色命名的函数来执行相关的 ANSI 转义序列。 案例一：

```
# 一. 使用Python中自带的print输出带有颜色或者背景的字符串

# 其中，显示方式、前景色、背景色都是可选参数（可缺省一个或多个）。
print('\033[显示方式;前景色;背景色m输出内容\033[0m')
print(f'\033[31m5. ---zhangjskf ---\033[0m ')


print("显示方式：")
# 显示方式	效果
# 0	默认
# 1	粗体
# 4	下划线
# 5	闪烁
# 7	反白显示
print("\033[0mSuixinBlog: https://suixinblog.cn\033[0m")
print("\033[1mSuixinBlog: https://suixinblog.cn\033[0m")
print("\033[4mSuixinBlog: https://suixinblog.cn\033[0m")
print("\033[5mSuixinBlog: https://suixinblog.cn\033[0m")
print("\033[7mSuixinBlog: https://suixinblog.cn\033[0m")


# 字体色编号	背景色编号	颜色
# 30	40	黑色
# 31	41	红色
# 32	42	绿色
# 33	43	黄色
# 34	44	蓝色
# 35	45	紫色
# 36	46	青色
# 37	47	白色
print("字体色：")
print("\033[30mSuixinBlog: https://suixinblog.cn\033[0m")
print("\033[31mSuixinBlog: https://suixinblog.cn\033[0m")
print("\033[32mSuixinBlog: https://suixinblog.cn\033[0m")
print("\033[4;33mSuixinBlog: https://suixinblog.cn\033[0m")
print("\033[34mSuixinBlog: https://suixinblog.cn\033[0m")
print("\033[1;35mSuixinBlog: https://suixinblog.cn\033[0m")
print("\033[4;36mSuixinBlog: https://suixinblog.cn\033[0m")
print("\033[37mSuixinBlog: https://suixinblog.cn\033[0m")
print("背景色：")
print("\033[1;37;40m\tSuixinBlog: https://suixinblog.cn\033[0m")
print("\033[37;41m\tSuixinBlog: https://suixinblog.cn\033[0m")
print("\033[37;42m\tSuixinBlog: https://suixinblog.cn\033[0m")
print("\033[37;43m\tSuixinBlog: https://suixinblog.cn\033[0m")
print("\033[37;44m\tSuixinBlog: https://suixinblog.cn\033[0m")
print("\033[37;45m\tSuixinBlog: https://suixinblog.cn\033[0m")
print("\033[37;46m\tSuixinBlog: https://suixinblog.cn\033[0m")
print("\033[1;30;47m\tSuixinBlog: https://suixinblog.cn\033[0m")

```

案例二：

```
# Python program to print
# colored text and background
def prRed(skk): print("\033[91m {}\033[00m".format(skk))


def prGreen(skk): print("\033[92m {}\033[00m".format(skk))


def prYellow(skk): print("\033[93m {}\033[00m".format(skk))


def prLightPurple(skk): print("\033[94m {}\033[00m".format(skk))


def prPurple(skk): print("\033[95m {}\033[00m".format(skk))


def prCyan(skk): print("\033[96m {}\033[00m".format(skk))


def prLightGray(skk): print("\033[97m {}\033[00m".format(skk))


def prBlack(skk): print("\033[98m {}\033[00m".format(skk))


prCyan("Hello World, ")
prYellow("It's")
prGreen("Geeks")
prRed("For")
prGreen("Geeks")


```
