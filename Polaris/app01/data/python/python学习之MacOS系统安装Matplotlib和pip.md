
--- 
title:  python学习之MacOS系统安装Matplotlib和pip 
tags: []
categories: [] 

---
        今天终于学习完了《Python编程--从入门到实践》的第一部分，现在学习到了第二部分。我打算先学习项目2--数据可视化。

        在学习数据可视化的最开始是要先安装Matplotlib，书上用终端中pip的方法安装，但是会出现语法报错SyntaxError: invalid syntax，并且错误指向pip处。一开始我以为是我python版本的问题，但其实是电脑中没安装pip（/尴尬）。在我安装完pip之后就可以正常安装Matplotlib了。



####         1.下面介绍如何安装pip：

>  
 ****在终端中输入：   curl https://bootstrap.pypa.io/get-pip.py | python3**** 


        <img alt="3f41843518394c21b8aed82a32aa79fc.png" src="https://img-blog.csdnimg.cn/3f41843518394c21b8aed82a32aa79fc.png">

输入之后等待几分钟安装，如果显示Successfully uninstalled pip-版本号的话，就说明pip安装成功了！！



#### 2.如何安装Matplotlib

>  
 ****在安装完pip之后，在终端中输入： python3 -m pip install matplotlib**** 


<img alt="7379500a9a6c4d94b6ee04f290b1e39f.png" src="https://img-blog.csdnimg.cn/7379500a9a6c4d94b6ee04f290b1e39f.png">

同样是等待几分钟之后，Matplotlib就安装好了。



#### 3.PyCharm CE中的设置

        在安装完Matplotlib之后回到PyCharm CE之后，需要进行配置Matplotlib。步骤如下：

**第一步：点击Preferences**

<img alt="2de248b0ce944fab8d6acba7bb83ffeb.png" src="https://img-blog.csdnimg.cn/2de248b0ce944fab8d6acba7bb83ffeb.png">



**第二步：找到Python Interperter，双击列表中的matplotlib**

<img alt="c6f13c37c8da408ca013348715a5f869.png" src="https://img-blog.csdnimg.cn/c6f13c37c8da408ca013348715a5f869.png">



**第三步：点击对话框左下角的Install Package，等待几秒钟**

<img alt="a80fef67b5194f7aaabe24f5f66a248b.png" src="https://img-blog.csdnimg.cn/a80fef67b5194f7aaabe24f5f66a248b.png">

 <img alt="e7bd272fee274b90b418b24ec23c50c9.png" src="https://img-blog.csdnimg.cn/e7bd272fee274b90b418b24ec23c50c9.png">



        在配置完成后就可以正常运行数据可视化的程序了。

<img alt="77190a34034c4150bf85edc7140f9412.png" src="https://img-blog.csdnimg.cn/77190a34034c4150bf85edc7140f9412.png">



———本记录来自一个Python萌新up，希望各位大佬轻喷！谢谢！ 


