
--- 
title:  [Python]win11环境下python怎么通过命令行升级版本 
tags: []
categories: [] 

---
在Windows 11环境下，可以通过以下命令行来升级Python版本： 可以在查看最新版本。 值得注意的是，最新版的python pip的数据源们可能没有，不必强求使用pip安装，可以在官网下载需要的python版本，然后覆盖安装的。

## 1、cmd升级python版本

首先打开命令行终端，可以使用快捷键"Win+R"打开运行窗口，输入"cmd"并按下"Enter"键。

然后在命令行中输入以下命令来安装Python的升级工具pip：

```
python -m ensurepip --default-pip

```

安装完成后，使用以下命令来升级Python版本：

```
pip install --upgrade python

```

如果你想将Python版本升级到特定的版本，可以使用以下命令：

```
pip install --upgrade python==3.x.x

```

如果网络连接异常，检查网络无误后，可以在命令后指定数据源，例如

```
pip install --upgrade python==3.11.4 -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com

```

其中，将"3.x.x"替换为你想要安装的Python版本号即可。 升级完成后，可以使用以下命令来确认Python版本号：

```
python --version

```

如果输出的版本号与你期望的版本号不一致，可以重新打开一个命令行窗口来确认。

**本文为使用ChatGPT获取，ChatGPT用在不熟悉的领域、用在不了解关键词的场景、用在当做字典与备忘录方面都很好用。**

## 2、国内常用镜像

阿里云 http://mirrors.aliyun.com/pypi/simple

豆瓣 http://pypi.douban.com/simple

清华大学 https://pypi.tuna.tsinghua.edu.cn/simple

中科大 http://pypi.mirrors.ustc.edu.cn/simple

网易云 https://mirrors.163.com/pypi/simple

```
--trusted-host 镜像域名

```
