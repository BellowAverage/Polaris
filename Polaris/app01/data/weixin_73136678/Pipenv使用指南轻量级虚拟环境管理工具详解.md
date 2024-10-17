
--- 
title:  Pipenv使用指南:轻量级虚拟环境管理工具详解 
tags: []
categories: [] 

---
<img alt="" src="https://img-blog.csdnimg.cn/img_convert/ecb9860ba9c988baf115c679614e8113.webp?x-oss-process=image/format,png">

## 前言

终于能够挤出一点时间来总结最近学到的一些技术知识点了，博主这两周被居家隔离-集中隔离-居家隔离来回折腾，现在终于是得到解放能够空出的时间来写写博客了，但是项目又催的紧，写博文的时间还是有限，这周我会尽量更新博文带来更多干货知识，一直以来谢谢大家的支持！学习是一个不断坚持的动态过程，学以致用才是关键。

## 一、为什么使用pipenv？

首先我们要明白pipenv存在的开发驱动是什么，对于python虚拟环境来说已经有virtualenv了，在anaconda直接切换一下环境就好了，那么为什么要使用pipenv这个虚拟管理工具呢？

再者就是为什么要使用虚拟环境，我们直接将所有的库都集中安装到一个环境中，想怎么使用就怎么使用，直接调取任何库就可以完成功能，为啥要将其他的库给分开呢？

那么首先来讲讲将所有库都集成到一个环境下带来的问题，可能前期会觉得特别方便，但是等到开发的项目越来越多或者是有打包的需求的话，就很麻烦了，总结一下共有三点弊端：
- 库之间版本调试，切换问题。对于每个库来说都有兼容与不兼容的python版本，一些特殊的库，比如Jython库就不支持3.x以上的库，仅支持2.7的。如果你的项目需要使用到例如此类的库，但是总不可能将原来的python版本给完全删除重新装过该版本的库。那么环境管理工具就派上用场了。- 使用pyinstaller打包成为一个exe程序，一般来说如果使用原始的环境去打包的话，那么由于pyinstaller的特性会使得打包的文件过于巨大。那是因为pyinstaller打包会将整个环境的依赖库统一打包起来，而一些该程序没有用到的库会造成冗余问题。- 包之间的依赖版本冲突，有时候集成了过多包会造成这个情况，相互依赖之间的包版本会冲突，但是如果都集中到一个环境里面就很难排查。
故有以上场景就诞生了不同python环境集成各种不同版本不同包的需求，那么让我们再来了解一下这些虚拟环境管理工具的对比。

### **virtualenv**
- 一个操作系统下，可以有多个“操作系统级别的”Python解释器；- 每个Python解释器有一个指向自己的pip工具，两者一一对应；- 通过virtualenv可以虚拟任何一个“操作系统级别的”Python解释器成为一个“虚拟级别”的解释器；- 每个“虚拟级别”的解释器又拥有自己独立的pip工具和site-packages。
### **virtualenvwrapper**

virtualenvwrapper是对virtualenv接口的封装。virtualenvwrapper会将虚拟环境的目录统一保存，不需手动管理，使用起来更加便利；

### pipenv

pipenv是Kenneth Reitz在2017年1月发布的Python依赖管理工具，现在由PyPA维护。你可以把它看做是pip和virtualenv的组合体，而它基于的Pipfile则用来替代旧的依赖记录方式（requirements.txt），pipenv 在易用性上要简单很多，同时增加了 lock 文件，能更好的锁定版本。如果没有特殊要求可以 pipenv 直接使用 lock 的版本，开发又可以小步迭代，实现依赖的稳步升级。

### pipenv优缺点

优点：
- 自动关联项目相关的 virtualenv，能够快速的加载 virtualenv 。- 提供的pipenv替代pip并自带一个依赖清单Pipfile，和依赖锁定Pipfile.lock。- Pipfile除了依赖清单还支持固定pypi源地址,固定python版本。- Pipfile还支持dev依赖清单.pipenv install的包会强制使用Pipfile中的源.- 使用pipenv graph命令可以看到依赖树。- 可以直接切换python2和python3
缺点：
- Windows下命令行终端开头没有没有venv的名称，让你不知道是否在虚拟环境中，容易误操作- 永久设置了Pipfile文件中的源以后，Pipfile文件中看到的还是官方源，但是实际上是已经走了你设置的源了。
## 二、使用步骤

### 1.安装

推荐使用python3版本：

```
pip3 install pipenv

复制代码
```

安装完成后可通过

```
pipenv --version

复制代码
```

查看版本和检测是否安装成功:

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/4d72adbae36a34f81422e8afd86f79b6.webp?x-oss-process=image/format,png">

### 2.创建虚拟环境

使用命令`pipenv install`，可在当前目录下创建 `Pipfile` 、 `Pipfile.lock` 文件，在虚拟环境目录下新增一个虚拟环境

**Pipfile文件：** 用于保存项目的python版本、依赖包等相关信息 。

```
[[source]]
url = "https://pypi.tuna.tsinghua.edu.cn/simple"
verify_ssl = true
name = "pypi"
 
[packages]
requests = "*"
pyyaml = "*"
Django = "*"
 
[dev-packages]
pytest = "*"
 
[requires]
python_version = "3.7"
 
[scripts]
django = "python manage.py runserver 0.0.0.0:8080"
复制代码
```
-  source 用来设置仓库地址，即指定镜像源下载虚拟环境所需要的包 -  packages 用来指定项目依赖的包，可以用于生产环境和生成requirements文件 -  dev-packages 用来指定开发环境需要的包，这类包只用于开发过程，不用于生产环境。 <li> 
  <ul>- requires 指定目标Python版本
scripts 添加自定义的脚本命令，并通过 pipenv run + 名称 的方式在虚拟环境中执行对应的命令 。

Pipfile 文件可以复制到其他项目内，通过执行pipenv install命令， 根据这个 Pipfile 文件生成虚拟环境和依赖包的安装

Pipfile.lock文件： 通过hash算法将包的名称和版本，及依赖关系生成哈希值，保证包的完整性，除修改镜像源，非必要情况不对该文件进行修改。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/c0c9add42e0374e56baf213a7146defc.webp?x-oss-process=image/format,png">

### 指定目录存放虚拟环境

存放虚拟环境的目录默认指定是`C:\Users\bobo.virtualenvs`目录下。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/2afedd55f8388250aeaf1904d59bb720.webp?x-oss-process=image/format,png">

```
pipenv install --python +版本号
复制代码
```

可指定python版本创建虚拟环境。

也可以通过：

```
pipenv install --two           创建指定python2.x版本的虚拟环境
pipenv install --three         创建指定python3.x版本的虚拟环境
复制代码
```

下载默认的环境。

### 安装第三方库

`pipenv`兼容pip命令，同样使用`pipenv install + 包名`的方式安装第三方库。在此目录下打开pycharm时会默认加载此目录对应的虚拟环境。

在pycharm的 `Terminal`终端输入命令：

```
pipenv install requests

复制代码
```

就可以了

### 修改镜像源

如果官方源站安装第三方库的速度很慢，安装失败，可以修改镜像源

`pipenv`兼容`pip`命令，所以也可以在命令加上参数

```
pipenv install requests -i https://pypi.tuna.tsinghua.edu.cn/simple

复制代码
```

若想要永久该虚拟环境的镜像源，则需要打开项目目录下的Pipfile 、 Pipfile.lock 文件，将source栏 url = "" 链接内容修改为需要的镜像源，例如修改为清华的镜像源url = ""

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/9fe8c3769d75bedc938c16f9d1e15621.webp?x-oss-process=image/format,png">

###  安装到dev环境

安装调试工具、性能测试工具、python语法工具，这些内容仅在本地环境有用，生产环境不需要这些。

比如单元测试相关的包unittest、pytest，只在开发阶段有用，为了和生产环境的包区分开来，可以通过命令 pipenv install --dev + 包名将其归类到【dev-packages】下。

例如安装pytest到开发环境

```
pipenv install --dev pytest

复制代码
```

### 常用命令

`pipenv`兼容大部分的pip命令，所以 `pip`命令能实现的内容，也能通过`pipenv`命令实现

#### 卸载命令

在项目所在虚拟环境中卸载requests包，并在Pipfile文件移除包名

```
pipenv uninstall requests 	
复制代码
```

在项目所在虚拟环境中卸载所有包，并在Pipfile文件移除包名

```
pipenv uninstall --all 	
复制代码
```

在项目所在虚拟环境中卸载所有dev环境的包，并在Pipfile文件移除[dev-packages]中的所有包名

```
pipenv uninstall --all --dev	
复制代码
```

#### 更新命令

在项目所在虚拟环境中更新requests包，并在Pipfile.lock文件中更新相应版本信息

```
pipenv update requests 
复制代码
```

在项目所在虚拟环境中更新所有包，并在Pipfile.lock文件中更新相应版本信息

```
pipenv update
复制代码
```

在项目所在虚拟环境中查看已过期的包的信息

```
pipenv update --outdated
复制代码
```

根据项目所在虚拟环境的Pipfile文件生成/更新Pipfile.lock文件中的依赖包信息

```
pipenv lock
复制代码
```

####  查看命令

查看项目位置

```
pipenv --where	
复制代码
```

 查看虚拟环境位置

```
pipenv --venv	
复制代码
```

 查看虚拟环境python解释器位置

```
pipenv --py	
复制代码
```

查看依赖包信息

```
pipenv graph	
复制代码
```

#### 激活与退出虚拟环境

使用pipenv install 命令创建虚拟环境时，创建成功会默认激活虚拟环境

若想退出虚拟环境，可输入 exit 退出（仅适用于黑屏终端，pycharm默认打开项目就加载了虚拟环境，只能修改指定的虚拟环境） 目录下存在 Pipfile 、 Pipfile.lock 文件，已创建过虚拟环境，可通过命令 pipenv shell进行激活。

#### 删除虚拟环境

直接在该目录下面打开终端输入：

```
pipenv --rm
复制代码
```

该命令无法在pycharm的Terminal终端执行。删除虚拟环境后，如果目录下仍存在 `Pipfile` 、 `Pipfile.lock` 文件，可以通过`pipenv install`重新进行安装虚拟环境，且重新安装的虚拟环境，名称与删除前一致

#### 生成requirements.txt 文件

`pipenv`可以像`virtualenv`一样使用命令生成`requirements.txt文件`

```
pipenv lock -r --dev &gt;requirement.txt
复制代码
```

命令中的`--dev`并不是说把 `Pipfile`文件中 `[dev-packages]`下的包导出，而是把所有依赖包导出。 `pipenv`还可以通过`requirements.txt文件 `安装依赖包

```
pipenv install -r requirement.txt
复制代码
```

### 通过pyinstaller导出

首先需要到安装pipenv虚拟环境下的目录安装pyinstaller

```
pipenv install pyinstaller
复制代码
```

将依赖包都安装完成后直接：

```
#开始打包
pyinstaller -Fw -i xx.ico ./xxx.py
复制代码
```

就好了

### 点关注，防走丢，**如有纰漏之处，请留言指教，非常感谢**
