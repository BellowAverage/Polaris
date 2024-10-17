
--- 
title:  nginx - 负载均衡配置-负载均衡策略 
tags: []
categories: [] 

---
**目录**



















































### 知识点1：网站流量分析指标

#### 什么是pv？

>  
 **PV（page view），即页面浏览量，通常是衡量一个网络新闻频道或网站的主要指标** 


#### 什么是uv？

>  
 **UV（unique visitor），指的是访问某个站点或点击某个网站的不同ip地址的人数** 
 **在同一天内，uv只记录第一次进入网站的具有独立IP的访问者，在同一天内再次访问该网站则不计数** 


#### 什么是IP？

>  
 **IP表示拥有特定唯一IP地址的计算机访问您的网站的次数，** 


** ###########################################################################################**

### 知识点2：正向代理和反向代理

>  
 **正向代理：** 
 **        代理的对象为客户** 
 **        代理清楚知道客户要访问的目标** 


>  
 **反向代理：** 
 **        代理的对象为服务器** 
 **        代理不知道客户要访问的目标** 


 <img alt="" height="276" src="https://img-blog.csdnimg.cn/ab7c16a1faa6422e8138ed64c7b71ba1.png" width="992"> 

 ** ###########################################################################################**

### 知识点3：负载均衡实验

#### 什么是负载均衡？

>  
 **负载均衡就是将用户的访问请求，平均的分配给后端服务器** 


#### IP地址规划：

>  
 **load balance 负载均衡服务器：192.168.44.132** 
 **web1 真实web服务器 ：192.168.44.166** 
 **web2 真实web服务器：192.168.44.141** 
 **web3 真实web服务器：192.168.44.205** 


#### 实验拓扑图

<img alt="" height="420" src="https://img-blog.csdnimg.cn/f853f20506ec40bd9393df41f3c8b29c.png" width="1049">

** 首先在web1，web2，web3，三台web服务器安装nginx软件，使用一键安装nginx脚本安装**

**一键安装nginx脚本：**

```
[root@web1 ~]# cat onekey_install_nginx.sh 

#!/bin/bash
 
#解决软件的依赖关系，需要安装的软件包
yum install epel-release -y
yum -y install zlib zlib-devel openssl openssl-devel pcre pcre-devel gcc gcc-c++ autoconf automake make psmisc net-tools lsof vim geoip geoip-devel wget -y
 
#新建liming用户和组
id  liming || useradd liming -s /sbin/nologin
 
#下载nginx软件
mkdir  /liming99 -p
cd /liming99
wget  https://nginx.org/download/nginx-1.21.6.tar.gz
 
#解压软件
tar xf nginx-1.21.6.tar.gz 
#进入解压后的文件夹
cd nginx-1.21.6
 
#编译前的配置
./configure --prefix=/usr/local/scliming99  --user=liming --group=liming  --with-http_ssl_module   --with-threads  --with-http_v2_module  --with-http_stub_status_module  --with-stream  --with-http_geoip_module --with-http_gunzip_module
 
#如果上面的编译前的配置失败，直接退出脚本
if (( $? != 0));then
	exit
fi
#编译
make -j 2
#编译安装
make  install
 
#修改PATH变量
echo  "PATH=$PATH:/usr/local/scliming99/sbin" &gt;&gt;/root/.bashrc
#执行修改了环境变量的脚本
source /root/.bashrc
 
 
#firewalld and selinux
 
#stop firewall和设置下次开机不启动firewalld
service firewalld stop
systemctl disable firewalld
 
#临时停止selinux和永久停止selinux
setenforce 0
sed  -i '/^SELINUX=/ s/enforcing/disabled/' /etc/selinux/config
 
#开机启动
chmod +x /etc/rc.d/rc.local
echo  "/usr/local/scliming99/sbin/nginx" &gt;&gt;/etc/rc.local
 
#修改nginx.conf的配置，例如：端口号，worker进程数，线程数，服务域名
 
sed  -i '/worker_processes/ s/1/2/' /usr/local/scliming99/conf/nginx.conf
sed  -i  '/worker_connections/ s/1024/2048/' /usr/local/scliming99/conf/nginx.conf
sed  -i -r '36c \\tlisten  80;' /usr/local/scliming99/conf/nginx.conf
sed  -i -r '37c \\tserver_name www.liming.com;' /usr/local/scliming99/conf/nginx.conf
 
#killall nginx进程
killall -9 nginx
 
#启动nginx
/usr/local/scliming99/sbin/nginx


```

**修改web服务首页index.html**

```
[root@web1 html]# cat index.html
this is nginx-web1  192.168.44.166

```

```
[root@web2 html]# cat index.html 
this is nginx-web2  192.168.44.141

```

```
[root@web3 html]# cat index.html 
this is nginx-web3  192.168.44.205

```

**修改load balance 负载均衡服务器nginx的配置文件nginx.conf**

**在http块里面定义一个负载均衡器，然后创建一个路由规则，使用创建的upstream节点**

```
    # 定义上游服务器集群，定义一个负载均衡器
    upstream myweb1{
        server 192.168.44.166;
        server 192.168.44.141;
        server 192.168.44.205;

    }

    server {
        listen       80;
        location / {
            # 使用myweb1分配规则，即刚才定义的upstream节点
            proxy_pass http://myweb1;

```

>  
  **修改完配置文件以后刷新一下nginx服务，然后再访问****load balance****服务器就会将流量采用****轮询****的方式分发到三台真实web服务器上面** 


<img alt="" height="221" src="https://img-blog.csdnimg.cn/4775c89a4bff41c49d4d048d31056a55.png" width="1193">

<img alt="" height="177" src="https://img-blog.csdnimg.cn/594b989719c54a1681b1312ebf571d2b.png" width="1198">

<img alt="" height="177" src="https://img-blog.csdnimg.cn/26d5aafd60ea4c409f06ec385d1b0101.png" width="1200">

**############################################################################################**

### 知识点4：负载均衡策略

#### 1、请求轮询

>  
 **依次转发给配置的服务器，即上个实验，默认是以轮询的方式来分发流量访问** 


#### 2、增加权重

>  
 **使用服务器权重，还可以进一步影响ngixn负载均衡算法，谁的权重越大，分发到的请求就越多** 


>  
 **修改负载均衡服务器配置文件** 


```
    # 定义上游服务器集群，定义一个负载均衡器
    upstream myweb1{
        server 192.168.44.166 weight=3;
        server 192.168.44.141 weight=1;
        server 192.168.44.205 weight=1;

    }

    server {
        listen       80;
        location / {
            # 使用myweb1分配规则，即刚才定义的upstream节点
            proxy_pass http://myweb1;

    }

```

>  
 ** 接下来访问负载均衡服务器，它会根据权重的多少来分发流量，权重越大，分发到的请求就越多** 


<img alt="" height="181" src="https://img-blog.csdnimg.cn/41e1c7f55e37450290376b7a689c4e4e.png" width="1194">

<img alt="" height="178" src="https://img-blog.csdnimg.cn/5bd3b641d93a4e418c22f03f5b6c274d.png" width="1200">

<img alt="" height="176" src="https://img-blog.csdnimg.cn/ce108ca3da11444da0f65357e7985187.png" width="1198">

<img alt="" height="176" src="https://img-blog.csdnimg.cn/c075de1a743e47f1a67476a5fed61608.png" width="1193">

<img alt="" height="185" src="https://img-blog.csdnimg.cn/5541867860b546278d90a63058a47897.png" width="1192">

 **############################################################################################**

####  3、最少连接数

>  
 **在连接负载最少的情况下，nginx会尽量避免过多的请求分发给繁忙的应用程序服务器，而是将新请求分发给不太繁忙的服务器，避免服务器过载** 
 **轮询法不能识别在给定的时间里保持了多少连接，因此可能发生，服务器B服务器收到的连接比服务器A少但是它已经超载，比如B服务器虽然收到的连接数少，但是都保持连接，没有断开，A服务器虽然收到的连接数多，但是实际大都断开连接，这时候就需要优先选择活跃连接数最少的服务器** 




```
    # 定义上游服务器集群，定义一个负载均衡器
    upstream myweb1{
        least_conn;
        server 192.168.44.166;
        server 192.168.44.141;
        server 192.168.44.205;

    }

    server {
        listen       80;
        location / {
            # 使用myweb1分配规则，即刚才定义的upstream节点
            proxy_pass http://myweb1;

    }

```

 **############################################################################################**

#### 4、ip_hash 策略 

>  
 **每个请求按访问的ip分配hash，即一个客户端第一次请求nginx后，会分配到hash，下次改客户端请求 ##的结果还是一样的，不会改变，解决session问题。** 


```
    # 定义上游服务器集群，定义一个负载均衡器
    upstream myweb1{
        ip_hash;
        server 192.168.44.166;
        server 192.168.44.141;
        server 192.168.44.205;

    }

    server {
        listen       80;
        location / {
            # 使用myweb1分配规则，即刚才定义的upstream节点
            proxy_pass http://myweb1;

    }

```

 **############################################################################################**

### 知识点5：获取访问机器的真实ip地址

>  
 **当我们使用负载均衡服务器来分发流量以后，在真实web服务器上的访问日志是谁的ip？负载均衡服务器的还是真实访问ip的？** 
 **可以看到，web1机器上nginx的访问日志是负载均衡服务器的ip地址，那么如何让web服务器知道真实访问机器的IP地址？ ** 


<img alt="" height="175" src="https://img-blog.csdnimg.cn/4447f394046248ffbb0ffbdaedac543a.png" width="1200">

让web服务器日志显示真实访问机器的IP

#### 1、在负载均衡器上修改http请求报文头部字段，谈价一个X_Real-IP字段

>  
 **将nginx内部的remote_addr 这个变量的值，赋值给X_Real-IP这个变量，X_Real-IP这个变量会在http协议的请求报文里面添加一个X_Real-IP的字段，后端的real server服务器上的nginx就可以读取这个字段的值** 


```
    server {
        listen       80;
        location / {
            # 使用myweb1分配规则，即刚才定义的upstream节点
            proxy_pass http://myweb1;
            proxy_set_header X-Real-IP $remote_addr;

    }

```

#### 2、修改web服务器的nginx配置文件，在日志格式里面添加http_x_real_ip字段

```
    log_format  main  '$remote_addr - $http_x_real_ip  $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

```

修改配置文件以后重新启动服务

```
[root@web1 conf]# nginx -t
nginx: the configuration file /usr/local/scliming99/conf/nginx.conf syntax is ok
nginx: configuration file /usr/local/scliming99/conf/nginx.conf test is successful
[root@web1 conf]# nginx -s reload

```

测试访问负载均衡服务器后查看日志文件

<img alt="" height="711" src="https://img-blog.csdnimg.cn/eabe80bb1fd7446687a93728c3e2e1bf.png" width="1200"> 

  **############################################################################################**

###  知识点6：nginx的四层负载均衡和七层负载均衡

#### 七层负载均衡：

>  
 **七层负载均衡主要工作在网络七层ISO协议的第七层，即应用层。由于在应用层主要是处理对应的应用层协议的相关数据，如HTTP协议，而无法操作传输层TCP连接相关细节，故在七层负载均衡当中，负载均衡器主要是基于应用层协议的相关数据来进行请求转发，** 


#### 四层负载均衡 

>  
 **所谓四层就是基于IP+端口的负载均衡，它通过用户请求的端口来决定将请求转发至哪台后端服务器。就是通过第三层（网络层）的IP地址并加上四层（传输层）的端口号，来决定哪些流量需要做负载均衡。对需要负载均衡的流量进行NAT转换，然后转发至后端服务器节点，并记录这个TCP或者UDP的流量是由哪台后端服务器处理的，后续这个连接的所有流量都同样转发到同一台服务器处理。** 


#### nginx四层负载均衡和七层负载均衡的区别

>  
 **七层负载均衡是工作在第七层，只能给web应用，使用http协议的** 
 **四层负载均衡是根据端口进行转发的，支持的服务数量比七层多** 
 **四层负载均衡数据包是在底层就进行了分发，而七层负载均衡数据包则在最顶端进行分发，所以四层负载均衡的效率比七层负载均衡的要高。 四层负载均衡不识别域名，而七层负载均衡识别域名。** 


   **############################################################################################**

### 知识点7：lvs负载均衡和nginx负载均衡的区别

#### 层数的区别

>  
 **lvs只支持四层负载均衡** 
 **nginx支持四层和七层负载均衡** 


#### 效率的区别

>  
 **lvs的效率更高，lvs已经在内核里内置了，不需要安装，数据通过网卡解封装后，经过kernel space，然后lvs直接调用** 
 **nginx工作在user space，nginx需要等内核将数据处理以后送到user space，然后nginx再处理，所以lvs比nginx工作少一层，lvs效率较高** 


<img alt="" height="597" src="https://img-blog.csdnimg.cn/f553b639bd224cb8a0ccff05c7524560.png" width="695"> 

 

**############################################################################################**





 
