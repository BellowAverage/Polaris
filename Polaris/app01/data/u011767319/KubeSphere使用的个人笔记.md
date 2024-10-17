
--- 
title:  KubeSphere使用的个人笔记 
tags: []
categories: [] 

---
### 官方地址



### 在centos上的安装流程

**安装需要的环境**

```
yum install socat
yum install conntrack
yum install ebtables
yum install ipset

```

**下载KubeKey**

>  
 电脑必须可以访问github，很重要。不然安装过程会出问题 


```
curl -sfL https://get-kk.kubesphere.io | VERSION=v1.2.1 sh -

```

**为 kk 添加可执行权限：**

```
chmod +x kk

```

**开始安装**

```
./kk create cluster --with-kubernetes v1.21.5 --with-kubesphere v3.2.1

```

**安装效果：** <img src="https://img-blog.csdnimg.cn/3d98146bfb6d473fb4248a0ce8b75fee.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> **安装成功，会显示地址和账号密码** <img src="https://img-blog.csdnimg.cn/da788ad8557e43859ff39371d529894e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> **登录效果** <img src="https://img-blog.csdnimg.cn/8dcea51708f241ebb542f5f78f2a25f4.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 忘记了admin的密码，修改密码

```
#这里将密码设置为Qq@123456

kubectl patch users admin -p '{<!-- -->"spec":{<!-- -->"password":"Qq@123456"}}' --type='merge' &amp;&amp; kubectl annotate users admin iam.kubesphere.io/password-encrypted-


```

### 开启DevOps

<img src="https://img-blog.csdnimg.cn/17aade75800f4deba663203281086043.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20564ddd8bd746dea88cd638436981d5.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/c5b645a0b7c5418b851ce13be64d7527.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### devops-jenkins容器为pending状态，报0/1 nodes are available: 1 Insufficient cpu解决方法

<img src="https://img-blog.csdnimg.cn/bb2edc6469eb4405aa73c233ac89f329.png" alt="在这里插入图片描述">

### 配置maven加速

<img src="https://img-blog.csdnimg.cn/f051caac1ed1496ea616791daa68b97a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/a0b002d6a7b143f29bcab0ad6f8914de.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/230622c2a7944e4cbcaac926253faf37.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

```
&lt;mirror&gt;
    &lt;id&gt;nexus-aliyun&lt;/id&gt;
    &lt;mirrorOf&gt;central&lt;/mirrorOf&gt;
    &lt;name&gt;Nexus aliyun&lt;/name&gt;
    &lt;url&gt;http://maven.aliyun.com/nexus/content/groups/public/&lt;/url&gt;
&lt;/mirror&gt;

```

然后保存就可以了

### 创建流水线

<img src="https://img-blog.csdnimg.cn/1859868e9ef3425887d4057cc896cc1b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 编辑流水线（部署项目）

<img src="https://img-blog.csdnimg.cn/367edc5da49745c4b6d5466496496ba3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

>  
 运行后，效果 


<img src="https://img-blog.csdnimg.cn/5f0676ffdd56441b87bdb0c9bed2e91c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

>  
 拉取git 代码 首先起名字 点击添加步骤， 先添加指定容器，一个maven的容器 再添加步骤，git 在创建git拉取需要的凭证，选好凭证后，在填写需要拉取的分支 


<img src="https://img-blog.csdnimg.cn/3b1efe99975a4d4f9b76849a7157c9c0.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/36646d201b5f4ebfa1ca3547ff901ea0.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/7ea7d326908a4c6d9244d04c2b5c1f3f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/070c21369bcd4413b86bf22078e02c8b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

>  
 编译项目 添加步骤maven容器后，在添加步骤shell -Dmaven.test.skip=true 代表跳过测试 -P test 代表选用测试环境 


<img src="https://img-blog.csdnimg.cn/b657bc061df54b43a3c4403c0dcc028e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

```
mvn clean package -Dmaven.test.skip=true -P test

```

>  
 打包镜像 打包多个就添加并行阶段 具体步骤就不描述了 <img src="https://img-blog.csdnimg.cn/5639b558fde84daa89bb7f662541acc8.png" alt="在这里插入图片描述"> 


<img src="https://img-blog.csdnimg.cn/8d48e7d0f4724bf5bcf58eeefbcff1aa.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

```
//-t gateway:latest 指定容器名和版本
//-f gateway/src/main/resources/Dockerfile 指定Dockerfile 路径
//./gateway/ 进入的工作目录
docker build -t gateway:latest -f gateway/src/main/resources/Dockerfile ./gateway/

```

>  
 将打包好的镜像推送到仓库 仓库自己选 现在示例的是dockerhub 


<img src="https://img-blog.csdnimg.cn/cfae685f756543c2b76479f5b9bd16dc.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/2343ca44ab20490191ddd53085caacd1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_14,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

>  
 先添加maven运行容器 后添加一下shell 运行命令 


```
docker login -u 账号 -p 密码
//更改名称
docker tag gateway:latest 空间/项目:latest （latest可以写成这样 项目-环境-版本 chat-test-v1）
//例子: docker tag gateway:latest test/base-web:latest
//推送
docker push 空间/项目:latest （latest可以写成这样 项目-环境-版本 chat-test-v1）
//例子: docker push gateway:latest test/base-web:latest

```

>  
 运行部署deploy（运行项目） 先添加maven运行容器 在添加凭证（将kebu的权限授于部署命令，配置将没有权限，就部署不了） 在写运行脚本 


**创建权限凭证** <img src="https://img-blog.csdnimg.cn/7b6deff94368455d95b8991eda310b45.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/4596a9b729f648b88335841bf4ef72b5.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 由于已经创建好了，请忽略已存在提示

<img src="https://img-blog.csdnimg.cn/3370062d8dee4b179697bd9b10db2aac.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_14,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/9577f3091fea47dcbec75b346ba2bfa9.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

```
KUBECONFIG_CONTENT

```

**部署项目命令**

```
//为什么要加|| echo 0呢，是因为并行有任务先创建了这个目录，就不用创建了
mkdir ~/.kube || echo 0
echo "$KUBECONFIG_CONTENT" &gt; ~/.kube/config
envsubst &lt; gateway/deploy/deploy_test.yaml | kubectl apply -f -

```

### 遇到k8s证书过期的情况怎么处理

```
kubeadm certs check-expiration

```

<img src="https://img-blog.csdnimg.cn/f375a2f93de0452db19019059ea419b0.png" alt="在这里插入图片描述"> **或者使用**

```
openssl x509 -in /etc/kubernetes/pki/apiserver.crt -noout -text |grep 'Not'

```

**如何更新证书呢？运行以下方法**

```
kubeadm certs renew all

```

**效果如下** <img src="https://img-blog.csdnimg.cn/3283ce644f2845c9ace7c733ae4001f7.png" alt="在这里插入图片描述"> **重启相关服务**

```
docker ps | grep -v pause | grep -E "etcd|scheduler|controller|apiserver" | awk '{<!-- -->print $1}' | awk '{<!-- -->print "docker","restart",$1}' | bash

```

### 登录k8s

```
export KUBECONFIG=/etc/kubernetes/admin.conf

```
