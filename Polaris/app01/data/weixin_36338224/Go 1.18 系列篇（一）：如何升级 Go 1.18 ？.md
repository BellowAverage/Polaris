
--- 
title:  Go 1.18 系列篇（一）：如何升级 Go 1.18 ？ 
tags: []
categories: [] 

---
在上周，Go 1.18 终于是发布了，在上一篇文章中，我在留言中说，接下来几天会把玩一下 Go 1.18 的新特性，并跟大家分享一下学习心得。 今天第一篇，先升级一下 Go 1.18 ，关于新特性，咱明天再开整～

Go 官方推荐的 Go 升级方法是先安装新版本的下载器，再使用下载器去安装新版本的 Go，总结一下就是如下三条命令

```
~ ➤ go install golang.org/dl/go1.18@latest
~ ➤ go1.18 download
~ ➤ go1.18 version


```

由于国内网络问题，使用这种方式并不适合国内的用户，因为基本下载不下来，因此明哥今天推荐一种更通用的方法，教你快速升级 Go 1.18。

<img src="https://img-blog.csdnimg.cn/img_convert/18b6edd8fc09a891c2bc6b25e512f748.png" alt="">

### 1. 下载 &amp; 安装

到 https://go.dev/dl/ 下载界面去，选择与你电脑想匹配的 Go 二进制文件，然后直接使用 wget 进行下载，这些链接不需要梯子也可以轻松访问

由于我的是 M1 的 mac，因此使用如下链接

```
~ ➤ wget https://go.dev/dl/go1.18.darwin-arm64.tar.gz


```

使用二进制安装 Go，是我一直惯用的方式，它
- 非常地简单：只需要解压再移动即可- 主要是通用：不依赖网络，而且跨平台
在以前的教程中，也曾多次介绍过。

```
# 先解压
~ ➤ tar -C /tmp/ -xzf go1.18.darwin-arm64.tar.gz

# 再移动
~ ➤ sudo mv /tmp/go /usr/local/go18

# 后访问
~ ➤ /usr/local/go18/bin/go version
go version go1.18 darwin/arm64


```

### 2. 配置环境

现实中，我们不会使用绝对路径去访问 go，因此需要做一些 magic 的事情，这些我在以前的文章中也分享中

```
~ ➤ cat &lt;&lt; EOF &gt;/usr/local/go18/bin/go18
unset GOROOT
go env -w GOROOT="/usr/local/go18/"
/usr/local/go18/bin/go \$@
EOF
~ ➤ cat /usr/local/go18/bin/go18
unset GOROOT
go env -w GOROOT="/usr/local/go18/"
/usr/local/go18/bin/go $@
~ ➤ 
~ ➤ sudo ln -s /usr/local/go18/bin/go18 /usr/local/bin/go18
~ ➤


```

配置完成后，就可以直接使用 go18 命令去访问 go1.18，并且它与你默认的 go 版本不会冲突

<img src="https://img-blog.csdnimg.cn/img_convert/ca048dffb2ecd0cbb0e50f3e37baa818.png" alt="">

如此一来，环境就配置好啦～

下篇我就开始介绍 Go 1.18 的第一个特性：泛型。
