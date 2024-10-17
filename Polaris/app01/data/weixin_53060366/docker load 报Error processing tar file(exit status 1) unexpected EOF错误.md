
--- 
title:  docker load 报Error processing tar file(exit status 1) unexpected EOF错误 
tags: []
categories: [] 

---
## docker load 报Error processing tar file(exit status 1): unexpected EOF错误

#### 1、将本地的镜像打包后，上传到服务器进行load，显示这个错误：

```
docker load -i myrasa.tar 
Error processing tar file(exit status 1): unexpected EOF

```

#### 2、解决思路：

[一个新手的学习docker的教程]()



>  
 <mark>（我的是因为下载的镜像文件损坏了。所以加载失败。）</mark> 


查过一些资料，发现可能原因有两种：

>  
 <pre><code class="prism language-text">1、.tar文件损坏（因为在本地看到的文件大小和通过fxp上传显示的大小不一致，本地显示5G左右，但
是传送显示大概在500M左右，所以一直在纠结是不是.tar文件的缺失）

2、有可能是docker的docker根目录空间不足，然后进行解决，解决的方案在x这个z链接里面
</code></pre> 


##### 拉取docker镜像时提示 no space left on device 问题解决

出现此问题一般是docker 根目录空间不足导致。**可修改其 Docker Root Dir 的值，使其指向一个更大空间的目录即可**

1、查看docker 的根目录：

```
docker info 

#显示信息中有docker根目录的位置信息， 
Docker Root Dir: /var/lib/docker/

# 查看目录所剩空间
df  -hl   /var/lib/docker/

```

可以发现，其它空间占用率为100% 已经满了。

我把它改到/home/docker/lib/docker目录下

```
# 创建目标目录
mkdir -p /etc/systemd/system/docker.service.d/

# 创建配置文件
vi /etc/systemd/system/docker.service.d/devicemapper.conf

# 录入配置信息
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd  --graph=/home/docker/lib/docker

# 依次执行以下命令
systemctl daemon-reload

systemctl restart docker

systemctl enable docker

```

>  
 注意，由于更换了docker 目录，以前下载的镜像需要转移到新目录下，本人通过 cp -R 命令复制过来后，启动时遇到一些问题，建议直接删除原来的镜像，重新下载。 

