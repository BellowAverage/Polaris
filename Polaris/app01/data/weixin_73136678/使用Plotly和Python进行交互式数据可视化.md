
--- 
title:  使用Plotly和Python进行交互式数据可视化 
tags: []
categories: [] 

---
<img alt="" src="https://img-blog.csdnimg.cn/img_convert/9a3d51fa4054c31b4c2dd3a8fd027967.jpeg">

## 使用Plotly和Python进行交互式数据可视化

Python是数据探索和数据分析的好帮手，这都要归功于numpy、pandas、matplotlib等神奇库的支持。在我们的数据探索和数据分析阶段，理解我们正在处理的数据是非常重要的，为此，数据的可视化表示可能是非常重要的。

对我们来说，使用Jupyter笔记本来完成这些项目是很常见的，因为它们很好，很快速，很简单，而且它们允许我们与我们的数据进行互动和游戏。然而，我们能做的事情是有限制的，通常我们在处理图表时，会使用matplotlib或seaborn等库，但这些库会呈现出我们的图表和图形的静态图像。但是，很多东西会在细节中丢失，因此我们需要对我们的图表进行微调，以探索我们数据的各个部分。如果我们可以通过缩放来与我们的图表互动，为我们的数据点添加上下文信息，如悬停互动，那不是很好吗？这里就是Plotly可以帮助我们的地方。

Plotly是一个Python库，可以制作交互式的、具有出版质量的图表，如线图、散点图、面积图、条形图、误差条、箱形图、直方图、热图、子图，以及更多更多。

但我们谈得够多了，让我们开始制作一些图表......

### 安装依赖项

在我们构建任何东西之前，让我们先安装依赖性。我喜欢使用`pipenv` ，但同样适用于Anaconda或其他软件包管理器。

下面是我们需要的依赖项的列表:

 - jupyter。网络应用程序，允许你创建和分享包含实时代码的文档，方程式....，你知道的！
 - pandas。非常强大的数据分析库，我们将在我们的项目中使用它来处理我们的数据
 - numpy。Python的科学计算，在我们的项目中用于数学和生成随机数
 - seaborn。基于matplotlib的统计数据可视化，我们将使用它来加载库中的一些样本数据。
 - cufflinks。允许 plotly 与 pandas 一起工作
 - plotly。交互式图表库

以下是安装它们的命令:

```
pipenv install jupyter
pipenv install plotly cufflinks pandas seaborn numpy
复制代码
```

### 入门

为了开始，我们需要启动我们的 jupyter 笔记本并创建一个新的文档:

```
pipenv run jupyter notebook
复制代码
```

一旦我们在那里，我们可以开始添加一些代码。由于这篇文章不是一个关于Jupyter笔记本的教程，我将只关注代码
