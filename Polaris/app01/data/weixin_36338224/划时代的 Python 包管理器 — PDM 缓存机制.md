
--- 
title:  划时代的 Python 包管理器 — PDM 缓存机制 
tags: []
categories: [] 

---
**PDM 系列目录**

1、 2、 3、 4、 5、 6、

pdm 引入了 pep 582 的本地包目录，有很多人在质疑：每个项目都在自己项目目录之下，那和 venv 虚拟环境有什么区别？

不少人对于虚拟环境及 pep 582 的理解不深，有这个疑问也是正常的。

首先，第一点不同，虚拟环境有自己的 Python 解释器，而 pep 582 并没有新增 Python 解释器，因此 pep 582 更加轻量。

然后，第二点不同，就是我们今天的核心内容，pdm 缓存机制的支持。

如果多个 pdm 项目，依赖相同版本的同一个 python 包，正常情况下，每个项目会自己存一份到自己的 `__pypackages__` 目录下。

但这样有几个问题：
1. 浪费磁盘空间1. 安装速度慢
你或许会认为，现在磁盘是最便宜的硬件了，浪费一点无所谓，但有些 Python 项目的依赖包多到你无法想象，比如世界上最大的 Python 项目 OpenStack ，依赖包更是达到了上千个，就算你不心疼你的磁盘，那你的时间肯定很宝贵吧？

你创建一个新的 pdm 项目，要重头安装一遍这么多依赖包，没个一天时间也搞不定，到时你就知道缓存的重要性了。

### 1. 开启缓存

pdm 默认是关闭 cache 的，如有需要，可以通过如下命令进行开启

```
$ pdm config install.cache on


```

与缓存相关的配置有三个
- install.cache：是否开启缓存- install.cache_method：选择连接缓存的方式- cache_dir：指定缓存的存放目录
关于 cache_dir 如无特殊需要，可以不用管，用默认的目录即可

```
/Users/iswbm/Library/Caches/pdm


```

比较难以理解的，值得一讲的是 install.cache_method，它的值有两种：
- symlink：以软链接的方式连接- pth：以 pth 的方式连接
关于它们的区别，我在后边有详细的讲解，请继续往下

### 2. 简单示例

这边以一个简单的示例，让你了解缓存的工作原理。

首先我创建两个 pdm 项目

```
# 初始化第一个 pdm 项目
mkdir pdm-demo1 &amp;&amp; cd pdm-demo1
pdm init


# 初始化第二个 pdm 项目
mkdir pdm-demo2 &amp;&amp; cd pdm-demo2
pdm init


```

在 pdm-demo1 下，安装 typer 的包

```
pdm add typer


```

然后进入 python 交互式解释器，试着导入一下，查看导入的 typer 包路径是什么？

可以发现，存放的目录正是 cache_dir 所配置的目录

<img src="https://img-blog.csdnimg.cn/img_convert/bd17310d65c608f60ea9d2f6de4eade0.png" alt="">

然后进入 pdm-demo2 下，同样安装 typer 包

```
pdm add typer


```

同样进入 python 交互式解释器，试着导入一下，查看导入的 typer 包路径是什么？

可以发现，导入的 typer 与之前 pdm-demo1 的路径一致，说明这两个项目用的同一个 typer 包，避免了同个包同个版本的重复安装。

<img src="https://img-blog.csdnimg.cn/img_convert/d69a372e9173945a05cefc8f0703f73c.png" alt="">

### 3. 缓存的原理

关于缓存原理，其实并不难，对于不同的 install.cache_method 原理也不一样

#### cache_method=symlink

symlink 是默认的连接方式，也是最好理解的一种方式。

当你安装了 typer 包后，在本地包目录下就可以看到 typer 通过一个软链接的方式指向了缓存目录下的 typer 包

<img src="https://img-blog.csdnimg.cn/img_convert/030b89e29670c28888a48753e693d007.png" alt="">

#### cache_method=pth

对于 `.pth` 相信有不少人不清楚它的用法和原理，这里简单提一下。

当 Python 在遍历已知的库文件目录过程中，如果发现有 .pth 文件，就会将文件中所记录的路径加入到 sys.path 设置中，于是 .pth 文件说指明的库也就可以被 Python 运行环境找到了。

焦点回到 pdm 中来，如果你使用 cache_method=pth 的模式，你每安装一个包，在你的本地包目录下就会生成一个 `.pth` 文件，里面记录要缓存的包的 lib 目录。

这样一来，当 Python 在 `__pypackages__` 目录下查找包时，一旦发现有 `.pth` 文件，就会把 `.pth` 文件中记录的路径加入 sys.path 中去。

在上面的例子中，查看 `__pypackages__` 目录，可以发现有许多 aaa_xxx.pth 的文件，而这些文件的内容，即是我们缓存目录下对应包的 lib 目录

<img src="https://img-blog.csdnimg.cn/img_convert/48ccb48f7e65c59a256ea76e8c47baee.png" alt="">

### 4. 缓存的管理

pdm 管理缓存的命令帮助如下

<img src="https://img-blog.csdnimg.cn/img_convert/432a01bb9c722b01995d2f002f5f66f8.png" alt="">
- pdm cache clear：清理所有的缓存- pdm cache info：查看所有的缓存信息- pdm remove [pattern]：移除匹配到的文件- pdm cache list：列出所有在缓存中的 wheel 文件