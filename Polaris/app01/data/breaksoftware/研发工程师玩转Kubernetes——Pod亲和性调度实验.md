
--- 
title:  研发工程师玩转Kubernetes——Pod亲和性调度实验 
tags: []
categories: [] 

---


#### 大纲
- - <ul><li>- - - - <ul><li>- 


在一文中我们介绍了Pod的反亲和性应用。本节我们将使用亲和性做几个实验。 nginx Pod在每个Node上只能存在一个；alpine Pod在每个Node上只能存在一个，同时要求该Node上还要有nginx Pod。 实验分为3组：
1. 创建2个nginx Pod和2个alpine Pod，观察它们在Node上的分布。1. 将alpine Pod数调整到3，观察其状态；再将nginx Pod数调整到3，观察整体变化。1. 将nginx Pod数调整到2，观察整体变化。
## 清单文件

### nginx清单文件

```
# nginx_deployment_pod_affinity.yaml 
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      affinity:
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
          - labelSelector:
                matchExpressions:
                - key: app
                  operator: In
                  values:
                  - nginx
            topologyKey: "kubernetes.io/hostname"
      containers:
      - name: nginx-container
        image: nginx
        ports:
        - containerPort: 80

```

该清单文件指定一个Node上只能有一个nginx Pod。

### alpine清单文件

```
# alpine_deployment_pod_affinity.yaml 
apiVersion: apps/v1
kind: Deployment
metadata:
  name: alpine-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: alpine
  template:
    metadata:
      labels:
        app: alpine
    spec:
      affinity:
        podAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
          - labelSelector:
                matchExpressions:
                - key: app
                  operator: In
                  values:
                  - nginx
            topologyKey: "kubernetes.io/hostname"
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
          - labelSelector:
                matchExpressions:
                - key: app
                  operator: In
                  values:
                  - alpine
            topologyKey: "kubernetes.io/hostname"
      containers:
      - name: alpine-container
        image: alpine
        stdin: true
        tty: true


```

该清单文件指定在每个Node上只能存在一个alpine Pod，同时要求该Node上还要有nginx Pod。

## 实验

### 创建2个nginx Pod和2个alpine Pod

```
kubectl create -f nginx_deployment_pod_affinity.yaml -f alpine_deployment_pod_affinity.yaml

```

>  
 deployment.apps/nginx-deployment created deployment.apps/alpine-deployment created 


```
kubectl get pod -o wide

```

```
NAME                                 READY   STATUS    RESTARTS   AGE   IP            NODE      NOMINATED NODE   READINESS GATES
nginx-deployment-57555788b6-t8xqg    1/1     Running   0          8s    10.1.226.8    ubuntue   &lt;none&gt;           &lt;none&gt;
nginx-deployment-57555788b6-4c58f    1/1     Running   0          8s    10.1.43.214   ubuntuc   &lt;none&gt;           &lt;none&gt;
alpine-deployment-7f8b7cf975-vxvkq   1/1     Running   0          8s    10.1.226.9    ubuntue   &lt;none&gt;           &lt;none&gt;
alpine-deployment-7f8b7cf975-cfvqm   1/1     Running   0          8s    10.1.43.215   ubuntuc   &lt;none&gt;           &lt;none&gt;

```

可以看到，alpine按照我们的预期被调度到存在nginx的Pod上。

### 将alpine Pod数调整到3，再将nginx Pod数调整到3

#### 将alpine Pod数调整到3

```
kubectl scale --replicas=3 deployment alpine-deployment 

```

>  
 deployment.apps/alpine-deployment scaled 


使用下面指令观察Pod的变化

```
kubectl get pod --watch

```

```
NAME                                 READY   STATUS    RESTARTS   AGE
nginx-deployment-57555788b6-t8xqg    1/1     Running   0          8m44s
nginx-deployment-57555788b6-4c58f    1/1     Running   0          8m44s
alpine-deployment-7f8b7cf975-vxvkq   1/1     Running   0          8m44s
alpine-deployment-7f8b7cf975-cfvqm   1/1     Running   0          8m44s
alpine-deployment-7f8b7cf975-jjzqc   0/1     Pending   0          1s

```

可以看到alpine一直处于Pending状态。因为它要求被调度的Node上有nginx Pod，而又不能有alpine Pod。这个也符合预期。 在新窗口中，可以通过下面指令看到其状态

```
kubectl describe pod alpine-deployment-7f8b7cf975-jjzqc 

```

```
Name:             alpine-deployment-7f8b7cf975-jjzqc
Namespace:        default
Priority:         0
Service Account:  default
Node:             &lt;none&gt;
Labels:           app=alpine
                  pod-template-hash=7f8b7cf975
Annotations:      &lt;none&gt;
Status:           Pending
IP:               
IPs:              &lt;none&gt;
Controlled By:    ReplicaSet/alpine-deployment-7f8b7cf975
Containers:
  alpine-container:
    Image:        alpine
    Port:         &lt;none&gt;
    Host Port:    &lt;none&gt;
    Environment:  &lt;none&gt;
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-rqrls (ro)
Conditions:
  Type           Status
  PodScheduled   False 
Volumes:
  kube-api-access-rqrls:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       &lt;nil&gt;
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              &lt;none&gt;
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type     Reason            Age    From               Message
  ----     ------            ----   ----               -------
  Warning  FailedScheduling  4m38s  default-scheduler  0/5 nodes are available: 2 node(s) didn't match pod anti-affinity rules, 3 node(s) didn't match pod affinity rules. preemption: 0/5 nodes are available: 2 No preemption victims found for incoming pod, 3 Preemption is not helpful for scheduling..

```

#### 将nginx Pod数调整到3

在新窗口中执行下面指令调整

```
kubectl scale --replicas=3 deployment nginx-deployment 

```

再回到之前观察Pod变化的窗口

```
NAME                                 READY   STATUS    RESTARTS   AGE
nginx-deployment-57555788b6-t8xqg    1/1     Running   0          8m44s
nginx-deployment-57555788b6-4c58f    1/1     Running   0          8m44s
alpine-deployment-7f8b7cf975-vxvkq   1/1     Running   0          8m44s
alpine-deployment-7f8b7cf975-cfvqm   1/1     Running   0          8m44s
alpine-deployment-7f8b7cf975-jjzqc   0/1     Pending   0          1s
nginx-deployment-57555788b6-hmklk    0/1     Pending   0          0s
nginx-deployment-57555788b6-hmklk    0/1     Pending   0          0s
alpine-deployment-7f8b7cf975-jjzqc   0/1     Pending   0          6m46s
nginx-deployment-57555788b6-hmklk    0/1     ContainerCreating   0          0s
alpine-deployment-7f8b7cf975-jjzqc   0/1     ContainerCreating   0          6m46s
nginx-deployment-57555788b6-hmklk    0/1     ContainerCreating   0          0s
alpine-deployment-7f8b7cf975-jjzqc   0/1     ContainerCreating   0          6m46s
nginx-deployment-57555788b6-hmklk    1/1     Running             0          4s
alpine-deployment-7f8b7cf975-jjzqc   1/1     Running             0          6m52s

```

可以看到处于Pending状态的alpine在新扩出来的nginx Pod还处在ContainerCreating时，也变成了ContainerCreating状态，并在之后变成running状态。

### 将nginx Pod数调整到2

```
kubectl scale --replicas=2 deployment nginx-deployment

```

>  
 deployment.apps/nginx-deployment scaled 


观察整体变化

```
kubectl get pod -o wide 

```

```
NAME                                 READY   STATUS    RESTARTS   AGE   IP             NODE      NOMINATED NODE   READINESS GATES
nginx-deployment-57555788b6-t8xqg    1/1     Running   0          20m   10.1.226.8     ubuntue   &lt;none&gt;           &lt;none&gt;
nginx-deployment-57555788b6-4c58f    1/1     Running   0          20m   10.1.43.214    ubuntuc   &lt;none&gt;           &lt;none&gt;
alpine-deployment-7f8b7cf975-vxvkq   1/1     Running   0          20m   10.1.226.9     ubuntue   &lt;none&gt;           &lt;none&gt;
alpine-deployment-7f8b7cf975-cfvqm   1/1     Running   0          20m   10.1.43.215    ubuntuc   &lt;none&gt;           &lt;none&gt;
alpine-deployment-7f8b7cf975-jjzqc   1/1     Running   0          11m   10.1.202.201   ubuntud   &lt;none&gt;           &lt;none&gt;

```

可以看到alpine并没有变化。因为亲和性只是调度，所以在亲和条件发生变化时，之前已经调度好的结果并不会改变。
