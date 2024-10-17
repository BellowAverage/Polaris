
--- 
title:  Docker consul--容器服务更新与发现 
tags: []
categories: [] 

---
## Docker consul–容器服务更新与发现



#### 文章目录
- - <ul><li>- <ul><li><ul><li>- <ul><li>- - - - - 


### 1、consul简介

consul是HashiCorp公司推出使用  编写的开源工具，用于实现分布式系统的服务发现与配置。
- consul支持健康检查，允许存储键值对- 一致性协议采用Raft算法，用来保证服务的高可用- 成员管理和消息广播采用GOSSIP协议，支持ACL访问控制- 方便部署，与Docker等轻量级容器可无缝配合
##### docker consul 服务更新与发现的服务架构

<img src="https://img-blog.csdnimg.cn/72b7d42193934b68827cf835aa294a24.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/827d0ab284dd4aebbd9315c5278ef4e5.png#pic_center" alt="在这里插入图片描述">

上方拓扑图是基于Docker完成的，然后将consul、consul template、registrator和nginx组装成一个值得信任且可扩展的服务框架，此架构可以灵活的、不需要重启任何服务、不需要重写任何配置的添加和移除服务；

当后方增加了一个容器时，容器会注册registrator，registrator发现增加了一个容器的时候，会通知consul server要更新，consul server使用consul template模板更新。

**这里我们主要注意三个模块：**
- consul template： 配置文件模板- registrator： 自动发现与注册机制- consul server：consul服务
**Docker consul自动发现服务架构的构建**
- 每个提供服务的节点上都要部署和运行consul的agent- consul agent有两种运行模式：server和client- server和client只是consul集群层面的区分，与搭建在cluster之上的应用服务无关
### 2、实验部署

|consul|192.168.111.40|Docker-ce,consul,consul-template,nginx
|------
|web|192.168.111.10|dokcer-ce,registrator

**consul节点**

```
mkdir /root/consul
cd /root/consul
#拉取consul包
unzip consul_0.9.2_linux_amd64.zip
[root@docker consul]#ls
consul  consul_0.9.2_linux_amd64.zip
mv consul /usr/bin/

consul agent \   #设置代理
-server \      #开启服务功能
-bootstrap \   #参与选举
-ui \          #提供UI界面
-data-dir=/var/lib/consul-data \    #提供代理存储数据目录
-bind=192.168.111.40 \   #绑定本机IP
-client=0.0.0.0 \    #客户端地址（所有网段）
-node=consul-server01 &amp;&gt; /var/log/consul.log &amp;    #定义节点日志

```

<img src="https://img-blog.csdnimg.cn/e49b546ab1c74036a8bb6ebd4b1c7cef.png#pic_center" alt="在这里插入图片描述">

```
#查看集群信息
consul members
consul info | grep leader   #查看管理信息

```

<img src="https://img-blog.csdnimg.cn/c859b952c9e344b39579688c830adafa.png#pic_center" alt="在这里插入图片描述">

访问：192.168.111.40:8500

<img src="https://img-blog.csdnimg.cn/09da6ae5420b4fc2a2ec643a42777bbb.png#pic_center" alt="在这里插入图片描述">

##### 容器服务自动加入consul 集群（web节点）

安装Gliderlabs/Registrator：

Gliderlabs/Registrator可检查容器运行状态自动注册，还可注销docker容器的服务到服务配置中心。目前支持Consul、Etcd和SkyDNS2。

```
docker run -d \
--name=registrator \    #定义容器名称
--net=host \    #定义网络
-v /var/run/docker.sock:/tmp/docker.sock \     #指定数据卷，存储信息
--restart=always \    #重启策略（只要容器是非up状态，都将重启）
gliderlabs/registrator:latest \    #定义镜像
-ip=192.168.111.10 \    #本机IP
consul://192.168.111.40:8500    #consul节点的地址，端口

```

##### 测试服务看功能是否正常：

```
docker run -itd -p:81:80 --name test-01 -h test01 nginx
docker run -itd -p:82:80 --name test-02 -h test02 nginx
docker run -itd -p:83:80 --name test-03 -h test03 httpd
docker run -itd -p:84:80 --name test-04 -h test04 httpd

```

<img src="https://img-blog.csdnimg.cn/8ac3612d0e744e689372fca8dd14c2d2.png#pic_center" alt="在这里插入图片描述">

**验证http和nginx服务是否注册到consul**

浏览器输入http://192.168.111.40:8500，“单击SERVICES”，然后单击"consurl-server01"，会出现5个服务：

<img src="https://img-blog.csdnimg.cn/62312422eb324c7c8f3ac55cd0f3416f.png#pic_center" alt="在这里插入图片描述">

**在web节点输入以下命令可以实时查看访问记录**

```
docker logs -f test-02

```

<img src="https://img-blog.csdnimg.cn/fb307cd8c7014275828185ea649bf044.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/93433088fa8842d682b2da4c48afc63c.png#pic_center" alt="在这里插入图片描述">

##### 安装consul-template（consul节点）

Consul-Template_是一个守护进程，用于实时查询Consul集群信息，并更新文件系统上任意数量的指定模板，生成配置文件。更新完成以后，可以选择运行shell命令执行更新操作，重新加载Nginx。

Consul-Template可以查询Consul中的服务目录、Key、Key-values等。 这种强大的抽象功能和查询语言模板可以使Consul-Template特别适合动态的创建配置文件。例如:创建Apache/Nginx 、Proxy Balancers、Haproxy Backends等。

```
cd /root/consul
#拉取consul-template_0.19.3_linux_amd64.zip
unzip consul-template_0.19.3_linux_amd64.zip
mv consul-template /usr/bin

```

**准备template nginx 模板文件**

```
vim /root/consul/nginx.ctmpl

upstream http_backend {<!-- -->
  {<!-- -->{<!-- -->range service "nginx"}}
  server {<!-- -->{<!-- -->.Address}}:{<!-- -->{<!-- -->.Port}};
  {<!-- -->{<!-- -->end}}
}

server {<!-- -->
  listen 1234;
  server_name localhost 192.168.111.40;
  access_log /var/log/nginx/access.log;
  index index.html index.php;
  location / {<!-- -->
    proxy_set_header HOST $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header Client-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_pass http://http_backend;
  }
}


```
- 此模板用于nginx反向代理模板- nginx.ctmpl跟nginx没有直接关系- consul是docker的一种自动管理机制- nginx.ctmpl中的参数以变量的形式写入
##### 编译安装nginx

```
yum install gcc pcre-devel zlib-devel -y
cd /opt
#拉取nginx源码包
tar zxvf nginx-1.12.2.tar.gz 
cd nginx-1.12.2/
./configure --prefix=/usr/local/nginx
make &amp;&amp; make install
#创建软连接
ln -s /usr/local/nginx/sbin/nginx /usr/local/sbin

#配置nginx
vim /usr/local/nginx/conf/nginx.conf	
http {<!-- -->
      include        mime.types;
      include    vhost/*.conf;             #添加虚拟主机目录
      default_type  application/octet-stream;

#创建虚拟主机目录
mkdir /usr/local/nginx/conf/vhost
#创建日志文件目录
mkdir /var/log/nginx
#启动nginx
nginx

```

##### 配置并启动 template

```
#启用模板
consul-template -consul-addr 192.168.111.40:8500 -template "/root/consul/nginx.ctmpl:/usr/local/nginx/conf/vhost/wt.conf:/usr/local/nginx/sbin/nginx -s reload" --log-level=info

```

出现此界面说明 template 启动成功;

<img src="https://img-blog.csdnimg.cn/b267d277c90444faa1200405fd222ff4.png#pic_center" alt="在这里插入图片描述">

再重新打开一个终端，查看配置文件

<img src="https://img-blog.csdnimg.cn/f8e59031c8234ba4ad15926e25e84a33.png#pic_center" alt="在这里插入图片描述">

```
#增加一个nginx容器节点，测试服务器发现以及配置更新功能
#在 registrator/192.168.111.10 节点注册
docker run -itd -p 85:80 --name test-05 -h test05 nginx

#打开一个新的xshell终端查看生成配置文件，可以看到多了一个nginx节点

```

<img src="https://img-blog.csdnimg.cn/a363f7af7c5e47278aa4645a3e3b7dbc.png#pic_center" alt="在这里插入图片描述">

##### 测试

在网页端查看，发现85端口出现

<img src="https://img-blog.csdnimg.cn/1787d04dd9274255a728253ee14da875.png#pic_center" alt="在这里插入图片描述">

再去查看三台nginx容器日志，请求正常轮训到各个容器节点上；

```
docker logs -f test-01
docker logs -f test-02
docker logs -f test-03

```

### 总结

项目实验要自己动手操作，再多的原理不去实践也只是纸上谈兵，有句诗词说的很妙： 纸上得来终觉浅，绝知此事要躬行。加油吧，少年！
