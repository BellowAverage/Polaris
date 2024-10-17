
--- 
title:  docker部署zabbix 
tags: []
categories: [] 

---
## docker部署zabbix

### 1、zabbix入门：

Zabbix 是一款能够监控各种网络参数以及服务器健康性和完整性的软件。

Zabbix 使用灵活的通知机制，允许用户为几乎任何事件配置基于邮件的告警，这样可以快速反馈服务器的问题。

##### zabbix基础框架：

<img src="https://img-blog.csdnimg.cn/1f0598742fa94b099ace0cf35ac6e328.png#pic_center" alt="在这里插入图片描述">

##### 核心组件：
-  agent： 负责采集数据并通过主动或者被动的方式采集数据发送到 Server/Proxy，除此之外，为了扩展监控项，Agent 还支持执行自定义脚本。 -  server： Server 主要负责接收 Agent 发送的监控信息，并进行汇总存储，触发告警等 
>  
 Zabbix Server 将收集的监控数据存储到 Zabbix Database 中。Zabbix Database 支持常用的关系型数据库，如果 MySQL、PostgreSQL、Oracle 等，默认是 MySQL，并提供 Zabbix Web页面（PHP 编写）数据查询。 
 现在zabbix也支持TSDB 时序数据库，用于监控docker等。 


### 2、zabbix和Prometheus对比：

|监控软件|发行时间|开发语言|性能|社区支持|容器支持|企业使用|部署难度
|------
|Prometheus|2016|go|支持万为单位|相对不如zabbix，但人数与日剧增|支持swarm、k8s等容器集群的监控，监控容器最好的方案|使用容器与k8s的企业|只有一个核心server组件，一条命令即可启动
|zabbix|2012|C+php|上限约为10000节点|应用广泛，支持较成熟|服务器相关监控具有绝对优势|传统服务器监控|多种系统，多种监控信息采集方式

结论：
-  如果监控的是物理机，用 Zabbix，Zabbix 在传统监控系统中，尤其是在服务器相监控方面，占据绝对优势。甚至环境变动不会很频繁的情况下，Zabbix 也会比 Prometheus 好使 -  如果是云环境的话，除非是 Zabbix 玩的非常溜，可以做各种定制，否则还是Prometheus 吧，毕竟人家就是干这个的。 -  Prometheus 开始成为主导及容器监控方面的标配，并且在未来可见的时间内被广泛应用。如果是刚刚要上监控系统的话，不用犹豫了，Prometheus 准没错。 
### 3、linux安装docker：

##### （1）手动安装docker：

docker入门及部署

##### （2）脚本一键部署docker：

[脚本一键安装docker]()

```
#!/bin/bash 
#file:docker_install.sh 
echo "--检查内核版本......--"
yum -y install bc &amp;&gt; /dev/null
kenel=`uname -r`
ken=`echo ${<!-- -->kenel:0:4}`
if [ $(echo "${ken} &gt;= 3.10" | bc) = 1 ]
then
  echo "--检查Docker......!--"
  docker -v &amp;&gt; /dev/null
  a=`echo $?`
  while [ $a -ne 0 ]; do
    echo "--安装docker环境...--"
    echo "--安装基础依赖...--"
    yum install yum-utils device-mapper-persistent-data lvm2 -y &amp;&gt; /dev/null
    echo "--安装docker-ce.repo--"
    cd /etc/yum.repo.d
    yum-config-manager --add-repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo &amp;&gt; /dev/null
    echo "--安装docker环境...--"
    yum install docker-ce -y
    docker -v &amp;&gt; /dev/null
    a=`echo $?`
  done
  echo "--安装完成!启动Docker--"
  systemctl start docker
  systemctl enable docker &amp;&gt; /dev/null
  echo "----网络优化----"
  sed -i '$a net.ipv4.ip_forward=1' /etc/sysctl.conf
  sysctl -p
  systemctl restart network
  systemctl restart docker
  docker version
else
  echo "--内核版本太低，请您升级内核版本!--"
fi

```

```
#!/bin/bash
#file:docker_net.sh 
echo "----镜像加速-----"
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json &lt;&lt;-'EOF'
{
"registry-mirrors": ["https://yagayyvn.mirror.aliyuncs.com"]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker
echo "镜像加速完成！！！"

```

##### （3）脚本安装docker compose：

```
#!/bin/bash
#file：docker-compose_install.sh
curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

chmod +x /usr/local/bin/docker-compose
ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
docker-compose --version

```

### 4、docker环境下部署zabbix：

>  
 zabbix在docker官方的镜像源中，有维护zabbix公司官方的镜像，我们可以通过hub.docker.com进行下载，搭建docker环境下的zabbix，可以使我们的安装和部署更加快捷。 


##### 1、zabbix的docker镜像源：
- 这里  我们可以打开看到zabbix官方在docker仓库里面维护的镜像源信息。- 官方的dockerhub仓库中有各个zabbix的组件的镜像源，可以根据需求自行pull。
<img src="https://img-blog.csdnimg.cn/2aef724cf7eb4cfb81957d391e39061f.png#pic_center" alt="在这里插入图片描述">

##### 2、zabbix官方文档：

>  
 初始化数据文件可以从 [zabbix的官方]() 进行下载，一些操作啥的，官方文档有详细的说明，并且支持中文。 


<img src="https://img-blog.csdnimg.cn/773286e7018f4e9bb67b95a62d65e9b3.png#pic_center" alt="在这里插入图片描述">

##### 3、docker compose一键部署zabbix：
- 先配置环境：
```
#创建相关的目录及文件
cd /home
mkdir -p docker/mysql
vi docker/zabbix.yml

#下面是zabbix的yml文件

```

```
version: '3.7'
services:
  mysql-server:
    image: mysql:latest
    environment:
      MYSQL_ROOT_PASSWORD: password
      MYSQL_USER: zabbix
      MYSQL_PASSWORD: zabbix
      MYSQL_DATABASE: zabbix
    volumes:
      - "/etc/localtime:/etc/localtime"
      - "/home/docker/mysql:/var/lib/mysql"
    ports:
      - "3306:3306"
    networks:
      - zbx_net

  zabbix-server:
    image: zabbix/zabbix-server-mysql:centos-latest
    environment:
      DB_SERVER_HOST: mysql-server
      MYSQL_DATABASE: zabbix
      MYSQL_USER: zabbix
      MYSQL_PASSWORD: zabbix
    ports:
      - "10051:10051"
    depends_on:
      - "mysql-server"
    volumes:
      - /etc/localtime:/etc/localtime:ro
      - /etc/timezone:/etc/timezone:ro 
      - "zabbix:/var/lib/zabbix"
    networks:
      - zbx_net


  zabbix-web:
    image: zabbix/zabbix-web-nginx-mysql:latest
    environment:
      DB_SERVER_HOST: mysql-server
      MYSQL_DATABASE: zabbix
      MYSQL_USER: zabbix
      MYSQL_PASSWORD: zabbix
      PHP_TZ: Asia/Shanghai
      ZBX_SERVER_HOST: zabbix-server
    ports:
      - 8088:8080
    depends_on:
      - mysql-server
      - zabbix-server    
    networks:
      - zbx_net

  zabbix-agent:
    image: zabbix/zabbix-agent:latest
    environment:
      ZBX_SERVER_HOST: zabbix-server
    ports:
     - "10050:10050"
    depends_on:
     - "zabbix-server"
    networks:
     - zbx_net

networks:
 zbx_net:
volumes:
  zabbix:

```

##### 4、使用zabbix：
- 访问地址：ip:8088
这个ip是你主机的ip，端口是yml 文件中映射在你主机上的端口；可以自行修改。

<img src="https://img-blog.csdnimg.cn/7fecdc8453db4f9790f7a6f9bd7adeab.png#pic_center" alt="在这里插入图片描述">

这是Zabbix的“欢迎”界面。输入用户名 **Admin** 以及密码 **zabbix** 以作为 登陆。

下面想要快速入门的话，可以看官方文档，超级详细。

<img src="https://img-blog.csdnimg.cn/ea67956fde9143a183c643a01f30dfef.png#pic_center" alt="在这里插入图片描述">

>  
 zabbix 里面还可将web 界面设置成中文： 


<img src="https://img-blog.csdnimg.cn/6d1ff3c15240420793e5bd86ede43814.png#pic_center" alt="在这里插入图片描述">

下面就开始使用zabbix吧！！！

>  
 zabbix 还支持脚本编写来进行告警哦。比如利用shell 写一个调用短信接口的脚本，然后利用这个脚本进行短信告警，会实时的发送短信。 

