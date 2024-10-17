
--- 
title:  ubuntu各种常用命令，个人常用收录 
tags: []
categories: [] 

---
```
cd /     回到根目录   
cd /文件目录
du -sh 文件名 
cat /proc/cpuinfo 查看CPU信息
free -m 查看内存和swap分区
du -sh * 查看当前目录下的文件大小
lscpu (查看cpu信息)
df -h 查看硬盘分区信息）
top 动态查看cpu、内存使用情况的信息
cat /etc/issue 查看当前linux系统的版本

编辑模式
　　使用vi进入文本后，按i开始编辑文本

退出编辑模式 
　　按ESC键，然后：
　　　　退出vi
　　　:q!  不保存文件，强制退出vi命令
　　　 :w   保存文件，不退出vi命令
　　　 :wq  保存文件，退出vi命令

du -sh 当前文件或文件夹大小
   df -lh  查看磁盘各文件夹使用情况和df -h效果一样
df -h选项，通过它可以产生可读的格式df命令的输出：

find / -name "filename"   知道文件名，但是不知道存放路径，可以使用这个命令，进行查询

1.shutdown -h now马上关机

这句命令的意思是立即关机，此外，通过改变now的参数值还可以设置定时关机。如：shutdown -h 5 这句命令的意思是5分钟以后关机，我们还能规定关机的时间，如：shutdown -h 17:00下午17点下班后马上关机。

2.shutdown -r now马上重启

这句命令的意思是执行完这句命令，系统会马上进行重启。

3.reboot重启

从字面意思就可以得知，这是重启命令，这句话的意思等同于shutdown -h now。

4.halt关机

这句命令的字面意思也是关机，它等同于2中的shutdown -h now。

```

## df -h

```
Filesystem      Size  Used   Avail Use% Mounted on 
/dev/sda6       29G   4.2G   23G   16%     / 
udev            1.5G  4.0K   1.5G   1%     /dev 
tmpfs           604M  892K   603M   1%     /run 
none            5.0M     0   5.0M   0%     /run/lock 
none            1.5G  156K   1.5G   1%     /run/shm 

```

###### 我们可以看到输出显示的数字形式的’G’（千兆字节），“M”（兆字节）和"K"（千字节）。

这使输出容易阅读和理解，从而使显示可读的。请注意，第二列的名称也发生了变化，为了使显示可读的"大小"。

```
~# 解压xxx.zip里面的yyy文件到dir目录
~# unzip xxx.zip yyy -d dir
~# 如果解压的是tar.gz文件
~# tar -zxvf 文件名 -C 指定目录
~# 如果解压的是rar文件
~# rar x 文件名      《--这样解压的话，dir1就会保持原来的目录结构

```

###### 由于需要经常查看各个文件的具体大小 ，所以这里记一下。

命令如下：

```
du -h --max-depth=1

```

##### 修改Opt文件权限为全权限

```
chmod 777 -R Opt 

```

## ubuntu账户创建

###### 在非默认磁盘目录创建账户hdpaii152

```
useradd -r /disk2（挂载的磁盘，非默认）/hdpaii152 -m hdpaii152 -s /bin/bash
passwd hdpaii152  创建密码  

```

###### 在默认磁盘目录下创建账户hdpaii152

```
useradd -r -m -s  /bin/bash  hdpaii152
passwd hdpaii152  创建密码
输入ls  /home/，可以看到用户目录被成功创建了：

```

###### 切换用户的命令为：su username

从普通用户切换到root用户，还可以使用命令：sudo su

###### 腾讯云服务器设置root账户登录

1、先用ubuntu账号登录，执行sudo passwd root

2、按要求输入密码，请牢记。

3、执行sudo vi /etc/ssh/sshd_config

4、找到PermitRootLogin without-password这一行，把后面的without-password改为yes，取消注释，保存文件。

5、执行sudo service ssh restart

现在就可以用root账号登录了。

###### 在终端输入exit或logout或使用快捷方式ctrl+d，可以退回到原来用户，其实ctrl+d也是执行的exit命令

在切换用户时，如果想在切换用户之后使用新用户的工作环境，可以在su和username之间加-，例如：【su - root】

su切换到超级用户；（root账户下不需要） useradd -r /disk/username -m username -s /bin/bash -r指定用户主目录路径 -m如果路径不存在，将自动创建 -s指定默认shell，不然出了错误有可能要在/etc/passwd再修改。。。 然后passwd username即可。

###### 修改文件或文件夹名

```
mv file1 file2 

```

把当前目录下的file1文件名改成file2，如果该目录下有file2，则覆盖以前的file2文件。

错误信息如下:

```
/usr/bin/xauth: file /home/user/.Xauthority does not exist

```

错误原因: 是因为添加用户时没有授权对应的目录，仅仅执行了useradd user而没有授权对应的家目录 直接解决办法如下(执行如下命令，以后就登录到终端上就不会出现上面的错误信息):

```
chown username:username -R /home/user_dir

```

网上也用说 使用以下命令即可：

```
rm -rf .Xauthority-*

```

不过一般是可以避免这种情况的出现，添加用户执行如下命令即可:

```
useradd username -m (-m 相当于会创建对应的用户家目录)

usermod -s /bin/bash username (指定shell，否则会非常不便于终端操作)

```

### 查看当前谁在登陆服务器

###### 1.w 命令

<img src="https://img-blog.csdnimg.cn/31a87aca0e2d4959b811102c400a9d12.png" alt="在这里插入图片描述">

###### 2.who 命令

<img src="https://img-blog.csdnimg.cn/70abdfdeda934313ac8f7592c30a417c.png" alt="在这里插入图片描述">

###### 3.who am i 命令 显示当前用户信息

<img src="https://img-blog.csdnimg.cn/795701dd7038455a97b7f31f00c72f72.png" alt="在这里插入图片描述">

###### 4.有时候 我需要把其他人给清理下去。例如维护时

```
root@hdpaii-ecs:~# pkill  -kill -t pts/1

```

###### 5.踢人之前是否需要跟人家通话一下。免得误会，使用w命令 我们可以看到当前有2个终端在服务器上，使用tty命令查看自己的tty信息

<img src="https://img-blog.csdnimg.cn/d2bd003182a54901a255cf214ee25cca.png" alt="在这里插入图片描述">

###### 6.可以使用echo命令和对方通话

```
root@hdpaii-ecs:~# echo "系统维护，请下线 " &gt; /dev/pts/2

```

###### 对方显示

<img src="https://img-blog.csdnimg.cn/1a4b82f247d64cada3493df648fb50db.png" alt="在这里插入图片描述">

或者使用write 命令也可 <img src="https://img-blog.csdnimg.cn/eeaf3a9d9b3b44f4b9da6672674a0093.png" alt="在这里插入图片描述"> 接下来就是将讯息打上去，结束请按 ctrl+c
