
--- 
title:  研发工程师玩转Kubernetes——PVC使用Label和storage选择PV 
tags: []
categories: [] 

---


#### 大纲
- - - <ul><li>


在和中，我们介绍了指定VPC的spec.volumeName为PV名称来绑定它们的方法。本文将介绍PVC在创建时，系统自动选择绑定哪个PV。 在设计上，PV是系统管理员分配的，它用于隔绝具体是哪种介质。比如一些PV来源于谷歌云，一些PV来源于阿里云，还有一些PV来源于AWS。 <img src="https://img-blog.csdnimg.cn/c2c0c6396c08429e8a1c1f4633e8088b.png" alt="在这里插入图片描述"> 使用者只要通过PVC向其申请使用即可。 <img src="https://img-blog.csdnimg.cn/02fa37a7a59b4915b6e101d30391306a.png" alt="在这里插入图片描述"> 申请时可以通过spec.volumeName指定特定名称PV，还可以使用spec.selector在一堆PV中选择符合条件的PV。

## 创建多个PV

我们分别使用下面三个配置创建storage为256K、512K和1M的PV。它们都有名字是volume，值是lb-default-storage-class-pv的label。

```
# default_storage_class_pv_256k.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: default-storage-class-pv-256k
  labels:
    volume: lb-default-storage-class-pv
spec:
  capacity:
    storage: 256Ki
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

```
# default_storage_class_pv_512k.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: default-storage-class-pv-256k
  labels:
    volume: lb-default-storage-class-pv
spec:
  capacity:
    storage: 512Ki
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

```
# default_storage_class_pv_1024k.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: default-storage-class-pv-256k
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

## 创建带选择功能的PVC

PVC申请的空间是600K，介于512K和1M。

```
# default_storage_class_pvc_600k.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: default-storage-class-pvc-600k
spec:
  resources:
    requests:
      storage: 600Ki
  accessModes:
    - ReadWriteOnce
  selector:
    matchLabels:
      volume: lb-default-storage-class-pv

```

创建之后，我们查看该PVC的信息。

```
kubectl describe persistentvolumeclaims default-storage-class-pvc-600k 

```

```
Name:          default-storage-class-pvc-600k
Namespace:     default
StorageClass:  
Status:        Bound
Volume:        default-storage-class-pv-1024k
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

可以看到，因为这三个PV的Label都符合PVC的选择器。但是由于256K和512K的PV都小于600K的要求，于是它只能选择最接近它的1M大小的PV。

### 不匹配的Label

我们创建一个Label不匹配的PVC清单，并创建它。

```
# default_storage_class_pvc_100k_not_match.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: default-storage-class-pvc-100k-not-match
spec:
  resources:
    requests:
      storage: 100Ki
  accessModes:
    - ReadWriteOnce
  selector:
    matchLabels:
      volume: lb-default-storage-class-pv-not-match

```

可以看到它一直处于Pending状态，因为没有符合Label要求的PV。

```
kubectl describe persistentvolumeclaims default-storage-class-pvc-100k-not-match

```

```
Name:          default-storage-class-pvc-100k-not-match
Namespace:     default
StorageClass:  
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
  Type    Reason         Age               From                         Message
  ----    ------         ----              ----                         -------
  Normal  FailedBinding  5s (x2 over 11s)  persistentvolume-controller  no persistent volumes available for this claim and no storage class is set

```

## 无法满足大小的PVC

之前创建的600K大小的default-storage-class-pvc-600k已经把default-storage-class-pv-256k占用了，只剩下512K和256K大小的PV。 我们再创建一个不满足剩余PV大小的PVC。

```
# default_storage_class_pvc_700k.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: default-storage-class-pvc-700k
spec:
  resources:
    requests:
      storage: 700Ki
  accessModes:
    - ReadWriteOnce
  selector:
    matchLabels:
      volume: lb-default-storage-class-pv

```

观察其状态，可以发现其也处于Pending状态。

```
kubectl describe persistentvolumeclaims default-storage-class-pvc-700k 

```

```
Name:          default-storage-class-pvc-700k
Namespace:     default
StorageClass:  
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
  Type    Reason         Age              From                         Message
  ----    ------         ----             ----                         -------
  Normal  FailedBinding  8s (x2 over 9s)  persistentvolume-controller  no persistent volumes available for this claim and no storage class is set

```

## 延迟绑定

对于处于Pending状态的PVC，只要我们创建符合条件的PV，系统就会自动将其绑定。 创建下面的PV，它大小是2M，可以满足上面700K请求空间的PVC。

```
# default_storage_class_pv_2m.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: default-storage-class-pv-2048k
  labels:
    volume: lb-default-storage-class-pv
spec:
  capacity:
    storage: 2Mi
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

然后再观察之前处于Pending状态的PVC状态。可以看到其变成了Bound状态，且其绑定的PV就是刚创建的符合其条件的default-storage-class-pv-2048k。

```
kubectl describe persistentvolumeclaims default-storage-class-pvc-700k

```

```
Name:          default-storage-class-pvc-700k
Namespace:     default
StorageClass:  
Status:        Bound
Volume:        default-storage-class-pv-2048k
Labels:        &lt;none&gt;
Annotations:   pv.kubernetes.io/bind-completed: yes
               pv.kubernetes.io/bound-by-controller: yes
Finalizers:    [kubernetes.io/pvc-protection]
Capacity:      2Mi
Access Modes:  RWO
VolumeMode:    Filesystem
Used By:       &lt;none&gt;
Events:
  Type    Reason         Age                     From                         Message
  ----    ------         ----                    ----                         -------
  Normal  FailedBinding  2m36s (x26 over 8m37s)  persistentvolume-controller  no persistent volumes available for this claim and no storage class is set

```
