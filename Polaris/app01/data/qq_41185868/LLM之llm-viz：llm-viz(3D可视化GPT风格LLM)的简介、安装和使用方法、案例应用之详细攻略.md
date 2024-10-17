
--- 
title:  LLM之llm-viz：llm-viz(3D可视化GPT风格LLM)的简介、安装和使用方法、案例应用之详细攻略 
tags: []
categories: [] 

---
LLM之llm-viz：llm-viz(3D可视化GPT风格LLM)的简介、安装和使用方法、案例应用之详细攻略





**目录**





















## **llm-viz的简介**

<img alt="" height="908" src="https://img-blog.csdnimg.cn/direct/a19a90d561d345188f71c3aa71be18eb.png" width="1200">

2023年3月，软件工程师Brendan Bycroft开发了llm-viz，这是一个3D可视化GPT风格LLM的项目。为了方便部署和共享一些在其他情况下难以共享的js工具，它们被保存在一个单一的存储库中。项目主要包括： &gt;&gt; LLM可视化：GPT风格的LLM网络运行推理的3D交互模型。 &gt;&gt; [WIP] CPU模拟：带有完整执行模型的2D数字原理图编辑器，展示基于简单的RISC-V CPU的模型。

**<strong>GitHub地址**</strong>：

**<strong>在线体验地址**</strong>：





### **<strong><strong>1、LLM可视化**</strong></strong>

该项目展示了一个GPT风格网络的工作实现的3D模型。也就是说，这是OpenAI的**<strong>GPT-2**</strong>、**<strong>GPT-3（**</strong>以及可能的GPT-4）中使用的网络拓扑结构。

显示的第一个具有工作权重的网络是一个微小的网络，用于对字母A、B和C的小列表进行排序。这是Andrej Karpathy的minGPT实现的演示示例模型。

渲染器还支持可视化任意大小的网络，并与较小的gpt2大小一起工作，尽管权重没有被下载（因为它是数百MB）。





### **<strong><strong>2、CPU模拟（WIP；尚未公开！）**</strong></strong>

该项目运行2D原理数字电路，带有完整的编辑器。其目的是添加一些演练，展示诸如： &gt;&gt; 如何构建简单的RISC-V CPU； &gt;&gt; 构建到门级别的组成部分：指令解码、ALU、加法等； &gt;&gt; 更高级的CPU思想，如各种级别的流水线、缓存等；







## **llm-viz的安装和使用方法**

本地运行 安装依赖项：yarn 启动开发服务器：yarn dev





## **llm-viz的案例应用**

**<strong>在线体验地址**</strong>：



### **<strong><strong>1、三维可视化nano-GPT进而理解**</strong></strong>Transformer内在机制

<img alt="" height="839" src="https://img-blog.csdnimg.cn/direct/5e47204e90914f8aa49092badcb50f71.gif" width="1200">

欢迎来到GPT大型语言模型的演练！在这里，我们将探索模型nano-gpt，它只有85,000个参数。 它的目标很简单：接收一个包含六个字母的序列： C B A B B C 并将它们按字母顺序排序，即变成"ABBBCC"。 我们称这些字母中的每一个为一个标记（token），模型的不同标记集合组成了它的词汇表： 标记    A    B    C 索引    0    1    2 从这个表格中，每个标记都被分配一个数字，即它的标记索引。现在我们可以将这个数字序列输入模型中： 2 1 0 1 1 2 在3D视图中，每个绿色单元格代表一个正在处理的数字，每个蓝色单元格是一个权重。 -0.7 0.4 0.8 正在处理 -0.7 0.7 -0.1 权重 序列中的每个数字首先被转换为一个48元素向量（为这个特定模型选择的大小）。这被称为嵌入（embedding）。 然后，嵌入通过模型传递，经过一系列层，称为变换器（transformers），最终到达底部。

那么输出是什么呢？是序列中下一个标记的预测。因此，在第6个条目，我们得到了下一个标记是'A'、'B'或'C'的概率。 在这种情况下，模型非常确信下一个标记将是'A'。现在，我们可以将这个预测反馈到模型的顶部，并重复整个过程。 在我们深入算法的复杂性之前，让我们先退后一步。 这个指南专注于推理，而不是训练，因此只是整个机器学习过程的一小部分。在我们的情况下，模型的权重已经被预先训练，我们使用推理过程生成输出。这直接在您的浏览器中运行。 这里展示的模型是GPT（生成式预训练Transformer）家族的一部分，可以描述为“基于上下文的标记预测器”。OpenAI于2018年推出了这个家族，其中有一些显著的成员，如GPT-2、GPT-3和GPT-3.5 Turbo，后者是广泛使用的ChatGPT的基础。它可能也与GPT-4有关，但具体细节仍然未知。 这个指南受到了minGPT GitHub项目的启发，这是由Andrej Karpathy创建的一个在PyTorch中实现的极简GPT。他的YouTube系列《Neural Networks: Zero to Hero 》和minGPT项目对本指南的制作提供了宝贵的资源。这里展示的玩具模型基于minGPT项目中的一个模型。



#### LLM之llm-viz：基于llm-viz工具深度理解和剖析nano-gpt模型结构及其Transformer结构内在机制实现原理之详细攻略






