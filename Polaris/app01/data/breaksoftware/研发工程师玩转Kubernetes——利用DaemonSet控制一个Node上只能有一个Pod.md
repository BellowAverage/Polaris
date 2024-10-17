
--- 
title:  研发工程师玩转Kubernetes——利用DaemonSet控制一个Node上只能有一个Pod 
tags: []
categories: [] 

---
有一种比一文中介绍的更简单的方法控制一个Node上只有一个Pod，那就是使用DaemonSet。

```
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: nginx-daemonset
spec:
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80

```

通过上述清单文件创建Pod。可以看到每个Node都被部署了一个Pod。

```
kubectl get pod -o wide

```

```
NAME                    READY   STATUS    RESTARTS   AGE     IP             NODE      NOMINATED NODE   READINESS GATES
nginx-daemonset-kl9jm   1/1     Running   0          4m23s   10.1.202.212   ubuntud   &lt;none&gt;           &lt;none&gt;
nginx-daemonset-zr8k7   1/1     Running   0          4m23s   10.1.94.67     ubuntua   &lt;none&gt;           &lt;none&gt;
nginx-daemonset-z2ptj   1/1     Running   0          4m23s   10.1.209.145   ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-daemonset-6c2vp   1/1     Running   0          4m23s   10.1.226.1     ubuntue   &lt;none&gt;           &lt;none&gt;
nginx-daemonset-tbj4w   1/1     Running   0          4m23s   10.1.43.209    ubuntuc   &lt;none&gt;           &lt;none&gt;

```
