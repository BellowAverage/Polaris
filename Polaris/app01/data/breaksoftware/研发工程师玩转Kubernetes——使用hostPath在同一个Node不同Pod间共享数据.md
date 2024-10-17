
--- 
title:  研发工程师玩转Kubernetes——使用hostPath在同一个Node不同Pod间共享数据 
tags: []
categories: [] 

---


#### 大纲
- 


有别于一文中介绍的emptyDir，hostPath可以在**同一个Node的不同Pod间共享**卷。 <img src="https://img-blog.csdnimg.cn/1d88e9d718cf4125b962409d6e408498.png" alt="在这里插入图片描述"> 下面的清单文件利用了Pod亲和性，让Pod集中到一个Node上。

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hostpath-deployment
spec:
  selector:
    matchLabels:
      app: hostpath-container
  replicas: 2
  template:
    metadata:
      labels:
        app: hostpath-container
    spec:
      affinity:
        podAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
          - labelSelector:
                matchExpressions:
                - key: app
                  operator: In
                  values:
                  - hostpath-container
            topologyKey: "kubernetes.io/hostname"
      containers:
      - name: hostpath-container
        image: busybox
        command: ["/bin/sh", "-c" ,"if [ -f /tempdir/lockfile ] &amp;&amp; ! { set -C; 2&gt;/dev/null &gt;/tempdir/lockfile; }; then tail -f /tempdir/lockfile; else exec 3&gt;/tempdir/lockfile; if [ -n \"$POD_NAME\" ]; then name=$POD_NAME; else name=\"unknown\"; fi; while true; do echo \"this is $name.$name write something to lockfile\"; echo \"$name write something to lockfile\" &gt;&amp;3; sleep 5; done; fi"]
        volumeMounts:
        - name: hostpath-volume
          mountPath: /tempdir
        env:
        - name: POD_NAME
          valueFrom:
            fieldRef:
              fieldPath: metadata.name
      volumes:
      - name: hostpath-volume
        hostPath:
          path: /tmp
          type: Directory

```

我们观察创建的两个Pod中文件的内容

```
kubectl exec pods/hostpath-deployment-65cddc7df8-9qtlv -it -- tail -f /tempdir/lockfile

```

>  
 hostpath-deployment-65cddc7df8-9qtlv write something to lockfile hostpath-deployment-65cddc7df8-9qtlv write something to lockfile hostpath-deployment-65cddc7df8-9qtlv write something to lockfile …… 


```
kubectl exec pods/hostpath-deployment-65cddc7df8-ltbgs -it -- tail -f /tempdir/lockfile

```

>  
 hostpath-deployment-65cddc7df8-9qtlv write something to lockfile hostpath-deployment-65cddc7df8-9qtlv write something to lockfile hostpath-deployment-65cddc7df8-9qtlv write something to lockfile …… 


可以看到它们的文件内容一样，即可以证明它们可以共享同一个文件。 我们在hostpath映射的宿主机目录/tmp下可以找到lockfile文件，且其内容也是明文可读的。 <img src="https://img-blog.csdnimg.cn/0651c8d63ad8469c9f7b2647e7305808.png" alt="在这里插入图片描述">

## 参考资料
- 