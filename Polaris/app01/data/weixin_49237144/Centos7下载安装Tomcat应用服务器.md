
--- 
title:  Centos7下载安装Tomcat应用服务器 
tags: []
categories: [] 

---
## Centos7安装Apache-Tomcat-9



#### 文章目录
- - <ul><li><ul><li>- - - - - - 


#### 1. 前言

```
    Apache-Tomcat服务器是一个免费的开放源代码的Web 应用服务器，属于轻量级应用服务器，
    在中小型系统和并发访问用户不是很多的场合下被普遍使用，是开发和调试JSP 程序的首选。
    对于一个初学者来说，可以这样认为，当在一台机器上配置好Apache 服务器，
    可利用它响应HTML（标准通用标记语言）页面的访问请求。实际上Tomcat是Apache 服务器的扩展，
    但运行时它是独立运行的，所以当你运行tomcat 时，它实际上作为一个与Apache 独立的进程单独运行的。

```

#### 2. 官网下载Apache-Tomcat

<th align="center">Apache-Tomcat官网</th><th align="center">https://tomcat.apache.org/</th>
|------
<td align="center"></td><td align="center"></td>

<img src="https://img-blog.csdnimg.cn/134bda1a148d4795a04bd11be6628b99.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/61d2276e30ad4c5498eeb841e169eaf6.png#pic_center" alt="在这里插入图片描述">

#### 3. 使用xftp工具或者rz工具传输文件

```
3.1 使用xftp工具将Tomcat迁移到 /opt目录下

```

<img src="https://img-blog.csdnimg.cn/b764c41733fc433ba034d92cf2eb4b79.png#pic_center" alt="在这里插入图片描述">

```
3.2 或者使用rz工具将Tomcat迁移到 /opt目录下
[root@localhost ~]# yum install lrzsz -y
[root@localhost ~]# rz

```

<img src="https://img-blog.csdnimg.cn/9a55298378b749c39843bca38fd43914.png#pic_center" alt="在这里插入图片描述">

#### 4. 解压Tomcat文件并启动Tomcat文件

```
4.1 进入 /opt目录下查看文件是否存在（上面已经将Tomcat文件传输到/opt）
[root@localhost ~]# cd /opt
[root@localhost opt]# ls
4.2 将Tomcat文件解压缩
z:Gzip压缩算法
x:解压缩
v:输出显示执行过程
f:文件名
C:解压缩到指定路径
./:当前路径
[root@localhost opt]# tar -zxvf apache-tomcat-9.0.65.tar.gz -C ./
4.3 查看是否解压缩完成
[root@localhost opt]# ls

```

<img src="https://img-blog.csdnimg.cn/c75b406b6381455baf220651d302d8fb.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/9717a6a183d54c25a40f728470df3e17.png#pic_center" alt="在这里插入图片描述">

#### 5. 关闭防火墙并访问Apache-Tomcat

```
5.1 进入Tomcat的bin目录，并授权
[root@localhost opt]# chmod 777 -R /opt/apache-tomcat-9.0.65/bin/
5.2 关闭防火墙（无法访问才关闭）
[root@localhost opt]# systemctl stop firewalld.service
启动Tomcat
[root@localhost opt]# cd /opt/apache-tomcat-9.0.65/bin/
[root@localhost bin]# sh startup.sh

```

<img src="https://img-blog.csdnimg.cn/0967d71b34464ad1be26a909aff15122.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/111f39d333be42b784983a08a1a61843.png#pic_center" alt="在这里插入图片描述">

```
5.2 打开浏览器访问192.168.1.222:8080  (默认端口号：8080)

```

<img src="https://img-blog.csdnimg.cn/ece292e25af34587b824330cca9c1c8a.png#pic_center" alt="在这里插入图片描述">

#### 6. 可以修改端口号

```
[root@localhost conf]# vim /opt/apache-tomcat-9.0.65/conf/server.xml

```

<img src="https://img-blog.csdnimg.cn/5d9d17f9ee3d4e94815908885d86b061.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/e52925c655624904b94882cb5602fa63.png#pic_center" alt="在这里插入图片描述">

#### 7. 开放端口

```
7.1 查看系统中的所有端口
[root@localhost conf]# firewall-cmd --list-ports
7.2 开放8080端口
[root@localhost conf]# irewall-cmd --zone=public --add-port=8080/tcp --permanent

```

md --list-ports 7.2 开放8080端口 [root@localhost conf]# irewall-cmd --zone=public --add-port=8080/tcp --permanent

```


```
