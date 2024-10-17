
--- 
title:  Python之硬汉巴特勒 
tags: []
categories: [] 

---
## 一、前言

  2023年4月27日，NBA季后赛热火4:1淘汰雄鹿，实现黑八。全NBA联盟最硬气的男人——巴特勒，再次向全世界证明了他是NBA最硬气的男人。上一场刚狂轰56分大比分逆转雄鹿，这一场又是带领球队打出了血性，超高难度绝平球，加时关键进球，轰下42分8篮板4助攻2抢断1盖帽的全面数据逆转16分，鏖战加时后取胜，黑八淘汰兵强马壮的雄鹿队。这一场比赛包含了黑八、加时、逆转、绝平、跌宕起伏、精彩进球、紧咬比分、超强防守、身体对抗、精彩三分、精彩战术PK、三大主力被罚下场等等诸多经常比赛的元素。说实在的，经过这场比赛我被巴特勒圈粉了。所以我想做点什么，做点什么呢？那就用python画一副字符画，展现一下这个最硬气的男人吧。 <img src="https://img-blog.csdnimg.cn/381e19b668a04f99a9212170a5d96616.png" alt="在这里插入图片描述">

## 二、实现步骤

### 1、安装python

  我们可以使用anaconda3创建python虚拟环境，anaconda3的安装可以参照博文。安装完成后我们创建一个用于运行此打印巴特勒帅气字符图案的虚拟环境，环境名称btl。

>  
 (base) [wuhs@s142 ~]$ conda create -n btl python=3.8 (base) [wuhs@s142 ~]$ conda activate btl 


### 2、安装PIL库

  对图片的处理需要用到PIL库，所以我们需要在python虚拟环境下安装PIL库，安装方式如下。

>  
 (btl) [wuhs@s142 ~]$ pip install pillow 


### 3、编写python代码

  实现的基本思路就是选择一张帅气的巴特勒照片；使用python的PIL库将彩色照片降噪处理；然后转换为黑白图片；然后获取图片像素点的颜色值；将值转换为指定字符，黑色全部用硬气的Y代替；将字符写入文本文档；使用浏览器缩放到最小查看文本文档。

```
(btl) [wuhs@s142 ~]$ cd anaconda3/envs/btl/
(btl) [wuhs@s142 btl]$ cat btl.py
#!/home/wuhs/anaconda3/envs/btl/bin/python
# coding=utf-8
#引入PIL模块的包
from PIL import Image,ImageEnhance
#打开图片
im = Image.open('btl.jpg')
#增加对比度
im = ImageEnhance.Contrast(im).enhance(2.0)
#降低亮度
im = ImageEnhance.Brightness(im).enhance(0.9)
#重新设定图片像素
im2 = im.resize((400 int(im.size[1]/im.size[0]*400)))
#彩色图片转换为黑白图片
im2 = im2.convert('1')
X = ''
#获取像素点，黑色替换为Y字符，白色替换为空格
for i in range(im2.size[1]):
        for j in range(im2.size[0]):
                if im2.getpixel((j,i))== 0:
                        X += 'Y'
                else:
                        X += ' '
        else:
                X += '\n'
#将像素点值写入文本文档btl.txt                
with open('btl.txt', 'w') as f:
        f.write(X)

```

### 4、选择图片

  百度搜索巴特勒硬汉，找到一张自己最满意的照片，实际上我们还可以选择图片后自己配文字，下载图片，文件另存为btl.jpg。 <img src="https://img-blog.csdnimg.cn/e200cb69ab6642cf9c37e02db8d7d37e.png" alt="在这里插入图片描述">

### 5、执行python代码

  将btl.jpg图片上传到虚拟机环境，python脚本路径下，然后执行python代码。

>  
 (btl) [wuhs@s142 btl]$ python btl.py 


### 6、下载图片转换后的文本

  文本图案需要缩放才能看出全貌，我们将文本文档下载。

>  
 (btl) [wuhs@s142 btl]$ ll |grep -E “jpg|txt|py” -rw-r–r–. 1 wuhs wuhs 61861 Apr 28 16:16 btl2.jpg -rw-r–r–. 1 wuhs wuhs 607 Apr 28 16:17 btl2.py -rw-rw-r–. 1 wuhs wuhs 202537 Apr 28 16:17 btl2.txt -rw-r–r–. 1 wuhs wuhs 83244 Apr 28 14:35 btl.jpg -rw-r–r–. 1 wuhs wuhs 477 Apr 28 17:24 btl.py -rw-rw-r–. 1 wuhs wuhs 90225 Apr 28 16:03 btl.txt -rw-r–r–. 1 wuhs wuhs 187110 Apr 28 17:23 jp.jpg -rw-rw-r–. 1 wuhs wuhs 102255 Apr 28 17:24 jp.txt (btl) [wuhs@s142 btl]$ sz btl.txt 


### 7、浏览器查看字符文本文件

  使用浏览器打开btl.txt，利用浏览器的缩放功能将浏览器页面缩到最新，至此大功告成。当然此python代码可以打印任意图片。 <img src="https://img-blog.csdnimg.cn/de3e09cbb1e948708db9ff8cee0968bd.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/c3ee353a6e484ceaa43b9d4191e0f3ca.png" alt="在这里插入图片描述">
