
--- 
title:  研发工程师玩转Kubernetes——就绪探针（Readiness Probe）和服务（Service） 
tags: []
categories: [] 

---


#### 大纲
- - - - <ul><li>- 


## 带Readiness Probe的Nginx

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: readiness-nginx-deployment
spec:
  selector:
    matchLabels:
      app: readiness-nginx
  replicas: 2
  template:
    metadata:
      labels:
        app: readiness-nginx
    spec:
      containers:
      - name: readiness-nginx-container
        image: nginx
        ports:
        - containerPort: 80
        command: ["/bin/sh", "-c", "sleep 3; touch /tempdir/readiness-nginx; while true; do sleep 5; done"]
        volumeMounts:
        - name:  probe-volume
          mountPath:  /tempdir
        readinessProbe:
          exec:
            command:
            - cat
            - /tempdir/readiness-nginx
          initialDelaySeconds: 2
          failureThreshold: 6
          periodSeconds: 1
          successThreshold: 1
      volumes:
      - name: probe-volume
        emptyDir: 
          medium: Memory
          sizeLimit: 1Gi

```

## Nginx关联的Service

```
kind: Service
apiVersion: v1
metadata:
  name: readiness-nginx-service
spec:
  selector:
    app: readiness-nginx
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80

```

## 实验

创建上述组件，可以看到启动了下面的Pod

```
kubectl get pod -o wide

```

```
NAME                                          READY   STATUS    RESTARTS   AGE   IP             NODE      NOMINATED NODE   READINESS GATES
readiness-nginx-deployment-57b7fd5644-7x7wc   1/1     Running   0          25s   10.1.43.223    ubuntuc   &lt;none&gt;           &lt;none&gt;
readiness-nginx-deployment-57b7fd5644-lhszp   1/1     Running   0          25s   10.1.209.155   ubuntub   &lt;none&gt;           &lt;none&gt;

```

Service也绑定了这些IP。

```
kubectl describe endpoints readiness-nginx-service 

```

```
Name:         readiness-nginx-service
Namespace:    default
Labels:       &lt;none&gt;
Annotations:  endpoints.kubernetes.io/last-change-trigger-time: 2023-08-14T14:35:33Z
Subsets:
  Addresses:          10.1.209.155,10.1.43.223
  NotReadyAddresses:  &lt;none&gt;
  Ports:
    Name     Port  Protocol
    ----     ----  --------
    &lt;unset&gt;  80    TCP

Events:  &lt;none&gt;

```

现在我们挑选一个容器（readiness-nginx-deployment-57b7fd5644-7x7wc，10.1.43.223），观察该容器的Event状态：

```
kubectl describe pod readiness-nginx-deployment-57b7fd5644-7x7wc

```

```
Name:             readiness-nginx-deployment-57b7fd5644-7x7wc
Namespace:        default
Priority:         0
Service Account:  default
Node:             ubuntuc/172.22.247.176
Start Time:       Mon, 14 Aug 2023 14:35:27 +0000
Labels:           app=readiness-nginx
                  pod-template-hash=57b7fd5644
Annotations:      cni.projectcalico.org/containerID: c475d3e82ff0d5adbd35252ab990608ad75955f8d0862bb8b0c54ee60a0878eb
                  cni.projectcalico.org/podIP: 10.1.43.223/32
                  cni.projectcalico.org/podIPs: 10.1.43.223/32
Status:           Running
IP:               10.1.43.223
IPs:
  IP:           10.1.43.223
Controlled By:  ReplicaSet/readiness-nginx-deployment-57b7fd5644
Containers:
  readiness-nginx-container:
    Container ID:  containerd://5d82d8467bc6e0c8151e40ee3258d54bffec8659bcdad4a441848ea8f77a3223
    Image:         nginx
    Image ID:      docker.io/library/nginx@sha256:67f9a4f10d147a6e04629340e6493c9703300ca23a2f7f3aa56fe615d75d31ca
    Port:          80/TCP
    Host Port:     0/TCP
    Command:
      /bin/sh
      -c
      sleep 3; touch /tempdir/readiness-nginx; while true; do sleep 5; done
    State:          Running
      Started:      Mon, 14 Aug 2023 14:35:30 +0000
    Ready:          True
    Restart Count:  0
    Readiness:      exec [cat /tempdir/readiness-nginx] delay=2s timeout=1s period=1s #success=1 #failure=6
    Environment:    &lt;none&gt;
    Mounts:
      /tempdir from probe-volume (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-c4tcl (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  probe-volume:
    Type:       EmptyDir (a temporary directory that shares a pod's lifetime)
    Medium:     Memory
    SizeLimit:  1Gi
  kube-api-access-c4tcl:
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
  Type     Reason     Age                    From               Message
  ----     ------     ----                   ----               -------
  Normal   Scheduled  3m53s                  default-scheduler  Successfully assigned default/readiness-nginx-deployment-57b7fd5644-7x7wc to ubuntuc
  Normal   Pulling    3m53s                  kubelet            Pulling image "nginx"
  Normal   Pulled     3m50s                  kubelet            Successfully pulled image "nginx" in 2.489885583s (2.489893984s including waiting)
  Normal   Created    3m50s                  kubelet            Created container readiness-nginx-container
  Normal   Started    3m50s                  kubelet            Started container readiness-nginx-container
  Warning  Unhealthy  3m48s (x2 over 3m48s)  kubelet            Readiness probe failed: cat: /tempdir/readiness-nginx: No such file or directory

```

可以看到就绪探针在第3次检测时就存在了，这个时候Pod的Ready和ContainersReady都是True的状态。

### 就绪-&gt;非就绪

现在我们删除就绪标志文件

```
kubectl exec pods/readiness-nginx-deployment-57b7fd5644-7x7wc --container readiness-nginx-container -- rm /tempdir/readiness-nginx

```

再观察其状态，可以发现

```
Name:             readiness-nginx-deployment-57b7fd5644-7x7wc
Namespace:        default
Priority:         0
Service Account:  default
Node:             ubuntuc/172.22.247.176
Start Time:       Mon, 14 Aug 2023 14:35:27 +0000
Labels:           app=readiness-nginx
                  pod-template-hash=57b7fd5644
Annotations:      cni.projectcalico.org/containerID: c475d3e82ff0d5adbd35252ab990608ad75955f8d0862bb8b0c54ee60a0878eb
                  cni.projectcalico.org/podIP: 10.1.43.223/32
                  cni.projectcalico.org/podIPs: 10.1.43.223/32
Status:           Running
IP:               10.1.43.223
IPs:
  IP:           10.1.43.223
Controlled By:  ReplicaSet/readiness-nginx-deployment-57b7fd5644
Containers:
  readiness-nginx-container:
    Container ID:  containerd://5d82d8467bc6e0c8151e40ee3258d54bffec8659bcdad4a441848ea8f77a3223
    Image:         nginx
    Image ID:      docker.io/library/nginx@sha256:67f9a4f10d147a6e04629340e6493c9703300ca23a2f7f3aa56fe615d75d31ca
    Port:          80/TCP
    Host Port:     0/TCP
    Command:
      /bin/sh
      -c
      sleep 3; touch /tempdir/readiness-nginx; while true; do sleep 5; done
    State:          Running
      Started:      Mon, 14 Aug 2023 14:35:30 +0000
    Ready:          False
    Restart Count:  0
    Readiness:      exec [cat /tempdir/readiness-nginx] delay=2s timeout=1s period=1s #success=1 #failure=6
    Environment:    &lt;none&gt;
    Mounts:
      /tempdir from probe-volume (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-c4tcl (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  probe-volume:
    Type:       EmptyDir (a temporary directory that shares a pod's lifetime)
    Medium:     Memory
    SizeLimit:  1Gi
  kube-api-access-c4tcl:
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
  Type     Reason     Age                 From     Message
  ----     ------     ----                ----     -------
  Warning  Unhealthy  7s (x22 over 6m6s)  kubelet  Readiness probe failed: cat: /tempdir/readiness-nginx: No such file or directory

```

可以看到Ready和ContainersReady都变成了False状态。 我们再观察Service

```
kubectl describe endpoints readiness-nginx-service 

```

```
Name:         readiness-nginx-service
Namespace:    default
Labels:       &lt;none&gt;
Annotations:  endpoints.kubernetes.io/last-change-trigger-time: 2023-08-14T14:41:18Z
Subsets:
  Addresses:          10.1.209.155
  NotReadyAddresses:  10.1.43.223
  Ports:
    Name     Port  Protocol
    ----     ----  --------
    &lt;unset&gt;  80    TCP

Events:  &lt;none&gt;

```

可以看到被删除了就绪探针检测文件的Pod被从Service中摘掉了。

### 非就绪-&gt;就绪

我们再将检测文件还原

```
kubectl exec pods/readiness-nginx-deployment-57b7fd5644-7x7wc --container readiness-nginx-container -- touch /tempdir/readiness-nginx

```

观察对应Pod的状态，其Ready和ContainersReady又变成了True状态。

```
Name:             readiness-nginx-deployment-57b7fd5644-7x7wc
Namespace:        default
Priority:         0
Service Account:  default
Node:             ubuntuc/172.22.247.176
Start Time:       Mon, 14 Aug 2023 14:35:27 +0000
Labels:           app=readiness-nginx
                  pod-template-hash=57b7fd5644
Annotations:      cni.projectcalico.org/containerID: c475d3e82ff0d5adbd35252ab990608ad75955f8d0862bb8b0c54ee60a0878eb
                  cni.projectcalico.org/podIP: 10.1.43.223/32
                  cni.projectcalico.org/podIPs: 10.1.43.223/32
Status:           Running
IP:               10.1.43.223
IPs:
  IP:           10.1.43.223
Controlled By:  ReplicaSet/readiness-nginx-deployment-57b7fd5644
Containers:
  readiness-nginx-container:
    Container ID:  containerd://5d82d8467bc6e0c8151e40ee3258d54bffec8659bcdad4a441848ea8f77a3223
    Image:         nginx
    Image ID:      docker.io/library/nginx@sha256:67f9a4f10d147a6e04629340e6493c9703300ca23a2f7f3aa56fe615d75d31ca
    Port:          80/TCP
    Host Port:     0/TCP
    Command:
      /bin/sh
      -c
      sleep 3; touch /tempdir/readiness-nginx; while true; do sleep 5; done
    State:          Running
      Started:      Mon, 14 Aug 2023 14:35:30 +0000
    Ready:          True
    Restart Count:  0
    Readiness:      exec [cat /tempdir/readiness-nginx] delay=2s timeout=1s period=1s #success=1 #failure=6
    Environment:    &lt;none&gt;
    Mounts:
      /tempdir from probe-volume (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-c4tcl (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  probe-volume:
    Type:       EmptyDir (a temporary directory that shares a pod's lifetime)
    Medium:     Memory
    SizeLimit:  1Gi
  kube-api-access-c4tcl:
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
  Type     Reason     Age                   From     Message
  ----     ------     ----                  ----     -------
  Warning  Unhealthy  3m5s (x262 over 13m)  kubelet  Readiness probe failed: cat: /tempdir/readiness-nginx: No such file or directory

```

Service也重新将其加回来了。

```
Name:         readiness-nginx-service
Namespace:    default
Labels:       &lt;none&gt;
Annotations:  endpoints.kubernetes.io/last-change-trigger-time: 2023-08-14T14:48:23Z
Subsets:
  Addresses:          10.1.209.155,10.1.43.223
  NotReadyAddresses:  &lt;none&gt;
  Ports:
    Name     Port  Protocol
    ----     ----  --------
    &lt;unset&gt;  80    TCP

Events:  &lt;none&gt;

```
