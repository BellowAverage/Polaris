
--- 
title:  基于docker-k8s的web集群 
tags: []
categories: [] 

---
**目录**





















 ​​​​​​​

### 网络拓扑图

<img alt="" height="529" src="https://img-blog.csdnimg.cn/231f2fafe7cb49a0be58c1ec58e9fafd.png" width="1200">

##  基于docker-k8s的web集群搭建

### 项目描述

>  
 **实现一个高可用的负载均衡器的Web服务器集群，使用Kubeadm搭建K8s集群，底层采用K8s管理的Docker集群来提供Web服务，大量使用容器来完成Web服务的扩展性、高可用性。** 


### 详细步骤

### 1、集群ip地址的规划

>  
 **master  ：192.168.44.31        k8s master节点** 
 **node1  ：192.168.44.32         k8s node1节点** 
 **node2  ：192.168.44.33         k8s node2节点** 
 **Ansible-server  ：192.168.44.34        ansible 服务器** 
 **NFS-server：192.168.44.35                nfs服务器** 
 **Nginx-server  ：192.168.44.36           nginx负载均衡服务器** 
 **prometheus  ：192.168.44.37             prometheus监控服务器** 


** ########################################################################** 

###  2、Ansible批量部署服务器

使用ansible服务器给所有服务器之间建立免密通道

```
[root@ansible-server ~]# ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/root/.ssh/id_rsa): 
Created directory '/root/.ssh'.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /root/.ssh/id_rsa.
Your public key has been saved in /root/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:y4eZM33yM/5E+9JnvUL3Rkvs5N7mAJSUttzgdfMnYNk root@ansible-server
The key's randomart image is:
+---[RSA 2048]----+
|            .+   |
|           .B.E..|
|           =o* .o|
|           .+ o o|
|        S   . o..|
|       . *   + *.|
|        O + o Xo+|
|         + +oo.*X|
|           .o++O*|
+----[SHA256]-----+


[root@ansible-server .ssh]# ssh-copy-id -p 22 -i id_rsa.pub  root@192.168.44.31
[root@ansible-server .ssh]# ssh-copy-id -p 22 -i id_rsa.pub  root@192.168.44.32
[root@ansible-server .ssh]# ssh-copy-id -p 22 -i id_rsa.pub  root@192.168.44.33
[root@ansible-server .ssh]# ssh-copy-id -p 22 -i id_rsa.pub  root@192.168.44.35
[root@ansible-server .ssh]# ssh-copy-id -p 22 -i id_rsa.pub  root@192.168.44.36
[root@ansible-server .ssh]# ssh-copy-id -p 22 -i id_rsa.pub  root@192.168.44.37

```

>  
 **在ansible服务器上安装ansible** 


```
yum install epel-release -y
yum install ansible -y

```

```
vim /etc/ansible/hosts
[k8s]
192.168.44.31
192.168.44.32
192.168.44.33

[nfs]
192.168.44.31
192.168.44.32
192.168.44.33
192.168.44.35

[nginx]
192.168.44.36

```

>  
 **编写ansible-playbook** 


```
vim ansible_playbook.yaml 

- hosts: k8s
  remote_user: root
  tasks:
  - name: deploy kubeadm
    script: ~/install_kubeadm.sh

- hosts: nginx
  remote_user: root
  tasks:
  - name: deploy nginx
    script: ~/onekey_install_nginx.sh

- hosts: nfs
  remote_user: root
  tasks:
  - name: install nfs-utils
    script: ~/install_nfs.sh

```

>  
 **脚本：使用kubeadm部署K8s集群** 


```
vim install_kubeadm.sh

#!/bin/bash

# 卸载旧版本
yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine

yum install -y yum-utils

yum-config-manager \
            --add-repo \
                http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo

yum install -y docker-ce docker-ce-cli containerd.io

systemctl start docker
systemctl enable docker

#配置 Docker 使用 systemd 作为默认 Cgroup 驱动
cat &lt;&lt;EOF &gt; /etc/docker/daemon.json
{
   "exec-opts": ["native.cgroupdriver=systemd"],
   "registry-mirrors" : [
    "https://registry.docker-cn.com",
    "https://docker.mirrors.ustc.edu.cn",
    "http://hub-mirror.c.163.com",
    "https://cr.console.aliyun.com/"]
}
EOF

#重启docker
systemctl restart docker

#关闭swap分区
swapoff -a # 临时
sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab # 永久
# 修改主机名后使用su - root 重新登录
# su - root
cat &gt;&gt; /etc/hosts &lt;&lt; EOF 
192.168.44.31 master
192.168.44.32 node1
192.168.44.33 node2
EOF

#添加kubernetes YUM软件源
cat &gt; /etc/yum.repos.d/kubernetes.repo &lt;&lt; EOF
[kubernetes]
name=Kubernetes
baseurl=https://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=0
repo_gpgcheck=0
gpgkey=https://mirrors.aliyun.com/kubernetes/yum/doc/yum-key.gpg https://mirrors.aliyun.com/kubernetes/yum/doc/rpm-package-key.gpg
EOF

#安装kubeadm,kubelet和kubectl
yum install -y kubelet-1.23.6 kubeadm-1.23.6 kubectl-1.23.6
#设置开机自启
systemctl enable --now kubelet
#关闭防火墙
systemctl stop  firewalld
systemctl disable  firewalld
#关闭selinux
setenforce 0   #临时关闭
#永久关闭
sed -i  '/^SELINUX/ s/enforcing/disabled/' /etc/selinux/config

```

>  
 **脚本：编译安装nginx** 


```
vim onekey_install_nginx.sh 

#!/bin/bash

#解决软件的依赖关系，需要安装的软件包
yum -y install zlib zlib-devel openssl openssl-devel pcre pcre-devel gcc gcc-c++ autoconf automake make
#useradd wangsh
id wangsh || useradd -s /sbin/nologin wangsh
#download nginx
mkdir -p /nginx
cd /nginx
curl -O http://nginx.org/download/nginx-1.19.8.tar.gz
#解压 下载的nginx的源码包
tar xf nginx-1.19.8.tar.gz
cd nginx-1.19.8
#生成编译前配置工作 --&gt; Makefile
./configure --prefix=/usr/local/nginx  --user=cPen  --group=cPen --with-threads --with-http_ssl_module  --with-http_realip_module  --with-http_v2_module --with-file-aio  --with-http_stub_status_module --with-stream
#编译
make -j 2
#编译安装 --&gt; 将编译好的二进制程序安装到指定目录 /usr/local/nginx1
make install

#修改PATH变量
echo "PATH=$PATH:/usr/local/nginx/sbin" &gt;&gt;/root/.bashrc
#执行修改了环境变量的脚本
source /root/.bashrc

#启动nginx
/usr/local/nginx/sbin/nginx

#firewalld and selinux

#stop firewalld和设置下次开机不启动firewalld
service firewalld stop
systemctl disable firewalld

#临时停止selinux和永久停止selinux
setenforce 0
sed -i '/^SELINUX=/ s/enforcing/disabled/' /etc/sysconfig/selinux

#开机自启
echo "/usr/local/nginx/sbin/nginx" &gt;&gt;/etc/rc.local
chmod +x /etc/rc.d/rc.local

```

>  
 **脚本：下载nfs-utils** 


```
vim install_nfs.sh 

#!/bin/bash
  
yum install nfs-utils -y
service nfs-server start
systemctl enable nfs-server

setenforce 0
sed -i '/^SELINUX=/ s/enforcing/disabled/' /etc/sysconfig/selinux
service firewalld stop
systemctl disable firewalld

```

>  
 **执行ansible剧本play-book** 


```
[root@ansible-server ~]# ansible-playbook ansible_playbook.yaml 

PLAY [k8s] *******************************************************************************************

TASK [Gathering Facts] *******************************************************************************
ok: [192.168.44.31]
ok: [192.168.44.33]
ok: [192.168.44.32]

TASK [deploy kubeadm] ************************************************************************************
changed: [192.168.44.31]
changed: [192.168.44.33]
changed: [192.168.44.32]

PLAY [nginx] *********************************************************************************************

TASK [Gathering Facts] ***********************************************************************************
ok: [192.168.44.36]

TASK [deploy nginx] **************************************************************************************
changed: [192.168.44.36]

PLAY [nfs] ***********************************************************************************************

TASK [Gathering Facts] ***********************************************************************************
ok: [192.168.44.35]
ok: [192.168.44.31]
ok: [192.168.44.33]
ok: [192.168.44.32]

TASK [install nfs-utils] *********************************************************************************
changed: [192.168.44.31]
changed: [192.168.44.32]
changed: [192.168.44.33]
changed: [192.168.44.35]

PLAY RECAP ***********************************************************************************************
192.168.44.31              : ok=4    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
192.168.44.32              : ok=4    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
192.168.44.33              : ok=4    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
192.168.44.35              : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
192.168.44.36              : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

[root@ansible-server ~]# 

```



** ########################################################################**

### 3、创建k8s集群

>  
 **部署k8s master结点** 


```
kubeadm init \
--apiserver-advertise-address=192.168.44.31 \
--image-repository registry.aliyuncs.com/google_containers \
--service-cidr=10.1.0.0/16 \
--pod-network-cidr=10.244.0.0/16

```

>  
 **新建目录** 


```
  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

```

>  
 **将node节点加入集群** 
 **在node1和node2机器上面执行** 


```
kubeadm join 192.168.44.31:6443 --token 42jof9.le9kkrjyqeckfjf4 \
	--discovery-token-ca-cert-hash sha256:a690aff61e9399f88487aafd76599d762ac0b18cc390339937e6e9ab01aa9a15 

```

>  
 **将节点都加入k8s集群后查看集群状态** 


```
[root@master ~]# kubectl get nodes
NAME     STATUS     ROLES                  AGE   VERSION
master   NotReady   control-plane,master   18m   v1.23.6
node1    NotReady   &lt;none&gt;                 14s   v1.23.6
node2    NotReady   &lt;none&gt;                 8s    v1.23.6

```

>  
 **安装网络插件** 


```
vim kube-flannel.yml

---
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: psp.flannel.unprivileged
  annotations:
    seccomp.security.alpha.kubernetes.io/allowedProfileNames: docker/default
    seccomp.security.alpha.kubernetes.io/defaultProfileName: docker/default
    apparmor.security.beta.kubernetes.io/allowedProfileNames: runtime/default
    apparmor.security.beta.kubernetes.io/defaultProfileName: runtime/default
spec:
  privileged: false
  volumes:
  - configMap
  - secret
  - emptyDir
  - hostPath
  allowedHostPaths:
  - pathPrefix: "/etc/cni/net.d"
  - pathPrefix: "/etc/kube-flannel"
  - pathPrefix: "/run/flannel"
  readOnlyRootFilesystem: false
  # Users and groups
  runAsUser:
    rule: RunAsAny
  supplementalGroups:
    rule: RunAsAny
  fsGroup:
    rule: RunAsAny
  # Privilege Escalation
  allowPrivilegeEscalation: false
  defaultAllowPrivilegeEscalation: false
  # Capabilities
  allowedCapabilities: ['NET_ADMIN', 'NET_RAW']
  defaultAddCapabilities: []
  requiredDropCapabilities: []
  # Host namespaces
  hostPID: false
  hostIPC: false
  hostNetwork: true
  hostPorts:
  - min: 0
    max: 65535
  # SELinux
  seLinux:
    # SELinux is unused in CaaSP
    rule: 'RunAsAny'
---
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: flannel
rules:
- apiGroups: ['extensions']
  resources: ['podsecuritypolicies']
  verbs: ['use']
  resourceNames: ['psp.flannel.unprivileged']
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
  namespace: kube-system
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: flannel
  namespace: kube-system
---
kind: ConfigMap
apiVersion: v1
metadata:
  name: kube-flannel-cfg
  namespace: kube-system
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
  namespace: kube-system
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
      - name: install-cni
        image: quay.io/coreos/flannel:v0.13.1-rc2
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
        image: quay.io/coreos/flannel:v0.13.1-rc2
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
        volumeMounts:
        - name: run
          mountPath: /run/flannel
        - name: flannel-cfg
          mountPath: /etc/kube-flannel/
      volumes:
      - name: run
        hostPath:
          path: /run/flannel
      - name: cni
        hostPath:
          path: /etc/cni/net.d
      - name: flannel-cfg
        configMap:
          name: kube-flannel-cfg

```

** ########################################################################** 

### 4、配置NFS服务

>  
 **在NFS-server服务器上配置：** 


```
vim /etc/exports

/data  192.168.2.0/24(rw,no_root_squash,no_all_squash,sync)

```

```
[root@nfs-server ~]# mkdir /data/
[root@nfs-server ~]# chmod 777 /data/
[root@nfs-server ~]# service nfs-server restart
Redirecting to /bin/systemctl restart nfs-server.service
[root@nfs-server ~]# exportfs -rv
exporting 192.168.44.0/24:/data
[root@nfs-server ~]# systemctl enable nfs-server
[root@nfs-server ~]# echo "hello,this is my docker-k8s project" &gt;&gt;/data/index.html

```

** ########################################################################** 

### 5、pv，pvc，与NFS融合

>  
 **在k8s master节点上面创建pv持久卷** 


```
vim pv-nfs.yaml

apiVersion: v1
kind: PersistentVolume	#资源类型
metadata:
  name: cl-nginx-pv
  labels:
    type: cl-nginx-pv
spec:
  capacity:
    storage: 5Gi
  accessModes:
    - ReadWriteMany		#访问模式，多个客户端读写
  persistentVolumeReclaimPolicy: Recycle	#回收策略-可以回收
  storageClassName: nfs						#注：指定存储卷的类型
  nfs:
    path: "/data"
    server: 192.168.44.36 #k8s-nfs
    readOnly: false		#不是只读

```

>  
 **在k8s master节点上创建pvc持久卷消费者** 


```
vim pvc-nfs.yaml

apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: cl-nginx-pvc
spec:
  accessModes:
  - ReadWriteMany
  resources:
     requests:
       storage: 1Gi
  storageClassName: nfs

```

>  
 **使用yaml文件部署pod** 


```
vim new-pod-nginx.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend-nginx
spec:
  replicas: 10
  selector:
    matchLabels:
      app: cl
      tier: backend-nginx
      track: stable
  template:
    metadata:
      labels:
        app: cl
        tier: backend-nginx
        track: stable
    spec:
      containers:
        - name: cl-pv-container-nfs
          image: nginx
          ports:
            - containerPort: 80
              
          volumeMounts:
            - mountPath: "/usr/share/nginx/html"
              name: cl-pv-storage-nfs
      volumes:
      - name: cl-pv-storage-nfs
        persistentVolumeClaim:
            claimName: cl-nginx-pvc

```

>  
 **使用命令创建pv，pvc，pod** 


```
[root@master pv-pvc-pod-nfs]# kubectl apply -f pv-nfs.yaml 
persistentvolume/cl-nginx-pv created
[root@master pv-pvc-pod-nfs]# kubectl apply -f pvc-nfs.yaml
persistentvolumeclaim/cl-nginx-pvc created
[root@master pv-pvc-pod-nfs]# kubectl apply -f new-pod-nginx.yaml 
deployment.apps/backend-nginx created

```

>  
 **创建好pod以后，查看pod创建情况 ** 


```
[root@master pv-pvc-pod-nfs]# kubectl get pod -o wide
NAME                             READY   STATUS    RESTARTS   AGE     IP           NODE    NOMINATED NODE   READINESS GATES
backend-nginx-67f5b5c8d6-2kpdd   1/1     Running   0          7m29s   10.244.2.4   node2   &lt;none&gt;           &lt;none&gt;
backend-nginx-67f5b5c8d6-6qss2   1/1     Running   0          7m29s   10.244.1.8   node1   &lt;none&gt;           &lt;none&gt;
backend-nginx-67f5b5c8d6-8pwlx   1/1     Running   0          7m29s   10.244.1.4   node1   &lt;none&gt;           &lt;none&gt;
backend-nginx-67f5b5c8d6-hfpxj   1/1     Running   0          7m29s   10.244.1.5   node1   &lt;none&gt;           &lt;none&gt;
backend-nginx-67f5b5c8d6-hwrvl   1/1     Running   0          7m29s   10.244.2.5   node2   &lt;none&gt;           &lt;none&gt;
backend-nginx-67f5b5c8d6-kv2nx   1/1     Running   0          7m29s   10.244.2.3   node2   &lt;none&gt;           &lt;none&gt;
backend-nginx-67f5b5c8d6-np5cl   1/1     Running   0          7m29s   10.244.2.6   node2   &lt;none&gt;           &lt;none&gt;
backend-nginx-67f5b5c8d6-slj4f   1/1     Running   0          7m29s   10.244.2.2   node2   &lt;none&gt;           &lt;none&gt;
backend-nginx-67f5b5c8d6-sqrdx   1/1     Running   0          7m29s   10.244.1.7   node1   &lt;none&gt;           &lt;none&gt;
backend-nginx-67f5b5c8d6-vmh2q   1/1     Running   0          7m29s   10.244.1.6   node1   &lt;none&gt;           &lt;none&gt;
[root@master pv-pvc-pod-nfs]# kubectl get deployment
NAME            READY   UP-TO-DATE   AVAILABLE   AGE
backend-nginx   10/10   10           10          11m

```

>  
 **暴露端口** 


```
[root@master pv-pvc-pod-nfs]# kubectl expose deployment/backend-nginx --type="NodePort" --port 80
service/backend-nginx exposed

```

>  
 ** 查看service暴露的pod端口，然后访问，可以看到，我们的web集群就部署成功了。** 


```
[root@master pv-pvc-pod-nfs]# kubectl get service
NAME            TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)        AGE
backend-nginx   NodePort    10.1.16.59   &lt;none&gt;        80:31359/TCP   47h
kubernetes      ClusterIP   10.1.0.1     &lt;none&gt;        443/TCP        2d5h

```

<img alt="" height="229" src="https://img-blog.csdnimg.cn/893262405ae7463c90cbd51ad2ea7d2d.png" width="1200"> 

<img alt="" height="188" src="https://img-blog.csdnimg.cn/7d54dafb60cf4620ae5ebaed0befb79c.png" width="1054">

** ########################################################################** 

### **6、配置Nginx负载均衡**

```
vim /usr/local/nginx/conf/nginx.conf

……
    upstream myweb {
        server 192.168.44.31:31359;
        server 192.168.44.32:31359;
        server 192.168.44.33:34359;
    }
    server {
        listen       80;
        server_name  www.cl.com;
        
        location / {
            proxy_pass  http://myweb;
        }
……

```

** ########################################################################** 

### 7、 使用prometheus监控整个Docker-K8S集群

 
