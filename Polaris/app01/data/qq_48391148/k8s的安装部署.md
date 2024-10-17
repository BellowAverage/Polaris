
--- 
title:  k8s的安装部署 
tags: []
categories: [] 

---
**目录**

















































### k8s是什么？有什么作用？

>  
 **        kubernetes 是 k8s的全称** 
 **        k8s是用来管理容器的，可以用来管理容器的，可以用来部署，扩缩，管理容器** 
 **        有代码的地方就可以有k8s** 


容器运行时软件：

>  
 **        管理容器从创建，启动，关闭，镜像相关的操作的软件** 
 **        docker** 
 **        coreos ** 


#### CNCF是什么？

>  
 **CNCF，全称 Cloud Native Computing Foundation，译为云原生计算机基金会** 


####  k8s里面有哪些组件？

>  
 **从角色上来讲的话：master（管理节点）和node（工作节点）** 
 **master上的control plane 组件：** 
 **        1、kube-apiserver ** 
 **                组件：就是一个pod，pod里面有很多的容器，运行相关的软件，会有相应的docker镜像文件** 
 **                API服务器时Kubernetes 控制平面的组件，该组件负责公开了kubernetes API，负责处理接受请求的工作，api服务器时Kubernetes 控制平面的前端** 
 **                k8s的入口，通过这个接口可以了解整个k8s的信息和资源** 
 **        2、etcd：高可用的键值数据库，保存Kubernetes所有集群数据的后台数据库** 
 **        3、scheduler 调度器：负责监视新创建的，未指定运行节点（node）的pods，并选择节点来让Pod在上面运行** 
 **                        pod：是k8s里最小的计算单元，里面可以包含很多的容器，所有的容器共享一个ip地址** 
 **        4、controller-manager 控制器的管理创新** 
 **                        k8s有很多的控制器** 
 **                                deployment 部署pod的控制器** 
 **                                replicaSET  副本控制器** 
 **        5、cloud-controller-manager ** 
 **                        一个Kubernetes 控制平面组件，嵌入了特定于云平台的控制逻辑，云控制器管理器（cloud controller Manager）允许你将你的集群连接到云提供商的API之上，并将于该平台交互的组件同与你的集群交互的组件分离开来** 
  
 **Node组件** 
 **        1、kubelet 会在集群中每个节点（node）上运行，它保证容器（containers）都运行在pod中，启动pod会在node节点服务器上** 
 **        2、kube-proxy  维护节点上的一些网络规则，这些网络规则会允许从集群内部或外部的网络会话与pod进行网络通信** 
 **                网络通信：多个node之间的网络通信，负载均衡** 
  


k8s的使用

>  
 **        pod** 
 **        pv** 
 **        pvc** 
 **        控制器** 
 **        hpa** 


**#############################################################################**  

#### k8s架构图 

<img alt="" height="790" src="https://img-blog.csdnimg.cn/6b365e4c2b354fdeb5b1c3c3cbdc06fe.png" width="1200">

**#############################################################################**  

## k8s的安装部署

>  
 **        1、minikube** 
 **        2、kubeadm    k8s官方推荐的安装k8s的方式** 
 **        3、二进制安装** 
 **        4、第3方的部署工具：rancher等** 


k8s集群的架构

>  
 **        1、单master和多node** 
 **        2、多master和多node  -- 高可用** 
 **                3master  3node  1个负载均衡（nginx）** 


实验环境

>  
 **        1台master，3台node** 
 **        软件：centos7.9  docker** 
 **        硬件：2G/2c** 




### 1、IP地址规划：

>  
 **        k8s-master：192.168.44.210** 
 **        k8s-node1:192.168.44.211** 
 **        k8s-node2:192.168.44.212** 
 **        k8s-node3:192.168.44.213** 


**#############################################################################** 

### 2、关闭firewalld和selinux（在k8s集群master和node上都进行操作）

```
[root@k8s-master ~]# service firewalld stop
Redirecting to /bin/systemctl stop firewalld.service
[root@k8s-master ~]# systemctl disable firewalld
Removed symlink /etc/systemd/system/multi-user.target.wants/firewalld.service.
Removed symlink /etc/systemd/system/dbus-org.fedoraproject.FirewallD1.service.
[root@k8s-master ~]# setenforce 0
[root@k8s-master ~]# getenforce
Permissive

```

**#############################################################################** 

### 3、在所有机器上安装docker

#### 安装yum相关工具，下载docker-ce.repo文件

```
yum install -y yum-utils
```

```
yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
```

####  安装docker-ce软件

```
yum install docker-ce docker-ce-cli containerd.io docker-compose-plugin -y

```

#### 启动docker服务，设置docker开机自启

```
[root@k8s-master yum.repos.d]# systemctl start docker
[root@k8s-master yum.repos.d]# ps aux|grep docker
root      11877  6.1  2.6 1027340 48624 ?       Ssl  17:35   0:00 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
root      12001  0.0  0.0 112824   976 pts/0    S+   17:35   0:00 grep --color=auto docker
[root@k8s-master yum.repos.d]# systemctl enable docker
Created symlink from /etc/systemd/system/multi-user.target.wants/docker.service to /usr/lib/systemd/system/docker.service.
[root@k8s-master yum.repos.d]# 

```

**#############################################################################**

### 4、关闭交换分区

```
[root@k8s-master yum.repos.d]# swapoff -a
[root@k8s-master yum.repos.d]# free -m
              total        used        free      shared  buff/cache   available
Mem:           1819         298         779           9         741        1354
Swap:             0           0           0
[root@k8s-master yum.repos.d]# 

```

**#############################################################################**

### 5、重新命名主机名，并修改hosts文件

```
[root@k8s-master yum.repos.d]# cat &gt;&gt; /etc/hosts &lt;&lt; EOF
&gt; 192.168.44.210 k8s-master
&gt; 192.168.44.211 k8s-node1
&gt; 192.168.44.212 k8s-node2
&gt; 192.168.44.213 k8s-node3
&gt; EOF

```

**#############################################################################** 

### 6、修改一些内核参数

```
[root@k8s-master yum.repos.d]# cat &lt;&lt;EOF &gt;&gt;  /etc/sysctl.conf 
&gt; net.bridge.bridge-nf-call-ip6tables = 1
&gt; net.bridge.bridge-nf-call-iptables = 1
&gt; net.ipv4.ip_nonlocal_bind = 1
&gt; net.ipv4.ip_forward = 1
&gt; vm.swappiness=0
&gt; EOF

```

sysctl -p 让参数生效到内核里面

```
[root@k8s-master yum.repos.d]# sysctl -p
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_nonlocal_bind = 1
net.ipv4.ip_forward = 1
vm.swappiness = 0

```

**#############################################################################**

###  7、安装kubadm，kubctl，kublet软件

添加kubernetes yum软件源

```
[root@k8s-master ~]# cat &gt; /etc/yum.repos.d/kubernetes.repo &lt;&lt; EOF
&gt; [kubernetes]
&gt; name=Kubernetes
&gt; baseurl=https://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64
&gt; enabled=1
&gt; gpgcheck=0
&gt; repo_gpgcheck=0
&gt; gpgkey=https://mirrors.aliyun.com/kubernetes/yum/doc/yum-key.gpg https://mirrors.aliyun.com/kubernetes/yum/doc/rpm-package-key.gpg
&gt; EOF

```

安装kubeadm，kubelet，kubectl，并且指定版本，因为1.24的版本默认运行时环境不是docker了

```
yum install -y kubelet-1.23.6 kubeadm-1.23.6 kubectl-1.23.6
```

设置开机自启，因为kubelet是k8s在node节点上的代理，必须开机要运行的

```
[root@k8s-master ~]# systemctl enable  kubelet
Created symlink from /etc/systemd/system/multi-user.target.wants/kubelet.service to /usr/lib/systemd/system/kubelet.service.

```

**#############################################################################**

### 8、部署kubernetes master

 提前准备coredns:1.8.4的镜像，后面需要使用,需要在每台机器上下载镜像

```
[root@k8s-master ~]# docker pull  coredns/coredns:1.8.4
1.8.4: Pulling from coredns/coredns
c6568d217a00: Pull complete 
bc38a22c706b: Pull complete 
Digest: sha256:6e5a02c21641597998b4be7cb5eb1e7b02c0d8d23cce4dd09f4682d463798890
Status: Downloaded newer image for coredns/coredns:1.8.4
docker.io/coredns/coredns:1.8.4
[root@k8s-master ~]# docker images
REPOSITORY        TAG       IMAGE ID       CREATED         SIZE
coredns/coredns   1.8.4     8d147537fb7d   16 months ago   47.6MB
[root@k8s-master ~]# docker tag coredns/coredns:1.8.4 registry.aliyuncs.com/google_containers/coredns:v1.8.4
[root@k8s-master ~]# docker images
REPOSITORY                                        TAG       IMAGE ID       CREATED         SIZE
coredns/coredns                                   1.8.4     8d147537fb7d   16 months ago   47.6MB
registry.aliyuncs.com/google_containers/coredns   v1.8.4    8d147537fb7d   16 months ago   47.6MB

```

在master服务器上进行初始化操作

```
[root@k8s-master ~]# kubeadm init \
&gt; --apiserver-advertise-address=192.168.44.210 \
&gt; --image-repository registry.aliyuncs.com/google_containers \
&gt; --service-cidr=10.1.0.0/16 \
&gt; --pod-network-cidr=10.244.0.0/16
I0924 22:36:57.310381   20845 version.go:255] remote version is much newer: v1.25.2; falling back to: stable-1.23
[init] Using Kubernetes version: v1.23.12
[preflight] Running pre-flight checks
[preflight] Pulling images required for setting up a Kubernetes cluster
[preflight] This might take a minute or two, depending on the speed of your internet connection
[preflight] You can also perform this action in beforehand using 'kubeadm config images pull'
[certs] Using certificateDir folder "/etc/kubernetes/pki"
[certs] Generating "ca" certificate and key
[certs] Generating "apiserver" certificate and key
[certs] apiserver serving cert is signed for DNS names [k8s-master kubernetes kubernetes.default kubernetes.default.svc kubernetes.default.svc.cluster.local] and IPs [10.1.0.1 192.168.44.210]
[certs] Generating "apiserver-kubelet-client" certificate and key
[certs] Generating "front-proxy-ca" certificate and key
[certs] Generating "front-proxy-client" certificate and key
[certs] Generating "etcd/ca" certificate and key
[certs] Generating "etcd/server" certificate and key
[certs] etcd/server serving cert is signed for DNS names [k8s-master localhost] and IPs [192.168.44.210 127.0.0.1 ::1]
[certs] Generating "etcd/peer" certificate and key
[certs] etcd/peer serving cert is signed for DNS names [k8s-master localhost] and IPs [192.168.44.210 127.0.0.1 ::1]
[certs] Generating "etcd/healthcheck-client" certificate and key
[certs] Generating "apiserver-etcd-client" certificate and key
[certs] Generating "sa" key and public key
[kubeconfig] Using kubeconfig folder "/etc/kubernetes"
[kubeconfig] Writing "admin.conf" kubeconfig file
[kubeconfig] Writing "kubelet.conf" kubeconfig file
[kubeconfig] Writing "controller-manager.conf" kubeconfig file
[kubeconfig] Writing "scheduler.conf" kubeconfig file
[kubelet-start] Writing kubelet environment file with flags to file "/var/lib/kubelet/kubeadm-flags.env"
[kubelet-start] Writing kubelet configuration to file "/var/lib/kubelet/config.yaml"
[kubelet-start] Starting the kubelet
[control-plane] Using manifest folder "/etc/kubernetes/manifests"
[control-plane] Creating static Pod manifest for "kube-apiserver"
[control-plane] Creating static Pod manifest for "kube-controller-manager"
[control-plane] Creating static Pod manifest for "kube-scheduler"
[etcd] Creating static Pod manifest for local etcd in "/etc/kubernetes/manifests"
[wait-control-plane] Waiting for the kubelet to boot up the control plane as static Pods from directory "/etc/kubernetes/manifests". This can take up to 4m0s
[apiclient] All control plane components are healthy after 7.503688 seconds
[upload-config] Storing the configuration used in ConfigMap "kubeadm-config" in the "kube-system" Namespace
[kubelet] Creating a ConfigMap "kubelet-config-1.23" in namespace kube-system with the configuration for the kubelets in the cluster
NOTE: The "kubelet-config-1.23" naming of the kubelet ConfigMap is deprecated. Once the UnversionedKubeletConfigMap feature gate graduates to Beta the default name will become just "kubelet-config". Kubeadm upgrade will handle this transition transparently.
[upload-certs] Skipping phase. Please see --upload-certs
[mark-control-plane] Marking the node k8s-master as control-plane by adding the labels: [node-role.kubernetes.io/master(deprecated) node-role.kubernetes.io/control-plane node.kubernetes.io/exclude-from-external-load-balancers]
[mark-control-plane] Marking the node k8s-master as control-plane by adding the taints [node-role.kubernetes.io/master:NoSchedule]
[bootstrap-token] Using token: 0xp3gm.wzbsahhxwa1dtaeh
[bootstrap-token] Configuring bootstrap tokens, cluster-info ConfigMap, RBAC Roles
[bootstrap-token] configured RBAC rules to allow Node Bootstrap tokens to get nodes
[bootstrap-token] configured RBAC rules to allow Node Bootstrap tokens to post CSRs in order for nodes to get long term certificate credentials
[bootstrap-token] configured RBAC rules to allow the csrapprover controller automatically approve CSRs from a Node Bootstrap Token
[bootstrap-token] configured RBAC rules to allow certificate rotation for all node client certificates in the cluster
[bootstrap-token] Creating the "cluster-info" ConfigMap in the "kube-public" namespace
[kubelet-finalize] Updating "/etc/kubernetes/kubelet.conf" to point to a rotatable kubelet client certificate and key
[addons] Applied essential addon: CoreDNS
[addons] Applied essential addon: kube-proxy

Your Kubernetes control-plane has initialized successfully!

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

Alternatively, if you are the root user, you can run:

  export KUBECONFIG=/etc/kubernetes/admin.conf

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

Then you can join any number of worker nodes by running the following on each as root:

kubeadm join 192.168.44.210:6443 --token 0xp3gm.wzbsahhxwa1dtaeh \
	--discovery-token-ca-cert-hash sha256:bc28a61b1de3bfa7cb95c619ef050fe67238471347b16d9e34e400e405efe0bb 
[root@k8s-master ~]# 

```

完成初始化的新建文件和目录的操作，在master上完成 

```
[root@k8s-master ~]#   mkdir -p $HOME/.kube
[root@k8s-master ~]#   sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
[root@k8s-master ~]#   sudo chown $(id -u):$(id -g) $HOME/.kube/config

```

**#############################################################################** 

### 9、将node节点服务器加入k8s集群

在三台node节点服务器上都执行

```
[root@k8s-node1 ~]# kubeadm join 192.168.44.210:6443 --token 0xp3gm.wzbsahhxwa1dtaeh --discovery-token-ca-cert-hash sha256:bc28a61b1de3bfa7cb95c619ef050fe67238471347b16d9e34e400e405efe0bb 
[preflight] Running pre-flight checks
[preflight] Reading configuration from the cluster...
[preflight] FYI: You can look at this config file with 'kubectl -n kube-system get cm kubeadm-config -o yaml'
[kubelet-start] Writing kubelet configuration to file "/var/lib/kubelet/config.yaml"
[kubelet-start] Writing kubelet environment file with flags to file "/var/lib/kubelet/kubeadm-flags.env"
[kubelet-start] Starting the kubelet
[kubelet-start] Waiting for the kubelet to perform the TLS Bootstrap...

This node has joined the cluster:
* Certificate signing request was sent to apiserver and a response was received.
* The Kubelet was informed of the new secure connection details.

Run 'kubectl get nodes' on the control-plane to see this node join the cluster.

```

```
[root@k8s-node2 ~]# kubeadm join 192.168.44.210:6443 --token 0xp3gm.wzbsahhxwa1dtaeh --discovery-token-ca-cert-hash sha256:bc28a61b1de3bfa7cb95c619ef050fe67238471347b16d9e34e400e405efe0bb 
[preflight] Running pre-flight checks
[preflight] Reading configuration from the cluster...
[preflight] FYI: You can look at this config file with 'kubectl -n kube-system get cm kubeadm-config -o yaml'
[kubelet-start] Writing kubelet configuration to file "/var/lib/kubelet/config.yaml"
[kubelet-start] Writing kubelet environment file with flags to file "/var/lib/kubelet/kubeadm-flags.env"
[kubelet-start] Starting the kubelet
[kubelet-start] Waiting for the kubelet to perform the TLS Bootstrap...

This node has joined the cluster:
* Certificate signing request was sent to apiserver and a response was received.
* The Kubelet was informed of the new secure connection details.

Run 'kubectl get nodes' on the control-plane to see this node join the cluster.

```

```
[root@k8s-node3 ~]# kubeadm join 192.168.44.210:6443 --token 0xp3gm.wzbsahhxwa1dtaeh --discovery-token-ca-cert-hash sha256:bc28a61b1de3bfa7cb95c619ef050fe67238471347b16d9e34e400e405efe0bb 
[preflight] Running pre-flight checks
[preflight] Reading configuration from the cluster...
[preflight] FYI: You can look at this config file with 'kubectl -n kube-system get cm kubeadm-config -o yaml'
[kubelet-start] Writing kubelet configuration to file "/var/lib/kubelet/config.yaml"
[kubelet-start] Writing kubelet environment file with flags to file "/var/lib/kubelet/kubeadm-flags.env"
[kubelet-start] Starting the kubelet
[kubelet-start] Waiting for the kubelet to perform the TLS Bootstrap...

This node has joined the cluster:
* Certificate signing request was sent to apiserver and a response was received.
* The Kubelet was informed of the new secure connection details.

Run 'kubectl get nodes' on the control-plane to see this node join the cluster.

```

在master上查看node节点信息

```
[root@k8s-master ~]# kubectl get nodes
NAME         STATUS     ROLES                  AGE     VERSION
k8s-master   NotReady   control-plane,master   11m     v1.23.6
k8s-node1    NotReady   &lt;none&gt;                 3m49s   v1.23.6
k8s-node2    NotReady   &lt;none&gt;                 100s    v1.23.6
k8s-node3    NotReady   &lt;none&gt;                 96s     v1.23.6

```

NotReady 说明master和node节点之间的通信还是有问题的，容器之间通信还没有准备好

**#############################################################################** 

### 10.安装网络插件flannel(在master节点执行) 

>  
 ** k8s的网络插件：作用就是实现不同宿主机之间pod的通信** 
 **        1、flannel  --》overlay --》vxlan** 
 **        2、calico  --》 ipip  BGP** 


>  
 **kube-flannel.yaml 文件需要自己去创建，内容如下：** 


```
---
kind: Namespace
apiVersion: v1
metadata:
  name: kube-flannel
  labels:
    pod-security.kubernetes.io/enforce: privileged
---
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: flannel
rules:
- apiGroups:
  - ""
  resources:
  - pods
  verbs:
  - get
- apiGroups:
  - ""
  resources:
  - nodes
  verbs:
  - list
  - watch
- apiGroups:
  - ""
  resources:
  - nodes/status
  verbs:
  - patch
---
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: flannel
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: flannel
subjects:
- kind: ServiceAccount
  name: flannel
  namespace: kube-flannel
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: flannel
  namespace: kube-flannel
---
kind: ConfigMap
apiVersion: v1
metadata:
  name: kube-flannel-cfg
  namespace: kube-flannel
  labels:
    tier: node
    app: flannel
data:
  cni-conf.json: |
    {
      "name": "cbr0",
      "cniVersion": "0.3.1",
      "plugins": [
        {
          "type": "flannel",
          "delegate": {
            "hairpinMode": true,
            "isDefaultGateway": true
          }
        },
        {
          "type": "portmap",
          "capabilities": {
            "portMappings": true
          }
        }
      ]
    }
  net-conf.json: |
    {
      "Network": "10.244.0.0/16",
      "Backend": {
        "Type": "vxlan"
      }
    }
---
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: kube-flannel-ds
  namespace: kube-flannel
  labels:
    tier: node
    app: flannel
spec:
  selector:
    matchLabels:
      app: flannel
  template:
    metadata:
      labels:
        tier: node
        app: flannel
    spec:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: kubernetes.io/os
                operator: In
                values:
                - linux
      hostNetwork: true
      priorityClassName: system-node-critical
      tolerations:
      - operator: Exists
        effect: NoSchedule
      serviceAccountName: flannel
      initContainers:
      - name: install-cni-plugin
       #image: flannelcni/flannel-cni-plugin:v1.1.0 for ppc64le and mips64le (dockerhub limitations may apply)
        image: docker.io/rancher/mirrored-flannelcni-flannel-cni-plugin:v1.1.0
        command:
        - cp
        args:
        - -f
        - /flannel
        - /opt/cni/bin/flannel
        volumeMounts:
        - name: cni-plugin
          mountPath: /opt/cni/bin
      - name: install-cni
       #image: flannelcni/flannel:v0.19.1 for ppc64le and mips64le (dockerhub limitations may apply)
        image: docker.io/rancher/mirrored-flannelcni-flannel:v0.19.1
        command:
        - cp
        args:
        - -f
        - /etc/kube-flannel/cni-conf.json
        - /etc/cni/net.d/10-flannel.conflist
        volumeMounts:
        - name: cni
          mountPath: /etc/cni/net.d
        - name: flannel-cfg
          mountPath: /etc/kube-flannel/
      containers:
      - name: kube-flannel
       #image: flannelcni/flannel:v0.19.1 for ppc64le and mips64le (dockerhub limitations may apply)
        image: docker.io/rancher/mirrored-flannelcni-flannel:v0.19.1
        command:
        - /opt/bin/flanneld
        args:
        - --ip-masq
        - --kube-subnet-mgr
        resources:
          requests:
            cpu: "100m"
            memory: "50Mi"
          limits:
            cpu: "100m"
            memory: "50Mi"
        securityContext:
          privileged: false
          capabilities:
            add: ["NET_ADMIN", "NET_RAW"]
        env:
        - name: POD_NAME
          valueFrom:
            fieldRef:
              fieldPath: metadata.name
        - name: POD_NAMESPACE
          valueFrom:
            fieldRef:
              fieldPath: metadata.namespace
        - name: EVENT_QUEUE_DEPTH
          value: "5000"
        volumeMounts:
        - name: run
          mountPath: /run/flannel
        - name: flannel-cfg
          mountPath: /etc/kube-flannel/
        - name: xtables-lock
          mountPath: /run/xtables.lock
      volumes:
      - name: run
        hostPath:
          path: /run/flannel
      - name: cni-plugin
        hostPath:
          path: /opt/cni/bin
      - name: cni
        hostPath:
          path: /etc/cni/net.d
      - name: flannel-cfg
        configMap:
          name: kube-flannel-cfg
      - name: xtables-lock
        hostPath:
          path: /run/xtables.lock
          type: FileOrCreate

```

####  部署flannel

```
[root@k8s-master ~]#  kubectl apply -f kube-flannel.yml
Warning: policy/v1beta1 PodSecurityPolicy is deprecated in v1.21+, unavailable in v1.25+
podsecuritypolicy.policy/psp.flannel.unprivileged created
clusterrole.rbac.authorization.k8s.io/flannel created
clusterrolebinding.rbac.authorization.k8s.io/flannel created
serviceaccount/flannel created
configmap/kube-flannel-cfg created
daemonset.apps/kube-flannel-ds created

```

#### ** 查看集群状态（状态为Ready就代表k8s部署成功）**

```
[root@k8s-master ~]# kubectl get nodes
NAME         STATUS   ROLES                  AGE   VERSION
k8s-master   Ready    control-plane,master   21m   v1.23.6
k8s-node1    Ready    &lt;none&gt;                 20m   v1.23.6
k8s-node2    Ready    &lt;none&gt;                 20m   v1.23.6
k8s-node3    Ready    &lt;none&gt;                 20m   v1.23.6

```

#### **查看各个节点详细信息**

```
[root@k8s-master ~]# kubectl get pod -n kube-system
NAME                                 READY   STATUS    RESTARTS   AGE
coredns-6d8c4cb4d-92g7b              1/1     Running   0          20m
coredns-6d8c4cb4d-kl4q5              1/1     Running   0          20m
etcd-k8s-master                      1/1     Running   0          20m
kube-apiserver-k8s-master            1/1     Running   0          20m
kube-controller-manager-k8s-master   1/1     Running   0          20m
kube-proxy-422b5                     1/1     Running   0          19m
kube-proxy-6qpcz                     1/1     Running   0          19m
kube-proxy-ggnnt                     1/1     Running   0          20m
kube-proxy-vjcnc                     1/1     Running   0          19m
kube-scheduler-k8s-master            1/1     Running   0          20m

```

#### **查看k8s里的命名空间有哪些（k8s自己创建的） **

```
[root@k8s-master ~]# kubectl get ns
NAME              STATUS   AGE
default           Active   22m
kube-flannel      Active   10m
kube-node-lease   Active   22m
kube-public       Active   22m
kube-system       Active   22m

```

#### 查看pod运行在哪个node上，

```
[root@k8s-master ~]# kubectl get pod -n kube-flannel 
NAME                    READY   STATUS    RESTARTS   AGE
kube-flannel-ds-c7crw   1/1     Running   0          29m
kube-flannel-ds-pr5pr   1/1     Running   0          29m
kube-flannel-ds-rphnc   1/1     Running   0          29m
kube-flannel-ds-v8rxz   1/1     Running   0          29m
[root@k8s-master ~]# kubectl get pod -n kube-flannel -o wide
NAME                    READY   STATUS    RESTARTS   AGE   IP               NODE         NOMINATED NODE   READINESS GATES
kube-flannel-ds-c7crw   1/1     Running   0          29m   192.168.44.211   k8s-node1    &lt;none&gt;           &lt;none&gt;
kube-flannel-ds-pr5pr   1/1     Running   0          29m   192.168.44.212   k8s-node2    &lt;none&gt;           &lt;none&gt;
kube-flannel-ds-rphnc   1/1     Running   0          29m   192.168.44.210   k8s-master   &lt;none&gt;           &lt;none&gt;
kube-flannel-ds-v8rxz   1/1     Running   0          29m   192.168.44.213   k8s-node3    &lt;none&gt;           &lt;none&gt;

```

**#############################################################################**


