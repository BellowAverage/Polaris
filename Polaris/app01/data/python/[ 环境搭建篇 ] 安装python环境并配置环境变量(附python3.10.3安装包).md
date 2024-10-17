
--- 
title:  [ 环境搭建篇 ] 安装python环境并配置环境变量(附python3.10.3安装包) 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - <ul><li>- - <ul><li>- - - - - - - 


## 一、下载安装python

### 1、下载python

>  
 下载链接在文末给出，下载之后是一个python的exe程序 也可以去官网下载： 


```
https://www.python.org/downloads/windows/

```

<img src="https://img-blog.csdnimg.cn/9022bbc939244775ae3748c4aa420832.png" alt="在这里插入图片描述">

### 2、安装python

>  
 下载之后双击exe程序安装就OK了 


#### 1.选择安装方式

>  
 双击打开exe文件开始安装 勾选Add Python 3.6 to PATH 这个选项 在安装python的过程中，自动添加了环境变量，在3.0以前，环境变量都是手动添加的，很多人都在这里卡很久。 点击Customize installation 这种安装方式允许我们自由配置安装选项。 


<img src="https://img-blog.csdnimg.cn/44d58bd1a6b643bfb13743b769b02ff8.png" alt="在这里插入图片描述">

#### 2.配置安装选项

>  
 这里它默认都勾选上了，直接点击下一步，进入下一个配置界面 


<img src="https://img-blog.csdnimg.cn/6d34361718df4ca9a8c20d600cb16f7a.png" alt="在这里插入图片描述">

>  
 这里我们勾选Install for all users，勾上这个选项后，会在系统的环境变量里加入python，有关python的环境变量会设置在系统变量中，Path的值里面你刚刚安装好的python和python目录里的Scripts目录。 当在cmd命令窗口执行python或者pip命令时，计算机会从Path所设置的文件夹中寻找python.exe文件或者pip.exe文件，如果找不到就会报出类似“xx不是内部或外部命令”的错误。 修改python的安装位置，我这里是靶机，我就直接默认了，你可以根据自己的电脑情况选择安装。 


<img src="https://img-blog.csdnimg.cn/3a27e2dc6741482c8d9890e640a6e2af.png" alt="在这里插入图片描述">

#### 3.开始安装

>  
 上面我们点击install就开始安装了，能看到如下面板，需要等一会儿 


<img src="https://img-blog.csdnimg.cn/2d6a62f7cb624b4faa68f8dc6cc3e466.png" alt="在这里插入图片描述">

>  
 这是安装结束时的界面，出现了successful，关闭安装界面就可以了 


<img src="https://img-blog.csdnimg.cn/451c686d68c448218a7a6b041cc52d40.png" alt="在这里插入图片描述">

#### 4.查看安装目录

>  
 进入跟目录，默认是C:\Program Files\Python310 如果你没有安装在默认路径，你就打开自己的安装路径 在这个安装目录里，我们注意Scripts文件夹和python.exe， 这个python.exe就是python解释器，你在配置pycharm的时候还会用到它。 Scripts文件夹里放的是pip和easy_install第三方库管理工具 Lib\site-packages目录，是安装存储第三方库的地方。 


<img src="https://img-blog.csdnimg.cn/9626ef9d00e143388260faf3eb351b9b.png" alt="在这里插入图片描述">

#### 5.进入python交互式解释器

>  
 打开运行窗口，输入python即可 


<img src="https://img-blog.csdnimg.cn/23f19d611ff0456193f1a89c2df7d122.png" alt="在这里插入图片描述">

>  
 在交互式解释器里，可以验证一些简单的代码 交互式是指你写的代码，会立刻被执行并显示结果，这样及时反馈，有助于学习基础。 复杂的代码，例如函数，虽然也可以在这里编写，但写起来不方便，而且无法保存代码。 


#### 6.检查环境变量

>  
 在系统变量里找到Path变量，由于我们勾选Add Python 3.6 to PATH和Install for all users，所以，有关python的环境变量会自动配置。我们来检查一下。 


>  
 1、首先右击计算机进入属性然后选择其中的高级系统设置。 


<img src="https://img-blog.csdnimg.cn/a3b15308b0d940b7b005021d7f367d75.png" alt="在这里插入图片描述">

>  
 2、点击进入高级中的环境变量，进入环境变量编辑界面。 


<img src="https://img-blog.csdnimg.cn/3934a2f007114d9284231f6ef13b1673.png" alt="在这里插入图片描述">

>  
 3、查看系统变量path Path的值存在python和python目录里的Scripts目录路径，所以没有问题 


<img src="https://img-blog.csdnimg.cn/5cc9b664c8bb4ee1812f4627c4dfad70.png" alt="在这里插入图片描述">

## 二、python环境变量配置过程

>  
 有过不幸，你忘记勾选勾选Add Python 3.6 to PATH和Install for all users，那就手动配置环境变量吧 


### 1、配置环境变量

>  
 1、首先右击计算机进入属性然后选择其中的高级系统设置。 


<img src="https://img-blog.csdnimg.cn/b00e1d249a4b4971aca88263355c24f6.png" alt="在这里插入图片描述">

>  
 2、点击进入高级中的环境变量，进入环境变量编辑界面。 


<img src="https://img-blog.csdnimg.cn/6c1c1b342658408db9ac995bd0ef5a1d.png" alt="在这里插入图片描述">

>  
 3、在下方的系统变量中，双击打开path路径 添加python和python目录里的Scripts目录路径即可 


<img src="https://img-blog.csdnimg.cn/efcbfde35a834fa492ba3b6dcfe2b975.png" alt="在这里插入图片描述">

### 2、配置成功

>  
 打开运行窗口，输入python进入交互式解释器配置成功 


<img src="https://img-blog.csdnimg.cn/7a46c2927e7d4a8b801bcf891d284c94.png" alt="在这里插入图片描述">

## 三、相关资源


