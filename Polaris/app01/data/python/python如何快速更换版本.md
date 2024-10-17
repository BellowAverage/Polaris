
--- 
title:  python如何快速更换版本 
tags: []
categories: [] 

---
window环境，由于python3.10版本没有twisted对应的版本，需要更换到python11（VScode）

从python10到python11:

1、进入终端查看python版本，可以看到是python10版本

<img src="https://img-blog.csdnimg.cn/62c2db5823e043e0ab758edc94a1a5ee.png" alt="62c2db5823e043e0ab758edc94a1a5ee.png"> 

2、从python官网下载python11版本，下载保存为python11的文件夹（环境变量可以不添加）

<img src="https://img-blog.csdnimg.cn/a2f993d4fc354bdb9bcbfe8683a5b3b2.png" alt="a2f993d4fc354bdb9bcbfe8683a5b3b2.png"> 

3、打开环境变量，点击系统变量里的Path，双击进入，添加新python版本的环境变量，在原来python版本复制修改一下就行

<img src="https://img-blog.csdnimg.cn/5e3789bd4f0648cfa97da4bb06fead9a.png" alt="5e3789bd4f0648cfa97da4bb06fead9a.png"> 

4、把新版本的环境变量上移到旧版本的python就可以了

<img src="https://img-blog.csdnimg.cn/99a9eddcd769482680bf78a27be64867.png" alt="99a9eddcd769482680bf78a27be64867.png"> 

5、与系统变量一样，新版本在旧版本上面

<img src="https://img-blog.csdnimg.cn/4e47dc35016d46d59ff29d652ee45ef6.png" alt="4e47dc35016d46d59ff29d652ee45ef6.png">

6、重新进入终端，输出python，可以看到，版本已切换。

<img src="https://img-blog.csdnimg.cn/1345d53a782e45b78c4ecd877398f615.png" alt="1345d53a782e45b78c4ecd877398f615.png">

7、打开一个python文件，在vscode中可以切换： <img src="https://img-blog.csdnimg.cn/580cbe5ac9ac4277802dda348ed4bad9.png" alt="580cbe5ac9ac4277802dda348ed4bad9.png">

 最后，缺点就是得重新在新的python版本重新下载文件，需要什么在新版本python文件夹中，导航栏中输出cmd进入终端下载，注意更新pip版本最好！
