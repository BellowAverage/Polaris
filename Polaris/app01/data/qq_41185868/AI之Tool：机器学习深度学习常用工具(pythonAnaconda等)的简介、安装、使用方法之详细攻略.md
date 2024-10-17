
--- 
title:  AI之Tool：机器学习/深度学习常用工具(python/Anaconda等)的简介、安装、使用方法之详细攻略 
tags: []
categories: [] 

---
AI之Tool：机器学习/深度学习常用工具(python/Anaconda等)的简介、安装、使用方法之详细攻略





**目录**



















## **<strong><strong>机器学习/深度学习常用工具的简介**</strong></strong>

### **<strong><strong>1、面向个人—环境配置：操作系统+编译环境+编程语言**</strong></strong>
<td style="width:82px;"> **<strong>操作系统**</strong> </td><td style="width:606px;"> 推荐Windows(适合小白) Python是一种跨平台的编程语言，几乎可以在各种操作系统上运行。比如Linux、Windows、macOS等 </td>

推荐Windows(适合小白)
<td rowspan="3" style="width:82px;"> **<strong>开发环境**</strong> </td><td style="width:606px;"> 推荐Pycharm </td>

推荐Pycharm
<td style="width:606px;"> **<strong>T1、本地的IDE**</strong> **<strong>IDLE（Python自带的集成开发环境）**</strong>： Python的标准发行版中自带的简单集成开发环境，适合初学者。 **<strong>PyCharm**</strong>： 由JetBrains公司开发，是一款功能丰富的商业IDE，支持Python和其他多种语言。 **<strong>Jupyter Notebook**</strong>： 交互式计算环境，适用于数据科学、机器学习等领域。 **<strong>Visual Studio Code（VSCode）**</strong>： 由Microsoft开发，是一款轻量级的跨平台编辑器，支持Python和许多其他编程语言。 **<strong>Spyder**</strong>： 适用于科学计算和数据分析的IDE，集成了IPython控制台。 **<strong>Atom**</strong>： 由GitHub开发，是一个开源的文本编辑器，支持Python和其他多种语言。 **<strong>Sublime Text**</strong>： 一款轻量级但功能强大的文本编辑器，通过插件支持Python开发。 **<strong>Thonny**</strong>： 一个专为初学者设计的Python IDE，具有简单易用的界面。 </td>

**<strong>IDLE（Python自带的集成开发环境）**</strong>： Python的标准发行版中自带的简单集成开发环境，适合初学者。

**<strong>Jupyter Notebook**</strong>： 交互式计算环境，适用于数据科学、机器学习等领域。

**<strong>Spyder**</strong>： 适用于科学计算和数据分析的IDE，集成了IPython控制台。

**<strong>Sublime Text**</strong>： 一款轻量级但功能强大的文本编辑器，通过插件支持Python开发。
<td style="width:606px;"> **<strong>T2、在线的IDE**</strong> **<strong>Jupyter Notebooks（Google Colab）**</strong>：Google Colab 是基于Jupyter Notebooks的云端平台，特别适用于数据科学和机器学习。它允许用户在云端运行Python代码，并提供了免费的GPU资源。 地址： **<strong>Repl.it**</strong>：Repl.it 提供了一个在线的编程环境，支持多种编程语言，包括Python。用户可以创建、共享和运行Python代码。 地址： **<strong>PythonAnywhere**</strong>：PythonAnywhere 提供了一个在线的Python开发环境，支持Web开发和数据分析。用户可以直接在浏览器中编写、运行和部署Python代码。 地址： **<strong>Trinket**</strong>：Trinket 是一个在线的编程平台，支持多种编程语言，包括Python。它适用于教育和快速原型开发。 地址： **<strong>CodeSandbox**</strong>：CodeSandbox 主要用于Web开发，但也支持Python。它提供了一个沙箱环境，让用户能够在浏览器中编辑和运行代码。 地址： **<strong>IDEOne**</strong>：IDEOne 是一个在线的IDE，支持多种编程语言，包括Python。用户可以在浏览器中编写、运行和分享代码。 地址： </td>

**<strong>Jupyter Notebooks（Google Colab）**</strong>：Google Colab 是基于Jupyter Notebooks的云端平台，特别适用于数据科学和机器学习。它允许用户在云端运行Python代码，并提供了免费的GPU资源。

**<strong>Repl.it**</strong>：Repl.it 提供了一个在线的编程环境，支持多种编程语言，包括Python。用户可以创建、共享和运行Python代码。

**<strong>PythonAnywhere**</strong>：PythonAnywhere 提供了一个在线的Python开发环境，支持Web开发和数据分析。用户可以直接在浏览器中编写、运行和部署Python代码。

**<strong>Trinket**</strong>：Trinket 是一个在线的编程平台，支持多种编程语言，包括Python。它适用于教育和快速原型开发。

**<strong>CodeSandbox**</strong>：CodeSandbox 主要用于Web开发，但也支持Python。它提供了一个沙箱环境，让用户能够在浏览器中编辑和运行代码。

**<strong>IDEOne**</strong>：IDEOne 是一个在线的IDE，支持多种编程语言，包括Python。用户可以在浏览器中编写、运行和分享代码。
<td style="width:82px;"> **<strong>编程语言**</strong> </td><td style="width:606px;"> 推荐Python **<strong>Python**</strong>：Python是机器学习和深度学习领域最常用的编程语言之一。它有丰富的库和框架，如NumPy、Pandas、Scikit-learn、TensorFlow和PyTorch，使其成为研究和实际应用中的首选语言。 **<strong>R**</strong>：R语言在统计学、数据分析和可视化方面非常强大，因此在一些统计学和数据科学的任务中得到广泛应用。有一些机器学习库，如caret和randomForest，提供了在R中实现机器学习算法的功能。 **<strong>Matlab**</strong>：Matlab是一种用于科学计算和工程领域的高级编程语言和环境，广泛用于数学建模、数据分析和信号处理。有一些机器学习工具，如Machine Learning Toolbox和Deep Learning Toolbox。 **<strong>C++**</strong>：C++在性能要求较高的领域中得到广泛应用，例如深度学习框架TensorFlow和Caffe就使用了C++。同时，也有一些C++库和工具用于机器学习。 **<strong>Java**</strong>：Java在企业级应用中有很大的影响力，而且也有一些用于机器学习和深度学习的库，如Deeplearning4j。 **<strong>Julia**</strong>：Julia是一种专为科学计算设计的新兴语言，由于其高性能的特性，一些深度学习框架如Flux.jl开始支持它。 </td>

推荐Python

**<strong>R**</strong>：R语言在统计学、数据分析和可视化方面非常强大，因此在一些统计学和数据科学的任务中得到广泛应用。有一些机器学习库，如caret和randomForest，提供了在R中实现机器学习算法的功能。

**<strong>C++**</strong>：C++在性能要求较高的领域中得到广泛应用，例如深度学习框架TensorFlow和Caffe就使用了C++。同时，也有一些C++库和工具用于机器学习。

**<strong>Julia**</strong>：Julia是一种专为科学计算设计的新兴语言，由于其高性能的特性，一些深度学习框架如Flux.jl开始支持它。



### **<strong><strong>2、面向企业和个人—**</strong>**<strong>企业级机器学习云服务**</strong></strong>
| **<strong>低代码形式**</strong> | **<strong>企业级机器学习云服务：**</strong> **<strong>阿里云的机器学习PAI**</strong>：拖拉傻瓜式的进行各个步骤。 地址： **<strong>AWS ML：**</strong>  

**<strong>企业级机器学习云服务：**</strong>

地址：









## **<strong><strong>机器学习/深度学习常用工具的安装**</strong></strong>

### **<strong><strong>1、直接安装python**</strong></strong>

相关资料很多，可自行查询本博客内的文章，持续更新中……





### **<strong><strong>2、安装Anaconda**</strong></strong>

相关资料很多，可自行查询本博客内的文章，持续更新中……












