
--- 
title:  研发工程师玩转Kubernetes——PVC通过storageClassName进行延迟绑定 
tags: []
categories: [] 

---


#### 大纲
- - <ul><li>- - <ul><li>- - - - <ul><li>- 


不同的PV可以使用相同的StorageClass，它们是一对多的关系。 <img src="https://img-blog.csdnimg.cn/751370f3b12349c2a9a5d9c24725721d.png" alt="在这里插入图片描述"> PV可以设置节点亲和性。比如下图，local-storage-class-waitforfirstconsumer-pv-ubuntuc只能在节点ubuntuc上；local-storage-class-waitforfirstconsumer-pv-ubuntud只能在节点ubuntud上。 <img src="https://img-blog.csdnimg.cn/9daa5d8f4d9b4bd1b53d66b418b67e50.png" alt="在这里插入图片描述">

如果我们使用一文中的“立即绑定”型的StorageClass。

```
# local_storage_class_immediate.yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: local-storage-class-immediate
provisioner: kubernetes.io/no-provisioner
volumeBindingMode: Immediate

```

则在创建PVC时，立即会选择一个PV。这样这个PVC可能绑定到节点ubuntuc对应的PV上，也可能绑定到节点ubuntud对应的PV上。现在我们假定它绑定到ubuntuc对应的PV——local-storage-class-immediate-pv-ubuntuc上。 假如PVC的使用者——Pod在调度时，清单文件要求它只能在ubuntud上使用。而其PVC却在ubuntuc上，则会调度失败。

## 立即绑定导致Pod调度失败的案例

### StorageClass

注意volumeBindingMode是Immediate，即PVC创建时立即绑定PV。

```
# local_storage_class_immediate.yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: local-storage-class-immediate
provisioner: kubernetes.io/no-provisioner
volumeBindingMode: Immediate

```

### PersistentVolume

#### ubuntuc

```
# local_storage_class_immediate_pv_ubuntuc.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: local-storage-class-immediate-pv-ubuntuc
spec:
  capacity:
    storage:  1Mi
  volumeMode: Filesystem
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Delete
  storageClassName: local-storage-class-immediate
  local:
    path: /tmp
  nodeAffinity:
    required:
      nodeSelectorTerms:
      - matchExpressions:
        - key: kubernetes.io/hostname
          operator: In
          values:
          - ubuntuc

```

#### ubuntud

```
# local_storage_class_immediate_pv_ubuntud.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: local-storage-class-immediate-pv-ubuntud
spec:
  capacity:
    storage:  1Mi
  volumeMode: Filesystem
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Delete
  storageClassName: local-storage-class-immediate
  local:
    path: /tmp
  nodeAffinity:
    required:
      nodeSelectorTerms:
      - matchExpressions:
        - key: kubernetes.io/hostname
          operator: In
          values:
          - ubuntud

```

### PersistentVolumeClaim

```
# local_storage_class_immediate_pvc_600k.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: local-storage-class-immediate-pvc-600k
spec:
  resources:
    requests:
      storage: 600Ki
  accessModes:
    - ReadWriteOnce
  storageClassName: local-storage-class-immediate

```

创建完上述组件，我们查看下PVC的状态。

```
kubectl describe persistentvolumeclaims local-storage-class-immediate-pvc-600k 

```

```
Name:          local-storage-class-immediate-pvc-600k
Namespace:     default
StorageClass:  local-storage-class-immediate
Status:        Bound
Volume:        local-storage-class-immediate-pv-ubuntuc
Labels:        &lt;none&gt;
Annotations:   pv.kubernetes.io/bind-completed: yes
               pv.kubernetes.io/bound-by-controller: yes
Finalizers:    [kubernetes.io/pvc-protection]
Capacity:      1Mi
Access Modes:  RWO
VolumeMode:    Filesystem
Used By:       &lt;none&gt;
Events:        &lt;none&gt;

```

可以看到这个PVC处于绑定状态。

### Deployment

```
# local_deployment_immediate.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: local-pv-app-immediate-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: local-pv-app-immediate
  template:
    metadata:
      labels:
        app: local-pv-app-immediate
    spec:
      containers:
      - name: local-pv-app-immediate
        image: busybox
        command: ["/bin/sh", "-c", "if [ -f /tempdir/lockfile ] &amp;&amp; ! { set -C; 2&gt;/dev/null &gt;/tempdir/lockfile; }; then tail -f /tempdir/lockfile; else exec 3&gt;/tempdir/lockfile; if [ -n \"$POD_NAME\" ]; then name=$POD_NAME; else name=\"unknown\"; fi; while true; do echo \"this is $name.$name write something to lockfile\"; echo \"$name write something to lockfile\" &gt;&amp;3; sleep 1; done; fi"]  
        volumeMounts:
        - name: local-pvc-volume
          mountPath: /tempdir
        env:
        - name: POD_NAME
          valueFrom:
            fieldRef:
              fieldPath: metadata.name
      volumes:
      - name: local-pvc-volume
        persistentVolumeClaim:
          claimName: local-storage-class-immediate-pvc-600k
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: kubernetes.io/hostname
                operator: In
                values:
                - ubuntud    

```

这个清单要求Pod使用local-storage-class-immediate-pvc-600k这个PVC，但是要求自己只能被部署在节点ubuntud上。

### 错误表现

```
kubectl describe pod local-pv-app-immediate-deployment-6dd57d98f5-s5vpz 

```

```
Name:             local-pv-app-immediate-deployment-6dd57d98f5-s5vpz
Namespace:        default
Priority:         0
Service Account:  default
Node:             &lt;none&gt;
Labels:           app=local-pv-app-immediate
                  pod-template-hash=6dd57d98f5
Annotations:      &lt;none&gt;
Status:           Pending
IP:               
IPs:              &lt;none&gt;
Controlled By:    ReplicaSet/local-pv-app-immediate-deployment-6dd57d98f5
Containers:
  local-pv-app-immediate:
    Image:      busybox
    Port:       &lt;none&gt;
    Host Port:  &lt;none&gt;
    Command:
      /bin/sh
      -c
      if [ -f /tempdir/lockfile ] &amp;&amp; ! {<!-- --> set -C; 2&gt;/dev/null &gt;/tempdir/lockfile; }; then tail -f /tempdir/lockfile; else exec 3&gt;/tempdir/lockfile; if [ -n "$POD_NAME" ]; then name=$POD_NAME; else name="unknown"; fi; while true; do echo "this is $name.$name write something to lockfile"; echo "$name write something to lockfile" &gt;&amp;3; sleep 1; done; fi
    Environment:
      POD_NAME:  local-pv-app-immediate-deployment-6dd57d98f5-s5vpz (v1:metadata.name)
    Mounts:
      /tempdir from local-pvc-volume (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-r48fn (ro)
Conditions:
  Type           Status
  PodScheduled   False 
Volumes:
  local-pvc-volume:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:  local-storage-class-immediate-pvc-600k
    ReadOnly:   false
  kube-api-access-r48fn:
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
  Warning  FailedScheduling  8s    default-scheduler  0/5 nodes are available: 1 node(s) didn't match Pod's node affinity/selector. preemption: 0/5 nodes are available: 1 Preemption is not helpful for scheduling, 4 No preemption victims found for incoming pod..

```

可以看到Pod调度失败，处于Pending状态。 <img src="https://img-blog.csdnimg.cn/623457ee1a9f4f169ff9161dd3d094da.png" alt="在这里插入图片描述">

## 延迟绑定导致Pod调度成功的案例

### StorageClass

注意volumeBindingMode是WaitForFirstConsumer，即PVC创建时不绑定PV。而在PVC被使用（Pod被调度到）时绑定PV。

```
# local_storage_class_waitforfirstconsumer.yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: local-storage-class-waitforfirstconsumer
provisioner: kubernetes.io/no-provisioner
volumeBindingMode: WaitForFirstConsumer

```

### PersistentVolume

和之前的PV设置相似，核心就是storageClassName不同，使用了延迟绑定的StorageClass。

#### ubuntuc

```
# local_storage_class_waitforfirstconsumer_pv_ubuntuc.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: local-storage-class-waitforfirstconsumer-pv-ubuntuc
spec:
  capacity:
    storage:  1Mi
  volumeMode: Filesystem
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Delete
  storageClassName: local-storage-class-waitforfirstconsumer
  local:
    path: /tmp
  nodeAffinity:
    required:
      nodeSelectorTerms:
      - matchExpressions:
        - key: kubernetes.io/hostname
          operator: In
          values:
          - ubuntuc

```

#### ubuntud

```
# local_storage_class_waitforfirstconsumer_pv_ubuntud.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: local-storage-class-waitforfirstconsumer-pv-ubuntud
spec:
  capacity:
    storage:  1Mi
  volumeMode: Filesystem
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Delete
  storageClassName: local-storage-class-waitforfirstconsumer
  local:
    path: /tmp
  nodeAffinity:
    required:
      nodeSelectorTerms:
      - matchExpressions:
        - key: kubernetes.io/hostname
          operator: In
          values:
          - ubuntud

```

### PersistentVolumeClaim

和之前例子的区别就是storageClassName选择了延迟绑定的local-storage-class-waitforfirstconsumer。

```
# local_storage_class_waitforfirstconsumer_pvc_600k.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: local-storage-class-waitforfirstconsumer-pvc-600k
spec:
  resources:
    requests:
      storage: 600Ki
  accessModes:
    - ReadWriteOnce
  storageClassName: local-storage-class-waitforfirstconsumer

```

我们先创建上述组件，然后观察PVC的状态。

```
kubectl describe persistentvolumeclaims local-storage-class-waitforfirstconsumer-pvc-600k

```

```
Name:          local-storage-class-waitforfirstconsumer-pvc-600k
Namespace:     default
StorageClass:  local-storage-class-waitforfirstconsumer
Status:        Pending
Volume:        
Labels:        &lt;none&gt;
Annotations:   &lt;none&gt;
Finalizers:    [kubernetes.io/pvc-protection]
Capacity:      
Access Modes:  
VolumeMode:    Filesystem
Used By:       &lt;none&gt;
Events:
  Type    Reason                Age               From                         Message
  ----    ------                ----              ----                         -------
  Normal  WaitForFirstConsumer  2s (x2 over 11s)  persistentvolume-controller  waiting for first consumer to be created before binding

```

可以看到这次PVC没有立即绑定，而是处于Pending状态，且原因是等待第一个使用者触发绑定。

### Deployment

```
# local_deployment_waitforfirstconsumer.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: local-pv-app-waitforfirstconsumer-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: local-pv-app-waitforfirstconsumer
  template:
    metadata:
      labels:
        app: local-pv-app-waitforfirstconsumer
    spec:
      containers:
      - name: local-pv-app-waitforfirstconsumer
        image: busybox
        command: ["/bin/sh", "-c", "if [ -f /tempdir/lockfile ] &amp;&amp; ! { set -C; 2&gt;/dev/null &gt;/tempdir/lockfile; }; then tail -f /tempdir/lockfile; else exec 3&gt;/tempdir/lockfile; if [ -n \"$POD_NAME\" ]; then name=$POD_NAME; else name=\"unknown\"; fi; while true; do echo \"this is $name.$name write something to lockfile\"; echo \"$name write something to lockfile\" &gt;&amp;3; sleep 1; done; fi"]  
        volumeMounts:
        - name: local-pvc-volume
          mountPath: /tempdir
        env:
        - name: POD_NAME
          valueFrom:
            fieldRef:
              fieldPath: metadata.name
      volumes:
      - name: local-pvc-volume
        persistentVolumeClaim:
          claimName: local-storage-class-waitforfirstconsumer-pvc-600k
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: kubernetes.io/hostname
                operator: In
                values:
                - ubuntud    

```

创建完我们查看Pod的状态。

```
kubectl describe pod local-pv-app-waitforfirstconsumer-deployment-84449895c4-x7ddx

```

```
Name:             local-pv-app-waitforfirstconsumer-deployment-84449895c4-x7ddx
Namespace:        default
Priority:         0
Service Account:  default
Node:             ubuntud/172.22.244.197
Start Time:       Wed, 09 Aug 2023 17:07:01 +0000
Labels:           app=local-pv-app-waitforfirstconsumer
                  pod-template-hash=84449895c4
Annotations:      cni.projectcalico.org/containerID: cb10dba20771f872b242bc6284eb9d790565b7f2c1a2fbb096ff1581a73d4de5
                  cni.projectcalico.org/podIP: 10.1.202.206/32
                  cni.projectcalico.org/podIPs: 10.1.202.206/32
Status:           Running
IP:               10.1.202.206
IPs:
  IP:           10.1.202.206
Controlled By:  ReplicaSet/local-pv-app-waitforfirstconsumer-deployment-84449895c4
Containers:
  local-pv-app-waitforfirstconsumer:
    Container ID:  containerd://3fda11a2670236dc37409dd1fd6c5efae36d48bbcf1ce71266f72bd7b0b55b98
    Image:         busybox
    Image ID:      docker.io/library/busybox@sha256:3fbc632167424a6d997e74f52b878d7cc478225cffac6bc977eedfe51c7f4e79
    Port:          &lt;none&gt;
    Host Port:     &lt;none&gt;
    Command:
      /bin/sh
      -c
      if [ -f /tempdir/lockfile ] &amp;&amp; ! {<!-- --> set -C; 2&gt;/dev/null &gt;/tempdir/lockfile; }; then tail -f /tempdir/lockfile; else exec 3&gt;/tempdir/lockfile; if [ -n "$POD_NAME" ]; then name=$POD_NAME; else name="unknown"; fi; while true; do echo "this is $name.$name write something to lockfile"; echo "$name write something to lockfile" &gt;&amp;3; sleep 1; done; fi
    State:          Running
      Started:      Wed, 09 Aug 2023 17:07:04 +0000
    Ready:          True
    Restart Count:  0
    Environment:
      POD_NAME:  local-pv-app-waitforfirstconsumer-deployment-84449895c4-x7ddx (v1:metadata.name)
    Mounts:
      /tempdir from local-pvc-volume (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-52426 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  local-pvc-volume:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:  local-storage-class-waitforfirstconsumer-pvc-600k
    ReadOnly:   false
  kube-api-access-52426:
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
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  8s    default-scheduler  Successfully assigned default/local-pv-app-waitforfirstconsumer-deployment-84449895c4-x7ddx to ubuntud
  Normal  Pulling    8s    kubelet            Pulling image "busybox"
  Normal  Pulled     5s    kubelet            Successfully pulled image "busybox" in 2.266071612s (2.266078813s including waiting)
  Normal  Created    5s    kubelet            Created container local-pv-app-waitforfirstconsumer
  Normal  Started    5s    kubelet            Started container local-pv-app-waitforfirstconsumer

```

可以看到Pod按清单要求被成功调度到ubuntud上。

```
kubectl describe persistentvolumeclaims local-storage-class-waitforfirstconsumer-pvc-600k 

```

```
Name:          local-storage-class-waitforfirstconsumer-pvc-600k
Namespace:     default
StorageClass:  local-storage-class-waitforfirstconsumer
Status:        Bound
Volume:        local-storage-class-waitforfirstconsumer-pv-ubuntud
Labels:        &lt;none&gt;
Annotations:   pv.kubernetes.io/bind-completed: yes
               pv.kubernetes.io/bound-by-controller: yes
Finalizers:    [kubernetes.io/pvc-protection]
Capacity:      1Mi
Access Modes:  RWO
VolumeMode:    Filesystem
Used By:       local-pv-app-waitforfirstconsumer-deployment-84449895c4-x7ddx
Events:
  Type    Reason                Age                    From                         Message
  ----    ------                ----                   ----                         -------
  Normal  WaitForFirstConsumer  2m23s (x16 over 6m2s)  persistentvolume-controller  waiting for first consumer to be created before binding

```

这个Pod使用的PVC也被分配到ubuntud上。 <img src="https://img-blog.csdnimg.cn/bdf2ed913b214a09a40288416640e55b.png" alt="在这里插入图片描述">

## 参考资料
- 