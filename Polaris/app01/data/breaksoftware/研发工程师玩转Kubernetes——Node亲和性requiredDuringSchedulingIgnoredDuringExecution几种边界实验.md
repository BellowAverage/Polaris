
--- 
title:  研发工程师玩转Kubernetes——Node亲和性requiredDuringSchedulingIgnoredDuringExecution几种边界实验 
tags: []
categories: [] 

---


#### 大纲
- - <ul><li>- <ul><li>- - 


在中，我们提到requiredDuringSchedulingIgnoredDuringExecution只有在规则被满足的时候才能执行调度。本节我们将测试几种边界情况，看看Kubernetes的行为。

## 没有满足的条件

假设我们测试的Node都没有Label:not_exist=“”，于是我们在清单中要求必须有这个Label，来测试这个边界。

```
# nginx_deployment.yaml 
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
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: not_exist
                operator: In
                values:
                - ""
      containers:
      - name: nginx-container
        image: nginx
        ports:
        - containerPort: 80

```

执行下面的指令

```
kubectl create -f nginx_deployment.yaml

```

>  
 deployment.apps/nginx-deployment created 


### 观察

#### Pod的情况

```
kubectl get pod --watch -o wide

```

```
NAME                                READY   STATUS    RESTARTS   AGE   IP       NODE     NOMINATED NODE   READINESS GATES
nginx-deployment-6b5d69bc9d-94vgl   0/1     Pending   0          0s    &lt;none&gt;   &lt;none&gt;   &lt;none&gt;           &lt;none&gt;
nginx-deployment-6b5d69bc9d-94vgl   0/1     Pending   0          0s    &lt;none&gt;   &lt;none&gt;   &lt;none&gt;           &lt;none&gt;

```

#### Deployment的情况

```
kubectl get deployments.apps --watch -o wide

```

```
NAME               READY   UP-TO-DATE   AVAILABLE   AGE   CONTAINERS        IMAGES   SELECTOR
nginx-deployment   0/1     1            0           59s   nginx-container   nginx    app=nginx

```

可以看到Pod一直处于Pending状态，也没调度到任何Node上。

## 多个nodeSelectorTerms

为了进行这个测试，我们给UbuntuB和UbunutC设置对应的Label。

```
kubectl label nodes ubuntub name:ubuntub

```

>  
 node/ubuntub labeled 


```
kubectl label nodes ubuntuc name=ubuntuc

```

>  
 node/ubuntuc labeled 


我们使用下面指令查看下修改后的Labels。

```
kubectl get nodes --show-labels     

```

```
NAME      STATUS   ROLES    AGE   VERSION   LABELS
ubuntud   Ready    &lt;none&gt;   21h   v1.26.4   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=ubuntud,kubernetes.io/os=linux,microk8s.io/cluster=true,node.kubernetes.io/microk8s-worker=microk8s-worker
ubuntuc   Ready    &lt;none&gt;   21h   v1.26.4   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=ubuntuc,kubernetes.io/os=linux,microk8s.io/cluster=true,name=ubuntuc,node.kubernetes.io/microk8s-worker=microk8s-worker
ubuntub   Ready    &lt;none&gt;   21h   v1.26.4   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=ubuntub,kubernetes.io/os=linux,microk8s.io/cluster=true,name=ubuntub,node.kubernetes.io/microk8s-worker=microk8s-worker
ubuntue   Ready    &lt;none&gt;   21h   v1.26.4   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=ubuntue,kubernetes.io/os=linux,microk8s.io/cluster=true,node.kubernetes.io/microk8s-worker=microk8s-worker
ubuntua   Ready    &lt;none&gt;   21h   v1.27.2   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=ubuntua,kubernetes.io/os=linux,microk8s.io/cluster=true,node.kubernetes.io/microk8s-controlplane=microk8s-controlplane

```

然后清单改成多个nodeSelectorTerms

```
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
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: name
                operator: In
                values:
                - "ubuntub"
            - matchExpressions:
              - key: name
                operator: In
                values:
                - "ubuntuc"
      containers:
      - name: nginx-container
        image: nginx
        ports:
        - containerPort: 80

```

调用下面指令创建Deployment

```
kubectl create -f nginx_deployment.yaml 

```

>  
 deployment.apps/nginx-deployment created 


### 观察

```
kubectl get pod --watch -o wide

```

```
NAME                                READY   STATUS    RESTARTS   AGE   IP       NODE     NOMINATED NODE   READINESS GATES
nginx-deployment-58d4498bdd-s5fvd   0/1     Pending   0          0s    &lt;none&gt;   &lt;none&gt;   &lt;none&gt;           &lt;none&gt;
nginx-deployment-58d4498bdd-s5fvd   0/1     Pending   0          0s    &lt;none&gt;   ubuntuc   &lt;none&gt;           &lt;none&gt;
nginx-deployment-58d4498bdd-s5fvd   0/1     ContainerCreating   0          0s    &lt;none&gt;   ubuntuc   &lt;none&gt;           &lt;none&gt;
nginx-deployment-58d4498bdd-s5fvd   0/1     ContainerCreating   0          0s    &lt;none&gt;   ubuntuc   &lt;none&gt;           &lt;none&gt;
nginx-deployment-58d4498bdd-s5fvd   1/1     Running             0          4s    10.1.43.212   ubuntuc   &lt;none&gt;           &lt;none&gt;

```

```
kubectl get deployments.apps --watch -o wide

```

```
NAME               READY   UP-TO-DATE   AVAILABLE   AGE   CONTAINERS        IMAGES   SELECTOR
nginx-deployment   0/1     0            0           0s    nginx-container   nginx    app=nginx
nginx-deployment   0/1     0            0           0s    nginx-container   nginx    app=nginx
nginx-deployment   0/1     0            0           0s    nginx-container   nginx    app=nginx
nginx-deployment   0/1     1            0           0s    nginx-container   nginx    app=nginx
nginx-deployment   1/1     1            1           4s    nginx-container   nginx    app=nginx

```

可以看到Node的requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchExpressions之间是取或的关系，即只要满足其中一个条件就可以被调度到。 为了再次验证，我们可以让UbuntC驱逐这个Pod。

```
 kubectl taint node ubuntuc node_type=worker:NoExecute

```

>  
 node/ubuntuc tainted 


再观察

```
kubectl get pod --watch -o wide

```

```
NAME                                READY   STATUS    RESTARTS   AGE   IP       NODE     NOMINATED NODE   READINESS GATES
nginx-deployment-58d4498bdd-s5fvd   1/1     Running             0          8m28s   10.1.43.212   ubuntuc   &lt;none&gt;           &lt;none&gt;
nginx-deployment-58d4498bdd-s5fvd   1/1     Terminating         0          8m28s   10.1.43.212   ubuntuc   &lt;none&gt;           &lt;none&gt;
nginx-deployment-58d4498bdd-s5fvd   1/1     Terminating         0          8m28s   10.1.43.212   ubuntuc   &lt;none&gt;           &lt;none&gt;
nginx-deployment-58d4498bdd-kc2fz   0/1     Pending             0          1s      &lt;none&gt;        &lt;none&gt;    &lt;none&gt;           &lt;none&gt;
nginx-deployment-58d4498bdd-kc2fz   0/1     Pending             0          1s      &lt;none&gt;        ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-58d4498bdd-kc2fz   0/1     ContainerCreating   0          1s      &lt;none&gt;        ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-58d4498bdd-s5fvd   1/1     Terminating         0          8m29s   10.1.43.212   ubuntuc   &lt;none&gt;           &lt;none&gt;
nginx-deployment-58d4498bdd-kc2fz   0/1     ContainerCreating   0          1s      &lt;none&gt;        ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-58d4498bdd-s5fvd   0/1     Terminating         0          8m30s   10.1.43.212   ubuntuc   &lt;none&gt;           &lt;none&gt;
nginx-deployment-58d4498bdd-s5fvd   0/1     Terminating         0          8m30s   10.1.43.212   ubuntuc   &lt;none&gt;           &lt;none&gt;
nginx-deployment-58d4498bdd-s5fvd   0/1     Terminating         0          8m30s   10.1.43.212   ubuntuc   &lt;none&gt;           &lt;none&gt;
nginx-deployment-58d4498bdd-kc2fz   1/1     Running             0          4s      10.1.209.132   ubuntub   &lt;none&gt;           &lt;none&gt;

```

可以看到Pod被调度到另外一个匹配的条件对应的Node（UbuntuB）上。

## 被彻底驱逐

再让UbuntuB驱逐这个Pod，这样没有哪个Node可以符合条件。

```
kubectl taint node ubuntub node_type=worker:NoExecute

```

>  
 node/ubuntub tainted 


再观察

```
kubectl get pod --watch -o wide

```

```
NAME                                READY   STATUS    RESTARTS   AGE   IP       NODE     NOMINATED NODE   READINESS GATES
nginx-deployment-58d4498bdd-kc2fz   1/1     Terminating         0          3m30s   10.1.209.132   ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-58d4498bdd-kc2fz   1/1     Terminating         0          3m30s   10.1.209.132   ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-58d4498bdd-wjkbx   0/1     Pending             0          0s      &lt;none&gt;         &lt;none&gt;    &lt;none&gt;           &lt;none&gt;
nginx-deployment-58d4498bdd-wjkbx   0/1     Pending             0          0s      &lt;none&gt;         &lt;none&gt;    &lt;none&gt;           &lt;none&gt;
nginx-deployment-58d4498bdd-kc2fz   1/1     Terminating         0          3m30s   10.1.209.132   ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-58d4498bdd-kc2fz   0/1     Terminating         0          3m31s   10.1.209.132   ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-58d4498bdd-kc2fz   0/1     Terminating         0          3m31s   10.1.209.132   ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-58d4498bdd-kc2fz   0/1     Terminating         0          3m32s   10.1.209.132   ubuntub   &lt;none&gt;           &lt;none&gt;

```

因为被驱逐，老的Pod被终止，而新的Pod因为哪个Node可以被匹配到，而变成pending状态。

## 取消Label

接上上步，我们使用下面指令取消UbuntuB对Pod的驱逐

```
kubectl taint node ubuntub node_type=worker:NoExecute-

```

>  
 node/ubuntub untainted 


可以看到Deployment将Pod调度到UbuntuB上

```
NAME                                READY   STATUS    RESTARTS   AGE   IP       NODE     NOMINATED NODE   READINESS GATES
nginx-deployment-58d4498bdd-wjkbx   0/1     ContainerCreating   0          5m20s   &lt;none&gt;         ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-58d4498bdd-wjkbx   0/1     ContainerCreating   0          5m20s   &lt;none&gt;         ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-58d4498bdd-wjkbx   1/1     Running             0          5m23s   10.1.209.133   ubuntub   &lt;none&gt;           &lt;none&gt;

```

然后我们使用下面指令取消UbuntuB的Label：name=unbuntb

```
kubectl label nodes ubuntub name- 

```

这次Deployment不会驱逐该Pod

```
 kubectl get pod  -o wide 

```

```
NAME                                READY   STATUS    RESTARTS   AGE   IP             NODE      NOMINATED NODE   READINESS GATES
nginx-deployment-58d4498bdd-wjkbx   1/1     Running   0          11m   10.1.209.133   ubuntub   &lt;none&gt;           &lt;none&gt;

```

## 总结
- requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchExpressions之间是取或的关系，即只要满足其中一个条件就可以被调度到。- 没有匹配的条件，Pod会被创建，但是处于Pending状态，不会被部署到任何一个Node上。- 如果Pod已经在Node上运行，此时删除Node匹配上的Label，Deployment不会终止该Pod。