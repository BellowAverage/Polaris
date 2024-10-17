
--- 
title:  研发工程师玩转Kubernetes——Node失效后恢复的实验 
tags: []
categories: [] 

---


#### 大纲
- - - - <ul><li>- - 


在中我们看到Kubernetes会一直等待Node状态恢复。这节我们将做实验，看看Node恢复后Kubernetes的表现。 仍然借助的实验过程。

## Node失效前

在停止前Node前，各个组件的状态如下：

```
kubectl get deployments.apps -o wide --watch

```

```
NAME               READY   UP-TO-DATE   AVAILABLE   AGE   CONTAINERS        IMAGES   SELECTOR
nginx-deployment   1/1     1            1           20s   nginx-container   nginx    app=nginx

```

```
kubectl get pod --watch -o wide

```

```
NAME                               READY   STATUS    RESTARTS   AGE   IP             NODE      NOMINATED NODE   READINESS GATES
nginx-deployment-8f788645b-qszpv   1/1     Running   0          10s   10.1.209.134   ubuntub   &lt;none&gt;           &lt;none&gt;

```

```
kubectl get node --watch -o wide

```

```
NAME      STATUS   ROLES    AGE    VERSION   INTERNAL-IP     EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION      CONTAINER-RUNTIME
ubuntub   Ready    &lt;none&gt;   2d5h   v1.26.4   172.23.79.69    &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntua   Ready    &lt;none&gt;   2d7h   v1.26.4   172.23.71.113   &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntud   Ready    &lt;none&gt;   24h    v1.26.4   172.23.74.199   &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntuc   Ready    &lt;none&gt;   2d5h   v1.26.4   172.23.67.151   &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntue   Ready    &lt;none&gt;   24h    v1.26.4   172.23.73.117   &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15

```

可见Pod被部署在UbuntuB上。

## Node失效中

现在我们关闭Node UbuntuB。登录该机器执行

```
sudo poweroff

```

再查看上述组件状态

```
kubectl get deployments.apps -o wide --watch

```

```
NAME               READY   UP-TO-DATE   AVAILABLE   AGE   CONTAINERS        IMAGES   SELECTOR
nginx-deployment   1/1     1            1           20s   nginx-container   nginx    app=nginx
nginx-deployment   0/1     1            0           5m38s   nginx-container   nginx    app=nginx

```

上述显示，Deployment已经发现Pod不可用了，因为AVAILABLE字段变成了0，READY也变成了0/1。

```
kubectl get pod --watch -o wide

```

```
NAME                               READY   STATUS    RESTARTS   AGE   IP             NODE      NOMINATED NODE   READINESS GATES
nginx-deployment-8f788645b-qszpv   1/1     Running   0          10s   10.1.209.134   ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-qszpv   1/1     Running   0          5m38s   10.1.209.134   ubuntub   &lt;none&gt;           &lt;none&gt;

```

但是查看Pod的指令则显示该Pod还在运行中。

```
get node --watch -o wide

```

```
NAME      STATUS   ROLES    AGE    VERSION   INTERNAL-IP     EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION      CONTAINER-RUNTIME
ubuntub   Ready    &lt;none&gt;   2d5h   v1.26.4   172.23.79.69    &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntua   Ready    &lt;none&gt;   2d7h   v1.26.4   172.23.71.113   &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntud   Ready    &lt;none&gt;   24h    v1.26.4   172.23.74.199   &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntuc   Ready    &lt;none&gt;   2d5h   v1.26.4   172.23.67.151   &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntue   Ready    &lt;none&gt;   24h    v1.26.4   172.23.73.117   &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntub   Ready    &lt;none&gt;   2d5h   v1.26.4   172.23.79.69    &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntua   Ready    &lt;none&gt;   2d7h   v1.26.4   172.23.71.113   &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntud   Ready    &lt;none&gt;   24h    v1.26.4   172.23.74.199   &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntuc   Ready    &lt;none&gt;   2d5h   v1.26.4   172.23.67.151   &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntue   Ready    &lt;none&gt;   24h    v1.26.4   172.23.73.117   &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntub   NotReady   &lt;none&gt;   2d5h   v1.26.4   172.23.79.69    &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntub   NotReady   &lt;none&gt;   2d5h   v1.26.4   172.23.79.69    &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntub   NotReady   &lt;none&gt;   2d5h   v1.26.4   172.23.79.69    &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15

```

Node也一直在报UbuntuB失效了。

## Node恢复后

因为Deployment会等待比较长的时间，才会将失效的Node上的Pod迁移。于是Node恢复会分为几种场景：
1. 在Pod迁移尚未迁移时恢复1. 在Pod迁移中恢复1. 在Pod迁移完成后恢复
### 在Pod迁移尚未迁移时恢复

我们再次启动UbuntuB。要尽量迅速，以赶在Kubernetes判定Pod彻底失效并迁移其到其他Node上之前完成启动。

```
kubectl get deployments.apps -o wide --watch

```

```
NAME               READY   UP-TO-DATE   AVAILABLE   AGE   CONTAINERS        IMAGES   SELECTOR
nginx-deployment   1/1     1            1           20s   nginx-container   nginx    app=nginx
nginx-deployment   0/1     1            0           5m38s   nginx-container   nginx    app=nginx
nginx-deployment   1/1     1            1           9m6s    nginx-container   nginx    app=nginx

```

可以看到Deployment很快恢复到正常状态（READY变成了1/1）。

```
get pod --watch -o wide

```

```
NAME                               READY   STATUS    RESTARTS   AGE   IP             NODE      NOMINATED NODE   READINESS GATES
nginx-deployment-8f788645b-qszpv   1/1     Running   0          10s   10.1.209.134   ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-qszpv   1/1     Running   0          5m38s   10.1.209.134   ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-qszpv   0/1     Unknown   0          8m14s   &lt;none&gt;         ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-qszpv   0/1     Unknown   0          8m57s   &lt;none&gt;         ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-qszpv   0/1     Unknown   0          8m57s   &lt;none&gt;         ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-qszpv   1/1     Running   1 (53s ago)   9m3s    10.1.209.135   ubuntub   &lt;none&gt;           &lt;none&gt;

```

Pod在经历了3次Unknown状态后也恢复了，但是其IP发生了变化（从10.1.209.134变成了10.1.209.135）。

```
kubectl get node --watch -o wide

```

```
NAME      STATUS   ROLES    AGE    VERSION   INTERNAL-IP     EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION      CONTAINER-RUNTIME
ubuntub   Ready    &lt;none&gt;   2d5h   v1.26.4   172.23.79.69    &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntua   Ready    &lt;none&gt;   2d7h   v1.26.4   172.23.71.113   &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntud   Ready    &lt;none&gt;   24h    v1.26.4   172.23.74.199   &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntuc   Ready    &lt;none&gt;   2d5h   v1.26.4   172.23.67.151   &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntue   Ready    &lt;none&gt;   24h    v1.26.4   172.23.73.117   &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntub   Ready    &lt;none&gt;   2d5h   v1.26.4   172.23.79.69    &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntua   Ready    &lt;none&gt;   2d7h   v1.26.4   172.23.71.113   &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntud   Ready    &lt;none&gt;   24h    v1.26.4   172.23.74.199   &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntuc   Ready    &lt;none&gt;   2d5h   v1.26.4   172.23.67.151   &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntue   Ready    &lt;none&gt;   24h    v1.26.4   172.23.73.117   &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntub   NotReady   &lt;none&gt;   2d5h   v1.26.4   172.23.79.69    &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntub   NotReady   &lt;none&gt;   2d5h   v1.26.4   172.23.79.69    &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntub   NotReady   &lt;none&gt;   2d5h   v1.26.4   172.23.79.69    &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntua   Ready      &lt;none&gt;   2d7h   v1.26.4   172.23.71.113   &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntud   Ready      &lt;none&gt;   24h    v1.26.4   172.23.74.199   &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntub   NotReady   &lt;none&gt;   2d5h   v1.26.4   172.23.69.88    &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntub   NotReady   &lt;none&gt;   2d5h   v1.26.4   172.23.69.88    &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntub   NotReady   &lt;none&gt;   2d5h   v1.26.4   172.23.69.88    &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntub   Ready      &lt;none&gt;   2d5h   v1.26.4   172.23.69.88    &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntub   Ready      &lt;none&gt;   2d5h   v1.26.4   172.23.69.88    &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15
ubuntub   Ready      &lt;none&gt;   2d5h   v1.26.4   172.23.69.88    &lt;none&gt;        Ubuntu 22.04.2 LTS   5.15.0-73-generic   containerd://1.6.15

```

失效的Node（UbuntuB） 在重启后自动加入了Kubernetes集群，但是其IP（可能）发生了变化。

### 在Pod迁移完成后恢复

```
kubectl get deployments.apps -o wide --watch

```

```
NAME               READY   UP-TO-DATE   AVAILABLE   AGE   CONTAINERS        IMAGES   SELECTOR
nginx-deployment   1/1     1            1           24m   nginx-container   nginx    app=nginx
nginx-deployment   0/1     1            0           26m   nginx-container   nginx    app=nginx
nginx-deployment   0/1     0            0           31m   nginx-container   nginx    app=nginx
nginx-deployment   0/1     1            0           31m   nginx-container   nginx    app=nginx
nginx-deployment   1/1     1            1           32m   nginx-container   nginx    app=nginx

```

可以看到在AGE为31m时，Deployment开始着手迁移Pod了，并在32m时，Pod迁移完成。

```
kubectl get pod --watch -o wide

```

```
NAME                               READY   STATUS    RESTARTS      AGE   IP             NODE      NOMINATED NODE   READINESS GATES
nginx-deployment-8f788645b-qszpv   1/1     Running   1 (16m ago)   24m   10.1.209.135   ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-qszpv   1/1     Running   1 (17m ago)   26m   10.1.209.135   ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-qszpv   1/1     Running   1 (23m ago)   31m   10.1.209.135   ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-qszpv   1/1     Terminating   1 (23m ago)   31m   10.1.209.135   ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-qxxj2   0/1     Pending       0             0s    &lt;none&gt;         &lt;none&gt;    &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-qxxj2   0/1     Pending       0             0s    &lt;none&gt;         ubuntua   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-qxxj2   0/1     ContainerCreating   0             0s    &lt;none&gt;         ubuntua   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-qxxj2   0/1     ContainerCreating   0             0s    &lt;none&gt;         ubuntua   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-qxxj2   1/1     Running             0             58s   10.1.94.69     ubuntua   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-qszpv   0/1     Terminating         1 (24m ago)   32m   &lt;none&gt;         ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-qszpv   0/1     Terminating         1             33m   &lt;none&gt;         ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-qszpv   0/1     Terminating         1             33m   &lt;none&gt;         ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-qszpv   0/1     Terminating         1             33m   &lt;none&gt;         ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-qszpv   0/1     Terminating         1             33m   &lt;none&gt;         ubuntub   &lt;none&gt;           &lt;none&gt;

```

上面信息显示，位于失效Node上的Pod nginx-deployment-8f788645b-qszpv于31m时开始终止（Terminating）。然后Pod被迁移到UbuntuA上，并换了名字——nginx-deployment-8f788645b-qxxj2。后续，虽然失效的Node UbuntuB重新加入了集群，但是其上的Pod一直处于失效状态，且不会被删除。 node的信息和上个场景一样，这儿就不表了。

### 在Pod迁移中恢复

因为上例中新Pod在Master Node UbuntuA上分配的，而我们不能关闭这个Node。于是我们就删除之前的Deployment，并使用“污点”特性，让后续Pod不分配在UbuntuA上，才能进行实验。 待Deployment在UbuntuC上部署Pod时，我们启动失效的Node UbuntuB。其在新Pod部署完之前重新加入集群。

```
kubectl get deployments.apps -o wide --watch

```

```
NAME               READY   UP-TO-DATE   AVAILABLE   AGE   CONTAINERS        IMAGES   SELECTOR
nginx-deployment   0/1     0            0           1s    nginx-container   nginx    app=nginx
nginx-deployment   0/1     0            0           1s    nginx-container   nginx    app=nginx
nginx-deployment   0/1     0            0           1s    nginx-container   nginx    app=nginx
nginx-deployment   0/1     1            0           1s    nginx-container   nginx    app=nginx
nginx-deployment   1/1     1            1           4s    nginx-container   nginx    app=nginx
nginx-deployment   0/1     1            0           68s   nginx-container   nginx    app=nginx
nginx-deployment   0/1     0            0           6m13s   nginx-container   nginx    app=nginx
nginx-deployment   0/1     1            0           6m13s   nginx-container   nginx    app=nginx
nginx-deployment   1/1     1            1           7m12s   nginx-container   nginx    app=nginx

```

Deployment在6m13s时开始终止失效Node上的Pod，并开始在其他Node上部署新的Pod。7m12s时，新的Pod部署完成。

```
kubectl get pod --watch -o wide

```

```
NAME                               READY   STATUS    RESTARTS   AGE   IP       NODE     NOMINATED NODE   READINESS GATES
nginx-deployment-8f788645b-qd8ct   0/1     Pending   0          0s    &lt;none&gt;   &lt;none&gt;   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-qd8ct   0/1     Pending   0          0s    &lt;none&gt;   ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-qd8ct   0/1     ContainerCreating   0          0s    &lt;none&gt;   ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-qd8ct   0/1     ContainerCreating   0          0s    &lt;none&gt;   ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-qd8ct   1/1     Running             0          3s    10.1.209.138   ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-qd8ct   1/1     Running             0          67s   10.1.209.138   ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-qd8ct   1/1     Running             0          6m12s   10.1.209.138   ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-qd8ct   1/1     Terminating         0          6m12s   10.1.209.138   ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-p9ntd   0/1     Pending             0          0s      &lt;none&gt;         &lt;none&gt;    &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-p9ntd   0/1     Pending             0          0s      &lt;none&gt;         ubuntuc   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-p9ntd   0/1     ContainerCreating   0          1s      &lt;none&gt;         ubuntuc   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-p9ntd   0/1     ContainerCreating   0          2s      &lt;none&gt;         ubuntuc   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-qd8ct   0/1     Terminating         0          6m49s   &lt;none&gt;         ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-p9ntd   1/1     Running             0          59s     10.1.43.194    ubuntuc   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-qd8ct   0/1     Terminating         0          7m31s   &lt;none&gt;         ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-qd8ct   0/1     Terminating         0          7m38s   &lt;none&gt;         ubuntub   &lt;none&gt;           &lt;none&gt;
nginx-deployment-8f788645b-qd8ct   0/1     Terminating         0          7m38s   &lt;none&gt;         ubuntub   &lt;none&gt;           &lt;none&gt;

```

6m12s时，失效Node UbuntuB上的Pod nginx-deployment-8f788645b-qd8ct变成Terminating状态。Node UbuntuC上开始部署新的Pod nginx-deployment-8f788645b-p9ntd。6m49s时，失效Node UbuntuB试图通知Kubernetes Master让其上的Pod nginx-deployment-8f788645b-qd8ct加入Deployment维护的Pod副本，但是此时Kubernetes Master已经让这个Pod终止了，于是老的Pod恢复失败。7m11s时，新的Pod nginx-deployment-8f788645b-p9ntd运行成功。

## 总结

总结下：Node失效后，Kubernetes并不会自动将其摘除，而是一直等待它可用。失效后的Node在重启后，会自动向Kubernetes Master Node(本例中是Node UbuntuA)请求恢复。相应的，如果此时Deployment没有将原本在失效Node上的Pod设置为终止（Terminating）状态，则则Pod会就地恢复（IP会变动）；如果设置为终止状态，则老的Pod会失效，Deployment会使用新启动的Pod。
