
--- 
title:  常用的 55 个 Linux Shell 脚本（包括基础案例、文件操作、实用工具、图形化、sed、gawk） 
tags: []
categories: [] 

---
### 一. shell基础案例

#### 1、第一个案例：helloworld

```
#!/bin/bash

function example {<!-- -->
	echo "Hello world!"
}
example

```

#### 2、打印运行的python进程

```
#!/bin/sh
pidlist=`ps -aux | grep python | awk '{print $2}'`
echo $pidlist

```

#### 3、获取并打印参数

```
#!/bin/bash
echo "$0 $1 $2 $3"  // 传入三个参数
echo $#    //获取传入参数的数量
echo $@    //打印获取传入参数
echo $*    //打印获取传入参数

```

#### 4、用脚本写for循环

```
#!/bin/bash

s=0;
for((i=1;i&lt;100;i++))
do 
 s=$[$s+$i]
done 

echo $s

r=0;
a=0;
b=0;
for((x=1;x&lt;9;x++))
do 
 a=$[$a+$x] 
echo $x
done
for((y=1;y&lt;9;y++))
do 
 b=$[$b+$y]
echo $y

done

echo $r=$[$a+$b]

```

#### 5、使用C语言风格的for命令

```
#!/bin/bash
#testing the C-style for loop

for (( i=1; i&lt;=10; i++ ))
do
	echo "The next number is $i"
done

```

#### 6、while循环案例

```
#!/bin/bash

s=0
i=1
while [ $i -le 100 ]
do
        s=$[$s + $i]
        i=$[$i + 1]
done

echo $s
echo $i

```

#### 7、使用break跳出外部循环

```
#!/bin/bash
# break n，默认为1

for (( a=1; a&lt;=3; a++ ))
do
	echo "Outer loop : $a"
	for (( b=1; b &lt; 100; b++ ))
	do 
		if [ $b -gt 4 ]
		then
			break 2
		fi
		echo " Inner loop:$b"
	done
done

```

#### 8、使用continue命令

```
#!/bin/bash

#using the continue command

for (( var1 = 1; var1 &lt; 15; var1++ ))
do
	if [ $var1 -gt 5 ] &amp;&amp; [ $var1 -lt 10 ]
	then
		continue
	fi
	echo "Iteration number:$var1"
done

```

#### 9、case案例

```
#!/bin/bash 

case $1 in 
1) 
 echo "wenmin "
;;
2)
 echo "wenxing "
;; 
3)  
 echo "wemchang "
;;
4) 
 echo "yijun"
;;
5)
 echo "sinian"
;;
6)  
 echo "sikeng"
;;
7) 
 echo "yanna"
;;
*)
 echo "danlian"
;; 
esac

```

#### 10、判断两个数是否相等

```
num1=100
num2=100
if test $[num1] -eq $[num2]
then
    echo '两个数相等！'
else
    echo '两个数不相等！'
fi

```

#### 11、使用双圆括号

```
#!/bin/bash
# using double parenthesis

var1=10

if (( $var1 ** 2 &gt; 90))
then 
	(( var2 = $var1 ** 2))
	echo "The square of $var1 if $var2"
fi


```

#### 12、使用双方括号

```
#!/bin/bash
# using pattern matching

if [[ $USER == r* ]]
then 
	echo "Hello $USER"
else
	echo "Sorry, I do not know you"
fi

```

#### 13、反引号的使用

```
#!/bin/bash
#using the backtick character  会把反引号里面当作一条命令来执行

testing=`date`
echo "The date and time are:$testing"

```

#### 14、字符串比较

```
#!/bin/bash
#testing string equality

testuser=tiandi

if [ $USER = $testuser ]
then
	echo "Welcome $testuser"
fi

```

#### 15、读取列表中的值

```
#!/bin/bash

# basic for command
for test in Alabama Alaska Arizona
do
	echo The next state is $test
done

```

#### 16、打印99乘法表

```
#!/bin/bash

for i in `seq 9`
do 
 for j in `seq $i`
 do 
 echo -n "$j*$i=$[i*j] "
 done
    echo
done

```

#### 17、脚本编写 求和 函数运算 function xx()

```
#!/bin/bash

function sum()
{<!-- -->
 s=0;
 s=$[$1+$2]
 echo $s
}
read -p "input your parameter " p1
read -p "input your parameter " p2

sum $p1 $p2

function multi()
{<!-- -->
 r=0;
 r=$[$1/$2]
 echo $r
}
read -p "input your parameter " x1
read -p "input your parameter " x2

multi $x1 $x2

v1=1
v2=2
let v3=$v1+$v2
echo $v3

```

#### 18、用户猜数字

```
#!/bin/bash

# 脚本生成一个 100 以内的随机数,提示用户猜数字,根据用户的输入,提示用户猜对了,
# 猜小了或猜大了,直至用户猜对脚本结束。

# RANDOM 为系统自带的系统变量,值为 0‐32767的随机数
# 使用取余算法将随机数变为 1‐100 的随机数
num=$[RANDOM%100+1]
echo "$num"

# 使用 read 提示用户猜数字
# 使用 if 判断用户猜数字的大小关系:‐eq(等于),‐ne(不等于),‐gt(大于),‐ge(大于等于),
# ‐lt(小于),‐le(小于等于)
while :
do 
 read -p "计算机生成了一个 1‐100 的随机数,你猜: " cai  
    if [ $cai -eq $num ]   
    then     
        echo "恭喜,猜对了"     
        exit  
     elif [ $cai -gt $num ]  
     then       
            echo "Oops,猜大了"    
       else      
            echo "Oops,猜小了" 
  fi
done

```

#### 19、编写剪刀 、 石头、布游戏

```
#!/bin/bash

game=(石头 剪刀 布)
num=$[RANDOM%3]
computer=${game[$sum]}

echo "请根据下列提示选择您的出拳手势"
echo " 1. 石头"
echo " 2. 剪刀"
echo " 3. 布 "

read -p "请选择 1-3 ：" person
case $person in
1)
  if [ $num -eq 0 ]
  then 
    echo "平局"
    elif [ $num -eq 1 ]
    then
      echo "你赢"
    else 
      echo "计算机赢"
fi;;
2)
 if [ $num -eq 0 ]
 then
    echo "计算机赢"
    elif [ $num -eq 1 ] 
    then
     echo "平局"
    else 
      echo "你赢"
fi;;
3)
 if [ $num -eq 0 ]
 then  
   echo "你赢"
   elif [ $num -eq 1 ]
   then 
     echo "计算机赢"
   else 
      echo "平局"
fi;;
*)
  echo "必须输入1-3 的数字"
esac

```

#### 20、检测当前用户是否为管理员

```
#!/bin/bash

# 检测本机当前用户是否为超级管理员
if [ $USER == "root" ]
then
 echo "您是管理员，有权限安装软件"
else
 echo "您不是管理员，没有权限安装软件"
fi

```

#### 21、接收参数

传入参数3运行：`sh demo.sh 3`，控制台会打印：wo ai wenxing

```
#!/bin/bash -xv

if [ $1 -eq 2 ] ;then
 echo "wo ai wenmin"
elif [ $1 -eq 3 ] ;then
 echo "wo ai wenxing "
elif [ $1 -eq 4 ] ;then
 echo "wo de xin "
elif [ $1 -eq 5 ] ;then
 echo "wo de ai "
fi

```

#### 22、读取控制台传入的参数

```
#!/bin/bash
read -t 7 -p "input your name " NAME
echo $NAME

read -t 11 -p "input you age " AGE
echo $AGE

read -t 15 -p "input your friend " FRIEND
echo $FRIEND

read -t 16 -p "input your love " LOVE
echo $LOVE

```

#### 23、获取用户输入

```
#!/bin/bash

# testing the reading command

echo -n "Enter your name:"
read name
echo "Hello $name, welcome to my program"

read -p "Please enter your age: " age
days=$[ $age * 365 ]
echo "That makes you over $days days old"

#指定多个变量，输入的每个数据值都会分配给表中的下一个变量，如果用完了，就全分配各最后一个变量
read -p "Please enter name:" first last
echo "Checking data for $last. $first..."

#如果不指定变量，read命令就会把它收到的任何数据都放到特殊环境变量REPLY中
read -p "Enter a number:"
factorial=1
for (( count=1; count&lt;=$REPLY; count++))
do
	factorial=$[ $factorial * $count ]
done
echo "The factorial of $REPLY is $factorial"


```

#### 24、根据计算机当前时间，返回问候语

```
#!/bin/bash
# 根据计算机当前时间,返回问候语,可以将该脚本设置为开机启动 

# 00‐12 点为早晨,12‐18 点为下午,18‐24 点为晚上
# 使用 date 命令获取时间后,if 判断时间的区间,确定问候语内容
tm=$(date +%H)
if [ $tm -le 12 ];then
 msg="Good Morning $USER"
elif [ $tm -gt 12 -a $tm -le 18 ];then
   msg="Good Afternoon $USER"
else
   msg="Good Night $USER"
fi
echo "当前时间是:$(date +"%Y‐%m‐%d %H:%M:%S")"
echo -e "\033[34m$msg\033[0m"

```

### 二. 文件操作

#### 1、将字符串写入到文件中

比如，将 I love cls 写入到 demo.txt 文件中

```
#!/bin/bash

cd /home/wenmin/
touch demo.txt
echo "I love cls" &gt;&gt;demo.txt

```

#### 2、目录文件计数

```
#!/bin/bash

# count number of files in your PATH

mypath=`echo $PATH | sed 's/:/ /g'`
count=0
for directory in $mypath
do
	check=`ls $directory`
	echo $check
	for item in $check
	do
		count=$(( $count + 1 ))
	done
	echo "$directory - $count"
	count=0
done


```

#### 3、从文件中读取数据

```
#!/bin/bash
# reading data from a file

count=1
cat test | while read line
do
	echo "Line $count: $line"
	count=$[ $count + 1 ]
done
echo "Finished processing the file"

```

#### 4、用脚本实现复制

```
#!/bin/bash

cp $1 $2

```

#### 5、用脚本实现文件是否存在的判断

```
#!/bin/bash

if [ -f file.txt ];then
 echo "文件存在"
else 
 echo "文件不存在"
fi

```

#### 6、检查指定目录下是否有指定文件

```
#!/bin/bash

if [ -f /home/wenmin/datas ]
then 
echo "File exists"
fi

```

#### 7、脚本 每周 5 使用 tar 命令备份/var/log 下的所有日志文件

```
#!/bin/bash
# 每周 5 使用 tar 命令备份/var/log 下的所有日志文件
# vim  /root/logbak.sh
# 编写备份脚本,备份后的文件名包含日期标签,防止后面的备份将前面的备份数据覆盖
# 注意 date 命令需要使用反引号括起来,反引号在键盘&lt;tab&gt;键上面

tar -czf log-`date +%Y%m%d`.tar.gz /var/log 

# crontab -e #编写计划任务，执行备份脚本
00 03 * * 5 /home/wenmin/datas/logbak.sh

```

#### 8、sed文件操作

```
#!/bin/bash

#向文件写入
sed '1,2w test1' test1

echo -e "next\n"

#从文件读取
sed '3r ./test' ./test

echo -e "next\n"

#从文件读取，并插入字符流
sed '/lazy/r test' test

#向数据流末尾添加数据
sed '$r test' test

echo -e "next1\n"

sed '/lazy/ {
r test
d
}' test

```

### 三. 实用工具

#### 1、定时执行脚本

```
#!/bin/bash

# testing the at command

at -f 4.sh 22:10

```

#### 2、查看有多少ip在连接本机

```
#!/bin/bash
# 查看有多少远程的 IP 在连接本机(不管是通过 ssh 还是 web 还是 ftp 都统计) 

# 使用 netstat ‐atn 可以查看本机所有连接的状态,‐a 查看所有,
# -t仅显示 tcp 连接的信息,‐n 数字格式显示
# Local Address(第四列是本机的 IP 和端口信息)
# Foreign Address(第五列是远程主机的 IP 和端口信息)
# 使用 awk 命令仅显示第 5 列数据,再显示第 1 列 IP 地址的信息
# sort 可以按数字大小排序,最后使用 uniq 将多余重复的删除,并统计重复的次数
netstat -atn  |  awk  '{print $5}'  | awk  '{print $1}' | sort -nr  |  uniq -c

```

#### 3、实时监控本机内存和硬盘剩余空间

剩余内存小于500M、根分区剩余空间小于1000M时，发送报警邮件给root管理员

```
#!/bin/bash

# 实时监控本机内存和硬盘剩余空间,剩余内存小于500M、根分区剩余空间小于1000M时,发送报警邮件给root管理员

# 提取根分区剩余空间
disk_size=$(df / | awk '/\//{print $4}')

# 提取内存剩余空空间
mem_size=$(free | awk '/Mem/{print $4}')
while :
do 
# 注意内存和磁盘提取的空间大小都是以 Kb 为单位
if  [  $disk_size -le 512000 -a $mem_size -le 1024000  ]
then
    mail  ‐s  "Warning"  root  &lt;&lt;EOF
 Insufficient resources,资源不足
EOF
fi
done

```

#### 4、统计当前 Linux 系统中可以登录计算机的账户有多少个

```
#!/bin/bash

# 统计当前 Linux 系统中可以登录计算机的账户有多少个
#方法 1:
grep "bash$" /etc/passwd | wc -l
#方法 2：
awk -f : '/bash$/{x++}end{print x}' /etc/passwd

```

#### 5、杀掉 tomcat 进程并重新启动

```
#!/bin/bash

#kill tomcat pid

pidlist=`ps -ef|grep apache-tomcat-7.0.75|grep -v "grep"|awk '{print $2}'`  #找到tomcat的PID号

echo "tomcat Id list :$pidlist"  //显示pid

kill -9 $pidlist  #杀掉改进程

echo "KILL $pidlist:" //提示进程以及被杀掉

echo "service stop success"

echo "start tomcat"

cd /opt/apache-tomcat-7.0.75

pwd 

rm -rf work/*

cd bin

./startup.sh #;tail -f ../logs/catalina.out

```

#### 6、使用return命令返回函数

```
#!/bin/bash

# using the return command in a function

function db1 {<!-- -->
	read -p "Enter a value:" value
	echo "doubling the value"
	return $[ $value * 2 ]
}

db1
echo "The new value is $?"

```

#### 7、用脚本安装memcached服务器

```
#!/bin/bash
# 一键部署 memcached 

# 脚本用源码来安装 memcached 服务器
# 注意:如果软件的下载链接过期了,请更新 memcached 的下载链接
wget http://www.memcached.org/files/memcached-1.5.1.tar.gz
yum -y install gcc
tar -xf  memcached‐1.5.1.tar.gz
cd memcached‐1.5.1
./configure
make
make install

```

#### 8、备份MySQL数据库

```
#!/bin/sh

source /etc/profile
dbName=mysql
tableName=db
echo [`date +'%Y-%m-%d %H:%M:%S'`]' start loading data...'
mysql -uroot -proot -P3306 ${dbName} -e "LOAD DATA LOCAL INFILE '# /home/wenmin/wenxing.txt' INTO TABLE ${tableName} FIELDS TERMINATED BY ';'"
echo [`date +'%Y-%m-%d %H:%M:%S'`]' end loading data...'
exit
EOF

```

#### 9、一键部署 LNMP（RPM 包版本）

```
#!/bin/bash 

# 一键部署 LNMP(RPM 包版本)
# 使用 yum 安装部署 LNMP,需要提前配置好 yum 源,否则该脚本会失败
# 本脚本使用于 centos7.2 或 RHEL7.2
yum -y install httpd
yum -y install mariadb mariadb-devel mariadb-server
yum -y install php php-mysql

systemctl start httpd mariadb
systemctl enable httpd mariadb

```

### 四. 图形化操作

#### 1、打印带颜色的棋盘

```
#!/bin/bash
# 打印国际象棋棋盘
# 设置两个变量,i 和 j,一个代表行,一个代表列,国际象棋为 8*8 棋盘
# i=1 是代表准备打印第一行棋盘,第 1 行棋盘有灰色和蓝色间隔输出,总共为 8 列
# i=1,j=1 代表第 1 行的第 1 列;i=2,j=3 代表第 2 行的第 3 列
# 棋盘的规律是 i+j 如果是偶数,就打印蓝色色块,如果是奇数就打印灰色色块
# 使用 echo ‐ne 打印色块,并且打印完成色块后不自动换行,在同一行继续输出其他色块
for i in {<!-- -->1..8}
do
   for j in {<!-- -->1..8}
   do
    sum=$[i+j]
  if [  $[sum%2] -eq 0 ];then
    echo -ne "\033[46m  \033[0m"
  else
   echo -ne "\033[47m  \033[0m"
  fi
   done
   echo
done

```

#### 2、使用msgbox部件

```
#!/bin/bash

dialog --title text --msgbox "This is a test" 10 20

```

#### 3、使用菜单显示指令操作

```
#!/bin/bash

function menu {<!-- -->
	clear
	echo
	echo -e "\t\tSys Admin Menu\n"
	echo -e "\t1. Display disk space"
	echo -e "\t2. Display logged on users"
	echo -e "\t3. Display memory usage"
	echo -e "\t0. Exit program\n\n"
	echo -en "\t\tEnter option:"
	read -n 1 option
}

function diskspace {<!-- -->
	clear 
	df -k
}

function whoseon {<!-- -->
	clear
	who
}

function menusage {<!-- -->
	clear
	cat /proc/meminfo
}

while [ 1 ]
do
	menu
	case $option in
	0) 
		break;;
	1) 
		diskspace;;
	2)
		whoseon;;
	3)
		menusage;;
	*)
		clear
		echo "Sorry, wrong selection";;
	esac
	echo -en "\n\n\t\tHit any key to continue"
	read -n 1 line
done
clear

```

#### 4、在脚本中使用dialog命令

```
#!/bin/bash

# using dialog to create a menu

temp=`mktemp -t test.XXXXXX`
temp2=`mktemp -t test2.XXXXXX`

function diskspace {<!-- -->
	df -k &gt; $temp
	dialog --textbox $temp 20 60
}

function whoseon {<!-- -->
	who &gt; $temp
	dialog --textbox $temp 20 50
}

function menusage {<!-- -->
	cat /proc/meminfo &gt; $temp
	dialog --textbox $temp 20 50
}

while [ 1 ]
do
	dialog --menu "Sys Admin Menu" 20 30 10 1 "Display disk space" 2 "Display users" 3 "Display memory usage" 0 "Exit" 2&gt; $temp2
	if [ $? -eq 1 ]
	then
		break
	fi

	selection=`cat $temp2`

	case $selection in
	1)
		diskspace;;
	2)
		whoseon;;
	3)
		menusage;;
	0)
		break;;
	*)
		dialog --msgbox "Sorry,invalid selection" 10 30
	esac
done
rm -f $temp 2&gt; /dev/null
rm -f $temp2 2&gt; /dev/null

```

#### 5、使用select命令

```
#!/bin/bash
# using select in the menu

function diskspace {<!-- -->
	clear 
	df -k
}

function whoseon {<!-- -->
	clear
	who
}

function menusage {<!-- -->
	clear
	cat /proc/meminfo
}

PS3="Enter option:"
select option in "Display disk space" "Display logged on users" "Display memory usage" "Exit program"
do
	case $option in
	"Exit program")
		break;;
	"Display disk space")
		diskspace;;
	"Display logged on users")
		whoseon;;
	"Display memory usage")
		menusage;;
	*)
		clear
		echo "Sorry, wrong selection";;
	esac
done
clear

```

### 五. sed操作

#### 1、sed编辑器基础

```
#!/bin/bash
#sed编辑器基础

#替换标记
sed 's/lazy/ht/' ./test

echo -e "next\n"

#可用的替换标记
#1.数字 表明新闻本将替换第几处模式匹配的地方
sed 's/lazy/ht/2' ./test
#2.g 表明新文件将会替换所有已有文本出现的地方
sed 's/lazy/ht/g' ./test
#3.p 表明原来行的内容要打印出来,替换后的
sed 's/lazy/ht/p' ./test
#4.w file 将替换的结果写到文件中
sed 's/lazy/ht/w test1' ./test

echo -e "next\n"

#替换字符
sed 's/\/bin\/bash/\/bin\/csh/' /etc/passwd
#或者
sed 's!/bin/bash!/bin/csh!' /etc/passwd

echo -e "next\n"

#使用地址
#1.数字方式的行寻址
sed '2s/lazy/cat/' ./test
sed '2,3s/lazy/cat/' ./test
sed '2,$s/lazy/cat/' ./test
#2.使用文本模式过滤器
sed '/tiandi/s/bash/csh/' /etc/passwd

echo -e "next\n"

#组合命令
sed '2{
s/fox/elephant/
s/dog/cat/
}' test
sed '2,${
s/fox/elephant/
s/dog/cat/
}' test

echo -e "next\n"

#删除行
sed '3d' ./test
sed '2,$d' ./test
sed '/number 1/d' ./test
#删除两个文本模式来删除某个范围的行，第一个开启删除功能，第二个关闭删除功能
sed '/1/,/3/d' ./test

echo -e "next\n"

#插入和附加文本
sed '3i\
This is an appended line.' ./test

sed '$a\
This is a new line of text.' ./test

#修改行
sed '3c\
This a changed line of text.' ./test
sed '/number 1/c\
This a changed line of text.' ./test
#替换两行文本
#sed '2,3c\
#This a changed line of text.' ./test

#转换命令，处理单个字符
#sed 'y/123/789/' ./test

echo -e "next\n"

#回顾打印
# p 打印文本行
# -n 禁止其他行，只打印包含匹配文本模式的行
sed -n '/number 3/p' ./test

#查看修改之前的行和修改之后的行
#sed -n '/3/{<!-- -->
#p
#s/line/test/p
#}' ./test

echo -e "next\n"

# 打印行号
sed '=' ./test

#打印指定的行和行号
#sed -n '/lazy/{<!-- -->
#=
#p
#}' ./test

#列出行 打印数据流中的文本和不可打印的ASCII字符，任何不可打印的字符都用它们的八进制值前加一个反斜线或标准C风格的命名法，比如用\t来代表制表符
sed -n 'l' ./test


```

#### 2、输出末尾指定行数的数据

```
#!/bin/bash
#输出末尾10行数据

sed '{
:start
$q
N
11,$D
b start
}' /etc/passwd

```

#### 3、删除指定的空白行和删除html标签

```
#!/bin/bash

#多个空格只保留一个
#sed '/./,/^$/!d' test

#删除开头的空白行
#sed '/./,$!d' test

#删除结尾的空白行
sed '{
:start
/^\n*$/{$d; N; b start}
}' test

#删除html标签
#有问题
#s/&lt;.*&gt;//g

#sed 's/&lt;[^&gt;]*&gt;//g' test1

#sed 's/&lt;[^&gt;]*&gt;//g;/^$/d' test1

```

#### 4、模式替代

```
#!/bin/bash

#and符号，代表替换命令中的匹配模式，不管预定义模式是什么文本，都可以用and符号替换，and符号会提取匹配替换命令中指定替换模式中的所有字符串
echo "The cat sleeps in his hat" | sed 's/.at/"&amp;"/g'

#替换单独的单词
echo "The System Administrator manual" | sed 's/\(System\) Administrator/\1 user/'

#在长数字中插入逗号
echo "1234567" | sed '{:start; s/\(.*[0-9]\)\([0-9]\{3\}\)/\1,\2/; t start}'

```

### 六. gawk操作

#### 1、使用变量

```
#!/bin/bash
#使用内建变量

# NF 当前记录的字段个数
# NR 到目前为止读的记录数量
#下面的程序在每行开头输出行号，并在最后输出文件的总字段数
gawk '{ total+=NF; print NR, $0 }END{ print "Total: ", total}'

gawk 'BEGIN {testing="This is a test";  print testing; testing=45;  print testing}'

#处理数字值

gawk 'BEGIN{x=4; x= x*2+3; printx}'

#处理数组
gawk 'BEGIN{capital["Ill"] = "SprintField"; print capital["Ill"]}'

#遍历数组变量
gawk 'BEGIN{
var["a"] = 1
var["g"] = 2
var["m"] = 3
for( test in var)
{
	print "Index:",test,"- Value:",var[test]
}
}'

print "------"

#删除数组变量
gawk 'BEGIN{
var["a"] = 1
var["g"] = 2
for (test in var)
{
	print "Index:",test," - Value:", var[test]
}
delete var["g"]

print "----"

for (test in var)
{
	print "Index;",test," - Value:", var[test]
}
}'

```

#### 2、使用模式，结构化命令

```
#!/bin/bash
#正则表达式

gawk 'BEGIN{FS=","} 
/11/{print $1}
' test

#if-else语句
gawk '{
if($1 &gt; 20)
{
	x=$1*20
	print x
}
else
{
	x=$1/2
	print x
}
}' test

#while 语句
gawk '{
total = 0
i=1
while(i&lt;4)
{
	total+=$i
	i++
}
avg = total/3
print "Average:".avg
}' test


#do-while语句
gawk '{
total=0
i=1
do
{
	total += $i
	i++
}while(total &lt; 150)
print total }' test


#for语句
gawk '{
total = 0
for (i=1; i&lt;4; i++)
{
	total+=$i
}
avg = total/3
print "Average:".avg
}' test

```

#### 3、自定义函数

```
#!/bin/bash
#gawk 自定义函数

gawk '
function myprint()
{
	printf "%-16s - %s\n", $1, $4
}
BEGIN{FS="\n"; RS=""}
{
	myprint()
}' test

```

#### 4、调用函数库和脚本

```
#!/bin/bash

#使用函数库和gawk脚本

gawk -f gawk函数库 -f gawk脚本 test

```

#### 5、输出

```
#!/bin/bash

#print用于产生简单输出
#多个表达式的字符串值之间用输出字段分隔符分开

gawk '{ print $1, $2 }'

#输出字段分割符与输出记录分隔符存储在内建变量OFS与ORS中，
#初始情况下，OFS与ORS被设置成一个空格符与一个换行符，但它们的值可以在任何时候改变
#下面这个程序打印每一行的第1第2个字段，字段之间用分号分开，在每一行的第2个字段之后输出两个换行符

gawk 'BEGIN { OFS = ":"; ORS = "\n\n" }
      { print $1, $2 }'

#下面这个程序拼接第1个与第2个字段，两个字段之间没有输出字段分隔符插入

gawk '{ print $1 $2 }'

#这两句话等价

gawk '{ print }'
gawk '{ print $0 }'

#输出空行

gawk '{ print "" }'


#printf用于产生格式化输出

#printf不会自动换行，需要手动添加\n
#格式说明符以%开始，以转换字符结束
# - 表达式在它的域内左对齐，没有则右对齐
# width 为了达到规定的宽度，必要时填充空格
# .prec 字符串最大宽度, 或十进制数的小数部分的位数

gawk '{ printf ("Name:%-10sAge:%-5dWeight:%7.2f\n", $1, $2, $3) }'


#输出到文件
#重定向运算符&gt;与&gt;&gt;用于将输出重定向到文件，文件名必须用双引号括起来

#下面这个程序将所有输入行的第1个与第3个字段输出到两个文件中：如果第3个字段大于100，则输出到bigpop，否则输出到smallpop
gawk '{ print($1, $3) &gt; ($3 &gt; 100 ? "bigpop" : "smallpop") }'


#输出到管道
#print的输出将以管道的方式传递给command

# Canada 3852
# China 3705
# USA 3615
# Brazil 3286

gawk '{ pop[$1]+=$2 }
END{ for(c in pop) printf("%15-s%6d\n", c, pop[c]) | "sort -nk 2"; close("sort -nk 2") }'


#关闭文件与管道
#语句close(expression)关闭一个文件或管道，文件或管道由expression指定。
#expression的字符串值必须与最初用于创建文件或管道的字符串值相同。
#在同一个程序中，如果你写了一个文件，而待会儿想要读取它，那么就需要调用close。
#某一时刻，同时处于打开状态的文件或管道数量最大值由实现定义。

close("sort -nk 2")


```
