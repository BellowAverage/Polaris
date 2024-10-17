
--- 
title:  研发工程师玩转Kubernetes——使用emptyDir在同一Pod不同容器间共享数据 
tags: []
categories: [] 

---


#### 大纲
- - - 


kubernets可以通过emptyDir实现在**同一Pod的不同容器间**共享文件系统。 <img src="https://img-blog.csdnimg.cn/a494198410c24ab8809bca3271b792c0.png" alt="在这里插入图片描述"> 正如它的名字，当Pod被创建时，emptyDir卷会被创建，这个时候它是一个空的文件夹；当Pod被删除时，emptyDir卷也会被**永久**删除。

## 同一Pod上不同容器之间共享

```
# bash
if [ -f /tempdir/lockfile ] &amp;&amp; ! {<!-- --> set -C; 2&gt;/dev/null &gt;/tempdir/lockfile; }; then
    tail -f /tempdir/lockfile
else
    exec 3&gt;/tempdir/lockfile
    if [ -n "$POD_NAME" ]; then
        pod_name=$POD_NAME
    else
        pod_name="unknown_pod"
    fi
    if [ -n "$CONTAINER_NAME" ]; then
        container_name=$CONTAINER_NAME
    else
        container_name="unknown_container"
    fi
    while true; do
        echo "$pod_name $container_name write something to lockfile" &gt;&amp;3
        sleep 5
    done
fi

```

我们使用上面这段脚本，会检测/tempdir/lockfile文件是否存在。如果不存在则创建这个文件，并获取Pod和Container名称，然后每隔5秒钟在/tempdir/lockfile写入一句话；如果存在，则不停打印新写入这个文件的内容。 然后使用下面的清单文件创建一个deployment

```
# emptydir_same_pod.yaml 
apiVersion: apps/v1
kind: Deployment
metadata:
  name: emptydir-deployment
spec:
  selector:
    matchLabels:
      app: emptydir-container
  replicas: 1
  template:
    metadata:
      labels:
        app: emptydir-container
    spec:
      containers:
      - name: emptydir-container1
        image: busybox
        command: ["/bin/sh", "-c", "if [ -f /tempdir/lockfile ] &amp;&amp; ! { set -C; 2&gt;/dev/null &gt;/tempdir/lockfile; }; then tail -f /tempdir/lockfile; else exec 3&gt;/tempdir/lockfile; if [ -n \"$POD_NAME\" ]; then pod_name=$POD_NAME; else pod_name=\"unknown_pod\"; fi; if [ -n \"$CONTAINER_NAME\" ]; then container_name=$CONTAINER_NAME; else container_name=\"unknown_container\"; fi; while true; do echo \"$pod_name $container_name write something to lockfile\" &gt;&amp;3; sleep 5; done; fi;"]
        volumeMounts:
        - name: emptydir-volume
          mountPath: /tempdir
        env:
        - name: POD_NAME
          valueFrom:
            fieldRef:
              fieldPath: metadata.name
        - name: CONTAINER_NAME
          value: emptydir-container1
      - name: emptydir-container2
        image: busybox
        command: ["/bin/sh", "-c" ,"if [ -f /tempdir/lockfile ] &amp;&amp; ! { set -C; 2&gt;/dev/null &gt;/tempdir/lockfile; }; then tail -f /tempdir/lockfile; else exec 3&gt;/tempdir/lockfile; if [ -n \"$POD_NAME\" ]; then pod_name=$POD_NAME; else pod_name=\"unknown_pod\"; fi; if [ -n \"$CONTAINER_NAME\" ]; then container_name=$CONTAINER_NAME; else container_name=\"unknown_container\"; fi; while true; do echo \"$pod_name $container_name write something to lockfile\" &gt;&amp;3; sleep 5; done; fi;"]
        volumeMounts:
        - name: emptydir-volume
          mountPath: /tempdir
        env:
        - name: POD_NAME
          valueFrom:
            fieldRef:
              fieldPath: metadata.name
        - name: CONTAINER_NAME
          value: emptydir-container2
      volumes:
      - name: emptydir-volume
        emptyDir: 
          medium: Memory
          sizeLimit: 1Gi

```

这个Deployment会创建一个Pod，这个Pod会含有两个容器：emptydir-container1和emptydir-container2。 使用下面命令创建这个部署

```
kubectl create -f emptydir_same_pod.yaml 

```

>  
 deployment.apps/emptydir-deployment created 


然后登录到容器中查看/tempdir/lockfile文件的内容

```
kubectl exec pods/emptydir-deployment-75c6545df5-slznj --container emptydir-container1 -it -- tail -f /tempdir/lockfile

```

>  
 emptydir-deployment-75c6545df5-slznj emptydir-container1 write something to lockfile emptydir-deployment-75c6545df5-slznj emptydir-container1 write something to lockfile emptydir-deployment-75c6545df5-slznj emptydir-container1 write something to lockfile …… 


```
kubectl exec pods/emptydir-deployment-75c6545df5-slznj --container emptydir-container2 -it -- tail -f /tempdir/lockfile

```

>  
 emptydir-deployment-75c6545df5-slznj emptydir-container1 write something to lockfile emptydir-deployment-75c6545df5-slznj emptydir-container1 write something to lockfile emptydir-deployment-75c6545df5-slznj emptydir-container1 write something to lockfile …… 


可以看到emptydir-container1容器在持续写入内容；emptydir-container2因为检测到/tempdir/lockfile文件存在，就不会写入文件。 通过下面指令可以看到emptydir-container2的输出

```
kubectl logs pods/emptydir-deployment-75c6545df5-slznj --container emptydir-container2

```

>  
 emptydir-deployment-75c6545df5-slznj emptydir-container1 write something to lockfile emptydir-deployment-75c6545df5-slznj emptydir-container1 write something to lockfile emptydir-deployment-75c6545df5-slznj emptydir-container1 write something to lockfile …… 


## 同一个Node的不同Pod间不可以共享

我们应用Pod亲和性，让Deployment在同一个Node上部署相同的Pod。

```
# emptydir_same_node.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: emptydir-same-node-deployment
spec:
  selector:
    matchLabels:
      app: emptydir-container
  replicas: 2
  template:
    metadata:
      labels:
        app: emptydir-container
    spec:
      affinity:
        podAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
          - labelSelector:
                matchExpressions:
                - key: app
                  operator: In
                  values:
                  - emptydir-container
            topologyKey: "kubernetes.io/hostname"
      containers:
      - name: emptydir-container
        image: busybox
        command: ["/bin/sh", "-c", "if [ -f /tempdir/lockfile ] &amp;&amp; ! { set -C; 2&gt;/dev/null &gt;/tempdir/lockfile; }; then tail -f /tempdir/lockfile; else exec 3&gt;/tempdir/lockfile; if [ -n \"$POD_NAME\" ]; then pod_name=$POD_NAME; else pod_name=\"unknown_pod\"; fi; if [ -n \"$CONTAINER_NAME\" ]; then container_name=$CONTAINER_NAME; else container_name=\"unknown_container\"; fi; while true; do echo \"$pod_name $container_name write something to lockfile\" &gt;&amp;3; sleep 5; done; fi;"]
        volumeMounts:
        - name: emptydir-volume
          mountPath: /tempdir
        env:
        - name: POD_NAME
          valueFrom:
            fieldRef:
              fieldPath: metadata.name
        - name: CONTAINER_NAME
          value: emptydir-container
      volumes:
      - name: emptydir-volume
        emptyDir: 
          medium: Memory
          sizeLimit: 1Gi

```

创建好这个部署后，我们可以通过下面指令确认它们被部署在同一个Node（ubuntuc）上。

```
kubectl get pods -o wide

```

```
NAME                                             READY   STATUS    RESTARTS   AGE   IP            NODE      NOMINATED NODE   READINESS GATES
emptydir-same-node-deployment-6b6cfbb769-vhj7k   1/1     Running   0          34s   10.1.43.199   ubuntuc   &lt;none&gt;           &lt;none&gt;
emptydir-same-node-deployment-6b6cfbb769-mgh8h   1/1     Running   0          34s   10.1.43.198   ubuntuc   &lt;none&gt;           &lt;none&gt;

```

然后查看每个Pod上/tempdir/lockfile文件的内容

```
kubectl exec pods/emptydir-same-node-deployment-6b6cfbb769-mgh8h --container emptydir-container -it -- tail -f /tempdir/lockfile

```

>  
 emptydir-same-node-deployment-6b6cfbb769-mgh8h emptydir-container write something to lockfile emptydir-same-node-deployment-6b6cfbb769-mgh8h emptydir-container write something to lockfile emptydir-same-node-deployment-6b6cfbb769-mgh8h emptydir-container write something to lockfile …… 


```
kubectl exec pods/emptydir-same-node-deployment-6b6cfbb769-vhj7k --container emptydir-container -it -- tail -f /tempdir/lockfile

```

>  
 emptydir-same-node-deployment-6b6cfbb769-vhj7k emptydir-container write something to lockfile emptydir-same-node-deployment-6b6cfbb769-vhj7k emptydir-container write something to lockfile emptydir-same-node-deployment-6b6cfbb769-vhj7k emptydir-container write something to lockfile …… 


可以看到它们打印出来的Pod名称不同，即可以证明：同一个Node上不同Pod创建的emptyDir是不同的。

## 参考资料
- 