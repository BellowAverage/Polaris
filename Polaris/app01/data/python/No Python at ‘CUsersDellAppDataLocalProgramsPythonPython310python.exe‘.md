
--- 
title:  No Python at ‘C:\Users\Dell\AppData\Local\Programs\Python\Python310\python.exe‘ 
tags: []
categories: [] 

---
## No Python at ‘C:\Users\Dell\AppData\Local\Programs\Python\Python310\python.exe’

`提示：这里简述项目相关背景：`

`提示：这里描述项目中遇到的问题：`

## 问题描述：

>  
 这里填写问题的分析：刚开始安装了python3.10,但因需要，于是通过双击python3.10的安装包来卸载python3.10（这里安装python的时候是选择了自动配置环境变量）。之后重新安装python2.7并修改pycharm中的解释器，pycharm可以正常运行。但是，在命令行中输入python却有问题，如下： 


<img src="https://img-blog.csdnimg.cn/c010acd359ea49249bd60e79747d8dfa.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAd2VpeGluXzQ0NjA2MTM5,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

## 原因分析：

>  
 这里填写问题的分析：这里我已经卸载了python3.10并安装了python2.7.后来觉得是环境变量的问题，这里环境变量配置的还是3.10的，所以会出错。 


<img src="https://img-blog.csdnimg.cn/e17a9464874a48b0a9b76ee7eaccd9f5.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAd2VpeGluXzQ0NjA2MTM5,size_15,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

## 解决方案：

>  
 于是，我把python2.7的环境变量置顶，放到最上面，成功解决！ 


<img src="https://img-blog.csdnimg.cn/0d659a7511f84b4b821305b2b58969f9.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAd2VpeGluXzQ0NjA2MTM5,size_15,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/3e1b3e3fe8d742d4978a567d37295eb2.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAd2VpeGluXzQ0NjA2MTM5,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">
