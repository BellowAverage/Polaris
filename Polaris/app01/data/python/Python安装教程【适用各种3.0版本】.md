
--- 
title:  Python安装教程【适用各种3.0版本】 
tags: []
categories: [] 

---


#### 文章目录
- - - - - - - <ul><li>- <ul><li>


## 1.前言：

Python官网： 解释器版本：python-3.11.0.exe 系统：Windows

## 2.Python下载
1. 点击网址进入Python官网下载。 <img src="https://img-blog.csdnimg.cn/3a8504ae9eb6431cb61aed6535ae660c.png#pic_center" alt="">1. 下载Python解释器。 <img src="https://img-blog.csdnimg.cn/9e5cfa28a82146eabf8caa2418374a31.png#pic_center" alt="" width="450">1. 下载完成我们会在文件夹里面看到一个名称为：python-3.11.0-amd64.exe的文件。<img src="https://img-blog.csdnimg.cn/cfa69f2424564f2dbd31dcda8f7da748.png#pic_center" alt="在这里插入图片描述">
## 3.Python安装
1. 在当前文件夹内找到刚刚下载好的Python-3.11.0.exe的应用程序。 <img src="https://img-blog.csdnimg.cn/e3c2e7458bb74c72b2b41f0ff134c381.png#pic_center" alt="在这里插入图片描述" width="700">1. 双击运行此程序，进入安装向导，勾选上最下面Add Python.exe to PATH（配置环境变量，让电脑能够运行Python），此时鼠标单击Install Now（默认Python安装到C盘）。 <img src="https://img-blog.csdnimg.cn/2ce5c0236dc44170ba5af30f88955825.png#pic_center" alt="在这里插入图片描述" width="600">1. 如果不想将Python安装到C盘，那么请选择下面的 Customize installation(自定义安装)。进入如下界面，一般会默认勾选，点击Next，进入路径选择。 <img src="https://img-blog.csdnimg.cn/a3f8ebf3a5174709901a731723b6dcc6.png#pic_center" alt="在这里插入图片描述" width="600">1. Advanced Options里面的选项勾选前五项，找到Browse，自定义安装路径（切记安装路径一定要`英文`，不要有中文存在，不然会出现问题），设置好安装路径，点击右下角 `Install` 安装。 <img src="https://img-blog.csdnimg.cn/09ef4d322bed433aaba7a02836344dfb.png#pic_center" alt="在这里插入图片描述" width="600">
## 4.安装成功

<img src="https://img-blog.csdnimg.cn/74ce2d805f2b496084274e4f0e9bd1a3.png#pic_center" alt="在这里插入图片描述" width="600">

## 5.运行 Python 确认是否安装成功
1. 当我们安装完成Python后，需要验证去Python是否安装正确。步骤：win+R 调出运行 ——&gt; 输入cmd 进入windows命令交互窗口 ——&gt;输入Python ——&gt; 按下Enter 回车键确认。 <img src="https://img-blog.csdnimg.cn/5c19ed813df945e092174cdf7a09d7c2.png#pic_center" alt="在这里插入图片描述" width="400">1. 在弹窗的命令行窗口中输入`python` 。此时出现 Python 版本号表示安装成功。你看到提示符 &gt;&gt;&gt; 就表示我们已经在Python交互式环境中了，可以输入任何Python代码，回车后会立刻得到执行结果。输入`exit()`并回车，或直接关闭窗口就可以退出了。（当然代码不是在这里编写）
<img src="https://img-blog.csdnimg.cn/aeb088d31a8c443cb52a0904e91fdf2d.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/5f70c4d98c0147e995e63b9f88eecc59.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/da8026b770f447458c15c28e599863f5.png#pic_center" alt="在这里插入图片描述">

## 6.如果出现以下情况：得到错误

<img src="https://img-blog.csdnimg.cn/30728cecdecf43a4b11d24200e22b651.png#pic_center" alt="在这里插入图片描述">

### 6.1解决方法：

#### 配置环境变量
- 这是因为Windows会根据一个Path的环境变量设定的路径去查找Python.exe，如果没找到，就会报错。如果在安装时漏掉了勾选Add Python.exe to PATH，那就要手动把Python.exe所在的路径添加到Path中。- 如果忘记勾选或者不会设置PATH的路径，那么请重新安装一遍Python，记得勾选上Add Python.exe to PATH 就OK了。- 设置PATH的步骤：
>  
 环境变量主要有用户变量和系统变量，需要设置的环境变量就在这两个变量中。用户变量是将自己下载的程序可以在cmd中使用，把程序的绝对路径写到用户变量中即可。 

1.  在桌面找到此电脑图标，鼠标右击——&gt;点击属性 <img src="https://img-blog.csdnimg.cn/11257a9e84a542ec9917b2083ef6f977.png#pic_center" alt="在这里插入图片描述" width="250"> 1.  在弹出的窗口右侧找到高级系统设置。 <img src="https://img-blog.csdnimg.cn/fa9eaf0843a74e44b61708e795394fa3.png#pic_center" alt="在这里插入图片描述" width="250"> 1.  点击右下角的环境变量 <img src="https://img-blog.csdnimg.cn/f900f93009b145249ac5cb50aea842bb.png#pic_center" alt="在这里插入图片描述" width="400"> 1.  在系统变量中找到`Path` 变量，鼠标单击编辑 <img src="https://img-blog.csdnimg.cn/8083ece3dd6c4fafa98db882a7acea55.png#pic_center" alt="在这里插入图片描述" width="400"> 1.  找到Python解释器的安装路径，复制到系统变量中 <img src="https://img-blog.csdnimg.cn/dcf3b20757404ed984b08556a318ea38.png" alt="在这里插入图片描述"> 1.  在弹出的系统变量编辑窗口中，单击新建按钮，并写入如图所示的两个文件路径。一个是Python安装路径，另一个是Python文件下的Scripts文件夹，点击确定。 <img src="https://img-blog.csdnimg.cn/9d605373804d4aa4a8f2515c4a8d48ad.png" alt="在这里插入图片描述"> 1.  此时再次win+R ,输入cmd 回车 输入Python，进入python编译环境，表示成功。 <img src="https://img-blog.csdnimg.cn/5a8f05272d854a3eaeb29ff8296f6850.png" alt="在这里插入图片描述"> 安装好Python解释器后就可以开始你的闯关之路了!  