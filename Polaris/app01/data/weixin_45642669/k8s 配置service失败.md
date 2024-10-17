
--- 
title:  k8s 配置service失败 
tags: []
categories: [] 

---
#### 服务暴露的端口不可用

查看容器的状态是否为Running。   进入容器，然后对容器进行curl。

```
curl 127.0.0.0:&lt;需要查询的端口&gt;

```

如果是refuse或者其他返回，说明服务完全不可用。

很多人认为修改了pod的端口信息，那么代表着服务的端口也自动迁移过去，这个是根本不可能的。 pod的端口信息和服务的端口信息完全无关。

#### 注册service

能够进行外网访问的必须是NodePort类型。NodeIP是无法进行外网访问的 访问的地址为任意node节点。

如果是Nodeport，那么不能够配置Session Affinity项目，不然会无法暴露服务

#### 查看是否绑定endPoints

```
kubectl describe svc

```

如果endpoints为null，那么说明没有成功绑定

一个Service由一组Pod组成，这些Pod通过Endpoint暴露出来，Endpoint是实现实际服务的端点集合，Service与Pod之间的联系是通过Endpoints实现的；

所以当endPoints为空那么说明没有成功绑定pod， 需要重新配置label进行配置。

<img src="https://img-blog.csdnimg.cn/2c83af2a849546758fca0e5e57cac4e2.png" alt="在这里插入图片描述">
