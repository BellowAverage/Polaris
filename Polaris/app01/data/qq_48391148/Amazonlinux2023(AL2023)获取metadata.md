
--- 
title:  Amazonlinux2023(AL2023)获取metadata 
tags: []
categories: [] 

---
今年AWS发布了新的Amazonlinux2023版本，其中获取metadata元数据方式发生了一点改变。

早些时候，在 Amazon Linux 2 中，使用以下命令获取实例元数据

```
http://169.254.169.254/latest/meta-data/
```

具体可以获取的元数据类别可以查阅如下aws官方文档

在AL2023中获取实例metadata之前需要先获取一个token

```
TOKEN=$(curl --request PUT "http://169.254.169.254/latest/api/token" --header "X-aws-ec2-metadata-token-ttl-seconds: 3600")
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    56  100    56    0     0  39886      0 --:--:-- --:--:-- --:--:-- 56000


# 可以使用echo $TOKEN来查看这个token
```

然后在给aws接口发送请求的头部信息里面加入token信息

示例：获取实例的instance-id：

```
 curl http://169.254.169.254/latest/meta-data/instance-id --header "X-aws-ec2-metadata-token:$TOKEN"

返回实例id：i-xxxxxxxxx
```


