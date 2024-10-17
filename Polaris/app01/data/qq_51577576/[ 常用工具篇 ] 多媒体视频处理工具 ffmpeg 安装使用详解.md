
--- 
title:  [ 常用工具篇 ] 多媒体视频处理工具 ffmpeg 安装使用详解 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ Vulhub是一个面向大众的开源漏洞靶场，无需docker知识，简单执行两条命令即可编译、运行一个完整的漏洞靶场镜像。旨在让漏洞复现变得更加简单，让安全研究者更加专注于漏洞原理本身。 




#### 文章目录
- - - - <ul><li>- - - - <ul><li>- 


## 一、ffmpeg介绍

>  
 FFmpeg是一套可以用来记录、转换数字音频、视频，并能将其转化为流的开源计算机程序。采用LGPL或GPL许可证。它提供了录制、转换以及流化音视频的完整解决方案。它包含了非常先进的音频/视频编解码库libavcodec，为了保证高可移植性和编解码质量，libavcodec里很多code都是从头开发的。 


## 二、手工下载安装

### 1、下载ffmpeg安装包

>  
 到ffmpeg官网按照下图所示下载 


```
https://ffmpeg.org/download.html 

```

<img src="https://img-blog.csdnimg.cn/3998032c0a924c2b8d877517da094d98.png" alt="在这里插入图片描述">

```
http://www.gyan.dev/ffmpeg/builds/

```

<img src="https://img-blog.csdnimg.cn/04eaaaf5a9514e5f8d17185251ca6229.png" alt="在这里插入图片描述">

>  
 下载完成 


<img src="https://img-blog.csdnimg.cn/79567714189449a3a8613d00bd72a027.png" alt="在这里插入图片描述">

### 2、解压到安装目录（自己选择）

>  
 解压文件，进入bin目录，能看到ffmpeg.exe、ffplay.exe、ffprobe.exe三个文件。 


<img src="https://img-blog.csdnimg.cn/8adc740436da4aa7be382416792c282f.png" alt="在这里插入图片描述">

### 3、配置环境变量

>  
 点击系统属性-&gt;高级系统设置-&gt;环境变量-&gt;用户变量 


<img src="https://img-blog.csdnimg.cn/52b4af35936e4239adca2eb2519227df.png" alt="在这里插入图片描述">

>  
 选择“Path”条目，点击“编辑-&gt;新建”，把第一步的bin文件夹路径复制粘贴进去，然后点击确定即可。 


<img src="https://img-blog.csdnimg.cn/2ce576cadac6471fa4530576812d211f.png" alt="在这里插入图片描述">

>  
 注意，此处我设置的是用户变量，仅当前windows用户可以使用，如果需要每个用户都能够使用，需要添加到“系统变量”的“Path”条目中。 


### 4、简单实用

#### 1、验证安装成功

```
ffmpeg -version

```

<img src="https://img-blog.csdnimg.cn/df837076bf444f2889d9e60d243948ef.png" alt="在这里插入图片描述">

#### 2、拼接音视频

>  
 采用idm下载的视频，分为两部分，音频和视频，合并一下 


<img src="https://img-blog.csdnimg.cn/6d5806060065422e840e17ad9f026062.png" alt="在这里插入图片描述">

```
ffmpeg -i 1006606804_nb3-1-30280.mp4 -i 1006606804-1-30077.mp4 out.mp4

```

<img src="https://img-blog.csdnimg.cn/f2e8af4babd24de0b909015f2f98b476.png" alt="在这里插入图片描述">

>  
 合并完成之后生成了一个新的mp4文件，这就是我自己命名的out.mp4 


## 三、利用pip下载安装

>  
 也可以使用pip直接安装（可能会报错）建议手工安装 


```
pip install FFmpeg

```

<img src="https://img-blog.csdnimg.cn/0687c34c2f414781a317adcde78ffb88.png" alt="在这里插入图片描述">
