
--- 
title:  10分钟学会python写游戏脚本！Python其实很简单 
tags: []
categories: [] 

---
### 前言

最近在玩儿公主连结，之前也玩儿过阴阳师这样的游戏，这样的游戏都会有个初始号这样的东西，或者说是可以肝的东西。

当然，作为一名程序员，肝这种东西完全可以用写代码的方式帮我们自动完成。游戏脚本其实并不高深，最简单的体验方法就是下载一个Airtest了，直接截几个图片，写几层代码，就可以按照自己的逻辑玩儿游戏了。

<img src="https://img-blog.csdnimg.cn/f83fd1dd64314e9ab1f73c882166ab25.jpeg#pic_center" alt="在这里插入图片描述">

当然，本篇文章不是要讲Airtest这个怎么用，而是用原始的python+opencv来实现上面的操作。

### 准备工作

首先，我们要完成以下准备。
- **安卓设备**一个：模拟器或者真机都可以。- 安装**ADB**，并添加到系统的PATH里：adb是用来- 安装**tesseract-ocr**，并添加到系统的PATH里：帮助我们实现简单的字符识别- 安装**python3.7**以上的版本
### python库安装

```
pip install pillow pytesseract opencv-python

```

除此以外，如果有需要可以安装uiautomator2，这篇文章就不涉及这块知识了。

### 使用adb获取安卓设备

这里我们主要是涉及到单个安卓设备的ADB连接操作，首先我们打开模拟器。

然后我们调用adb devices来获取当前的安卓设备，我这里是一个模拟器。

<img src="https://img-blog.csdnimg.cn/c3e1c13ea6fe4ea0ace1f3c5a091e20d.jpeg#pic_center" alt="在这里插入图片描述">

接下来可以调用adb shell测试一下是否能进入到安卓设备的shell环境下，确认可以输入exit退出即可。

<img src="https://img-blog.csdnimg.cn/1f1e0db150c34fafa7952c77031f5d9a.jpeg#pic_center" alt="在这里插入图片描述">

如果有的时候进不了shell，可以先调用一下adb kill-server，然后再调用adb devices。

### 可能常用的ADB Shell命令

接下来是一些ADB的命令操作。通过adb命令，我们可以用python来操作的安卓设备。

### 屏幕截图

最常见的操作就是截图了，先调用screencap截图放到安卓设备里，然后再把截图下拉到电脑。

```
def take_screenshot():
    os.system("adb shell screencap -p /data/screenshot.png")
    os.system("adb pull /data/screenshot.png ./tmp.png")

```

### 下拉文件

下拉文件就是刚刚那个adb pull了，以公主连结为例，以下代码可以导出账号信息的xml，以后通过xml就可以登录了。

```
os.system(f"adb pull /data/data/tw.sonet.princessconnect/shared_prefs/tw.sonet.princessconnect.v2.playerprefs.xml ./user_info.xml")

```

### 上传文件

有了下拉自然就有上传了，通过adb push即可完成。以公主连结为例，以下代码可以完成账号的切换。

```
# 切换账号1
os.system("adb push ./user_info1.xml /data/data/tw.sonet.princessconnect/shared_prefs/tw.sonet.princessconnect.v2.playerprefs.xml")

# 切换账号2
os.system("adb push ./user_info2.xml /data/data/tw.sonet.princessconnect/shared_prefs/tw.sonet.princessconnect.v2.playerprefs.xml")

```

### 点击屏幕某个位置

```
def adb_click(center, offset=(0, 0)):
    (x, y) = center
    x += offset[0]
    y += offset[1]
    os.system(f"adb shell input tap {x} {y}")

```

### 输入文字

```
text = "YourPassword"
os.system(f"adb shell input text {text}")

```

### 删除字符

有的时候输入框会有输入的缓存，我们需要删除字符。

```
# 删除10个字符
for i in range(10):
    os.system("adb shell input keyevent 67")

```

### 查询当前运行的包名和Activity

通过以下代码，可以查询当前运行的程序的Activity，也可以顺便查包名。

```
adb shell dumpsys activity activities

```

<img src="https://img-blog.csdnimg.cn/6b48dd82efc540fcaf38cf86c57f0138.png#pic_center" alt="在这里插入图片描述">

### 停止某个应用

有时候会需要停止某个应用，需要提供应用的包名。

```
adb shell am force-stop tw.sonet.princessconnect

```

### 开启某个应用

开启某个应用需要提供包名以及Activity。

```
adb shell am start -W -n tw.sonet.princessconnect/jp.co.cygames.activity.OverrideUnityActivity

```

### 图像操作

对于图像的操作第一就是图像查找了，比如说像Airtest提供的这种，无非就是判断某个图像在不在截屏中，在的话在什么位置。

<img src="https://img-blog.csdnimg.cn/7a19b673e22f4e39bb207d7271a3ee18.jpeg#pic_center" alt="在这里插入图片描述"> 除此之外还需要一些抠图，比如说我们想获取账号的id，账号的等级，需要截取出一部分图片然后进行OCR操作。

<img src="https://img-blog.csdnimg.cn/6c5dd5870ad0433097f0137cf3c7fcf0.png#pic_center" alt="在这里插入图片描述">

### 图像查找

图像查找其实就是先拿到两张图片，然后调用cv2.matchTemplate方法来查找是否存在以及位置，这里匹配是一个相对模糊的匹配，会有一个相似度的概率，最高是1。我们设定一个阈值来判断模板是否在截屏里即可。

这里截屏如下，文件名为tmp.png：

<img src="https://img-blog.csdnimg.cn/b80edf58de524fa88a17883fa353f3f1.png#pic_center" alt="在这里插入图片描述">

模板如下：

<img src="https://img-blog.csdnimg.cn/eda51466c9864caeb47772e85c4a79e5.jpeg#pic_center" alt="在这里插入图片描述">

代码如下：

```
import cv2

def image_to_position(screen, template):
    image_x, image_y = template.shape[:2]
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print("prob:", max_val)
    if max_val &gt; 0.98:
        global center
        center = (max_loc[0] + image_y / 2, max_loc[1] + image_x / 2)
        return center
    else:
        return False

if __name__ == "__main__":
    screen = cv2.imread('tmp.png')
    template =  cv2.imread('Xuandan.png')
    print(image_to_position(screen, template))

```

运行上述代码后，可以看到模板匹配出来的概率为0.9977，位置为(1165, 693)，对于一张图片，左上角为原点，因为我的分辨率是1280 * 720，那么右下角的坐标就是(1280, 720)。可以看到我们这个选单其实就是刚好在右下角的位置。

<img src="https://img-blog.csdnimg.cn/7c0f34cc0afb4803904d9fd886f2b632.jpeg#pic_center" alt="在这里插入图片描述">

### 如何快速裁剪模板？（win10）

游戏脚本其实并不是代码很难写，而是需要截很多的图，这些图要保证分辨率和原始一样。我发现在win10如果用画图打开图片

<img src="https://img-blog.csdnimg.cn/9237822fc1ca4fb7bc319e6bd1fb5121.jpeg#pic_center" alt="在这里插入图片描述">

可以保证使用QQ截屏出来的分辨率，和图片本身的分辨率一样。

<img src="https://img-blog.csdnimg.cn/0f9ff0cd75ff4cd99eb8f0b469739d97.png#pic_center" alt="在这里插入图片描述">

这个时候直接用qq截屏出来的模板即可直接用于识别。

### 图像裁剪

接下来就是有时候需要裁剪一些图像了，当然我们的模板图片也可以通过裁剪图片的方式得到，这样的模板图片是最准的。

裁剪其实就是需要裁剪的位置，以及需要的高度和宽度，说白了就是一篇长方形的区域，下面的代码使用PIL库实现。

```
from PIL import Image

def crop_screenshot(img_file, pos_x, pos_y, width, height, out_file):
    img = Image.open(img_file)
    region = (pos_x, pos_y, pos_x + width, pos_y + height)
    cropImg = img.crop(region)
    cropImg.save(out_file)
    print("exported:", out_file)

if __name__ == "__main__":
    crop_screenshot("tmp.png", 817,556, 190, 24, "test_id.png")

```

上面的代码以截取玩家的id为例。

<img src="https://img-blog.csdnimg.cn/be96312ed68c4cdbab8f29270be8416a.png#pic_center" alt="在这里插入图片描述">

运行代码后，得到截图如下：

<img src="https://img-blog.csdnimg.cn/6db3a2a8f502457b8f183a386eae598c.jpeg#pic_center" alt="在这里插入图片描述">

### 简单的OCR

得到了以上的图片信息后就是进行OCR了，也就是光学字符识别。这里代码非常简单，只要调用API即可。

```
from PIL import Image
import pytesseract

image = Image.open('test_id.png')
content = pytesseract.image_to_string(image)   # 识别图片
print(content)

```

<img src="https://img-blog.csdnimg.cn/1fc856205d984af48680cc7f64e83b55.jpeg#pic_center" alt="在这里插入图片描述">

不过需要注意的一点就是pytesseract识别出来的结果会有空格符，换行符这样的符号，真正要用的时候进行一些字符的过滤即可。

### 关于Python技术储备

学好 Python 不论是就业还是做副业赚钱都不错，但要学会 Python 还是要有一个学习规划。最后大家分享一份全套的 Python 学习资料，给那些想学习 Python 的小伙伴们一点帮助！

#### 一、Python所有方向的学习路线

Python所有方向路线就是把Python常用的技术点做整理，形成各个领域的知识点汇总，它的用处就在于，你可以按照上面的知识点去找对应的学习资源，保证自己学得较为全面。

<img src="https://img-blog.csdnimg.cn/img_convert/9f49b566129f47b8a67243c1008edf79.png" alt="">

#### 二、学习软件

工欲善其事必先利其器。学习Python常用的开发软件都在这里了，给大家节省了很多时间。

<img src="https://img-blog.csdnimg.cn/img_convert/8c4513c1a906b72cbf93031e6781512b.png" alt="">

#### 三、入门学习视频

我们在看视频学习的时候，不能光动眼动脑不动手，比较科学的学习方法是在理解之后运用它们，这时候练手项目就很适合了。

<img src="https://img-blog.csdnimg.cn/afc935d834c5452090670f48eda180e0.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56iL5bqP5aqb56eD56eD,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="">

#### 四、实战案例

光学理论是没用的，要学会跟着一起敲，要动手实操，才能将自己的所学运用到实际当中去，这时候可以搞点实战案例来学习。

<img src="https://img-blog.csdnimg.cn/img_convert/252731a671c1fb70aad5355a2c5eeff0.png" alt="">

#### 五、面试资料

我们学习Python必然是为了找到高薪的工作，下面这些面试题是来自阿里、腾讯、字节等一线互联网大厂最新的面试资料，并且有阿里大佬给出了权威的解答，刷完这一套面试资料相信大家都能找到满意的工作。

<img src="https://img-blog.csdnimg.cn/img_convert/6c361282296f86381401c05e862fe4e9.png" alt=""> <img src="https://img-blog.csdnimg.cn/img_convert/d2d978bb523c810abca3abe69e09bc1a.png" alt="">

###### 这份完整版的Python全套学习资料已经上传CSDN，朋友们如果需要可以微信扫描下方CSDN官方认证二维码免费领取【`保证100%免费`】

<img src="https://img-blog.csdnimg.cn/1d2a69f2d57e4d1cb444037b17af8607.png" alt="">
