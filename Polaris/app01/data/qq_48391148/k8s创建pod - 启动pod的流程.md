
--- 
title:  k8s创建pod - 启动pod的流程 
tags: []
categories: [] 

---
**目录**



















































## 知识点一：启动一个pod

###  1、使用命令启动一个nginx pod

>  
 **deployment 控制器：专门负责在k8s里安装部署pod** 
 **kubectl create deployment  ：创建部署****控制器** 
 **k8s-nginx ：是****控制器****的名字** 
 **--image=nginx ：指定控制器去启动pod使用的镜像** 
 **-r 3  ：启动3个nginx的pod** 
 **副本控制器replicaSET（rs）：作用就是监控pod副本的数量，如果某个node节点挂了，这个节点上的pod也会挂，副本控制器就会在其他的node节点上启动新的pod，数量总数达到副本控制器当时设置的数量 -- 》高可用的体现** 


```
[root@k8s-master ~]# kubectl create deployment k8s-nginx --image=nginx -r 3
deployment.apps/k8s-nginx created
[root@k8s-master ~]# kubectl get pod
NAME                         READY   STATUS    RESTARTS   AGE
k8s-nginx-6d779d947c-58j42   1/1     Running   0          114s
k8s-nginx-6d779d947c-mphkp   1/1     Running   0          114s
k8s-nginx-6d779d947c-zwplb   1/1     Running   0          114s
[root@k8s-master ~]# kubectl get deploy
NAME        READY   UP-TO-DATE   AVAILABLE   AGE
k8s-nginx   3/3     3            3           3m10s
[root@k8s-master ~]# kubectl get pod -o wide
NAME                         READY   STATUS    RESTARTS   AGE   IP           NODE        NOMINATED NODE   READINESS GATES
k8s-nginx-6d779d947c-58j42   1/1     Running   0          13m   10.244.1.2   k8s-node1   &lt;none&gt;           &lt;none&gt;
k8s-nginx-6d779d947c-mphkp   1/1     Running   0          13m   10.244.2.2   k8s-node2   &lt;none&gt;           &lt;none&gt;
k8s-nginx-6d779d947c-zwplb   1/1     Running   0          13m   10.244.3.4   k8s-node3   &lt;none&gt;           &lt;none&gt;

```

 **##########################################################################################** 

#### 1.1、访问刚才创建的pod的nginx服务

目前只能在内部访问pod的nginx服务，因为还没有将它发布出去，10.244网段是k8s内部的网段

```
[root@k8s-master ~]# curl 10.244.1.2
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
&lt;title&gt;Welcome to nginx!&lt;/title&gt;
&lt;style&gt;
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
&lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;h1&gt;Welcome to nginx!&lt;/h1&gt;
&lt;p&gt;If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.&lt;/p&gt;

&lt;p&gt;For online documentation and support please refer to
&lt;a href="http://nginx.org/"&gt;nginx.org&lt;/a&gt;.&lt;br/&gt;
Commercial support is available at
&lt;a href="http://nginx.com/"&gt;nginx.com&lt;/a&gt;.&lt;/p&gt;

&lt;p&gt;&lt;em&gt;Thank you for using nginx.&lt;/em&gt;&lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;

```

 **##########################################################################################** 

####  1.2、删除deployment

```
[root@k8s-master ~]# kubectl get deploy
NAME        READY   UP-TO-DATE   AVAILABLE   AGE
k8s-nginx   3/3     3            3           18h
[root@k8s-master ~]# kubectl get pod
NAME                         READY   STATUS    RESTARTS   AGE
k8s-nginx-6d779d947c-58j42   1/1     Running   0          18h
k8s-nginx-6d779d947c-mphkp   1/1     Running   0          18h
k8s-nginx-6d779d947c-zwplb   1/1     Running   0          18h
[root@k8s-master ~]# kubectl delete deployment  k8s-nginx
deployment.apps "k8s-nginx" deleted
[root@k8s-master ~]# kubectl get deploy
No resources found in default namespace.
[root@k8s-master ~]# kubectl get pod
No resources found in default namespace.

```

 **##########################################################################################** 

### 2、将pod里的服务发布出去

>  
 <h4 id="%C2%A0%E9%A6%96%E5%85%88%E5%88%9B%E5%BB%BA%E6%A0%B9%E6%8D%AEyaml%E6%96%87%E4%BB%B6%E5%88%9B%E5%BB%BApod">** 首先创建根据yaml文件创建pod**</h4> 


yaml文件：

```
[root@k8s-master pod]# cat my_nginx.yaml 
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-nginx
spec:
  selector:
    matchLabels:
      run: my-nginx
  replicas: 3
  template:
    metadata:
      labels:
        run: my-nginx
    spec:
      containers:
      - name: my-nginx
        image: nginx
        ports:
        - containerPort: 80

```

```
[root@k8s-master pod]# kubectl apply -f my_nginx.yaml 
deployment.apps/my-nginx created
[root@k8s-master pod]# kubectl get deploy
NAME       READY   UP-TO-DATE   AVAILABLE   AGE
my-nginx   3/3     3            3           12s
[root@k8s-master pod]# kubectl get pod -o wide
NAME                       READY   STATUS    RESTARTS   AGE   IP           NODE        NOMINATED NODE   READINESS GATES
my-nginx-cf54cdbf7-5tnfx   1/1     Running   0          24s   10.244.1.5   k8s-node1   &lt;none&gt;           &lt;none&gt;
my-nginx-cf54cdbf7-c8wbq   1/1     Running   0          24s   10.244.2.6   k8s-node2   &lt;none&gt;           &lt;none&gt;
my-nginx-cf54cdbf7-rhqcv   1/1     Running   0          24s   10.244.3.7   k8s-node3   &lt;none&gt;           &lt;none&gt;

```

 **##########################################################################################** 

####  2.1、创建Service

my_service.yaml内容：

```
apiVersion: v1
kind: Service
metadata:
  name: my-nginx
  labels:
    run: my-nginx
spec:
  type: NodePort
  ports:
  - port: 8080
    targetPort: 80
    protocol: TCP
    name: http
  selector:
    run: my-nginx
```

 创建service

```
[root@k8s-master pod]# kubectl apply -f my_service.yaml 
service/my-nginx created
[root@k8s-master pod]# kubectl get service
NAME         TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)          AGE
kubernetes   ClusterIP   10.1.0.1      &lt;none&gt;        443/TCP          24h
my-nginx     NodePort    10.1.20.144   &lt;none&gt;        8080:32697/TCP   5s

```

 **##########################################################################################** 

#### 2.2、访问发布的pod

我们只要随便访问k8s几区任何一台node节点服务器，包括master

<img alt="" height="457" src="https://img-blog.csdnimg.cn/c1c92387895244fe8fec1ccd0b279e5e.png" width="1200">

<img alt="" height="432" src="https://img-blog.csdnimg.cn/43bd11f85dd046a28c03b6b1024b7135.png" width="1200">





**##########################################################################################** 

###  3、利用yaml文件创建pod

以下是nginx-pod.yaml文件内容

```
apiVersion: v1   # k8s的api版本 --》用来给k8s传递参数
kind: Pod        # k8s的资源对象类型：pod，deployment，replicaSET，daemonSET
metadata:        # 定义的元数据，描述数据
  name: sc-nginx    # pod的名字
spec:            # 详细信息，指定的信息
  containers:    # 容器
  - name: nginx  # 容器名字
    image: nginx:1.14.2     #容器镜像版本
    ports:       # 端口
    - containerPort: 80
```

 **##########################################################################################** 

#### 3.1、根据yaml文件启动pod

```
[root@k8s-master ~]# vim nginx-pod.yaml 
[root@k8s-master ~]# kubectl apply -f nginx-pod.yaml 
pod/sc-nginx created
[root@k8s-master ~]# kubectl get pod -o wide
NAME       READY   STATUS    RESTARTS   AGE   IP           NODE        NOMINATED NODE   READINESS GATES
sc-nginx   1/1     Running   0          80s   10.244.2.3   k8s-node2   &lt;none&gt;           &lt;none&gt;

```

#### 3.2、删除pod

```
[root@k8s-master ~]# kubectl delete pod sc-nginx
pod "sc-nginx" deleted
[root@k8s-master ~]# kubectl get pod
No resources found in default namespace.

```

**##########################################################################################** 

### 4、pod的几种状态 

>  
 **Pending（悬决）        pod已经被kubernetes系统接受，但有一个或者多个容器尚未创建，亦未运行，可以通过kubectl describe 查看处于 Pending 状态的原因** 
 **Running （运行中）        Pod已经绑定到了某个节点，Pod中所有容器都已被创建，至少有一个容器任在运行** 
 **Successed （成功）        Pod中的所有容器都已经执行成功并终止，并且不会再重启** 
 **Failed （失败）        Pod中所有容器都终止，并且至少有一个容器是因为失败终止** 
 **Unknown （未知）         因为某些原因无法取得Pod的状态，通常是因为与Pod所在主机通信失败** 


```
[root@k8s-master ~]# kubectl get  pod -n kube-system
NAME                                 READY   STATUS             RESTARTS         AGE
coredns-6d8c4cb4d-92g7b              0/1     CrashLoopBackOff   32 (3m44s ago)   2d23h
coredns-6d8c4cb4d-kl4q5              0/1     CrashLoopBackOff   32 (3m44s ago)   2d23h
etcd-k8s-master                      1/1     Running            0                2d23h
kube-apiserver-k8s-master            1/1     Running            0                2d23h
kube-controller-manager-k8s-master   1/1     Running            0                2d23h
kube-proxy-422b5                     1/1     Running            0                2d23h
kube-proxy-6qpcz                     1/1     Running            0                2d23h
kube-proxy-ggnnt                     1/1     Running            0                2d23h
kube-proxy-vjcnc                     1/1     Running            0                2d23h
kube-scheduler-k8s-master            1/1     Running            0                2d23h

```

**##########################################################################################**

## 知识点二：启动pod的流程



 <img alt="" height="563" src="https://img-blog.csdnimg.cn/3d14456a74c148fe80fd73226c8b2ea4.png" width="897">

>  
 **用户通过kubectl提交pod创建指令，这个指令可以是命令也可以是yaml文件，yaml文件里面指定了很多关于pod的参数，例如名字，镜像，版本等** 
 **pod创建指令信息传给API Server，API Server将Pod信息存入etcd** 
 **Controller Manager控制器通过API Server接口发现pod信息的更新，做编排工作，创建应用锁需要的pod，并将创建信息返回给API Server，API Server再将pod信息更新到etcd** 
 **Scheduler通过API Server中新pod信息的变化，就会为pod分配一个节点Node，并将分配结果反馈给API Server，API Server再将Pod信息存到etcd** 
 **API Server通知对应节点的kubelet，kubelet发现Pod调度到本节点，通过容器（例如docker）创建并运行Pod的容器** 
 **Kube-proxy给pod分配网络资源，包括服务的发布以及负载均衡的配置** 


 **##########################################################################################**

##  知识点三：pod有哪些调度算法

>  
 **根据pod调度策略和方法** 
 **1、deployment：全自动调度，根据node的算力（cpu，内存，带宽，已经运行的pod等）** 
 **2、node selector：定向调度** 
 **3、nodeaffinity：  尽量把不同的pod放到一台node上** 
 **4、podaffinity：    尽量把相同的pod放到一起** 
 **5、taints和tolerations：污点和容忍** 


### 1、 kubectl describe node k8s-master  输出一个node的详细信息

```
[root@k8s-master ~]# kubectl describe node k8s-master
Name:               k8s-master
Roles:              control-plane,master
Labels:             beta.kubernetes.io/arch=amd64
                    beta.kubernetes.io/os=linux
                    kubernetes.io/arch=amd64
                    kubernetes.io/hostname=k8s-master
                    kubernetes.io/os=linux
                    node-role.kubernetes.io/control-plane=
                    node-role.kubernetes.io/master=
                    node.kubernetes.io/exclude-from-external-load-balancers=
Annotations:        flannel.alpha.coreos.com/backend-data: {"VNI":1,"VtepMAC":"fe:ca:d8:cc:01:2e"}
                    flannel.alpha.coreos.com/backend-type: vxlan
                    flannel.alpha.coreos.com/kube-subnet-manager: true
                    flannel.alpha.coreos.com/public-ip: 192.168.44.210
                    kubeadm.alpha.kubernetes.io/cri-socket: /var/run/dockershim.sock
                    node.alpha.kubernetes.io/ttl: 0
                    volumes.kubernetes.io/controller-managed-attach-detach: true
CreationTimestamp:  Sun, 25 Sep 2022 18:20:27 +0800
Taints:             node-role.kubernetes.io/master:NoSchedule
Unschedulable:      false
Lease:
  HolderIdentity:  k8s-master
  AcquireTime:     &lt;unset&gt;
  RenewTime:       Wed, 28 Sep 2022 17:36:36 +0800
Conditions:
  Type                 Status  LastHeartbeatTime                 LastTransitionTime                Reason                       Message
  ----                 ------  -----------------                 ------------------                ------                       -------
  NetworkUnavailable   False   Sun, 25 Sep 2022 18:33:20 +0800   Sun, 25 Sep 2022 18:33:20 +0800   FlannelIsUp                  Flannel is running on this node
  MemoryPressure       False   Wed, 28 Sep 2022 17:33:08 +0800   Sun, 25 Sep 2022 18:20:26 +0800   KubeletHasSufficientMemory   kubelet has sufficient memory available
  DiskPressure         False   Wed, 28 Sep 2022 17:33:08 +0800   Sun, 25 Sep 2022 18:20:26 +0800   KubeletHasNoDiskPressure     kubelet has no disk pressure
  PIDPressure          False   Wed, 28 Sep 2022 17:33:08 +0800   Sun, 25 Sep 2022 18:20:26 +0800   KubeletHasSufficientPID      kubelet has sufficient PID available
  Ready                True    Wed, 28 Sep 2022 17:33:08 +0800   Sun, 25 Sep 2022 18:33:28 +0800   KubeletReady                 kubelet is posting ready status
Addresses:
  InternalIP:  192.168.44.210
  Hostname:    k8s-master
Capacity:
  cpu:                4
  ephemeral-storage:  17394Mi
  hugepages-1Gi:      0
  hugepages-2Mi:      0
  memory:             1863028Ki
  pods:               110
Allocatable:
  cpu:                4
  ephemeral-storage:  16415037823
  hugepages-1Gi:      0
  hugepages-2Mi:      0
  memory:             1760628Ki
  pods:               110
System Info:
  Machine ID:                 6d6ca2c7ec0f478097733b00d2892ca0
  System UUID:                0A004D56-3924-4215-F717-9E4DAD9C840B
  Boot ID:                    dd78d95d-a6e7-460e-892b-8d4cf8191823
  Kernel Version:             3.10.0-1160.el7.x86_64
  OS Image:                   CentOS Linux 7 (Core)
  Operating System:           linux
  Architecture:               amd64
  Container Runtime Version:  docker://20.10.18
  Kubelet Version:            v1.23.6
  Kube-Proxy Version:         v1.23.6
PodCIDR:                      10.244.0.0/24
PodCIDRs:                     10.244.0.0/24
Non-terminated Pods:          (6 in total)
  Namespace                   Name                                  CPU Requests  CPU Limits  Memory Requests  Memory Limits  Age
  ---------                   ----                                  ------------  ----------  ---------------  -------------  ---
  kube-flannel                kube-flannel-ds-rphnc                 100m (2%)     100m (2%)   50Mi (2%)        50Mi (2%)      2d23h
  kube-system                 etcd-k8s-master                       100m (2%)     0 (0%)      100Mi (5%)       0 (0%)         2d23h
  kube-system                 kube-apiserver-k8s-master             250m (6%)     0 (0%)      0 (0%)           0 (0%)         2d23h
  kube-system                 kube-controller-manager-k8s-master    200m (5%)     0 (0%)      0 (0%)           0 (0%)         2d23h
  kube-system                 kube-proxy-ggnnt                      0 (0%)        0 (0%)      0 (0%)           0 (0%)         2d23h
  kube-system                 kube-scheduler-k8s-master             100m (2%)     0 (0%)      0 (0%)           0 (0%)         2d23h
Allocated resources:
  (Total limits may be over 100 percent, i.e., overcommitted.)
  Resource           Requests    Limits
  --------           --------    ------
  cpu                750m (18%)  100m (2%)
  memory             150Mi (8%)  50Mi (2%)
  ephemeral-storage  0 (0%)      0 (0%)
  hugepages-1Gi      0 (0%)      0 (0%)
  hugepages-2Mi      0 (0%)      0 (0%)
Events:              &lt;none&gt;

```

 **##########################################################################################** 

###  2、pod的重启策略

>  
 **always ：当容器失败时，由kubelet自动重启该容器** 
 **OnFailure ：当容器终止运行且退出码为0时，由kubelet自动重启该容器** 
 **Never ：不论容器运行状态如何，kubelet都不会重启该容器** 


 **##########################################################################################**

##  知识点四：pod的通信方式

**kubernetes 的网络模型假定了所有Pod都在一个可以直接连通的扁平的网络空间中，kubernetes假定这个网络已经存在，**

 **##########################################################################################**

## 知识点五：k8s的各种控制器

### 1、k8s里面有哪些控制器？

>  
 **deployment** 
 **replicaSET** 
 **daemonSET** 


#### 1.1、ReplicaSET 副本控制器 

>  
 **ReplicaSET 副本控制器，用来确保容器应用的副本数始终保持在用户定义的副本数，即如果有容器异常退出，会自动创建新的pod来替代，而如果异常出来的容器也会自动回收** 


#### 1.2、DaemonSet 

>  
 **Daemon确保全部node（或者一些）上运行一个pod的副本，当有node加入集群时，也会为他们新增一个pod，当有node从集群移除时，这些pod也会被回收，删除DaemonSet会删除它创建的所有pod** 


####  1.3、Job

>  
 **Job负责批处理任务，即仅执行一次的任务，它保证批处理任务的一个或多个Pod成功结束** 


 **##########################################################################################**

#### 2、deployment，replicaSET，pod的关系

<img alt="" height="602" src="https://img-blog.csdnimg.cn/5283e7cea4df4c949f22f6d0d3e34be1.png" width="605">

>  
 **首先部署一个deployment k8s-nginx，启动三个pod，pod里面运行nginx** 


```
[root@k8s-master ~]# kubectl create deployment k8s-nginx --image=nginx -r 3
deployment.apps/k8s-nginx created
[root@k8s-master ~]# kubectl get pod -o wide
NAME                         READY   STATUS    RESTARTS   AGE   IP           NODE        NOMINATED NODE   READINESS GATES
k8s-nginx-6d779d947c-hd64b   1/1     Running   0          21s   10.244.1.3   k8s-node1   &lt;none&gt;           &lt;none&gt;
k8s-nginx-6d779d947c-j9pkd   1/1     Running   0          21s   10.244.3.5   k8s-node3   &lt;none&gt;           &lt;none&gt;
k8s-nginx-6d779d947c-rf7tm   1/1     Running   0          21s   10.244.2.4   k8s-node2   &lt;none&gt;           &lt;none&gt;
[root@k8s-master ~]# kubectl get deploy
NAME        READY   UP-TO-DATE   AVAILABLE   AGE
k8s-nginx   3/3     3            3           27s
[root@k8s-master ~]# kubectl get replicaset
NAME                   DESIRED   CURRENT   READY   AGE
k8s-nginx-6d779d947c   3         3         3       41s


```

#### 2.1、既然pod是replicaSET启动的，那么删除replicaSET会发生什么？

```
[root@k8s-master ~]# kubectl delete replicaset k8s-nginx-6d779d947c
replicaset.apps "k8s-nginx-6d779d947c" deleted
[root@k8s-master ~]# kubectl get pod
NAME                         READY   STATUS    RESTARTS   AGE
k8s-nginx-6d779d947c-2xp8r   1/1     Running   0          7s
k8s-nginx-6d779d947c-gw5x8   1/1     Running   0          7s
k8s-nginx-6d779d947c-rmx9x   1/1     Running   0          7s
[root@k8s-master ~]# kubectl get rs
NAME                   DESIRED   CURRENT   READY   AGE
k8s-nginx-6d779d947c   3         3         3       12s

```

>  
 **可以看到，删除replicaSET以后，又会重新生成一个replicaSET副本控制器，因为replicaSET是由deployment部署的，所以replicaSET挂了以后又会重新生成** 
 **但是如果删除了deployment，无论是replicaSET，pod，都会被删除** 


 **##########################################################################################**


