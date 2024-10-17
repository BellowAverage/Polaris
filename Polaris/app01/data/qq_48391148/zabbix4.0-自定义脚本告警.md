
--- 
title:  zabbix4.0-自定义脚本告警 
tags: []
categories: [] 

---
**目录**

















### 1、在zabbix-server端下载mailx

```
[root@zabbix-server ~]# yum install -y mailx
已加载插件：fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirrors.ustc.edu.cn
 * centos-sclo-rh: mirrors.ustc.edu.cn
 * centos-sclo-sclo: mirrors.ustc.edu.cn
 * extras: mirrors.ustc.edu.cn
 * updates: mirrors.ustc.edu.cn
base                                                                                             | 3.6 kB  00:00:00     
centos-sclo-rh                                                                                   | 3.0 kB  00:00:00     
centos-sclo-sclo                                                                                 | 3.0 kB  00:00:00     
extras                                                                                           | 2.9 kB  00:00:00     
updates                                                                                          | 2.9 kB  00:00:00     
zabbix                                                                                           | 2.9 kB  00:00:00     
zabbix-non-supported                                                                             | 2.9 kB  00:00:00     
正在解决依赖关系
--&gt; 正在检查事务
---&gt; 软件包 mailx.x86_64.0.12.5-19.el7 将被 安装
--&gt; 解决依赖关系完成

依赖关系解决

========================================================================================================================
 Package                   架构                       版本                               源                        大小
========================================================================================================================
正在安装:
 mailx                     x86_64                     12.5-19.el7                        base                     245 k

事务概要
========================================================================================================================
安装  1 软件包

总下载量：245 k
安装大小：466 k
Downloading packages:
mailx-12.5-19.el7.x86_64.rpm                                                                     | 245 kB  00:00:00     
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  正在安装    : mailx-12.5-19.el7.x86_64                                                                            1/1 
  验证中      : mailx-12.5-19.el7.x86_64                                                                            1/1 

已安装:
  mailx.x86_64 0:12.5-19.el7                                                                                            

完毕！

```

**#################################################### **

### 2、配置mailx配置文件

>  
 **编辑mailx配置文件，添加参数 ** 


```
vim /etc/mail.rc 

```

```
set from=发件邮箱@163.com smtp=smtp.163.com
set smtp-auth-user=发件邮箱@163.com smtp-auth-password=smtp授权码
set smtp-auth=login

```

>  
 **使用mailx测试能否发送邮件给对应收件邮箱** 


```
echo "this is a email for test from zabbix" | mail -s "zabbix test" 收件邮箱@163.com
```

>  
 **邮件接收显示成功** 


<img alt="" height="401" src="https://img-blog.csdnimg.cn/d59daee2281e4c4a958eea5f5d68cb13.png" width="646">

>  
 **刚才的测试是通过mailx来发送的邮件，那么怎么让zabbix-server找到这个脚本呢？** 


**#################################################### ** 

###  3、查看zabbix-server设置的 AlertScriptsPath变量

```
vim zabbix_server.conf 
AlertScriptsPath=/usr/lib/zabbix/alertscripts

```

### 4、在对应路径下面编写邮件脚本

>  
 **安装dos2unix包，这个包可以将正文变成附件的形式** 


```
yum install -y dos2unix

```

```
[root@zabbix-server alertscripts]# cd /usr/lib/zabbix/alertscripts/
[root@zabbix-server alertscripts]# cat sendmail.sh 
#!/bin/bash

sendto=$1   # 邮件发送给谁
subject=$2  # 邮件标题
body=$3     #邮件正文
FILE=/tmp/mail.tmp
echo "$body" &gt; $FILE
dos2unix -k $FILE    # 将正文变成附件
mail -s "$subject" "$sendto"  &lt; $FILE  # 发送邮件

```

>  
 **给与脚本可执行权限、** 


```
 chmod +x sendmail.sh 

```

>  
 **将zabbix设置为/tmp/mail.tmp的拥有者** 


```
chown zabbix.zabbix /tmp/mail.tmp 

```

>  
 **执行脚本，传入三个参数，测试是否可以发送邮件** 


```
./sendmail.sh 接收邮箱@163.com zabbix "123456zabbix"
```

>  
 **邮件接收成功** 


<img alt="" height="251" src="https://img-blog.csdnimg.cn/b32d69eb3bae45da913bc9a0bd4aef51.png" width="581">

**#################################################### ** 

###  5、创建一个媒介类型

<img alt="" height="584" src="https://img-blog.csdnimg.cn/1b69fb0bc78f4f15ae2252f84553a1d5.png" width="944">

<img alt="" height="586" src="https://img-blog.csdnimg.cn/d97d4240e16641ad9d9d2a8ced724030.png" width="1200"> 

**#################################################### ** 

### 6、为用户指定媒介类型

 <img alt="" height="847" src="https://img-blog.csdnimg.cn/d1a8a96fd6084839a28fd332f1fd7b00.png" width="1079">

**#################################################### ** 

###  7、更改触发器表达式进行测试

<img alt="" height="428" src="https://img-blog.csdnimg.cn/d5127598c5624d4e86c05bd13f2eb7ed.png" width="967">

>  
 ** 触发器触发成功，邮件已发送** 


<img alt="" height="845" src="https://img-blog.csdnimg.cn/607815f29cf54c0493f48cb9a6b12a70.png" width="1200">

 <img alt="" height="424" src="https://img-blog.csdnimg.cn/c863ae6bba464dfa8b822ac52e3715c9.png" width="667">

>  
 **将触发器修改回来以后，可以正常收到恢复邮件** 


<img alt="" height="417" src="https://img-blog.csdnimg.cn/aba772cfddbf448db0ae0d854a8ba1c9.png" width="833">

 <img alt="" height="384" src="https://img-blog.csdnimg.cn/3c81a7aa1ae34c9d9c57e425dc3b3291.png" width="544">

 

>  
 ** 邮件接收成功，使用脚本发送告警邮件的方式成功。** 


 
