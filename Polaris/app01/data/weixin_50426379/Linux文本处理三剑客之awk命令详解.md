
--- 
title:  Linux|文本处理三剑客之awk命令详解 
tags: []
categories: [] 

---


#### 文章目录
- <ul><li>- <ul><li>- - - - - - - - 


### awk：文本截取命令

>  
 awk是一门编程语言 
 Gawk is the GNU Project’s implementation of the AWK programming language 


#### 完整语法

<mark>awk ‘BEGIN{commands}pattern{commands}END{commands}’ filename</mark>

>  
 BEGIN{commands} 处理数据前执行的命令 pattern{commands} 每行都执行的命令，支持正则 END{commands} 处理数据后执行的命令 


#### -F 指定分隔符

>  
 <mark>awk -F 分隔符 ‘/模式/{动作}’ 文件</mark> 
 模式可以是<mark>正则表达式、条件表达式或两种组合</mark> 
 如果模式是<mark>正则表达式要用/定界符</mark> 
 多个动作之间用==;==号分开 


#### awk命令的操作符

>  
 正则表达式和bash一致 
 数学运算: +，-，*，/，%，++， – 
 逻辑关系符: &amp;&amp;,||，! 
 &amp;&amp;比|的优先级要高 
 比较操作符: &gt;，&lt;，&gt;=，!=，&lt;=, == ，<sub>，!</sub> 
 文本 数据 表达式: == (精确匹配) ~：模糊匹配 


**完整语法举例**

```
[root@weihong logs]# awk -F: 'BEGIN{print "####start####"} $3&gt;500 &amp;&amp; $3&lt;1000{print $1,$3} END{print "####end#####"}' /etc/passwd
####start####
polkitd 999
libstoragemgmt 998
chrony 997
syslog 996
####end#####

[root@wh ~]# awk -F: 'BEGIN{num=0;print"开始统计/etc/passwd文件"} $1~/feng/ || $3&gt;1005{print NR,NF,$1,length($1),$(NF-1),$NF,$3;num++} END{print "结束统计",num}' /etc/passwd
开始统计/etc/passwd文件
29 7 liuqingtian 11 /home/liuqingtian /bin/bash 1007
30 7 liwenqian 9 /home/liwenqian /bin/bash 1008
...
125 7 yueyang 7 /home/yueyang /bin/bash 12426
126 7 liu 3 /home/liu /bin/bash 12427
结束统计 96

#命令解析：
num=0 ：自定义变量
$1~/feng/ || $3&gt;1005 ： ~为模糊匹配，第一个字段中包含feng或者第三个字段大于1005
NR number of record 行号
NF number of field 字段数
length() 内置的函数，用来统计字符串的长度
$NF  --&gt;最后一个字段 
$(NF-1) --&gt; 倒数第2个字段


# 获取df -Th命令中第一个字段和倒数第二个字段
[root@wh ~]# df -Th|awk '{print $1,$(NF-1)}'
文件系统 已用%
devtmpfs 0%
tmpfs 0%
tmpfs 2%
tmpfs 0%
/dev/mapper/centos-root 66%
/dev/sda1 20%
tmpfs 0%

```

**-F 指定分隔符**

```
# 指定分隔符为':'
[root@wh 0704]# awk -F: '{print $1,$2}'  /etc/passwd
[root@wh 0704]# head -1 /etc/passwd|awk -F":" '{print $1,$2}' 
root x
[root@wh 0704]# head -1 /etc/passwd|awk -F: '{print $1,$2}' 
root x
[root@wh 0704]# head -1 /etc/passwd|awk -F: '{print $1$2}' 
rootx
[root@wh 0704]# head -10 /etc/passwd|awk -F: 'OFS="#"{print $1,$2}' 
root#x

awk -F: '{print $1,$2}'  /etc/passwd
-F 指定输入分隔符，默认的分隔符是空白（空格+tab，Enter）
print是awk内部的命令，用于输出
$1,$2中的',' 引用输出分隔符，默认输出分隔符是一个空格
分隔符：
	1.输入分隔符
		-F
	2.输出分隔符
		定义OFS="#"
		output field separater

# 指定分隔符为:或者/
[root@localhost 74]# awk -F[:/]  '{print $1,$10}'  /etc/passwd

```

**pattern位置为正则表达式**

```
# 包含feng的行，输出第1,3,个字段
[root@wh ~]# awk -F: '/feng/{print $1,$3}' /etc/passwd
califeng 1017
fengdeyong 1029
zhangsanfeng 7799
qiaofeng 12369
#正则 第三个字段是三位的字符串
[root@wh ~]# awk -F: '$3~/\&lt;...\&gt;/{print $1,$3}' /etc/passwd
systemd-network 192
polkitd 999
chrony 998
nginx 997
mysql 996
wuyazi 995
# 10以内能整除5或者以1开头
[root@wh ~]# seq 10|awk '$1%5==0||$1~/^1/{print $1}'
1
5
10

```

#### awk的数据字段变量

>  
 $0表示整行文本 
 $1表示文本中第一个数据字段 
 $2表示文本中第二个数据字段 
 $n表示文本中第n个数据字段 
 awk的用-F来指定分隔符 
 默认的字段分隔符是任意空白字符(空格或者TAB) 


```
[root@wh 426]# df -h
文件系统                 容量  已用  可用 已用% 挂载点
devtmpfs                 898M     0  898M    0% /dev
tmpfs                    910M     0  910M    0% /dev/shm
tmpfs                    910M  9.6M  901M    2% /run
tmpfs                    910M     0  910M    0% /sys/fs/cgroup
/dev/mapper/centos-root   17G   10G  7.1G   59% /
/dev/sda1               1014M  151M  864M   15% /boot
tmpfs                    182M     0  182M    0% /run/user/0

[root@wh 426]# df -h|grep "/boot$"|awk '{print $1 $5}'
/dev/sda115%
#， 指定输出分隔符，默认为空格
[root@wh 426]# df -h|grep "/boot$"|awk '{print $1,$5}'
/dev/sda1 15%
# tr --&gt; transfer   -d --&gt; delete  删除%
[root@wh 426]# df -h|grep "/boot$"|awk '{print $5}'|tr -d %
15

# 输出df -Th命令中使用率超过50%的行
[root@wh ~]# df -Th|awk '$6&gt;"50%"{print $0}'
文件系统                类型      容量  已用  可用 已用% 挂载点
/dev/mapper/centos-root xfs        17G   12G  5.9G   66% /

```

**awk基本命令示例**

```
[root@wh ~]# head -1 /etc/passwd
root:x:0:0:root:/root:/bin/bash
# 输出uid &gt;= 500的用户名
[root@wh ~]# awk -F: '$3&gt;=500{print $1}' /etc/passwd 
polkitd
chrony
# 输出500&lt;=uid&lt;=6000的用户名
[root@wh ~]# awk -F: '$3&gt;=500 &amp;&amp; $3&lt;=6000{print $1}' /etc/passwd
polkitd
chrony
# 输出uid不等于gid的用户名
[root@wh ~]# awk -F: '$3 != $4{print $1}' /etc/passwd
adm
lp
# 输出以h开头的用户名
[root@wh ~]# awk -F: '/^h/{print $1}' /etc/passwd
halt
hsenjiemi
# ps aux里查找cpu和mem使用率超过0.1%的pid号和进程名
[root@wh ~]# ps aux|awk ' $3&gt;0.1 &amp;&amp; $4&gt;0.1 {print $2,$11}'
999 /usr/local/mysql/bin/mysqld
# 统计有多少个用户uid&gt;1000并且使用的shell是bash
[root@wh 0705]# awk -F: 'BEGIN{num=0} $3&gt;1000 &amp;&amp; /bash$/{print $0;num++}END{print num}' /etc/passwd
...
pingguo:x:12424:12421::/home/pingguo:/bin/bash
jingshi:x:12425:12422::/home/jingshi:/bin/bash
yueyang:x:12426:12423::/home/yueyang:/bin/bash
liu:x:12427:12427::/home/liu:/bin/bash
97

# 显示passwd文件中5~10行的用户名
[root@wh 0705]# awk -F: 'NR&gt;=5 &amp;&amp; NR&lt;=10{print $1}' /etc/passwd
lp
sync
shutdown
halt
mail
operator
# 显示passwd文件中5~10行的用户名和行号
[root@wh 0705]# awk -F: 'NR&gt;=5 &amp;&amp; NR&lt;=10{print NR,$1}' /etc/passwd
5 lp
6 sync
7 shutdown
8 halt
9 mail
10 operator
# 显示第5行及行号
[root@wh 0705]# awk  'NR==5 {print NR,$0}' /etc/passwd
5 lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin

```

**以下两条命令的区别**

```
[root@localhost 74]# cat /etc/passwd|awk -F: '/feng/{print $1,$3}'
fengdeyong 1011
[root@localhost 74]# awk -F: '/feng/{print $1,$3}'  /etc/passwd
fengdeyong 1011
# 第一条命令会启动2个进程，| 会启动一个子进程，系统会消耗更多的cpu，内存，磁盘IO,时间
# 推荐使用第二条

```

**统计日志文件中2022-7月份每分钟的流量**

```
[root@wh 0704]# cat log.txt 
2022-7-1 00:01:01 78
2022-7-1 00:01:03 78
2022-7-1 00:01:04 89
2022-7-1 00:03:01 178
2022-7-1 00:03:05 890
2022-7-2 00:04:01 178
2022-7-2 00:04:09 78
2022-7-3 00:05:10 78
2022-7-3 00:05:25 890
2022-7-4 12:04:10 78
2022-7-4 12:04:21 78
[root@wh 0704]# cat min_io.sh 
#!/bin/bash
for i in {<!-- -->1..31}
do
    for j in {<!-- -->00..24}
    do
        for n in {<!-- -->00..59}
        do
            if egrep "2022-7-$i $j:$n" log.txt &gt;/dev/null;then   
                egrep "2022-7-$i $j:$n:[0-5][0-9]" log.txt|awk 'BEGIN{sum=0}{print $0;sum=sum+$NF}END{print "这一分钟内流量总和为：",sum}'
            fi
        done    
    done
done

[root@wh 0704]# bash min_io.sh 
2022-7-1 00:01:01 78
2022-7-1 00:01:03 78
2022-7-1 00:01:04 89
这一分钟内流量总和为： 245
2022-7-1 00:03:01 178
2022-7-1 00:03:05 890
这一分钟内流量总和为： 1068
2022-7-2 00:04:01 178
2022-7-2 00:04:09 78
这一分钟内流量总和为： 256
2022-7-3 00:05:10 78
2022-7-3 00:05:25 890
这一分钟内流量总和为： 968
2022-7-4 12:04:10 78
2022-7-4 12:04:21 78
这一分钟内流量总和为： 156

# 方法二，用数组进行统计
[root@wh 0704]# awk '{time[$1,substr($1,5,1),substr($2,1,5)]+=$3}END{for (i in time)print i,time[i]}' log.txt |sort -n -k 3 -t -
2022-7-1-00:01 245
2022-7-1-00:03 1068
2022-7-2-00:04 256
2022-7-3-00:05 968
2022-7-4-12:04 156

```

**awk命令会不会一次性消耗文件大小的内存呢**

```
[root@wh 0705]# free -h
              total        used        free      shared  buff/cache   available
Mem:           1.8G        338M        1.0G        9.5M        417M        1.3G
Swap:          2.0G          0B        2.0G

[root@wh 0705]# du -sh sc_bigfile.txt 
2.0G	sc_bigfile.txt

[root@wh 0704]# awk '{print $2,$3}' sc_bigfile.txt 
# 不会，可以对比内存大的文件进行操作，运行脚本的同时可以敲top查看cpu、内存的使用率

[root@localhost 75]# awk -F"[ :]+" '{print $2,$4}' sc_bigfile.txt
# 连续的空格和：当作一个分割符号

```

#### awk使用shell变量

```
# 第一种方法 
# echo（也可以是其他的命令，ls） 通过管道符号将shell变量传递给awk
[root@wh 0705]# name=mengmeng
[root@wh 0705]# echo |awk -v username=$name '{print username}' 
mengmeng

# 方法二
# 直接使用shell里面的变量，使用双引号，有些地方需要考虑转义
[root@wh 0705]# mn=mengmeng
# $0没有转义
[root@wh 0705]# awk -F: "\$1~/$mn/{print $0}" /etc/passwd
0
0
0
[root@wh 0705]# awk -F: "\$1~/$mn/{print \$0}" /etc/passwd
mengmeng:x:12429:12429::/home/mengmeng:/bin/bash
mengmeng1:x:12430:12430::/home/mengmeng1:/bin/bash
mengmeng2:x:12431:12431::/home/mengmeng2:/bin/bash

```

#### awk的字段求和（累加）

```
[root@wh 0705]# cat grade.txt 
id   name    chinese    english    math
1    cali    80		80	   80
2    tom     90         90         70
3    jarry   70         100        90

12    cali    80	80	   80
11    tom     90        90         70
13    jarry   70        100        90
# 两者效果一样，变量默认定义为0
# 统计语文成绩的和
[root@wh 0705]# awk 'NR&gt;1{sum+=$3}END{print sum}' grade.txt 
480
[root@wh 0705]# awk 'BEGIN{sum=0}NR&gt;1{sum+=$3}END{print sum}' grade.txt 
480

```

#### awk内置函数length、substr，split

```
# 统计shadow文件中没有设置密码的用户名和用户个数
[root@wh 0705]# awk -F: 'length($2)&lt;=2 {print $1;sum++}END{print sum}' /etc/shadow
...
mengmeng
mengmeng1
mengmeng2
97
# 统计shadow文件中密码为*或者为!!的用户名的前两个字母和用户个数
[root@wh 0705]# awk -F: 'length($2)&lt;=2{print substr($1,1,2);sum++}END{print sum}' /etc/shadow
...
me
me
me
97
#取出ip  split
[root@wh 0706]# ip add|awk '/inet.*ens[0-9]+$/{split($2,a,"/")}END{for (i in a)print i,a[i]}'
1 192.168.72.129
2 24
[root@wh 0706]# ip add|awk '/inet.*ens[0-9]+$/{split($2,a,"/");print a[1]}'
192.168.72.129
# 分割第二个字段192.168.72.129/24，以“/”为分隔符，存到数组a中

# toupper函数
[root@wh 0706]# awk -F: '{print toupper($1)}' /etc/passwd
ROOT
BIN
DAEMON

```

#### awk的流控（if else）

```
# 输出passwd文件中用户名是三个字符的行
[root@wh 0705]# awk -F: 'length($1)==3 {print $0}' /etc/passwd
bin:x:1:1:bin:/bin:/sbin/nologin
...
liu:x:12427:12427::/home/liu:/bin/bash
[root@wh 0705]# awk -F: '{if (length($1)==3)print $0}' /etc/passwd
bin:x:1:1:bin:/bin:/sbin/nologin
...
liu:x:12427:12427::/home/liu:/bin/bash

# 如果用户名是三个字符，输出整行，否则输出用户名
[root@wh 0705]# awk -F: '{if (length($1)==3)print $0 ;else print $1}' /etc/passwd

# uid为0：超级用户，uid为1~999：系统用户，uid大于1000：普通用户
[root@wh 0705]# awk -F: '{if ($3==0)print $1"是超级用户" ;else if ($3 &gt;=1 &amp;&amp; $3 &lt;=999) print $1"是系统用户";else print $1"是普通用户"}' /etc/passwd

# uid为0：超级用户，uid为1~999：系统用户，uid大于1000：普通用户，并统计三类用户的数量
[root@wh 0705]# awk -F: '{if ($3==0) {print $1,"为超级用户";num1++;}else if($3&gt;0 &amp;&amp; $3&lt;1000) {print $1,"为系统用户";num2++;}else {print $1,"为普通用户";num3++}}END{print " 超级用户的数量是:"num1,"系统用户的数量:"num2,"普通用户的数量:"num3}' /etc/passwd

if语句后面执行多个命令的时候，使用{<!-- -->}括起来，使用;隔开，最后的命令接;结尾，外面的else if和else前面不需要接;了

```

#### awk的for循环

>  
 格式 
 for (i=0;i&lt;10;i++) {print $i;} 
 for (i in array) {print array[i]} 数组：用于统计效果很好 


```
# 数组用法
[root@wh 0705]# awk -F: '{user[$1]=$3}END{for (i in user) print user[i]}' /etc/passwd

#统计相同省份的投票数
[root@wh 0705]# cat vote.txt 
山东 aa  2
河南 bb  3
江西 cc 3
湖南 aa 40
山东 bb 10
江西 dd 6
河南 cc 3
湖南 cc 3
[root@wh 0705]# awk '{vote[$1]+=$3}END{for (i in vote) print i,vote[i]}' vote.txt |sort -n -k 2
河南 6
江西 9
山东 12
湖南 43

```

上期文章grep命令详解: 
