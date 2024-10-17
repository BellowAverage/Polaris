
--- 
title:  linux 搭建Nginx网页（编译安装） 
tags: []
categories: [] 

---
>  
 ♥️**作者：小刘在C站** 
 ♥️**个人主页：<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong> 
 ♥️**不能因为人生的道路坎坷,就使自己的身躯变得弯曲;不能因为生活的历程漫长,就使求索的 脚步迟缓。** 
 ♥️**学习两年总结出的运维经验，以及思科模拟器全套网络实验教程。专栏：** 
 ♥️**感谢CSDN让你我相遇！** 


<img alt="" height="80" src="https://img-blog.csdnimg.cn/fd3fee85df1d4cffba97164ba01cdf81.gif" width="640">

**Nginx是什么？**

>  
 **Nginx** (engine x) 是一个高性能的和web服务器  ，同时也提供了IMAP/POP3/服务。Nginx是由伊戈尔·赛索耶夫为第二的Rambler.ru站点（：Рамблер）开发的，公开版本1.19.6发布于2020年12月15日。 其将以类的形式发布，因它的稳定性、丰富的功能集、简单的和低的消耗而闻名。2022年01月25日，nginx 1.21.6发布。 Nginx是一款轻量级的 服务器/服务器及（IMAP/）代理服务器，在-like 协议下发行。其特点是占有内存少，并发能力强，事实上nginx的并发能力在同类型的服务器中表现较好。 


**目录**



















### Nginx的好处

一款高性能、轻量级Web服务软件 稳定性高 系统资源消耗低 对HTTP并发连接的处理能力高 单台物理服务器可支持30000~50000个并发请求

### Nginx的服务说明：

主配置文件：/usr/local/nginx/conf/nginx.conf 检查语法：nginx  -t 启动服务：nginx 重新加载服务：killall  -s   HUP   nginx 停止服务： killall   -s    QUIT    nginx 网页文件：/usr/local/nginx/html/ 端口号： tcp     80

### linux搭建Nginx网页

#### 1.环境所需

Nginx的配置及运行需要pcre、zlib等软件包的支持，因此应预先安装这些软件的开发包(devel)以便提供相应的库和头文件，确保Ngix的安装顺利完成

yum源配置完成后可以进行安装pcre  zlib（yum源镜像通过各大厂商官网进行下载如：阿里，清华，等..）

<img alt="" height="36" src="https://img-blog.csdnimg.cn/7e6077119af0418d958aea353877da5e.png" width="647">

#### 2.创建程序用户

Nginx服务程序默认以nobody身份运行，建议为其创建专门的用户账号，以便更准确地控制其 访问权限，增加灵活性，降低安全风险。例如，创建一个名为nginx的用户，不建立宿主文件也 禁止登录到Shell环境。

<img alt="" height="47" src="https://img-blog.csdnimg.cn/34fe88e7ebb140959b90242b6da7f843.png" width="645">

其中-M选项作用为不为此用户创建家目录

其中-s选项作用为指定此用户的shell为/sbin/nologin

/sbin/nologin不为目录，是一个可执行文件可以作为shell但是不能登录到系统中

#### 3.编译安装Nginx

配置Nginx的编译选项时，将安装目录设为/usr/local/nginx,运行用户及组均设为nginx;启用 http_stub_status_.module模块以支持状态统计，便于查看服务器的连接信息。后再进行make编译与make install编译安装，./configure具体选项根据实际需要来定，配置前可参考”./configure   --help”给出的说明。

<img alt="" height="181" src="https://img-blog.csdnimg.cn/2bfb6e5e26994b9a8cfd7a46bbebbb2b.png" width="861">

之后我们使nginx安装的命令可以再控制台使用，需要将nginx的可执行命令链接到用户本地的磨炼中也就是/usr/local/sbin/下面即可，ls查看是否成功链接



<img alt="" height="158" src="https://img-blog.csdnimg.cn/207d97ec7f7a453d966ded4fe7f79b90.png" width="884">

到这里可以使用nginx  -t命令查看对配置文件进行语法检查以便找不到错误位置

Nginx的默认配置文件路径/usr/local/nginx/conf/nginx.conf

<img alt="" height="109" src="https://img-blog.csdnimg.cn/b916875745a64504943b681ce2c97f18.png" width="884">

最后使用nginx启动服务就可以了需要注意的是，若服务器中已装有 httpd等其他Web服务软件，应采取修改端口、停用或卸载等措施避免端口冲突

<img alt="" height="37" src="https://img-blog.csdnimg.cn/97352121b08c45779bba5940b8d73dca.png" width="577">

可以通过netstat 命令查看是否开启服务

<img alt="" height="59" src="https://img-blog.csdnimg.cn/20e9e2a4ea9c4c88ad32a0592bdc571d.png" width="849">

#### 4.网页制作

网页文件路径在/usr/local/nginx/html/

可以修改index.html进行网页的编写，到这里就结束了谢谢您的阅读

>  
 人生要尽全力度过每一关,不管遇到什么困难不可轻言放弃！！！ 

