
--- 
title:  使用docker安装redis时报错 ‘WARNING: IPv4 forwarding is disabled.‘ 
tags: []
categories: [] 

---
```
docker pull redis
docker run --name trend_redis_xueliang10 -d -p 16379:6379 redis
报错
WARNING: IPv4 forwarding is disabled. Networking will not work.

```



#### 文章目录
- - 


## 解决1 (有root权限)

在运行Docker容器时出现 “WARNING: IPv4 forwarding is disabled. Networking will not work.” 的警告通常是由于主机的 IP 转发被禁用导致的。您可以通过以下方式解决这个问题：
1. **启用 IPv4 转发**： 在终端中执行以下命令以临时启用 IPv4 转发：
```
sudo sysctl -w net.ipv4.ip_forward=1

```

如果想要永久启用 IPv4 转发，可以编辑 `/etc/sysctl.conf` 文件，并确保以下行存在并设置为 `1`：

```
net.ipv4.ip_forward = 1

```

保存更改后，运行以下命令使更改生效：

```
sudo sysctl -p

```
1. **重新运行 Docker 容器**： 一旦您已经启用了 IPv4 转发，您可以尝试重新运行 Redis 容器：
```
docker run --name trend_redis_xueliang10 -d -p 16379:6379 redis

```

通过以上步骤，您应该能够成功启动 Redis 容器而不再收到 IPv4 转发被禁用的警告。

## 解决2 (无root权限)

如果您尝试启用 IPv4 转发后仍然遇到问题，还有其他方法可以解决 Docker 容器 networking 的问题：
1. **使用 host 网络模式**：(推荐) 您可以在运行 Docker 容器时使用 `--network host` 参数来将容器连接到主机网络，而不是创建一个独立的网络命名空间。这样可以避免一些网络配置的问题。
```
docker run --name trend_redis_xueliang10 -d --network host redis

```
1. **使用 bridge 网络模式**： 尝试使用默认的 bridge 网络模式，并指定端口映射。
```
docker run --name trend_redis_xueliang10 -d -p 16379:6379 redis

```
1. **检查防火墙设置**： 确保防火墙未阻止 Docker 容器的网络连接。您可以暂时关闭防火墙进行测试，看是否能够解决问题。
这些方法中，使用 host 网络模式可能是最简单的解决方案之一。您可以尝试以上方法中的一个或多个来解决 Docker 容器 networking 的问题。
