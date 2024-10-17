
--- 
title:  Linux 下 python3.9.8的安装 
tags: []
categories: [] 

---
#### 1. 准备安装环境

#### 2. linux 下 python 安装包的获取

官网下载地址:

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/ab843e6a5767f048c1db82faec930d23.png">

 找到 自己想要的版本。

方式一：直接点击该链接下载，然后将安装包通过xftp 传送到远程服务器 的

路径下

方式二：

 <li> 
  <ol>
   <li> 右键复制该链接： <img alt="" src="https://img-blog.csdnimg.cn/img_convert/6a01be9bf2e68d8cb10098e58279f040.png">  在 opt 路径下,使用wget命令下载： <pre>cd /opt
wget https://www.python.org/ftp/python/3.9.8/Python-3.9.8.tgz</pre> </li>
  </ol></li>
 <li> 
  <ol>
   -  如果系统没有wget ,先下载 wget ,再重复上一步。 <pre>yum -y install wget</pre> 
  </ol></li>

#### 3. 解压刚刚下载的安装包

并将解压后的文件夹更名 (非必要步骤)
