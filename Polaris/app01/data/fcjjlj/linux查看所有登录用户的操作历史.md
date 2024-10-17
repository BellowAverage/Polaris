
--- 
title:  linux查看所有登录用户的操作历史 
tags: []
categories: [] 

---
在linux系统的环境下，不管是root用户还是其它的用户只有登陆系统后用进入操作我们都可以通过命令history来查看历史记录，可是假如一台服务器多人登陆，一天因为某人误操作了删除了重要的数据。这时候通过查看历史记录（命令：history）是没有什么意义了（因为history只针对登录用户下执行有效，即使root用户也无法得到其它用户histotry历史）。那有没有什么办法实现通过记录登陆后的IP地址和某用户名所操作的历史记录呢？答案：有的。

### 通过在/etc/profile里面加入以下代码就可以实现：

```
PS1="`whoami`@`hostname`:"'[$PWD]'
history
USER_IP=`who -u am i 2&gt;/dev/null| awk '{print $NF}'|sed -e 's/[()]//g'`
if [ "$USER_IP" = "" ]
then
USER_IP=`hostname`
fi
if [ ! -d /tmp/dishdp ]
then
mkdir /tmp/dishdp
chmod 777 /tmp/dishdp
fi
if [ ! -d /tmp/dishdp/${<!-- -->LOGNAME} ]
then
mkdir /tmp/dishdp/${<!-- -->LOGNAME}
chmod 300 /tmp/dishdp/${<!-- -->LOGNAME}
fi
export HISTSIZE=4096
DT=`date "+%Y-%m-%d_%H:%M:%S"`
export HISTFILE="/tmp/dishdp/${LOGNAME}/${USER_IP} dishdp.$DT"
chmod 600 /tmp/dishdp/${<!-- -->LOGNAME}/*dishdp* 2&gt;/dev/null
 

```

### source /etc/profile 使用脚本生效

### 退出用户，重新登录

上面脚本在系统的/tmp新建个dishdp目录，记录所有登陆过系统的用户和IP地址（文件名），每当用户登录/退出会创建相应的文件，该文件保存这段用户登录时期内操作历史，可以用这个方法来监测系统的安全性。

```
root@ecs-ywsj:/tmp/dishdp# ls
10.1.80.47 dishdp.2013-10-24_12:53:08 
root@ecs-ywsj:/tmp/dishdp# cat 10.1.80.47 dishdp.2013-10-24_12:53:08

```

#### 查看在12:53:08从10.1.80.47登录的root用户操作命令历史
