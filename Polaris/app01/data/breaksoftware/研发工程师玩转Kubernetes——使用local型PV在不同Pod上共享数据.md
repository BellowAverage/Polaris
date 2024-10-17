
--- 
title:  研发工程师玩转Kubernetes——使用local型PV在不同Pod上共享数据 
tags: []
categories: [] 

---


#### 大纲
- - - - - 


在一文中，我们使用了hostPath类型卷在一个Node上实现了不同Pod的数据共享。本节我们将使用local型持久卷（PV）来实现。

## PV清单

```
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
    path: /tmp/default_storage_class_pv
  nodeAffinity:
    required:
      nodeSelectorTerms:
      - matchExpressions:
        - key: kubernetes.io/hostname
          operator: In
          values:
          - ubuntud

```

事先我们在Node ubuntud上创建一个空的目录/tmp/default_storage_class_pv。然后限定其大小是100K（后面测试发现不能控制住）。

## PVC清单

```
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

PVC通过volumeName先PV default-storage-class-pv申请了10K空间（后面测试发现不能控制住）。

## Pod使用VPC

```
# local_deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: local-pv-app-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: local-pv-app
  template:
    metadata:
      labels:
        app: local-pv-app
    spec:
      containers:
      - name: local-pv-app
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
          claimName: default-storage-class-pvc

```

在spec.volumes.persistentVolumeClaim.claimName中，我们定义了之前申请的PVC名称。这样PVC就和这个Pod上的卷（local-pvc-volume）产生了关联。 在spec.containers[0].volumeMounts[0].name中，我们设置了Pod上卷的名称。mountPath表示挂载位置。即将该Pod上的卷（local-pvc-volume）挂载到/tempdir目录。

## 测试

依次创建完PV、PVC和Deployment后，我们观察不同Pod上表现。

```
kubectl exec pods/local-pv-app-deployment-56d955856f-llgvr -- tail -f /tempdir/lockfile

```

>  
 local-pv-app-deployment-56d955856f-llgvr write something to lockfile local-pv-app-deployment-56d955856f-llgvr write something to lockfile local-pv-app-deployment-56d955856f-llgvr write something to lockfile …… 


```
kubectl logs pods/local-pv-app-deployment-56d955856f-2hq28

```

>  
 local-pv-app-deployment-56d955856f-llgvr write something to lockfile local-pv-app-deployment-56d955856f-llgvr write something to lockfile local-pv-app-deployment-56d955856f-llgvr write something to lockfile …… 


可以发现Deployment创建的两个Pod共享了/tempdir/lockfile文件，且local-pv-app-deployment-56d955856f-llgvr负责写入，local-pv-app-deployment-56d955856f-2hq28负责读取。

## storage有效性

理论上，如果/tempdir/lockfile文件大小达到PVC申请的10K或者PV规定的100K时，脚本继续写入将失败。但是我们通过频繁获取文件大小会发现，该文件大小会一直膨胀。

```
kubectl exec pods/local-pv-app-deployment-56d955856f-llgvr -- ls -lh /tempdir/lockfile

```

>  
 -rw-r–r-- 1 root root 2.4K Aug 9 10:25 /tempdir/lockfile -rw-r–r-- 1 root root 9.8K Aug 9 10:26 /tempdir/lockfile -rw-r–r-- 1 root root 10.0K Aug 9 10:26 /tempdir/lockfile -rw-r–r-- 1 root root 10.1K Aug 9 10:26 /tempdir/lockfile -rw-r–r-- 1 root root 99.7K Aug 9 10:49 /tempdir/lockfile -rw-r–r-- 1 root root 100.0K Aug 9 10:49 /tempdir/lockfile -rw-r–r-- 1 root root 100.1K Aug 9 10:49 /tempdir/lockfile -rw-r–r-- 1 root root 593.4K Aug 9 12:51 /tempdir/lockfile 

