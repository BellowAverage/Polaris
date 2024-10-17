
--- 
title:  安装最新版Visual Studio Code来开发Python应用程序 
tags: []
categories: [] 

---
## 安装最新版Visual Studio Code来开发Python应用程序

### Develop Python Applications by Installing the Latest Visual Studio Code

#### 1. 下载和安装Python最新版3.12.0

访问Python官网： ,可以获取Python最新版3.12.0的安装包。

具体安装和使用步骤，请参见笔者文章：

#### 2. 获取并安装Visual Studio Code最新版

打开官网，访问Visual Studio Code官网页面 

<img src="https://img-blog.csdnimg.cn/79f53ecb145043c4ba7b2928e7a6eaf7.png" alt="在这里插入图片描述"> 点击主页面右上角**Download**进入到下载页面。

选择Windows 64位安装程序，点击下载VS Code最新版1.83.1。

<img src="https://img-blog.csdnimg.cn/877fb9c8e77b4cf6a3774c471e276503.png" alt="在这里插入图片描述"> 选择下载页面左侧的Windows下的**User Installer x64**选型，下载64位安装程序。

<img src="https://img-blog.csdnimg.cn/a0e6e6d764f3471d9e18cf34c2b1bf44.png" alt="在这里插入图片描述"> 开始下载…

如果尚未开始下载，可以点击页面上方蓝色链接**Try this direct download link**(尝试点击直接下载链接)完成下载。

下载完毕后，安装文件**VSCodeUserSetup-x64-1.83.1.msi**可在Windows的**下载**文件夹里找到。

#### 3. 安装Visual Studio Code

当下载结束时，双击名为**VSCodeUserSetup-x64-1.83.1.msi**的安装程序，开始Visual Studio Code安装。 <img src="https://img-blog.csdnimg.cn/cb1f6d2ea28e460695c34892097264af.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/caacb94fab2946df98261829a88a6ac2.png" alt="在这里插入图片描述"> 以上对话框中，复选**Add to PATH**，即增加安装路径到环境变量**PATH**，这样，安装完毕后，可在命令行用python命令直接启动交互式命令行Python开发环境。点击**Next**继续。 <img src="https://img-blog.csdnimg.cn/c6cb533c70fa4e439725402cc5add335.png" alt="在这里插入图片描述"> 点击**Install**开始安装。 <img src="https://img-blog.csdnimg.cn/590f2b89b25f4095897be516f7f4558f.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/8effd58cad824cd5b33de96fb6b0d971.png" alt="在这里插入图片描述"> 安装完毕后，点击Finish完成安装，退出安装向导。

#### 4. 安装必要的Extension

为了使Python的强大功能，在VS Code这个同样强大的IDE平台上发挥作用，就需要安装必要的Extension(扩展程序)。

###### 1） Python

具有Intellisense功能, 可以实现代码格式化、自动联想补全代码等功能。 <img src="https://img-blog.csdnimg.cn/668162f5b45543e981e8027a183a7e79.png" alt="在这里插入图片描述">

###### 2） Tabnine AI

<img src="https://img-blog.csdnimg.cn/21a91e2722c2499c83d7835279c79d01.png" alt="在这里插入图片描述"> 具有AI代码补全功能，在经验人士的操作下，能快速写出高质量的Python代码。

>  
 注：在VS Code的Marketplace, 还有很多有趣的、相关的Extension, 如果需要安装，可以在VS Code的扩展(Extension)搜索得到更多的Extension, 可随时安装或者卸载。 


#### 5. 运行Python应用程序

安装完毕后，运行第一个Python应用程序。

<img src="https://img-blog.csdnimg.cn/64a56aa09f524df699b68d4468008a33.png" alt="在这里插入图片描述"> 仅仅写一个最简单的Python程序**hello_world.py** 就可以验证了。

```
print(“Hello, world!”)

```

<img src="https://img-blog.csdnimg.cn/b3e8fdccca054353b4613758d0ec4139.png" alt="在这里插入图片描述"> 如上图，在Visual Studio Code运行该程序后，在Terminal（终端）可以看到打印输出结果:

```
Hello, world!

```

让我们继续写代码吧，来发挥Visual Studio Code和其Python的Extension的强大功能吧。

关于Python编程，笔者会持续推出好文。…

喜欢就点赞吧！欢迎关注。😊
