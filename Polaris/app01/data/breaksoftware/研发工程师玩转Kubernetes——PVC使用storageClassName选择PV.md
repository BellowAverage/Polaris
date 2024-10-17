
--- 
title:  研发工程师玩转Kubernetes——PVC使用storageClassName选择PV 
tags: []
categories: [] 

---


#### 大纲
- - - - 


## StorageClass清单

```
# local_storage_class_immediate.yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: local-storage-class-immediate
provisioner: kubernetes.io/no-provisioner
volumeBindingMode: Immediate

```

我们创建了一个名字叫local-storage-class，使用本地存储的StorageClass。它的绑定类型是Immediate（立即）。Immediate 模式表示一旦创建了 PersistentVolumeClaim 也就完成了卷绑定。

## PV清单

这次我们创建的PV没有设置Label，而是设置了storageClassName字段为上述StorageClass的名字。

```
# local_storage_class_immediate_pv_512k.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: local-storage-class-immediate-pv-512k
spec:
  capacity:
    storage:  512Ki
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

```
# local_storage_class_immediate_pv_1024k.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: local-storage-class-immediate-pv-1024k
spec:
  capacity:
    storage:  1024Ki
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

## PVC清单

这个清单也没使用spec.selector对PV的Label做选择，而是使用了storageClassName。

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

## 测试

为了验证测试，我们同时创建下面这个PV，它只是在storage上满足上述PVC申请。

```
# default_storage_class_pv_1024k.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: default-storage-class-pv-1024k
  labels:
    volume: lb-default-storage-class-pv
spec:
  capacity:
    storage: 1Mi
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

使用下面指令创建上述资源

```
kubectl create -f local_storage_class_immediate.yaml -f default_storage_class_pv_1024k.yaml  -f local_storage_class_immediate_pv_1024k.yaml -f local_storage_class_immediate_pv_512k.yaml -f local_storage_class_immediate_pvc_600k.yaml 

```

查看PVC的状态，可以发现系统让storageClassName名相同的PV和PVC进行了绑定。

```
kubectl describe persistentvolumeclaims  local-storage-class-immediate-pvc-600k 

```

```
Name:          local-storage-class-immediate-pvc-600k
Namespace:     default
StorageClass:  local-storage-class-immediate
Status:        Bound
Volume:        local-storage-class-immediate-pv-1024k
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

为了进一步测试，我们再创建相同配置，但是名字不同的PVC，看它是否会选择没有设置相同storageClassName的PV。

```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: local-storage-class-immediate-pvc-600k-1
spec:
  resources:
    requests:
      storage: 600Ki
  accessModes:
    - ReadWriteOnce
  storageClassName: local-storage-class-immediate

```

```
kubectl describe persistentvolumeclaims local-storage-class-immediate-pvc-600k-1

```

```
Name:          local-storage-class-immediate-pvc-600k-1
Namespace:     default
StorageClass:  local-storage-class-immediate
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
  Type     Reason              Age   From                         Message
  ----     ------              ----  ----                         -------
  Warning  ProvisioningFailed  6s    persistentvolume-controller  no volume plugin matched name: kubernetes.io/no-provisioner

```

可以看到即使storage满足PVC申请的大小，但是由于storageClassName不同，它还是没有选择default-storage-class-pv-1024k这个PV。

```
kubectl describe persistentvolume default-storage-class-pv-1024k 

```

```
Name:              default-storage-class-pv-1024k
Labels:            volume=lb-default-storage-class-pv
Annotations:       &lt;none&gt;
Finalizers:        [kubernetes.io/pv-protection]
StorageClass:      
Status:            Available
Claim:             
Reclaim Policy:    Retain
Access Modes:      RWO
VolumeMode:        Filesystem
Capacity:          1Mi
Node Affinity:     
  Required Terms:  
    Term 0:        kubernetes.io/hostname in [ubuntud]
Message:           
Source:
    Type:  LocalVolume (a persistent volume backed by local storage on a node)
    Path:  /tmp
Events:    &lt;none&gt;

```
