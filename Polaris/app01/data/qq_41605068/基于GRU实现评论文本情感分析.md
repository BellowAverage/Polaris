
--- 
title:  基于GRU实现评论文本情感分析 
tags: []
categories: [] 

---
## 一、问题建模  

在线评论的细粒度情感分析对于深刻理解商家和用户、挖掘用户情感等方面有至关重要的价值，并且在互联网行业有极其广泛的应用，主要用于个性化推荐、智能搜索、产品反馈、业务安全等。此博文，共包含6大类20个细粒度要素的情感倾向。根据标注的细粒度要素的情感倾向建立算法模型，对用户评论文本进行情感挖掘。

**问题建模**：

<img alt="" height="409" src="https://img-blog.csdnimg.cn/direct/b94ee73598314fdbaf0d1282e14cc09d.png" width="976">

 **解决方向**：

<img alt="" height="262" src="https://img-blog.csdnimg.cn/direct/1905e6be4b2f4608b503b21662c429a9.png" width="990">

## 二、数据集

>  
 数据下载： 


###  2.1数据集说明

数据集分为训练、验证、测试三部分。

数据集中的评价对象按照粒度不同划分为两个层次，层次一为粗粒度的评价对象，例如评论文本中涉及的服务、位置等要素；层次二为细粒度的情感对象，例如“服务”属性中的“服务人员态度”、“排队等候时间”等细粒度要素。评价对象的具体划分如下表所示：

|层次一(The first layer)|层次二(The second layer)|情感倾向值(Sentimental labels）|含义（Meaning）
|------
<td colspan="1" rowspan="3">位置(location)</td>|交通是否便利(traffic convenience)<td colspan="1" rowspan="20"> 四种状态：正向、中性、负向、未提及。使用[1,0,-1,-2]四个值对情感倾向进行描述：  </td><td colspan="1" rowspan="20"> 正面情感(Positive)为1 中性情感(Neutral)为0 负面情感（Negative）为-1 情感倾向未提及（Not mentioned）为-2 </td>



中性情感(Neutral)为0

情感倾向未提及（Not mentioned）为-2
|距离商圈远近(distance from business district)
|是否容易寻找(easy to find)
<td colspan="1" rowspan="4">服务(service)</td>|排队等候时间(wait time)
|服务人员态度(waiter’s attitude)
|是否容易停车(parking convenience)
|点菜/上菜速度(serving speed)
<td colspan="1" rowspan="3">价格(price)</td>|价格水平(price level)
|性价比(cost-effective)
|折扣力度(discount)
<td colspan="1" rowspan="4">环境(environment)</td>|装修情况(decoration)
|嘈杂情况(noise)
|就餐空间(space)
|卫生情况(cleaness)
<td colspan="1" rowspan="4">菜品(dish)</td>|分量(portion)
|口感(taste)
|外观(look)
|推荐程度(recommendation)
<td colspan="1" rowspan="2">其他(others)</td>|本次消费感受(overall experience)
|再次消费的意愿(willing to consume again)

### 2.2举例分析

>  
 某条评论如下： 
 <u>“味道不错的面馆，性价比也相当之高，分量很足～女生吃小份，胃口小的，可能吃不完呢。环境在面馆来说算是好的，至少看上去堂子很亮，也比较干净，一般苍蝇馆子还是比不上这个卫生状况的。中午饭点的时候，人很多，人行道上也是要坐满的，隔壁的冒菜馆子，据说是一家，有时候也会开放出来坐吃面的人。“</u> 
 <hr> 
 对该条评论进行6大类20个的细粒度要素的情感倾向进行预测，预测结果使用[-2,-1,0,1]四个值进行描述，返回的结果如下： 


|层次一(The first layer)|层次二(The second layer)|标注 (Label)
|------
<td colspan="1" rowspan="3">位置(location)</td>|交通是否便利(traffic convenience)|-2
|距离商圈远近(distance from business district)|-2
|是否容易寻找(easy to find)|-2
<td colspan="1" rowspan="4">服务(service)</td>|排队等候时间(wait time)|-2
|服务人员态度(waiter’s attitude)|-2
|是否容易停车(parking convenience)|-2
|点菜/上菜速度(serving speed)|-2
<td colspan="1" rowspan="3">价格(price)</td>|价格水平(price level)|-2
|性价比(cost-effective)|1
|折扣力度(discount)|-2
<td colspan="1" rowspan="4">环境(environment)</td>|装修情况(decoration)|1
|嘈杂情况(noise)|-2
|就餐空间(space)|-2
|卫生情况(cleaness)|1
<td colspan="1" rowspan="4">菜品(dish)</td>|分量(portion)|1
|口感(taste)|1
|外观(look)|-2
|推荐程度(recommendation)|-2
<td colspan="1" rowspan="2">其他(others)</td>|本次消费感受(overall experience)|1
|再次消费的意愿(willing to consume again)|-2

## 三、算法选择

### 3.1问题

（RNN，Recurrent Neural Network）受到短期记忆的影响。如果一个序列足够长，就很难将早期产生的信息带到后续的步骤中来。因此，如果试图处理一段文字来做预测，RNN可能会从一开始就遗漏了重要信息。 在反向传播过程中，循环神经网络会受到梯度消失问题的影响。梯度是用于更新神经网络权重的数值。梯度消失问题是指当梯度通过时间反向传播时，梯度会缩小。如果一个梯度值变得非常小，它就不会有太多的学习贡献。因此，在循环神经网络中，获得小梯度更新的层会停止学习。这些通常是早期的层。因此，在较长序列中，会忘记这些不学习的层，就像有一个短期记忆。

### 3.2解决办法

LSTM（Long Short-Term Memory）和GRU（Gated Recurrent Unit）的诞生是为了解决短期记忆问题。它们利用具有内部机制的门控来调节信息的流动。

### <img alt="" height="738" src="https://img-blog.csdnimg.cn/direct/9df3c4fde84c438b96af5a7ab189f49d.png" width="1200">

### 3.3举例

假设你正在看网上的评论，决定是否想买一件衣服。你首先阅读评论，然后确定是否有人认为它是好还是坏。

当你阅读评论时，你的大脑下意识地只记住了重要的关键词。你会对像“惊人” 和“完美”这样的词印象深刻。你对“这个”、“给了”、“所有”、“应该”等词不太在意。如果第二天有朋友问你评论说了什么，你可能不会一字不落地记住。但你可能会记得主要内容，如“一定会再次购买”，其他的词则会从记忆中消失了。

这基本上就是LSTM或GRU的作用。它可以学习只保留相关信息来进行预测，而忘记不相关的数据。在这种情况下，你记住的那些话让你判断它是好的。

## 四、模型建立

### 4.1流程

1. 数据预处理： 首先需要对原始数据进行预处理，包括文本清洗、分词、去除停用词等操作。预处理的目标是将文本转化为适合模型输入的形式。

2. 特征提取： 接下来，从经过预处理的文本中提取特征，用于表示文本内容。常用的特征提取方法包括词袋模型、TF-IDF、word2vec、BERT等。这些方法可以将文本转化为向量表示，能够保留词语的语义和上下文信息。然后，模型逐一处理向量序列。

3. 构建分类模型： 在特征提取完成后，需要选择合适的算法或模型来进行情感分类。常用的分类模型包括朴素贝叶斯、支持向量机（SVM）、逻辑回归、深度学习模型（如卷积神经网络、循环神经网络、Transformer等）。这些模型能够学习从特征到情感类别的映射关系。

4. 模型应用： 训练好的模型可以用于对新的未标注数据进行情感分类。对于未知的文本数据，可以使用训练好的模型预测其情感类别。

### 4.2代码实现

#### 4.2.1版本

```
torch==1.11.0
torchaudio==0.11.0
torchinfo==1.8.0
torchvision==0.12.0

- jieba==0.42.1
```

#### 4.2.2建立词典

```
def build_wordmap(contents):
    word_freq = Counter()

    for sentence in tqdm(contents):
        seg_list = jieba.cut(sentence.strip())
        # Update word frequency
        word_freq.update(list(seg_list))

    # Create word map
    words = [w for w in word_freq.keys() if word_freq[w] &gt; min_word_freq]
    word_map = {k: v + 4 for v, k in enumerate(words)}
    word_map['&lt;pad&gt;'] = 0
    word_map['&lt;start&gt;'] = 1
    word_map['&lt;end&gt;'] = 2
    word_map['&lt;unk&gt;'] = 3
    print('len(word_map): ' + str(len(word_map)))
    print(words[:10])

    with open('data/WORDMAP.json', 'w') as file:
        json.dump(word_map, file, indent=4)
```

#### 4.2.3建立模型

<img alt="" height="401" src="https://img-blog.csdnimg.cn/direct/db14029e39e34361936968a1de1b8a8d.png" width="865">

>  
 全部代码： 


参考学习：
- - 