
--- 
title:  DL之Transformer：《The Annotated Transformer带注释的变压器》的翻译与解读—思路步骤及实现代码 
tags: []
categories: [] 

---
DL之Transformer：《The Annotated Transformer带注释的变压器》的翻译与解读—思路步骤及实现代码

>  
 **<strong>导读**</strong>：该文章主要阐述了Transformer神经机器翻译模型的具体实现细节。主要核心要点： 
 &gt;&gt; 模型整体架构：Transformer模型采用Encoder-Decoder框架，Encoder负责编码输入序列，Decoder负责解码Encoder输出生成目标序列。 
 &gt;&gt; 注意力机制：Transformer模型使用多头注意力机制来建立输入与输入，Decoder与Encoder之间以及Decoder自身序列元素之间的关系。 
 &gt;&gt; 模型细节设计：Encoder和Decoder均由多层结构组成，每层包含多头自注意力模块和前馈网络模块。同时采用残差连接和层归一化策略。 
 &gt;&gt; 位置编码：为弥补Transformer没有递归结构的不足，加入位置编码方式将位置信息注入模型。 
 &gt;&gt; 实验结果：在WMT2014英德翻译任务上，大模型达到28.4BLEU，在当时状态免费效果。同时在英法翻译上也优于目前最佳单模型。 
 &gt;&gt; 模型训练细节：文章详细说明了数据预处理，批处理，多GPU训练，学习率计划，正则化方法等训练细节。 
 &gt;&gt; 注意力可视化：文章通过可视化展示了模型不同层次多头注意力模块的注意力分布，说明其学到的语义依赖关系。 






**目录**































































































## **《The Annotated Transformer》的翻译与解读**
<td style="vertical-align:top;width:32.25pt;"> **<strong>地址**</strong> </td><td style="vertical-align:top;width:393.85pt;"> GitHub地址： 文章地址： </td>

GitHub地址：
<td style="vertical-align:top;width:32.25pt;"> **<strong>时间**</strong> </td><td style="vertical-align:top;width:393.85pt;"> v2022 </td>

v2022
<td style="vertical-align:top;width:32.25pt;"> **<strong>作者**</strong> </td><td style="vertical-align:top;width:393.85pt;"> Austin Huang, Suraj Subramanian, Jonathan Sum, Khalid Almubarak, and Stella Biderman. </td>

Austin Huang, Suraj Subramanian, Jonathan Sum, Khalid Almubarak, and Stella Biderman.





## **导言**

Transformer在过去的五年中一直备受人们关注。本文以逐行实现的方式呈现了论文的注释版本。我们重新排列和删除了原始论文中的一些部分，并在整个过程中添加了注释。本文档本身是一个工作笔记，并且应该是一个完全可用的实现。代码可以在这里找到。

我的评论被大量引用。正文全部来自论文本身。

```
# # Uncomment for colab
# #
# !pip install -q torchdata==0.3.0 torchtext==0.12 spacy==3.2 altair GPUtil
# !python -m spacy download de_core_news_sm
# !python -m spacy download en_core_web_sm
```



#### 代码：深度学习脚本的框架

这段代码是一个深度学习脚本的框架，包含了数据处理、模型训练和测试的基本结构，同时也为分布式训练和GPU监控提供了支持。

```
import os
from os.path import exists
import torch
import torch.nn as nn
from torch.nn.functional import log_softmax, pad
import math
import copy
import time
from torch.optim.lr_scheduler import LambdaLR
import pandas as pd
import altair as alt
from torchtext.data.functional import to_map_style_dataset
from torch.utils.data import DataLoader
from torchtext.vocab import build_vocab_from_iterator
import torchtext.datasets as datasets
import spacy
import GPUtil
import warnings
from torch.utils.data.distributed import DistributedSampler
import torch.distributed as dist
import torch.multiprocessing as mp
from torch.nn.parallel import DistributedDataParallel as DDP


# Set to False to skip notebook execution (e.g. for debugging)
warnings.filterwarnings("ignore")
RUN_EXAMPLES = True


# Some convenience helper functions used throughout the notebook


def is_interactive_notebook():
    return __name__ == "__main__"


def show_example(fn, args=[]):
    if __name__ == "__main__" and RUN_EXAMPLES:
        return fn(*args)


def execute_example(fn, args=[]):
    if __name__ == "__main__" and RUN_EXAMPLES:
        fn(*args)


class DummyOptimizer(torch.optim.Optimizer):
    def __init__(self):
        self.param_groups = [{"lr": 0}]
        None

    def step(self):
        None

    def zero_grad(self, set_to_none=False):
        None


class DummyScheduler:
    def step(self):
        None
```







## **背景**

减少顺序计算的目标也构成了Extended Neural GPU、ByteNet和ConvS2S的基础，它们都使用卷积神经网络作为基本构建块，在所有输入和输出位置并行计算隐藏表示。在这些模型中，将两个任意输入或输出位置的信号相关联所需的操作数量随着位置之间的距离增加而增长，对于ConvS2S是线性增长，对于ByteNet是对数增长。这使得学习远距离位置之间的依赖关系变得更加困难。在Transformer中，这被减少到一个恒定的操作数量，尽管其代价是由于平均注意加权位置而降低了有效分辨率，我们通过使用多头注意抵消了这一影响。

自注意力，有时被称为内部注意力，是一种注意机制，用于关联序列中不同位置以计算该序列的表示。自注意力已经成功地应用于各种任务，包括阅读理解、抽象总结、文本蕴涵和学习任务无关的句子表示。端到端记忆网络基于循环注意机制，而不是顺序排列的递归，而不是序列对齐的循环，并且已经显示出在简单语言问答和语言建模任务上表现良好。

据我们所知，然而，据我们所知，Transformer是第一个完全依赖于自关注来计算其输入和输出表示的转导模型，而不使用序列对齐RNN或卷积。



## **第1部分:模型体系结构**

### **<strong><strong>模型架构**</strong></strong>

大多数竞争性的神经序列转换模型都具有编码器-解码器结构（引用）。在这里，编码器将输入序列的符号表示(x1,...,xn)映射到连续表示序列z=(z1,...,zn)。给定 z，解码器然后生成一个输出序列(y1,...,ym)中的符号，每次生成下一个符号时，模型都是自回归的（引用），使用先前生成的符号作为附加输入。

#### 代码：

```
class EncoderDecoder(nn.Module):
    """
    A standard Encoder-Decoder architecture. Base for this and many
    other models.
    """

    def __init__(self, encoder, decoder, src_embed, tgt_embed, generator):
        super(EncoderDecoder, self).__init__()
        self.encoder = encoder
        self.decoder = decoder
        self.src_embed = src_embed
        self.tgt_embed = tgt_embed
        self.generator = generator

    def forward(self, src, tgt, src_mask, tgt_mask):
        "Take in and process masked src and target sequences."
        return self.decode(self.encode(src, src_mask), src_mask, tgt, tgt_mask)

    def encode(self, src, src_mask):
        return self.encoder(self.src_embed(src), src_mask)

    def decode(self, memory, src_mask, tgt, tgt_mask):
        return self.decoder(self.tgt_embed(tgt), memory, src_mask, tgt_mask)
```



#### 代码：

```
class Generator(nn.Module):
    "Define standard linear + softmax generation step."

    def __init__(self, d_model, vocab):
        super(Generator, self).__init__()
        self.proj = nn.Linear(d_model, vocab)

    def forward(self, x):
        return log_softmax(self.proj(x), dim=-1)
```

Transformer遵循这种整体架构，使用堆叠的自注意力和点式的全连接层作为编码器和解码器，分别显示在图1的左半部分和右半部分。

<img alt="" height="560" src="https://img-blog.csdnimg.cn/direct/d844785e94ae4ce38f19697683d186cf.png" width="380">







### **<strong><strong>编码器和解码器堆栈**</strong></strong>

#### **<strong><strong>编码器**</strong></strong>

编码器由一堆N=6 个相同层的堆栈组成。

```
def clones(module, N):
    "Produce N identical layers."
    return nn.ModuleList([copy.deepcopy(module) for _ in range(N)])


class Encoder(nn.Module):
    "Core encoder is a stack of N layers"

    def __init__(self, layer, N):
        super(Encoder, self).__init__()
        self.layers = clones(layer, N)
        self.norm = LayerNorm(layer.size)

    def forward(self, x, mask):
        "Pass the input (and mask) through each layer in turn."
        for layer in self.layers:
            x = layer(x, mask)
        return self.norm(x)
```



我们在每个子层周围采用了一个残差连接（引用），然后是层归一化（引用）。

```
class LayerNorm(nn.Module):
    "Construct a layernorm module (See citation for details)."

    def __init__(self, features, eps=1e-6):
        super(LayerNorm, self).__init__()
        self.a_2 = nn.Parameter(torch.ones(features))
        self.b_2 = nn.Parameter(torch.zeros(features))
        self.eps = eps

    def forward(self, x):
        mean = x.mean(-1, keepdim=True)
        std = x.std(-1, keepdim=True)
        return self.a_2 * (x - mean) / (std + self.eps) + self.b_2
```



也就是说，每个子层的输出是LayerNorm(x+Sublayer(x))，其中Sublayer(x)是子层本身实现的函数。我们对每个子层的输出应用dropout（引用），然后将其添加到子层输入并进行归一化。

为了促进这些残差连接，模型中的所有子层以及嵌入层都会产生维度为 dmodel=512的输出。

```
class SublayerConnection(nn.Module):
    """
    A residual connection followed by a layer norm.
    Note for code simplicity the norm is first as opposed to last.
    """

    def __init__(self, size, dropout):
        super(SublayerConnection, self).__init__()
        self.norm = LayerNorm(size)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, sublayer):
        "Apply residual connection to any sublayer with the same size."
        return x + self.dropout(sublayer(self.norm(x)))
```



每一层有两个子层。第一个是多头自注意力机制，第二个是简单的位置逐点全连接前馈网络。

```
class EncoderLayer(nn.Module):
    "Encoder is made up of self-attn and feed forward (defined below)"

    def __init__(self, size, self_attn, feed_forward, dropout):
        super(EncoderLayer, self).__init__()
        self.self_attn = self_attn
        self.feed_forward = feed_forward
        self.sublayer = clones(SublayerConnection(size, dropout), 2)
        self.size = size

    def forward(self, x, mask):
        "Follow Figure 1 (left) for connections."
        x = self.sublayer[0](x, lambda x: self.self_attn(x, x, x, mask))
        return self.sublayer[1](x, self.feed_forward)
```



#### **<strong><strong>解码器**</strong></strong>

解码器也由一堆N=6 个相同的层组成。

```
class Decoder(nn.Module):
    "Generic N layer decoder with masking."

    def __init__(self, layer, N):
        super(Decoder, self).__init__()
        self.layers = clones(layer, N)
        self.norm = LayerNorm(layer.size)

    def forward(self, x, memory, src_mask, tgt_mask):
        for layer in self.layers:
            x = layer(x, memory, src_mask, tgt_mask)
        return self.norm(x)
```



除了每个编码器层中的两个子层外，解码器还插入第三个子层，该子层对编码器堆栈的输出执行多头注意力。与编码器类似，我们在每个子层周围采用了残差连接，然后是层归一化。

```
class DecoderLayer(nn.Module):
    "Decoder is made of self-attn, src-attn, and feed forward (defined below)"

    def __init__(self, size, self_attn, src_attn, feed_forward, dropout):
        super(DecoderLayer, self).__init__()
        self.size = size
        self.self_attn = self_attn
        self.src_attn = src_attn
        self.feed_forward = feed_forward
        self.sublayer = clones(SublayerConnection(size, dropout), 3)

    def forward(self, x, memory, src_mask, tgt_mask):
        "Follow Figure 1 (right) for connections."
        m = memory
        x = self.sublayer[0](x, lambda x: self.self_attn(x, x, x, tgt_mask))
        x = self.sublayer[1](x, lambda x: self.src_attn(x, m, m, src_mask))
        return self.sublayer[2](x, self.feed_forward)
```

我们还修改了解码器堆栈中的自注意力子层，以防止位置关注或关联后续位置。这种掩蔽，再加上输出嵌入被偏移一个位置的事实，确保了位置i的预测只能依赖于位置小于i的已知输出。

```
def subsequent_mask(size):
    "Mask out subsequent positions."
    attn_shape = (1, size, size)
    subsequent_mask = torch.triu(torch.ones(attn_shape), diagonal=1).type(
        torch.uint8
    )
    return subsequent_mask == 0
```



下面的注意力掩码显示了每个目标词（行）被允许查看的位置（列）。在训练期间，对未来词的注意被阻止。

```
def example_mask():
    LS_data = pd.concat(
        [
            pd.DataFrame(
                {
                    "Subsequent Mask": subsequent_mask(20)[0][x, y].flatten(),
                    "Window": y,
                    "Masking": x,
                }
            )
            for y in range(20)
            for x in range(20)
        ]
    )

    return (
        alt.Chart(LS_data)
        .mark_rect()
        .properties(height=250, width=250)
        .encode(
            alt.X("Window:O"),
            alt.Y("Masking:O"),
            alt.Color("Subsequent Mask:Q", scale=alt.Scale(scheme="viridis")),
        )
        .interactive()
    )


show_example(example_mask)
```

<img alt="" height="301" src="https://img-blog.csdnimg.cn/direct/2558065bf25d46d9baf832c4720f52bc.png" width="421">



#### **<strong><strong>注意力**</strong></strong>

一个注意力函数可以描述为将查询和一组键-值对映射到输出的过程，其中查询、键、值和输出都是向量。输出是通过值的加权和计算得到的，其中分配给每个值的权重由查询与相应键的兼容性函数计算得到。我们将我们特定的注意力称为“**<strong>缩放的点积注意力**</strong>”。输入由维度为 dk的查询和键组成，以及维度为 dv的值。我们计算查询与所有键的点积，将每个除以 dk，并应用 softmax 函数以获得值的权重。

<img alt="" height="221" src="https://img-blog.csdnimg.cn/direct/dfaab85ab723439e9649df00a70dcaf8.png" width="112">

在实践中，我们同时在一组查询上计算注意力函数，将它们打包成一个矩阵 Q。键和值也打包成矩阵 K和 V。我们计算输出矩阵如下：

<img alt="" height="55" src="https://img-blog.csdnimg.cn/direct/da5cd3d1bae244db88018e6cd768e5fd.png" width="292">

```
def attention(query, key, value, mask=None, dropout=None):
    "Compute 'Scaled Dot Product Attention'"
    d_k = query.size(-1)
    scores = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(d_k)
    if mask is not None:
        scores = scores.masked_fill(mask == 0, -1e9)
    p_attn = scores.softmax(dim=-1)
    if dropout is not None:
        p_attn = dropout(p_attn)
    return torch.matmul(p_attn, value), p_attn
```

两个最常用的注意力函数是加性注意力(引用)和点积注意力(乘法)。点积注意力与我们的算法相同，除了比例因子为1dk。加性注意使用一个具有单个隐藏层的前馈网络来计算兼容性函数。虽然两者在理论复杂性上相似，但在实践中，点积注意力更快，更节省空间，因为它可以使用高度优化的矩阵乘法代码来实现。

虽然对于较小的dk值，这两种机制的表现相似，但在不缩放较大dk值的情况下，加性注意力优于点积注意力(引用)。我们怀疑，对于较大的dk值，点积的大小会变大，将softmax函数推到具有极小梯度的区域(为了说明点积变大的原因，假设q和k的分量是独立的随机变量，平均值为0，方差为1。它们的点积为∑i=1dk qi ki，均值为0，方差为dk)。为了抵消这种影响，我们将点积乘以1dk。

<img alt="" height="353" src="https://img-blog.csdnimg.cn/direct/b640df8f1b4f462a959b9126fd7d5425.png" width="230">



##### **<strong><strong>多头注意力**</strong></strong>

多头注意允许模型在不同位置同时关注来自不同表示子空间的信息。对于单一注意力头，平均会抑制这一点。

<img alt="" height="63" src="https://img-blog.csdnimg.cn/direct/ef7ce6c3ce8d4eeeb01a8da78ce3d73b.png" width="438">

其中投影为参数矩阵

在这项工作中，我们使用了&lt;s:1&gt; =8h=8个并行注意力层或头。对于每一个我们使用= model/ &lt;s:1&gt; =64dk =dv =dmodel /h=64。由于每个头的维度减小，总计算成本与具有完整维度的单头注意力类似。

```
class MultiHeadedAttention(nn.Module):
    def __init__(self, h, d_model, dropout=0.1):
        "Take in model size and number of heads."
        super(MultiHeadedAttention, self).__init__()
        assert d_model % h == 0
        # We assume d_v always equals d_k
        self.d_k = d_model // h
        self.h = h
        self.linears = clones(nn.Linear(d_model, d_model), 4)
        self.attn = None
        self.dropout = nn.Dropout(p=dropout)

    def forward(self, query, key, value, mask=None):
        "Implements Figure 2"
        if mask is not None:
            # Same mask applied to all h heads.
            mask = mask.unsqueeze(1)
        nbatches = query.size(0)

        # 1) Do all the linear projections in batch from d_model =&gt; h x d_k
        query, key, value = [
            lin(x).view(nbatches, -1, self.h, self.d_k).transpose(1, 2)
            for lin, x in zip(self.linears, (query, key, value))
        ]

        # 2) Apply attention on all the projected vectors in batch.
        x, self.attn = attention(
            query, key, value, mask=mask, dropout=self.dropout
        )

        # 3) "Concat" using a view and apply a final linear.
        x = (
            x.transpose(1, 2)
            .contiguous()
            .view(nbatches, -1, self.h * self.d_k)
        )
        del query
        del key
        del value
        return self.linears[-1](x)
```



##### **<strong><strong>多头注意在我们模型中的应用**</strong></strong>

Transformer 在三个不同的方式中使用多头注意力：

1. 在“编码器-解码器注意力”层中，查询来自前一个解码器层，而记忆键和值来自编码器的输出。这允许解码器中的每个位置都能关注输入序列中的所有位置。这模拟了序列到序列模型中典型的编码器-解码器注意力机制。

2. 编码器包含自注意力层。在自注意力层中，所有的键、值和查询都来自同一个地方，即编码器中前一层的输出。编码器中的每个位置都可以关注编码器前一层中的所有位置。

3. 类似地，解码器中的自注意力层允许解码器中的每个位置关注包括该位置在内的解码器中的所有位置。我们需要防止解码器中的左向信息流以保持自回归属性。我们通过在缩放的点积注意力中屏蔽（设置为 −∞）softmax 输入中对应于非法连接的所有值来实现这一点。



### **<strong><strong>位置前馈网络**</strong></strong>

除了注意子层之外，编码器和解码器中的每一层都包含一个完全连接的前馈网络，该网络分别相同地应用于每个位置。这包括两个线性转换，中间有一个ReLU激活。

<img alt="" height="34" src="https://img-blog.csdnimg.cn/direct/0de88e6394fb476cb23a9cc944874b3b.png" width="311">

虽然线性变换在不同位置上是相同的，但它们在每一层之间使用不同的参数。另一种描述它的方式是2个核大小为1的卷积。输入输出的维数为dmodel =512，内层的维数为dff =2048。

```
class PositionwiseFeedForward(nn.Module):
    "Implements FFN equation."

    def __init__(self, d_model, d_ff, dropout=0.1):
        super(PositionwiseFeedForward, self).__init__()
        self.w_1 = nn.Linear(d_model, d_ff)
        self.w_2 = nn.Linear(d_ff, d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        return self.w_2(self.dropout(self.w_1(x).relu()))
```



### **<strong><strong>嵌入和Softmax**</strong></strong>

与其他序列转换模型类似，我们使用学习嵌入将输入令牌和输出令牌转换为维度dmodel的向量。我们还使用常规的学习的线性变换和softmax函数将解码器输出转换为预测的下一个令牌概率。在我们的模型中，我们在两个嵌入层和pre-softmax线性变换之间共享相同的权重矩阵，类似于(引用)。在嵌入层中，我们将这些权重乘以dmodel。

```
class Embeddings(nn.Module):
    def __init__(self, d_model, vocab):
        super(Embeddings, self).__init__()
        self.lut = nn.Embedding(vocab, d_model)
        self.d_model = d_model

    def forward(self, x):
        return self.lut(x) * math.sqrt(self.d_model)
```



### **<strong><strong>位置编码**</strong></strong>

由于我们的模型不包含循环和卷积，为了使模型利用序列的顺序，我们必须注入一些关于序列中标记的相对或绝对位置的信息。为此，我们在编码器和解码器堆栈底部的输入嵌入中添加了“位置编码”。位置编码与嵌入具有相同的维数模型，因此可以对两者进行求和。位置编码有很多选择，学习的和固定的(引用)。

在这项工作中，我们使用了不同频率的正弦和余弦函数:

<img alt="" height="80" src="https://img-blog.csdnimg.cn/direct/c075686c93b844b48d3fd0b1cf1a28d6.png" width="325">

其中pos为位置，i为维度。也就是说，位置编码的每一个维度对应于一个正弦波。波长形成从 2π到2 10000⋅2π的几何级数，或形成等比级数。我们选择这个函数是因为我们假设它可以让模型很容易地通过相对位置学习，因为对于任何固定的偏移量k， + PEpos+k可以表示为PEpos的线性函数。

此外，我们将dropout应用于编码器和解码器堆栈中的嵌入和位置编码之和。对于基本模型，我们使用=0.1的速率。

```
class PositionalEncoding(nn.Module):
    "Implement the PE function."

    def __init__(self, d_model, dropout, max_len=5000):
        super(PositionalEncoding, self).__init__()
        self.dropout = nn.Dropout(p=dropout)

        # Compute the positional encodings once in log space.
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len).unsqueeze(1)
        div_term = torch.exp(
            torch.arange(0, d_model, 2) * -(math.log(10000.0) / d_model)
        )
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0)
        self.register_buffer("pe", pe)

    def forward(self, x):
        x = x + self.pe[:, : x.size(1)].requires_grad_(False)
        return self.dropout(x)
```

下面的位置编码将根据位置添加正弦波。波的频率和偏移量在每个维度上都是不同的。

```
def example_positional():
    pe = PositionalEncoding(20, 0)
    y = pe.forward(torch.zeros(1, 100, 20))

    data = pd.concat(
        [
            pd.DataFrame(
                {
                    "embedding": y[0, :, dim],
                    "dimension": dim,
                    "position": list(range(100)),
                }
            )
            for dim in [4, 5, 6, 7]
        ]
    )

    return (
        alt.Chart(data)
        .mark_line()
        .properties(width=800)
        .encode(x="position", y="embedding", color="dimension:N")
        .interactive()
    )


show_example(example_positional)
```



我们还尝试使用学习位置嵌入(引用)，并发现这两个版本产生了几乎相同的结果。我们选择正弦版本是因为它可以允许模型外推到比训练期间遇到的序列长度更长的序列。

<img alt="" height="433" src="https://img-blog.csdnimg.cn/direct/3a805ccf15f24f9b9d8184d3224dd842.png" width="1162">



### **<strong><strong>完整的模型**</strong></strong>

这里我们定义了一个从超参数到全模型的函数。

```
def make_model(
    src_vocab, tgt_vocab, N=6, d_model=512, d_ff=2048, h=8, dropout=0.1
):
    "Helper: Construct a model from hyperparameters."
    c = copy.deepcopy
    attn = MultiHeadedAttention(h, d_model)
    ff = PositionwiseFeedForward(d_model, d_ff, dropout)
    position = PositionalEncoding(d_model, dropout)
    model = EncoderDecoder(
        Encoder(EncoderLayer(d_model, c(attn), c(ff), dropout), N),
        Decoder(DecoderLayer(d_model, c(attn), c(attn), c(ff), dropout), N),
        nn.Sequential(Embeddings(d_model, src_vocab), c(position)),
        nn.Sequential(Embeddings(d_model, tgt_vocab), c(position)),
        Generator(d_model, tgt_vocab),
    )

    # This was important from their code.
    # Initialize parameters with Glorot / fan_avg.
    for p in model.parameters():
        if p.dim() &gt; 1:
            nn.init.xavier_uniform_(p)
    return model
```





### **<strong><strong>推理**</strong></strong>

在这里，我们进行一次向前步骤来生成模型的预测。我们试着用Transformer来记忆输入。正如您将看到的，由于模型尚未训练，因此输出是随机生成的。在下一篇教程中，我们将构建训练函数并尝试训练我们的模型来记忆从1到10的数字。

```
def inference_test():
    test_model = make_model(11, 11, 2)
    test_model.eval()
    src = torch.LongTensor([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
    src_mask = torch.ones(1, 1, 10)

    memory = test_model.encode(src, src_mask)
    ys = torch.zeros(1, 1).type_as(src)

    for i in range(9):
        out = test_model.decode(
            memory, src_mask, ys, subsequent_mask(ys.size(1)).type_as(src.data)
        )
        prob = test_model.generator(out[:, -1])
        _, next_word = torch.max(prob, dim=1)
        next_word = next_word.data[0]
        ys = torch.cat(
            [ys, torch.empty(1, 1).type_as(src.data).fill_(next_word)], dim=1
        )

    print("Example Untrained Model Prediction:", ys)


def run_tests():
    for _ in range(10):
        inference_test()


show_example(run_tests)
```

```
Example Untrained Model Prediction: tensor([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
Example Untrained Model Prediction: tensor([[0, 3, 4, 4, 4, 4, 4, 4, 4, 4]])
Example Untrained Model Prediction: tensor([[ 0, 10, 10, 10,  3,  2,  5,  7,  9,  6]])
Example Untrained Model Prediction: tensor([[ 0,  4,  3,  6, 10, 10,  2,  6,  2,  2]])
Example Untrained Model Prediction: tensor([[ 0,  9,  0,  1,  5, 10,  1,  5, 10,  6]])
Example Untrained Model Prediction: tensor([[ 0,  1,  5,  1, 10,  1, 10, 10, 10, 10]])
Example Untrained Model Prediction: tensor([[ 0,  1, 10,  9,  9,  9,  9,  9,  1,  5]])
Example Untrained Model Prediction: tensor([[ 0,  3,  1,  5, 10, 10, 10, 10, 10, 10]])
Example Untrained Model Prediction: tensor([[ 0,  3,  5, 10,  5, 10,  4,  2,  4,  2]])
Example Untrained Model Prediction: tensor([[0, 5, 6, 2, 5, 6, 2, 6, 2, 2]])
```







## **第2部分****：****模型训练**

### **<strong><strong>训练**</strong></strong>

本节描述了我们模型的训练过程。

我们停下来休息一下，介绍一些训练标准编码器和解码器模型所需的工具。首先，我们定义一个批处理对象，其中包含用于训练的源语句和目标语句，以及构建掩码。



#### **<strong><strong>批**</strong>**<strong>处理**</strong>**<strong>和掩码**</strong></strong>

接下来，我们创建一个通用的训练和评分函数来跟踪损失。我们传递一个通用的损失计算函数，该函数也处理参数更新。

```
class Batch:
    """Object for holding a batch of data with mask during training."""

    def __init__(self, src, tgt=None, pad=2):  # 2 = &lt;blank&gt;
        self.src = src
        self.src_mask = (src != pad).unsqueeze(-2)
        if tgt is not None:
            self.tgt = tgt[:, :-1]
            self.tgt_y = tgt[:, 1:]
            self.tgt_mask = self.make_std_mask(self.tgt, pad)
            self.ntokens = (self.tgt_y != pad).data.sum()

    @staticmethod
    def make_std_mask(tgt, pad):
        "Create a mask to hide padding and future words."
        tgt_mask = (tgt != pad).unsqueeze(-2)
        tgt_mask = tgt_mask &amp; subsequent_mask(tgt.size(-1)).type_as(
            tgt_mask.data
        )
        return tgt_mask
```



#### **<strong><strong>循环训练**</strong></strong>

```
class TrainState:
    """Track number of steps, examples, and tokens processed"""

    step: int = 0  # Steps in the current epoch
    accum_step: int = 0  # Number of gradient accumulation steps
    samples: int = 0  # total # of examples used
    tokens: int = 0  # total # of tokens processed
```



```
def run_epoch(
    data_iter,
    model,
    loss_compute,
    optimizer,
    scheduler,
    mode="train",
    accum_iter=1,
    train_state=TrainState(),
):
    """Train a single epoch"""
    start = time.time()
    total_tokens = 0
    total_loss = 0
    tokens = 0
    n_accum = 0
    for i, batch in enumerate(data_iter):
        out = model.forward(
            batch.src, batch.tgt, batch.src_mask, batch.tgt_mask
        )
        loss, loss_node = loss_compute(out, batch.tgt_y, batch.ntokens)
        # loss_node = loss_node / accum_iter
        if mode == "train" or mode == "train+log":
            loss_node.backward()
            train_state.step += 1
            train_state.samples += batch.src.shape[0]
            train_state.tokens += batch.ntokens
            if i % accum_iter == 0:
                optimizer.step()
                optimizer.zero_grad(set_to_none=True)
                n_accum += 1
                train_state.accum_step += 1
            scheduler.step()

        total_loss += loss
        total_tokens += batch.ntokens
        tokens += batch.ntokens
        if i % 40 == 1 and (mode == "train" or mode == "train+log"):
            lr = optimizer.param_groups[0]["lr"]
            elapsed = time.time() - start
            print(
                (
                    "Epoch Step: %6d | Accumulation Step: %3d | Loss: %6.2f "
                    + "| Tokens / Sec: %7.1f | Learning Rate: %6.1e"
                )
                % (i, n_accum, loss / batch.ntokens, tokens / elapsed, lr)
            )
            start = time.time()
            tokens = 0
        del loss
        del loss_node
    return total_loss / total_tokens, train_state
```





#### **<strong><strong>训练数据和批处理**</strong></strong>

我们在标准的WMT 2014英德数据集上进行了训练，该数据集包含大约450万个句子对。句子使用字节对编码进行编码，该编码有一个大约37000个标记的共享源-目标词汇。对于**<strong>英法翻译**</strong>，我们使用了大得多的WMT 2014英法数据集，包含3600万个句子，并将标记分割成32000个词片段词汇。

句子对按照近似序列长度进行批处理。每个训练批次包含一组句子对，其中大约包含25000个源标记和25000个目标标记。

### **<strong><strong>硬件和时间表**</strong></strong>

我们在一台配备8个NVIDIA P100 GPU的机器上训练我们的模型。对于使用本文档中描述的超参数的基本模型，每个训练步骤大约需要0.4秒。我们训练基本模型总共10万个步骤或12小时。对于我们的大型模型，步骤时间为1.0秒。大型模型训练了30万步（3.5天）。



#### **<strong><strong>优化器**</strong></strong>

我们使用Adam优化器(引用),1 = 0.9β1 = 0.9,2 = 0.98β2 = 0.98,= 10−9ϵ= 10−9。在训练过程中，我们根据以下公式在训练过程中改变学习率:

这对应于在前_warmup_steps训练步骤中线性增加学习率，然后按步数的平方根的倒数成比例地降低学习率。我们使用_ =4000warmup_steps=4000。

<img alt="" height="296" src="https://img-blog.csdnimg.cn/direct/58cc0a5371ba4be19edf84e06eeba99d.png" width="999">

注意：这部分非常重要。需要用这个模型的设置进行训练。

该模型在不同模型尺寸和优化超参数下的曲线示例。

```
def rate(step, model_size, factor, warmup):
    """
    we have to default the step to 1 for LambdaLR function
    to avoid zero raising to negative power.
    """
    if step == 0:
        step = 1
    return factor * (
        model_size ** (-0.5) * min(step ** (-0.5), step * warmup ** (-1.5))
    )
```



```
def example_learning_schedule():
    opts = [
        [512, 1, 4000],  # example 1
        [512, 1, 8000],  # example 2
        [256, 1, 4000],  # example 3
    ]

    dummy_model = torch.nn.Linear(1, 1)
    learning_rates = []

    # we have 3 examples in opts list.
    for idx, example in enumerate(opts):
        # run 20000 epoch for each example
        optimizer = torch.optim.Adam(
            dummy_model.parameters(), lr=1, betas=(0.9, 0.98), eps=1e-9
        )
        lr_scheduler = LambdaLR(
            optimizer=optimizer, lr_lambda=lambda step: rate(step, *example)
        )
        tmp = []
        # take 20K dummy training steps, save the learning rate at each step
        for step in range(20000):
            tmp.append(optimizer.param_groups[0]["lr"])
            optimizer.step()
            lr_scheduler.step()
        learning_rates.append(tmp)

    learning_rates = torch.tensor(learning_rates)

    # Enable altair to handle more than 5000 rows
    alt.data_transformers.disable_max_rows()

    opts_data = pd.concat(
        [
            pd.DataFrame(
                {
                    "Learning Rate": learning_rates[warmup_idx, :],
                    "model_size:warmup": ["512:4000", "512:8000", "256:4000"][
                        warmup_idx
                    ],
                    "step": range(20000),
                }
            )
            for warmup_idx in [0, 1, 2]
        ]
    )

    return (
        alt.Chart(opts_data)
        .mark_line()
        .properties(width=600)
        .encode(x="step", y="Learning Rate", color="model_size:warmup:N")
        .interactive()
    )


example_learning_schedule()
```

<img alt="" height="433" src="https://img-blog.csdnimg.cn/direct/e73d517f8c9d474886e44412a093c23d.png" width="990">



### **<strong><strong>正则化**</strong></strong>

#### **<strong><strong>标签平滑**</strong></strong>

在训练过程中，我们使用值ϵls =0.1的标签平滑(引用)。这损害了困惑，这会损害复杂度，因为模型学习变得更加不确定，但提高了准确性和BLEU分数。

我们使用KL散度损失来实现标签平滑。我们没有使用单一目标分布，而是创建一个分布，该分布对正确单词有信心，其余的平滑质量分布在整个词汇表中。

```
class LabelSmoothing(nn.Module):
    "Implement label smoothing."

    def __init__(self, size, padding_idx, smoothing=0.0):
        super(LabelSmoothing, self).__init__()
        self.criterion = nn.KLDivLoss(reduction="sum")
        self.padding_idx = padding_idx
        self.confidence = 1.0 - smoothing
        self.smoothing = smoothing
        self.size = size
        self.true_dist = None

    def forward(self, x, target):
        assert x.size(1) == self.size
        true_dist = x.data.clone()
        true_dist.fill_(self.smoothing / (self.size - 2))
        true_dist.scatter_(1, target.data.unsqueeze(1), self.confidence)
        true_dist[:, self.padding_idx] = 0
        mask = torch.nonzero(target.data == self.padding_idx)
        if mask.dim() &gt; 0:
            true_dist.index_fill_(0, mask.squeeze(), 0.0)
        self.true_dist = true_dist
        return self.criterion(x, true_dist.clone().detach())
```



在这里，我们可以看到一个示例，根据信心如何将质量分配给单词。

```
# Example of label smoothing.


def example_label_smoothing():
    crit = LabelSmoothing(5, 0, 0.4)
    predict = torch.FloatTensor(
        [
            [0, 0.2, 0.7, 0.1, 0],
            [0, 0.2, 0.7, 0.1, 0],
            [0, 0.2, 0.7, 0.1, 0],
            [0, 0.2, 0.7, 0.1, 0],
            [0, 0.2, 0.7, 0.1, 0],
        ]
    )
    crit(x=predict.log(), target=torch.LongTensor([2, 1, 0, 3, 3]))
    LS_data = pd.concat(
        [
            pd.DataFrame(
                {
                    "target distribution": crit.true_dist[x, y].flatten(),
                    "columns": y,
                    "rows": x,
                }
            )
            for y in range(5)
            for x in range(5)
        ]
    )

    return (
        alt.Chart(LS_data)
        .mark_rect(color="Blue", opacity=1)
        .properties(height=200, width=200)
        .encode(
            alt.X("columns:O", title=None),
            alt.Y("rows:O", title=None),
            alt.Color(
                "target distribution:Q", scale=alt.Scale(scheme="viridis")
            ),
        )
        .interactive()
    )


show_example(example_label_smoothing)
```

<img alt="" height="227" src="https://img-blog.csdnimg.cn/direct/3eacc705e11b474e9e94f507b950b31e.png" width="346">

标签平滑实际上开始惩罚模型，如果模型对给定选择非常有信心。

```
def loss(x, crit):
    d = x + 3 * 1
    predict = torch.FloatTensor([[0, x / d, 1 / d, 1 / d, 1 / d]])
    return crit(predict.log(), torch.LongTensor([1])).data


def penalization_visualization():
    crit = LabelSmoothing(5, 0, 0.1)
    loss_data = pd.DataFrame(
        {
            "Loss": [loss(x, crit) for x in range(1, 100)],
            "Steps": list(range(99)),
        }
    ).astype("float")

    return (
        alt.Chart(loss_data)
        .mark_line()
        .properties(width=350)
        .encode(
            x="Steps",
            y="Loss",
        )
        .interactive()
    )


show_example(penalization_visualization)
```

<img alt="" height="315" src="https://img-blog.csdnimg.cn/direct/54805d276e694258bee8adf3f5c86ed5.png" width="362">



### **<strong><strong>第一个示例**</strong></strong>

我们可以从一个简单的复制任务开始。给定一个小词汇表中的随机输入符号集，目标是生成这些相同的符号。

#### **<strong><strong>合成数据**</strong></strong>

```
def data_gen(V, batch_size, nbatches):
    "Generate random data for a src-tgt copy task."
    for i in range(nbatches):
        data = torch.randint(1, V, size=(batch_size, 10))
        data[:, 0] = 1
        src = data.requires_grad_(False).clone().detach()
        tgt = data.requires_grad_(False).clone().detach()
        yield Batch(src, tgt, 0)
```



#### **<strong><strong>损失计算**</strong></strong>

```
class SimpleLossCompute:
    "A simple loss compute and train function."

    def __init__(self, generator, criterion):
        self.generator = generator
        self.criterion = criterion

    def __call__(self, x, y, norm):
        x = self.generator(x)
        sloss = (
            self.criterion(
                x.contiguous().view(-1, x.size(-1)), y.contiguous().view(-1)
            )
            / norm
        )
        return sloss.data * norm, sloss
```



#### **<strong><strong>贪婪的解码**</strong></strong>

为了简单起见，此代码使用贪婪解码预测翻译。

```
def greedy_decode(model, src, src_mask, max_len, start_symbol):
    memory = model.encode(src, src_mask)
    ys = torch.zeros(1, 1).fill_(start_symbol).type_as(src.data)
    for i in range(max_len - 1):
        out = model.decode(
            memory, src_mask, ys, subsequent_mask(ys.size(1)).type_as(src.data)
        )
        prob = model.generator(out[:, -1])
        _, next_word = torch.max(prob, dim=1)
        next_word = next_word.data[0]
        ys = torch.cat(
            [ys, torch.zeros(1, 1).type_as(src.data).fill_(next_word)], dim=1
        )
    return ys
```



```
# Train the simple copy task.


def example_simple_model():
    V = 11
    criterion = LabelSmoothing(size=V, padding_idx=0, smoothing=0.0)
    model = make_model(V, V, N=2)

    optimizer = torch.optim.Adam(
        model.parameters(), lr=0.5, betas=(0.9, 0.98), eps=1e-9
    )
    lr_scheduler = LambdaLR(
        optimizer=optimizer,
        lr_lambda=lambda step: rate(
            step, model_size=model.src_embed[0].d_model, factor=1.0, warmup=400
        ),
    )

    batch_size = 80
    for epoch in range(20):
        model.train()
        run_epoch(
            data_gen(V, batch_size, 20),
            model,
            SimpleLossCompute(model.generator, criterion),
            optimizer,
            lr_scheduler,
            mode="train",
        )
        model.eval()
        run_epoch(
            data_gen(V, batch_size, 5),
            model,
            SimpleLossCompute(model.generator, criterion),
            DummyOptimizer(),
            DummyScheduler(),
            mode="eval",
        )[0]

    model.eval()
    src = torch.LongTensor([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])
    max_len = src.shape[1]
    src_mask = torch.ones(1, 1, max_len)
    print(greedy_decode(model, src, src_mask, max_len=max_len, start_symbol=0))


# execute_example(example_simple_model)
```





## **第3部分:一个真实世界的例子**

现在我们考虑一个使用Multi30k德语-英语翻译任务的真实示例。这个任务比本文中考虑的WMT任务小得多，但它说明了整个系统。我们还展示了如何使用多gpu处理使其非常快。

### **<strong><strong>数据加载**</strong></strong>

我们将使用torchtext和spacy加载数据集进行标记化。

批处理对速度至关重要。我们希望有非常均匀的分批，用绝对最小的填充。要做到这一点，我们必须破解一些默认的torchtext批处理。这段代码修补了它们的默认批处理，以确保我们搜索足够多的句子来找到紧密的批处理。

```
# Load spacy tokenizer models, download them if they haven't been
# downloaded already


def load_tokenizers():

    try:
        spacy_de = spacy.load("de_core_news_sm")
    except IOError:
        os.system("python -m spacy download de_core_news_sm")
        spacy_de = spacy.load("de_core_news_sm")

    try:
        spacy_en = spacy.load("en_core_web_sm")
    except IOError:
        os.system("python -m spacy download en_core_web_sm")
        spacy_en = spacy.load("en_core_web_sm")

    return spacy_de, spacy_en


def tokenize(text, tokenizer):
    return [tok.text for tok in tokenizer.tokenizer(text)]


def yield_tokens(data_iter, tokenizer, index):
    for from_to_tuple in data_iter:
        yield tokenizer(from_to_tuple[index])


def build_vocabulary(spacy_de, spacy_en):
    def tokenize_de(text):
        return tokenize(text, spacy_de)

    def tokenize_en(text):
        return tokenize(text, spacy_en)

    print("Building German Vocabulary ...")
    train, val, test = datasets.Multi30k(language_pair=("de", "en"))
    vocab_src = build_vocab_from_iterator(
        yield_tokens(train + val + test, tokenize_de, index=0),
        min_freq=2,
        specials=["&lt;s&gt;", "&lt;/s&gt;", "&lt;blank&gt;", "&lt;unk&gt;"],
    )

    print("Building English Vocabulary ...")
    train, val, test = datasets.Multi30k(language_pair=("de", "en"))
    vocab_tgt = build_vocab_from_iterator(
        yield_tokens(train + val + test, tokenize_en, index=1),
        min_freq=2,
        specials=["&lt;s&gt;", "&lt;/s&gt;", "&lt;blank&gt;", "&lt;unk&gt;"],
    )

    vocab_src.set_default_index(vocab_src["&lt;unk&gt;"])
    vocab_tgt.set_default_index(vocab_tgt["&lt;unk&gt;"])

    return vocab_src, vocab_tgt


def load_vocab(spacy_de, spacy_en):
    if not exists("vocab.pt"):
        vocab_src, vocab_tgt = build_vocabulary(spacy_de, spacy_en)
        torch.save((vocab_src, vocab_tgt), "vocab.pt")
    else:
        vocab_src, vocab_tgt = torch.load("vocab.pt")
    print("Finished.\nVocabulary sizes:")
    print(len(vocab_src))
    print(len(vocab_tgt))
    return vocab_src, vocab_tgt


if is_interactive_notebook():
    # global variables used later in the script
    spacy_de, spacy_en = show_example(load_tokenizers)
    vocab_src, vocab_tgt = show_example(load_vocab, args=[spacy_de, spacy_en])


```

```
Finished.
Vocabulary sizes:
59981
36745
```





### **<strong><strong>迭代器**</strong></strong>

```
def collate_batch(
    batch,
    src_pipeline,
    tgt_pipeline,
    src_vocab,
    tgt_vocab,
    device,
    max_padding=128,
    pad_id=2,
):
    bs_id = torch.tensor([0], device=device)  # &lt;s&gt; token id
    eos_id = torch.tensor([1], device=device)  # &lt;/s&gt; token id
    src_list, tgt_list = [], []
    for (_src, _tgt) in batch:
        processed_src = torch.cat(
            [
                bs_id,
                torch.tensor(
                    src_vocab(src_pipeline(_src)),
                    dtype=torch.int64,
                    device=device,
                ),
                eos_id,
            ],
            0,
        )
        processed_tgt = torch.cat(
            [
                bs_id,
                torch.tensor(
                    tgt_vocab(tgt_pipeline(_tgt)),
                    dtype=torch.int64,
                    device=device,
                ),
                eos_id,
            ],
            0,
        )
        src_list.append(
            # warning - overwrites values for negative values of padding - len
            pad(
                processed_src,
                (
                    0,
                    max_padding - len(processed_src),
                ),
                value=pad_id,
            )
        )
        tgt_list.append(
            pad(
                processed_tgt,
                (0, max_padding - len(processed_tgt)),
                value=pad_id,
            )
        )

    src = torch.stack(src_list)
    tgt = torch.stack(tgt_list)
    return (src, tgt)



def create_dataloaders(
    device,
    vocab_src,
    vocab_tgt,
    spacy_de,
    spacy_en,
    batch_size=12000,
    max_padding=128,
    is_distributed=True,
):
    # def create_dataloaders(batch_size=12000):
    def tokenize_de(text):
        return tokenize(text, spacy_de)

    def tokenize_en(text):
        return tokenize(text, spacy_en)

    def collate_fn(batch):
        return collate_batch(
            batch,
            tokenize_de,
            tokenize_en,
            vocab_src,
            vocab_tgt,
            device,
            max_padding=max_padding,
            pad_id=vocab_src.get_stoi()["&lt;blank&gt;"],
        )

    train_iter, valid_iter, test_iter = datasets.Multi30k(
        language_pair=("de", "en")
    )

    train_iter_map = to_map_style_dataset(
        train_iter
    )  # DistributedSampler needs a dataset len()
    train_sampler = (
        DistributedSampler(train_iter_map) if is_distributed else None
    )
    valid_iter_map = to_map_style_dataset(valid_iter)
    valid_sampler = (
        DistributedSampler(valid_iter_map) if is_distributed else None
    )

    train_dataloader = DataLoader(
        train_iter_map,
        batch_size=batch_size,
        shuffle=(train_sampler is None),
        sampler=train_sampler,
        collate_fn=collate_fn,
    )
    valid_dataloader = DataLoader(
        valid_iter_map,
        batch_size=batch_size,
        shuffle=(valid_sampler is None),
        sampler=valid_sampler,
        collate_fn=collate_fn,
    )
    return train_dataloader, valid_dataloader



```



### **<strong><strong>训练**</strong>**<strong>系统**</strong></strong>

经过训练后，我们可以解码模型以生成一组翻译。这里我们简单地翻译验证集中的第一个句子。这个数据集非常小，所以贪婪搜索的翻译是相当准确的。

```
def train_worker(
    gpu,
    ngpus_per_node,
    vocab_src,
    vocab_tgt,
    spacy_de,
    spacy_en,
    config,
    is_distributed=False,
):
    print(f"Train worker process using GPU: {gpu} for training", flush=True)
    torch.cuda.set_device(gpu)

    pad_idx = vocab_tgt["&lt;blank&gt;"]
    d_model = 512
    model = make_model(len(vocab_src), len(vocab_tgt), N=6)
    model.cuda(gpu)
    module = model
    is_main_process = True
    if is_distributed:
        dist.init_process_group(
            "nccl", init_method="env://", rank=gpu, world_size=ngpus_per_node
        )
        model = DDP(model, device_ids=[gpu])
        module = model.module
        is_main_process = gpu == 0

    criterion = LabelSmoothing(
        size=len(vocab_tgt), padding_idx=pad_idx, smoothing=0.1
    )
    criterion.cuda(gpu)

    train_dataloader, valid_dataloader = create_dataloaders(
        gpu,
        vocab_src,
        vocab_tgt,
        spacy_de,
        spacy_en,
        batch_size=config["batch_size"] // ngpus_per_node,
        max_padding=config["max_padding"],
        is_distributed=is_distributed,
    )

    optimizer = torch.optim.Adam(
        model.parameters(), lr=config["base_lr"], betas=(0.9, 0.98), eps=1e-9
    )
    lr_scheduler = LambdaLR(
        optimizer=optimizer,
        lr_lambda=lambda step: rate(
            step, d_model, factor=1, warmup=config["warmup"]
        ),
    )
    train_state = TrainState()

    for epoch in range(config["num_epochs"]):
        if is_distributed:
            train_dataloader.sampler.set_epoch(epoch)
            valid_dataloader.sampler.set_epoch(epoch)

        model.train()
        print(f"[GPU{gpu}] Epoch {epoch} Training ====", flush=True)
        _, train_state = run_epoch(
            (Batch(b[0], b[1], pad_idx) for b in train_dataloader),
            model,
            SimpleLossCompute(module.generator, criterion),
            optimizer,
            lr_scheduler,
            mode="train+log",
            accum_iter=config["accum_iter"],
            train_state=train_state,
        )

        GPUtil.showUtilization()
        if is_main_process:
            file_path = "%s%.2d.pt" % (config["file_prefix"], epoch)
            torch.save(module.state_dict(), file_path)
        torch.cuda.empty_cache()

        print(f"[GPU{gpu}] Epoch {epoch} Validation ====", flush=True)
        model.eval()
        sloss = run_epoch(
            (Batch(b[0], b[1], pad_idx) for b in valid_dataloader),
            model,
            SimpleLossCompute(module.generator, criterion),
            DummyOptimizer(),
            DummyScheduler(),
            mode="eval",
        )
        print(sloss)
        torch.cuda.empty_cache()

    if is_main_process:
        file_path = "%sfinal.pt" % config["file_prefix"]
        torch.save(module.state_dict(), file_path)



def train_distributed_model(vocab_src, vocab_tgt, spacy_de, spacy_en, config):
    from the_annotated_transformer import train_worker

    ngpus = torch.cuda.device_count()
    os.environ["MASTER_ADDR"] = "localhost"
    os.environ["MASTER_PORT"] = "12356"
    print(f"Number of GPUs detected: {ngpus}")
    print("Spawning training processes ...")
    mp.spawn(
        train_worker,
        nprocs=ngpus,
        args=(ngpus, vocab_src, vocab_tgt, spacy_de, spacy_en, config, True),
    )


def train_model(vocab_src, vocab_tgt, spacy_de, spacy_en, config):
    if config["distributed"]:
        train_distributed_model(
            vocab_src, vocab_tgt, spacy_de, spacy_en, config
        )
    else:
        train_worker(
            0, 1, vocab_src, vocab_tgt, spacy_de, spacy_en, config, False
        )


def load_trained_model():
    config = {
        "batch_size": 32,
        "distributed": False,
        "num_epochs": 8,
        "accum_iter": 10,
        "base_lr": 1.0,
        "max_padding": 72,
        "warmup": 3000,
        "file_prefix": "multi30k_model_",
    }
    model_path = "multi30k_model_final.pt"
    if not exists(model_path):
        train_model(vocab_src, vocab_tgt, spacy_de, spacy_en, config)

    model = make_model(len(vocab_src), len(vocab_tgt), N=6)
    model.load_state_dict(torch.load("multi30k_model_final.pt"))
    return model


if is_interactive_notebook():
    model = load_trained_model()
```







### **<strong><strong>附加组件**</strong>**<strong>：**</strong>**<strong>BPE，搜索，平均**</strong></strong>

附加组件:BPE，搜索，平均

这主要涵盖了transformer模型本身。有四个方面我们没有明确讨论。我们还在OpenNMT-py中实现了所有这些附加功能。

1.BPE/字块/词片段：我们可以使用一个库首先将数据预处理成子词单元。参见Rico Sennrich的subword-nmt实现。这些模型将把训练数据转换成这样:

&gt;&gt; 共享嵌入：当使用BPE和共享词汇表时，我们可以在源/目标/生成器之间共享相同的权重向量。详情请参阅(引用)。要将其添加到模型中，只需这样做:

```
if False:
    model.src_embed[0].lut.weight = model.tgt_embeddings[0].lut.weight
    model.generator.lut.weight = model.tgt_embed[0].lut.weight
```

&gt;&gt; 光束搜索：这有点太复杂了，无法在这里介绍。有关pytorch的实现，请参阅OpenNMT-py。

&gt;&gt; 模型平均：本文对最后k个检查点进行平均，以创建集成效果。我们可以在事后这样做，如果我们有一堆模型:

```
def average(model, models):
    "Average models into model"
    for ps in zip(*[m.params() for m in [model] + models]):
        ps[0].copy_(torch.sum(*ps[1:]) / len(ps[1:]))
```



## **结果**

在WMT 2014英德翻译任务中，大型transformer模型(表2中的transformer (big))比之前报道的最佳模型(包括集成)高出2.0 BLEU以上，建立了新的最先进的BLEU分数28.4。该模型的配置列在表3的底线。训练时间为3.5天，使用的是8个P100图形处理器。甚至我们的基本模型也超过了所有以前发表的模型和集合，而训练成本只是任何竞争模型的一小部分。

在WMT 2014英法翻译任务上，我们的大模型获得了41.0的BLEU分数，超过了所有先前发布的所有单一模型，而训练成本不到之前最先进模型的1/4。训练为英语到法语的Transformer(大)模型使用的辍学率Pdrop = 0.1，而不是0.3。

<img alt="" height="230" src="https://img-blog.csdnimg.cn/direct/855f090056fa48a2b469d127161a8c3b.png" width="509">

通过上一节中的附加扩展，OpenNMT-py复制在EN-DE WMT上达到了26.9。这里我已经将这些参数加载到我们的重新实现中。

```
# Load data and model for output checks


def check_outputs(
    valid_dataloader,
    model,
    vocab_src,
    vocab_tgt,
    n_examples=15,
    pad_idx=2,
    eos_string="&lt;/s&gt;",
):
    results = [()] * n_examples
    for idx in range(n_examples):
        print("\nExample %d ========\n" % idx)
        b = next(iter(valid_dataloader))
        rb = Batch(b[0], b[1], pad_idx)
        greedy_decode(model, rb.src, rb.src_mask, 64, 0)[0]

        src_tokens = [
            vocab_src.get_itos()[x] for x in rb.src[0] if x != pad_idx
        ]
        tgt_tokens = [
            vocab_tgt.get_itos()[x] for x in rb.tgt[0] if x != pad_idx
        ]

        print(
            "Source Text (Input)        : "
            + " ".join(src_tokens).replace("\n", "")
        )
        print(
            "Target Text (Ground Truth) : "
            + " ".join(tgt_tokens).replace("\n", "")
        )
        model_out = greedy_decode(model, rb.src, rb.src_mask, 72, 0)[0]
        model_txt = (
            " ".join(
                [vocab_tgt.get_itos()[x] for x in model_out if x != pad_idx]
            ).split(eos_string, 1)[0]
            + eos_string
        )
        print("Model Output               : " + model_txt.replace("\n", ""))
        results[idx] = (rb, src_tokens, tgt_tokens, model_out, model_txt)
    return results


def run_model_example(n_examples=5):
    global vocab_src, vocab_tgt, spacy_de, spacy_en

    print("Preparing Data ...")
    _, valid_dataloader = create_dataloaders(
        torch.device("cpu"),
        vocab_src,
        vocab_tgt,
        spacy_de,
        spacy_en,
        batch_size=1,
        is_distributed=False,
    )

    print("Loading Trained Model ...")

    model = make_model(len(vocab_src), len(vocab_tgt), N=6)
    model.load_state_dict(
        torch.load("multi30k_model_final.pt", map_location=torch.device("cpu"))
    )

    print("Checking Model Outputs:")
    example_data = check_outputs(
        valid_dataloader, model, vocab_src, vocab_tgt, n_examples=n_examples
    )
    return model, example_data


# execute_example(run_model_example)
```





### **<strong><strong>注意力**</strong>**<strong>可视化**</strong></strong>

即使有一个贪婪的解码器，翻译看起来也很好。我们可以进一步可视化它，看看在每一层注意力上发生了什么。

```
def mtx2df(m, max_row, max_col, row_tokens, col_tokens):
    "convert a dense matrix to a data frame with row and column indices"
    return pd.DataFrame(
        [
            (
                r,
                c,
                float(m[r, c]),
                "%.3d %s"
                % (r, row_tokens[r] if len(row_tokens) &gt; r else "&lt;blank&gt;"),
                "%.3d %s"
                % (c, col_tokens[c] if len(col_tokens) &gt; c else "&lt;blank&gt;"),
            )
            for r in range(m.shape[0])
            for c in range(m.shape[1])
            if r &lt; max_row and c &lt; max_col
        ],
        # if float(m[r,c]) != 0 and r &lt; max_row and c &lt; max_col],
        columns=["row", "column", "value", "row_token", "col_token"],
    )


def attn_map(attn, layer, head, row_tokens, col_tokens, max_dim=30):
    df = mtx2df(
        attn[0, head].data,
        max_dim,
        max_dim,
        row_tokens,
        col_tokens,
    )
    return (
        alt.Chart(data=df)
        .mark_rect()
        .encode(
            x=alt.X("col_token", axis=alt.Axis(title="")),
            y=alt.Y("row_token", axis=alt.Axis(title="")),
            color="value",
            tooltip=["row", "column", "value", "row_token", "col_token"],
        )
        .properties(height=400, width=400)
        .interactive()
    )

Explain
def get_encoder(model, layer):
    return model.encoder.layers[layer].self_attn.attn


def get_decoder_self(model, layer):
    return model.decoder.layers[layer].self_attn.attn


def get_decoder_src(model, layer):
    return model.decoder.layers[layer].src_attn.attn


def visualize_layer(model, layer, getter_fn, ntokens, row_tokens, col_tokens):
    # ntokens = last_example[0].ntokens
    attn = getter_fn(model, layer)
    n_heads = attn.shape[1]
    charts = [
        attn_map(
            attn,
            0,
            h,
            row_tokens=row_tokens,
            col_tokens=col_tokens,
            max_dim=ntokens,
        )
        for h in range(n_heads)
    ]
    assert n_heads == 8
    return alt.vconcat(
        charts[0]
        # | charts[1]
        | charts[2]
        # | charts[3]
        | charts[4]
        # | charts[5]
        | charts[6]
        # | charts[7]
        # layer + 1 due to 0-indexing
    ).properties(title="Layer %d" % (layer + 1))
```



### **<strong><strong>编码器自我注意**</strong></strong>

```
def viz_encoder_self():
    model, example_data = run_model_example(n_examples=1)
    example = example_data[
        len(example_data) - 1
    ]  # batch object for the final example

    layer_viz = [
        visualize_layer(
            model, layer, get_encoder, len(example[1]), example[1], example[1]
        )
        for layer in range(6)
    ]
    return alt.hconcat(
        layer_viz[0]
        # &amp; layer_viz[1]
        &amp; layer_viz[2]
        # &amp; layer_viz[3]
        &amp; layer_viz[4]
        # &amp; layer_viz[5]
    )


show_example(viz_encoder_self)
```

```
Preparing Data ...
Loading Trained Model ...
Checking Model Outputs:

Example 0 ========

Source Text (Input)        : &lt;s&gt; Zwei Frauen in pinkfarbenen T-Shirts und &lt;unk&gt; unterhalten sich vor einem &lt;unk&gt; . &lt;/s&gt;
Target Text (Ground Truth) : &lt;s&gt; Two women wearing pink T - shirts and blue jeans converse outside clothing store . &lt;/s&gt;
Model Output               : &lt;s&gt; Two women in pink shirts and face are talking in front of a &lt;unk&gt; . &lt;/s&gt;
```

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/direct/e51e0e615627433dbbaea90eabaa44ed.png" width="1200">



### **<strong><strong>解码器自我注意**</strong></strong>

```
def viz_decoder_self():
    model, example_data = run_model_example(n_examples=1)
    example = example_data[len(example_data) - 1]

    layer_viz = [
        visualize_layer(
            model,
            layer,
            get_decoder_self,
            len(example[1]),
            example[1],
            example[1],
        )
        for layer in range(6)
    ]
    return alt.hconcat(
        layer_viz[0]
        &amp; layer_viz[1]
        &amp; layer_viz[2]
        &amp; layer_viz[3]
        &amp; layer_viz[4]
        &amp; layer_viz[5]
    )


show_example(viz_decoder_self)
```

```
Preparing Data ...
Loading Trained Model ...
Checking Model Outputs:

Example 0 ========

Source Text (Input)        : &lt;s&gt; Eine Gruppe von Männern in Kostümen spielt Musik . &lt;/s&gt;
Target Text (Ground Truth) : &lt;s&gt; A group of men in costume play music . &lt;/s&gt;
Model Output               : &lt;s&gt; A group of men in costumes playing music . &lt;/s&gt;
```

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/direct/96493c6e1c74497a9e93f06f47caa729.png" width="1200">



### **<strong><strong>解码器SRC自我注意**</strong></strong>

```
def viz_decoder_src():
    model, example_data = run_model_example(n_examples=1)
    example = example_data[len(example_data) - 1]

    layer_viz = [
        visualize_layer(
            model,
            layer,
            get_decoder_src,
            max(len(example[1]), len(example[2])),
            example[1],
            example[2],
        )
        for layer in range(6)
    ]
    return alt.hconcat(
        layer_viz[0]
        &amp; layer_viz[1]
        &amp; layer_viz[2]
        &amp; layer_viz[3]
        &amp; layer_viz[4]
        &amp; layer_viz[5]
    )


show_example(viz_decoder_src)


```

```
Preparing Data ...
Loading Trained Model ...
Checking Model Outputs:

Example 0 ========

Source Text (Input)        : &lt;s&gt; Ein kleiner Junge verwendet einen Bohrer , um ein Loch in ein Holzstück zu machen . &lt;/s&gt;
Target Text (Ground Truth) : &lt;s&gt; A little boy using a drill to make a hole in a piece of wood . &lt;/s&gt;
Model Output               : &lt;s&gt; A little boy uses a machine to be working in a hole in a log . &lt;/s&gt;
```

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/direct/71d7b8d2b36940dca9258a7d6e19c89b.png" width="1200">





## **结论**

希望这段代码对未来的研究有用。如果你有任何问题，请联系我们。

Cheers, Sasha Rush, Austin Huang, Suraj Subramanian, Jonathan Sum, Khalid Almubarak, Stella Biderman




