
--- 
title:  慎用！3个容易被打的Python恶搞脚本 
tags: []
categories: [] 

---
Python 无限恶搞朋友电脑，别提有多爽了，哈哈，打造自己的壁纸修改器，电脑无限锁屏， 无线弹窗，都在这里！！！

**1、修改电脑桌面壁纸**

**工具使用**
- 开发环境：python3.7， Windows10- 使用工具包：win32api，win32con, win32gui, os, random- win32的工具下载命令：
```
pip install pywin32
```

**项目解析思路**

桌面数据信息是保存在注册表上的内容，数据保存在第二项 的Control PanelDesktop子项里就可以了。

<img src="https://img-blog.csdnimg.cn/img_convert/8e6cf244419e2b22ba131cff3c191d1f.png" alt="8e6cf244419e2b22ba131cff3c191d1f.png">

通过win32api 打开注册表选择配置的对应子项生成对应句柄

```
k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, 'Control PanelDesktop', 0, win32con.KEY_SET_VALUE)
```

将桌面样式调整拉伸模式 2 拉伸壁纸 0 壁纸居中 6 适应 10 填充

准备好需要修改的图片壁纸（壁纸数据通过爬虫技术进行采集）

<img src="https://img-blog.csdnimg.cn/img_convert/2f4b4a38d5262d9832698abfdb1820e1.png" alt="2f4b4a38d5262d9832698abfdb1820e1.png">

win32gui提交数据将桌面修改成自己准备的桌面壁纸

```
win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, img_path, win32con.SPIF_SENDWININICHANGE)
```

**源码分享**

```
import win32api   # 调用Windows底层的接口配置   pip install pywin32
import win32con   # 修改数据
import win32gui   # 提交对应的数据
import os       # Python 管理文件工具包
import random   # 取出对应的随机值
import time   # 时间管理模块


def set_wallpaper():
    path = os.listdir(r'图片文件夹')
    for i in path:
        img_path = r'图片文件夹' + "\" + i
        print(img_path)
        # 打开注册表  句柄
        k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, 'Control PanelDesktop', 0, win32con.KEY_SET_VALUE)
        # 2 拉伸壁纸   0 壁纸居中  6 适应 10 填充
        win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, '2')
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, img_path, win32con.SPIF_SENDWININICHANGE)
        time.sleep(10)


set_wallpaper()
```

**2、电脑无限锁屏**

**工具使用**
- 开发环境：python3.7， Windows10- 使用工具包：ctypes ctypes
ctypes ctypes是 Python 的外部函数库。它提供了与 C 兼容的数据类型，并允许调用 DLL 或共享库中的函数。可使用该模块以纯 Python 形式对这些库进行封装。通过操作系统底层的 user32.dll 实现锁屏效果

<img src="https://img-blog.csdnimg.cn/img_convert/fcaa348f8ac6ca8a903d8f70d497cb0e.png" alt="fcaa348f8ac6ca8a903d8f70d497cb0e.png">

```
def lock_windows(): while True: user = windll.LoadLibrary("user32.dll") user.LockWorkStation() lock_windows()
```

代码以提供各位大佬可自行尝试

<img src="https://img-blog.csdnimg.cn/img_convert/3f54d7324f4945586ad4a410b9e7d86e.png" alt="3f54d7324f4945586ad4a410b9e7d86e.png">

打包的方法：pyinstaller -F 你的文件名

打包之后可给你朋友同事尝试一下（为了朋友同事间的友谊最好加个延时操作）

**3、无限弹窗**

之前大家应该都了解过熊猫烧香（类似，如果有相识跟我没有关系） 通过os模块执行打开cmd窗口页面（确保是环境变量里有的选项）

```
for i in range(2000):
    os.system('start cmd')
```

电脑配置低的请勿轻易尝试 win关闭页面命令 ：**start taskkill /f /im cmd.exe /t**

**<strong>往期推荐**</strong>
- - - 