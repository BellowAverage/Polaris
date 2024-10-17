
--- 
title:  redis搭建教程linux 
tags: []
categories: [] 

---
Linux 安装redis

服务器：linux centOS6.6

一、redis安装

1. 安装gcc依赖 。由于redis是用C语言编写的，所以必需要先安装gcc依赖。

yum -y install gcc

2. 下载redis安装包

redis版本查看，这里选择的是redis5.0.7

这里我们把redis安装在 /usr/local 目录下，所以先进入到这个目录下将安装包下载下来

>  
 cd /usr/local 


>  
 wget http://download.redis.io/releases/redis-5.0.7.tar.gz 


解压文件

>  
 tar -zxvf redis-5.0.7.tar.gz 


3.编译、安装redis

a. 先进入刚刚解压的redis文件

>  
 cd redis-5.0.7 


b. 编译

>  
 make 


c. 安装。PREFIX指定安装目录为/usr/local/redis，目录不存在时会自动创建目录

>  
 make install PREFIX=/usr/local/redis install 


<img alt="" height="150" src="https://img-blog.csdnimg.cn/30c96522c7da4e499feac6079958f449.png" width="641">

进入到redis的安装目录下

>  
 cd /usr/local/redis/bin 


可以看到以下几个文件<img alt="" height="128" src="https://img-blog.csdnimg.cn/14d5db75161949c88b3e760bd075ba2d.png" width="580">

redis-benchmark 本地环境的性能测试工具

reids-check-aof 修复有问题的AOF文件

redis-check-rdb 修复有问题的rdb文件

redis-sentinel redis哨兵模式

redis-cli 客户端入口

redis-server  服务启动命令 



d. 复制redis配置文件到安装目录

>  
 cp redis.conf /usr/local/redis 


4.编辑redis.conf 配置

a. 进入redis的安装目录

>  
 cd /usr/local/redis/ 


c. 编辑配置

>  
 vim redis.conf 


1). daemonize 后台启动设置修改为 yes 默认为no

2). port 绑定端口 默认端口为6379，可以使用默认端口。服务器的安全组需开放此端口。

3). dir 设置数据存放的路径 dir /usr/local/redis/log 如果目录不存在需要先创建目录，否则启动会失败。

4). 指定持久化方式，appendonly yes

5). requirepass XXXXX 设置密码

6).bind 绑定IP 注意这里有一个坑。这里是指绑定本机访问的网卡IP并不是外网访问的IP. 所以这里配置成 0.0.0.0

5.启动redis

执行redis-server 使用redis.conf这里的配置

>  
 /usr/local/redis/bin/redis-server /usr/local/redis/redis.conf 


6.查看redis是否成功

>  
 ps -aux | grep redis 


如果有redis的进程则启动成功

7. 打开redis-cli客户端

>  
 /usr/local/redis/bin/redis-cli --raw （--raw 处理中文乱码） 


8. 测试连接

        /usr/local/redis/bin/redis-cli进入到客户端

        auth [第4步中设置的密码内容]

          <img alt="" height="79" src="https://img-blog.csdnimg.cn/6afe60cb0c8d48358d88d0086ec44c63.png" width="395">

        ping  出现 PONG则表示连接成功

9. 重启redis

先杀死redis进程再重新开启

>  
 pkill redis 
 /usr/local/redis/bin/redis-server /user/local/redis/redis.conf 


二、添加环境变量

vim ~/.bash_profile                # .bash_profile是隐藏文件, 在该文件中自定义环境变量

　　以下两行为.bash_profile最后两行内容: 

　　PATH=$PATH:$HOME/bin: /usr/local/redis          # 添加redis目录路径到这里

　　export PATH

　　:wq                                                                    # 编辑完成保存退出

　　source ~/.bash_profile                                        # 使配置的环境变量立即生效

　　至此, 即可在任何位置使用redis-server和redis-cli命令来操作redis了

　　如果需要指定配置文件启动则切换到redis.conf文件所在目录去执行

三、防火墙的设置

这里是针对CentOS 6的设置 centOS 7的命令是不一样的

1. iptables -I INPUT -p tcp --dport 6379 -j DROP //先关闭所有6379的访问权限

2. iptables -I INPUT -s 127.0.0.1 -p tcp --dport 6379 -j ACCEPT //指定本机访问

3. iptables -I INPUT -s 110.110.110.110 -p tcp --dport 6379 -j ACCEPT //指定IP为 110.110.110.110可以访问

4. service iptables save //保存IPtables设置

5. service iptables restart //重启防火墙

四、总结

我们原本是想要限制IP访问，之前一直理解为在redis.conf配置里设置bind IP。后来才发现并不是这样的，bind只是针对绑定本机的网卡IP，也就是说，我们的主机可能会有多个网卡，那么就会有多个网卡IP,那么这里设置的只是指定本机的哪个网卡IP可以访问。

如果需要限制外部IP的访问，只能是通过端口的访问做限制，在防火墙里设置只允许哪些IP可以访问该端口就行。
