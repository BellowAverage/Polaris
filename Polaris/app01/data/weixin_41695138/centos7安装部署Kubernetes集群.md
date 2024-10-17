
--- 
title:  centos7安装部署Kubernetes集群 
tags: []
categories: [] 

---
参考 ，请移步到此博客（https://www.jianshu.com/p/32eedbebb6b8） 参考 ，请移步到此博客（https://blog.csdn.net/weixin_47049334/article/details/126341792）

### 前言：

结合此博客加上自己的实操，总结如下：
1. 服务器版本： CentOS Linux release 7.9.2009 (Core)1. 安装前准备的1-7 步，安装K8S中的 1-4步，要在三个节点上同时操作
### 安装前准备
1. 部署规划
```
192.168.8.106  k8s-master
192.168.8.186  k8s-node1
192.168.8.187  k8s-node2

```
1.  修改 hostname master节点上操作：hostnamectl set-hostname k8s-master node1节点上操作： hostnamectl set-hostname k8s-node1 node2节点上操作：hostnamectl set-hostname k8s-node2 <img src="https://img-blog.csdnimg.cn/003f119364b14fd2986bc8c45a20e362.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/1a27597d89564a4e8267cc677429c8ac.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/e020edd867654fd3b4c7bac80747fe24.png" alt="在这里插入图片描述"> 通过 cat /etc/hostname 可查看是否更改成功 1.  关闭selinux（临时关闭：输入命令setenforce 0，重启系统后还会开启。） 
```
setenforce 0

```

<img src="https://img-blog.csdnimg.cn/dfd45a2d215f403fb5b44e026297b2c6.png" alt="在这里插入图片描述"> 永久关闭：输入命令vi /etc/selinux/config，将SELINUX=enforcing改为SELINUX=disabled，然后保存退出。
1. 关闭防火墙
```
systemctl stop firewalld.service
systemctl disable firewalld.service 
firewall-cmd --state

```

<img src="https://img-blog.csdnimg.cn/3b579c1e66aa45efaeca334b5fda3a1d.png" alt="在这里插入图片描述"> 4. 设置host

```
vim /etc/hosts
192.168.8.106  k8s-master
192.168.8.186  k8s-node1
192.168.8.187  k8s-node2

```

可通过 cat /etc/hosts 查看是否修改成功 <img src="https://img-blog.csdnimg.cn/47e96acf6e9641c69e3778a0d53c009a.png" alt="在这里插入图片描述">
1. 禁用swap
```
swapoff -a  #临时生效，重启失效


```

```
vim /etc/fstab  #永久禁用


```

<img src="https://img-blog.csdnimg.cn/5dd92829c93246529bcd124b21521ecc.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

```
mount -a  # 重新加载生效


```
1. 将桥接的IPV4流量传递到iptables 的链
```
cat &gt; /etc/sysctl.d/k8s.conf &lt;&lt; EOF
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF

```

```
sysctl --system

```

<img src="https://img-blog.csdnimg.cn/4e4b23cd7b134e31b898d45a9253a97b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 7. 安装Docker 备份源

```
sudo mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak

```

修改OS源为阿里的仓库

```
curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo

```

安装常用命令

```
yum -y install conntrack ipvsadm ipset jq sysstat curl iptables libseccomp wget lrzsz nmap lsof net-tools zip unzip vim telnet

```

安装依赖项

```
yum install -y yum-utils device-mapper-persistent-data lvm2

```

安装Docker源为阿里

```
yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo

```

清理缓存

```
yum clean all

```

** 重新生成缓存**

```
yum makecache

```

再次查看yum源信息

```
yum repolist

```

<img src="https://img-blog.csdnimg.cn/90674e2352884e7f9985a2073eafb756.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 我们安装18.06.3版本

```
sudo yum install docker-ce-18.06.3.ce-3.el7

```

安装完毕后，查看docker 版本信息

```
 docker version

```

<img src="https://img-blog.csdnimg.cn/d13c47302fde482e814460b389cec510.png" alt="在这里插入图片描述"> 启动Docker，设置开机启动

```
sudo chkconfig docker on
systemctl start docker

```

<img src="https://img-blog.csdnimg.cn/3bfac0a6942143038278624ccb1e4891.png" alt="在这里插入图片描述"> 修改Docker镜像仓库为阿里源镜像

```
vim /etc/docker/daemon.json
{
  "registry-mirrors": ["https://sv69k1rc.mirror.aliyuncs.com"],
  "exec-opts": ["native.cgroupdriver=systemd"]
}

```

https://sv69k1rc.mirror.aliyuncs.com，是小编的阿里源地址，请更换为自己的地址。 修改后刷新daemon.json，重启docker服务使配置生效

```
systemctl daemon-reload
sudo systemctl restart docker.service

```

<img src="https://img-blog.csdnimg.cn/7759e5678f8e47fb835b034542d0425e.png" alt="在这里插入图片描述">

执行完后，可以查看下docker状态及详细信息

```
service docker status
docker info

```

<img src="https://img-blog.csdnimg.cn/4753ef8379824e94a6d68ca511906667.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 安装K8S
1. 安装K8S源
```
cat &lt;&lt;EOF &gt; /etc/yum.repos.d/kubernetes.repo    
[kubernetes]    
name=Kubernetes 
baseurl=https://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64
enabled=1   
gpgcheck=1  
repo_gpgcheck=1 
gpgkey=https://mirrors.aliyun.com/kubernetes/yum/doc/yum-key.gpg 
https://mirrors.aliyun.com/kubernetes/yum/doc/rpm-package-key.gpg   
EOF

```

<img src="https://img-blog.csdnimg.cn/195232c645ba4ccba232733dabee2ad2.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 2. 导入公钥

```
wget  https://mirrors.aliyun.com/kubernetes/yum/doc/yum-key.gpg
rpm --import yum-key.gpg
wget https://mirrors.aliyun.com/kubernetes/yum/doc/rpm-package-key.gpg
rpm --import rpm-package-key.gpg

```

<img src="https://img-blog.csdnimg.cn/3ba2920cdf12422a996499779fda343a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 3. 安装

```
yum install -y kubelet-1.15.9-0 kubeadm-1.15.9-0 kubectl-1.15.9-0

```

<img src="https://img-blog.csdnimg.cn/75d9c0e00b9544adaf0fce7ea4f8912b.png" alt="在这里插入图片描述"> 4. 开机启动 很重要（如不设置，服务重启后，则需要重新启动 k8s）

```
systemctl enable kubelet &amp;&amp; systemctl start kubelet
systemctl status kubelet 

```

<img src="https://img-blog.csdnimg.cn/3672a4f4e16b4e65bbf1783b07405b3f.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/cd5e07e01f8346e28ad429a0511a4161.png" alt="在这里插入图片描述"> 执行这个语句 systemctl status kubelet ，虽然有失败信息，不用管，等到后面初始化完成和加载calico.yml后，就好了。
1. 初始化K8S集群（在 master 节点上操作）\
```
kubeadm init --kubernetes-version=v1.15.9 --pod-network-cidr=10.244.0.0/16 --apiserver-advertise-address=192.168.88.106 --apiserver-cert-extra-sans=192.168.88.106,k8s-master   --image-repository registry.aliyuncs.com/google_containers

```

192.168.8.106 是 master 的ip地址， 由于小编后期修改过ip地址，请把 192.168.88.XXX 看成 192.168.8.XXX <img src="https://img-blog.csdnimg.cn/6d24a492894542878980ea9c79e03f9a.png" alt="在这里插入图片描述"> 6. 将当前用户配置为集群管理员（如果不配置，下次连接时会无法使用kubectl）master节点操作

```
  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

```

<img src="https://img-blog.csdnimg.cn/44b3d77a1f9b450da254c2c12aafbc7e.png" alt="在这里插入图片描述"> 7. 安装Calico(master节点上操作)

```
wget https://docs.projectcalico.org/v3.10/getting-started/kubernetes/installation/hosted/kubernetes-datastore/calico-networking/1.7/calico.yaml --no-check-certificate
kubectl apply -f calico.yaml

```

<img src="https://img-blog.csdnimg.cn/4aae3955f0384d38bb8bb5c4160a6509.png" alt="在这里插入图片描述">
1. 然后到其他两个节点执行如下命令，添加节点到master.（在node1 node2 上操作）
```
kubeadm join 192.168.88.106:6443 --token xfmjke.mh9e32ocm4kayg41 \
    --discovery-token-ca-cert-hash sha256:e22cce363e8d0251785a0920024bd4a4146d64b4b52e58978b0e6c28dc80e09a 

```

<img src="https://img-blog.csdnimg.cn/fb517eef538d4d25a0b2f1ec13b1ca3b.png" alt="在这里插入图片描述"> 9. 加入完毕后，我们用命令kubectl get nodes获取所有节点(master节点上操作，要等上一会才能都是 Ready状态)

```
kubectl get nodes

```

<img src="https://img-blog.csdnimg.cn/2fe8e963641449c5a62d2fb6994ee81c.png" alt="在这里插入图片描述">

验证安装信息

```
kubectl get componentstatus

```

<img src="https://img-blog.csdnimg.cn/cf61a5f56db7457eb020ac697886a0ad.png" alt="在这里插入图片描述"> 检查系统pod状态

```
 kubectl get pods -n kube-system

```

<img src="https://img-blog.csdnimg.cn/3b12f5763245435e844d1efc0e51f706.png" alt="在这里插入图片描述"> 查看日志的命令： journalctl -f -u kubelet
1. 测试K8S集群 这里为了快速地验证一下我们的K8S集群是否可用，创建一个示例Pod：
```
kubectl create deployment nginx --image=nginx
 kubectl expose deployment nginx --port=80 --type=NodePort
 kubectl get pod,svc

```

<img src="https://img-blog.csdnimg.cn/7a53c6c187e44076bec19a983c9ad57d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 32085 是nginx 的访问端口

http://192.168.8.106:32085/ http://192.168.8.186:32085/ http://192.168.8.187:32085/ 都能访问nginx: <img src="https://img-blog.csdnimg.cn/62bce8400bea4bb98bb18d4f388b1bbb.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 11. 经过测试 重启服务，也是能直接访问 ngixn的， 说明集群自启动了。
