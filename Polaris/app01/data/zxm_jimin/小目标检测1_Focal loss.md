
--- 
title:  小目标检测1_Focal loss 
tags: []
categories: [] 

---
主要参考：    

有参考很多文章与博客，有的可能忘记放出处了，侵权请联系，马上修改~



#### 文章目录
- - - - 


Focal loss是何恺明大神提出，最初用于图像领域解决数据不平衡造成的模型性能问题。

**Focal loss作用：** 1、控制正负样本的权重 2、控制容易分类和难分类样本的权重

## 准备知识

**正负样本**： 一张图像可能生成成千上万的候选框，但是其中只有很少一部分是包含目标的的，有目标的就是正样本，没有目标的就是负样本。

**容易分类和难分类样本**： 假设存在一个二分类，样本1属于类别1的pt=0.9，样本2属于类别1的pt=0.6，显然前者更可能是类别1，其就是容易分类的样本；后者有可能是类别1，所以其为难分类样本。

**one-stage方法效果：** 类别不平衡问题，不利于模型学习 positive examples 很少 hard examples 很少 easy examples 很多（背景类）：

>  
 easy examples 过多：产生的梯度会主导模型学习，削弱对 hard examples 的学习能力，从而降低 hard examples 的准确率 


**熵和信息的定义：**

>  
 我们每时每刻都在获取信息，理解信息，那么到底什么是信息？ 当一件事情（宏观态）有多种可能情况（微观态）时，这种事情（宏观态）对某人（观察者）而言具体是哪种情况（微观态）的**不确定性**叫做**熵**，而能够**消除对该件事情的不确定性的事物**叫做**信息**。 


**信息量**-信息量的大小和事件发生的概率P成反比

<img src="https://img-blog.csdnimg.cn/6984fb444fae4cf4b97711740c8dfdd2.png" alt="在这里插入图片描述"> **信息熵:** 用来衡量事物不确定性的。信息熵越大（信息量越大，P越小），事物越具不确定性，事物越复杂。

**信息熵的公式：** 在结果出来之前对可能产生的**信息量的期望**，期望可以理解为所有可能结果的概率乘以该对应的结果。 <img src="https://img-blog.csdnimg.cn/a0d69e1cfa314d3091a66274581464cc.png" alt="在这里插入图片描述"> 可以把信息熵理解为是求log2 ( p ) <img src="https://img-blog.csdnimg.cn/8e8ff148d6cb423082b92c37def58498.png#pic" alt="在这里插入图片描述" width="50%"> （p=1时，熵=0，不导致任何信息量的增加）

**相对熵:** 相对熵，又被称为KL散度（Kullback-Leible）或信息散度，是两个概率分布间差异的非对称性度量 。在信息论中，相对熵等价于两个概率分布的信息熵的差值，若其中一个概率分布为**真实分布**，另一个为**理论（拟合）分布**，则此时相对熵等于交叉熵与真实分布的信息熵之差，表示使用理论分布拟合真实分布时产生的信息损耗 。 （两个随机分布相同时，它们的相对熵为零，当两个随机分布的差别增大时，它们的相对熵也会增大 ） <img src="https://img-blog.csdnimg.cn/d9bcedb3e3a64be08fe33be2dda99d64.png" alt="在这里插入图片描述">

相对熵与相对熵的推导过程可参考：写得特别好！  

**交叉熵** <img src="https://img-blog.csdnimg.cn/5dae9e11abb644d783f53b174ccd8b47.png" alt="在这里插入图片描述">

>  
 在逻辑回归中： p:真实样本分布，服从参数为p的0-1分布，即X~B(1,p) q:待估计的模型，服从参数为q的0-1分布，即X~B(1,q) 0-1分布，我们把其中一种事件的结果发生的概率定为p，那么另一种结果的概率就是1-p，两者的概率和是1. 


<img src="https://img-blog.csdnimg.cn/ba58ad76cd704e83bb30c97243d6e5ca.png" alt="在这里插入图片描述">

## Focal loss

<img src="https://img-blog.csdnimg.cn/1cedeea0f3c84df98211819d3310359d.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/b60a478e3b604e9483c8c86f3b1ffb44.png" alt="在这里插入图片描述"> **权重因子αt：** 解决 positive/negative examples 问题

**Pt：** 解决 hard/easy examples 问题

>  
 反映了与ground truth即类别y的接近程度， Pt越大说明越接近类别y，即分类越准确 对于正样本而言，1-p的值越大，样本越难分类。 对于负样本而言，p的值越大，样本越难分类。 


<img src="https://img-blog.csdnimg.cn/8735d82079d3400d808a322bdd67f702.png" alt="在这里插入图片描述"> 利用1-Pt就可以计算出每个样本属于容易分类或者难分类。

**调制系数γ：** <img src="https://img-blog.csdnimg.cn/578690f687034a11bb5ede9ace231532.png" alt="在这里插入图片描述"> γ越大，越关注负样本调整该抑制作用的大小（当γ=0的时候，focal loss就是传统的交叉熵损失）

最终公式： <img src="https://img-blog.csdnimg.cn/af32dc50387e4db8871aa42c5b7c4999.png" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/71475636ac7445b9af62c7325df2c5b0.png" alt="在这里插入图片描述">

## OHEM与Focal loss

OHEM本身用在了一个two-stage的模型上，那么正负样本就是可控的，OHEM做的事情是难例挖掘的过程 Focal loss应用在one-stage模型上，无论如何正负样本都不能自由组合，所以只能靠最后计算损失的时候抑制负样本，抑制简单样本，挖掘难例。

## 实现

（未完待续） 可参考：

<img src="https://img-blog.csdnimg.cn/52a92b0608cc4d9299520187dde77ed5.jpeg#pic" alt="在这里插入图片描述" width="30%">
