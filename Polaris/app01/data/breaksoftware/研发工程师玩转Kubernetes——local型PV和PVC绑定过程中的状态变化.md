
--- 
title:  研发工程师玩转Kubernetes——local型PV和PVC绑定过程中的状态变化 
tags: []
categories: [] 

---


#### 大纲
- - - - - - 


PV全称是PersistentVolume，即持久卷，是由管理员事先准备好的资源。它可以是本地磁盘，也可以是网络磁盘。 PVC全称是PersistentVolumeClaim，即持久卷申领。它表示卷的使用者，对PV的申请。即我们可以认为，PV是整体，PVC是申请其中的部分。

## local型PV

local类型的持久卷分配的是本地磁盘空间。K8S要求该类型的卷在配置时指定其节点亲和性（nodeAffinity），即我们优先（只能）在哪些节点上分配空间。

```
# default_storage_class_pv.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: default-storage-class-pv
spec:
  capacity:
    storage: 100Ki
  volumeMode: Filesystem
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
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

accessModes是卷的访问模式。有如下选项：
1. ReadWriteOnce：读写权限，只能被一个Node挂载。1. ReadOnlyMany：只读权限，可以被多个Node挂载。1. ReadWriteMany：读写权限，可以被多个Node挂载。
由于上例是本地磁盘，所以只能是ReadWriteOnce，因为它只能被一个Node挂载。 persistentVolumeReclaimPolicy选择Retain，表示资源回收需要手工进行。 local和nodeAffinity表示我们将在ubuntud的/tmp目录下分配卷空间。

## 静态绑定的PVC

```
# default_storage_class_pvc.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: default-storage-class-pvc
spec:
  resources:
    requests:
      storage: 10Ki
  volumeName: default-storage-class-pv
  accessModes:
    - ReadWriteOnce

```

volumeName指定了PV的名称。这样PVC就和PV进行了绑定。

## 绑定过程中状态的变化

我们创建上述资源PV。

```
kubectl create -f default_storage_class_pv.yaml 

```

然后观察其状态：

```
kubectl describe persistentvolume default-storage-class-pv

```

```
Name:              default-storage-class-pv
Labels:            &lt;none&gt;
Annotations:       &lt;none&gt;
Finalizers:        [kubernetes.io/pv-protection]
StorageClass:      
Status:            Available
Claim:             
Reclaim Policy:    Retain
Access Modes:      RWO
VolumeMode:        Filesystem
Capacity:          100Ki
Node Affinity:     
  Required Terms:  
    Term 0:        kubernetes.io/hostname in [ubuntud]
Message:           
Source:
    Type:  LocalVolume (a persistent volume backed by local storage on a node)
    Path:  /tmp
Events:    &lt;none&gt;

```

可以看到PV处于**Available**状态。 然后我们创建绑定其的PVC：

```
kubectl create -f default_storage_class_pvc.yaml 

```

过段时间后我们查看PVC状态。

```
kubectl describe persistentvolumeclaims default-storage-class-pvc

```

```
Name:          default-storage-class-pvc
Namespace:     default
StorageClass:  
Status:        Bound
Volume:        default-storage-class-pv
Labels:        &lt;none&gt;
Annotations:   pv.kubernetes.io/bind-completed: yes
Finalizers:    [kubernetes.io/pvc-protection]
Capacity:      100Ki
Access Modes:  RWO
VolumeMode:    Filesystem
Used By:       &lt;none&gt;
Events:        &lt;none&gt;

```

可以看到PVC的状态是Bound（已绑定）。 最后我们看下PV的状态，它的状态也变成了**Bound**（已绑定）。至此，该PV和PVC已经绑定了。

```
kubectl describe persistentvolume default-storage-class-pv

```

```
Name:              default-storage-class-pv
Labels:            &lt;none&gt;
Annotations:       pv.kubernetes.io/bound-by-controller: yes
Finalizers:        [kubernetes.io/pv-protection]
StorageClass:      
Status:            Bound
Claim:             default/default-storage-class-pvc
Reclaim Policy:    Retain
Access Modes:      RWO
VolumeMode:        Filesystem
Capacity:          100Ki
Node Affinity:     
  Required Terms:  
    Term 0:        kubernetes.io/hostname in [ubuntud]
Message:           
Source:
    Type:  LocalVolume (a persistent volume backed by local storage on a node)
    Path:  /tmp
Events:    &lt;none&gt;

```

**已经绑定的PV不可以再绑定PVC**。我们创建一个新的PVC，进行测试

```
# default_storage_class_pvc_invalid.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: default-storage-class-pvc-invalid
spec:
  resources:
    requests:
      storage: 10Ki
  volumeName: default-storage-class-pv
  accessModes:
    - ReadWriteOnce

```

```
 kubectl create -f default_storage_class_pvc_invalid.yaml

```

>  
 persistentvolumeclaim/default-storage-class-pvc-invalid created 


显示创建成功，但是实际状态是**Pending**。原因是default-storage-class-pv已经绑定到其他PVC。

```
kubectl describe persistentvolumeclaims default-storage-class-pvc-invalid 

```

```
Name:          default-storage-class-pvc-invalid
Namespace:     default
StorageClass:  
Status:        Pending
Volume:        default-storage-class-pv
Labels:        &lt;none&gt;
Annotations:   &lt;none&gt;
Finalizers:    [kubernetes.io/pvc-protection]
Capacity:      0
Access Modes:  
VolumeMode:    Filesystem
Used By:       &lt;none&gt;
Events:
  Type     Reason         Age               From                         Message
  ----     ------         ----              ----                         -------
  Warning  FailedBinding  8s (x2 over 22s)  persistentvolume-controller  volume "default-storage-class-pv" already bound to a different claim.

```

## 删除过程中的状态变化

我们先删掉上面创建的PVC

```
kubectl delete persistentvolumeclaims default-storage-class-pvc-invalid
kubectl delete persistentvolumeclaims default-storage-class-pvc

```

然后观察PV的变化

```
kubectl describe persistentvolume default-storage-class-pv 

```

```
Name:              default-storage-class-pv
Labels:            &lt;none&gt;
Annotations:       pv.kubernetes.io/bound-by-controller: yes
Finalizers:        [kubernetes.io/pv-protection]
StorageClass:      
Status:            Released
Claim:             default/default-storage-class-pvc
Reclaim Policy:    Retain
Access Modes:      RWO
VolumeMode:        Filesystem
Capacity:          100Ki
Node Affinity:     
  Required Terms:  
    Term 0:        kubernetes.io/hostname in [ubuntud]
Message:           
Source:
    Type:  LocalVolume (a persistent volume backed by local storage on a node)
    Path:  /tmp
Events:    &lt;none&gt;

```

此时PV因为绑定的PVC被删除，而其persistentVolumeReclaimPolicy选择了Retain，资源没有被回收，而变成了Released状态。卷的状态如下：
- Available（可用）-- 卷是一个空闲资源，尚未绑定到任何申领；- Bound（已绑定）-- 该卷已经绑定到某申领；- Released（已释放）-- 所绑定的申领已被删除，但是资源尚未被集群回收；- Failed（失败）-- 卷的自动回收操作失败。
这个时候我们再创建上述PVC，还是会处于pending状态。因为PV没有处于Available状态。

```
kubectl create -f default_storage_class_pvc.yaml

```

>  
 persistentvolumeclaim/default-storage-class-pvc created 


```
kubectl describe persistentvolumeclaims default-storage-class-pvc

```

```
Name:          default-storage-class-pvc
Namespace:     default
StorageClass:  
Status:        Pending
Volume:        default-storage-class-pv
Labels:        &lt;none&gt;
Annotations:   &lt;none&gt;
Finalizers:    [kubernetes.io/pvc-protection]
Capacity:      0
Access Modes:  
VolumeMode:    Filesystem
Used By:       &lt;none&gt;
Events:
  Type     Reason         Age   From                         Message
  ----     ------         ----  ----                         -------
  Warning  FailedBinding  8s    persistentvolume-controller  volume "default-storage-class-pv" already bound to a different claim.

```

## 再绑定Released状态的PV

使用下面指令，删除描述绑定信息的claimRef段。

```
kubectl edit persistentvolume default-storage-class-pv

```

```
# Please edit the object below. Lines beginning with a '#' will be ignored,
# and an empty file will abort the edit. If an error occurs while saving this file will be
# reopened with the relevant failures.
#
apiVersion: v1
kind: PersistentVolume
metadata:
  annotations:
    pv.kubernetes.io/bound-by-controller: "yes"
  creationTimestamp: "2023-08-09T09:26:04Z"
  finalizers:
  - kubernetes.io/pv-protection
  name: default-storage-class-pv
  resourceVersion: "285190"
  uid: 09782be4-09b9-4116-9b44-8dbb75f08dbf
spec:
  accessModes:
  - ReadWriteOnce
  capacity:
    storage: 100Ki
  claimRef:
    apiVersion: v1
    kind: PersistentVolumeClaim
    name: default-storage-class-pvc
    namespace: default
    resourceVersion: "285153"
    uid: c55398f4-77cd-4627-8a11-57b0e049c594
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
  persistentVolumeReclaimPolicy: Retain
  volumeMode: Filesystem
status:
  phase: Released

```

保存完后过一会儿，PV就会变成Available状态。而之前处于Pending状态的PVC也会因为PV的状态变化从Pending变成Bound状态，PV也会进而变成Bound状态

```
kubectl describe persistentvolume default-storage-class-pv 

```

```
Name:              default-storage-class-pv
Labels:            &lt;none&gt;
Annotations:       pv.kubernetes.io/bound-by-controller: yes
Finalizers:        [kubernetes.io/pv-protection]
StorageClass:      
Status:            Bound
Claim:             default/default-storage-class-pvc
Reclaim Policy:    Retain
Access Modes:      RWO
VolumeMode:        Filesystem
Capacity:          100Ki
Node Affinity:     
  Required Terms:  
    Term 0:        kubernetes.io/hostname in [ubuntud]
Message:           
Source:
    Type:  LocalVolume (a persistent volume backed by local storage on a node)
    Path:  /tmp
Events:    &lt;none&gt;

```

```
kubectl describe persistentvolumeclaims default-storage-class-pvc

```

```
Name:          default-storage-class-pvc
Namespace:     default
StorageClass:  
Status:        Bound
Volume:        default-storage-class-pv
Labels:        &lt;none&gt;
Annotations:   pv.kubernetes.io/bind-completed: yes
Finalizers:    [kubernetes.io/pvc-protection]
Capacity:      100Ki
Access Modes:  RWO
VolumeMode:    Filesystem
Used By:       &lt;none&gt;
Events:        &lt;none&gt;

```

## 参考资料
- - 