
--- 
title:  ubuntu 添加systemctl 启动程序 
tags: []
categories: [] 

---
### 1.添加service启动文件

```
cd /lib/systemd/system
sudo touch test.service

```

**添加启动内容：**

```
sudo vim test.service
# 将下列信息添加到test.service
[Unit]
Description=my_test

[Service]
ExecStart=/usr/local/test_server/bin/test #服务程序地址，一般为可执行文件
TimeoutSec=45s
Restart=always
WorkingDirectory=/usr/local/test_server
User=xiaoming #用户名
Group=xiaoming #用户所在组
LimitNOFILE=65535/


[Install]
WantedBy=multi-user.target


```

### 2.加载systemctl更新新消息

```
sudo systemctl daemon-reload

```

### 3.验证是否添加成功

```
# 启动服务
sudo systemctl start test.service

# 重启服务
sudo systemctl restart test.service

# 停止服务
sudo systemctl stop test.service

```
