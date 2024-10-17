
--- 
title:  Linux之日志检查工具logcheck 
tags: []
categories: [] 

---
## 一、logcheck简介

  Logcheck用来分析庞大的日志文件，过滤出有潜在安全风险或其他不正常情况的日志项目，然后以电子邮件的形式通知指定的用户。Logcheck是一个软件包，用于自动运行和检查系统日志文件，查看是否存在安全违规和异常活动。Logcheck使用一个名为logtail的程序，该程序会记住它在日志文件中读取的最后一个位置，并在后续运行中使用该位置来处理新信息。这个软件包有一些功能，但可能更容易使用，因为它不需要一个持续运行的程序，并且可以将许多系统的所有结果发送回单个位置。此外，它还报告您以前可能没有见过的任何异常系统消息，这是一个明显的优势，因为通常不可能知道可能从守护程序进入日志的每个可能的系统日志消息。

## 二、安装及使用实践

### 1、下载软件包

>  
 [root@s142 tmp]# wget --no-check-certificate https://cfhcable.dl.sourceforge.net/project/logcheck/logcheck-1.1.2/Logcheck%20under%20new%20mgmt./logcheck-1.1.2.tar.gz … 2022-09-22 10:38:43 (118 KB/s) - ‘logcheck-1.1.2.tar.gz’ saved [30683/30683] 


### 2、解压软件包

>  
 [root@s142 tmp]# tar -zxvf logcheck-1.1.2.tar.gz 


### 3、make安装

>  
 [root@s142 tmp]# cd logcheck-1.1.2 [root@s142 logcheck-1.1.2]# make linux <img src="https://img-blog.csdnimg.cn/0a0d5ba553b0480bb792705adbe3e529.png" alt="在这里插入图片描述"> 


### 4、配置定时任务

>  
 [root@s142 logcheck-1.1.2]# crontab -e no crontab for root - using an empty one  */5 * * * * /usr/local/etc/logcheck.sh 


### 5、安装mailx

>  
 [root@s142 logcheck-1.1.2]# yum install -y mailx … Installed: mailx.x86_64 0:12.5-19.el7  Complete! 


### 6、查看邮件

>  
 [root@s142 logcheck-1.1.2]# mail Heirloom Mail version 12.5 7/5/10. Type ? for help. “/var/spool/mail/root”: 1 message 1 new N 1 root Thu Sep 22 11:00 36/1629 “s142 09/22/22:11.00 system check” &amp; 1 <img src="https://img-blog.csdnimg.cn/764b3efafab34350a244e1c16634e93e.png" alt="在这里插入图片描述"> 


### 7、邮件发送到其他账户

  将默认的root账户修改为wuhs账户，保存后，则报告邮件发送给wuhs。

>  
 [root@s142 etc]# vim +43 logcheck.sh … SYSADMIN=wuhs … <img src="https://img-blog.csdnimg.cn/58b355db24e54709967e878199902ff6.png" alt="在这里插入图片描述"> 


### 8、增加忽略关键字

  检查日志判断，如果确定是系统正常日志的，我们可以更新logcheck.ignore文件，添加待忽略的日志关键字，排除这些正常日志。 <img src="https://img-blog.csdnimg.cn/c91ce36c0bb04e00858579fe7e552f66.png" alt="在这里插入图片描述">

>  
 [root@s142 etc]# echo “postfix” &gt;&gt; logcheck.ignore <img src="https://img-blog.csdnimg.cn/e8c174a10cd7418489933c8a9e8017e3.png" alt="在这里插入图片描述"> 


### 9、添加yum.log日志监控

  logcheck工具默认只检查/var/log/messages、/var/log/secure 、/var/log/maillog日志，我们可以自定义添加我们自己想监控的日志，还可以同步更新我们需要监控的关键字和忽略的关键字。

>  
 [root@s142 etc]# vim +172 logcheck.sh … #添加如下一行 $LOGTAIL /var/log/yum.log &gt;&gt; $TMPDIR/check.$$ … [root@s142 etc]# echo “Installed” &gt;&gt; logcheck.violations 


<img src="https://img-blog.csdnimg.cn/734ea79a2f714a11a0a2454bb8b995c3.png" alt="在这里插入图片描述">

## 三、主要文件说明

  make安装完成后，配置文件和运行脚本默认安装在/usr/local/etc/下。

### 1、logcheck.sh

  这是Logcheck的shell脚本，用于分析本次的日志文件并汇报结果。

### 2、logcheck.hacking

  这个文件设置在日志文件中过滤的关键字，该关键字提示了潜在安全风险的信息。用户可以定制自己的日志文件，在logcheck.hacking文件中增加或删除关键字。

### 3、logcheck.ignore

  如果系统日志文件记录了可能遭遇攻击的消息，但含有logcheck.ignore文件中的关键字，则Logcheck视为正常，在分析报告文件中不包含这些消息。

### 4、logcheck.violations

  这个文件设置在日志文件分析过滤系统运行时出现异常情况的关键字。

### 5、logcheck.violations.ignore

  如果系统出现异常情况，但含有此文件中的关键字，则视为正常，不写入Logcheck的分析报告文件中。
