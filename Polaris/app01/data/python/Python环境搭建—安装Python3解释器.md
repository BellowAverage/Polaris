
--- 
title:  Python环境搭建—安装Python3解释器 
tags: []
categories: [] 

---
>  
 🥇<font size="3" color="#8A2BE2">**作者简介：CSDN内容合伙人、新星计划第三季Python赛道Top1** <font size="3" color="red">🔥**本文已收录于Python系列专栏：**  </font> <font size="3" color="#0099ff">**💬订阅专栏后可私信博主进入Python学习交流群，进群可领取Python视频教程以及Python相关电子书合集**</font> `私信未回可以加V：hacker0327 备注零基础学Python` <img src="https://img-blog.csdnimg.cn/direct/bd6c194f87224cc7a9fb30e008916b50.png#pic_center" alt="在这里插入图片描述"></font> 


>  
 `订阅专栏附赠此专栏思维导图，可直接点击链接跳转学习` <img src="https://img-blog.csdnimg.cn/direct/8e6f83db6be546b392ac6694e7e5bffe.gif#pic_center" alt="在这里插入图片描述"> 


>  
 `零基础学Python系列专栏面向零基础读者倾心打造，永久免费订阅，一个专栏带你吃透Python，旨在帮助初学者从零开始学习Python` `从搭建环境、基础语法入手到深入学习掌握各种核心库和框架，学习利用Requests、Beautiful Soup、Scrapy等库从网络上获取数据、利用Pygame库进行游戏开发、利用NumPy、Pandas、Matplotlib等库进行数据分析，数据可视化、利用Django、Flask框架构建网站和Web应用程序等等，最终掌握并应用于实际项目。学习不断，持续更新，火热订阅中🔥` <img src="https://img-blog.csdnimg.cn/direct/6ff118ba83c447f6b2e796c1bae26825.png#pic_center" alt="在这里插入图片描述"> 




#### Python环境搭建—安装Python3解释器
- - - - 


## 💬Python简介

Python是一种高级的、解释型的、面向对象的编程语言，由Guido van Rossum于1989年开始开发，并于1991年首次发布。它具有简单易学、代码可读性强、功能丰富、跨平台等特点，因此在多个领域广泛应用。

⏺`Python语言特点`
- 简单易学： Python语法简洁清晰，易于理解和学习，适合初学者入门。- 开源： Python是开源的，用户可以免费获取并参与其开发。- 面向对象： Python支持面向对象的编程范式，允许开发者使用类和对象来组织和管理代码。- 解释型语言： Python代码不需要编译成机器语言，而是通过解释器逐行执行，使得开发和调试更加高效。- 跨平台： Python可以在多个操作系统上运行，包括Windows、Linux、macOS等。- 强大的标准库： Python拥有丰富的标准库和第三方库，涵盖了各种领域，从Web开发到科学计算再到人工智能等。
⏺`Python语言应用领域`
- Web开发： 通过框架如Django和Flask，Python可用于开发Web应用和网站。- 数据科学与人工智能： Python在数据处理、数据可视化、机器学习和人工智能等领域拥有强大的工具和库，如NumPy、Pandas、Matplotlib、TensorFlow和PyTorch等。- 自动化与脚本编程： Python可以用于编写脚本和自动化任务，简化日常工作流程。- 游戏开发： Python在游戏开发中也有一定应用，例如使用Pygame等库进行2D游戏开发。- 网络爬虫： Python可以用于编写网络爬虫，从网页中提取数据。- 教育： Python由于其简单易学的特性，被广泛用于学校和大学的教学。
## 💬安装Python

以Windows10系统为例进行安装

>  
 Python官网：  


✅第一步：访问上方链接进入Python官网，点击`Downloads-Windows-Python3.12.2`

<img src="https://img-blog.csdnimg.cn/direct/5755a9701d0b44aa94231fb9f9579818.png#pic_center" alt="在这里插入图片描述"> ✅第二步：下载完毕双击打开安装包`python-3.12.2-amd63.exe`

<img src="https://img-blog.csdnimg.cn/direct/8c8e7f5d0c8e41f7aca67a0b4ccf2d77.png#pic_center" alt="在这里插入图片描述"> ✅第三步：勾选`Add python.exe to PATH`然后选择`Customize installation`

<img src="https://img-blog.csdnimg.cn/direct/a280f430a3e44ac88f3d05da6b3df55d.png#pic_center" alt="在这里插入图片描述"> ✅第四步：点击`Next`

<img src="https://img-blog.csdnimg.cn/direct/09baede9678945619e43f24a9310511f.png#pic_center" alt="在这里插入图片描述"> ✅第五步：在除C盘的其他盘符新建一个空文件夹`Python312`,点击`Browse`选择创建的文件夹，确定无误后点击`Install`安装

<img src="https://img-blog.csdnimg.cn/direct/c180cbf1d8364954938dbe7c72520bde.png#pic_center" alt="在这里插入图片描述"> ✅第六步：点击`Close`

<img src="https://img-blog.csdnimg.cn/direct/a81d66f51b934ac0b47f923323c4354b.png#pic_center" alt="在这里插入图片描述">

## 💬检验是否安装成功

`win+R`输入`cmd`输入以下代码验证是否安装成功

>  
 `python --version` 输出python版本号则python安装成功 `pip --version` 输出pip版本和pip安装路径则pip安装成功 


出现以下提示即为安装成功

<img src="https://img-blog.csdnimg.cn/direct/04894ae86a1f4c38af3d248f6c720f3a.png#pic_center" alt="在这里插入图片描述">

## 💬结束语

>  
 以上就是零基础学Python之Python环境搭建—安装Python3解释器 
 - `专栏订阅地址:` - `专栏订阅者可私信博主领取专栏订阅福利，进入Python学习交流群，如私信未回可以加V：hacker0327 备注零基础学Python`- `此专栏内容会持续更新直到完结为止(如有任何纰漏请在评论区留言或者私信）` 


<img src="https://img-blog.csdnimg.cn/direct/58bfd8c234304ff38ff6a5d4680bbbf4.png#pic_center" alt="在这里插入图片描述">
