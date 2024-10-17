
--- 
title:  K8s svc失效 
tags: []
categories: [] 

---
## 问题描述
- svc失效，无法ping通svc提供的端口- 通过内网pod ip去调用，内网联通，但是无法通过外网联通- svc信息确认无误，在其他环境测试正常
## 解决

怀疑是K8s调度的时候出现了一些bug，导致nginx初始化失败 如果使用helm的话，直接uninstall以后重新install。问题即可解决。

第二种：直接重新部署svc

```
kubectl get deployment  《svc的名字》-o yaml  

```

确认无误以后导出svc并删除：

```
kubectl get svc  《svc的名字》-o yaml  &gt; 1.yaml
kubectl delete svc 《svc的名字》 

```

删除1.yaml中关于uid的信息（不然无法重新部署）

然后重新：

```
kubectl apply -f 1.yaml

```

即可通过相同的部署逻辑重新部署svc
