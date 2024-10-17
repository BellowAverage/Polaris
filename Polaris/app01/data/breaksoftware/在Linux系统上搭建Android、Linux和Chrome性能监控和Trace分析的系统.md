
--- 
title:  在Linux系统上搭建Android、Linux和Chrome性能监控和Trace分析的系统 
tags: []
categories: [] 

---
perfetto是知名的Android系统性能分析平台。我们还可以用它去分析Linux系统和Chrome（需要装扩展）。本文我们只介绍如何安装的验证。

## 部署

我们使用Docker部署perfetto ui系统。

```
FROM ubuntu:20.04
WORKDIR /perfetto-ui
RUN apt-get update -y
RUN apt-get install -y git python3 curl gcc
RUN git clone https://android.googlesource.com/platform/external/perfetto/
RUN perfetto/tools/install-build-deps --ui
RUN perfetto/ui/build
EXPOSE 10000

```

然后使用下面代码打镜像包

```
docker build --pull --rm -f "Dockerfile" -t perfetto:latest "."

```

这个过程比较漫长。我这台24核CPU大概需要13分钟左右才能完成，特别在perfetto/ui/build环节，CPU会满负荷运行。 <img src="https://img-blog.csdnimg.cn/direct/1fef7ba384f9415ab1662933b1b471e0.png#pic_center" alt="在这里插入图片描述"> 然后启动镜像

```
docker container run -d -p 10000:10000 --name perfetto-ui perfetto:latest

```

启动到服务可用大概需要1分钟左右。 <img src="https://img-blog.csdnimg.cn/direct/ca149d68571248d98676c0da723b1f73.png" alt="在这里插入图片描述">

## 验证

打开浏览器，输入本机地址（不是127.0.0.1）和映射的10000端口号，就能看到页面 <img src="https://img-blog.csdnimg.cn/direct/acc3560aafa347c79e39f41163ab69c9.png" alt="在这里插入图片描述">

### Linux Trace

#### 获取Trace

我们单开一台有管理员权限的Linux机器，然后按如下指令安装perfetto

```
sudo apt-get update -y
sudo apt-get install -y git python3 curl gcc
git clone https://android.googlesource.com/platform/external/perfetto/
perfetto/tools/install-build-deps --linux-arm
cd perfetto/
tools/gn gen --args='is_debug=false' out/linux
tools/ninja -C out/linux tracebox traced traced_probes perfetto

```

生成trace信息

```
sudo out/linux/tracebox -o trace_file.perfetto-trace --txt -c test/configs/scheduling.cfg

```

### 展现Trace

在刚才的网页中选择“Open trace file”，然后选中刚产出的文件（可通过远程命令，比如sz导出到本地） <img src="https://img-blog.csdnimg.cn/direct/339131e55fc746c09c787d4390e62b3a.png#pic_center" alt="在这里插入图片描述"> 我们就看到Linux系统上各个CPU核心和各个进程的运行情况 <img src="https://img-blog.csdnimg.cn/direct/93ac8ea4f2e4433e8816c88c00324cf7.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/19840f92e5b9445ea0381fe261299073.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/124571408351453f80122f099ba56f2d.png" alt="在这里插入图片描述">

## 参考资料
- - - 