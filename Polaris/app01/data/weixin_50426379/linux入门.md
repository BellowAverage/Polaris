
--- 
title:  linux入门 
tags: []
categories: [] 

---


#### 文章目录
- - <ul><li>- - <ul><li>- - - - - - - <ul><li>- - - <ul><li>- - - - 


## Linux入门

### 一、Linux和Windows的区别？

1.Linux是**开源**的（open source），Windows不开源

2.Windows**用户多**–》图形化界面、点鼠标、入门容易–》对用户友好

3.Linux在**企业中使用量很多**

### 二、Linux内核

#### 1.查看内核版本

[root@scchen lianxi]# <mark>uname -r</mark> --》查看Linux内核的版本 3.10.0-1160.el7.x86_64

#### 2.内核是什么

操作系统是一个软件，而<mark>操作系统</mark><mark>内部最核心的软件是内核kernel</mark>，如果将操作系统比喻成一台汽车的话，那内核就是汽车的发动机

#### 3.内核的作用：（是对硬件进行管理的）

1.对CPU进行调度管理

2.对内存进行分配管理

3.对磁盘（文件系统）进行管理

4.对进程进行管理

5.对其他硬件进行管理

<img src="https://img-blog.csdnimg.cn/img_convert/81f0e19c5ae138bf47f13b7795c5af50.png" alt="image.png">

推荐操作系统的书籍：操作系统openEuler

### 三、命令提示符

#### 主提示符：第1提示符–》

<mark>PS1</mark> ：（prompt symbol）是第一提示符，操作系统里预先定义了，直接使用

提示符的作用：给使用者提示

提示符：

[root@scchen ~]# --》root用户

[dengchao@scchen ~]$ --》普通用户

```
[root@siyuxiang ~]# echo $PS1
[\u@\h \W]\$
[root@siyuxiang ~]# set  #查看终端中定义的变量，包括预定义变量和自定义变量
PS1='[\u@\h \W]\$ '

```

<mark>PS1是变量名</mark> <mark>[] 只是符号，没有特殊作用</mark> <mark>\u 代表引用用户名 user</mark> <mark>@ 只是符号，用来分割</mark> <mark>\h 代表引用主机名 hostname</mark> <mark>\W 代表引用你当前所在的工作目录–》working</mark> <mark>$ 当我们的用户的uid是0的时候，就显示# 非0 就显示$</mark> uid 是user的id 用户的编号 id card 身份证 uid 为0的用户是root

#### 查看用户的id

```
[root@siyuxiang ~]# id root
uid=0(root) gid=0(root) 组=0(root)
[root@siyuxiang ~]# id dengchao
uid=1001(dengchao) gid=1001(dengchao) 组=1001(dengchao)
[root@siyuxiang ~]# 

```

#### 修改PS1

```
[dengchao@siyuxiang ~]$ echo  $PS1
[\u@\h \W]\$
[dengchao@siyuxiang ~]$ PS1='[\h@\u \t@\W]\$sanchuang '  #PS1变量修改后立马生效
[siyuxiang@dengchao 16:53:22@~]$sanchuang 
[siyuxiang@dengchao 16:54:10@~]$sanchuang 
[siyuxiang@dengchao 16:54:10@~]$sanchuang 
[siyuxiang@dengchao 16:54:10@~]$sanchuang
#不推荐修改PS1变量，因为默认的非常经典
[siyuxiang@dengchao 16:54:10@~]$sanchuang PS1='[\u@\h \W]\$'
[dengchao@siyuxiang ~]$

```

#### 修改主机名

##### 临时修改主机名

```
[root@localhost ~]# hostname
localhost.localdomain
[root@localhost ~]# hostname  www.sanchuang.com  临时修改主机名，重启系统会导致名字失效
[root@localhost ~]# hostname
www.sanchuang.com
[root@localhost ~]# hostname  www
[root@localhost ~]# hostname
www
[root@localhost ~]# 

```

<mark>临时修改了主机名后不会立马生效</mark>，需要<mark>重新登录或者切换用户</mark>才会在PS1变量里体现出来

```
[root@localhost ~]# su      #不接用户，就是切换到自己重新登录
[root@www ~]#               #修改的主机名生效

```

```
[root@wh ~]# cat /etc/hostname
wh
[root@wh ~]# hostname weihong
[root@wh ~]# su
[root@weihong ~]# cat /etc/hostname 
wh                 #临时修改主机名，文件里面的值没有更改
[root@weihong ~]#       

```

##### 永久修改主机名

```
[root@localhost ~]# hostnamectl  set-hostname  siyuxiang  永久修改主机名，并且立马生效，同时也修改了/etc/hostname文件
#hostnamectl    是命令
#set-hostname   修改主机名
#siyuxiang      具体的名字

[root@localhost ~]# hostname
siyuxiang
[root@localhost ~]# cat  /etc/hostname
siyuxiang
[root@localhost ~]# 
[root@localhost ~]# su - root
上一次登录：日 3月  6 16:17:10 CST 2022从 192.168.2.104pts/1 上
[root@siyuxiang ~]# reboot 重启系统

```

#### 定义变量

<mark>shell命令里=左右不要有空格，会导致命令失败</mark>

<mark>$符号接变量名就是引用变量的值</mark>

```
[root@scchen lianxi]# sg=luoyawei  定义变量sg
[root@scchen lianxi]# echo $sg
luoyawei
[root@scchen lianxi]# sg1 = luoyawei
-bash: sg1: 未找到命令

```

<mark>echo 就是输出内容到屏幕，echo后面需要一个空格，多个空格也可以</mark>

```
[root@scchen lianxi]# sg2="wujun wangyutao"
[root@scchen lianxi]# echo $sg2
wujun wangyutao

```

<mark>当定义的变量里面有空格时，建议使用双引号括起来，表示一个联系的字符串</mark>

```
[root@scchen lianxi]# echo "hello.world  sanchuang  $sg  $sg1"
hello.world sanchuang luoyawei

```

#### echo语句中单引号和双引号的区别？

shell编程里，<mark>单引号： 所见即所得，里面的特殊符号没有特殊的作用</mark> 双引号： $ 符号有特殊作用

```
[root@localhost ~]# sg="liuchang"
[root@localhost ~]# sg1='liuchang'
[root@localhost ~]# echo $sg
liuchang
[root@localhost ~]# echo $sg1
liuchang
[root@localhost ~]# echo "hello,sanchuang $sg $sg1"
hello,sanchuang liuchang liuchang
[root@localhost ~]# echo 'hello,sanchuang $sg $sg1'
hello,sanchuang $sg $sg1
[root@localhost ~]# sg2="sanchuang $sg"
[root@localhost ~]# echo $sg2
sanchuang liuchang
[root@localhost ~]# sg3='sanchuang $sg'
[root@localhost ~]# echo $sg3
sanchuang $sg
[root@localhost ~]# 

```

#### 变量的类型

​ 1.预定义变量–》大写，例如PS1

​ 2.自定义变量–》喜欢使用小写，例如自己定义的sg变量

```
[root@scchen lianxi]# echo $PS1
[\u@\h \W]\$

[root@scchen lianxi]# set  

PS1='[\u@\h \W]\$ '
PS2='&gt; '
PS4='+ '

```

<mark>set</mark>：查看当前终端里定义的变量，包括预定义变量和自定义变量

### 四、文件夹结构

<img src="https://img-blog.csdnimg.cn/img_convert/69f7532af3ca551e27f54ca628060aec.png" alt="image.png">

<img src="https://img-blog.csdnimg.cn/img_convert/a03743f6a2944bea8097fdc16ca8b5e8.png" alt="image.png">

### 五、用户命令

#### centos7

##### 查看版本

```
[root@localhost ~]# cat  /etc/centos-release  #查看centos系统的版本
CentOS Linux release 7.9.2009 (Core)

```

##### 新建用户

```
[root@localhost ~]# useradd dengchao   #新建用户dengchao

root@localhost ~]# su  -  dengchao  #从当前的root用户切换到dengchao用户
[dengchao@localhost ~]$ pwd       #查看当前所在的路径--》你现在在哪个文件夹里
/home/dengchao  

```

~：家目录，用户登录进入系统的时候所在的文件夹 home directory

<mark>普通用户的家目录： /home/username</mark> <mark>root用户的家目录： /root</mark> <mark>root用户可以进入任何用户的家目录</mark> <mark>普通用户只能进入自己的家目录</mark>

```
[root@siyuxiang ~]# cd ~liwenqian
[root@siyuxiang liwenqian]# pwd
/home/liwenqian
[root@siyuxiang liwenqian]# su  -  dengchao
上一次登录：日 3月  6 16:37:16 CST 2022pts/0 上
[dengchao@siyuxiang ~]$ cd ~liwenqian
-bash: cd: /home/liwenqian: 权限不够
[dengchao@siyuxiang ~]$ 

```

<mark>root用户su到任何用户都不需要密码</mark> <mark>普通用户切换到任何用户都需要密码</mark>

#### ubantu

##### 查看版本

```
root@fengdeyong:~# cat   /etc/issue  #在Ubuntu里查看系统的版本
Ubuntu 21.10 \n \l

```

##### 新建用户

```
sc@fengdeyong:~$ sudo  useradd feng  #ubantu里面需要超级用户才能新建用户，所以需要加命令sudo
[sudo] password for sc: 

sc@fengdeyong:~$ su - feng  
Password: 
su: Authentication failure

sc@fengdeyong:~$ sudo  passwd  feng
New password: 
Retype new password: 
passwd: password updated successfully


```

##### 有关root用户相关操作

Ubuntu里<mark>默认情况下root用户是禁用的</mark>，使用安装Ubuntu的时候新建的用户登录，哪个用户相当于root用户

```
sc@fengdeyong:~$ sudo passwd  root  给root用户设置密码，启用root用户
New password: 
Retype new password: 
passwd: password updated successfully
sc@fengdeyong:~$ su - root
Password: 
root@fengdeyong:~# 

```

<mark>root用户可以给任何用户设置密码</mark>

```
[root@localhost ~]# passwd  dengchao
更改用户 dengchao 的密码 。
新的 密码：
无效的密码： 密码少于 8 个字符
重新输入新的 密码：
passwd：所有的身份验证令牌已经成功更新。

[root@localhost ~]# su - liwenqian
上一次登录：日 3月  6 14:36:18 CST 2022pts/0 上
[liwenqian@localhost ~]$ su - dengchao   切换到dengchao用户，输入dengchao用户的密码
密码：
上一次登录：日 3月  6 11:41:22 CST 2022pts/0 上
最后一次失败的登录：日 3月  6 14:44:45 CST 2022pts/0 上
最有一次成功登录后有 1 次失败的登录尝试。
[dengchao@localhost ~]$ 

```

ubantu用户在本地可以登陆，但是远程不可以，需要<mark>修改远程登陆服务的配置文件，允许root用户登陆，启用root用户远程登陆</mark>

```
root@fengdeyong:~# sudo vim /etc/ssh/sshd_config  修改ssh服务的配置文件
PermitRootLogin yes
root@fengdeyong:~# sudo  service sshd restart  #重启刷新sshd服务，让刚刚修改的配置生效

```

#### 请你讲讲centos和Ubuntu的区别？

​ 1.不同的公司出品的系统 ​ centos是redhat公司 ​ Ubuntu是canonical公司出品 ​ 2.有少数不同的命令的差异 ​ yum install vim --》centos ​ apt install vim --》Ubuntu ​ 3.Ubuntu默认是禁用root用户的 ​ 所以Ubuntu很多命令前面都需要执行sudo命令 ​ 4.Ubuntu喜欢快速的更新系统，推出新版本，迭代更新非常快

共同点都是开源并且免费，都是属于linux系统

#### 切换用户和退出用户

<img src="https://img-blog.csdnimg.cn/img_convert/65aa3e3e661bcbba185cc197f43245d6.png" alt="image.png">

### 六、vim编辑器的使用

<img src="https://img-blog.csdnimg.cn/img_convert/7e276fbbdfd0d03db8173bc2efb169d8.png" alt="image.png">
