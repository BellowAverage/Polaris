
--- 
title:  Elasticsearch 
tags: []
categories: [] 

---
## Elasticsearch

### 简介与原理

You know, for search!

文档https://www.elastic.co/guide/cn/elasticsearch/guide/current/index.html

#### 简介

**Elasticsearch是一个基于Lucene库的搜索引擎。**

它提供了一个分布式、支持多用户的全文搜索引擎，**具有HTTP Web接口和无模式JSON文档。<strong>所有其他语言可以使用**RESTful API 通过端口</strong>****9200******和 Elasticsearch 进行通信**

**Elasticsearch是用Java开发的**，并在Apache许可证下作为开源软件发布。官方客户端在Java、.NET（C#）、PHP、Python、Apache Groovy、Ruby和许多其他语言中都是可用的。

根据DB-Engines的排名显示，**Elasticsearch是最受欢迎的企业搜索引擎**，其次是Apache Solr，也是基于Lucene。

Elasticsearch可以用于搜索各种文档。它提供可扩展的搜索，具有接近实时的搜索，并支持多租户。

**Elasticsearch是分布式的**，这意味着索引可以被分成分片，每个分片可以有0个或多个副本。每个节点托管一个或多个分片，并充当协调器将操作委托给正确的分片。再平衡和路由是自动完成的。相关数据通常存储在同一个索引中，该索引由一个或多个主分片和零个或多个复制分片组成。一旦创建了索引，就不能更改主分片的数量。

**Elasticsearch 是一个实时的分布式搜索分析引擎，它被用作全文检索、结构化搜索、分析以及这三个功能的组合**
-  Wikipedia 使用 Elasticsearch 提供带有高亮片段的全文搜索，还有**search-as-you-type**和**did-you-mean** 的建议。 -  **卫报**使用 Elasticsearch 将网络社交数据结合到访客日志中，实时的给它的编辑们提供公众对于新文章的反馈。 -  Stack Overflow 将地理位置查询融入全文检索中去，并且使用**more-like-this**接口去查找相关的问题与答案。 -  GitHub 使用 Elasticsearch 对1300亿行代码进行查询。 Lucene 仅仅只是一个库，然而，Elasticsearch 不仅仅是 Lucene，并且也不仅仅只是一个全文搜索引擎。 它可以被下面这样准确的形容： -  一个分布式的实时文档存储，**每个字段**可以被索引与搜索 -  一个分布式实时分析搜索引擎 -  能胜任上百个服务节点的扩展，并支持 PB 级别的结构化或者非结构化数据 
###### 面向文档的数据库

Elasticsearch 是**面向文档**的，意味着它存储整个对象或**文档。Elasticsearch 不仅存储文档，而且**索引每个文档的内容使之可以被检索。在 Elasticsearch 中，你 对文档进行索引、检索、排序和过滤–而不是对行列数据。

**Elasticsearch 有2.x、5.x、6.x 三个大版本，我们在黑马头条中使用5.6版本。**

#### 搜索的原理——倒排索引（反向索引）、分析、相关性排序

##### 倒排索引

倒排索引（英语：**Inverted index**），也常被称为**反向索引**、置入档案或反向档案，是一种索引方法，被用来存储在全文搜索下某个单词在一个文档或者一组文档中的存储位置的映射。**它是文档检索系统中最常用的数据结构。**

假设我们有两个文档，每个文档的`content`域包含如下内容：
1. The quick brown fox jumped over the , lazy+ dog1. Quick brown foxes leap over lazy dogs in summer
正向索引： 存储每个文档的单词的列表

<th align="left">Doc</th><th align="left">Quick</th><th align="left">The</th><th align="left">brown</th><th align="left">dog</th><th align="left">dogs</th><th align="left">fox</th><th align="left">foxes</th><th align="left">in</th><th align="left">jumped</th><th align="left">lazy</th><th align="left">leap</th><th align="left">over</th><th align="left">quick</th><th align="left">summer</th><th align="left">the</th>
|------
<td align="left">Doc1</td><td align="left"></td><td align="left">X</td><td align="left">X</td><td align="left">X</td><td align="left"></td><td align="left">X</td><td align="left"></td><td align="left"></td><td align="left">X</td><td align="left">X</td><td align="left"></td><td align="left">X</td><td align="left">X</td><td align="left"></td><td align="left">X</td>
<td align="left">Doc2</td><td align="left">X</td><td align="left">X</td><td align="left"></td><td align="left">X</td><td align="left"></td><td align="left">X</td><td align="left"></td><td align="left">X</td><td align="left">X</td><td align="left"></td><td align="left">X</td><td align="left">X</td><td align="left">X</td><td align="left"></td><td align="left">X</td>

反向索引：

```
Term      Doc_1  Doc_2
-------------------------
Quick   |       |  X
The     |   X   |
brown   |   X   |  X
dog     |   X   |
dogs    |       |  X
fox     |   X   |
foxes   |       |  X
in      |       |  X
jumped  |   X   |
lazy    |   X   |  X
leap    |       |  X
over    |   X   |  X
quick   |   X   |
summer  |       |  X
the     |   X   |
------------------------

```

如果我们想搜索`quick brown`，我们只需要查找包含每个词条的文档：

```
Term      Doc_1  Doc_2
-------------------------
brown   |   X   |  X
quick   |   X   |
------------------------
Total   |   2   |  1

```

两个文档都匹配，但是第一个文档比第二个匹配度更高。如果我们使用仅计算匹配词条数量的简单**相似性算法**，那么，我们可以说，对于我们查询的相关性来讲，第一个文档比第二个文档更佳。

##### 分析

上面不太合理的地方：
- `Quick`和`quick`以独立的词条(token)出现，然而用户可能认为它们是相同的词。- `fox`和`foxes`非常相似, 就像`dog`和`dogs`；他们有相同的词根。- `jumped`和`leap`, 尽管没有相同的词根，但他们的意思很相近。他们是同义词。
进行**标准化**：
- `Quick`可以小写化为`quick`。- `foxes`可以**词干提取**–变为词根的格式-- 为`fox`。类似的，`dogs`可以为提取为`dog`。- `jumped`和`leap`是同义词，可以索引为相同的单词`jump`。
标准化的反向索引：

```
Term      Doc_1  Doc_2
-------------------------
brown   |   X   |  X
dog     |   X   |  X
fox     |   X   |  X
in      |       |  X
jump    |   X   |  X
lazy    |   X   |  X
over    |   X   |  X
quick   |   X   |  X
summer  |       |  X
the     |   X   |  X
------------------------

```

**对于查询的字符串必须与词条（token）进行相同的标准化处理，才能保证搜索的正确性。**

分词和标准化的过程称为**分析**（analysis） ：
- 首先，将一块文本分成适合于倒排索引的独立的**词条**， -&gt;**分词**- 之后，将这些词条统一化为标准格式以提高它们的“可搜索性” -&gt;**标准化**
分析工作是由**分析器**完成的： analyzer
-  字符过滤器 首先，字符串按顺序通过每个**字符过滤器**。他们的任务是在分词前整理字符串。一个字符过滤器可以用来去掉HTML，或者将`&amp;`转化成`and`。 -  分词器 其次，字符串被**分词器**分为单个的词条。一个简单的分词器遇到空格和标点的时候，可能会将文本拆分成词条。 -  Token 过滤器 （词条过滤器） 最后，词条按顺序通过每个**token 过滤器**。这个过程可能会改变词条（例如，小写化`Quick`），删除词条（例如， 像`a`，`and`，`the`等无用词），或者增加词条（例如，像`jump`和`leap`这种同义词）。 
##### 相关性排序

默认情况下，搜索结果是按照***相关性***进行倒序排序的——最相关的文档排在最前。

相关性可以用相关性评分表示，评分越高，相关性越高。

评分的计算方式取决于查询类型 不同的查询语句用于不同的目的：`fuzzy`查询（模糊查询）会计算与关键词的拼写相似程度，`terms`查询（词组查询）会计算 找到的内容与关键词组成部分匹配的百分比，但是通常我们说的 相关性 是我们用来计算全文本字段的值相对于全文本检索词相似程度的算法。

Elasticsearch 的相似度算法 被定义为检索词频率/反向文档频率，**TF/IDF**，包括以下内容：
-  检索词频率 检索词在该字段出现的频率？出现频率越高，相关性也越高。 字段中出现过 5 次要比只出现过 1 次的相关性高。 -  反向文档频率 每个检索词在索引中出现的频率？频率越高，相关性越低。检索词出现在多数文档中会比出现在少数文档中的权重更低。 -  字段长度准则 字段的长度是多少？长度越长，相关性越低。 检索词出现在一个短的 title 要比同样的词出现在一个长的 content 字段权重更大。 
### 索引与集群

#### 索引

存储数据到 Elasticsearch 的行为叫做**索引**（indexing）

关于数据的概念

```
Relational DB -&gt; Databases 数据库 -&gt; Tables 表 -&gt; Rows 行 -&gt; Columns 列
Elasticsearch -&gt; Indices 索引库 -&gt; Types 类型 -&gt; Documents 文档 -&gt; Fields 字段/属性

```

一个 Elasticsearch 集群可以 包含多个**索引**（indices 数据库），相应的每个索引可以包含多个**类型**（type 表） 。 这些不同的类型存储着多个**文档**（document 数据行） ，每个文档又有 多个**属性**（field 列）。

#### Elasticsearch 集群（cluster）

Elasticsearch 尽可能地屏蔽了分布式系统的复杂性。这里列举了一些在后台自动执行的操作：
- 分配文档到不同的容器 或 **分片** 中，文档可以储存在一个或多个节点中- 按集群节点来均衡分配这些分片，从而对索引和搜索过程进行负载均衡- 复制每个分片以支持数据冗余，从而防止硬件故障导致的数据丢失- 将集群中任一节点的请求路由到存有相关数据的节点- 集群扩容时无缝整合新节点，重新分配分片以便从离群节点恢复 <img src="https://img-blog.csdnimg.cn/20200113224523727.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTgwNTMzOQ==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">
##### 节点（node）

**一个运行中的 Elasticsearch 实例称为一个 节点**，而集群是由一个或者多个拥有相同`cluster.name`配置的节点组成， 它们共同承担数据和负载的压力。当有节点加入集群中或者从集群中移除节点时，集群将会重新平均分布所有的数据。

当一个节点被选举成为****主******节点（master）时， 它将负责管理集群范围内的所有变更**，例如增加、删除索引，或者增加、删除节点等。 而**主节点并不需要涉及到文档级别的变更和搜索等操作**，所以当集群只拥有一个主节点的情况下，即使流量的增加它也不会成为瓶颈。 任何节点都可以成为主节点。我们的示例集群就只有一个节点，所以它同时也成为了主节点。

作为用户，**我们可以将请求发送到******集群中的任何节点******，包括主节点**。 每个节点都知道任意文档所处的位置，并且能够将我们的请求直接转发到存储我们所需文档的节点。 无论我们将请求发送到哪个节点，它都能负责从各个包含我们所需文档的节点收集回数据，并将最终结果返回給客户端。 Elasticsearch 对这一切的管理都是透明的。

##### 分片（shard）

一个**分片**是一个底层的**工作单元**，它仅保存了 全部数据中的一部分。

索引实际上是指向一个或者多个物理**分片**的**逻辑命名空间**。

文档被存储和索引到分片内，但是应用程序是直接与索引而不是与分片进行交互。

Elasticsearch 是利用分片将数据分发到集群内各处的。分片是数据的容器，文档保存在分片内，分片又被分配到集群内的各个节点里。 当你的集群规模扩大或者缩小时， Elasticsearch 会自动的在各节点中迁移分片，使得数据仍然均匀分布在集群里。

###### 主分片（primary shard）

索引内任意一个文档都归属于一个主分片，所以主分片的数目决定着索引能够保存的最大数据量。

###### 复制分片（副分片 replica shard)

一个副本分片只是一个主分片的拷贝。 副本分片作为硬件故障时保护数据不丢失的冗余备份，并为搜索和返回文档等读操作提供服务。

**在索引建立的时候就已经确定了主分片数，但是副本分片数可以随时修改.**

初始设置索引的分片方法

```
PUT /blogs
{<!-- -->
   "settings" : {<!-- -->
      "number_of_shards" : 3,
      "number_of_replicas" : 1
   }
}

```
-  number_of_shards 每个索引的主分片数，默认值是`5`。这个配置在索引创建后不能修改。 -  number_of_replicas 每个主分片的副本数，默认值是`1`。对于活动的索引库，这个配置可以随时修改。 
2 个节点 <img src="https://img-blog.csdnimg.cn/20200113224619810.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTgwNTMzOQ==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

3 个节点 <img src="https://img-blog.csdnimg.cn/20200113224634529.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTgwNTMzOQ==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 分片是一个功能完整的搜索引擎，它拥有使用一个节点上的所有资源的能力。 我们这个拥有6个分片（3个主分片和3个副本分片）的索引可以最大扩容到6个节点，每个节点上存在一个分片，并且每个分片拥有所在节点的全部资源。

修改复制分片数目的方法

```
PUT /blogs/_settings
{<!-- -->
   "number_of_replicas" : 2
}

```

拥有越多的副本分片时，也将拥有越高的吞吐量。 <img src="https://img-blog.csdnimg.cn/20200113224719683.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTgwNTMzOQ==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

##### 故障转移 failover

<img src="https://img-blog.csdnimg.cn/20200113224735582.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTgwNTMzOQ==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">
- 选举新的主节点- 提升复制分片为主分片
##### 查看集群健康状态

```
GET /_cluster/health

{<!-- -->
   "cluster_name":          "elasticsearch",
   "status":                "green", 
   "timed_out":             false,
   "number_of_nodes":       1,
   "number_of_data_nodes":  1,
   "active_primary_shards": 0,
   "active_shards":         0,
   "relocating_shards":     0,
   "initializing_shards":   0,
   "unassigned_shards":     0
}

```

`status`字段指示着当前集群在总体上是否工作正常。它的三种颜色含义如下：
-  `green` 所有的主分片和副本分片都正常运行。 -  `yellow` 所有的主分片都正常运行，但不是所有的副本分片都正常运行。 -  `red` 有主分片没能正常运行。 