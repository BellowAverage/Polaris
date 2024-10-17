
--- 
title:  k8s安装KubeSphere 
tags: []
categories: [] 

---
### 安装helm

参考 https://blog.bwcxtech.com/posts/678a712d/

1、 Helm 客户端安装（master上操作） https://get.helm.sh/helm-v2.14.1-linux-amd64.tar.gz， 迅雷下载，并上传至服务器

```
tar -zxf helm-v2.14.1-linux-amd64.tar.gz
cd linux-amd64/
cp helm /usr/local/bin/

```

<img src="https://img-blog.csdnimg.cn/e13d9b499e4c447597568467abdced9e.png" alt="在这里插入图片描述"> 验证：

```
helm version

```

<img src="https://img-blog.csdnimg.cn/335d35f631d04e4399f2efa5859622d6.png" alt="在这里插入图片描述"> 2. Helm 服务端安装Tiller 在 K8S 集群上每个节点安装 socat 软件（除了这一步，其余的操作都在master执行）

```
yum install -y socat


```

<img src="https://img-blog.csdnimg.cn/4812e5b80a9a4b39955bd55f68420186.png" alt="在这里插入图片描述"> 创建tiller.yaml

```
vim tiller.yaml

```

```
apiVersion: v1
kind: ServiceAccount
metadata:
  name: tiller
  namespace: kube-system
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: tiller
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
  - kind: ServiceAccount
    name: tiller
    namespace: kube-system


```

```
 kubectl create -f tiller.yaml

```

<img src="https://img-blog.csdnimg.cn/4aa983f89a6c4ced9b1ed799c89559eb.png" alt="在这里插入图片描述"> 初始化helm服务端

```
helm init --service-account tiller --tiller-image yaokun/tiller:v2.15.2 --stable-repo-url https://kubernetes.oss-cn-hangzhou.aliyuncs.com/charts


```

<img src="https://img-blog.csdnimg.cn/34d1ec689a7f4d7f98f14653cab2be43.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

```
kubectl get pod -n kube-system


```

<img src="https://img-blog.csdnimg.cn/56ccc4a50ce947f2a883be021ae5ecd9.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 最后在master上修改helm chart仓库的地址为azure提供的镜像地址：

```
helm repo add stable http://mirror.azure.cn/kubernetes/charts
helm repo list

```

<img src="https://img-blog.csdnimg.cn/fd47ae1d1f6f4e64b58fd4dc319e26f5.png" alt="在这里插入图片描述">

### 安装 OpenEBS（小编的节点名称为 k8s-master， 前提条件和安装 OpenEBS所有步骤全部在master节点执行）

 官网： https://v2-1.docs.kubesphere.io/docs/zh-CN/appendix/install-openebs/

### 前提条件

已有 Kubernetes 集群，并安装了 kubectl 或 Helm Pod 可以被调度到集群的 master 节点（可临时取消 master 节点的 Taint） 关于第二个前提条件，是由于安装 OpenEBS 时它有一个初始化的 Pod 需要在 master 节点启动并创建 PV 给 KubeSphere 的有状态应用挂载。因此，若您的 master 节点存在 Taint，建议在安装 OpenEBS 之前手动取消 Taint，待 OpenEBS 与 KubeSphere 安装完成后，再对 master 打上 Taint，以下步骤供参考：
1. 例如本示例有一个 master 节点，节点名称即 master，可通过以下命令查看节点名称
```
kubectl get node -o wide

```

<img src="https://img-blog.csdnimg.cn/e23b3a3b64374cb7a9b74a4f5061b84a.png" alt="在这里插入图片描述"> 2. 确认 master 节点是否有 Taint，如下看到 master 节点有 Taint

```
kubectl describe node k8s-master | grep Taint

```

<img src="https://img-blog.csdnimg.cn/8f77fd7ee86e4ce58b8ad60aa9db7938.png" alt="在这里插入图片描述"> 3. 去掉 master 节点的 Taint：

```
kubectl taint nodes k8s-master node-role.kubernetes.io/master:NoSchedule-

```

<img src="https://img-blog.csdnimg.cn/9d30a10d8ae54172acb601fe934e26e9.png" alt="在这里插入图片描述">

### 安装 OpenEBS
1. 创建 OpenEBS 的 namespace，OpenEBS 相关资源将创建在这个 namespace 下：
```
 kubectl create ns openebs

```

<img src="https://img-blog.csdnimg.cn/902372ca4ab04b62bf5b19ba5b92445d.png" alt="在这里插入图片描述"> 2. 通过 Helm 命令来安装 OpenEBS：

```
helm init
helm install --namespace openebs --name openebs stable/openebs --version 1.5.0

```

<img src="https://img-blog.csdnimg.cn/bfe7bd7e2e44482ebe43d02039ff8064.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 3. 安装 OpenEBS 后将自动创建 4 个 StorageClass，查看创建的 StorageClass：

```
kubectl get sc

```

<img src="https://img-blog.csdnimg.cn/7367bbfa3cc84a79b302e5b839a18504.png" alt="在这里插入图片描述"> 需要等一会儿才能创建完 4 个 StorageClass， 小编等待了大约一分钟的时间。 4. 将 openebs-hostpath设置为 默认的 StorageClass：

```
 kubectl patch storageclass openebs-hostpath -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'

```

<img src="https://img-blog.csdnimg.cn/52b4d6588dc9478c8b46650ed67f3ce6.png" alt="在这里插入图片描述"> 5. 至此，OpenEBS 的 LocalPV 已作为默认的存储类型创建成功。可以通过命令 kubectl get pod -n openebs来查看 OpenEBS 相关 Pod 的状态，若 Pod 的状态都是 running，则说明存储安装成功

```
kubectl get pod -n openebs

```

<img src="https://img-blog.csdnimg.cn/c1033ad8213945e0957056abdfa588e3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 在 Kubernetes 安装 KubeSphere(全部操作都在master节点上执行)

 官网地址： https://v2-1.docs.kubesphere.io/docs/zh-CN/installation/install-on-k8s/ 完整安装 KubeSphere 若集群可用 CPU &gt; 8 Core 且可用内存 &gt; 16 G，可以使用以下命令完整安装 KubeSphere。 注意，应确保集群中有一个节点的可用内存大于 8 G。 提示：若您的服务器提示无法访问 GitHub，可将 kubesphere-minimal.yaml 或 kubesphere-complete-setup.yaml 文件保存到本地作为本地的静态文件，再参考上述命令进行安装 小编提前下载了 kubesphere-complete-setup.yaml 并上传至服务器(小编从gitee上下载的，地址为： https://gitee.com/learning1126/ks-installer/tree/master) <img src="https://img-blog.csdnimg.cn/36c336d71f64425ab7d830ab9d2b49b5.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 请根据自己的情况，选择下载kubesphere-minimal.yaml 或 kubesphere-complete-setup.yaml <img src="https://img-blog.csdnimg.cn/e5b6ec33387b4e9eb54f65e179af97d1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 验证与访问
1. 查看滚动刷新的安装日志，请耐心等待安装成功。
```
kubectl logs -n kubesphere-system $(kubectl get pod -n kubesphere-system -l app=ks-install -o jsonpath='{.items[0].metadata.name}') -f

```

<img src="https://img-blog.csdnimg.cn/a9ebb9021eea4177b5b627e447be3971.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 说明：安装过程中若遇到问题，也可以通过以上日志命令来排查问题。 <img src="https://img-blog.csdnimg.cn/d7dd892d3221465a9477c0da00fcc8e1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 出现此截图，则说明安装成功
1. 通过 kubectl get pod --all-namespaces查看 KubeSphere 相关 namespace 下所有 Pod 状态是否为 Running。确认 Pod 都正常运行后，可使用 IP:30880访问 KubeSphere UI 界面，默认的集群管理员账号为 admin/P@88w0rd。
```
kubectl get pod --all-namespaces

```
1. 页面访问
```
192.168.8.106:30880

```

<img src="https://img-blog.csdnimg.cn/0720291dadef475484fe6e4663d75281.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 输入 admin/P@88w0rd 登录即可 <img src="https://img-blog.csdnimg.cn/f737f5421e3f40c185946b497ae352cf.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">
