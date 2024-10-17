
--- 
title:  静态分析Golang语言生成函数调用关系的利器——go-callvis 
tags: []
categories: [] 

---


#### 目录
- - <ul><li>- - - - <ul><li>- - - - <ul><li>- - 


不同于之前分析C语言项目的工具，go-callvis还是很方便使用。只要把两项工作做好就能顺利的使用。
1. go使用1.19及以上版本。1. 要在被分析工程的根目录执行分析指令。
我的测试环境是Ubuntu 22 TLS版，默认的Golang是1.18。这会导致go-callvis安装失败。如果版本匹配，可以忽略下面Golang升级的步骤。

## 升级go

### 删除旧版本

```
sudo apt remove golang-go golang-1.18-doc golang-1.18-go golang-1.18-src

```

### 安装新版本

直接上1.21版本。

```
sudo apt install golang-1.21

```

### 配置环境变量

```
sudo vim /etc/profile

```

在文件末尾另起新行填入以下内容

```
export GOROOT=/usr/lib/go-1.21
export GOPATH=$HOME/gowork
export GOBIN=$GOPATH/bin
export PATH=$GOPATH:$GOBIN:$GOROOT/bin:$PATH

```

### 载入环境

#### 修改当前环境

```
source /etc/profile

```

#### 修改之后进入的环境

```
sudo vim ~/.bashrc

```

在文件末尾另起一行新增

```
source /etc/profile

```

## 分析

我们以gorush的源码为例。它是一套基于Gin实现的消息推送框架。

```
https://github.com/appleboy/gorush.git

```

### 安装go-callvis

进入待分析工程目录

```
cd gorush

```

然后安装

```
go install github.com/ofabry/go-callvis@master

```

最后执行分析命令

```
go-callvis ./

```

>  
 2024/01/28 07:55:35 http serving at http://localhost:7878 2024/01/28 07:55:35 OpenURL error: exec: “xdg-open,x-www-browser,www-browser”: executable file not found in $PATH 


这样我们就在浏览器中打开http://localhost:7878看到分析结果 <img src="https://img-blog.csdnimg.cn/direct/d120593085464a7b8fd3d6636dab5911.png" alt="在这里插入图片描述"> go-callvis默认是寻找main包名，并以此为入口分析代码调用关系的。而且每个方法是以包名聚合的。如上图中，nats就是一个包名，其下的方法都被聚合在一起。这个特性由-group指定，默认是pkg（包），还可以是type。

### 分析其他包

如果我们希望分析其他包名，则需要使用-focus指定，而且路径要制定到包所在的目录（注意不是根目录），并且还要添加-algo static。如果路径不对，go-callvis会找不到对应的包（不会遍历子目录）。比如我们需要查看router包，它实际位于~/gorush/router目录下。如果执行

```
go-callvis -focus router -algo static ./

```

则会报错

>  
 focus failed, could not find package: router 


正确的指令是

```
 go-callvis -algo static -focus router ./router/

```

<img src="https://img-blog.csdnimg.cn/direct/f0feaa6937c94bfab9ff9bb5b5b02883.png" alt="在这里插入图片描述">

#### 总结

```
 go-callvis -algo static -focus 【package_name】 ./【package_path】

```

### 导出文件

上述方法都会启动一个服务器，然后在浏览器中查看。如果网络环境不允许，则我们可以让其产出图片。-format用于指定文件格式；-file用于指定导出的文件名。

```
 go-callvis -algo static \
  -focus router \
  -format=png \
  -file=gorush_router \
  ./router/

```

>  
 2024/01/28 08:14:51 writing dot output… 2024/01/28 08:14:51 converting dot to png… 


<img src="https://img-blog.csdnimg.cn/direct/8a75755a853d447f9ec2f5c1becd1c2d.png" alt="请添加图片描述"> 如果觉得这个图太长，则可以使用-rankdir转变成其他绘制方向（[LR | RL | TB | BT] (default “LR”)）。

```
go-callvis -algo static \
 -focus router \
 -format=png \
 -file=gorush_router_tb \
 -rankdir TB \
 ./router/

```

<img src="https://img-blog.csdnimg.cn/direct/96291e604b514033b6e655835bbdddae.png" alt="请添加图片描述">

#### 总结

```
 go-callvis -algo static \
  -focus 【package_name】\
  -format=【[svg | png | jpg | ...] (default "svg")】 \
  -file=【file_name】\
  ./【package_path】

```

### 清晰主体脉络

上面的图片还是很大，提供了大量信息。但是大量的信息也会带来一些干扰，我们可以通过增加一些参数，忽略一些不太重要的信息，来让调用框架清晰起来。

>  
 -nointer Omit calls to unexported functions. -nostd Omit calls to/from packages in standard library. 


-nostd表示标准库的包就不用展现了，这个可以省去大量最后一层的调用关系；-nointer则表示忽略非导出方法，这样我们就关注于包之间调用关系即可。

```
go-callvis -algo static \
 -focus router \
 -format=png \
 -file=gorush_router_noiter_nostd \
 -nointer -nostd \
 ./router/

```

<img src="https://img-blog.csdnimg.cn/direct/c582bba1c2dc4afba45c26cd18d1ef0d.png" alt="请添加图片描述">

#### 总结

```
 go-callvis -algo static \
  -focus 【package_name】\
  -format=【[svg | png | jpg | ...] (default "svg")】 \
  -file=【file_name】\
  -nointer -nostd \
  ./【package_path】

```

### 其他

我还对gin的源码做了测试

```
git clone https://github.com/gin-gonic/gin.git
cd gin
go install github.com/ofabry/go-callvis@master
go-callvis -algo static -focus gin -format=png -file=gin -nointer -nostd ./

```

<img src="https://img-blog.csdnimg.cn/direct/fa707a5228714c9089978819ddcc9e47.png" alt="请添加图片描述">

## 参考资料
- 