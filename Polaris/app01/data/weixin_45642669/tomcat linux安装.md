
--- 
title:  tomcat linux安装 
tags: []
categories: [] 

---
### 预先安装jdk

这个不用说：

```
yum list installed|grep jdk

```

如果没有

```
yum list| grep jdk
yum install XX(你需要的版本)

```

### 获取下载链接

进入官网：

然后选择需要的版本，然后获取下载链接

### 下载并解压

下载文件

```
cd /usr/local
mkdir local
wget 下载链接

```

```
ls -alh
tar -xzvf 你下载的文件名

```

### 开启防火墙

```
// 这个是centos7的命令
firewall-cmd --zone=public --add-port=8080/tcp --permanent（端口可以变化，不一定是8080）
firewall-cmd --reload
firewall-cmd --zone=public --list-ports

```

### 开启服务

如果路径没有变化的话，系统是在bin里面

```
cd bin
./startup.sh

```

开启服务

### 测试网络连通性

查看IP外网地址

```
ifconfig -a // 这是外网
curl ifconfig.me // 这是内网

```

由于没有DNS解析，也不能用80端口，所以直接在任何一台能够联网的电脑上

```
http://你的外网地址：8080

```

这个操作是不安全的建议还是内网比较合适这种操作。

出现tomcat登陆界面即可。
