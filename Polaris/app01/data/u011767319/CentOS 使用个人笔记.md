
--- 
title:  CentOS 使用个人笔记 
tags: []
categories: [] 

---
### 检查端口被哪个进程占用
-  `netstat -lnp|grep 8000` -  如下图，<img src="https://img-blog.csdn.net/20170102210940021?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxMTM4OTQ1Mg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" alt="在这里插入图片描述"> -  **找到进程号：11100** `ps 11100` **杀掉进程** `kill -9 11100` 
### CentOS下tar解压 gz解压 bz2等各种解压文件使用方法

**tar**

```
.tar 
　　解包：tar xvf FileName.tar 
　　打包：tar cvf FileName.tar DirName 
　　（注：tar是打包，不是压缩！） 
　　——————————————— 
　　.gz 
　　解压 1：gunzip FileName.gz 
　　解压2：gzip -d FileName.gz 
　　压缩：gzip FileName 
　　.tar.gz 和 .tgz 
　　解压：tar zxvf FileName.tar.gz 
　　压缩：tar zcvf FileName.tar.gz DirName 
　　——————————————— 
　　.bz2 
　　解压1：bzip2 -d FileName.bz2 
　　解压2：bunzip2 FileName.bz2 
　　压缩： bzip2 -z FileName 
　　.tar.bz2 
　　解压：tar jxvf FileName.tar.bz2        或tar --bzip xvf FileName.tar.bz2 
　　压缩：tar jcvf FileName.tar.bz2 DirName 
　　 ——————————————— 
　　.bz 
　　解压1：bzip2 -d FileName.bz 
　　解压2：bunzip2 FileName.bz 
　　压缩：未知 
　　.tar.bz 
　　解压：tar jxvf FileName.tar.bz 
　　压缩：未知 
　　——————————————— 
　　.Z 
　　解压：uncompress FileName.Z 
　　压缩：compress FileName 
　　.tar.Z 
　　解压：tar Zxvf FileName.tar.Z 
　　压缩：tar Zcvf FileName.tar.Z DirName 
　　——————————————— 
　　.zip 
　　解压：unzip FileName.zip 
　　压缩：zip FileName.zip DirName 
　　压缩一个目录使用 -r 参数，-r 递归。例： $ zip -r FileName.zip DirName 
　　——————————————— 
　　.rar 
　　解压：rar x FileName.rar 
　　压缩：rar a FileName.rar DirName 
　　 
　　rar 请到：http://www.rarsoft.com/download.htm 下载！ 
　　解压后请将rar_static拷贝到/usr /bin目录（其他由$PATH环境变量指定的目录也可以）： 
　　[root@www2 tmp]# cp rar_static /usr/bin/rar 
　　——————————————— 
　　.lha 
　　解压：lha -e FileName.lha 
　　压缩：lha -a FileName.lha FileName 
　　 
　　lha请到：http://www.infor.kanazawa-it.ac.jp/~ishii/lhaunix/下载！ 
　　&gt;解压后请将 lha拷贝到/usr/bin目录（其他由$PATH环境变量指定的目录也可以）： 
　　[root@www2 tmp]# cp lha /usr/bin/ 
　　——————————————— 
　　.rpm 
　　解包：rpm2cpio FileName.rpm | cpio -div 
　　——————————————— 
　　.deb 
　　解包：ar p FileName.deb data.tar.gz | tar zxf - 
　　——————————————— 
　　.tar .tgz .tar.gz .tar.Z .tar.bz .tar.bz2 .zip .cpio .rpm .deb .slp .arj .rar .ace .lha .lzh .lzx .lzs .arc .sda .sfx .lnx .zoo .cab .kar .cpt .pit .sit .sea 
　　解压：sEx x FileName.* 
　　压缩：sEx a FileName.* FileName 
　　 
　　sEx只是调用相关程序，本身并无压缩、解压功能，请注意！ 
　　sEx请到： http://sourceforge.net/projects/sex下载！ 
　　解压后请将sEx拷贝到/usr/bin目录（其他由$PATH环境变量指定的目录也可以）： 
　　[root@www2 tmp]# cp sEx /usr/bin/　　Linux下常见文件解压方法及命令 
　　系统·System 
　　 
　　1.以.a为扩展名的文件: 
　　#tar xv file.a 
　　2.以.z为扩展名的文件: 
　　#uncompress file.Z 
　　3.以.gz为扩展名的文件: 
　　#gunzip file.gz 
　　4.以.bz2为扩展名的文件: 
　　#bunzip2 file.bz2 
　　5.以.tar.Z为扩展名的文件: 
　　#tar xvZf file.tar.Z 
　　或 #compress -dc file.tar.Z | tar xvf 
　　6.以.tar.gz/.tgz为扩展名的文件: 
　　#tar xvzf file.tar.gz 
　　或 gzip -dc file.tar.gz | tar xvf - 
　　7.以.tar.bz2为扩展名的文件: 
　　#tar xvIf file.tar.bz2 
　　或 bzip2 -dc file.tar.bz2 | xvf - 
　　8.以.cpio.gz/.cgz为扩展名的文件: 
　　#gzip -dc file.cgz | cpio -div 
　　9. 以.cpio/cpio为扩展名的文件: 
　　#cpio -div file.cpio 
　　或cpio -divc file.cpio 
　　10.以.rpm为扩展名的文件安装: 
　　#rpm -i file.rpm 
　　11.以.rpm为扩展名的文件解压缩： 
　　 #rpm2cpio file.rpm | cpio -div 
　　12.以.deb为扩展名的文件安装： 
　　#dpkg -i file.deb 
　　13.以.deb为扩展名的文件解压缩: 
　　#dpkg-deb -fsys-tarfile file.deb | tar xvf - ar p 
　　file.deb data.tar.gz | tar xvzf - 
　　14.以.zip为扩展名的文件: 
　　#unzip file.zip 
　　在linux下解压Winzip格式的文件 
　　要是装了jdk的话，可以用 jar命令；还可以使用unzip命令。 
　　直接解压.tar.gz文件 
　　xxxx.tar.gz文件使用tar带zxvf参数，可以一次解压开。XXXX为文件名。 例如： 
　　$tar zxvf xxxx.tar.gz 各种压缩文件的解压（安装方法） 
　　 
　　文件扩展名 解压（安装方法） 
　　　 
　　.a ar xv file.a 
　　.Z uncompress file.Z 
　　.gz gunzip file.gz 
　　.bz2 bunzip2 file.bz2 
　　.tar.Z tar xvZf file.tar.Z 
　　compress -dc file.tar.Z | tar xvf - 
　　.tar.gz/.tgz tar xvzf file.tar.gz 
　　gzip -dc file.tar.gz | tar xvf - 
　　.tar.bz2 tar xvIf file.tar.bz2 
　　bzip2 -dc file.tar.bz2 | xvf - 
　　.cpio.gz/.cgz gzip -dc file.cgz | cpio -div 
　　.cpio/cpio cpio -div file.cpio 
　　cpio -divc file.cpio 
　　.rpm/install rpm -i file.rpm 
　　.rpm/extract rpm2cpio file.rpm | cpio -div 
　　.deb/install dpkg -i file.deb 
　　.deb/exrtact dpkg-deb -fsys-tarfile file.deb | tar xvf - 
　　ar p file.deb data.tar.gz | tar xvzf - 
　　.zip unzip file.zip 
　　 
　　bzip2 -d myfile.tar.bz2 | tar xvf 

　　tar xvfz myfile.tar.bz2 
　　 
　　x 是解压 
　　v 是复杂输出 
　　f 是指定文件 
　　z gz格式 

```

**gzip**

```
gzip 
　　gzip[选项]要压缩（或解压缩）的文件名 
　　-c将输出写到标准输出上，并保留原有文件。 
　　-d将压缩文件压缩。 
　　-l对每个压缩文件，显示下列字段：压缩文件的大小，未压缩文件的大小、压缩比、未压缩文件的名字 
　　-r递归式地查找指定目录并压缩或压缩其中的所有文件。 
　　-t测试压缩文件是正完整。 
　　-v对每一个压缩和解压缩的文件，显示其文件名和压缩比。 
　　-num-用指定的数字调整压缩的速度。 
　　举例： 
　　把/usr目录并包括它的子目录在内的全部文件做一备份，备份文件名为usr.tar 
　　tar cvf usr.tar /home 
　　把/usr 目录并包括它的子目录在内的全部文件做一备份并进行压缩，备份文件名是usr.tar.gz 
　　tar czvf usr.tar.gz /usr 
　　压缩一组文件，文件的后缀为tar.gz 
　　#tar cvf back.tar /back/ 
　　#gzip -q back.tar 
　　or 
　　#tar cvfz back.tar.gz /back/ 
　　释放一个后缀为tar.gz 的文件。 
　　#tar zxvf back.tar.gz 
　　#gzip back.tar.gz 
　　#tar xvf back.tar

```

### 重置centos 密码

>  
 重置Centos 7 Root密码的方式和Centos 6完全不同。让我来展示一下到底如何操作。 在启动grub菜单，选择编辑选项启动 


<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcubGludXgubmV0LmNuL2RhdGEvYXR0YWNobWVudC9hbGJ1bS8yMDE0MTAvMDcvMDAwOTU0ejd2MmR0N3V2MnoycmwzdS5wbmc?x-oss-process=image/format,png" alt="在这里插入图片描述">

>  
 按键盘e键，来进入编辑界面 


<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcubGludXgubmV0LmNuL2RhdGEvYXR0YWNobWVudC9hbGJ1bS8yMDE0MTAvMDcvMDAwOTU1emFqYThyYWthMGFxOWZyZC5wbmc?x-oss-process=image/format,png" alt="在这里插入图片描述">

>  
 找到Linux 16的那一行，将ro改为rw init=/sysroot/bin/sh 


<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcubGludXgubmV0LmNuL2RhdGEvYXR0YWNobWVudC9hbGJ1bS8yMDE0MTAvMDcvMDAwOTU2eGc0bGJyNTdkbDVnaWxiZy5wbmc?x-oss-process=image/format,png" alt="在这里插入图片描述">

>  
 现在按下 Control+x ，使用单用户模式启动 


<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcubGludXgubmV0LmNuL2RhdGEvYXR0YWNobWVudC9hbGJ1bS8yMDE0MTAvMDcvMDAwOTU4aGxiZzVvN3NzNzY1OTVqcy5wbmc?x-oss-process=image/format,png" alt="在这里插入图片描述">

>  
 现在，可以使用下面的命令访问系统 


```
chroot /sysroot

```

>  
 重置密码 


```
passwd root

```

>  
 更新系统信息 


```
touch /.autorelabel

```

>  
 退出chroot 


```
exit

```

>  
 重启你的系统 


```
reboot

```

### SSH服务器拒绝了密码，请再试一次，亲测有效

**一、常规方法：**

```
应该是sshd的设置不允许root用户用密码远程登录
 
1、修改 vim /etc/ssh/sshd_config
 
找到# Authentication:
LoginGraceTime 120
PermitRootLogin without passwd
StrictModes yes
 
改成
 
# Authentication:
LoginGraceTime 120
PermitRootLogin yes
StrictModes yes
2、重启ssh
systemctl restart sshd

```

**二、暴力一点，重启服务器试试** **三、如果尝试过N种方法还是不行则进行如下操作**

```
1、修改 vim /etc/sshd/sshd_config
找到
UsePAM yes
改为
UsePAM no
 
2、重启ssh
systemctl restart sshd

```

### Centos7_linux分区满了，如何进行扩容



### centos添加用户并赋予 root管理员权限

**新建用户，这里新建一个 summer 的用户**

```
adduser summer

```

**设置新用户密码**

```
passwd summer

```

**将sudoers文件的权限修改成可编辑**

```
chmod -v u+w /etc/sudoers

```

**使用vim编辑sudoers文件**

```
vim /etc/sudoers

```

**在sudoes文件中添加如下的内容**

```
root       ALL=(ALL)           ALL

summer     ALL=(ALL)       ALL

```

如需新用户使用sudo时不用输密码，把最后一个ALL改为NOPASSWD:ALL即可。

**将sudoers文件的权限修改成不可编辑**

```
chmod -v u-w /etc/sudoers

```

**修改 /etc/passwd 文件，找到如下行，把用户ID修改为 0 ，如下所示**

```
tommy:x:500:500:tommy:/home/tommy:/bin/bash

```

保存，用tommy账户登录后，直接获取的就是root帐号的权限。

### 配置java环境

**首先下载linux下的安装包 ** <img src="https://img-blog.csdnimg.cn/20201122142436636.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> 下载并解压到自己定义的目录

>  
 配置jdk1.8的环境 


```
sudo vim /etc/profile

```

在末尾添加以下几行文字：

```
#set java env
export JAVA_HOME=/usr/lib/jdk/jdk1.8.0_202
export JRE_HOME=${<!-- -->JAVA_HOME}/jre    
export CLASSPATH=.:${<!-- -->JAVA_HOME}/lib:${<!-- -->JRE_HOME}/lib    
export PATH=${<!-- -->JAVA_HOME}/bin:$PATH

```

执行命令使修改立即生效

```
source /etc/profile

```

>  
 配置软连接(也可以不配置) 软连接相当于windows系统中的快捷键，部分软件可能会从/usr/bin目录下查找Java，因此添加该软连接防止其他软件查找不到的情况。 


```
sudo update-alternatives --install /usr/bin/java  java  /usr/lib/jdk/jdk1.8.0_202/bin/java 300   
sudo update-alternatives --install /usr/bin/javac  javac  /usr/lib/jdk/jdk1.8.0_202/bin/javac 300 

```

### 防火墙相关操作

```
systemctl status firewalld 	 # 查看防火墙状态
systemctl start firewalld	 # 开启防火墙
systemctl stop firewalld 	 # 关闭防火墙
systemctl disable firewalld.service 禁用防火墙

//开启 80 443 端口
firewall-cmd --zone=public --add-port=80/tcp --permanent
firewall-cmd --zone=public --add-port=443/tcp --permanent

//重启防火墙
systemctl restart firewalld

```

### 系统时间不对，校对方法

```
centos系统有时候时间是不同步的，但是只要我们是在国内下载，一般时区是亚洲/上海的，所以我们只要做这一步就行了

1.使用yum 安装ntpdate


yum install -y ntpdate
2.然后ntpdate us.pool.ntp.org

再date一下


时间就同步了


如果你的时区不是上海的，那么就复制过去吧

cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
然后进行1-2步

```
