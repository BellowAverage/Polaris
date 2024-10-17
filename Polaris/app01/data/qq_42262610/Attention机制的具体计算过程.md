
--- 
title:  Attention机制的具体计算过程 
tags: []
categories: [] 

---
#### 一、介绍Query、Key、Value的来源

一个输入，经过embedding+位置编码后得到最终的输入X（512维），最终的输入X与矩阵参数WQ（512*64维）相乘，得到Query；与矩阵参数WK（512*64维）相乘，得到Key；与矩阵参数WV（512*64维）相乘，得到Value。

Query-某个词（婴儿）转化后的输入向量-64维

Key-整个句子中，每个词转化的某个向量（Key1，Key2，Key3，Key4）-64维

Value-整个句子中，每个词转化的某个向量（Value1，Value2，Value3，Value4）-64维

#### 二、Attention机制的具体计算过程
1. <h5 style="margin-left:1.4em;list-style-type:decimal;text-indent:0;"><li>根据Query和Key计算两者的相似性和相关性。得到s1，s2，s3，s4</h5> 
 </li>
Query和Key点乘（表示一个向量在另一个向量上的长度，是标量，可以反映两个向量之间的相似度，两个向量的点乘越大，相似度越大，表明越关注）

常用方法

（1）求两者的向量点积

（2）求两者的向量【cosine相似性】

（3）引入额外的神经网络来求值，MLP网络。
1. <h5 style="margin-left:1.4em;list-style-type:decimal;text-indent:0;"><li>对原始的分值进行softmax归一化处理（dk=64），得到a1，a2，a3，a4</h5> 
 </li>
公式中为甚要除以根号dk？

因为Query和Key的值很大，进行softmax时反向传播使梯度很小，容易出现梯度消失，除以根号dk是为了保持方差为1.

##### 3. 根据权重系数进行加权求和

#### 三、多头注意力机制是什么？

在实际应用中，使用矩阵方便计算。前面提到的矩阵参数WQ、WK、WV为一套参数，在实际应用中，我们会用到多套WQ、WK、WV参数，例如WQ1、WK1、WV1；WQ2、WK2、WV2；......，将经过embedding+位置编码后得到最终的输入X同时流经多套参数，分别得到各自的Q、K、V，经过上述二的计算过程得到各自参数的attention value，最后将多个输出合并在一起并在此投影得到最终输出。这就是多头注意力机制。

多头注意力机制可以得到不同子空间的信息，使得效果很好。


