
--- 
title:  linux目录和其他系统的目录的目录结构 
tags: []
categories: [] 

---
### 程序必须
- boot：启动的时候的服务<li>etc：配置文件 
  <ul>- 用户名一般记录在/etc/passwd文件中， 密码一般记录在/etc/shadow文件中， 群组一般记录在/etc/group文件中
### 命令
<li> bin 程序的入口，配置一些可执行命令。 比如要执行：pathon、Java、hadoop的一些脚本就在这个位置，linux自带的在/bin,用户自己安装的在/usr/bin 系统自带的一些功能，比如cat、vim 
  <ul>- 记录一下如果系统配置文档，那么可以做一个ln -s指向对应的目录来实现功能
sbin
- 通常是系统服务的配置，比如reboot，ip，各种服务的启停- 超级用户的配置，权限比较高，用户自己的在usr/sbin
### 用户目录
<li> root：超级用户的目录 
  <ul>- 用户其他的目录在/home、用户名
home：用户目录，里面一般放用户自己的文档、程序、游戏等

usr：文件系统，系统安装(相当于windows的Progream files)
-  通常定义为可分享、不可变更的文件 -  usr/local： 用户自己后续安装的文件，usr里面是linux自带的 -  usr/src，内核源代码的位置 
tmp：临时文件

opt，安装包文件

srv：系统启动以后需要的各种服务，比如www、FTP等伺服器

### 硬盘
- dev（device）：设备(相当于windows下我的电脑\C:)- mnt，临时挂载的其他磁盘的位置- media，软碟、光碟、DVD等的配置位置，一般是可插拔的，和mnt一样
#### 其他（不可分享）
<li> var:系统运行时候产生的文件的目录，这个通常是可变但是不和分享的 
  <ul>-  里面的数据经常修改 -  var/log里面记录了日志 -  var/lock,不可分享 -  var/pid，进程放在里面？？？ -  var/pool,线程队列 
lost + found：当系统非法关机的时候才会有文件

proc：进程在磁盘的映射，本质是内存
