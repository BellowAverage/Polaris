
--- 
title:  研发工程师玩转Kubernetes——通过PV的节点亲和性影响Pod部署 
tags: []
categories: [] 

---


#### 大纲
- - - - - <ul><li>- - 


在一文中，我们利用Node亲和性，让Pod部署在节点ubuntud上。因为Pod使用的PVC可以部署在节点ubuntuc或者ubuntud上，而系统为了让Pod可以部署成功，则让PVC与Pod亲和的ubuntud上的PV绑定。这样Pod在自身节点亲和性和PVC上都满足了条件。 <img src="https://img-blog.csdnimg.cn/26000c1e9ee0401693672ebc36144791.png" alt="在这里插入图片描述"> 在一些业务场景下，我们通过磁盘来保存数据，而程序通过数据设置自身状态。如果一旦一个Pod崩溃，我们希望新补充的Pod可以延续之前的状态。这个时候我们就可以使用PV的节点亲和性来完成上述调度。 <img src="https://img-blog.csdnimg.cn/0538419e0fac49a892e874584445f22b.png" alt="在这里插入图片描述">

## PersistentVolume

下面PersistentVolume配置的节点亲和性要求资源只会在ubuntuc或者ubuntud上创建。

```
# default_storage_class_pv_ubuntucd.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: default-storage-class-pv-ubuntucd
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
          - ubuntuc
          - ubuntud

```

## PersistentVolumeClaim

PVC直接和上述PV绑定。

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

## Deployment

下面这个Deployment会创建2个Pod。由于Pod的反亲和性，它们被强制要求调度到不同Node上。

```
# default_deployment_one_on_node.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: default-pv-app-one-on-node-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: default-pv-app-one-on-node
  template:
    metadata:
      labels:
        app: default-pv-app-one-on-node
    spec:
      containers:
      - name: default-pv-app-one-on-node
        image: busybox
        command: ["/bin/sh", "-c", "if [ -f /tempdir/lockfile ] &amp;&amp; ! { set -C; 2&gt;/dev/null &gt;/tempdir/lockfile; }; then tail -f /tempdir/lockfile; else exec 3&gt;/tempdir/lockfile; if [ -n \"$POD_NAME\" ]; then name=$POD_NAME; else name=\"unknown\"; fi; while true; do echo \"this is $name.$name write something to lockfile\"; echo \"$name write something to lockfile\" &gt;&amp;3; sleep 1; done; fi"]  
        volumeMounts:
        - name: default-pvc-volume
          mountPath: /tempdir
        env:
        - name: POD_NAME
          valueFrom:
            fieldRef:
              fieldPath: metadata.name
      volumes:
      - name: default-pvc-volume
        persistentVolumeClaim:
          claimName: default-storage-class-pvc-600k
      affinity:
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
          - labelSelector:
                matchExpressions:
                - key: app
                  operator: In
                  values:
                  - default-pv-app-one-on-node
            topologyKey: "kubernetes.io/hostname"

```

## 实验

### 查看Pod状态

```
kubectl get pod -o wide

```

```
NAME                                                    READY   STATUS    RESTARTS   AGE   IP             NODE      NOMINATED NODE   READINESS GATES
default-pv-app-one-on-node-deployment-76bf96bb5-7tzxd   1/1     Running   0          21s   10.1.202.210   ubuntud   &lt;none&gt;           &lt;none&gt;
default-pv-app-one-on-node-deployment-76bf96bb5-mtk67   1/1     Running   0          21s   10.1.43.207    ubuntuc   &lt;none&gt;           &lt;none&gt;

```

可以看到两个Pod分别被调度到ubuntuc和ubuntud上。

### 调整Pod数量

```
kubectl scale deployment default-pv-app-one-on-node-deployment --replicas 3

```

```
kubectl get pod -o wide

```

```
NAME                                                    READY   STATUS    RESTARTS   AGE   IP             NODE      NOMINATED NODE   READINESS GATES
default-pv-app-one-on-node-deployment-76bf96bb5-7tzxd   1/1     Running   0          46s   10.1.202.210   ubuntud   &lt;none&gt;           &lt;none&gt;
default-pv-app-one-on-node-deployment-76bf96bb5-mtk67   1/1     Running   0          46s   10.1.43.207    ubuntuc   &lt;none&gt;           &lt;none&gt;
default-pv-app-one-on-node-deployment-76bf96bb5-9wvq5   0/1     Pending   0          3s    &lt;none&gt;         &lt;none&gt;    &lt;none&gt;           &lt;none&gt;

```

可以看到，新创建的Pod处于Pending状态。当前系统还有ubuntua、ubuntud、ubunutue三个节点，它们由于不能满足Pod对PVC的要求（实际是PVC绑定的PV的要求），而没有被调度到。

```
kubectl get  nodes

```

```
NAME      STATUS   ROLES    AGE     VERSION
ubuntud   Ready    &lt;none&gt;   2d22h   v1.27.4
ubuntuc   Ready    &lt;none&gt;   2d23h   v1.27.4
ubuntue   Ready    &lt;none&gt;   2d22h   v1.27.4
ubuntub   Ready    &lt;none&gt;   2d23h   v1.27.4
ubuntua   Ready    &lt;none&gt;   2d23h   v1.27.4

```

### 恢复Pod

```
kubectl scale deployment default-pv-app-one-on-node-deployment --replicas 2
kubectl delete pod default-pv-app-one-on-node-deployment-76bf96bb5-7tzxd 
kubectl get pod -o wide

```

```
NAME                                                    READY   STATUS    RESTARTS   AGE     IP             NODE      NOMINATED NODE   READINESS GATES
default-pv-app-one-on-node-deployment-76bf96bb5-mtk67   1/1     Running   0          2m12s   10.1.43.207    ubuntuc   &lt;none&gt;           &lt;none&gt;
default-pv-app-one-on-node-deployment-76bf96bb5-qqtlm   1/1     Running   0          39s     10.1.202.211   ubuntud   &lt;none&gt;           &lt;none&gt;

```

可以看到Pod被正确的调度到刚被删掉Pod的Node上，进而可以继续使用它的PV，从而实现服务状态恢复和衔接上的目的。
