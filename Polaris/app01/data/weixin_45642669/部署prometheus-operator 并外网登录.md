
--- 
title:  部署prometheus-operator 并外网登录 
tags: []
categories: [] 

---
### 下载普罗米修斯

```
git clone https://github.com/prometheus-operator/kube-prometheus

```

#### 部署普罗米修斯

```
kubectl apply -f kube-prometheus/manifests/
kubectk apply -f kube-prometheus/manifests/step/

```

然后就会自动创建普罗米修斯。

#### 查看状态

```
kubectl get all -n monitoring

```

<img src="https://img-blog.csdnimg.cn/660a41cb96e3474284ecf76127428720.png" alt="在这里插入图片描述"> 修改service中
- service/grafana- service/prometheus-k8s- service/alertmanager-main 为NodePort。
删除sessionAffinity: ClientIP这一行（这会导致外网暴露失效）

然后查看暴露的端口为： <img src="https://img-blog.csdnimg.cn/eaa3dedbc36745d99d38defd9428fe7e.png" alt="在这里插入图片描述">

#### 查看状态

进入普罗米修斯 <img src="https://img-blog.csdnimg.cn/5bf697a853da4b2990656412248de6df.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/ec0d46e2aaa144a4a79dda60a925b8b7.png" alt="在这里插入图片描述"> 点击Test，得到 <img src="https://img-blog.csdnimg.cn/7d1acfe76035404e89f1adbd961b150a.png" alt="在这里插入图片描述"> 配置完成。
