
--- 
title:  k8s - 容器类型 - logrotate日志轮转工具 - HPA的部署 - Dashboard安装部署 
tags: []
categories: [] 

---
**目录**



































































## 知识点1：容器类型

### 1.1、init初始化容器

**官方文档：**

 

>  
 **Init 容器是一种特殊容器，在 <strong>** 内的应用容器启动之前运行。Init 容器可以包括一些应用镜像中不存在的实用工具和安装脚本。</strong>  
 **Init 容器和应用容器都在一个Pod里面，它们共享同一个命名空间。** 


怎样理解init容器？

>  
 **每个  中可以包含多个容器， 应用运行在这些容器里面，同时 Pod 也可以有一个或多个先于应用容器启动的 Init 容器。** 
 **Init 容器与普通的容器非常像，除了如下两点：** 
 - **它们总是运行到完成。**- **每个都必须在下一个启动之前成功完成。** 
 **如果 Pod 的 Init 容器失败，kubelet 会不断地重启该 Init 容器直到该容器成功为止。 然而，如果 Pod 对应的 `restartPolicy` 值为 "Never"，并且 Pod 的 Init 容器失败， 则 Kubernetes 会将整个 Pod 状态设置为失败。** 


**################################################################### **

###  1.2、pause容器

>  
 **每个Pod里运行着一个特殊的被称之为Pause的容器，其他容器则为业务容器，这些业务容器共享Pause容器的网络栈和Volume挂载卷， ** 
 **pause容器是在创建一个pod的时候，最先创建的容器** 
 **pause会将Pod的公用命名空间都创建好** 


<img alt="" height="216" src="https://img-blog.csdnimg.cn/c37fe50d7d854376ac257af3103fd6eb.png" width="836">

<img alt="" height="812" src="https://img-blog.csdnimg.cn/65368bb15dd94223bfe821253b15e17f.png" width="1085">

 **################################################################### **

###  1.3、app容器

>  
 **app容器就是跑业务代码的容器** 


 **################################################################### ** 

###  1.4、logrotate 日志轮转工具

>  
 **logrorate日志轮转工具是linux系统自带的程序，不是一直在内存里运行的守护进程** 
 **计划任务会定时启动logrotate进行日志轮转** 


#### 配置文件：/etc/logrotate.conf

<img alt="" height="714" src="https://img-blog.csdnimg.cn/8dd459ef64984dcd9c8552891d94dde2.png" width="906">

####  /etc/logrotate.d目录：

```
[root@k8s-master log]# cd /etc/logrotate.d/
[root@k8s-master logrotate.d]# ls
bootlog  chrony  firewalld  syslog  wpa_supplicant  yum
[root@k8s-master logrotate.d]# cat bootlog 
/var/log/boot.log
{
    missingok
    daily
    copytruncate
    rotate 7
    notifempty
}
[root@k8s-master logrotate.d]# 

```

>  
 **示例：bootlog 配置文件的作用就是告诉logrotate按照它的要求进行日志轮转** 


#### 日志轮转的好处：

>  
 **防止一个日志文件过大，对日志分析的时候不便，读取某天的日志，很难去定位，需要去查找的数据量很大**  


  **################################################################### ** 

## 知识点2：HPA和VPA的区别

### 2.1：HPA水平扩缩

官方文档：



>  
 **在 Kubernetes 中，**HorizontalPodAutoscaler** 自动更新工作负载资源 （例如  或者 ）， 目的是自动扩缩工作负载以满足需求。** 
 **水平扩缩意味着对增加的负载的响应是部署更多的 。 这与 “垂直（Vertical）” 扩缩不同，对于 Kubernetes， 垂直扩缩意味着将更多资源（例如：内存或 CPU）分配给已经为工作负载运行的 Pod。** 
 **如果负载减少，并且 Pod 的数量高于配置的最小值， HorizontalPodAutoscaler 会指示工作负载资源（ Deployment、StatefulSet 或其他类似资源）缩减。** 
 **水平 Pod 自动扩缩不适用于无法扩缩的对象（例如：。）** 
 **HorizontalPodAutoscaler 被实现为 Kubernetes API 资源和。** 
 **资源决定了控制器的行为。在 Kubernetes 内运行的水平 Pod 自动扩缩控制器会定期调整其目标（例如：Deployment）的所需规模，以匹配观察到的指标， 例如，平均 CPU 利用率、平均内存利用率或你指定的任何其他自定义指标。** 


<img alt="" height="656" src="https://img-blog.csdnimg.cn/a33d9ff1fb7f49d487fede476a47ca33.png" width="772">

### 2.2、VPA垂直扩缩 

>  
 ** VPA 全称 Vertical Pod Autoscaler，即垂直 Pod 自动扩缩容，可以根据容器资源使用情况自动设置 CPU 和 内存 的请求值，从而允许在节点上进行适当的调度，以便为每个 Pod 提供适当的资源。它既可以缩小过度请求资源的容器，也可以根据其使用情况随时提升资源不足的容量。** 


 <img alt="" height="285" src="https://img-blog.csdnimg.cn/8869c16c52d946dc904b5ef5a2115d8d.png" width="735">



  **################################################################### ** 

##  知识点3：安装metrics-server

### 1、下载官方yaml文件，修改image为阿里云的地址

>  
 **示例：因为官方yaml文件的metrics镜像地址是github的，所以修改为阿里云的地址** 


```
apiVersion: v1
kind: ServiceAccount
metadata:
  labels:
    k8s-app: metrics-server
  name: metrics-server
  namespace: kube-system
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  labels:
    k8s-app: metrics-server
    rbac.authorization.k8s.io/aggregate-to-admin: "true"
    rbac.authorization.k8s.io/aggregate-to-edit: "true"
    rbac.authorization.k8s.io/aggregate-to-view: "true"
  name: system:aggregated-metrics-reader
rules:
- apiGroups:
  - metrics.k8s.io
  resources:
  - pods
  - nodes
  verbs:
  - get
  - list
  - watch
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  labels:
    k8s-app: metrics-server
  name: system:metrics-server
rules:
- apiGroups:
  - ""
  resources:
  - nodes/metrics
  verbs:
  - get
- apiGroups:
  - ""
  resources:
  - pods
  - nodes
  verbs:
  - get
  - list
  - watch
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  labels:
    k8s-app: metrics-server
  name: metrics-server-auth-reader
  namespace: kube-system
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: extension-apiserver-authentication-reader
subjects:
- kind: ServiceAccount
  name: metrics-server
  namespace: kube-system
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  labels:
    k8s-app: metrics-server
  name: metrics-server:system:auth-delegator
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: system:auth-delegator
subjects:
- kind: ServiceAccount
  name: metrics-server
  namespace: kube-system
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  labels:
    k8s-app: metrics-server
  name: system:metrics-server
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: system:metrics-server
subjects:
- kind: ServiceAccount
  name: metrics-server
  namespace: kube-system
---
apiVersion: v1
kind: Service
metadata:
  labels:
    k8s-app: metrics-server
  name: metrics-server
  namespace: kube-system
spec:
  ports:
  - name: https
    port: 443
    protocol: TCP
    targetPort: https
  selector:
    k8s-app: metrics-server
---
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    k8s-app: metrics-server
  name: metrics-server
  namespace: kube-system
spec:
  selector:
    matchLabels:
      k8s-app: metrics-server
  strategy:
    rollingUpdate:
      maxUnavailable: 0
  template:
    metadata:
      labels:
        k8s-app: metrics-server
    spec:
      containers:
      - args:
        - --kubelet-insecure-tls
        - --kubelet-preferred-address-types=InternalIP 
        - --cert-dir=/tmp
        - --secure-port=4443
        - --kubelet-preferred-address-types=InternalDNS,InternalIP,ExternalIP,Hostname
        - --kubelet-use-node-status-port
        - --metric-resolution=15s
        image: registry.aliyuncs.com/google_containers/metrics-server:v0.6.0
        imagePullPolicy: IfNotPresent
        livenessProbe:
          failureThreshold: 3
          httpGet:
            path: /livez
            port: https
            scheme: HTTPS
          periodSeconds: 10
        name: metrics-server
        ports:
        - containerPort: 4443
          name: https
          protocol: TCP
        readinessProbe:
          failureThreshold: 3
          httpGet:
            path: /readyz
            port: https
            scheme: HTTPS
          initialDelaySeconds: 20
          periodSeconds: 10
        resources:
          requests:
            cpu: 100m
            memory: 200Mi
        securityContext:
          allowPrivilegeEscalation: false
          readOnlyRootFilesystem: true
          runAsNonRoot: true
          runAsUser: 1000
        volumeMounts:
        - mountPath: /tmp
          name: tmp-dir
      nodeSelector:
        kubernetes.io/os: linux
      priorityClassName: system-cluster-critical
      serviceAccountName: metrics-server
      volumes:
      - emptyDir: {}
        name: tmp-dir
---
apiVersion: apiregistration.k8s.io/v1
kind: APIService
metadata:
  labels:
    k8s-app: metrics-server
  name: v1beta1.metrics.k8s.io
spec:
  group: metrics.k8s.io
  groupPriorityMinimum: 100
  insecureSkipTLSVerify: true
  service:
    name: metrics-server
    namespace: kube-system
  version: v1beta1
  versionPriority: 100

```

**################################################################################### ** 

### 2、执行安装命令

```
[root@k8s-master ~]# kubectl apply -f aliyun-components.yaml 
serviceaccount/metrics-server created
clusterrole.rbac.authorization.k8s.io/system:aggregated-metrics-reader created
clusterrole.rbac.authorization.k8s.io/system:metrics-server created
rolebinding.rbac.authorization.k8s.io/metrics-server-auth-reader created
clusterrolebinding.rbac.authorization.k8s.io/metrics-server:system:auth-delegator created
clusterrolebinding.rbac.authorization.k8s.io/system:metrics-server created
service/metrics-server created
deployment.apps/metrics-server created
apiservice.apiregistration.k8s.io/v1beta1.metrics.k8s.io created

```

  **################################################################### **  

### 3、查看效果：

>  
 **能够使用下面的命令查看到pod的效果，说明metrics server已经安装成功** 


```
[root@k8s-master pod]# kubectl top pod
NAME                       CPU(cores)   MEMORY(bytes)   
my-nginx-cf54cdbf7-6hbmp   0m           3Mi             
my-nginx-cf54cdbf7-dsrvm   0m           3Mi             
redis                      0m           0Mi             
[root@k8s-master pod]# kubectl top node
NAME         CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
k8s-master   223m         5%     1020Mi          59%       
k8s-node1    57m          1%     661Mi           38%       
k8s-node2    73m          1%     615Mi           35%       
k8s-node3    70m          1%     662Mi           38%     
```

   **################################################################### ** 

## 知识点4：安装HPA

**官方文档：**



### 1、安装好metrics-server

### 2、创建HPA功能

#### 2.1、编辑Dockerfile和index.php

Dockerfiel文件：

```
FROM php:5-apache
COPY index.php /var/www/html/index.php
RUN chmod a+rx index.php
```

index.php:

```
&lt;?php
  $x = 0.0001;
  for ($i = 0; $i &lt;= 1000000; $i++) {
    $x += sqrt($x);
  }
  echo "OK!";
?&gt;
```

**################################################################################### ** 

#### 2.2、生成镜像文件

```
[root@k8s-master HPA]# docker build -t sc-hpa:1.0 .
Sending build context to Docker daemon  3.072kB
Step 1/3 : FROM php:5-apache
5-apache: Pulling from library/php
5e6ec7f28fb7: Pull complete 
cf165947b5b7: Pull complete 
7bd37682846d: Pull complete 
99daf8e838e1: Pull complete 
ae320713efba: Pull complete 
ebcb99c48d8c: Pull complete 
9867e71b4ab6: Pull complete 
936eb418164a: Pull complete 
bc298e7adaf7: Pull complete 
ccd61b587bcd: Pull complete 
b2d4b347f67c: Pull complete 
56e9dde34152: Pull complete 
9ad99b17eb78: Pull complete 
Digest: sha256:0a40fd273961b99d8afe69a61a68c73c04bc0caa9de384d3b2dd9e7986eec86d
Status: Downloaded newer image for php:5-apache
 ---&gt; 24c791995c1e
Step 2/3 : COPY index.php /var/www/html/index.php
 ---&gt; 303d25be9de8
Step 3/3 : RUN chmod a+rx index.php
 ---&gt; Running in b1ed3ceefc79
Removing intermediate container b1ed3ceefc79
 ---&gt; c48f70fa8ede
Successfully built c48f70fa8ede
Successfully tagged sc-hpa:1.0

```

>  
 **创建一个链接的镜像hpa-example指向我们自己创建的sc-hpa镜像** 


```
[root@k8s-master HPA]# docker tag sc-hpa:1.0 hpa-example:latest
[root@k8s-master HPA]# docker images
REPOSITORY                                                        TAG        IMAGE ID       CREATED         SIZE
hpa-example                                                       latest     c48f70fa8ede   2 minutes ago   355MB
sc-hpa                                                            1.0        c48f70fa8ede   2 minutes ago   355MB

```

>  
 **创建php-apache.yaml ** 


```
apiVersion: apps/v1
kind: Deployment
metadata:
  namespace: default
  name: php-apache
spec:
  selector:
    matchLabels:
      run: php-apache
  replicas: 1
  template:
    metadata:
      labels:
        run: php-apache
    spec:
      containers:
      - name: php-apache
        image: sc-hpa:1.0
        ports:
        - containerPort: 80
        resources:
          limits:
            cpu: 200m
          requests:
            cpu: 100m

---

apiVersion: v1
kind: Service
metadata:
  namespace: default
  name: php-apache
  labels:
    run: php-apache
spec:
  ports:
  - port: 80
  selector:
    run: php-apache

```

#### 2.3、启动php-apache.yaml文件

```
[root@k8s-master HPA]# kubectl apply -f php-apache.yaml  
deployment.apps/php-apache created
service/php-apache created
[root@k8s-master HPA]# kubectl get pod -o wide
NAME                          READY   STATUS    RESTARTS   AGE   IP           NODE        NOMINATED NODE   READINESS GATES
php-apache-7c97954b84-lvqsj   1/1     Running   0          4s    10.244.1.3   k8s-node1   &lt;none&gt;           &lt;none&gt;

```

**################################################################################### **  

### 3、创建HPA

```
[root@k8s-master HPA]# kubectl autoscale deployment php-apache --cpu-percent=10 --min=1 --max=10
horizontalpodautoscaler.autoscaling/php-apache autoscaled
[root@k8s-master HPA]# kubectl get hpa
NAME         REFERENCE               TARGETS   MINPODS   MAXPODS   REPLICAS   AGE
php-apache   Deployment/php-apache   1%/10%    1         10        1          29s
[root@k8s-master HPA]# kubectl get pod
NAME                          READY   STATUS    RESTARTS   AGE
php-apache-7c97954b84-lvqsj   1/1     Running   0          11m

```

可以通过运行以下命令检查新制作的 HorizontalPodAutoscaler 的当前状态：

```
[root@k8s-master HPA]# kubectl get hpa
NAME         REFERENCE               TARGETS   MINPODS   MAXPODS   REPLICAS   AGE
php-apache   Deployment/php-apache   1%/10%    1         10        1          15m

```

**################################################################################### ** 

### 4、增加负载

>  
 **接下来，看看自动扩缩器如何对增加的负载做出反应。 为此，你将启动一个不同的 Pod 作为客户端。 客户端 Pod 中的容器在无限循环中运行，向 php-apache 服务发送查询。** 


```
# 在单独的终端中运行它
# 以便负载生成继续，你可以继续执行其余步骤
[root@k8s-master HPA]#  kubectl run -i --tty load-generator --rm --image=busybox:1.28 --restart=Never -- /bin/sh -"while sleep 0.01; do wget -q -O- http://10.244.2.4; done"

```



 <img alt="" height="586" src="https://img-blog.csdnimg.cn/195b4bcc38b5490dbe4e869ec0ede316.png" width="1052">

>  
 **在增加负载的同时，使用kubectl get hpa php-apache --watch观察cpu负载情况，pod数量 ** 
 **可以看到，一分钟左右，cpu的负载在不断升高，而HPA也在不断的增加pod的数量，一致到设置的最大pod数** 
 **同时，k8s集群中的php-apache的pod数量也和HPA增加的pod数一致** 


```
[root@k8s-master HPA]# kubectl get hpa php-apache --watch
NAME         REFERENCE               TARGETS   MINPODS   MAXPODS   REPLICAS   AGE
php-apache   Deployment/php-apache   1%/10%    1         10        1          18m
php-apache   Deployment/php-apache   63%/10%   1         10        1          21m
php-apache   Deployment/php-apache   199%/10%   1         10        4          21m
php-apache   Deployment/php-apache   107%/10%   1         10        8          21m
php-apache   Deployment/php-apache   51%/10%    1         10        10         22m
php-apache   Deployment/php-apache   24%/10%    1         10        10         22m
php-apache   Deployment/php-apache   22%/10%    1         10        10         22m
php-apache   Deployment/php-apache   15%/10%    1         10        10         22m
php-apache   Deployment/php-apache   1%/10%     1         10        10         23m

```

```
[root@k8s-master HPA]# kubectl get pod -o wide
NAME                          READY   STATUS    RESTARTS   AGE     IP           NODE        NOMINATED NODE   READISS GATES
php-apache-7c97954b84-27zc5   1/1     Running   0          4m11s   10.244.3.8   k8s-node3   &lt;none&gt;           &lt;none
php-apache-7c97954b84-2xp8r   1/1     Running   0          4m41s   10.244.1.4   k8s-node1   &lt;none&gt;           &lt;none
php-apache-7c97954b84-5tnfx   1/1     Running   0          4m26s   10.244.3.7   k8s-node3   &lt;none&gt;           &lt;none
php-apache-7c97954b84-64vn7   1/1     Running   0          4m11s   10.244.1.6   k8s-node1   &lt;none&gt;           &lt;none
php-apache-7c97954b84-c8wbq   1/1     Running   0          4m26s   10.244.2.4   k8s-node2   &lt;none&gt;           &lt;none
php-apache-7c97954b84-gw5x8   1/1     Running   0          4m41s   10.244.2.3   k8s-node2   &lt;none&gt;           &lt;none
php-apache-7c97954b84-lkk9p   1/1     Running   0          4m26s   10.244.2.5   k8s-node2   &lt;none&gt;           &lt;none
php-apache-7c97954b84-lvqsj   1/1     Running   0          21m     10.244.1.3   k8s-node1   &lt;none&gt;           &lt;none
php-apache-7c97954b84-rhqcv   1/1     Running   0          4m26s   10.244.1.5   k8s-node1   &lt;none&gt;           &lt;none
php-apache-7c97954b84-rmx9x   1/1     Running   0          4m41s   10.244.3.6   k8s-node3   &lt;none&gt;           &lt;none

```

**################################################################################### **

### 5、停止产生负载

>  
 **在我们创建 `busybox` 容器的终端中，输入 `&lt;Ctrl&gt; + C` 来终止负载的产生。** 
 **然后验证结果状态（大约一分钟后）：pod的数量显示它已经缩小了** 


```
[root@k8s-master HPA]# kubectl get hpa php-apache --watch
NAME         REFERENCE               TARGETS   MINPODS   MAXPODS   REPLICAS   AGE
php-apache   Deployment/php-apache   1%/10%    1         10        1          18m
php-apache   Deployment/php-apache   63%/10%   1         10        1          21m
php-apache   Deployment/php-apache   199%/10%   1         10        4          21m
php-apache   Deployment/php-apache   107%/10%   1         10        8          21m
php-apache   Deployment/php-apache   51%/10%    1         10        10         22m
php-apache   Deployment/php-apache   24%/10%    1         10        10         22m
php-apache   Deployment/php-apache   22%/10%    1         10        10         22m
php-apache   Deployment/php-apache   15%/10%    1         10        10         22m
php-apache   Deployment/php-apache   1%/10%     1         10        10         23m
php-apache   Deployment/php-apache   1%/10%     1         10        10         27m
php-apache   Deployment/php-apache   1%/10%     1         10        1          28m

```

```
[root@k8s-master HPA]# kubectl get pod -o wide
NAME                          READY   STATUS    RESTARTS   AGE    IP            NODE        NOMINATED NODE   READINESS GATES
php-apache-7c97954b84-77fgv   1/1     Running   0          7m2s   10.244.1.13   k8s-node1   &lt;none&gt;           &lt;none&gt;
[root@k8s-master HPA]# 

```

>  
 **一旦 CPU 利用率降至 0，HPA 会自动将副本数缩减为 1。** 
 **自动扩缩完成副本数量的改变可能需要几分钟的时间。** 


**################################################################################### **

## 知识点5：部署和访问 Kubernetes 仪表板（Dashboard）

**官方文档：**



>  
 **Dashboard 是基于网页的 Kubernetes 用户界面。 你可以使用 Dashboard 将容器应用部署到 Kubernetes 集群中，也可以对容器应用排错，还能管理集群资源。 你可以使用 Dashboard 获取运行在集群中的应用的概览信息，也可以创建或者修改 Kubernetes 资源 （如 Deployment，Job，DaemonSet 等等）。 例如，你可以对 Deployment 实现弹性伸缩、发起滚动升级、重启 Pod 或者使用向导创建新的应用。** 
 **Dashboard 同时展示了 Kubernetes 集群中的资源状态信息和所有报错信息。** 


### 1、下载yaml文件

```
[root@k8s-master HPA]# wget https://raw.githubusercontent.com/kubernetes/dashboard/v2.6.1/aio/deploy/recommended.yaml
--2022-10-06 20:57:46--  https://raw.githubusercontent.com/kubernetes/dashboard/v2.6.1/aio/deploy/recommended.yaml
正在解析主机 raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.108.133, 185.199.111.133, 185.199.109.133, ...
正在连接 raw.githubusercontent.com (raw.githubusercontent.com)|185.199.108.133|:443... 已连接。
已发出 HTTP 请求，正在等待回应... 200 OK
长度：7621 (7.4K) [text/plain]
正在保存至: “recommended.yaml”

100%[=======================================================================&gt;] 7,621       --.-K/s 用时 0s      

2022-10-06 20:57:47 (82.4 MB/s) - 已保存 “recommended.yaml” [7621/7621])

[root@k8s-master HPA]# ls
Dockerfile  hpa-example.tar  index.php  php-apache.yaml   recommended.yaml

```

**################################################################################### ** 

### 2、安装Dashboard

```
[root@k8s-master HPA]# kubectl apply -f recommended.yaml 
namespace/kubernetes-dashboard created
serviceaccount/kubernetes-dashboard created
service/kubernetes-dashboard created
secret/kubernetes-dashboard-certs created
secret/kubernetes-dashboard-csrf created
secret/kubernetes-dashboard-key-holder created
configmap/kubernetes-dashboard-settings created
role.rbac.authorization.k8s.io/kubernetes-dashboard created
clusterrole.rbac.authorization.k8s.io/kubernetes-dashboard created
rolebinding.rbac.authorization.k8s.io/kubernetes-dashboard created
clusterrolebinding.rbac.authorization.k8s.io/kubernetes-dashboard created
deployment.apps/kubernetes-dashboard created
service/dashboard-metrics-scraper created
deployment.apps/dashboard-metrics-scraper created

```

**################################################################################### ** 

### 3、查看Dashboard是否启动

```
[root@k8s-master HPA]# kubectl get pod --all-namespaces
NAMESPACE              NAME                                         READY   STATUS    RESTARTS   AGE
default                php-apache-7c97954b84-77fgv                  1/1     Running   0          167m
kube-flannel           kube-flannel-ds-c7crw                        1/1     Running   0          11d
kube-flannel           kube-flannel-ds-pr5pr                        1/1     Running   0          11d
kube-flannel           kube-flannel-ds-rphnc                        1/1     Running   0          11d
kube-flannel           kube-flannel-ds-v8rxz                        1/1     Running   0          11d
kube-system            coredns-6d8c4cb4d-92g7b                      1/1     Running   0          11d
kube-system            coredns-6d8c4cb4d-kl4q5                      1/1     Running   0          11d
kube-system            etcd-k8s-master                              1/1     Running   0          11d
kube-system            kube-apiserver-k8s-master                    1/1     Running   0          11d
kube-system            kube-controller-manager-k8s-master           1/1     Running   0          11d
kube-system            kube-proxy-422b5                             1/1     Running   0          11d
kube-system            kube-proxy-6qpcz                             1/1     Running   0          11d
kube-system            kube-proxy-ggnnt                             1/1     Running   0          11d
kube-system            kube-proxy-vjcnc                             1/1     Running   0          11d
kube-system            kube-scheduler-k8s-master                    1/1     Running   0          11d
kube-system            metrics-server-b9f7b695f-58j42               1/1     Running   0          5h22m
kubernetes-dashboard   dashboard-metrics-scraper-6f669b9c9b-mz49f   1/1     Running   0          81s
kubernetes-dashboard   kubernetes-dashboard-54c5fb4776-5h2lb        1/1     Running   0          81s

```

>  
 **查看Dashboard对应的服务，因为发布服务的类型是ClusterIP， 外面的机器不能访问，不便于外面的浏览器访问，** 


```
[root@k8s-master HPA]# kubectl get service  --all-namespaces
NAMESPACE              NAME                        TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)                  AGE
default                kubernetes                  ClusterIP   10.1.0.1       &lt;none&gt;        443/TCP                  11d
default                php-apache                  ClusterIP   10.1.148.215   &lt;none&gt;        80/TCP                   3h20m
kube-system            kube-dns                    ClusterIP   10.1.0.10      &lt;none&gt;        53/UDP,53/TCP,9153/TCP   11d
kube-system            metrics-server              ClusterIP   10.1.20.144    &lt;none&gt;        443/TCP                  5h23m
kubernetes-dashboard   dashboard-metrics-scraper   ClusterIP   10.1.59.19     &lt;none&gt;        8000/TCP                 117s
kubernetes-dashboard   kubernetes-dashboard        ClusterIP   10.1.3.28      &lt;none&gt;        443/TCP                  118s

```

>  
 **我们要搭建一个外部机器也可以访问Dashboard的service，所以先将Dashboard原来的service删除，然后重新部署一个service** 


**################################################################################### ** 

### 4、删除Dashboard 的service服务，

```
[root@k8s-master HPA]# kubectl delete service kubernetes-dashboard --namespace=kubernetes-dashboard
service "kubernetes-dashboard" deleted
[root@k8s-master HPA]# kubectl get svc --all-namespaces
NAMESPACE              NAME                        TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)                  AGE
default                kubernetes                  ClusterIP   10.1.0.1       &lt;none&gt;        443/TCP                  11d
default                php-apache                  ClusterIP   10.1.148.215   &lt;none&gt;        80/TCP                   3h31m
kube-system            kube-dns                    ClusterIP   10.1.0.10      &lt;none&gt;        53/UDP,53/TCP,9153/TCP   11d
kube-system            metrics-server              ClusterIP   10.1.20.144    &lt;none&gt;        443/TCP                  5h34m
kubernetes-dashboard   dashboard-metrics-scraper   ClusterIP   10.1.209.128   &lt;none&gt;        8000/TCP                 41s

```

### 5、重新创建一个service ，将服务类型设置为NodePort，然后启动它

```
[root@k8s-master HPA]# vim dashboard-svc.yaml
kind: Service
apiVersion: v1
metadata:
  labels:
    k8s-app: kubernetes-dashboard
  name: kubernetes-dashboard
  namespace: kubernetes-dashboard
spec:
  type: NodePort
  ports:
    - port: 443
      targetPort: 8443
  selector:
    k8s-app: kubernetes-dashboard
```

>  
 **启动service服务** 


```
[root@k8s-master HPA]# kubectl apply -f dashboard-svc.yaml 
service/kubernetes-dashboard created
[root@k8s-master HPA]# kubectl get svc --all-namespaces
NAMESPACE              NAME                        TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)                  AGE
default                kubernetes                  ClusterIP   10.1.0.1       &lt;none&gt;        443/TCP                  11d
default                php-apache                  ClusterIP   10.1.148.215   &lt;none&gt;        80/TCP                   3h33m
kube-system            kube-dns                    ClusterIP   10.1.0.10      &lt;none&gt;        53/UDP,53/TCP,9153/TCP   11d
kube-system            metrics-server              ClusterIP   10.1.20.144    &lt;none&gt;        443/TCP                  5h36m
kubernetes-dashboard   dashboard-metrics-scraper   ClusterIP   10.1.209.128   &lt;none&gt;        8000/TCP                 2m28s
kubernetes-dashboard   kubernetes-dashboard        NodePort    10.1.9.110     &lt;none&gt;        443:32697/TCP            4s
[root@k8s-master HPA]# 

```

**################################################################################### ** 

### 6、想要访问dashboard服务，就要有访问权限，创建kubernetes-dashboard管理员角色

```
[root@k8s-master HPA]#  vim dashboard-svc-account.yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: dashboard-admin
  namespace: kube-system
---
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: dashboard-admin
subjects:
  - kind: ServiceAccount
    name: dashboard-admin
    namespace: kube-system
roleRef:
  kind: ClusterRole
  name: cluster-admin
  apiGroup: rbac.authorization.k8s.io
```

```
[root@k8s-master HPA]# kubectl apply -f dashboard-svc-account.yaml 
serviceaccount/dashboard-admin created
clusterrolebinding.rbac.authorization.k8s.io/dashboard-admin created

```

>  
 **查看dashboard服务有没有启动** 


```
[root@k8s-master HPA]# kubectl get service --all-namespaces
NAMESPACE              NAME                        TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)                  AGE
default                kubernetes                  ClusterIP   10.1.0.1       &lt;none&gt;        443/TCP                  11d
default                php-apache                  ClusterIP   10.1.148.215   &lt;none&gt;        80/TCP                   3h45m
kube-system            kube-dns                    ClusterIP   10.1.0.10      &lt;none&gt;        53/UDP,53/TCP,9153/TCP   11d
kube-system            metrics-server              ClusterIP   10.1.20.144    &lt;none&gt;        443/TCP                  5h48m
kubernetes-dashboard   dashboard-metrics-scraper   ClusterIP   10.1.209.128   &lt;none&gt;        8000/TCP                 15m
kubernetes-dashboard   kubernetes-dashboard        NodePort    10.1.9.110     &lt;none&gt;        443:32697/TCP            12m

```

**################################################################################### ** 

###  7、获取token

>  
 **先获得dashboard的secret对象的名字** 


```
[root@k8s-master HPA]#  kubectl get secret -n kube-system|grep admin
dashboard-admin-token-z79k2                      kubernetes.io/service-account-token   3      73s
[root@k8s-master HPA]# kubectl get secret -n kube-system|grep admin|awk '{print $1}'
dashboard-admin-token-z79k2

```

```
[root@k8s-master HPA]# kubectl describe secret dashboard-admin-token-z79k2 -n kube-system
Name:         dashboard-admin-token-z79k2
Namespace:    kube-system
Labels:       &lt;none&gt;
Annotations:  kubernetes.io/service-account.name: dashboard-admin
              kubernetes.io/service-account.uid: f46b864d-91ec-47fe-96d0-f680b4079daf

Type:  kubernetes.io/service-account-token

Data
====
namespace:  11 bytes
token:      eyJhbGciOiJSUzI1NiIsImtpZCI6Inh6QzdwM1F5dy1rQUtBdnYyc0hVa09xdVFOVkQyUkJCeHdvTWlHU2s4X3cifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJkYXNoYm9hcmQtYWRtaW4tdG9rZW4tejc5azIiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiZGFzaGJvYXJkLWFkbWluIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQudWlkIjoiZjQ2Yjg2NGQtOTFlYy00N2ZlLTk2ZDAtZjY4MGI0MDc5ZGFmIiwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50Omt1YmUtc3lzdGVtOmRhc2hib2FyZC1hZG1pbiJ9.g-M-I5J5vxE8r6W1hkiaB7sGmj6lq2DRkcbDb1eqJRLoK6jNBicX59c9HbirtOPixg7u6nlUReS7FvK9dyQTl0YoMHUjltcmJA1gSr2SQhA6VrSmAMOyyc0owbQKa9_rv5c3cSoaedchlmAaWGuSW_4CPETWc6gXPKj_2gXVjew6kK-yxHXi6UovLm4ikBvwdX3IC7OxEwKLPoE1CIDUUf_UQQK47zaXKqRtH0ApFbP-0Ci0KvV5gYgjhyQ8hsBHMh0fidaS3z9RS1VzP-TYx6ZnUth0j88-eSUHWxcjInO9dsQsTm40sypzkUsJ7RKvCPLtK8SwKCsXIJvBTSNzeQ
ca.crt:     1099 bytes

```

```
[root@k8s-master HPA]# kubectl describe secret dashboard-admin-token-z79k2 -n kube-system|awk '/^token/ {print $2}'
eyJhbGciOiJSUzI1NiIsImtpZCI6Inh6QzdwM1F5dy1rQUtBdnYyc0hVa09xdVFOVkQyUkJCeHdvTWlHU2s4X3cifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJkYXNoYm9hcmQtYWRtaW4tdG9rZW4tejc5azIiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiZGFzaGJvYXJkLWFkbWluIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQudWlkIjoiZjQ2Yjg2NGQtOTFlYy00N2ZlLTk2ZDAtZjY4MGI0MDc5ZGFmIiwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50Omt1YmUtc3lzdGVtOmRhc2hib2FyZC1hZG1pbiJ9.g-M-I5J5vxE8r6W1hkiaB7sGmj6lq2DRkcbDb1eqJRLoK6jNBicX59c9HbirtOPixg7u6nlUReS7FvK9dyQTl0YoMHUjltcmJA1gSr2SQhA6VrSmAMOyyc0owbQKa9_rv5c3cSoaedchlmAaWGuSW_4CPETWc6gXPKj_2gXVjew6kK-yxHXi6UovLm4ikBvwdX3IC7OxEwKLPoE1CIDUUf_UQQK47zaXKqRtH0ApFbP-0Ci0KvV5gYgjhyQ8hsBHMh0fidaS3z9RS1VzP-TYx6ZnUth0j88-eSUHWxcjInO9dsQsTm40sypzkUsJ7RKvCPLtK8SwKCsXIJvBTSNzeQ

```

**################################################################################### ** 

### 8、访问dashboard

>  
 **https://+ 主机IP地址 : 端口号** 


<img alt="" height="866" src="https://img-blog.csdnimg.cn/9f69778f3f68488185e51cdf26c65e94.png" width="1200">

>  
 ** 登录成功效果：** 


<img alt="" height="986" src="https://img-blog.csdnimg.cn/69a16c1bc17d493e95cacf0a2bd8bf9a.png" width="1200">

 <img alt="" height="983" src="https://img-blog.csdnimg.cn/7a74ae7765eb496a852a689e6a1462b4.png" width="1200">


