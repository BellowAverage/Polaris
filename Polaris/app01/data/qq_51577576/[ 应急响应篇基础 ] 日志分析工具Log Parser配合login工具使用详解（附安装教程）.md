
--- 
title:  [ 应急响应篇基础 ] 日志分析工具Log Parser配合login工具使用详解（附安装教程） 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - - - - - - <ul><li>- - - 


## 一、Log Parser介绍

>  
 LogParser是微软公司提供的一款日志分析工具，可以对基于文本格式的日志文件、XML文件和CSV文件，以及Windows操作系统上的事件日志、注册表、文件系统等等进行处理分析，分析结果可以保存在基于文本的自定义格式中、SQL或者是利用各种图表进行展示，这里详细讲解其安装方式及配合login工具使用。 


## 二、Log Parser下载

>  
 百度网盘下载链接在文末给出 官网下载链接如下 


```
https://www.microsoft.com/en-us/download/details.aspx?id=24659 

```

<img src="https://img-blog.csdnimg.cn/d94fbf5480f945a7a2a5aa14f132c9a5.png" alt="在这里插入图片描述">

>  
 下载如下 <img src="https://img-blog.csdnimg.cn/36c50b26dec54738af9b009dc5b2e11c.png" alt="在这里插入图片描述"> 


## 三、Log Parser安装

>  
 直接双击msi程序即进入安装界面 


<img src="https://img-blog.csdnimg.cn/90e0818a3bb34163aa41a222513c2276.png" alt="在这里插入图片描述">

>  
 同意协议 


<img src="https://img-blog.csdnimg.cn/323af7eaa3f249d99241d3a3688b4f43.png" alt="在这里插入图片描述">

>  
 选择完全安装 


<img src="https://img-blog.csdnimg.cn/dd3daec4c33a40a98cddb5a854f5a476.png" alt="在这里插入图片描述">

>  
 点击完全安装即开始安装，没截到图，这里是安装完成截图 


<img src="https://img-blog.csdnimg.cn/7994955228ae4a7394113b704d20eb96.png" alt="在这里插入图片描述">

## 四、Log Parser配置环境变量

>  
 我这里使用的是windows server 2012 选择控制面板，选择系统和安全，选择系统，选择高级系统设置 


<img src="https://img-blog.csdnimg.cn/8efcd5695ae7409cb15f1ed737987808.png" alt="在这里插入图片描述">

>  
 进入系统属性，选择高级，选择环境变量 选择path，这里箭头标错了，应该指向path，点击编辑 


<img src="https://img-blog.csdnimg.cn/b11b1a76a788451fa8322f6b8f4d6fbd.png" alt="在这里插入图片描述">

>  
 将Log Parser安装路径添加到path中，注意各个环境变量中间的分号 


```
C:\Program Files (x86)\Log Parser 2.2

```

>  
 然后确认 


<img src="https://img-blog.csdnimg.cn/ae0bdd4dc3fd44e8bf2d499b4f89fc20.png" alt="在这里插入图片描述">

## 五、验证安装成功

>  
 进入终端 


```
logparser

```

>  
 出现版本信息以及帮助信息即安装成功 


<img src="https://img-blog.csdnimg.cn/4eb1d0c70e504a1d988f20c30f30b445.png" alt="在这里插入图片描述">

## 六、配合login使用

>  
 Login工具需要使用到Log Parser，所以我们需要先安装Log Parser才能使用login，不然提取出来的表格是空的 


### 1、login下载

>  
 login下载链接： 


```
https://pan.baidu.com/s/1jGjBTlHurdXWJRFNK16nwg?pwd=j09w 

```

>  
 包含文件如下 


<img src="https://img-blog.csdnimg.cn/9af4c931a7604f90a5698ff756531403.png" alt="在这里插入图片描述">

### 2、提取日志

>  
 将提取出来的日志，放到logon下的data里面(如果存在之前的日志需要全部删除)，这里就没有将如何提取了，提取可以使用evtx，也可以手动提取 


<img src="https://img-blog.csdnimg.cn/dbaf268b28cf4a73902bde05e91ee013.png" alt="在这里插入图片描述">

### 3、运行run.bat

>  
 然后运行bin里面的Run.bat程序即可。 


<img src="https://img-blog.csdnimg.cn/128eea47619b4b3595d030b7657ec55b.png" alt="在这里插入图片描述">

>  
 很快就跑完了 


<img src="https://img-blog.csdnimg.cn/0003a3f35c384efa824174f8d40826c6.png" alt="在这里插入图片描述">

### 4、查看结果

>  
 查看data文件，发现生成了很多表格，这些表格就是它分析完成的表格 


<img src="https://img-blog.csdnimg.cn/6732169e2881495e8199b16c7e16864f.png" alt="在这里插入图片描述">

## 七、相关资源

  
