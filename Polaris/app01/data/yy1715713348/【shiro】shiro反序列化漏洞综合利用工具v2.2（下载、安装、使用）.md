
--- 
title:  【shiro】shiro反序列化漏洞综合利用工具v2.2（下载、安装、使用） 
tags: []
categories: [] 

---
### 1 工具下载
1. shiro反序列化漏洞综合利用工具v2.2下载： 链接：https://pan.baidu.com/s/1kvQEMrMP-PZ4K1eGwAP0_Q?pwd=zbgp 提取码：zbgp1. 其他工具下载： 除了该工具之外，上还有其他大佬贡献的各种工具，有许多python编写的工具，功能简单，可以作为理解shiro漏洞原理并编写自己工具的教材。
### 2 依赖环境安装
1. **说明**：shiro反序列化漏洞综合利用工具v2.2是采用java编写的，需要使用java8环境来解析1. **下载java8环境**：可以在下载java8的安装包，根据自己系统情况选择适合自己的安装包。如果是win64系统可以按网盘链接下载：https://pan.baidu.com/s/1Yg7fq5_5zOMR6UphAA896w?pwd=e7hk 提取码：e7hk。 <img src="https://img-blog.csdnimg.cn/35b55d3197774a91b6711a0e290ad27a.png" alt="在这里插入图片描述">1. **安装java8**。右键刚下载到的exe安装包，以管理员方式运行，建议采用默认选项。1. **设置系统环境变量**。如下图新增JAVA HOME参数设置值为java的安装路径，并在path参数中新增两个值。 <img src="https://img-blog.csdnimg.cn/7763cf14d53945b5a77a86e6602fb6fa.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/8f12b1503d0c43eba9a3dfddd35a0839.png" alt="在这里插入图片描述">1. **验证是否安装成功**。按win+R弹出cmd窗口，输入命令`java -version`，查看回显版本是否如下图，以1.8开头说明安装成功。 <img src="https://img-blog.csdnimg.cn/067c3eb03ca9440390605c1cf58bb8bc.png" alt="在这里插入图片描述">1. 对于原先有安装其他版本导致无法查询到Java8的，请另找教程解决。
### 3 使用
1. 找到刚下载的“shiro反序列化漏洞综合利用工具v2.2”，解压，打开文件夹，可以看到里面有一个jar文件和一个文件夹，文件夹内的文件是存放key的字典。 <img src="https://img-blog.csdnimg.cn/3b99ff3075984f78b06b84ec177220d4.png" alt="在这里插入图片描述">1. 在该层文件夹地址栏处输入cmd并回车，打开终端，此时终端的路径定位在该文件夹处。 <img src="https://img-blog.csdnimg.cn/81d4a36c030c4774a19baaeca6668552.png" alt="在这里插入图片描述">1. 输入命令`java -jar shiro_attack-2.2.jar`，以java环境执行该文件。 <img src="https://img-blog.csdnimg.cn/0edfda2a9dfe42819f34b28a481b2236.png" alt="在这里插入图片描述">1. 弹出工具窗口如下。 <img src="https://img-blog.csdnimg.cn/86ab3bf9e7d049e884d9b119348bcd1a.png" alt="在这里插入图片描述">1. 具体使用方法在后续复现过程中再体现。
## 学习资料分享

当然，**只给予计划不给予学习资料的行为无异于耍流氓**，### 如果你对网络安全入门感兴趣，那么你点击这里**👉**

**如果你对网络安全感兴趣，学习资源免费分享，保证100%免费！！！（嘿客入门教程）**

**👉网安（嘿客）全套学习视频👈**

我们在看视频学习的时候，不能光动眼动脑不动手，比较科学的学习方法是在理解之后运用它们，这时候练手项目就很适合了。

#### 

#### <img src="https://img-blog.csdnimg.cn/img_convert/d1c617b78ee48eda7601e5b803e69276.png" alt="img">

#### **👉网安（嘿客红蓝对抗）所有方向的学习路线****👈**

对于从来没有接触过网络安全的同学，我们帮你准备了详细的学习成长路线图。可以说是最科学最系统的学习路线，大家跟着这个大的方向学习准没问题。

#### <img src="https://img-blog.csdnimg.cn/img_convert/de55dfd737dae0cf88e416d0454b17a8.png" alt="img">

#### 学习资料工具包

压箱底的好资料，全面地介绍网络安全的基础理论，包括逆向、八层网络防御、汇编语言、白帽子web安全、密码学、网络安全协议等，将基础理论和主流工具的应用实践紧密结合，有利于读者理解各种主流工具背后的实现机制。

<img src="https://img-blog.csdnimg.cn/9609a53465cf4253b492a5185896fa71.png" alt="在这里插入图片描述">

**面试题资料**

独家渠道收集京东、360、天融信等公司测试题！进大厂指日可待！ <img src="https://img-blog.csdnimg.cn/f5f267c281c543fb9cc9af53b9003a37.png" alt="在这里插入图片描述">

#### **👉<strong><strong>嘿客必备开发工具**</strong>👈</strong>

工欲善其事必先利其器。学习**嘿**客常用的开发软件都在这里了，给大家节省了很多时间。

#### 这份完整版的网络安全（**嘿**客）全套学习资料已经上传至CSDN官方，朋友们如果需要点击下方链接**也可扫描下方微信二v码获取网络工程师全套资料**【保证100%免费】

#### <img src="https://img-blog.csdnimg.cn/img_convert/16c400294b6fda8f01400f24f1f12b0c.png" alt="在这里插入图片描述">

#### 如果你对网络安全入门感兴趣，那么你点击这里**👉**
