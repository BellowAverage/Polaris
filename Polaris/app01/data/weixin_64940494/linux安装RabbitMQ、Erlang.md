
--- 
title:  linux安装RabbitMQ、Erlang 
tags: []
categories: [] 

---
        首先可以进入rabbitMQ官网上查看  。

<img alt="" src="https://img-blog.csdnimg.cn/1d6fa6311d194b00b50ecc07af752389.png">

        当前RabbitMQ的最新版本是3.10.7，要求Erlang版本最低是24.0，最高是25.0。我们选择安装最新版RabbitMQ也就是3.10.7。 

** 一、 下载安装Erlang**

1.  进入到Erlang官网下载  。复制链接地址。

<img alt="" height="393" src="https://img-blog.csdnimg.cn/b133158600644d24ac1eb3fa3284d005.png" width="630">

 这里我下载的目录时 /usr/local/rabbitmq，进入到该目录下下载安装包

>  
 cd /usr/local/rabbitmq    
 wget   


2. 解压安装包

>  
 tar -xvzf otp_src_25.0.tar.gz 


3. 安装erlang需要的依赖

>  
  yum -y install make gcc gcc-c++ kernel-devel m4 ncurses-devel openssl-devel unixODBC-devel   


4. 安装erlang的环境配置

        在erlang的下载目录下新建一个erlang文件目录，这里我的目录是/usr/local/rabbitmq/erlang

        进入解压后的erlang文件目录下执行安装命令

>  
 mkdir /usr/local/rabbitmq/erlang 
 cd /usr/local/rabbitmq/otp_src_25.0 
 ./configure --prefix=/usr/local/erlang --without-javac 


<img alt="" height="45" src="https://img-blog.csdnimg.cn/0f1ecccccf694444a535ce079b8cbf89.png" width="753">

 5. 编译并安装erlang

>  
        make &amp;&amp; make install 


6. 配置erlang环境变量

>  
        vim /etc/profile 


        在最后添加以下配置

>  
 #erlang 
 PATH=$PATH:/usr/local/rabbitmq/erlang/bin 


        执行以下命令将环境变量生效

>  
 source /etc/profile 


7. 验证erlang

        输入erl命令查看是否安装成功

<img alt="" height="83" src="https://img-blog.csdnimg.cn/5be79d154de84807b3effca56a16ac26.png" width="639">

** 二、安装RabbitMQ**

1. 进入到RabbitMQ官方GitHub上下载安装包， 。下载目录还是在/usr/local/rabbitmq

>  
 wget https://github.com/rabbitmq/rabbitmq-server/releases/download/v3.10.7/rabbitmq-server-generic-unix-3.10.7.tar.xz 


2. 解压安装包，如果 xz 和 tar解压工具未安装可以使用yum install xz 安装

>  
 xz -d rabbitmq-server-generic-unix-3.10.7.tar.xz 
 tar -xvf rabbitmq-server-generic-unix-3.10.7.tar 


3. 添加环境变量

>  
 PATH=$PATH:/usr/local/rabbitmq/rabbitmq_server-3.10.7/sbin 


执行以下命令将环境变量生效

>  
 source /etc/profile 


4. 进入到解压后的rabbitmq目录中，执行以下命令安装rabbitmq管理界面。

>  
 rabbitmq-plugins enable rabbitmq_management 


5. 开启rabbitmq服务

>  
 rabbitmq-server -detached  //使用后台守护进程开启 


6. 通过访问 IP地址:15672 进入到rabbitmq管理后台，15672端口需要先开启。

<img alt="" height="280" src="https://img-blog.csdnimg.cn/f07b04ed8ba449e4a42839d7390c8d69.png" width="590">



 出现该页面就证明rabbitmq已经安装完成。

7. 登录管理后台

       rabbitmq 安装完后默认会guest这个用户，但是这个用户只允许在本地登录，所以用 IP地址:15672访问登录时时出现"User can only log in via localhost"提示。<img alt="" height="263" src="https://img-blog.csdnimg.cn/8039ab0a2d2f4f3ebb491e5b83cd6638.png" width="572">

        解决方案可以新增一个新的用户并授予管理员角色去登录，这里我们创建一个 admin 123456

>  
 rabbitmqctl add_user admin 123456 rabbitmqctl set_user_tags admin administrator 


         这样就可以用admin 登录了，还有一种方式就是去修改rabbitmq配置文件,我们通过下载安装包的方式安装的是没有配置文件，需要自己创建配置文件并添加配置项，具体配置项参考官网介绍这里就不多介绍了。
