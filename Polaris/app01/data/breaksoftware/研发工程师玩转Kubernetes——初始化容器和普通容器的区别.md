
--- 
title:  研发工程师玩转Kubernetes——初始化容器和普通容器的区别 
tags: []
categories: [] 

---


#### 大纲
- - - 


在现实场景中，我们为了降低业务耦合，往往会将一个大大的功能拆解成若干独立的小功能。比如主要业务启动前，需要将其所依赖的各种资源都拉下来。一种做法是在一个Pod内完成上述两步操作，但是会导致业务逻辑不够独立；另外一种做法就是启动一个Pod专门用于拉取资源，待其完成后再启动业务Pod。

## 错误的示例

下面部署的Pod将启动3个容器。前两个运行的容器只在/data/whoami追加了一行文本后就退出了。

```
# common-container.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: common-container-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: common-container
  template:
    metadata:
      labels:
        app: common-container
    spec:
      containers:
      - name: common-container-1
        image: busybox
        command: ["/bin/sh", "-c", "echo \"this is init-common-container1\"; echo \"this is init-common-container-1\" &gt;&gt; /data/whoami"]
        volumeMounts:
        - name: emptydir-volume
          mountPath: /data
      - name: common-container-2
        image: busybox
        command: ["/bin/sh", "-c", "echo \"this is init-common-container2\"; echo \"this is init-common-container-2\" &gt;&gt; /data/whoami"]
        volumeMounts:
        - name: emptydir-volume
          mountPath: /data
      - name: common-container
        image: busybox
        command: ["/bin/sh", "-c", "while true; do cat /data/whoami; sleep 5; done"]
        volumeMounts:
        - name: emptydir-volume
          mountPath: /data
      volumes:
      - name: emptydir-volume
        emptyDir: 
          medium: Memory
          sizeLimit: 1Gi

```

查看Pod状态，可以发现Pod因为前两个容器中脚本执行结束后，没有了前台进程，容器就退出了。进而导致Pod创建失败。

```
kubectl get pod

```

```
NAME                                           READY   STATUS             RESTARTS     AGE
common-container-deployment-5569564499-qchgq   1/3     CrashLoopBackOff   4 (7s ago)   40s

```

```
kubectl describe pod common-container-deployment-5569564499-qchgq 

```

```
……
Events:
  Type     Reason     Age                From               Message
  ----     ------     ----               ----               -------
  Normal   Scheduled  17s                default-scheduler  Successfully assigned default/common-container-deployment-5569564499-qchgq to ubuntub
  Normal   Pulled     15s                kubelet            Successfully pulled image "busybox" in 2.257083309s (2.257101009s including waiting)
  Normal   Pulled     13s                kubelet            Successfully pulled image "busybox" in 2.260848562s (2.260857362s including waiting)
  Normal   Pulling    13s                kubelet            Pulling image "busybox"
  Normal   Pulled     11s                kubelet            Successfully pulled image "busybox" in 1.989747468s (1.989754568s including waiting)
  Normal   Created    11s                kubelet            Created container common-container
  Normal   Started    10s                kubelet            Started container common-container
  Normal   Pulling    10s (x2 over 17s)  kubelet            Pulling image "busybox"
  Normal   Pulled     8s                 kubelet            Successfully pulled image "busybox" in 2.033723483s (2.033734083s including waiting)
  Normal   Created    8s (x2 over 15s)   kubelet            Created container common-container-1
  Normal   Started    8s (x2 over 15s)   kubelet            Started container common-container-1
  Normal   Pulling    8s (x2 over 15s)   kubelet            Pulling image "busybox"
  Normal   Pulled     6s                 kubelet            Successfully pulled image "busybox" in 2.032193623s (2.032200723s including waiting)
  Normal   Created    6s (x2 over 13s)   kubelet            Created container common-container-2
  Normal   Started    6s (x2 over 13s)   kubelet            Started container common-container-2
  Warning  BackOff    4s (x2 over 5s)    kubelet            Back-off restarting failed container common-container-1 in pod common-container-deployment-5569564499-qchgq_default(fd19ae72-5fd0-420d-9931-0d976175cf77)
  Warning  BackOff    4s (x2 over 5s)    kubelet            Back-off restarting failed container common-container-2 in pod common-container-deployment-5569564499-qchgq_default(fd19ae72-5fd0-420d-9931-0d976175cf77)

```

## 正确的示例

我们将需要一次性运行结束后可以退出的容器使用initContainers描述。

```
# init_container.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: init-container
spec:
  replicas: 1
  selector:
    matchLabels:
      app: init-container
  template:
    metadata:
      labels:
        app: init-container
    spec:
      initContainers:
      - name: init-container-1
        image: busybox
        command: ["/bin/sh", "-c", "echo \"this is init-container-1\"; echo \"this is init-container-1\" &gt;&gt; /data/whoami"]
        volumeMounts:
        - name: emptydir-volume
          mountPath: /data
      - name: init-container-2
        image: busybox
        command: ["/bin/sh", "-c", "echo \"this is init-container-2\"; echo \"this is init-container-2\" &gt;&gt; /data/whoami"]
        volumeMounts:
        - name: emptydir-volume
          mountPath: /data
      containers:
      - name: init-container
        image: busybox
        command: ["/bin/sh", "-c", "while true; do cat /data/whoami; sleep 5; done"]
        volumeMounts:
        - name: emptydir-volume
          mountPath: /data
      volumes:
      - name: emptydir-volume
        emptyDir: 
          medium: Memory
          sizeLimit: 1Gi

```

查看Pod状态，可以发现已处于运行状态。说明Pod创建成功了。

```
kubectl get pod

```

```
NAME                              READY   STATUS    RESTARTS   AGE
init-container-55c6d46676-5knwk   1/1     Running   0          33s

```

使用initContainers描述的容器已经无法连接，只有最后一个有前台程序的容器在运行。

```
kubectl logs pods/init-container-55c6d46676-5knwk init-container1

```

>  
 error: container init-container1 is not valid for pod init-container-55c6d46676-5knwk 


```
 kubectl logs pods/init-container-55c6d46676-5knwk init-container2

```

>  
 error: container init-container2 is not valid for pod init-container-55c6d46676-5knwk 


```
kubectl logs pods/init-container-55c6d46676-5knwk init-container

```

>  
 this is init-container-1 this is init-container-2 


## 总结

初始化容器用于运行一次就可以退出的业务场景，而普通容器则要一直有前台程序在运行。
