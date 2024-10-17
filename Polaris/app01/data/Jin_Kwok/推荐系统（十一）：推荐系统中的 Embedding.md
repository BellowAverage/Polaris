
--- 
title:  推荐系统（十一）：推荐系统中的 Embedding 
tags: []
categories: [] 

---
本次讨论的问题目录有：
1. 什么是 Embedding？1. 推荐系统为什么需要 Embedding？1. 推荐系统代码中如何用数据生成 Embedding？1. 推荐系统代码中的 Embedding 技术分类有哪些？
## 1. 什么是 Embedding？

>  
 简单来看，Embedding 是一个向量 (如 [0.2,0.4] 这就是二维 Embedding）；往复杂了看，即用低维稠密的向量**“表示”**一个对象，这里所说的对象可以是一个词（Word2Vec），也可以是一个物品（Item2Vec），亦或是网络关系中的节点（Graph Embedding）。其中**“表示”**这个词意味着 Embedding 向量能够表达相应对象的**某些特征**，同时向量之间的距离反映了**对象之间的相似性。** 
  
 在推荐场景中，User 和 Item 是复杂多元的，它们分别具有各自的特征，我们很难直接评估这些特征。因此，我们需要将这些纷繁复杂的特征抽象到一个空间中来，以便【统一世界观】，在这一统一的空间中，原本纷繁复杂的特征蜕变成为相对简单的数字化向量。 
  
 基于上述理解，所谓嵌入——本质上是一种【抽象】，通过抽象，去粗存精、去伪存真，以便刻画 User 和 Item 的本质。通过抽象，我们将 User 和 Item 投射到另一个【空间】中以数学形式表达，这一【空间】是相对精简的。 


在 Embedding 成名之前，oneHot 才是最靓的仔。相较于 oneHot，直观上看，Embedding 相当于是对 oneHot 做了平滑，而 oneHot 相当于是对 Embedding 做了 max pooling。从抽象层面来看，oneHot 的抽象层次比较低，与其表征的对象直接具有较为明确的联系；相较之下，Embedding 的抽象层次非常高，与其表征的对象之间没有直接可评估的联系，但是，Embedding 的表达能力实际上比 oneHot 要强大得多。

<img alt="" height="350" src="https://img-blog.csdnimg.cn/img_convert/9da511b70133633f7beb0c2a953f459e.webp?x-oss-process=image/format,png" width="600">

<img alt="" src="//upload-images.jianshu.io/upload_images/4517635-784b6bd4af6b8046.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1156">

图 1 Embedding 和 oneHot 区别 

一般意义的 Embedding 是**神经网络倒数第二层的参数权重**，**只具有整体意义和相对意义**（很重要！很重要！很重要！），**不具备局部意义和绝对含义**（所有又叫 latent factor，隐向量，可以细看参考文献中——FM 的 DNN 实现）。这与 Embedding 的产生过程有关，任何 Embedding一开始都是一个随机数，然后随着优化算法，不断迭代更新，最后网络收敛停止迭代的时候，网络各个层的参数就相对固化，得到**隐层权重表**（此时就相当于得到了我们想要的 Embedding），然后在通过查表可以单独查看每个元素的 Embedding。

>  
 我解释一下为什么 Embedding 是**神经网络倒数第二层的参数权重**。首先，最后一层是预测层，倒数第二层与目标任务强相关，得到了 Embedding，就可以用权重来表征该样本。其次，获得 Embedding 的目的是为了方便检索，检索实际上就是求距离最近，就是叉积最小。倒数第二层之前的隐层和倒数第二层的权重相乘可以理解为检索的过程，因为也是求叉积，而且一次性求了和所有候选 Item 的叉积，所以可以拿 Embedding 直接做权重。 


从上面的解释可以获悉——直接审视 Embedding 是没有意义的，因为，其数学形式（一个向量）与其要表示的对象并非直接的映射关系。Embedding 是相应的事实对象在另一个空间的表达，既然空间不同，自然也就无法简单的用一个空间审视另一个空间。



## 2. 推荐系统为什么需要 Embedding？

>  
 在推荐系统中我们可以用Embedding作为向量，运用在推荐算法中作为近邻推推荐(Nearest Neighbor,NN)，从而实现物物推荐，人人推荐，人物推荐。 


Embedding 向量作为推荐算法中必不可少的部分，主要有四个运用方向：

### 2.1 在深度学习网络中作为 Embedding 层

完成从高维稀疏特征向量到低维稠密特征向量的转换（比如 Wide&amp;Deep、DIN 等模型）。因为推荐场景中大量使用 One-Hot 编码对类别、ID 型特征进行编码，导致样本特征向量极度稀疏，而深度学习的结构特点使其不利于稀疏特征向量的处理，因此几乎所有的深度学习推荐模型都会利用 Embedding 层将高维稀疏特征向量转换成稠密低维特征向量。因此，掌握各类 Embedding 技术是构建深度学习推荐模型的基础性操作。

### 2.2 作为预训练的 Embedding 特征向量

与其他特征向量连接后，一同输入深度学习网络进行训练（比如 FNN 模型）。 Embedding 本身就是极其重要的特征向量。**相比 MF 矩阵分解等传统方法产生的特征向量，Embedding 的表达能力更强**，特别是 Graph Embedding 技术被提出后，Embedding 几乎可以引入任何信息进行编码，使其本身就包含大量有价值的信息。在此基础上，Embedding 向量往往会与其他推荐系统特征连接后一同输入后续深度学习网络进行训练。

### 2.3 计算用户和物品的 Embedding 相似度

Embedding 可以直接作为推荐系统的召回层或者召回策略之一（比如 Youtube 推荐模型等）。 Embedding 对物品、用户相似度的计算是常用的推荐系统召回层技术。在局部敏感哈希（Locality-Sensitive Hashing）等快速最近邻搜索技术应用于推荐系统后，**Embedding 更适用于对海量备选物品进行快速“筛选”，过滤出几百到几千量级的物品交由深度学习网络进行“精排”**。

>  
 YouTube 是利用 Embedding 特征做推荐的开山之作，论文中 user_vec 是通过 DNN 学习到的，而引入 DNN 的好处则是任意的连续特征和离散特征可以很容易添加到模型当中。同样的，推荐系统常用的矩阵分解方法虽然也能得到 user_vec 和 item_vec，但同样是不能Embedding 嵌入更多 feature。 


<img alt="" height="440" src="https://img-blog.csdnimg.cn/img_convert/f24c86279ce0b39be6d5c843aa0adfe1.webp?x-oss-process=image/format,png" width="700">

图 2 Youtube 提出的基于 pooling 路线的用户行为序列建模

>  
 - 整个模型架构是包含三个隐层的 DNN 结构。输入是用户浏览历史 watch vector、搜索历史 search vector、人口统计学信息 gender，age 和其余上下文信息 concat 成的输入向量；输出分：线上和离线训练两个部分。- 类似于 word2vec 的做法，每个视频都会被 Embedding 到固定维度的向量中。用户的观看视频历史则是通过变长的视频序列表达，最终通过加权平均（可根据重要性和时间进行加权）得到固定维度的 watch vector 作为 DNN 的输入。- 离线训练阶段输出层为 softmax 层，而线上则直接利用 user 向量查询相关商品。模型进行 serving 的过程中，没有直接使用整个模型去做 inference，而是直接使用 user embedding 和 item embedding 去做相似度的计算。其中 user embedding 是模型最后一层 MLP 的输出，video embedding 则直接使用的是 softmax 的权重。 


**通过计算用户和物品的 Embedding，将其作为**实时**特征输入到推荐或者搜索模型中**（比如 Airbnb的 Embedding 应用）。值得一提的，就是以前的 Embedding 都是离线计算的，但是在 2017 年facebook 发布了 faiss 算法，就可以**流式添加 Embedding**，然后百万数据量的计算缩短在毫秒 ms级了。

>  
 2018 年 Airbnb 论文主要贡献是在稀疏样本的构造上有所创新， Airbnb 这个操作部分弥补了 YouTube 在新闻推荐领域水土不服的问题。从一个 Embedding 主义者的角度看，他的创新点主要有一下两点，一个是分群 Embedding，另一个是用户和 item 混合训练。 


<img alt="" height="412" src="https://img-blog.csdnimg.cn/img_convert/d3ac16090d5b4dd6b49d817e8aaa3711.webp?x-oss-process=image/format,png" width="700">

图 3 Embedding 发展历史



## 3. 推荐系统代码中如何用数据生成Embedding？

结合上图，罗列 3 个代码片段来说一下具体 Embedding 是怎么计算的？这 3 个场景分别为：**word2vec、系统过滤和 DNN**。

### 3.1 基于内容的 word2vec

先看红色方框有3句话是做为输入。然后 word2vec 就算了每个词的 Embedding。然后右边，我们可以把文档换成用户，词语换成电影，那么得到电影的推荐了。

<img alt="" height="315" src="https://img-blog.csdnimg.cn/img_convert/9a9e44815858bc4ebb71fa11c7074b49.webp?x-oss-process=image/format,png" width="700">

图 4 word2vec

###### 

### 3.2 协同过滤矩阵的分解方法

其实指定输入的 “用户 id”、“电影 id”、“评分”，然后采用 ALS 算法（Alternating Least Squares，全称为交替最小二乘法，是一种基于协同过滤思想的矩阵分解算法）fit，就的得到了每个 item（表中的 id）的 Embedding 向量（表中的 features），进而可以物物推荐，人人推荐，人物推荐。

<img alt="" height="359" src="https://img-blog.csdnimg.cn/img_convert/8d6732bf7569a8a49a8150c5ecbf8c8f.webp?x-oss-process=image/format,png" width="700">

图 5 协同过滤



### 3.3 DNN 深度学习的方法

其实上面特别说了一下，这里在细节说一下。Embedding 其实是 DNN 的副产品。什么意思呢？下面左边这个图，红色箭头指的 Relu，其实包含了 256 个向量，其实这个 256 向量就是Embedding，这个 Embedding 就是权重。然后最左边得到 video 的向量，配合着 Nearest Neighbor 就能把通过 Embedding 权重计算的结果一起送去 softmax 最后输出预测 top N。**是不是感觉似曾相识？其实 transformer 也是类似，利用 QW 的计算权重赋给 V，然后送给softmax，唯一区别在于这里用 DNN，而 transformer 用的是多头 attention。**

<img alt="" height="299" src="https://img-blog.csdnimg.cn/img_convert/73e3b26735bd45ec437e6398434b83e3.webp?x-oss-process=image/format,png" width="700">

图 6 dnn 的 Embedding



## 4. 推荐系统代码中的 Embedding 技术分类有哪些？

### 4.1 特征 Embedding 化

在特征工程中，对于离散值，连续值，多值大致有以下几种 Embedding 的方法。预先训练的 Embedding 特征向量，训练样本大，参数学习更充分。end2end 是通过 Embedding 层完成从高维稀疏向量到低维稠密特征向量的转换，优点是端到端，梯度统一，缺点是参数多，收敛速度慢，如果数据量少，参数很难充分训练。

<img alt="" height="349" src="https://img-blog.csdnimg.cn/img_convert/a0aecac469372d7ea8db1e5f03cb905d.webp?x-oss-process=image/format,png" width="700">

 图 7 特征 Embedding



### 4.2 Embedding 运算

不同的深度学习模型中，除了对网络结构的各种优化外，在 Embedding 的运算上也进行了各种优化的尝试，对网络结构的各种优化本质上也是对 Embedding 的运算的优化。

<img alt="" height="388" src="https://img-blog.csdnimg.cn/img_convert/8546a44b693468413a8f2afe99cceb16.webp?x-oss-process=image/format,png" width="700">

图 8 Embedding 运算

### 4.3 Embedding 缺陷

Embedding 作为一种技术，虽然很流行，但是他也存在一些缺陷，比如增量更新的语义不变性，很难同时包含多个特征，长尾数据难以训练等。

<img alt="" height="374" src="https://img-blog.csdnimg.cn/img_convert/3f0ca29defad23e8756576015ecb5570.webp?x-oss-process=image/format,png" width="700">

 图 9 Embedding缺陷

>  
 2020 的 KDD 会议中，华为的一篇 **AutoFIS 文章谈到了对 Embedding 持续优化，可以得到合适的特征向量化表达，同时得到内积“更合适”的值来表示组合特征的重要性**。 
  
 其原理是在 &lt;Vi, Vj&gt; 前面增加了一个参数。我们可能会问再引入一个参数不是多此一举？我反而觉得这才是 AutoFIS 精华。Embedding 的作用是将特征用向量化表示，并且保证相似特征的距离更近。基于此，相似特征内积就更大。而“相似”和“重要”是两码事，很“相似”的特征不一定能对预测起到更“重要”的作用。但是 DeepFM 在训练的过程中并没有将这两部分解耦，可能造成的结果就是 Embedding 的向量化表达不一定能让相似的特征距离更近，同时重要的特征内积也不一定大。 


<img alt="" height="362" src="https://img-blog.csdnimg.cn/img_convert/c9a7ebeebdf86485e1752fa18d331617.webp?x-oss-process=image/format,png" width="700">

图 10 总结

### 5.参考文献



6-
