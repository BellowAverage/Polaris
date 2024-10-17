
--- 
title:  Python3.9.0安装教程 
tags: []
categories: [] 

---
##### 一、下载安装步骤

1.官网下载地址： 下载Python3.9.0安装包 （最新的是3.10.6，这里下载的3.9.0版本，滑到下面下载特定版本） <img src="https://img-blog.csdnimg.cn/886b46d7483645fe9e3be2bb638f424f.png#pic_center" alt="下载特定版本"> ps:本机系统：Windows 10 （64位），去我的电脑查看，如图 <img src="https://img-blog.csdnimg.cn/8abeb71c699c4f0493d8d6292066c387.png#pic_center" alt="本机系统类型">

2.选择电脑对应的版本下载 <img src="https://img-blog.csdnimg.cn/5c478e78ca0143e5a263875c34652240.png#pic_center" alt="在这里插入图片描述"> 3.下载完成，开始安装

在安装界面你有两个选择：默认安装(Install Now) or 自定义安装(Customize installation)。

个人喜欢自定义安装，默认安装的安装路径太好找之后的安装位置，寻找起来较为困难，因此自定义安装一个浅目录，查找容易。

<img src="https://img-blog.csdnimg.cn/9edbeed6055f4e63b63944a66e36be41.png#pic_center" alt="在这里插入图片描述"> 自定义安装路径选项下的 “Add Python 3.9 to PATH”记得一定勾选上，它能够将 python.exe 文件添加到系统路径下，此时在系统自带的 cmd 窗口中可直接执行 Python 程序，进行编译，十分方便。 <img src="https://img-blog.csdnimg.cn/347d5f9e22ba41688de2f65ce86691af.png#pic_center" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/53c931615d874fceb0b7ad98a5ee28b8.png#pic_center" alt=" ">

你可以自定义选择(Browse)需要安装的路径，确认路径无误后点击安装(Install)： 【D:\MyDev\Python39】 <img src="https://img-blog.csdnimg.cn/fd7c8efc7a7e46ef9954dabba23f0d54.png#pic_center" alt="在这里插入图片描述">

##### 二、安装检查

1.打开cmd【快捷键win+R或者输入cmd】，检查下载的版本. <img src="https://img-blog.csdnimg.cn/8c608cd2e99042b48a217746092fa280.png#pic_center" alt="在这里插入图片描述"> 命令行输入【`python -V`】查看nodejs的版本号，输出版本号则安装成功！ ps：这里 v 一定要大写V！！ <img src="https://img-blog.csdnimg.cn/20c55b9acf594a4c85c4614c06770cc5.png#pic_center" alt="在这里插入图片描述">

##### 三、环境变量

说明：前面下载时勾选的"Add Python 3.9 to PATH"后会自动把python加入环境变量 <img src="https://img-blog.csdnimg.cn/d62b7f44c7ad4f889dced9d12892d0ff.png#pic_center" alt="在这里插入图片描述"> 若忘记勾选，手动添加，如下步骤： 比如，安装目录是【D:\Python3.9.0】，则此处需要增加D:\Python3.9.0和D:\Python3.9.0\Scripts两项配置，系统变量中添加 【D:\MyDev\Python39】和【D:\MyDev\Python39\Scripts】 <img src="https://img-blog.csdnimg.cn/f1cf8c3af2c5460b849f683c0724a148.png#pic_center" alt="在这里插入图片描述">

##### 四、IDLE 使用 下载好后Python自带编译工具

安装成功后，在我们的开始菜单中找到 Python 3.9 文件夹，点击打开，找到 IDLE(Python 3.9 64-bit)，双击运行，即可在其中调试 Python 代码了。 <img src="https://img-blog.csdnimg.cn/7cf9a8ebab584a80b6bb85ad87e2beb3.png#pic_center" alt="在这里插入图片描述"> 以上是Python 3.9.0 的安装方法，适合初学者学习，安装完成后，通常我们还要安装 pycharm，pycharm 是一种 Python IDE, 编写 Python 程序时，通常用此工具进行开发，调试和管理项目。
