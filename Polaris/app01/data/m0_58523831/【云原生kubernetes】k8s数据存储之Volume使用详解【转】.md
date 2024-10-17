
--- 
title:  【云原生kubernetes】k8s数据存储之Volume使用详解【转】 
tags: []
categories: [] 

---
**目录**



























































































## 一、什么是Volume

通过之前学习了解到，中Pod是最小的运行单元，Pod中运行的是一个个容器，但是容器的生命周期可能很短，被频繁地创建和销毁。

在学习docker的时候，创建一个容器，如果没有指定容器的数据卷，容器中的文件在磁盘上通常是临时存放的，这就给容器中运行的重要应用程序带来了一些问题 ，比如像下面的场景：
- 当容器崩溃时文件丢失，kubelet 会重新启动容器，但容器会以干净的状态重启，之前保存在容器中的数据也会被清除 ；- 当在一个 Pod 中同时运行多个容器时，常常需要在这些容器之间共享文件 ；
基于这些问题，k8s中就出现了“卷”这个组件来解决

>  
 Kubernetes 卷（Volume） 这一抽象概念能够解决这两个问题，卷的核心是包含一些数据的目录，Pod 中的容器可以访问该目录 


## 二、k8s中的Volume

关于k8s中卷的总结：
- Volume是k8s抽象出来的对象，它被定义在Pod上，然后被一个Pod里的多个容器挂载到具体的文件目录下 ；- kubernetes通过Volume实现同一个Pod中不同容器之间的数据共享以及数据的持久化存储 ；- Volume的生命周期不与Pod中单个容器的生命周期相关，当容器终止或者重启时，Volume中的数据也不会丢失；- K8S可以支持许多类型的卷，Pod 也能同时使用任意数量的卷；
## 三、k8s中常见的Volume类型

k8s中提供了很多种类型的Volume，下面列举一些常用的类型：
- 常规存储：EmptyDir、HostPath ；- 高级存储：PV、PVC ；- 配置存储：ConfigMap、Secret ；- 其他：网络存储系统 NFS、CIFS，包括云服务商提供的、本地、分布式 ；
接下来，针对日常业务中使用较多的Volume，通过实例一一演示下各自的使用。

## 四、Volume 之 EmptyDir

### 4.1 EmptyDir 特点
- 当 Pod 指定到某个节点上时，首先创建的是一个 `emptyDir` 卷，只要 Pod 在该节点上运行卷就一直存在 ；- 当 Pod 因为某些原因被从节点上删除时，`emptyDir` 卷中的数据也会永久删除 ；- 容器崩溃并不会导致 Pod 被从节点上移除，所以容器崩溃时 `emptyDir` 卷中的数据是安全的；
>  
 使用场景：临时缓存空间，存储一些运行过程中的中继日志； 


### 4.2 EmptyDir 实现文件共享

如图所示，我们的需求是，创建一个类型为EmptyDir的Volume，实现两个容器日志的共享；

<img src="https://img-blog.csdnimg.cn/8472cecfb4a74239b6ceeaf8da0ca5a4.png" alt="">

#### **4.2.1 关于busybox**

>  
 1、是⼀个集成了三百多个最常⽤ Linux 命令和⼯具的软件； 
 2、包含了简单的⼯具，例如 ls 、 cat 和 echo 等等，还包含了⼀些更复杂的⼯具，例grep 、 find 、 telnet等； 


### 4.3 操作步骤

下面通过案例演示下使用的步骤

#### 4.3.1 创建配置模板文件yaml

在当前目录下创建一个volume-emptydir.yaml 的文件，配置如下内容：

```
    apiVersion: v1kind: Podmetadata:  name: test-volume-emptydir  namespace: defaultspec:  containers:  - name: test-nginx    image: nginx:1.20    ports:    - containerPort: 80    volumeMounts:  # 将nginx-log-volume挂在到nginx容器中，对应的目录为 /var/log/nginx    - name: test-log-volume      mountPath: /var/log/nginx   - name: test-busybox    image: busybox:1.35.0     command: ["/bin/sh","-c","tail -f /usr/local/test/access.log"] # 容器启动后初始命令，读取指定文件中内容    volumeMounts:  # 将nginx-log-volume挂在到busybox容器中，对应的目录为 /logs    - name: test-log-volume      mountPath: /usr/local/test   volumes: # 这里声明volume存储劵， name为nginx-log-volume，类型是emptyDir  - name: test-log-volume    emptyDir: {}

```

配置中的关键位置如下：

<img src="https://img-blog.csdnimg.cn/c7a30357906b44af96881de667493c7f.png" alt="">

#### 4.3.2 创建Pod

使用apply命令执行pod的创建，创建成功后，可以看到在test-volume-emptydir 这个pod里面运行了2个容器；

<img src="https://img-blog.csdnimg.cn/0c81a28c2459401f84c5d61a03ef61e5.png" alt="">

#### 4.3.3 访问nginx使其产生访问日志

随机访问一下，使nginx中产生部分日志

<img src="https://img-blog.csdnimg.cn/0e440b70e7f74f458ba849605b33136d.png" alt="">

#### 4.3.4 查看容器日志

使用下面的命令查看容器产生的access.log日志

```
kubectl logs -f test-volume-emptydir -n default -c test-busybox

```

<img src="https://img-blog.csdnimg.cn/267187a505214115b85f5176a78b5ac2.png" alt="">

## 五、Volume 之 hostPath

上面我们聊了EmptyDir的使用，相信实际操作之后的同学应该能看出来，由于EmptyDir创建的这个Volume是一个虚拟的路径，所以当其销毁后，pod中容器产生的数据也就随之销毁了，即无法真正实现数据的落盘持久化，于是我们在想，是否可以做到下面这样呢？

当然是可以的，这就是接下来要说的另一种Volume ： **hostPath；**

<img src="https://img-blog.csdnimg.cn/b1effe4e802e40ab81552d90656fc5ea.png" alt="">

### 5.1 **hostPath 概述**
- emptyDir中数据没做持久化，随着Pod的结束而销毁，需要持久化到磁盘则选其他方式 ；- hostPath类型的磁盘就是挂在了主机的一个文件或者目录 ；- 某些应用需要用到docker的内部文件，这时只需要挂在本机的/var/lib/docker作为hostPath ；
### 5.2 **hostPath类型**

根据使用场景的不同，又可以细分成多个类型
- Directory 给定的目录路径必须存在 ；- DirectoryOrCreate 如果给定路径不存在，将根据需要在那里创建一个空目录 ；- File 给定路径上必须存在对应文件 ；- FileOrCreate 如果给定路径不存在，将根据需要在那里创建一个空文件 ；
### **5.3 hostPath 操作演示**

#### **5.3.1 创建模板配置文件**

在当前目录下创建一个名叫volume-hostpath.yaml的配置文件，内容如下：

```
apiVersion: v1kind: Podmetadata:  name: hostpath-volume-test  namespace: defaultspec:  containers:  - name: test-nginx    image: nginx:1.20    ports:    - containerPort: 80    volumeMounts:  # 将nginx-log-volume挂在到nginx容器中，对应的目录为 /var/log/nginx    - name: test-log-volume      mountPath: /var/log/nginx   - name: test-busybox    image: busybox:1.35.0     command: ["/bin/sh","-c","tail -f /usr/local/test/access.log"] # 容器启动后初始命令，读取指定文件中内容    volumeMounts:  # 将nginx-log-volume挂在到busybox容器中，对应的目录为 /logs    - name: test-log-volume      mountPath: /usr/local/test   volumes: # 这里声明volume存储劵， name为test-log-volume，类型是hostPath  - name: test-log-volume    hostPath:        path: /usr/local/test        type: DirectoryOrCreate #如果给定路径不存在，将根据需要在那里创建一个空目录

```

主要的配置和上面的emptyDir的案例中的差不多，最后的volumes类型那里改成hostPath相关的参数；

#### **5.3.2 **使用apply命令创建pod

创建成功后，可以看到产生了一个hostpath开头的一个Pod，里面包含两个容器；

<img src="https://img-blog.csdnimg.cn/175c0ad6e03345b7be0647609f362e87.png" alt="">

#### 5.3.3 访问nginx使其产生访问日志

<img src="https://img-blog.csdnimg.cn/90a6b804c0f94745b62af67a25c46e95.png" alt="">

#### 5.3.4 查看容器输出日志

这这里注意使用你自己定义的那个名称

```
kubectl logs -f hostpath-volume-test -n default -c test-busybox

```

<img src="https://img-blog.csdnimg.cn/23ed9ed9358248788612e652caed7f7e.png" alt="">

#### 5.3.5 查看挂载目录日志文件

工作节点查看对应的挂载目录的日志文件，登录工作节点的服务器，可以看到对应的nginx日志文件也在里面了；

<img src="https://img-blog.csdnimg.cn/fa76bc88d02a4ba9a5399af7c74a3362.png" alt="">

#### 5.3.6 删除当前的pod

<img src="https://img-blog.csdnimg.cn/654a352cbaa345b8965c3fd562aafb5e.png" alt="">

删除pod之后发现工作节点目录下的日志文件依然存在

<img src="https://img-blog.csdnimg.cn/df2d964e6aed49f98d5899fb1c7e90ff.png" alt="">

### 5.4 emptyDir和hostPath的对比

通过上面的演示，最后来对比一下emptyDir和hostPath使用上的异同点：
- 两者都是本地存储卷方式 ；- emptyDir是临时存储空间，完全不提供持久化支持；- hostPath的卷数据是持久化在node节点的文件系统中的，即便pod已经被删除了，volume卷中的数据还留存在node节点上；
## 六、Volume 之 ConfigMap

### 6.1 ConfigMap需求场景

很多应用在其初始化或运行期间要依赖一些配置信息 ，并且在大多数时候， 存在要调整配置参数所设置的数值的需求，而ConfigMap是Kubernetes 用来向应用 Pod 中注入配置数据的一种方法 ；

### 6.2 ConfigMap简介
- 是K8S的一种API对象，用来把【非加密数据】保存到键值对中，比如etcd ；- 可以用作环境变量、命令行参数等，将环境变量、配置信息和容器镜像解耦，便于应用配置的修改 ；
使用方式

>  
 kubectl create configmap 命令，基于目录、 文件或者键值对来创建 ConfigMap 


如下示例：

>  
 kubectl create configmap NAME --from-literal=key1=value1 --from-literal=key2=value2 


### 6.3 ConfigMap 创建操作演示

#### 6.3.1 使用命令行创建

使用下面的命令进行ConfigMap的创建

```
kubectl create configmap test-config --from-literal=account=test --from-literal=password=123456

```

<img src="https://img-blog.csdnimg.cn/8704bcdfbc964912931c671dc91e1f7e.png" alt="">

#### 6.3.2 **查看创建的configmap**

```
kubectl get configmap test-config -o yaml

```

<img src="https://img-blog.csdnimg.cn/51be6fd37a464c11af209a67771a7bc2.png" alt="">

#### 6.3.3 使用创建

在当前目录下创建一个 test-configmap.yaml的文件，核心配置内容如下：

```
apiVersion: v1kind: ConfigMapmetadata:  name: congge-configmap  namespace: defaultdata:  info:     username:congge    password:123456

```

使用apply命令执行创建

<img src="https://img-blog.csdnimg.cn/cfa462f87f204320b0600fd1f85849af.png" alt="">

#### 6.3.4 查看configmap详情

```
kubectl describe cm congge-configmap -n default

```

<img src="https://img-blog.csdnimg.cn/c2136f91c3e542fd9b435442f7f47ef8.png" alt="">

### 6.4 ConfigMap 使用操作演示

上面演示了两种创建configmap的方式，configmap创建出来后怎么使用呢？简单来说，只需要开启一个pod，将这个configmap挂载进去使用即可；

#### 6.4.1 使用配置文件创建pod

注意，里面的Volume使用上文yaml中创建的那个configmap的名字：

```
apiVersion: v1kind: Podmetadata:  name: pod-configmap  namespace: defaultspec:  containers:  - name: nginx    image: nginx:1.20    volumeMounts: # configmap挂载的目录    - name: config      mountPath: /config   volumes: # 声明configmap  - name: config    configMap:      name: congge-configmap

```

执行apply命令进行创建，然后检查下是否创建成功；

<img src="https://img-blog.csdnimg.cn/bb98c25643ac446facd92f3bf179c8e3.png" alt="">

#### 6.4.2 验证configmap中配置的值

进入pod容器

>  
 kubectl exec -it pod-configmap -n default – /bin/sh 


<img src="https://img-blog.csdnimg.cn/babf41a4f27c49239e84413af487b421.png" alt="">

进入配置文件中的挂载目录 /config，查看配置信息

<img src="https://img-blog.csdnimg.cn/789142514a9e44c8b96bbc8a3303b84a.png" alt="">

## 七、Volume 之 Secret

有些配置需要加密存储，ConfigMap只能使用明文保存，因此ConfigMap就不适合了；

### 7.1 Secret 简介

Secret 作用
- 用来保存敏感信息，例如密码、秘钥、证书、OAuth 令牌和 ssh key等 ；- 就不需要把这些敏感数据暴露到镜像或者Pod中 ；
不管是哪种Volume，最终都是为Pod服务的，对于Pod来说，可以用三种方式之一来使用 Secret：
- 作为挂载到一个或多个容器上的卷 中的文件 ；- 作为容器的环境变量 ；- 由 kubelet 在为 Pod 拉取镜像时使用 ；
### 7.2 secret 常见类型

下面列举secret中常用的几种类型

#### **7.2.1 dockerconfigjson**

>  
 用来存储私有 docker registry的认证信息 


#### **7.2.2 Service Account**

>  
 1、只要与Kubernetes API有交互的Pod，都会自动拥有此种类型的Secret； 
 2、K8S自动创建，并且会自动挂载到Pod的 /run/secrets/kubernetes.io/serviceaccount 目录中； 


**7.2.3 Opaque**

>  
 加密类型为base64，其特点就是将明文改为了密文 


### 7.3 Secret **Opaque使用**

下面以Secret中Opaque这种类型进行说明，首先用一个字符串做下测试，简单来说，就是将字符串进行base64编码，得到一串类似于密文的字符串；

<img src="https://img-blog.csdnimg.cn/bfcfd71350ad4b96b5642c8c3fbd0da7.png" alt="">

#### 7.3.1 创建模板配置文件

在当前目录下创建一个secret.yaml的配置文件，内容如下，其中，username和password用的就是上面测试中看到的：

```
apiVersion: v1kind: Secretmetadata:  name: my-secrettype: Opaquedata:  username: YWRtaW4=  password: MTIzNDU2

```

#### 7.3.2 使用apply命令创建secret

创建成功后，可以顺便使用get查看下创建的secret；

<img src="https://img-blog.csdnimg.cn/fa956449c70f449990352e78ab32de85.png" alt="">

#### 7.3.3 查看my-secret详细信息

使用下面的命令进行查看

>  
 kubectl get secret my-secret -o yaml 


<img src="https://img-blog.csdnimg.cn/cf33dbadef284946aff513fbcdc5f025.png" alt="">

#### 7.3.4 创建pod

创建一个新的pod并使用上面这个secret，在当前目录下，创建一个名叫pod-secret-volume.yaml的配置文件，内容如下：

```
apiVersion: v1kind: Podmetadata:  name: pod-secretspec:  containers:  - name: nginx    image: nginx:1.20    volumeMounts: # secret挂载    - name: congge-config      mountPath: /etc/secret  volumes:  - name: congge-config    secret:      secretName: my-secret

```

使用apply命令执行并创建pod

<img src="https://img-blog.csdnimg.cn/18fe6e48a0be4765909515c3c76ff1fd.png" alt="">

#### 7.3.5 查看secret信息

在pod中的secret信息实际已经被解密，使用下面的命令进入到pod

```
kubectl exec -it pod-secret -- /bin/sh

```

查看指定目录下secret中配置的username和password，可以看到，在pod中，加密的信息已被解密了；

<img src="https://img-blog.csdnimg.cn/c2e4641e865146ec8aa6d0aa1b3a75a7.png" alt="">

转：https://blog.csdn.net/zhangcongyi420/article/details/128433221
