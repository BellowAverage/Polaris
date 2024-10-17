
--- 
title:  机器学习分步走之一：安装使用scikit-learn 
tags: []
categories: [] 

---
## 机器学习分步走之一：安装使用scikit-learn

### Machine Learning Step by Step, First Pace to Install and Use scikit-learn

### 前言

为了适应快速发展的机器学习的需要，人们从经验中获取新知识、新技能的手段和方法日新月异，软件应用与开发也越来越普遍。

我们可能用这些机器学习程序，去电商网站购买自己喜欢的服装、电子设备等，并希望降价通知到我们；同时，在网络音乐应用上，搜索自己喜欢的歌手，喜欢音乐的风格，并希望推送给我们新的音乐等等。

机器学习恰恰是对软件工程项目的设计和学习，它可能使用已知的经验，已有的方法去预测和指导未来的决策。

机器学习系统通常被分为监督学习、无监督学习，有时候还有强化学习的分支情况，总之，都是从经验中学习。这其中，涉及到很多概念、知识点和必要的编程技能。本文试图从应用角度，分步骤介绍机器学习，从而希望达到逐步认知、循序渐进的效果，来满足对此感兴趣的读者。

### Scikit-learn简介

从2007年开始，由David Cournapeau主导的Google Summer of Code项目起步，开始研发scikit-learn项目；当年晚些时候，Matthieu Brucher开始了这个项目的工作，作为他的论文的组成部分。

此后，在2010年，INRIA公司的Fabian Pedregosa, Gael Varoquaux, 以及Alexandre Gramfort和Vincent Michel领导了该项目，并在2010年2月1日首次公开发布；此后，一个蓬勃发展的国际社区就一直在引领着这个领域的发展潮流。

截至2023年，scikit-learn和TensorFlow一道，已成为全球最佳的十大机器学习库之一，并且它们是由Python编程语言开发而成的。

Scikit-learn类库提供了用于机器学习的主要算法，包括分类、回归、降维和聚类。它也提供用于数据预处理、特征提取、优化超参数和评估模型的模块。

Scikit-learn类库基于广受欢迎的Numpy, Scipy库创建；其中，Numpy扩展了Python标准库，以支持大数组和多维矩阵并使其高效运作，而Scipy提供了科学计算的模块。另外，知名的可视化类库Matplotlib也常常与scikit-learn一起联合使用。

### 安装scikit-learn

本文将对安装scikit-learn的最新版本1.3.0展开讲述。 首先，如果第一次安装scikit-learn，需要访问其官网链接： 。

<img src="https://img-blog.csdnimg.cn/e90a958c920a4f1b8612d3ebffd510c7.png" alt="在这里插入图片描述"> 在上方导航栏，点击Install菜单，跳转到安装页面。 选择pip工具来安装scikit-learn最新版。（使用pip前提是已经安装了单机版Python软件包，或者安装了包含Python的Anaconda或MiniConda）.

>  
 *如需安装64位的Python 3，请访问其官网： 


接下来，打开Windows Terminal(即Power Shell) 或者Windows命令行（即cmd）,执行pip安装命令，完成scikit-learn的安装。

```
pip install -U scikit-learn

```

<img src="https://img-blog.csdnimg.cn/8591aeaa579c481d9f6db453f6bbc470.png" alt="在这里插入图片描述"> 安装完毕，如需验证scikit-learn版本，进入python控制台，输入以下命令：

```
&gt;&gt;&gt; import sklearn
&gt;&gt;&gt; sklearn.__version__
‘1.3.1’

```

*注：如果为了项目需求，需要独立的虚拟空间来运行机器学习，那么， 需要执行以下命令，来建立虚拟环境并激活它。

```
$ python -m venv sklearn-venv
$ sklearn-venv\Scripts\activate

```

之后，再进行scikit-learn的安装，以及其它相关库的安装。

>  
 同时，为了运行scikit-learn单元测试(Unit Test),还需要安装Python库的nose； nose扩展了Unittest的测试加载和运行功能，使编写、查找和运行测试变得更加容易可行。Nose附带的插件支持文档测试、代码覆盖和分析、灵活的测试选择（基于属性）及输出捕获等；有关编写插件，可在nose API文档中查询， 访问： 


现在，安装nose. 访问Python库网站： ,搜索到nose3；目前，最新版本位nose3 1.3.8. 发布于2022年1月27日。执行安装命令如下：

```
pip install nose3

```

<img src="https://img-blog.csdnimg.cn/ecde04817d6146bf9aa4926c53161614.png" alt="在这里插入图片描述"> 安装完毕后，在一个终端模拟器（例如：PowerShell）执行以下命令来验证nose3.

```
python -m pip show nose3

```

<img src="https://img-blog.csdnimg.cn/90bf0f4415224150975a59f1311a0a06.png" alt="在这里插入图片描述"> 以上命令输出的结果是：nose安装版本为1.3.8。

接下来，编写一个最简单的Python程序hello_world.py, 添加程序代码：

```
print(“Hello, world!”)

```

在Power Shell中查看代码，并进行nose测试（没有编写相应单元测试代码，仅运行nose）:

```
cat hello_world.py
nodetests hello_world.py

```

<img src="https://img-blog.csdnimg.cn/4a45b587b52641a09795753a88093d2f.png" alt="在这里插入图片描述">

可以看到OK字样，虽然没有关联测试代码，但是nose3运行正常。

至此，已经成功地安装了scikit-learn! 让我们继续吧，一起启动机器学习阶段！

下一篇见。😊
