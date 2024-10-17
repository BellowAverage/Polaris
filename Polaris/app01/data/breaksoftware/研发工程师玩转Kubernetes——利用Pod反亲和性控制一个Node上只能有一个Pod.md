
--- 
title:  研发工程师玩转Kubernetes——利用Pod反亲和性控制一个Node上只能有一个Pod 
tags: []
categories: [] 

---


#### 大纲
- - - <ul><li>- - - 


在、和中，我们介绍了Node的亲和性。后面几节我们将介绍Pod的亲和性和反亲和性。 Pod的亲和性和反亲和性通过Pod的标签来识别，而不是通过Node的标签。比如标题中“利用Pod反亲和性控制一个Node上只能有一个Pod”可以翻译成：只能将Pod调度到不存在该Pod标签的Node上。

## 清单文件

```
# nginx_deployment_pod_affinity.yaml 
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 1
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

## 反亲和性

这次亲和性（affinity）我们选择Pod反亲和性（podAntiAffinity）。它用于表达：如果满足下面条件就**不**调度。

### topologyKey

这儿有个非常重要的名称：topologyKey。它和labelSelector之间是与的关系，即topologyKey表达的条件要满足，labelSelector表达的条件也要满足。 topologyKey的写法非常简单，只要传入Node标签的一个Key的名称。比如本例中“topologyKey: “kubernetes.io/hostname” ”，表达的是：要在Node的标签Key为“kubernetes.io/hostname”对应的Value相同的Node上去对比labelSelector条件。

```
kubectl get nodes --show-labels 

```

```
NAME      STATUS   ROLES    AGE     VERSION   LABELS
ubuntue   Ready    &lt;none&gt;   173m    v1.27.2   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=ubuntue,kubernetes.io/os=linux,microk8s.io/cluster=true,node.kubernetes.io/microk8s-worker=microk8s-worker
ubuntuc   Ready    &lt;none&gt;   174m    v1.27.2   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=ubuntuc,kubernetes.io/os=linux,microk8s.io/cluster=true,node.kubernetes.io/microk8s-worker=microk8s-worker
ubuntub   Ready    &lt;none&gt;   174m    v1.27.2   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=ubuntub,kubernetes.io/os=linux,microk8s.io/cluster=true,node.kubernetes.io/microk8s-worker=microk8s-worker
ubuntud   Ready    &lt;none&gt;   174m    v1.27.2   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=ubuntud,kubernetes.io/os=linux,microk8s.io/cluster=true,node.kubernetes.io/microk8s-worker=microk8s-worker
ubuntua   Ready    &lt;none&gt;   3h23m   v1.27.2   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=ubuntua,kubernetes.io/os=linux,microk8s.io/cluster=true,node.kubernetes.io/microk8s-controlplane=microk8s-controlplane

```

我们看到每个Node标签kubernetes.io/hostname对应的Value都是Node的名称：ubuntua，ubuntub，ubuntuc，ubuntud和ubuntue。 这样我们就可以表达“在同一个Node”上的概念。 除了可以表达在“同一个Node”上，还可以表达“同一个zone”或者通过“region”，它们分别对应：“failure-domain.beta.kubernetes.io/zone"和"failure-domain.beta.kubernetes.io/region”。

```
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
          - labelSelector:
                matchExpressions:
                - key: app
                  operator: In
                  values:
                  - nginx
            topologyKey: "kubernetes.io/hostname"

```

这段核心代码可以解读成：在同一个Node（topologyKey: "kubernetes.io/hostname"限定）上，如果存在app:nginx的Pod（通过labelSelector限定），则绝对（通过requiredDuringSchedulingIgnoredDuringExecution限定）不可以调度（通过podAntiAffinity限定）到。

## 测试

### 创建Deployment

```
kubectl create -f  nginx_deployment_pod_affinity.yaml 

```

>  
 deployment.apps/nginx-deployment created 


这个时候，我们只是创建了一个副本。它被调度到ubuntue这个Node上。

```
kubectl get pods -o wide

```

```
NAME                                READY   STATUS    RESTARTS   AGE   IP           NODE      NOMINATED NODE   READINESS GATES
nginx-deployment-57555788b6-25bk8   1/1     Running   0          56s   10.1.226.4   ubuntue   &lt;none&gt;           &lt;none&gt;

```

### 扩容满

然后我们使用下面指令扩容。因为我们有5台可以运行的Node，则启动5个副本。可以看到它们被调度到5个不同的Node上。

```
kubectl scale --replicas=5 deployment nginx-deployment

```

>  
 deployment.apps/nginx-deployment scaled 


```
 kubectl get pods -o wide  

```

```
NAME                                READY   STATUS    RESTARTS   AGE    IP             NODE      NOMINATED NODE   READINESS GATES
nginx-deployment-57555788b6-25bk8   1/1     Running   0          4m7s   10.1.226.4     ubuntue   &lt;none&gt;           &lt;none&gt;
nginx-deployment-57555788b6-4hkm8   1/1     Running   0          45s    10.1.202.196   ubuntud   &lt;none&gt;           &lt;none&gt;
nginx-deployment-57555788b6-hv845   1/1     Running   0          45s    10.1.94.70     ubuntua   &lt;none&gt;           &lt;none&gt;
nginx-deployment-57555788b6-ln9tb   1/1     Running   0          45s    10.1.209.132   ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-57555788b6-6xg2s   1/1     Running   0          45s    10.1.43.204    ubuntuc   &lt;none&gt;           &lt;none&gt;

```

### 扩容失败

最后我们再扩容1个副本。可以发现它一直处于Pending状态。

```
kubectl scale --replicas=6 deployment nginx-deployment

```

>  
 deployment.apps/nginx-deployment scaled 


```
 kubectl get pods -o wide  

```

```
NAME                                READY   STATUS    RESTARTS   AGE     IP             NODE      NOMINATED NODE   READINESS GATES
nginx-deployment-57555788b6-25bk8   1/1     Running   0          5m50s   10.1.226.4     ubuntue   &lt;none&gt;           &lt;none&gt;
nginx-deployment-57555788b6-4hkm8   1/1     Running   0          2m28s   10.1.202.196   ubuntud   &lt;none&gt;           &lt;none&gt;
nginx-deployment-57555788b6-hv845   1/1     Running   0          2m28s   10.1.94.70     ubuntua   &lt;none&gt;           &lt;none&gt;
nginx-deployment-57555788b6-ln9tb   1/1     Running   0          2m28s   10.1.209.132   ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-57555788b6-6xg2s   1/1     Running   0          2m28s   10.1.43.204    ubuntuc   &lt;none&gt;           &lt;none&gt;
nginx-deployment-57555788b6-6f5tc   0/1     Pending   0          19s     &lt;none&gt;         &lt;none&gt;    &lt;none&gt;           &lt;none&gt;

```

查看其原因

```
kubectl describe pod nginx-deployment-57555788b6-6f5tc 

```

```
Name:             nginx-deployment-57555788b6-6f5tc
Namespace:        default
Priority:         0
Service Account:  default
Node:             &lt;none&gt;
Labels:           app=nginx
                  pod-template-hash=57555788b6
Annotations:      &lt;none&gt;
Status:           Pending
IP:               
IPs:              &lt;none&gt;
Controlled By:    ReplicaSet/nginx-deployment-57555788b6
Containers:
  nginx-container:
    Image:        nginx
    Port:         80/TCP
    Host Port:    0/TCP
    Environment:  &lt;none&gt;
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-6k5f8 (ro)
Conditions:
  Type           Status
  PodScheduled   False 
Volumes:
  kube-api-access-6k5f8:
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
  Type     Reason            Age   From               Message
  ----     ------            ----  ----               -------
  Warning  FailedScheduling  116s  default-scheduler  0/5 nodes are available: 5 node(s) didn't match pod anti-affinity rules. preemption: 0/5 nodes are available: 5 No preemption victims found for incoming pod..

```

可以看到，因为亲和性问题，没有Node可以被调度了。

## 参考资料
- - 