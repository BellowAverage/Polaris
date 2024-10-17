
--- 
title:  Nginx(无法解析PHP网页如何解决？FPM解决你的烦恼！) 
tags: []
categories: [] 

---
>  
  ♥️**作者：小刘在C站** 
  ♥️**个人主页：<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong> 
  ♥️**不能因为人生的道路坎坷,就使自己的身躯变得弯曲;不能因为生活的历程漫长,就使求索的 脚步迟缓。** 
  ♥️**学习两年总结出的运维经验，以及思科模拟器全套网络实验教程。专栏：** 
  ♥️**感谢CSDN让你我相遇！** 
 

**目录**

















#### Nginx是什么？

Nginx (engine x) 是一个高性能的HTTP和反向代理web服务器  ，同时也提供了IMAP/POP3/SMTP服务。Nginx是由伊戈尔·赛索耶夫为俄罗斯访问量第二的Rambler.ru站点（俄文：Рамблер）开发的，公开版本1.19.6发布于2020年12月15日。 其将源代码以类BSD许可证的形式发布，因它的稳定性、丰富的功能集、简单的配置文件和低系统资源的消耗而闻名  

#### PHP是什么？

PHP即Hypertext Preprocessor(超级文本预处理语言)的缩写，是一种服务器端的HTML嵌入式 脚本语言。PHP的语法混合了C、Java、Perl及部分自创的新语法，拥有更好的网页执行速度，更重要的是PHP支持绝大多数流行的数据库，在数据库层面的操作功能十分强大，而且能够支持UNXVindows、Linux等多种操作系统。



#### FPM是什么？

较新版本的PHP已经自带FPM(FastCGl Process Manager,FastCGl进程管理器)模块 用来对PHP解析实例进行管理、优化解析效率。单服务器的MP架构通常使用这种方式，因此在配 置PHP编译选项时应添加“--enable-fpm”以启用此模块。

#### FPM安装

###### 安装fpm模块

编译安装时添加模块--enable-fpm 

命令：./configure/   --prefix=/usr/local/php5  --enable-fpm

--prefix指定的路径为安装路径

##### 启用fpm进程

如果选用FPM方式，则需要先启动php-fpm进程，以便监听PHP解析请求。参考范例建立 php-fpm.conf配置文件，并修改其中的PID文件、运行用户、服务数（进程数量）等相关设置，然后启动php-fpm程序即可（默认监听本机的9000端口）。

<img alt="" height="304" src="https://img-blog.csdnimg.cn/direct/c80e338403b34fa89965c599b74a68d4.png" width="826">

<img alt="" height="161" src="https://img-blog.csdnimg.cn/direct/1ae0dbf87bd34749840709a07b3fad90.png" width="391">

上方配置作用为：

                                启动时开启的进程数

                                 最少空闲进程数

                                最多空闲进程数

                                最大的子进程数

完成后启用进程命令为：/usr/local/sbin/php_fpm（最后路径取决于安装时指定的路径）

                                    
