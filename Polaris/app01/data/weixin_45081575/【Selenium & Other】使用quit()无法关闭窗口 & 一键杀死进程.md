
--- 
title:  【Selenium & Other】使用quit()无法关闭窗口 & 一键杀死进程 
tags: []
categories: [] 

---
## 前言

>  
 有位读者留言，遇到了一件两难全的事儿。在关闭Python使用os模块执行cmd命令调用的chromedriver驱动打开的chrome浏览器时，有以下问题~ 
 - 使用`driver.quit()`退出浏览器，`chromedriver.exe`进程退出，关闭没有窗口- 使用`driver.close()`退出浏览器，`chromedriver.exe`进程没有退出，窗口关闭 


但是咱们这里全都要，下面就来解决它，顺便说一下关于杀死进程的事儿~

文章链接在这：

|标题|链接
|------
|**【Selenium】Selenium绕过检测 &amp; 隐藏特征**|****

问题在这： <img src="https://img-blog.csdnimg.cn/ae2d72f725b6457d974b38ba07f61e0a.png" alt="">

**解决方法如下：**
- 先关闭窗口，再杀掉 `chromedriver.exe` 进程。
```
driver.close()
driver.quit()

```

全文完~🎈🎈 下面且再吧啦一下吧🏹🏹

## 问题复现

>  
 这份代码贯穿全文，将用于多次示例。 


执行以下代码，详情看动图
- 执行以下代码，会启动一个名为 `chromedriver.exe`的进程，通过`任务管理器` 可看到
```
# -*- coding: utf-8 -*-
# Name:         hide_features.py
# Author:       小菜
# Date:         2022/8/29 15:43
# Description:

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':
    os.system(r'start chrome --remote-debugging-port=9527 --user-data-dir="F:\selenium"')
    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
    driver = webdriver.Chrome(options=options)
    driver.get('https://bot.sannysoft.com/')
    # driver.quit()
    driver.close()


```

这个是 `drivrt.quit()` 的
- 可以看到，`chromedriver.exe` 进程退出了，但窗口没有关闭
<img src="https://img-blog.csdnimg.cn/7d89b46040104363a7173aec74cead6c.gif" alt="请添加图片描述">

这个是 `drivrt.close()` 的
- 可以看到，`chromedriver.exe` 进程没有退出，但窗口关闭了。
<img src="https://img-blog.csdnimg.cn/e748bf16acc5456fa3c6c16b89c1f4cf.gif" alt="在这里插入图片描述">

问题成功复现，下面解决它。

## 解决方法

>  
 全程注意打开 `任务管理器`，实时查看 `chromedriver.exe`进程的情况~ 


这里准备两种解决方法，
1. 通过Python1. 通过Windows系统的`taskkill`（终止进程命令
两种方法
- 直接杀死chrome进程- 杀死置顶端口的进程
### Python实现

跟一下 `driver.quit()`，看到以下源码，不管执行成功与否，最终都是执行了 `self.service.stop()`

```
def quit(self) -&gt; None:
    """
    Closes the browser and shuts down the ChromiumDriver executable
    that is started when starting the ChromiumDriver
    """
    try:
        super().quit()
    except Exception:
        # We don't care about the message because something probably has gone wrong
        pass
    finally:
        self.service.stop()

```

这里我们改一下代码，将 `driver.quit()` 修改 成以下
- 先挂关闭浏览器，再停止`service`，可以达到杀死`chromedriver.exe`进程和关闭窗口的两全其美。
```
driver.close()
driver.service.stop()

```

然后执行代码，看以下动图

<img src="https://img-blog.csdnimg.cn/86305f76f71c445890f0b13618b32317.gif" alt="">

完美解决问题~

### Windows系统命令

>  
 这里会用到两个Windows的命令，分别是 `netstat` 和 `taskkill` 


可以通过以下链接获得更详细的介绍🎈

|命令|链接
|------
|`netstat`|
|`taskkill`|

**参数：**

<img src="https://img-blog.csdnimg.cn/3a98da1d9aee4d84b505573991ce0e99.png" alt="在这里插入图片描述">

#### `netstat`

>  
 命令用于显示活动的TCP链接、正在使用的端口等~ 


官方介绍截图如下：

<img src="https://img-blog.csdnimg.cn/113553473683481d85eeae7e5338b98e.png" alt="">

执行 `driver.close()` 的代码之后，`chromedriver.exe` 进程的状态还是 `正在运行`的， 现在打开电脑的`cmd` 窗口，输入以下命令，然后回车

```
netstat -ano | findstr 9527

```

代码释义( `查找所有活动的TCP连接中包含9527的连接`：
- `netstat -ano`：显示活动的TCP连接- `findstr`：Windows系统命令，用于查找指定的包含的字符串- `9527`：因为上面的代码中指定打开的端口是 **9527**
运行如下图所示：

<img src="https://img-blog.csdnimg.cn/55bf7fffa8574d46adfde3998f063613.png" alt="">

看到有两个TCP连接，这里后面跟的是它们的`PID`（Process Identification 干掉任意下面那个状态为`CLOSE_WAIT` 的 `进程` 就可以结束 `chromedriver.exe` 进程啦🐱‍🏍

接下来去干掉它！！！

#### `taskkill`

>  
 Windows系统自带命令，用于结束一个或多个进程~ 


官方介绍截图如下：

<img src="https://img-blog.csdnimg.cn/f3b89d80c9a04556b81f49ebfef7a8c2.png" alt="">

上面我们知道了 活动的 TCP连接，这里来干了它。

```
taskkill /f /t /pid 2024

```

代码释义（强制结束 `pid`为`2024` 的进程，你需要改为你的进程 `pid`：
- `/f`：指定强制结束进程- `/t`：结束指定进程以及由该进程启动的任何子进程- `/pid &lt;processID&gt;`：指定要终止的进程的进程 ID。
运行如下图所示：
- 成功结束`chromederiver.exe`进程<img src="https://img-blog.csdnimg.cn/a6ca1d7bfcf34b79829cccfa0b50efd7.png" alt="">
改写成 `Python`代码如下：
- 同样可以达到杀死`chromedriver.exe` 进程的目的~
```
import os
result = os.popen('netstat -ano | findstr 9527 | findstr CLOSE_WAIT')
port = result.strip().split('      ')[-1]
os.popen(f'taskkill /f -t /pid {<!-- -->port}')

```

但是！！！ 这个方法不是特别妙，有没有更妙的方法呢？答案是没有！不存在完美的方法🎃🎃

#### `tasklist`

>  
 显示本地计算机或远程计算机上当前正在运行的进程列表。 


官方介绍截图如下： <img src="https://img-blog.csdnimg.cn/fefaad9a66f34a8c89782e6910c19341.png" alt="">

使用 `tasklist ` 查看包含 `chromedriver.exe`的进程，然后再干掉它。
- 会存在误杀，你开启了两个窗口，端口分别是1234 和 9527，但不清楚哪个窗口对应哪个端口，所以可能会误杀~
```
tasklist | findstr chromedriver.exe

```

如下图：
- 可以获取到它的 `PID`，后面去干掉对应的 `PID` 就完事了
<img src="https://img-blog.csdnimg.cn/70d6e59fd7b049bf88991f3255cf01f3.png" alt="在这里插入图片描述">

#### 结合写法

如果进程存在就**kill** 了它

```
tasklist | find /i "chromedriver.exe" &gt; nul &amp;&amp; taskkill /f /im "chromedriver.exe" &gt; nul

```

## 关闭`N`个程序

>  
 思路发散一下，可以关闭多个电脑程序，不局限于Selenium浏览器的使用。 


**杀死指定进程**
- `im`： 指定要终止的进程的映像名称
```
taskkill /f /t /im chromedriver.exe

```

如下所示：
- 杀死所有进程名为 `chromedriver.exe` 的进程 <img src="https://img-blog.csdnimg.cn/9e748df18bf3499bb82dcc2eff3bca5c.gif" alt="">
**一行命令杀死多个进程**
- 这里干掉了4个进程树，甚至还关闭 `cmd`窗口~- 思路再发散一下，将平时经常会打开的程序都添加到这行代码里面去，然后编写成`.bat`批处理文件，一键执行关闭指定N个程序，实在不济，下面也还有个一键关闭所有程序的~
```
taskkill /f /t /im msedge.exe /im wps.exe /im Typora.exe /im cmd.exe

```

运行如下所示： <img src="https://img-blog.csdnimg.cn/27a4d01b18f74cb284a6c8f42e7248f9.gif" alt="">

**干掉所有程序**

```
taskkill /F /FI "USERNAME eq 【您的用户名】" /FI "IMAGENAME ne explorer.exe" /FI "IMAGENAME ne dwm.exe，

```

代码释义：
- 意思是在此用户账户下筛选 explorer.exe（文件资源管理器）和 dwm.exe（桌面窗口管理器），将这两项强制终止进程，即可达到关闭所有程序的目的。
## 后话

see you.🐱‍🏍🐱‍🏍
