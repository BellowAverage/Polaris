
--- 
title:  nginx和redis参数检查脚本 
tags: []
categories: [] 

---
### nginx和redis服务的参数脚本

#### redis相关参数：

```
#!/bin/bash

# 获取Redis进程ID
redis_pid=$(pidof redis-server)

# 检查Redis是否在运行中
if [ -z "$redis_pid" ]; then
  echo "Redis服务未运行"
  exit 1
fi

# 获取Redis的版本信息
redis_version=$(redis-server --version)

# 获取Redis的运行状态信息
redis_status=$(systemctl status redis | grep Active)

# 获取Redis的内存使用情况
redis_memory=$(redis-cli info memory | grep used_memory_human)

# 获取Redis的网络连接情况
redis_clients=$(redis-cli info clients | grep connected_clients)

# 获取Redis的键值对数量
redis_keys=$(redis-cli info keyspace | grep keys)

# 打印获取的Redis信息
echo "Redis服务版本：$redis_version"
echo "Redis服务状态：$redis_status"
echo "Redis内存使用：$redis_memory"
echo "Redis客户端连接数：$redis_clients"
echo "Redis键值对数量：$redis_keys"

```

#### nginx检查脚本：

```
#!/bin/bash

# 检查nginx进程是否正在运行
nginx_process=$(pgrep nginx)

if [ -z "$nginx_process" ]; then
  echo "Nginx进程未运行"
  echo "Nginx process is not running"
  exit 1
else
  echo "Nginx进程正在运行"
  echo "Nginx process is running"
fi

# 查询nginx的总请求数
total_requests=$(cat /usr/local/nginx/logs/access.log | awk '{print $7}' | wc -l)

echo "Nginx总请求数：$total_requests"
echo "Total number of Nginx requests: $total_requests"

# 查询nginx的并发连接数
concurrent_connections=$(cat /usr/local/nginx/logs/nginx.pid | wc -l)

echo "Nginx并发连接数：$concurrent_connections"
echo "Number of concurrent Nginx connections: $concurrent_connections"

# 查询nginx的内存使用情况
memory_usage=$(ps aux | grep nginx | grep -v grep | awk '{print $4}')

echo "Nginx内存使用情况：$memory_usage MB"
echo "Nginx memory usage: $memory_usage MB"

# 查询nginx的CPU使用情况
cpu_usage=$(ps aux | grep nginx | grep -v grep | awk '{print $3}')

echo "Nginx CPU使用情况：$cpu_usage%"
echo "Nginx CPU usage: $cpu_usage%"

```
