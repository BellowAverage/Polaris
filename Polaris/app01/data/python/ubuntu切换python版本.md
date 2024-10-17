
--- 
title:  ubuntu切换python版本 
tags: []
categories: [] 

---
## 一、概述

在ubuntu环境下进行嵌入式开发，我们在进行不同的项目开发时，可能会遇到python环境不统一的情况。这时，我们可以通过update-alternatives来方便更新ubuntu下的python环境，来适应不同的项目工程。

## 二、使用update-alternatives更新python版本

### 2.1、查看ubuntu下的所有python版本

```
ls /usr/bin/python*

```

输出结果：

```
/aic8800/target_test# ls /usr/bin/python*
/usr/bin/python     /usr/bin/python3.8         /usr/bin/python3-futurize
/usr/bin/python2.7  /usr/bin/python3.8-config  /usr/bin/python3-pasteurize
/usr/bin/python3    /usr/bin/python3-config


```

我这里本来是没有2.7版本的，可以通过apt-get install安装

```
sudo apt-get install python2.7

```

如果python后面没有跟版本号，可以直接使用“路径 --version 来查看”

```
/usr/bin/python --version

```

### 2.2、更新update-alternatives替代列表

```
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 2 # 添加Python2可选项，优先级为2
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.4 1 #添加Python3可选项，优先级为1

```

注意，如果没有上述命令，会产生如下错误：

```
update-alternatives: error: no alternatives for python

```

### 2.3、查看update-alternatives下的python版本

```
sudo update-alternatives --list python

```

输出结果：

```
root@ubuntu:/usr/bin# update-alternatives --list python
/usr/bin/python2.7
/usr/bin/python3.8


```

### 2.4、切换python版本

update-alternatives默认是auto模式，它会根据你设置的优先级，选择优先级最高的python版本，优先级值越大，优先级越高。 我们可以通过 --config选项手动切换python版本

```
sudo update-alternatives --config python

```

输出结果：

```
root@ubuntu:/usr/bin# sudo update-alternatives --config python
There are 2 choices for the alternative python (providing /usr/bin/python).

  Selection    Path                Priority   Status
------------------------------------------------------------
  0            /usr/bin/python2.7   2         auto mode
  1            /usr/bin/python2.7   2         manual mode
* 2            /usr/bin/python3.8   1         manual mode

Press &lt;enter&gt; to keep the current choice[*], or type selection number: 

```

我们在后面输入对应的数字即可选择对应的python版本。

### 2.5、删除python版本

如果不需要某个python版本，可以将其从update-alternatives中删除：

```
sudo update-alternatives --remove python /usr/bin/python2.7

```
