
--- 
title:  Shell脚本之linux服务器磁盘利用率监控 
tags: []
categories: [] 

---
## 一、需求说明

  作为一名主机运维工程师，日常工作中我们每天都需要巡检服务器的运行情况，包括服务器的网络通断性、磁盘利用率、服务进程等内容。为了减少工作量我们可以通过编写shell脚本，实现服务器的批量巡检。写好脚本之后我们可以设置定时任务，将巡检结果邮件发送给自己就OK啦。我们查看磁盘利用率就是使用df -h的命令，可以显示各磁盘分区的使用情况，此脚本就是基于此命令基础实现。 <img src="https://img-blog.csdnimg.cn/85a50b17c6814ea4b81166bcf9adb461.png" alt="在这里插入图片描述">

## 二、脚本内容

  脚本主要设计思路是通过ssh免密远程登录待巡检主机，并执行df -h命令。通过awk命令过滤中磁盘利用率列值并与阈值进行比较，超过阈值的值记录下来。配置定时任务执行脚本，将巡检结果邮件告知。   脚本包含文件如下：
- 主脚本文件：disk_check.sh- 待巡检主机列表：hosts.txt- 检查结果临时文件：df.txt- 超过阈值磁盘信息临时文件：ls.txt
  脚本主体内容如下：

```
#!/bin/bash
#scriptname: disk_check.sh 
#author: wuhs
#description: 此脚本用于检查linux服务器的磁盘使用率，超过预警阈值则邮件告警
#version: v1.0

#参数定义
#脚本工作目录
resultfiledir=/root/scripts/xunjian/diskinfo
#待巡检服务器列表
hostlist="/root/scripts/xunjian/diskinfo/hosts.txt"
#告警阈值
warnsize=95
#切换到工作目录，定时任务执行时默认在bash路径下执行，所以需要在脚本中切换路径
curdir=`cd -P $(dirname $0); pwd`
cd $curdir

#删除上一次执行记录，也可以执行完成脚本后删除，执行前删除是方便收到告警时人工核查
rm -rf $resultfiledir/df.txt
#通过while循环读取待巡检服务器列表
while read line
do
  #获取带巡检主机名或者IP地址，建议主机名
  host=`echo $line | awk '{print $1}'`
  #获取待巡检主机ssh端口，考虑部分主机考虑安全修改了ssh服务端口
  port=`echo $line | awk '{print $2}'`
  #将当前巡检的主机写入巡检结果df.txt文件
  echo "$host 磁盘检查结果" &gt;&gt; $resultfiledir/df.txt
  #将获取到的df -h数据写入到df.txt文件，记得采用追加写入的方式
  ssh $host -p $port -n df -h &gt;&gt; $resultfiledir/df.txt
done &lt;"$hostlist"
#获取磁盘使用率列值
list=`cat df.txt |awk '{print int($5)}'`
rm -rf ls.txt
#使用率值与阈值进行比较
for val in $list
do
    if [ "$val" -gt "$warnsize" ];then
        #过滤大于阈值的磁盘结果行和主机名记录行
        cat df.txt |egrep "磁盘检查|$val%" |egrep -B 1 "$val%" &gt;&gt; ls.txt
    fi
done
#保证顺序的情况下删除重复项
awk '!a[$0]++' ls.txt &gt; tmp.txt
rm -rf ls.txt
mv tmp.txt ls.txt
#发送告警邮件
if [ -s ls.txt ]; then
    mailx -s "有超过磁盘使用率告警阈值$warnsize %的磁盘，请检查！" 
    1234567qq@qq.com &lt; ls.txt
else
    if [ $(date +%H) -eq 09 ];then
      mailx -s "磁盘使用率检查结果正常!" 1234567qq@qq.com &lt; df.txt
    fi
fi

```

## 三、使用示例

### 1、手动执行脚本

>  
 [root@s146 diskinfo]# sh disk_check.sh [root@s146 diskinfo]# ll total 16 -rw-r–r-- 1 root root 1098 Oct 26 17:46 df.txt -rwxr–r-- 1 root root 1432 Oct 26 17:17 disk_check.sh -rw-r–r-- 1 root root 16 Oct 26 16:47 hosts.txt -rw-r–r-- 1 root root 150 Oct 26 17:46 ls.txt [root@s146 diskinfo]# cat ls.txt s146 磁盘检查结果 /dev/sda1 1014M 207M 808M 21% /boot s166 磁盘检查结果 /dev/mapper/centos-root 38G 11G 27G 30% / <img src="https://img-blog.csdnimg.cn/9d47fcc37dd74dd791f2c3224848bf4e.png" alt="在这里插入图片描述"> 


### 2、定时任务执行
- 首先配置定时任务，每天的早上6点到晚上10点之间每个小时执行一次。定时任务的配置可以参考。
>  
 [root@s146 diskinfo]# crontab -l ####磁盘使用率监测定时任务#### 12 6-22/1 * * * /root/scripts/xunjian/diskinfo/diskinfo_check.sh &amp;&gt; /tmp/diskinfo_check.log 

- 邮件坐等巡检结果，linux服务器邮件发送可以参考。 <img src="https://img-blog.csdnimg.cn/32f020d14b1646f7a462a6ca96862508.png" alt="在这里插入图片描述">