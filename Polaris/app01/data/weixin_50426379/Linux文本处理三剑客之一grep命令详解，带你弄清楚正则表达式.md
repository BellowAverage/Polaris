
--- 
title:  Linux|文本处理三剑客之一grep命令详解，带你弄清楚正则表达式 
tags: []
categories: [] 

---


#### 文章目录
- - <ul><li><ul><li>- <ul><li>- - - - - 


## grep:文本过滤命令

#### grep命令详解

<mark>匹配到的内容会整行输出到屏幕上</mark> --》文本过滤、文本查找

>  
 grep选项 <mark>-i 不区分大小写 -i, --ignore-case -o 只是显示匹配的内容 only-match -n 显示行号 line-number -v invert-match -A after 在什么之后 -B before 在什么以前 -C center（中心） context上下文 -r 递归查找</mark> 


```
[root@wh lianxi]# cat name.txt 
zhengyang ZHENGYANG
LIZHUOFU lizuofu123 12345lizhuofu
xiaomi huawei oppo
XIAOMI xiaomi12234+56 sc@163.com
wenke wenkeke
wanglianfang fangfang
liyili lili
zhengyang ZHENGYANG
LIZHUOFU lizuofu123 12345lizhuofu
xiaomi huawei oppo
XIAOMI xiaomi12234+56 sc@163.com
wenke wenkeke
wanglianfang fangfang
liyili lili

# -i 忽略大小写
[root@wh lianxi]# grep -i "xiaomi" name.txt
xiaomi huawei oppo
XIAOMI xiaomi12234+56 sc@163.com
xiaomi huawei oppo
XIAOMI xiaomi12234+56 sc@163.com
# -o 匹配符合条件的内容
[root@wh lianxi]# grep -o  "xiaomi" name.txt
xiaomi
xiaomi
xiaomi
xiaomi
# -n 显示匹配内容的对应行号
[root@wh lianxi]# grep -o -n  "xiaomi" name.txt
3:xiaomi
4:xiaomi
10:xiaomi
11:xiaomi
# -v 匹配不符合条件的行
[root@wh lianxi]# grep -v  "xiaomi" name.txt
zhengyang ZHENGYANG
LIZHUOFU lizuofu123 12345lizhuofu
wenke wenkeke
wanglianfang fangfang
liyili lili
zhengyang ZHENGYANG
LIZHUOFU lizuofu123 12345lizhuofu
wenke wenkeke
wanglianfang fangfang
liyili lili
# -A 匹配查找内容后多少行的内容
[root@wh lianxi]# grep -A 2  "wenke" name.txt
wenke wenkeke
wanglianfang fangfang
liyili lili
--
wenke wenkeke
wanglianfang fangfang
liyili lili
# -B 匹配查找内容前多少行的内容
[root@wh lianxi]# grep -B 2  "wenke" name.txt
xiaomi huawei oppo
XIAOMI xiaomi12234+56 sc@163.com
wenke wenkeke
--
xiaomi huawei oppo
XIAOMI xiaomi12234+56 sc@163.com
wenke wenkeke
# -C 匹配查找内容上下几行的内容
[root@wh lianxi]# grep -C 2  "wenke" name.txt
xiaomi huawei oppo
XIAOMI xiaomi12234+56 sc@163.com
wenke wenkeke
wanglianfang fangfang
liyili lili
--
xiaomi huawei oppo
XIAOMI xiaomi12234+56 sc@163.com
wenke wenkeke
wanglianfang fangfang
liyili lili
# -r 递归查找
[root@localhost lianxi]# cp name.txt xieshan
[root@localhost lianxi]# cp name.txt  daifurong/
[root@localhost lianxi]# grep -r  "xiaomi"  /lianxi
/lianxi/daifurong/name.txt:xiaomi  huawei  oppo
/lianxi/daifurong/name.txt:XIAOMI xiaomi12234+56  sc@163.com
/lianxi/daifurong/name.txt:xiaomi  huawei  oppo
/lianxi/daifurong/name.txt:XIAOMI xiaomi12234+56  sc@163.com
/lianxi/xieshan/name.txt:xiaomi  huawei  oppo
/lianxi/xieshan/name.txt:XIAOMI xiaomi12234+56  sc@163.com
/lianxi/xieshan/name.txt:xiaomi  huawei  oppo
/lianxi/xieshan/name.txt:XIAOMI xiaomi12234+56  sc@163.com
/lianxi/name.txt:xiaomi  huawei  oppo
/lianxi/name.txt:XIAOMI xiaomi12234+56  sc@163.com
/lianxi/name.txt:xiaomi  huawei  oppo
/lianxi/name.txt:XIAOMI xiaomi12234+56  sc@163.com

```

##### 基本正则和扩展正则：

>  
 grep命令支持扩展正则 1.基本正则 2.扩展正则 -E, --extended-regexp Interpret PATTERN as an extended regular expression (ERE, see below). 


区别：根据推出时间的不同，分为基本正则和扩展正则，扩展正则在基本正则的基础上做了一些优化新增了一些正则表达符号，因为一些命令没有及时更新，所以你可能会遇到有些命令只支持基本正则，不支持扩展正则，或者需要添加一些支持扩展正则的选项。

<img src="https://img-blog.csdnimg.cn/img_convert/290b2af6caad6d267dbe171d8b103c42.png#pic_center" alt="在这里插入图片描述">

```
# 匹配以xiaomi开头或者以lili结尾的行
[root@wh lianxi]# cat name.txt |egrep "^xiaomi|lili$"
xiaomi huawei oppo
liyili lili
xiaomi huawei oppo
liyili lili
# 匹配空行
[root@wh lianxi]# cat name.txt |egrep "^$"




#匹配空行以及他的行号
[root@wh lianxi]# cat name.txt |egrep "^$" -n
15:
16:
19:
21:

# 显示有效行
[root@wh lianxi]# cat /etc/ssh/sshd_config |egrep -v "^#|^$"

```

<img src="https://img-blog.csdnimg.cn/img_convert/176da99f258eefd4cbfdfde94ba386e3.png" alt="image.png">

```
# 词边界
\&lt;:词首部 等同于  \b
\&lt;abc\&gt; 表示abc这个单词
查找文本里单词的长度是12~16个字符的字符串
[root@wh 0701]# echo "ha haha hehe hahaha hahahaha"|egrep "\&lt;(ha){2,3}" -o 
haha
hahaha
hahaha
# ()分组

```

<img src="https://img-blog.csdnimg.cn/img_convert/007428aaa07579140561968bf4c43ebd.png" alt="image.png">

```
# 转义元字符

```

<img src="https://img-blog.csdnimg.cn/img_convert/6f9ce83187e577df2283c1ed2832c164.png#pic_center" alt="在这里插入图片描述">

##### 1. 匹配邮箱

```
[root@wh 0701]# cat mail.txt|egrep "[0-Z_]+@[0-Z]+\.[a-z]+" -o
feng@qq.com
1234feng@163.com
xianhui@yahoo.cn
liudehua@sina.com
10001@qq.com
123_ui@12306.cn
qilu@qilu.edu
qilu@qilu.edu

```

##### 2. 匹配url

>  
 写一个表示下面网址的正则表达式出来。例如： http://www.baidu.com fjdkfjdkfj http://www.sina.com fengdeyong http://www.163.com http://www.12306.cn 1212121 http://www.qillu.edu sanchuang rsync://www.github.com/abc ftp://192.168.0.1 ftp://www.baidu.com 12112 


```
[root@wh 0701]# egrep "[a-z]+://([0-z]+\.){2}[0-Z]+(\.[0-9]+)?(/[a-z]+)?" ip.txt -o
http://www.baidu.com
http://www.sina.com
http://www.163.com
http://www.12306.cn
http://www.qillu.edu
rsync://www.github.com/abc
ftp://192.168.0.1
ftp://www.baidu.com

```

##### 3. 时间的正则

>  
 时间的正则，表示18/Dec/2021:16:54分钟到18/Dec/2021:16:58分钟 
 7.1-7.7 7.1早上九点-晚上九点 
 7.1 早上九点-晚上九点 


```
# 18/Dec/2021:16:54分钟到18/Dec/2021:16:58分钟
[root@wh 0701]# egrep "18/Dec/2021:16:5[4-8]" time.txt -o
18/Dec/2021:16:54
18/Dec/2021:16:55
18/Dec/2021:16:56
18/Dec/2021:16:57
18/Dec/2021:16:58
# 7.1-7.7
[root@wh 0701]# egrep "[1-7]/jul/[0-9]{4}:[0-9]{2}:[0-9]{2}" time.txt -o
1/jul/2021:16:57
2/jul/2021:16:58
6/jul/2021:16:08
7/jul/2021:16:00
# 2021.7.1 早上九点-晚上九点 
[root@wh 0701]# egrep "1/jul/2021:9:00|1/jul/2021:21:00|1/jul/2021:1[0-9]:[0-9]{2}|1/jul/2021:20:[0-9]{2}" time.txt 
1/jul/2021:17:56
1/jul/2021:16:57
1/jul/2021:9:00

```

##### 4. 匹配ip地址正则

—》对日志作分析

>  
 ip地址：标识每台机器的一个id，通信地址，方便其他机器找到你的 
 ipv4：二进制 32位 
 ipv6：二进制 128位 
 公网ip分类： 
 A类地址范围：1.0.0.1～126.225.255.254。 
 B类地址范围：128.0.0.1～191.255.255.254。 
 C类地址范围：192.0.0.1～223.255.255.254。 
 D类地址范围：224.0.0.0～239.255.255.255。 
 E类地址范围：240.0.0.0～247.255.255.255。 
 127.0.0.0到127.255.255.255是保留地址，用做循环测试用的 。比如在本地做web开发时会用到。 
 私网ip分类： 
 A类的10.0.0.0～10.255.255.255 
 B类的172.16.0.0～172.31.255.255 
 C类的192.168.0.0～192.168.255.255为私网IP 
 除此之外，A、B、C三类的所有其余IP都是公网IP。私网IP只会出现在私网内，公网IP只会出现在公网内。 


```
# 普通ip地址 0~255
[root@wh ~]# netstat -anplut|egrep "\b(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\b" -o
0.0.0.0
0.0.0.0
192.168.72.129
192.168.72.1
192.168.72.129
192.168.72.1
127.0.0.1
0.0.0.0
[root@wh ~]# netstat -anplut|egrep "\b(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\b" -o|sort|uniq 
# 匹配ip地址再进行排序去重

# A类地址 0~126
[root@weihong logs]# head -10  access.log |awk '{print $1}'|egrep "\b([1-9]|[1-9][0-9]|1[01][0-9]|12[0-6])(\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}\b" 
119.39.127.108
119.39.127.108
119.39.127.108
119.39.127.108
110.52.210.78
110.52.210.78
116.162.0.29
110.52.210.78

# B类地址 128~191
[root@weihong logs]# head -10  access.log |awk '{print $1}'|egrep "\b(12[89]|1[3-8][0-9]|1[9][01])(\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3}\b"
185.180.143.72
185.180.143.72

```

##### 5. 密码复杂度

```
# 1.获得字符串长度
[root@wh ~]# sg="luoyawei"
[root@wh ~]# echo ${#sg}
8
[root@wh ~]# echo $sg|wc -L
8
# 2.有无大写字母、小写字母、特殊字符
[root@wh ~]# echo $sg|egrep [A-Z]
[root@wh ~]# echo $sg|egrep [a-z]
luoyawei
[root@wh ~]# echo $?
0
[root@wh ~]# echo $sg|egrep [0-9]
[root@wh ~]# echo $?
1
[root@wh ~]# echo $sg|egrep [^0-Z]
[root@wh ~]# echo $?
1
# 一条语句判断有无大写字母、小写字母、特殊字符
[root@wh ~]# echo $sg|egrep "[a-z]"|egrep "[A-Z]"|egrep "^[0-Z]"|egrep "[0-9]"
[root@wh ~]# sg="sfDFAE1233#"
[root@wh ~]# echo $sg|egrep "[a-z]"|egrep "[A-Z]"|egrep "^[0-Z]"|egrep "[0-9]"
sfDFAE1233#
# 最后能匹配到说明密码复杂度符合要求

#密码复杂度脚本
[root@wh 0704]# cat passwd.sh 
#!/bin/bash

if (( ${#1} &gt;= 10 ));then
    echo "密码长度符合要求"
else
    echo "密码长度少于10位，请重新输入符合要求的密码"
    exit #退出脚本，不再继续执行下面的命令
fi

# 判断密码里是否有数字、大小写、特殊符号
if echo $1|egrep "[a-z]"|egrep "[A-Z]"|egrep "[0-9]"|egrep "[^0-Z]";then
    echo "密码满足复杂性要求"
else
    echo "密码没有满足复杂性要求，请重新输入密码"
fi

[root@wh 0704]# bash passwd.sh yaolifan123
密码长度符合要求
密码没有满足复杂性要求，请重新输入密码
[root@wh 0704]# bash passwd.sh yaolifanA123
密码长度符合要求
密码没有满足复杂性要求，请重新输入密码
[root@wh 0704]# bash passwd.sh yaolifanA123#
密码长度符合要求
yaolifanA123#
密码满足复杂性要求

```
