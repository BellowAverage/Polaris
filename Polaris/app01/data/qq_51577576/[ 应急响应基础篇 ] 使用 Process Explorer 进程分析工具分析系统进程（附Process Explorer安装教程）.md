
--- 
title:  [ 应急响应基础篇 ] 使用 Process Explorer 进程分析工具分析系统进程（附Process Explorer安装教程） 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - - - - <ul><li>- <ul><li>- - - - - - 


## 一、环境介绍

>  
 在应急响应过程中，进程分析是至关重要的。 这里简单介绍一下windows官方提供的进程分析工具Process Explorer，包含他的简单介绍，下载及其简单使用。 


## 二、Process Explorer介绍

>  
 Process Explorer可以看成是一个加强版的任务管理器。 在较早的Windows版本中，任务管理器提供的功能是非常简单的（比如查看CPU、内存的使用情况，强制结束进程等），很难满足我们高级一些的需求。在这种情况下，Process Exploere就应运而生了，大大的方便了我们工作中监测进程和排除故障的工作。 这里我会从实际应用的角度对Process Explorer的一些功能点进行简单的介绍。 


## 三、Process Explorer下载

>  
 Process Explorer是微软官方提供的，直接在官网下载就可以了 官网下载： 


```
https://learn.microsoft.com/zh-cn/sysinternals/downloads/process-explorer

```

## 四、Process Explorer使用

### 1、替换任务管理器

>  
 Process Explorer提供了相对与任务管理器更加强大实用的功能，所以有的时候就会想着直接把任务管理器给替换掉得了。 Process Explorer提供了这样一个功能，可以在用户触发打开任务管理器的操作的时候直接打开Process Explorer。 


#### 1.操作步骤

>  
 选项（Options） --&gt; 替换任务管理器（Replace Task Manager） 


<img src="https://img-blog.csdnimg.cn/e92cfa2285844dcb9ae751334a1ed399.png" alt="在这里插入图片描述">

#### 2.替换成功

>  
 之后在我们运行任务管理器打开的就是Process Explorer了。 


#### 3.taskmgr打开

```
taskmgr

```

<img src="https://img-blog.csdnimg.cn/9c753c6d036547d1841868ae98fcd78d.png" alt="在这里插入图片描述">

#### 4.Ctrl+Shift+Del打开

>  
 Ctrl+Shift+Del的时候打开任务管理器 


<img src="https://img-blog.csdnimg.cn/3e657e27f6af430f9484b4f607763210.png" alt="在这里插入图片描述">

### 2、查看当前系统中运行的进程

#### 1.树形图展示进程

>  
 Process Explorer对进程以树形图的形式进行展示，这样方便我们观察父子进程之间的关系。从这里我们可以看出来，绝大部分的窗体应用程序都是wininit.exe的子进程 


<img src="https://img-blog.csdnimg.cn/c31cd24ac9bf4fc890f350a4338a1a9b.png" alt="在这里插入图片描述">

#### 2.颜色标示不同状态的进程

>  
 Process Explorer会以不同的颜色标示不同状态的进程 


<img src="https://img-blog.csdnimg.cn/7763783289ee481fb8c6613ce63e5e3d.png" alt="在这里插入图片描述">

>  
 这里我弄了一个中英文对照，因为我有汉化版，汉化版下载链接在文末给出 


<img src="https://img-blog.csdnimg.cn/b04f71368a5e41b887cd3958ebb525b8.png" alt="在这里插入图片描述">

#### 3.选择显示不同字段

>  
 我们还可以通过右键点击右侧列头选择显示我们感兴趣的属性 


<img src="https://img-blog.csdnimg.cn/44ba6867722945ffa1cda925db2e83c6.png" alt="在这里插入图片描述">

>  
 这里我弄了一个中英文对照，因为我有汉化版，汉化版下载链接在文末给出 


<img src="https://img-blog.csdnimg.cn/fde8b14c21a24f9eac6f1831d6bc13ee.png" alt="在这里插入图片描述">

### 3、查看进程的详细信息

>  
 如果我们对某个进程的感兴趣，我们可以双击这个进程查看它的详细信息Command line和Current directory这两个属性比较重要。 


```
Command line: 
启动进程的时候调用的命令。从这里我们可以了解怎么样去调用这个进程，和有关当前进程启动的详细信息。
Current directory: 
当前进程活动所在的文件夹。

```

<img src="https://img-blog.csdnimg.cn/8abd0534434b4ec7b27beec5270ef1cc.png" alt="在这里插入图片描述">

### 4、查看文件正在被什么进程占用

>  
 我们在操作文件（删除、重命名等）的时候遇到错误提示，说文件正在被其他进程占用，无法执行操作。这个时候可以打开Process Explorer对文件进行查找： 


```
Ctrl + f

```

>  
 输入要查找的文件名就可以看到有那些进程正在使用这个文件了，双击搜到的进程Process Explorer会在下面高亮显示出对应的文件句柄。 从这里我们可以强制关闭对应的句柄以达到不让文件被继续占用的目的。 


<img src="https://img-blog.csdnimg.cn/6775e18132384d7881eb0db6bb9737d3.png" alt="在这里插入图片描述">

### 5、实时监控系统的性能

>  
 通过视图(View) --&gt; 系统信息(System Info)我们可以打开Performance窗口查看过去一段时间内系统的性能数据 


<img src="https://img-blog.csdnimg.cn/40d2f1529f284445a4fee8fefeee1d7c.png" alt="在这里插入图片描述">

>  
 我们也可以通过设置把感兴趣的性能数据固定在任务栏里显示 


<img src="https://img-blog.csdnimg.cn/b78e9f37facc4dc495c891c80bc69d36.png" alt="在这里插入图片描述">

### 6、获取Dump文件

>  
 Dump文件是进程的内存镜像，通常在进程没有反应或者崩溃的时候我们需要借助Dump文件来分析进程里面发生了什么，Process Explorer提供了一个快捷的方式来获取Dump文件。 直接右键，创建就可以了Create Dump 我们可以根据需要选择获取最小的dump还是完整的dump文件。 


<img src="https://img-blog.csdnimg.cn/7bba58ffa6b84b8bb1ad14372ad398f1.png" alt="在这里插入图片描述">

### 7、官方文档

>  
 Process Explorer是很强大的，还有很多的功能这里就不详细介绍了，有需要的可以看官方文档，链接如下 


```
https://windowsexplored.com/2012/01/31/resolve-symbols-in-process-explorer-monitor-without-installing-the-debugging-tools/

```

## 五、相关资料

  
