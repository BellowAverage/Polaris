
--- 
title:  linux的centos系统安装MongoDB详细步骤（包括创建用户的各种操作及遇到的问题汇总） 
tags: []
categories: [] 

---
### 一. 安装MongoDB

#### 步骤1：下载MongoDB

可选择官网下载：

也可以根据自己服务器系统版本，选择对应的RPM包下载。对应网站：

若使用命令行方式下载，可在shell下使用 wget 下载。需要将对应版本的依赖包也一起下载下来。

```
wget https://repo.mongodb.org/yum/redhat/7/mongodb-org/5.0/x86_64/RPMS/mongodb-org-5.0.5-1.el7.x86_64.rpm

wget https://repo.mongodb.org/yum/redhat/7/mongodb-org/5.0/x86_64/RPMS/mongodb-org-mongos-5.0.5-1.el7.x86_64.rpm

wget https://repo.mongodb.org/yum/redhat/7/mongodb-org/5.0/x86_64/RPMS/mongodb-org-server-5.0.5-1.el7.x86_64.rpm

wget https://repo.mongodb.org/yum/redhat/7/mongodb-org/5.0/x86_64/RPMS/mongodb-org-shell-5.0.5-1.el7.x86_64.rpm

wget https://repo.mongodb.org/yum/redhat/7/mongodb-org/5.0/x86_64/RPMS/mongodb-org-tools-5.0.5-1.el7.x86_64.rpm


```

#### 步骤2：安装Mongodb

下载后先安装依赖，再安装Mongodb，如果遇到报错，请看下面的解决方案。

```
rpm -ivh mongodb-org-mongos-5.0.5-1.el7.x86_64.rpm

rpm -ivh mongodb-org-server-5.0.5-1.el7.x86_64.rpm

rpm -ivh mongodb-org-shell-5.0.5-1.el7.x86_64.rpm

rpm -ivh mongodb-org-tools-5.0.5-1.el7.x86_64.rpm

rpm -ivh mongodb-org-5.0.5-1.el7.x86_64.rpm


```

#### 步骤3：启动Mongodb服务

如果正在运行防火墙(firewalld)，则还需要打开27017端口：

终端运行：`firewall-cmd --permanent --zone=public --add-port=27017/tcp`

再运行：`firewall-cmd --reload` 重新加载mongo即可。

启动Mongodb服务：`systemctl start mongod`

检查其运行状态：`systemctl status mongod`

开机启动Mongodb服务：`systemctl enable mongod`

**至此，mongodb已启动成功，通过主机加端口即可访问，通过navicat客户端或者compass客户端等工具都可以访问。 `但是这样操作在外网往往是不安全的，建议更改端口，并增加复杂度高的账号密码`。**

### 二. 配置文件修改

Mongodb的配置文件为 ：/etc/mongod.conf

```
# mongod.conf

# for documentation of all options, see:
#   http://docs.mongodb.org/manual/reference/configuration-options/

# where to write logging data.
systemLog:
  destination: file
  logAppend: true
  path: /var/log/mongodb/mongod.log

# Where and how to store data.
storage:
  dbPath: /var/lib/mongo
  journal:
    enabled: true
#  engine:
#  mmapv1:
#  wiredTiger:

# how the process runs
processManagement:
  fork: true  # fork and run in background
  pidFilePath: /var/run/mongodb/mongod.pid  # location of pidfile
  timeZoneInfo: /usr/share/zoneinfo

# network interfaces
net:
  port: 27017
  bindIp: 127.0.0.1  # Enter 0.0.0.0,:: to bind to all IPv4 and IPv6 addresses or, alternatively, use the net.bindIpAll setting.


#security:
```
