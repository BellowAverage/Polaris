
--- 
title:  玩转docker之registry私有仓库(●ˇ∀ˇ●) 
tags: []
categories: [] 

---
## 玩转docker之registry私有仓库

### 关于registry

在了解registry之前，我们跟多的听到的是dockerHub。

官方的是一个用于管理公共镜像的好地方，我们可以在上面找到我们想要的镜像，也可以把我们自己的镜像推送上去。

但是，本地访问Docker Hub速度往往很慢，有时候，我们的使用场景需要我们拥有一个私有的镜像仓库用于管理我们自己的镜像。这个可以通过开源软件Registry来达成目的。

**registry版本：**
- Registry在github上有两份代码：和。- 老代码是采用python编写的，存在pull和push的性能问题，出到0.9.1版本之后就标志为deprecated，不再继续开发。- 从2.0版本开始就到在新代码库进行开发，新代码库是采用go语言编写，修改了镜像id的生成算法、registry上镜像的保存结构，大大优化了pull和push镜像的效率。
### 部署registry

#### 1、获取registry镜像：

```
docker pull registry:2.1.1
#启动容器
docker run -d -v /mnt/registry:/var/lib/registry -p 5000:5000 --restart=always --name registry registry:2.1.1

```

Registry服务默认会将上传的镜像保存在容器的/var/lib/registry，我们将主机的/mnt/registry目录挂载到该目录，即可实现将镜像保存到主机的/opt/registry目录了。

运行docker ps看一下容器情况:

```
docker ps -a

```

<img src="https://img-blog.csdnimg.cn/63fbea0285414570a9e686b0010c92b9.png#pic_center" alt="在这里插入图片描述">

说明我们已经启动了registry服务，打开浏览器输入http://192.168.111.40:5000/v2，出现下面情况说明registry运行正常。

<img src="https://img-blog.csdnimg.cn/8cef6908833f4153828d587eba7efff8.png#pic_center" alt="在这里插入图片描述">

#### 2、验证：

现在我们通过将镜像push到本地的registry来验证一下。

我的机器上有个 nginx:latest 的镜像，我们要通过docker tag 将该镜像标志为要推送到私有仓库。

```
docker tag nginx:latest 192.168.111.40:5000/nginx

```

<img src="https://img-blog.csdnimg.cn/6e8a51ea3920412b83e1871e387a3f9b.png#pic_center" alt="在这里插入图片描述">

接下来我们将刚打的 tag 镜像 push 到我们的私有仓库中：

```
docker push 192.168.111.40:5000/nginx

```

现在我们可以查看我们本地/mnt/registry目录下已经有了刚推送上来的 nginx:latest 。我们也在浏览器中输入http://192.168.111.40:5000/v2/_catalog，如下图所示:

<img src="https://img-blog.csdnimg.cn/4f952a7ec0c1437ba374fbfc5ba428e3.png#pic_center" alt="在这里插入图片描述">

现在我们把本地的nginx都删掉：

```
docker rmi -f 镜像ID

```

<img src="https://img-blog.csdnimg.cn/f18e713f9a114c8084a1251bde172fee.png#pic_center" alt="在这里插入图片描述">

接下来我们将我们registry中的nginx pull 下来即可：

```
docker pull 192.168.111.40:5000/nginx

```

### 总结：

docker的私有仓库registry在企业中经常用到，我们都会把自己编写的dockerfile文件构建的镜像push 到里面，以便于我们在需要时pull 下来，大大减少了docker启动时间。
