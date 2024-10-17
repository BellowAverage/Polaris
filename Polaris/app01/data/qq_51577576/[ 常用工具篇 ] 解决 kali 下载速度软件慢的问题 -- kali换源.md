
--- 
title:  [ 常用工具篇 ] 解决 kali 下载速度软件慢的问题 -- kali换源 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - - - - - 


## 前言

>  
 今天搭建环境的时候发现镜像拉取十分的慢，跟蜗牛一样，刚开始还以为是网络出了问题，然后测了一下网速，也不慢，我挠头了，哈哈哈哈哈哈哈哈哈哈 


<img src="https://img-blog.csdnimg.cn/265f50a038b644c3b0ae3c9c7f5b021a.png" alt="在这里插入图片描述">

>  
 然后我突然想起来，我想我这台机器没换源，我吐了，果真的是没换源，然后我把源换了，直接飞起 


## 一、为什么要换源

>  
 其实换源的目的很明显，就是为了速度和稳定而已，相信大家看了前言也就有所感触 1.默认的源用的人多 2.主站在国外 基于这两个点，速度快不了。 


## 二、打开kali源配置文件

>  
 1、打开kali 命令行，切换为root用户 


```
su root

```

2、进入kali源配置文件看一下，果真是官方源

```
vim /etc/apt/sources.list 

```

<img src="https://img-blog.csdnimg.cn/4da29915c1ff480ba68ac5813f943ae6.png" alt="在这里插入图片描述">

## 三、更新为中科大的源

>  
 1、输入 i 进入编辑模式 我们把原来的官方源注释掉，在官方源前面输入 # 就注释掉了 在下面添加中科大的软件源，复制一个国内源（我这里选了第一个中科大的原），然后按下鼠标滚轮，就可以粘贴到文档中了 


```
#中科大源
deb http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib
deb-src http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib

```

<img src="https://img-blog.csdnimg.cn/3afeb9fa3e074ef999b48bc68195cb87.png" alt="在这里插入图片描述">

>  
 2、然后点击ESC进行退出编辑操作，然后输入 :wq保存退出 


<img src="https://img-blog.csdnimg.cn/64e3643dbf484c8ba944a36938ecdaea.png" alt="在这里插入图片描述">

## 四、更新软件源

>  
 输入 apt update进行软件源清单更新 


```
apt update

```

<img src="https://img-blog.csdnimg.cn/4595866b2bc34cd686fedbd45b3233de.png" alt="在这里插入图片描述">

>  
 apt update执行完成之后源就更换成功了 


## 五、kali国内外源地址

```
#中科大源
deb http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib
deb-src http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib
#浙江大学源
deb http://mirrors.zju.edu.cn/kali kali-rolling main non-free contrib
deb-src http://mirrors.zju.edu.cn/kali kali-rolling main non-free contrib
#阿里云源
deb http://mirrors.aliyun.com/kali kali-rolling main non-free contrib
deb-src http://mirrors.aliyun.com/kali kali-rolling main non-free contrib
#东软大学源
deb http://mirrors.neusoft.edu.cn/kali kali-rolling/main non-free contrib
deb-src http://mirrors.neusoft.edu.cn/kali kali-rolling/main non-free contrib
#新加坡kali源
deb http://mirror.nus.edu.sg/kali/kali/ kali main non-free contrib
deb-src http://mirror.nus.edu.sg/kali/kali/ kali main non-free contrib
deb http://security.kali.org/kali-security kali/updates main contrib non-free
deb http://mirror.nus.edu.sg/kali/kali-security kali/updates main contrib non-free
deb-src http://mirror.nus.edu.sg/kali/kali-security kali/updates main contrib non-free
#官方源
deb http://http.kali.org/kali kali-rolling main non-free contrib
deb-src http://http.kali.org/kali kali-rolling main non-free contrib

```
