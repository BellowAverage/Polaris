
--- 
title:  Python安装教程-史上最全 
tags: []
categories: [] 

---


#### 文章目录
- <ul><li>- - - - - - <ul><li>- - - - - 


### 1. 前言：

​ 目前Python官网从2020-01-01就停止维护Python2.7版本

​ 目前Python官方推荐：使用Python3.X系列版本（不向下兼容python2.X版本）

​ 所以：惹怒了许多的Python2.X版本爱好者（不过Python3.X是未来的趋势）

​ 个人推荐：使用Python3.6 ~ Python3.8之间的版本

|Python官网|
|------
||

### 2. 进入首页，点击Downloads，选择Windows

<img src="https://img-blog.csdnimg.cn/cafd1ebce4504fd5936f056e60e84280.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aOs5p2w,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

### 3. 如下图：就可以看到许多的Python版本

**注意**：3.9版本（包括3.9）以上的无法在win7上安装

<img src="https://img-blog.csdnimg.cn/8aab7bceef094494ab221ad3b4f11645.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aOs5p2w,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

对前缀的说明：

​ 以Windows x86-64开头的是 64 位的 Python 安装程序；

​ 以Windows x86开头的是 32 位的 Python 安装程序。

对后缀的说明：

​ embeddable zip file ：表示.zip格式的绿色免安装版本，可以直接嵌入（集成）到其它的应用程序中；

​ executable installer ：表示.exe格式的可执行程序，这是完整的离线安装包，一般选择这个即可；

​ web-based installer ：表示通过网络安装的，也就是说下载到的是一个空壳，安装过程中还需要联网

### 4. 下载真正的 Python 安装包。

|Download Windows help file|：Python帮助文件
|------
|Download Windows x86-64 embeddable zip file|：64位可嵌入压缩包zip文件
|Download Windows x86-64 executable installer|：64位可执行.exe文件
|Download Windows x86-64 web-based installer|：64位基于网络安装文件
|Download Windows x86 embeddable zip file|：32位可嵌入压缩包zip文件
|Download Windows x86 executable installer|：32位可执行.exe文件
|Download Windows x86 web-based installer|：32位基于网络安装文件

### 5. 这里我选择的是：

“Windows x86-64 executable installer”，也即 64 位的完整的离线安装包。

<img src="https://img-blog.csdnimg.cn/7e31f1c86d9546038ed8326927942320.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aOs5p2w,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

### 6. 开始安装下载好的python离线包

双击下载得到的 python-3.7.8-amd64.exe，就可以正式开始安装 Python 了

#### 6.1

​ Install Now ：默认安装（直接安装在C盘，并且勾选所有组件并下载）

​ Customize installation：自定安装（可选择安装路径和组件）

​ Install launcher for all users(requires elevation) （默认勾选）

​ Add Python to PATH （一定要勾选，添加Python解释器的安装路径到系统变量，目的：为了操作系统更快的找到Python解释器）

<img src="https://img-blog.csdnimg.cn/970a7a4d46984de891622c78f8d1bd1c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aOs5p2w,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

|Documentation|：安装Python官方文档
|------
|Pip|：安装Python包管理器，可下载安装Python包
|tcl/tk and IDLE|：安装TK库和IDLE编辑器（开发环境）
|Python test suite|：安装标准库和测试套件
|Py launcher|：py 尾缀文件都以python解释器执行
|For all users|：所有用户都可使用

#### 6.2 全部都勾选

<img src="https://img-blog.csdnimg.cn/f14e745cad1e4e3eafc9764a267167a3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aOs5p2w,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

|Install for all users|：所有用户都可使用
|------
|Associate files with Python (requires the py launcher)|：将 py文件和python关联（需要python启动器）
|Create shortcuts for installed application|：为应用程序创建快捷方式
|Add Python to envirounment variables|：添加Python到虚拟环境
|Precompile standard library|：预编译标准库
|后两个都是Debug相关工具|：有pycharm这个IDE就不需要了

#### 6.3 勾选前五个

<img src="https://img-blog.csdnimg.cn/903b131bb1b3457db8d2ee7c3ded863b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aOs5p2w,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

#### 6.4 看到如下图就是安装成功了

<img src="https://img-blog.csdnimg.cn/c97e3af4a8fb4617985ba8f535bd266b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aOs5p2w,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

验证是否成功，按win+R，输入cmd ，输入Python回车

#### 6.5 如下图Python就是安装成功了

<img src="https://img-blog.csdnimg.cn/6f797017af7942fe9a33811ff2ac0c94.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aOs5p2w,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

#### 6.6 按win,就可以找到安装的Python

​ IDLE：Python编辑器

​ CPython：交互式命令行

按win,就可以找到安装的Python

​ IDLE：Python编辑器

​ CPython：交互式命令行

<img src="https://img-blog.csdnimg.cn/2f57a33112f84771bea2eb44400ff006.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aOs5p2w,size_15,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> Python下载与安装的美妙之旅就此完美落幕 下面将开启您自己的Hello World - - 代码造天下(带马找天下)

### **Pycharm下载与安装**


