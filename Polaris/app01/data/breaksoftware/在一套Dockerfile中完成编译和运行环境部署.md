
--- 
title:  在一套Dockerfile中完成编译和运行环境部署 
tags: []
categories: [] 

---


#### 大纲
- - - - - <ul><li>- - - <ul><li>- - - - - - - - - - - - 


对于像C、C++这类编译型语言，编译器会直接将代码编译成二进制，然后在操作系统上执行。而像Java这类解释型语言，编译器（Java编译器是Java写的）会将代码编译成中间码，然后在虚拟机上执行，而虚拟机（Java虚拟机是C++写的，最后编译成二进制码）是在操作系统上执行的。 <img src="https://img-blog.csdnimg.cn/direct/f45f17a5475746dfb2f65fb5c8af1bad.png" alt="在这里插入图片描述"> 不管是编译型语言还是解释型语言，我们都可以把上述过程拆解为两部分

## 解释型语言

## 编译环境

<img src="https://img-blog.csdnimg.cn/direct/f6bd7ecb63a944aaa2bfd71416c96a34.png" alt="在这里插入图片描述">

## 解释环境

<img src="https://img-blog.csdnimg.cn/direct/4587145d85864ae299ec17e9394d44e5.png" alt="在这里插入图片描述"> 只是去除了Java代码和编译器，并不会让Docker产出的镜像小多少。

## 编译型语言

### 编译环境

<img src="https://img-blog.csdnimg.cn/direct/72055303c7b843629519f5685762ad5b.png" alt="在这里插入图片描述">

### 运行环境

<img src="https://img-blog.csdnimg.cn/direct/8de6b36e6270498d90a016a9627ad1a6.png" alt="在这里插入图片描述"> C、C++这类语言编译时期往往需要大量的资源，比如本文案例中，编译环境的镜像是2个多G，而运行环境这是1百多M，减少了93%的大小。

## 方法

我们可以在一套Dockerfile中，将编译环境的产出放置到运行环境，并且抛弃编译环境，只留下运行环境的镜像。

```
FROM ubuntu:22.04 as builder
RUN apt-get update &amp;&amp; apt-get install -y binutils-dev uuid-dev libssl-dev python3 python3-pip cmake git zip
RUN pip3 install gil
RUN mkdir source
WORKDIR /source
RUN git clone https://github.com/chronoxor/CppServer.git
WORKDIR /source/CppServer/examples
COPY http_server_diff.patch ./http_server_diff.patch
RUN patch -p0 &lt; http_server_diff.patch
WORKDIR /source/CppServer
RUN gil update
WORKDIR /source/CppServer/build
COPY unix_diff.patch ./unix_diff.patch
RUN patch -p0 &lt; unix_diff.patch
RUN ./unix.sh
WORKDIR /source/CppServer
RUN zip -r www.zip www/

FROM ubuntu:22.04 as runner
RUN apt-get update &amp;&amp; apt-get install -y libbinutils unzip
COPY --from=builder /source/CppServer/bin/cppserver-example-http_server /usr/local/bin/cppserver-example-http_server
COPY --from=builder /source/CppServer/www.zip /usr/local/bin/www.zip
EXPOSE 8080
WORKDIR /cppserver
RUN unzip /usr/local/bin/www.zip -d /cppserver
RUN apt remove -y unzip
RUN rm /usr/local/bin/www.zip
WORKDIR /cppserver/bin
RUN mv /usr/local/bin/cppserver-example-http_server ./cppserver-example-http_server
CMD ["cppserver-example-http_server"]

```

这段Dockerfile分为两部分

### 编译环境

#### 安装系统

首先选择ubuntu 22作为基础系统。我们要保证运行环境和编译环境的操作系统版本是一致的。 as builder是标识我们要将其当做编译环境使用。在运行环境的Dockerfile中我们需要借此标识引用编译环境，来导出二进制编译结果等在运行环境中需要数据。

```
FROM ubuntu:22.04 as builder

```

#### 安装编译依赖

安装好系统后，我们更新系统中包装管理软件（apt），以及安装编译代码时需要用的软件以及依赖（这一步，不同软件会需要不同的依赖）。

```
RUN apt-get update &amp;&amp; apt-get install -y binutils-dev uuid-dev libssl-dev python3 python3-pip cmake git zip
RUN pip3 install gil

```

#### 下载代码

准备好基础环境后，就可以下载代码了

```
RUN mkdir source
WORKDIR /source
RUN git clone https://github.com/chronoxor/CppServer.git

```

#### 特殊处理（可以忽略）

因为我们使用的开源库，在设计上不太符合我们要求，导致一运行就会退出。于是我们对源码打了Patch。这块知识可以参考》

```
WORKDIR /source/CppServer/examples
COPY http_server_diff.patch ./http_server_diff.patch
RUN patch -p0 &lt; http_server_diff.patch

```

http_server_diff.patch文件如下。它不再判断getline的返回值，而根据输入字母来决定是否退出还是重启。

```
--- http_server.cpp     2024-04-04 13:23:38.519576917 +0000
+++ http_server_bak.cpp 2024-04-04 13:52:57.483416162 +0000
@@ -221,17 +221,18 @@ int main(int argc, char** argv)
     server-&gt;Start();
     std::cout &lt;&lt; "Done!" &lt;&lt; std::endl;

-    std::cout &lt;&lt; "Press Enter to stop the server or '!' to restart the server..." &lt;&lt; std::endl;
+    std::cout &lt;&lt; "Press 'q' to stop the server or 'r' to restart the server..." &lt;&lt; std::endl;

     // Perform text input
     std::string line;
-    while (getline(std::cin, line))
+    while (true)
     {<!-- -->
-        if (line.empty())
+       getline(std::cin, line);
+        if (line == "q")
             break;

         // Restart the server
-        if (line == "!")
+        if (line == "r")
         {<!-- -->
             std::cout &lt;&lt; "Server restarting...";
             server-&gt;Restart();

```

这一段具有特异性，算是针对该项目的一个补丁。一般项目不太需要这个步骤。

#### 编译准备（可以忽略）

这一步是该编译项目需要做的前置动作，不具有普遍性。

```
WORKDIR /source/CppServer
RUN gil update
WORKDIR /source/CppServer/build
COPY unix_diff.patch ./unix_diff.patch
RUN patch -p0 &lt; unix_diff.patch

```

因为上一步我们修改了代码，导致这个开源项目的原始自动化测试不通过。上述补丁我们就是将自动化测试从流程中去除。 unix_diff.patch文件如下。

```
--- unix.sh     2024-04-04 14:01:10.668521739 +0000
+++ unix_bak.sh 2024-04-04 14:06:59.667047513 +0000
@@ -3,7 +3,6 @@ set -e
 cd Unix
 ./01-generate.sh
 ./02-build.sh
-./03-tests.sh
 ./04-install.sh
 if [[ "$doxygen" ]]; then
     ./05-doxygen.sh

```

#### 编译

每个软件的编译指令不同。下面的指令只针对我们例子中的工程。

```
RUN ./unix.sh

```

#### 打包依赖（编译结果）

因为我们这个工程是http服务器，它会用到www目录下的一些网页文件，所以我们需要用zip指令对它们进行打包，以方便后续统一搬运到运行环境。

```
WORKDIR /source/CppServer
RUN zip -r www.zip www/

```

### 运行环境

运行环境的命令和编译环境的命令是在一个Dockerfile中的。

#### 安装操作系统

我们使用和编译环境一样的操作系统以及版本。

```
FROM ubuntu:22.04 as runner

```

#### 安装运行时依赖

这一步我们安装的依赖就减少很多，主要是libbinutils 。它主要提供一些动态链接库，这些都是在运行时软件需要加载的公共库。 安装unzip是为了解压之前压缩的文件，后续我们会卸载它。

```
RUN apt-get update &amp;&amp; apt-get install -y libbinutils unzip

```

#### 复制编译结果和依赖

这一步我们将编译环境的编译结果cppserver-example-http_server拷贝到运行时环境，同时拷贝它依赖的一些文件。

```
COPY --from=builder /source/CppServer/bin/cppserver-example-http_server /usr/local/bin/cppserver-example-http_server
COPY --from=builder /source/CppServer/www.zip /usr/local/bin/www.zip

```

#### 暴露端口（非必须）

cppserver-example-http_server 需要运行在8080端口上。

```
EXPOSE 8080

```

#### 重整目录

这一步，我们会将之前复制过来的文件按照软件的要求重新部署目录结构。 另外我们卸载了为了搬运方便而安装的unzip软件。

```
WORKDIR /cppserver
RUN unzip /usr/local/bin/www.zip -d /cppserver
RUN apt remove -y unzip
RUN rm /usr/local/bin/www.zip
WORKDIR /cppserver/bin
RUN mv /usr/local/bin/cppserver-example-http_server cppserver-example-http_server

```

#### 运行时命令

```
CMD ["./cppserver-example-http_server"]

```

### 打包命令和运行命令

```
docker build --pull --rm -f "Dockerfile" -t cppserver:latest "." 
docker container run -d -p 8080:8080 --name cppserver cppserver:latest cppserver-example-http_server

```

## 效果

<img src="https://img-blog.csdnimg.cn/direct/66d43f6338c54006b42194a258bdd4ec.png" alt="在这里插入图片描述"> 我们删除了运行时Dockerfile，生成的镜像cppserver-builder，然后对比下它和运行时镜像的大小。 <img src="https://img-blog.csdnimg.cn/direct/b91c0ef8ff3942aa8b1a5f8e86250f9b.png#pic_center" alt="在这里插入图片描述">

## 参考资料
- 