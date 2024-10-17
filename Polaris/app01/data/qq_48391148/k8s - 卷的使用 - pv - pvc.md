
--- 
title:  k8s - 卷的使用 - pv - pvc 
tags: []
categories: [] 

---
**目录**



































## 知识点1：卷

**官方文档：**



### 为什么要使用卷来存储数据？

>  
 **Container 中的文件在磁盘上是临时存放的，这给 Container 中运行的较重要的应用程序带来一些问题。 问题之一是当容器崩溃时文件丢失。 kubelet 会重新启动容器，但容器会以干净的状态重启。 第二个问题会在同一 `Pod` 中运行多个容器并共享文件时出现。** 


>  
 **Kubernetes 支持很多类型的卷。  可以同时使用任意数目的卷类型。 临时卷类型的生命周期与 Pod 相同，但持久卷可以比 Pod 的存活期长。 当 Pod 不再存在时，Kubernetes 也会销毁临时卷；不过 Kubernetes 不会销毁持久卷。 对于给定 Pod 中任何类型的卷，在容器重启期间数据都不会丢失。** 
 **卷的核心是一个目录，其中可能存有数据，Pod 中的容器可以访问该目录中的数据。 所采用的特定的卷类型将决定该目录如何形成的、使用何种介质保存数据以及目录中存放的内容。** 


### k8s卷的类型

#### emptyDir

>  
 **当 Pod 分派到某个节点上时，`emptyDir` 卷会被创建，并且在 Pod 在该节点上运行期间，卷一直存在。 就像其名称表示的那样，卷最初是空的。 尽管 Pod 中的容器挂载 `emptyDir` 卷的路径可能相同也可能不同，这些容器都可以读写 `emptyDir` 卷中相同的文件。 当 Pod 因为某些原因被从节点上删除时，`emptyDir` 卷中的数据也会被永久删除。** 
 **说明： 容器崩溃并不会导致 Pod 被从节点上移除，因此容器崩溃期间 `emptyDir` 卷中的数据是安全的。** 


>  
 **`emptyDir` 的一些用途：** 
 - **缓存空间，例如基于磁盘的归并排序。**- **为耗时较长的计算任务提供检查点，以便任务能方便地从崩溃前状态恢复执行。**- **在 Web 服务器容器服务数据时，保存内容管理器容器获取的文件。** 


#### 示例：创建一个使用emptyDir的卷

```
apiVersion: v1
kind: Pod
metadata:
  name: test-pd
spec:
  containers:
  - image: registry.k8s.io/test-webserver
    name: test-container
    volumeMounts:
    - mountPath: /cache
      name: cache-volume
  volumes:
  - name: cache-volume
    emptyDir: {}
```

#### hostPath（默认文件挂载是以读写模式）

>  
 **`hostPath` 卷能将主机节点文件系统上的文件或目录挂载到你的 Pod 中。 虽然这不是大多数 Pod 需要的，但是它为一些应用程序提供了强大的逃生舱。** 
 **例如，`hostPath` 的一些用法有：** 
 - **运行一个需要访问 Docker 内部机制的容器；可使用 `hostPath` 挂载 `/var/lib/docker` 路径。**- **在容器中运行 cAdvisor 时，以 `hostPath` 方式挂载 `/sys`。**- **允许 Pod 指定给定的 `hostPath` 在运行 Pod 之前是否应该存在，是否应该创建以及应该以什么方式存在。** 
 **除了必需的 `path` 属性之外，你可以选择性地为 `hostPath` 卷指定 `type`。** 
 **支持的 `type` 值如下：** 
 ** **<img alt="" height="617" src="https://img-blog.csdnimg.cn/77eb7dc499b54254b2dbb2169f321af3.png" width="1200"> 
  


 示例：使用hostPath方式创建一个pod

```
[root@k8s-master storage]# vim volume.yaml
apiVersion: v1
kind: Pod
metadata:
  name: test-pd
spec:
  containers:
  - image: nginx
    name: test-container
    volumeMounts:
    - mountPath: /test-pd
      name: test-volume
  volumes:
  - name: test-volume
    hostPath:
      # 宿主上目录位置
      path: /data
      # 此字段为可选
      type: Directory

```

>  
 **因为要挂载在宿主机上面，使用的type是Directlory，所以要先在宿主机上面新建一个目录** 


```
[root@k8s-master /]# mkdir /data -p
[root@k8s-master /]# ls
bin  boot  data  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var

```

>  
 **因为是起的pod是被调度在node3节点上，所以node3节点上要有/data这个目录，不然无法挂载** 


```
[root@k8s-master storage]# kubectl apply -f volume.yaml 
pod/test-pd created
[root@k8s-master storage]# kubectl get pod -o wide
NAME                          READY   STATUS    RESTARTS   AGE   IP            NODE        NOMINATED NODE   READINESS GATES
php-apache-7c97954b84-77fgv   1/1     Running   0          22h   10.244.1.13   k8s-node1   &lt;none&gt;           &lt;none&gt;
redis                         1/1     Running   0          18h   10.244.2.9    k8s-node2   &lt;none&gt;           &lt;none&gt;
test-pd                       1/1     Running   0          5s    10.244.3.15   k8s-node3   &lt;none&gt;           &lt;none&gt;

```

>  
 **进入pod内部，看看是否有test-pd这个目录** 


```
[root@k8s-master storage]# kubectl exec -it test-pd bash
kubectl exec [POD] [COMMAND] is DEPRECATED and will be removed in a future version. Use kubectl exec [POD] -- [COMMAND] instead.
root@test-pd:/# ls
bin   dev		   docker-entrypoint.sh  home  lib64  mnt  proc  run   srv  test-pd  usr
boot  docker-entrypoint.d  etc			 lib   media  opt  root  sbin  sys  tmp      var
root@test-pd:/# cd test-pd/
root@test-pd:/test-pd# ls
root@test-pd:/test-pd# echo "123456" &gt; test.txt
root@test-pd:/test-pd# ls
test.txt
root@test-pd:/test-pd# 

```

>  
 **在pod内部创建一个文件，输入123456，发现宿主机k8s-node3上的/data挂载目录页有了内容** 


```
[root@k8s-node3 ~]# cd /data/
[root@k8s-node3 data]# ls
test.txt
[root@k8s-node3 data]# cat test.txt 
123456
[root@k8s-node3 data]# 

```

#### 使用DirectoryOrCreate类型挂载卷

>  
 **DirectoryOrCreate：如果在给定路径上什么都不存在，那么将根据需要创建空目录，权限设置为 0755，具有与 kubelet 相同的组和属主信息。** 


```
[root@k8s-master storage]# vim volume2.yaml
apiVersion: v1
kind: Pod
metadata:
  name: test-pd2
spec:
  containers:
  - image: nginx
    name: test-container
    volumeMounts:
    - mountPath: /test-pd2
      name: test-volume2
  volumes:
  - name: test-volume2
    hostPath:
      # 宿主上目录位置
      path: /data2
      # 此字段为可选
      type: DirectoryOrCreate

```

```
[root@k8s-master storage]# kubectl apply -f volume2.yaml 
pod/test-pd2 created
[root@k8s-master storage]# kubectl get pod -o wide
NAME                          READY   STATUS              RESTARTS   AGE   IP            NODE        NOMINATED NODE   READINESS GATES
php-apache-7c97954b84-77fgv   1/1     Running             0          22h   10.244.1.13   k8s-node1   &lt;none&gt;           &lt;none&gt;
redis                         1/1     Running             0          19h   10.244.2.9    k8s-node2   &lt;none&gt;           &lt;none&gt;
test-pd                       1/1     Running             0          10m   10.244.3.15   k8s-node3   &lt;none&gt;           &lt;none&gt;
test-pd2                      0/1     ContainerCreating   0          6s    &lt;none&gt;        k8s-node1   &lt;none&gt;           &lt;none&gt;
[root@k8s-master storage]# kubectl get pod -o wide
NAME                          READY   STATUS    RESTARTS   AGE   IP            NODE        NOMINATED NODE   READINESS GATES
php-apache-7c97954b84-77fgv   1/1     Running   0          22h   10.244.1.13   k8s-node1   &lt;none&gt;           &lt;none&gt;
redis                         1/1     Running   0          19h   10.244.2.9    k8s-node2   &lt;none&gt;           &lt;none&gt;
test-pd                       1/1     Running   0          11m   10.244.3.15   k8s-node3   &lt;none&gt;           &lt;none&gt;
test-pd2                      1/1     Running   0          37s   10.244.1.16   k8s-node1   &lt;none&gt;           &lt;none&gt;
[root@k8s-master storage]# 

```

>  
 **进入容器内部，验证挂载目录是否存在** 


```
[root@k8s-master storage]# kubectl exec -it test-pd2 bash
kubectl exec [POD] [COMMAND] is DEPRECATED and will be removed in a future version. Use kubectl exec [POD] -- [COMMAND] instead.
root@test-pd2:/# ls
bin   dev		   docker-entrypoint.sh  home  lib64  mnt  proc  run   srv  test-pd2  usr
boot  docker-entrypoint.d  etc			 lib   media  opt  root  sbin  sys  tmp       var
root@test-pd2:/# cd test-pd2/
root@test-pd2:/test-pd2# echo "hello,world" &gt; test2.txt
root@test-pd2:/test-pd2# ls
test2.txt
root@test-pd2:/test-pd2# 

```

```
[root@k8s-node1 ~]# cd /
[root@k8s-node1 /]# ls
bin   data2  etc   lib    media  opt   root  sbin  sys  usr
boot  dev    home  lib64  mnt    proc  run   srv   tmp  var
[root@k8s-node1 /]# cd data2/
[root@k8s-node1 data2]# ls
test2.txt
[root@k8s-node1 data2]# cat test2.txt 
hello,world
[root@k8s-node1 data2]# 
```

**############################################################################**

## 知识点2：pv和pvc

### 什么是pv和pvc？

>  
 - **PV : 持久化卷的意思，是对底层的共享存储的一种抽象** 
 - **PVC（Persistent Volume Claim）是持久卷请求于存储需求的一种声明(PVC其实就是用户向kubernetes系统发出的一种资源需求申请。)** 


>  
 **PVC的使用逻辑：在pod中定义一个存储卷（该存储卷类型为PVC），定义的时候直接指定大小，pvc必须与对应的pv建立关系，pvc会根据定义去pv申请，而pv是由存储空间创建出来的。pv和pvc是kubernetes抽象出来的一种存储资源。** 


#### pv的状态：

<img alt="" height="311" src="https://img-blog.csdnimg.cn/a9668ddd2a7f4e89a6e8a5bed0b11180.png" width="1073"> 

#### pv的访问模式（accessModes）

<img alt="" height="359" src="https://img-blog.csdnimg.cn/7816282997854490bdbead0f1325008d.png" width="1078"> 

 

 **############################################################################**

**官方文档：**



### 配置 Pod 以使用 PersistentVolume 作为存储

#### 1、首先在所有节点上创建一个/sc/data/index.html文件

>  
 **因为不知道创建的pod会被调度到哪一台机器上面，所以我们在所有节点上都创建这个文件** 


```
[root@k8s-master ~]# mkdir /sc/data -p
[root@k8s-master ~]# cd /sc/data/
[root@k8s-master data]# ls
[root@k8s-master data]# sh -c "echo 'Hello from Kubernetes storage' &gt; /sc/data/index.html"
[root@k8s-master data]# ls
index.html
[root@k8s-master data]# cat index.html 
Hello from Kubernetes storage

```

**############################################################################** 

####  2、创建PersistentVolume

```
[root@k8s-master pv]# vim pv-volume.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: task-pv-volume
  labels:
    type: local
spec:
  storageClassName: manual
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/sc/data"

```

>  
 **应用yaml文件，创建成功后查看pv信息** 


```
[root@k8s-master pv]# kubectl apply -f  pv-volume.yaml 
persistentvolume/task-pv-volume created
[root@k8s-master pv]# kubectl get pv
NAME             CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS      CLAIM   STORAGECLASS   REASON   AGE
task-pv-volume   10Gi       RWO            Retain           Available           manual                  8s

```

**############################################################################** 

#### 3、创建PersistentVolumeClaim

>  
 **下一步是创建一个 PersistentVolumeClaim。 Pod 使用 PersistentVolumeClaim 来请求物理存储。** 


>  
 **PVC的使用逻辑：在pod中定义一个存储卷（该存储卷类型为PVC），定义的时候直接指定大小，pvc必须与对应的pv建立关系，pvc会根据定义去pv申请，而pv是由存储空间创建出来的。pv和pvc是kubernetes抽象出来的一种存储资源。 ** 


```
[root@k8s-master pv]# vim pv-claim.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: task-pv-claim
spec:
  storageClassName: manual
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 3Gi
```

>  
 **应用yaml文件，创建成功后查看pv信息** 


```
[root@k8s-master pv]# kubectl apply -f pv-claim.yaml 
persistentvolumeclaim/task-pv-claim created
[root@k8s-master pv]# kubectl get pvc
NAME            STATUS   VOLUME           CAPACITY   ACCESS MODES   STORAGECLASS   AGE
task-pv-claim   Bound    task-pv-volume   10Gi       RWO            manual         6s

```

####  4、创建 Pod

>  
 **下一步是创建一个使用你的 PersistentVolumeClaim 作为存储卷的 Pod。** 


```
[root@k8s-master pv]# vim pv-pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: task-pv-pod
spec:
  volumes:
    - name: task-pv-storage
      persistentVolumeClaim:
        claimName: task-pv-claim
  containers:
    - name: task-pv-container
      image: nginx
      ports:
        - containerPort: 80
          name: "http-server"
      volumeMounts:
        - mountPath: "/usr/share/nginx/html"
          name: task-pv-storage
```

>  
 **应用yaml文件，创建成功后查看pod信息** 


```
[root@k8s-master pv]# kubectl apply -f pv-pod.yaml 
pod/task-pv-pod created
[root@k8s-master pv]# kubectl get pod -o wide
NAME                          READY   STATUS    RESTARTS   AGE   IP            NODE        NOMINATED NODE   READINESS GATES
php-apache-7c97954b84-77fgv   1/1     Running   0          45h   10.244.1.13   k8s-node1   &lt;none&gt;           &lt;none&gt;
redis                         1/1     Running   0          41h   10.244.2.9    k8s-node2   &lt;none&gt;           &lt;none&gt;
task-pv-pod                   1/1     Running   0          77s   10.244.3.14   k8s-node3   &lt;none&gt;           &lt;none&gt;


```

>  
 **进入pod内部，查看/usr/share/nginx/html是否是使用的我们/sc/data/index.html文件** 


```
[root@k8s-master pv]# kubectl exec -it task-pv-pod bash
kubectl exec [POD] [COMMAND] is DEPRECATED and will be removed in a future version. Use kubectl exec [POD] -- [COMMAND] instead.
root@task-pv-pod:/# cd /usr/share/nginx/html/
root@task-pv-pod:/usr/share/nginx/html# ls
index.html
root@task-pv-pod:/usr/share/nginx/html# cat index.html 
Hello from Kubernetes storage

```

<img alt="" height="531" src="https://img-blog.csdnimg.cn/26e34ad9365247c3b80709b8c3d3a24b.png" width="922"> 

 **############################################################################**
