
--- 
title:  Python搭建编程环境-安装Python3解释器 
tags: []
categories: [] 

---
>  
 ✅作者简介：CSDN内容合伙人、阿里云专家博主、51CTO专家博主、新星计划第三季python赛道Top1🏆 📃个人主页： 🔥欢迎大家订阅系列专栏： 💬个人格言：不断的翻越一座又一座的高山，那样的人生才是我想要的。这一马平川，一眼见底的活，我不想要,我的人生，我自己书写，余生很长，请多关照，我的人生，敬请期待💖💖💖 


<img src="https://img-blog.csdnimg.cn/92b6f8a7e4c34feba8b20fb5583de221.gif#pic_center" alt="在这里插入图片描述">



#### Python编程环境搭建-安装Python3解释器
- - - - - - 


## Python简介

Python的创始人是荷兰的一位计算机程序员吉多·范罗苏姆(**Guido van Rossum**）江湖人称鬼叔，据说是为了打发圣诞节的无趣决定开发一个新的编程语言，做为ABC 语言的一种继承。
- Python是一种`解释型语言`：开发过程中没有了编译的环节，类似于Java和JavaScript语言- Python是一种`交互式语言`：你可以在Python提示符&gt;&gt;&gt;直接执行代码 <img src="https://img-blog.csdnimg.cn/0a1c2b34d25e481db7e0ba9ed27b6949.png" alt="在这里插入图片描述">- Python是一种`面向对象语言`：Python支持面向对象的风格或代码封装在对象的编程技术。
⏺`Python语言的特点`
- 易于学习：Python语言结构简单，语法简单易学- 易于阅读：Python代码的定义很清晰- 易于维护：Python的源代码非常容易维护- 拥有广泛的库：Python最大的优势之一就是有丰富的库，使用时安装完毕导入即可- 可移植：Python已经被移植到许多平台(Windows,Linux…）- 可扩展：想要编写一些不愿开放的算法，可以使用C或C++进行编写，然后用Python调用- 可嵌入性：可以把Python嵌入C/C++程序，从而向程序用户提供脚本功能。- 可交互：可以在Python提示符&gt;&gt;&gt;直接执行代码- 解释型：Python运行之前不需要编译
⏺`Python语言的应用领域`
- 网络爬虫- Web开发- 人工智能- 自动化办公- 数据分析- 游戏开发
## 安装python

**以windows10系统为例进行安装**

`python官网`：

`第一步`：访问上方链接进入Windows版本python安装官网

<img src="https://img-blog.csdnimg.cn/371f88f2ac8e43bb86f1907bc721bae7.png" alt="在这里插入图片描述"> `第二步`：`Ctrl+F`输入`3.7.5`(建议安装python旧版本较稳定，这里以Python3.7.5为例)

查看计算机操作系统版本：`此电脑右击点击属性查看` <img src="https://img-blog.csdnimg.cn/2b5cfef599f94dcab8349933388d9197.png" alt="在这里插入图片描述"> 如果是64位操作系统点击`Download Windows x86-64 executable installer` 如果是32位操作系统点击`Download Windows x86 executable installer`

<img src="https://img-blog.csdnimg.cn/0fdc253495c64cf0bbc50ed11b9c0cf3.png" alt="在这里插入图片描述"> `第三步`：双击下载好的安装程序 <img src="https://img-blog.csdnimg.cn/84b8d8849c204a76b48272f48e8f8588.png" alt="在这里插入图片描述"> `第四步`：勾选添加环境变量选择自定义安装

>  
 需要提前在除C盘的其他盘符新建一个`Python37`文件夹（这里我在E盘新建了Python37文件夹） 一定要勾选Add Python 3.7 to PATH（不勾选需要自己添加环境变量） 


<img src="https://img-blog.csdnimg.cn/2fd3db91d00942389418664ac567efb2.png" alt="在这里插入图片描述"> `第五步`：不做修改点击Next

<img src="https://img-blog.csdnimg.cn/6c19a059f2a940fc8e94f5d1f2375de9.png" alt=""> `第六步`：不做更改点击Browse选择你新建的Python37文件夹，确认无误后点击Install

<img src="https://img-blog.csdnimg.cn/ead5fe1b363b4df5a9edb39af33dd3ea.png" alt="在这里插入图片描述"> `第七步`：等待安装完成点击`Close`

<img src="https://img-blog.csdnimg.cn/581a68e000614a7096f740d52d1dfe58.png" alt="在这里插入图片描述">

## 手动添加环境变量

如果在安装Python第四步没有勾选`Add python37 to PATH`则需要手动添加环境变量(`若勾选了跳过此步骤`)

<img src="https://img-blog.csdnimg.cn/2d20177fa1df44fa8957cd5613c8e0ef.png" alt="在这里插入图片描述">

💬`此电脑右击选择属性`➡`高级系统设置`➡`环境变量`➡`Path编辑添加`

<img src="https://img-blog.csdnimg.cn/8c4d8d7a4f6e4af19d3cc5624fa1f05b.png" alt="在这里插入图片描述"> 将自己的Python37路径和Python安装路径下的Scrpits路径添加进去 `E:\Python37` `E:\Python37\Scripts`

<img src="https://img-blog.csdnimg.cn/29349ad9f3f44f22aa8a21dfb62f3496.png" alt="在这里插入图片描述">

## 验证是否安装成功

win+R输入cmd输入以下代码验证是否安装成功

>  
 `python --version` 输出python版本号则python安装成功 `pip --version` 输出pip版本和pip安装路径则pip安装成功 


<img src="https://img-blog.csdnimg.cn/3f9715a1329b4ceab8271db555fe503d.png" alt="在这里插入图片描述">

## 人生苦短，我用Python

使用自带的IDLE运行第一个Python程序 `只是用IDLE进行举例，Python开发大多使用Pycharm，IDLE只能执行简单的程序`

```
print("人生苦短,我用Python")

```

<img src="https://img-blog.csdnimg.cn/821178c889e24c7590db0bc072cd45f4.png" alt="在这里插入图片描述">

## 结束语🥇

>  
 以上就是Python基础入门篇之Python环境搭建-安装Python3解释器 
 - `欢迎大家订阅系列专栏:`- `此专栏内容会持续更新直到完结为止(如有任何纰漏请在评论区留言或者私信）` 


>  
 感谢大家一直以来对hacker的支持 你们的支持就是博主无尽创作的动力💖💖💖 


<img src="https://img-blog.csdnimg.cn/bdd237d869be4fee9ba4de0f100e35a8.gif#pic_center" alt="在这里插入图片描述">
