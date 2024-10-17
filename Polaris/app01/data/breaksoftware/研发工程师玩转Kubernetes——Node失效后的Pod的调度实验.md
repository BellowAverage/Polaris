
--- 
title:  研发工程师玩转Kubernetes——Node失效后的Pod的调度实验 
tags: []
categories: [] 

---


#### 大纲
- - - 


在中，我们创建了Master Node: UbunutA，以及四个Worker Node:UbunutB、UbunutC、UbunutD和UbunutE。本节我们将使用Deployment创建只含有一个nginx的Pod，然后关掉它所在的主机以模拟Node失效，观察kubernetes在这种情况下的表现。

## 创建Node

我们登录到UbuntuA机器，通过下面的清单文件维持只有一个副本的Pod。

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
      containers:
      - name: nginx-container
        image: nginx
        ports:
        - containerPort: 80

```

然后执行

```
kubectl create -f nginx_deployment.yaml

```

>  
 deployment.apps/nginx-deployment created 


通过下面的指令，我们可以看到这个Pod所在的Node——在UbuntuE上。

```
kubectl get pod -o wide

```

```
NAME                               READY   STATUS    RESTARTS   AGE     IP           NODE      NOMINATED NODE   READINESS GATES
nginx-deployment-8f788645b-n7s6d   1/1     Running   0          3m51s   10.1.226.1   ubuntue   &lt;none&gt;           &lt;none&gt;

```

在关闭UbuntuE之前，我们新开两个终端，分别监视Pod和Node的变化

```
kubectl get pod --watch -o wide

```

```
kubectl get node --watch -o wide

```

## 关闭Pod所在主机

登录到UbuntuE上，执行

```
sudo poweroff

```

## 查看

等待一段时间，kubernetes察觉到UbuntuE服务器（Node）失效了 <img src="https://img-blog.csdnimg.cn/867aef818ba54b5aa01d0d93e49faa65.png" alt="在这里插入图片描述"> 但是Pod的状态并**没有立即改变**，进而也**没立即迁移该Pod**。 <img src="https://img-blog.csdnimg.cn/babc42c18ebe4f5398a406b90672e5a9.png" alt="在这里插入图片描述"> Kubernetes 会一直保存着失效节点对应的对象，并持续检查该节点是否已经变得健康。

```
kubectl get nodes --show-labels

```

```
NAME      STATUS     ROLES    AGE   VERSION   LABELS
ubuntuc   Ready      &lt;none&gt;   24h   v1.26.4   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=ubuntuc,kubernetes.io/os=linux,microk8s.io/cluster=true,node.kubernetes.io/microk8s-worker=microk8s-worker
ubuntue   NotReady   &lt;none&gt;   17h   v1.26.4   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=ubuntue,kubernetes.io/os=linux,microk8s.io/cluster=true,node.kubernetes.io/microk8s-worker=microk8s-worker
ubuntub   Ready      &lt;none&gt;   24h   v1.26.4   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=ubuntub,kubernetes.io/os=linux,microk8s.io/cluster=true,node.kubernetes.io/microk8s-worker=microk8s-worker
ubuntua   Ready      &lt;none&gt;   26h   v1.26.4   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=ubuntua,kubernetes.io/os=linux,microk8s.io/cluster=true,node.kubernetes.io/microk8s-controlplane=microk8s-controlplane
ubuntud   Ready      &lt;none&gt;   24h   v1.26.4   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=ubuntud,kubernetes.io/os=linux,microk8s.io/cluster=true,node.kubernetes.io/microk8s-worker=microk8s-worker

```

我们可以手工删除这个失效的Node，这样对应的Pod对象也会被删除，进而触发Deployment新增一个Pod。

```
kubectl delete nodes ubuntue

```

>  
 node “ubuntue” deleted 


<img src="https://img-blog.csdnimg.cn/6fa762346b434f3a97103fd5f3298c52.png" alt="在这里插入图片描述"> 我们再做一次实验，将新Pod所在的Node也关闭，继续查看Pod的变化过程。 <img src="https://img-blog.csdnimg.cn/fe6d2510ee3a4d80af11977fb728c18e.png" alt="在这里插入图片描述"> 可以看到等待了大于5分钟，kubernetes终于发现Pod失效了。这样在其维持着失效的Node UbuntuD情况下，也会发现Pod无效，进而在可用的Node上部署新的Pod。

```
 kubectl get pod -o wide

```

```
NAME                               READY   STATUS        RESTARTS   AGE   IP             NODE      NOMINATED NODE   READINESS GATES
nginx-deployment-8f788645b-nnwfj   1/1     Terminating   0          37m   10.1.202.194   ubuntud   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-zw68t   1/1     Running       0          27m   10.1.209.129   ubuntub   &lt;none&gt;           &lt;none&gt;

```

总体而言，Node失效后，Kubernetes会相对快速的发现其失效，但是会一直维持着这个Node对象，且持续检查它的状态。但是Kubernetes并不会快速发现部署于失效Node上的Pod也失效了，大概要等待5分钟左右才会在其他可用的Node上部署Pod，而原来的Pod将一直处于Terminating状态。
