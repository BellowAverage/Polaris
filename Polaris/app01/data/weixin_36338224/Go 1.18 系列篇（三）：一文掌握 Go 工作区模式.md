
--- 
title:  Go 1.18 系列篇（三）：一文掌握 Go 工作区模式 
tags: []
categories: [] 

---
系列导读： 1、 2、

对我来说，Go1.18 最 “实用” 的功能，应该是 Go 工作区模式，虽然上篇文章中的泛型在某些场景下也是非常有用，但我还没遇到泛型的使用场景，因此它不能为我带来收益，而 Go 的工作区模式，则不一样，它使得开发者在多个模块中的开发工作变得更加简单。

接下来来简单介绍一下

### 1. 诞生背景

在介绍 **工作区模式** （workspace mode）之前，先简单地说一下工作区诞生的背景，只有了解了痛点之后，学习一个新的知识点，才更有动力。

我在 `$GOPATH/src` 目录下创建 github.com/iswbm/demo 及 github.com/iswbm/util 两个空的 go 包

<img src="https://img-blog.csdnimg.cn/img_convert/fa6f911ff4bb0ea21f52d9382a003c20.png" alt="">

然后分别使用 go mod init 来初始化

```
$ cd github.com/iswbm/demo
$ go mod init github.com/iswbm/demo

$ cd ../util
$ go mod init github.com/iswbm/util


```

并在 demo 中写入 main.go，在 util 写入 util.go ，内容如下

<img src="https://img-blog.csdnimg.cn/img_convert/46ea581ed8a70f794604ee6e561c53a0.png" alt="">

我们都知道，正常 Go 项目中引用的包，都需要在对应代码托管网站上有该包，才能编译及运行。

但如果 demo 引用 util 项目的包，而 util 本身也还在自己的本地上开发，并没有上传到 github，那么 demo 包在调试过程中肯定是无法找到 util 包的。

在没有工作区的情况下（也即 Go 1.18 之前），可以通过在 go.mod 中使用 replace 来重定向

```
module github.com/iswbm/demo

go 1.17

require github.com/iswbm/util v1.0.0

replace github.com/iswbm/util =&gt; ../util


```

修改完 go.mod 后，运行正常输出

<img src="https://img-blog.csdnimg.cn/img_convert/16a3ff2711d156155906615f10dc335a.png" alt="">

可使用 replace 存在两个问题：
- replace 本身编辑就比较麻烦，我一直是手动编辑的- 开发完成后，还要记得将 replace 删除，并执行 go mod tidy ，否则别人就无法使用
### 2. 工作区模式

Go 1.18 提供的工作区模式，就可以优雅的解决如上出现的问题。

上面我使用的是 go 1.17 初始化的项目，现在要用 go 1.18 的工作区模式，因此先将 go.mod 里的 go 版本改为 go 1.18，并都所有的依赖全部删除。

<img src="https://img-blog.csdnimg.cn/img_convert/72810338a1f59ba8747fab67f4bde5d7.png" alt="">

然后退回到 `$GOPATH/src` 目录，执行如下命令创建工作区文件 go.work

```
go18 work init github.com/iswbm/demo github.com/iswbm/util


```

创建的 go.work 文件如下所示

<img src="https://img-blog.csdnimg.cn/img_convert/d72a46b53f4f2cd387fa0339539dcdcc.png" alt="">

然后无论我在哪个目录下，只要所在位置的父级目录有 go.work 文件，即处于该工作区内，go 的编译器都会自动引用本地的 util 包

<img src="https://img-blog.csdnimg.cn/img_convert/1294dec91f1e1f054b48225fcca8fe97.png" alt="">

### 3. 写在最后

有了工作区模式，将使整个开发流程更加流畅，个人认为这可能是 go1.18 最为实用的功能，强烈推荐大家使用起来～

另外 go.work 文件是工作区的标志，该文件不用上传至 github，只用于本地开发测试使用。
