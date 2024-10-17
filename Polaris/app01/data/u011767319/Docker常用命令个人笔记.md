
--- 
title:  Docker常用命令个人笔记 
tags: []
categories: [] 

---
### 安装Docker先检查

>  
 以CentOS为例：查看当前当前的CentOs内核版本是不是高于3.10的。 查看CentOS内核命令：`uname -r` 如果不是,请升级内核，命令用：`yum update` 安装docker，命令：`yum install docker` 启动docker，命令：`systemctl start docker` 将docker服务设为开机自启，命令：`systemctl enable docker` 停止docker，命令：`systemctl stop docker` 


### 镜像操作

>  
 检索（搜索）：我们常去docker hub上检索镜像的详细信息，如镜像的TAG。 检索命令：`docker search 关键字` 拉取（下载）：:tag是可选的，tag表示标签，多为软件的版本，默认是latest 拉取命令：`docker pull 镜像名`或者`docker pull 镜像名:tag` 列表：查看所有本地镜像 列表命令：`docker images` 删除：删除指定的本地镜像 删除命令：`docker rmi image-id` 


### 容器操作

|操作|命令|说明
|------
|运行|docker run --name container -d image-name eg:docker run --name myredis - d redis|-name ：自定义容器名，-d：后台运行，image-name：指定镜像模板（eg:是如的意思）
|列表|docker ps （查看运行中的容器）|加上-a；可以查看所有容器
|停止|docker stop container-name/container-id|停止当前你运行的容器
|启动|docker start container-name/container-id|启动容器
|重启|docker restart container-name/container-id|重启容器
|删除|docker rm container-id|删除指定容器
|端口映射|-p 6379:6379 eg:docker run -d -p 6379:6379–name myerdis docker.io/redis|-p：主机端口（映射到）容器内部的端口
|容器日志|docker logs container-name/container-id|
|进入容器|docker exec -it container-name/container-id bash|进入容器bash并进入container-name/container-id命令行

### 更换镜像源

新版的 Docker 推荐使用 json 配置文件的方式，默认为 /etc/docker/daemon.json，非默认路径需要修改 dockerd 的 –config-file，在该文件中加入如下内容

```
{<!-- --> 
"registry-mirrors": ["https://docker.mirrors.ustc.edu.cn"] 
}
//https://8aqx0ma5.mirror.aliyuncs.com

```

```
//重启
systemctl restart docker

```

### 如何查看已经运行的进行的运行命令

```
runlike -p docker_name

```

效果图： <img src="https://img-blog.csdnimg.cn/6d71dd275bf949fe8be752b0a733ba3d.png" alt="在这里插入图片描述">

### mysql 启动记录

|操作|命令|说明
|------
|启动mysql|docker run --name 自定义名称 -e MYSQL_ROOT_PASSWORD=自定义密码 -p 3306:3306 -d mysql （可以额外加上） :tag|MYSQL_ROOT_PASSWORD设置MySQL 起始密码

### docker服务重启后容器也自动重启

在运行docker容器时可以加如下参数来保证每次docker服务重启后容器也自动重启：

```
docker run --restart=always
//使用例子
docker run -d --restart=always --log-driver json-file --log-opt max-size=100m --log-opt max-file=2  --name zookeeper -p 2181:2181 &lt;br&gt;-v /etc/localtime:/etc/localtime wurstmeister/zookeeper

```

如果已经启动了则可以使用如下命令：

```
docker update --restart=always &lt;CONTAINER ID&gt;

```

### 如何查看容器内部ip

```
docker inspect --format '{<!-- -->{<!-- --> .NetworkSettings.IPAddress }}'  容器ID

```

### 如何进入容器内部

```
docker exec -it kibana容器id /bin/bash

```

### 完美拷贝本地文件到docker容器



### docker容器中安装vim



### ubuntu安装docker

**使用官方安装脚本自动安装** **安装命令如下：**

```
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun

```

### 修改容器名称

```
docker rename 容器原来名 要改为的名字

```

### 安装docker-compose
<li> 安装epel源 <pre><code class="prism language-java">yum install -y epel-release
</code></pre> </li><li> 安装docker-compose <pre><code class="prism language-java">yum install -y docker-compose 
</code></pre> </li>
### 配置远程访问

>  
 修改宿主机配置文件 


```
vi /lib/systemd/system/docker.service

```

>  
 在 ExecStart 开头的这一行末尾添加 -H tcp://0.0.0.0:2375 


<img src="https://img-blog.csdnimg.cn/20210424221709835.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

>  
 重启docker 


```
systemctl daemon-reload &amp;&amp; systemctl restart docker

```

>  
 防火墙开放端口（关闭防火墙的请忽略） 


```
firewall-cmd --zone=public --add-port=2375/tcp --permanent

```

>  
 通过外网访问测试成功 http://ip地址:2375/version 


<img src="https://img-blog.csdnimg.cn/20210424221628238.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

### 上面方法开启远程后

>  
 本机不可以访问，怎么解决呢 <img src="https://img-blog.csdnimg.cn/20210428172652809.png" alt="在这里插入图片描述"> 


添加本地访问：

```
-H unix:///var/run/docker.sock

```

<img src="https://img-blog.csdnimg.cn/20210428172741624.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

>  
 重启docker 


```
systemctl daemon-reload &amp;&amp; systemctl restart docker

```

<img src="https://img-blog.csdnimg.cn/20210428172927320.png" alt="在这里插入图片描述">

### 配置docker 的远程安全访问

>  
 创建ca文件夹 本人创建的目录为 /home/ca 用来存放CA私钥和公钥 


```
cd /home
mkdir ca
cd ca/

```

**创建ca的公钥和私钥-设置密码**

>  
 需要连续输入两次相同的密码 


```
openssl genrsa -aes256 -out ca-key.pem 4096

```

>  
 依次输入密码、国家、省、市、组织名称等（除了密码外其他的可以直接回车跳过） 


```
openssl req -new -x509 -days 365 -key ca-key.pem -sha256 -out ca.pem

```

>  
 生成server.csr（把下面的IP换成你自己服务器外网的IP或者域名） 


```
openssl req -subj "/CN=123.123.123.123" -sha256 -new -key server-key.pem -out server.csr

```

>  
 或者也可以设置成域名 


```
echo subjectAltName = DNS:www.example.com,IP:123.123.123.123,IP:127.0.0.1 &gt;&gt; extfile.cnf

```

>  
 将Docker守护程序密钥的扩展使用属性设置为仅用于服务器身份验证 


```
echo extendedKeyUsage = serverAuth &gt;&gt; extfile.cnf

```

>  
 输入之前设置的密码，生成签名证书 


```
openssl x509 -req -days 365 -sha256 -in server.csr -CA ca.pem -CAkey ca-key.pem \
  -CAcreateserial -out server-cert.pem -extfile extfile.cnf

```

>  
 生成供客户端发起远程访问时使用的key.pem 


```
openssl genrsa -out key.pem 4096

```

>  
 生成client.csr（把下面的IP换成你自己服务器外网的IP或者域名） 


```
openssl req -subj "/CN=123.123.123.123" -new -key key.pem -out client.csr

```

>  
 创建扩展配置文件，把密钥设置为客户端身份验证用 


```
echo extendedKeyUsage = clientAuth &gt; extfile-client.cnf

```

>  
 生成cert.pem，输入前面设置的密码，生成签名证书 


```
openssl x509 -req -days 365 -sha256 -in client.csr -CA ca.pem -CAkey ca-key.pem \
  -CAcreateserial -out cert.pem -extfile extfile-client.cnf

```

>  
 删除不需要的配置文件和两个证书的签名请求 


```
rm -v client.csr server.csr extfile.cnf extfile-client.cnf

```

>  
 为了防止私钥文件被更改以及被其他用户查看，修改其权限为所有者只读 


```
chmod -v 0400 ca-key.pem key.pem server-key.pem

```

>  
 为了防止##### 公钥文件被更改，修改其权限为只读 


```
chmod -v 0444 ca.pem server-cert.pem cert.pem

```

>  
 修改Docker配置，使Docker守护程序仅接受来自提供CA信任的证书的客户端的连接 拷贝安装包单元文件到/etc，这样就不会因为docker升级而被覆盖 


```
cp /lib/systemd/system/docker.service /etc/systemd/system/docker.service

```

>  
 在ExecStart=/usr/bin/dockerd-current \下面增加 


```
--tlsverify \
--tlscacert=/etc/docker/certs/ca.pem \
--tlscert=/etc/docker/certs/server-cert.pem \
--tlskey=/etc/docker/certs/server-key.pem \
-H tcp://0.0.0.0:2376 \
-H unix:///var/run/docker.sock \

```

>  
 重新加载daemon并重启docker 


```
systemctl daemon-reload
systemctl restart docker

```

>  
 idea 如何链接呢 再win本地创建一个文件夹储存服务端的三个加密文件 将`ca.pem` `cert.pem` `key.pem` 拷贝到win文件夹 


<img src="https://img-blog.csdnimg.cn/20210513153142369.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/20210513153311734.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

### 挂载权限不够的解决办法

>  
 添加以下属性 


```
--privileged=true

```

### 重启全部docker容器

```
docker restart ${<!-- -->docker ps -q}

```
