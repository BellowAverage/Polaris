
--- 
title:  配置linux服务器XShell命令大全 
tags: []
categories: [] 

---
## shell注册码：**101210-450789-147200**

CentOS 7

(cd 路径)

1.修改主机名:hostnamectl set-hostname 新名

2.VI文本编辑命令:vi 文本文件

    它有三种模式，即 **命令模式（command mode,ESC进入）、插入模式（Insert mode，i进入）和底行模式（last line mode，：进入）**

**    1) command mode:控制屏幕光标的移动，字符、字或行的删除，移动复制某区段及进入Insert mode下；     2) Insert mode：只有在Insert mode下，才可以做文字输入，按「ESC」键可回到命令行模式。      3) last line mode：（shift+: 进入底行模式）将文件保存（:wq）、以指定文件名保存(:q fileName)、退出不保存（:q!）。**

3.上传文件至服务器

   1）连接至一台Linux服务器；

   2）输入rz命令，看是否已经安装了Lrzsz,如果没有安装(显示 bash:rz:command not found)则执行  yum -y install lrzsz 命令，进            行 安装；

   3)执行 rpm,显示第一行   Rpm version ****，则表示安装成功；

   4）执行 rz ,则会弹出本地文件上传框，选择文件上传。

   5）从服务器下载文件到本地  sz

   6）压缩文件  zip/tar 压缩文件名  待压缩文件

4.文件操作(文件名: test)

  1)新建文件：mkdir test，若新建文件目录，如: mkdir test/test.txt

  2)重命名: mv test  Test

  3)删除文件:rm -rf Test 

5.创建文本文档   touch test.txt

6.查看文档内容  cat  test.txt

7.清除文本文档内容: &gt; test.txt

8.重启服务器  shutdown -r now

#### 9.报错:-bash: *****: command not found

####    万能解决方法:yum install *****      

                          输入 ： y

10.报错  -bash:$'302\240 *** ':command not found    //这是因为你的命令有多余的空格，删除多余空格，重新执行即可！

11.检查Tomcat是否已启动

     ps -ef |grep tomcat

 12.查询所有端口使用情况    netstat -anp





firewall-cmd --reload

firewall-cmd --zone=public --add-port=3306/tcp --permanent

firewall-cmd --zone=public --list-ports




