
--- 
title:  使用Python/NetworkX的图表数据科学 
tags: []
categories: [] 

---
<img alt="" src="https://img-blog.csdnimg.cn/img_convert/6928041c7315cfac1455604fd25ca98a.png">

## 使用Python/NetworkX的图形数据科学

Albanese是一名开发人员和数据科学家，曾在Facebook工作，在那里他进行了机器学习模型的预测。他是一位Python专家，也是一位大学讲师。他的博士研究与图形机器学习有关。

我们被数据所淹没。不断扩大的数据库和电子表格中充斥着隐藏的商业洞察力。当数据如此之多时，我们如何分析数据并提取结论？图表（网络，而不是条形图）提供了一种优雅的方法。

我们经常使用表格来通用地表示信息。但图表使用了一种专门的数据结构。一个**节点**代表一个元素，而不是一个表格行。一条**边**连接两个节点以表示它们的关系。

这种图数据结构使我们能够从独特的角度观察数据，这就是为什么图数据科学被用于从分子生物学到社会科学的各个领域。



左图来源：TITZ, Björn, 等人 "The Binary Protein Interactome of Treponema Pallidum ..."PLoS One, 3, no.5 (2008).

右图来源：ALBANESE, Federico, et al. "Predicting Shifting Individuals Using Text Mining and Graph Machine Learning on Twitter."。(2020年8月24日): arXiv:2008.10749 [cs.SI]

那么，开发者如何利用图数据科学呢？让我们来看看。Python。

### 在Python中开始使用 "图论 "图形

有几个可用的图数据库，如NetworkX、igraph、SNAP和graph-tool。撇开优点和缺点不谈，它们都有非常相似的接口来处理Python的图数据结构。

我们将使用流行的 。它的安装和使用都很简单，并且支持我们将要使用的社区检测算法。

用NetworkX创建一个新图是很简单的：

```
import networkx as nx
G = nx.Graph()
复制代码
```

但是`G` ，因为没有节点和边，所以还算不上是一个图。

#### 如何向图中添加节点

我们可以通过将`Graph()` 的返回值与`.add_node()` （或`.add_nodes_from()` ，用于列表中的多个节点）连锁起来，向网络添加一个节点。我们还可以通过传递一个字典作为参数来向节点添加任意的特征或属性，正如我们在`node 4` 和`node 5` 中所展示的：

```
G.add_node("node 1")
G.add_nodes_from(["node 2", "node 3"])
G.add_nodes_from([("node 4", {"abc": 123}), ("node 5", {"abc": 0})])
print(G.nodes)
print(G.nodes["node 4"]["abc"]) # accessed like a dictionary
复制代码
```

这将输出：

```
['node 1', 'node 2', 'node 3', 'node 4', 'node 5']
123
复制代码
```

但是，如果没有节点之间的边，它们就会被孤立起来，而数据集也不会比一个简单的表格好。

#### 如何向图添加边


