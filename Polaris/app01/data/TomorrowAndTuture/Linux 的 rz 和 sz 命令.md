
--- 
title:  Linux 的 rz 和 sz 命令 
tags: []
categories: [] 

---
### 安装

我在 centos 上是可以直接用 yum 安装的，具体安装过程就不浪费版面来贴了。

```
yum install lrzsz
```

### 使用 

上面安装好以后，就可以直接使用 sz 和 rz 命令了。说实话，这两个命令的功能和 xftp 的功能很像，只不过 xftp 需要通过拖动的方式来实现文件的上传和下载（但是 xftp 支持文件夹的上传和下载）。

<img alt="" height="517" src="https://img-blog.csdnimg.cn/20210823144802255.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RvbW9ycm93QW5kVHV0dXJl,size_16,color_FFFFFF,t_70" width="1022">

#### sz

sz命令（Send ZMODEM），通过ZMODEM协议，可将多个文件从远程服务器下载到本地。注意不能下载文件夹，如果下载文件夹，请先打包再下载。

```
sz &lt;file1, file2, ...&gt;
```

<img alt="" height="506" src="https://img-blog.csdnimg.cn/20210823145029783.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RvbW9ycm93QW5kVHV0dXJl,size_16,color_FFFFFF,t_70" width="1130">

#### rz

```
rz
```

rz 命令（Receive ZMODEM），使用ZMODEM协议，将本地文件批量上传到远程Linux/Unix服务器，注意不能上传文件夹。

<img alt="" height="540" src="https://img-blog.csdnimg.cn/20210823145514377.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RvbW9ycm93QW5kVHV0dXJl,size_16,color_FFFFFF,t_70" width="1117">

### 优势

**其中的一个优势就在于 sz， rz 可以直接在宿主机下的虚拟机里边直接操作。**

比如说，你在一个物理机对应的虚拟机里边想下载一个文件到本地，你会做哪些操作呢？我自己弄的话就至少需要两步了。

第一步：先 scp 拷贝到宿主机上；

```
[root@master ~]# scp root@vm-machine:/root/insight-tool/output/conf_info_report-20210823142640.html .
conf_info_report-20210823142640.html                                100%  894KB  67.3MB/s   00:00  
```

第二步：使用 xftp 下载文件。
