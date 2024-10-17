
--- 
title:  【Python】如何将写好的Python代码打包成exe文件？ 
tags: []
categories: [] 

---
>  
 🆔作者简介：一名电子信息大学生. 📑 个人主页： 📫 如果文章知识点有错误的地方,请指正！和大家一起学习进步 🔥 如果感觉博主的文章还不错的话，还请不吝关注、点赞、收藏 




#### 文章目录
- - - <ul><li>- - - 


## 前言

最近在学习Python，因为刚刚比完2022年黑龙江省的电赛的B题自动泊车。在比赛中用到了Openmv视觉识别（用来识别黑线和T型的库角），而Openmv的视觉识别相关的代码就是用Python写的（比赛的时候没学Python），所以比完赛后就寻思着学学Python，做一个和Openmv相关的视觉识别项目。

`提示：以下是本篇文章正文内容`

## 操作步骤

### 1.Pyinstaller 模块下载

首先需要使用 **Windows+R** 快捷键打开如下图的运行窗口，并输入cmd点击 **确定** 。 <img src="https://img-blog.csdnimg.cn/c7fea8523b554ba3a1ab40366e3cb251.png#pic_center" alt="在这里插入图片描述"> 在弹出来的窗口中输入，如下指令：（安装需要等待几分钟，安装时间和网速有关）

```
pip3 install pyinstaller

```

<img src="https://img-blog.csdnimg.cn/2bb978c054294c0eadee3ff7aaeb1dda.png#pic_center" alt="在这里插入图片描述"> 如何检查是否安装成功呢？可以在窗口输入如下命令：

```
pip list

```

出现如下信息就是安装好了！

<img src="https://img-blog.csdnimg.cn/c8a92d5acba74afe89b8182910a7e528.png#pic_center" alt="在这里插入图片描述">

### 2.找到要打包的文件路径

找到 **需要打包的Python文件的路径**

<img src="https://img-blog.csdnimg.cn/b86b2cf2cea0495c929aeeb88f696e8d.png#pic_center" alt="在这里插入图片描述"> 选中该路径后 **输入cmd** 命令后，点击 **Enter** 键

<img src="https://img-blog.csdnimg.cn/9dbc5eab77ec44c5875b1c25268dad5c.png#pic_center" alt="在这里插入图片描述">

就会弹出 **带有文件路径的命令框**

<img src="https://img-blog.csdnimg.cn/ec213d24017b4c99b0245ddd7d8305ca.png#pic_center" alt="在这里插入图片描述">

### 3.输入pyinstaller -F name.py指令

**输入如下指令：**（PythonDraw是你要打包的文件名）

```
Pyinstaller -F PythonDraw.py

```

<img src="https://img-blog.csdnimg.cn/d190149213ea4221a1f8b6320d3beafb.png#pic_center" alt="在这里插入图片描述"> 执行完该命令后即可在下面的路径寻找 **生成的.exe文件**

<img src="https://img-blog.csdnimg.cn/6fcd5773c99648fea87588a409983e3f.png#pic_center" alt="在这里插入图片描述"> 并且你会发现文件夹下多出来 **三个文件**

<img src="https://img-blog.csdnimg.cn/83a81e0261e4490e888872b0bdc297cf.png#pic_center" alt="在这里插入图片描述"> 我们所需要的.exe文件就在 **dist文件夹** 下

<img src="https://img-blog.csdnimg.cn/9acca59168bc4837801cccd08e3fb4ab.png#pic_center" alt="在这里插入图片描述">

### 4.修改生成的.exe文件的图标（选做）

```
Pyinstaller -F -w -i tb.ico PythonDraw.py 打包指定exe图标打包 tb是图标文件名

```

自己做的软件都喜欢放上自己的图标，不过哪来那么多ico图片呢？ 我们可以自己生成，这里就给大家分享一个网站，可以把其他格式图片转成ico格式：

## 总结

```
Pyinstaller -F PythonDraw.py 打包exe

Pyinstaller -F -w PythonDraw.py 不带控制台的打包

Pyinstaller -F -w -i tb.ico PythonDraw.py 打包指定exe图标打包 tb是图标文件名

```
