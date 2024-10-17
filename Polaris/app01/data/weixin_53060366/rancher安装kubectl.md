
--- 
title:  rancher安装kubectl 
tags: []
categories: [] 

---
## rancher安装kubectl

>  
 rancher 宿主机上部署和使用kubectl 


可以下载kubectl工具

#### 用 curl 在 Linux 系统中安装 kubectl

```
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

# 下载 kubectl 校验和文件：
curl -LO "https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"

# 基于校验和文件，验证 kubectl 的可执行文件：
echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
kubectl: OK

验证通过时，输出为：

kubectl: OK
验证失败时，sha256 将以非零值退出，并打印如下输出：

kubectl: FAILED
sha256sum: WARNING: 1 computed checksum did NOT match


```

#### 安装kubectl

```
sudo install -o root -g root -m 0755 kubectl /usr/bin/kubectl

mkdir  -p  ~/.kube/  &amp;&amp; cd  ~/.kube/
cat &lt;&lt;'EOF' &gt;   ~/.kube/config 
##此处请输入从rancher页面复制的kubconfig内容#
EOF

###步骤5：验证命令(查看是否可以用 tab 键补全)
kubectl get node
kubectl get pods

```

<img src="https://img-blog.csdnimg.cn/bfb58e361e294b27b6c56b82d3f25f1e.png#pic_center" alt="在这里插入图片描述">

>  
 <h3>安装kubectl 命令完成</h3> 

