
--- 
title:  Linux命令之logrotate命令 
tags: []
categories: [] 

---
## 一、命令简介

  logrotate旨在简化生成大量日志文件的系统的管理。它允许自动旋转、压缩、删除和邮寄日志文件。每个日志文件可以每天、每周、每月处理，也可以在其增长过大时处理。   通常，logrotate作为日常cron作业运行。除非日志的标准是：根据日志的大小，logrotate每天运行一次以上，或者除非使用-f或–force选项。   可以在命令行上给出任意数量的配置文件。稍后的配置文件可能会覆盖先前文件中给出的选项，因此logrotate配置文件的列出顺序很重要。通常，应使用包含所需任何其他配置文件的单个配置文件。如果在命令行上指定了一个目录，则该目录中的每个文件都将用作配置文件。   如果没有给出命令行参数，logrotate将打印版本和版权信息，以及简短的使用摘要。如果在旋转日志时发生任何错误，logrotate将以非零状态退出。

## 二、使用示例

  关于logrotate的完整使用示例及配置文件参数说明见。命令使用示例主要介绍命令的语法、任务执行报错、任务执行失效情况下的问题排查。

### 1、获取命令帮助

>  
 [root@s142 logrotate.d]# logrotate --help <img src="https://img-blog.csdnimg.cn/0d58df2ad73843f2b18eecfbf795ff6c.png" alt="在这里插入图片描述"> 


### 2、查看命令版本

>  
 [root@s142 logrotate.d]# logrotate --version logrotate 3.8.6 


### 3、-d 模拟测试执行

>  
 [root@s142 logrotate.d]# cat test /var/log/logtest/catalina.out {<!-- --> daily minsize 10M missingok rotate 26 compress copytruncate delaycompress notifempty create 640 root root dateext } [root@s142 logrotate.d]# logrotate -d test <img src="https://img-blog.csdnimg.cn/1cf3393d1acf4584ac8c3b56e7833c8c.png" alt="在这里插入图片描述"> 


### 4、-f 强制执行日志分割

>  
 [root@s142 logrotate.d]# logrotate -f test <img src="https://img-blog.csdnimg.cn/3ea6852ab05b4d3780ab27f141c45792.png" alt="在这里插入图片描述"> 


### 5、-s 执行状态指定输出

>  
 [root@s142 logrotate.d]# logrotate -s /tmp/log.txt bootlog [root@s142 logrotate.d]# cat /tmp/log.txt logrotate state – version 2 “/var/log/boot.log” 2022-9-14-14:0:0 “/var/log/logtest/catalina.out” 2022-9-14-14:0:0 [root@s142 logrotate.d]# logrotate -s /tmp/log.txt -f test [root@s142 logrotate.d]# cat /tmp/log.txt logrotate state – version 2 “/var/log/boot.log” 2022-9-14-14:0:0 “/var/log/logtest/catalina.out” 2022-9-14-14:47:47 


### 6、-v 输出日志分割执行的详细信息

>  
 [root@s142 logrotate.d]# logrotate -s /tmp/log.txt -vf test <img src="https://img-blog.csdnimg.cn/20f0686ea2864e879202c328c98734c0.png" alt="在这里插入图片描述"> 


### 7、-l 将执行日志存入指定文件

>  
 [root@s142 logrotate.d]# logrotate -l 1.log test [root@s142 logrotate.d]# cat 1.log reading config file test Allocating hash table for state file, size 15360 B  Handling 1 logs  rotating pattern: /var/log/logtest/catalina.out after 1 days (26 rotations) empty log files are not rotated, only log files &gt;= 10485760 bytes are rotated, old logs are removed considering log /var/log/logtest/catalina.out log does not need rotating (log has been already rotated)[root@s142 logrotate.d]# 


### 8、查看logrotate执行记录

>  
 [root@s142 logrotate.d]# logrotate -v /etc/logrotate.conf reading config file /etc/logrotate.conf including /etc/logrotate.d reading config file bootlog reading config file chrony reading config file syslog reading config file test reading config file wpa_supplicant reading config file yum Allocating hash table for state file, size 15360 B … <img src="https://img-blog.csdnimg.cn/0921e085e8b0435a9ec5f7a8723fb279.png" alt="在这里插入图片描述"> 


## 三、使用语法及从参数说明

### 1、使用语法

>  
 用法：logrotate [OPTION…]  


### 2、参数说明

<th align="left">参数</th><th align="left">参数说明</th>
|------
<td align="left">-d, --debug</td><td align="left">调试用，打印执行结果，不会真正执行；</td>
<td align="left">-f, --force</td><td align="left">强制执行，用于刚添加或修改任务或历史切割文件被删除后，强制执行切割（每天只执行一次）。</td>
<td align="left">-m, --mail=command</td><td align="left">指定logrotate发送邮件时使用的命令，该命令需接收两个参数：邮件主题；邮件接收人。该命令必须阅读标准输入上的消息并将其邮寄给收件人。默认命令：/bin/mail -s 。**测试使用失败，如果有知道的朋友欢迎留言告知，谢谢！**</td>
<td align="left">-s, --state=statefile</td><td align="left">指定记录logrotate执行结果的文件，在使用特定用户执行logrotate时较有用。</td>
<td align="left">-v, --verbose</td><td align="left">开启详细模式。</td>
<td align="left">-l, --log=STRING</td><td align="left">指定执行日志记录文件</td>
<td align="left">–version</td><td align="left">查看命令版本</td>
<td align="left">-?, --help</td><td align="left">获取命令帮助信息</td>
<td align="left">–usage</td><td align="left">开启详细模式。</td>

### 3、重要文件
- 默认执行状态存储文件：/var/lib/logrotate/logrotate.status- 配置文件：/etc/logrotate.conf