
--- 
title:  最新openCV-Python安装教程（python：3.9||opencv-python：4.5.5） 
tags: []
categories: [] 

---
**opencv-python 版本：4.5.5 Python 版本： 3.9.10**

### 1. 升级pip

打开cmd，进入到你的pip.exe 所在位置（即在你的python 安装路径里找到scripts文件夹）<img src="https://img-blog.csdnimg.cn/06d9fa0426c8412dbe21ac217f2ee4bb.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATXIuenpj,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">比如我的路径是： **D:\python\Scripts**

<img src="https://img-blog.csdnimg.cn/b994d628717c4dd99e2aa5f50b943d3b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATXIuenpj,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在里插入图片描述"> 然后，升级你的pip 模块： 即在后面输入命令 **pip install --upgrade pip** 即可，按回车键，安装好后会提示你安装成功。

### 2. 安装wheel包

（wheel 包是一种类似于zip 格式的文件，此次安装wheel 模块，是为了后面安装opencv-python4.5.5.whl 做准备）<img src="https://img-blog.csdnimg.cn/79b200437c924e49a80f4f0ca5709d5a.png#pic_center" alt="install  wheel ">

在cmd 的Python 安装路径Scripts下输入 **pip install wheel** 即可，按回车键，会自动安装。

### 3. 安装 numpy 包

（numpy 包是一种科学计算的包，里面有很多包含矩阵，傅里叶变换，其他的很多计算，详情请百度下，本文只作简单介绍，这个包很有用，一定要安装） <img src="https://img-blog.csdnimg.cn/f958d9528a2a47459944dd70a825897d.png#pic_center" alt="install numpy">

在cmd 的Python 安装路径Scripts下输入**pip install numpy** 即可，按回车键，会自动安装。 安装好后会提示你安装成功。

### 4. 安装opencv-python

打开一个免费分享链接： **https://www.lfd.uci.edu/~gohlke/pythonlibs/** 然后找到 **OpenCV: a real time computer vision library.** 这一模块。 <img src="https://img-blog.csdnimg.cn/aa9aba04c25c4c9c85a3fc47ebcc2c5a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATXIuenpj,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="opencv version"> 根据你的Python 版本和CPU位数安装，比如说我的Python 版本是 3.9，CPU 是64位： opencv_python‑4.5.5‑cp39‑cp39‑win_amd64.whl (cp39 指CPython 3.9， amd64 指64位) 安装好后，把这个压缩包剪切到你的Scripts 文件夹中：<img src="https://img-blog.csdnimg.cn/cdedb5a433024b5a87b5a64feb4f67a9.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATXIuenpj,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="address"> 在cmd 的Python 安装路径Scripts下输入 **pip3.9.exe install D:\python\Scripts\opencv_python-4.5.5-cp39-cp39-win_amd64.whl**<img src="https://img-blog.csdnimg.cn/3522089248324b4abdd439af9b14fb66.png#pic_center" alt="install opencv-python"> pip 模块一定要符合你的Python 版本，比如说我的版本是Python 3.9，那么我就要选择pip3.9.exe，这个之前升级pip 后就自动安装好。 install 后面的是opencv-python 安装包的绝对路径，即

```
D:\python\Scripts\opencv_python-4.5.5-cp39-cp39-win_amd64.whl

```

按回车键，会显示安装成功。

### 最后：验证opencv-python 和numpy是否安装成功：

新建一个Python 工程： <img src="https://img-blog.csdnimg.cn/dcbdb651e3bd4ab58461351e94018714.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATXIuenpj,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="test-opencv"> 按照图片输入代码即可： 其中

```
C:\\Users\\15162\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\1.jpg 

```

是图片的绝对路径。 至此，opencv-python安装完毕。
