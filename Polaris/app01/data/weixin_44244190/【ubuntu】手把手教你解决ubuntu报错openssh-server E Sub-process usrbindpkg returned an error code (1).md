
--- 
title:  【ubuntu】手把手教你解决ubuntu报错openssh-server E: Sub-process /usr/bin/dpkg returned an error code (1) 
tags: []
categories: [] 

---
>  
 <img src="https://img-blog.csdnimg.cn/6e2c8c7bccdc41cd911dc26a692693a2.jpeg" alt="请添加图片描述"> 
 <hr> 
 👉博__主👈：米码收割机 👉技__能👈：C++/Python语言 👉公众号👈：测试开发自动化【获取源码+商业合作】 👉荣__誉👈：阿里云博客专家博主、51CTO技术博主 👉专__注👈：专注主流机器人、人工智能等相关领域的开发、测试技术。 


>  
 <h2>系列文章目录</h2> 
 <hr> 
  
  
  <h4>目录</h4> 
  - - -  
  
  


## 1. ubuntu安装软件报错

（这报错真TM烦人）

>  
 Setting up openssh-server (1:8.2p1-4ubuntu0.9) … dpkg: error processing package openssh-server (–configure): installed openssh-server package post-installation script subprocess returned error exit status 10 Setting up ufw (0.36-6ubuntu1.1) … dpkg: error processing package ufw (–configure): installed ufw package post-installation script subprocess returned error exit status 10 Errors were encountered while processing: **openssh-server ufw** **E: Sub-process /usr/bin/dpkg returned an error code (1)** 


## 2. 解决办法

第一步：现将info文件夹更名

```
sudo mv /var/lib/dpkg/info  /var/lib/dpkg/info.bak

```

第二步：备份到其他地方（这步可省略）

```
sudo cp -rf /var/lib/dpkg/info.bak/* /home/bak/info_bak/

```

第三步：再新建一个新的 info文 件

```
sudo mkdir /var/lib/dpkg/info

```

第四步：更新源

```
sudo apt-get update

```

第五步：重新安装有问题的依赖包（不知道的话，可以都执行一遍）

```
sudo apt-get -f install openssh-server
sudo apt-get -f install ssh
sudo apt-get -f install exim4-base
sudo apt-get -f install exim4-daemon-light
sudo apt-get -f install exim4

```

第六步：调整安装依赖后，把新的东西移动到备份文件夹 info.bak 里

```
sudo mv /var/lib/dpkg/info/* /var/lib/dpkg/info.bak


```

第七步：把自己新建的 info 文件夹删掉

```
sudo rm -rf /var/lib/dpkg/info


```

第八步：把备份的 info 文件夹重新改回名字

```
sudo mv /var/lib/dpkg/info.bak /var/lib/dpkg/info


```
