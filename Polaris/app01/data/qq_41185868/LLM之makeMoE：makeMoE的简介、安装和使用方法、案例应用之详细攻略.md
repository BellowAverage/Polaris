
--- 
title:  LLM之makeMoE：makeMoE的简介、安装和使用方法、案例应用之详细攻略 
tags: []
categories: [] 

---
LLM之makeMoE：makeMoE的简介、安装和使用方法、案例应用之详细攻略





**目录**























## **<strong><strong>makeMoE**</strong>**<strong>的简介**</strong></strong>

<img alt="" height="358" src="https://img-blog.csdnimg.cn/direct/2796e15562b74cf2bf3b030891acb90d.png" width="386">

2024年1月23日，AviSoori1x发布了makeMoE。makeMoE是一个从头开始实现的稀疏专家混合语言模型，灵感主要来自（并且在很大程度上基于）Andrej Karpathy的

**GitHub地址**：

**<strong>HuggingFace社区博客**</strong>**<strong>地址**</strong>：





### **<strong><strong>1、对比**</strong>**<strong>makemore**</strong></strong>
<td style="vertical-align:top;width:35.55pt;"> **<strong>简介**</strong> </td><td style="vertical-align:top;width:390.55pt;"> 这是一个从头开始实现的稀疏专家混合语言模型。灵感主要来自Andrej Karpathy的项目'makemore'，并借用了该实现的可重用组件。与makemore一样，makeMoE也是一个自回归的字符级语言模型，但使用了前述的稀疏专家混合架构。 </td>

这是一个从头开始实现的稀疏专家混合语言模型。灵感主要来自Andrej Karpathy的项目'makemore'，并借用了该实现的可重用组件。与makemore一样，makeMoE也是一个自回归的字符级语言模型，但使用了前述的稀疏专家混合架构。
<td rowspan="2" style="vertical-align:top;width:35.55pt;"> **<strong>对比**</strong> </td><td style="vertical-align:top;width:390.55pt;"> 与makemore一样，pytorch是唯一的要求（所以希望从头开始的说法是合理的）。 与makemore架构相比的重要变化： &gt;&gt; 稀疏专家混合代替独立的前馈神经网络。 &gt;&gt; Top-k门控和有噪声的Top-k门控实现。 &gt;&gt; 初始化 - 这里使用了Kaiming He初始化，但这个笔记本的目的是可黑客化的，所以你可以替换为Xavier Glorot等，并试试效果。 </td>

与makemore一样，pytorch是唯一的要求（所以希望从头开始的说法是合理的）。

&gt;&gt; 稀疏专家混合代替独立的前馈神经网络。

&gt;&gt; 初始化 - 这里使用了Kaiming He初始化，但这个笔记本的目的是可黑客化的，所以你可以替换为Xavier Glorot等，并试试效果。
<td style="vertical-align:top;width:390.55pt;"> 与makemore相同的部分： &gt;&gt; 数据集、预处理（标记化）和Andrej最初选择的语言建模任务 - 生成类似莎士比亚的文本。 &gt;&gt; 因果自注意力实现 &gt;&gt; 训练循环 &gt;&gt; 推理逻辑 </td>

&gt;&gt; 数据集、预处理（标记化）和Andrej最初选择的语言建模任务 - 生成类似莎士比亚的文本。

&gt;&gt; 训练循环
<td style="vertical-align:top;width:35.55pt;"> **<strong>引用**</strong> </td><td style="vertical-align:top;width:390.55pt;"> &gt;&gt; "Outrageously Large Neural Networks: The Sparsely-Gated Mixture-Of-Experts layer"：https://arxiv.org/pdf/1701.06538.pdf &gt;&gt; "Mixture of Experts"：https://arxiv.org/pdf/2401.04088.pdf </td>

&gt;&gt; "Outrageously Large Neural Networks: The Sparsely-Gated Mixture-Of-Experts layer"：https://arxiv.org/pdf/1701.06538.pdf





### **<strong><strong>2、相关代码文件**</strong></strong>

#### **<strong><strong>makMoE_from_Scratch.ipynb**</strong>**<strong>文件**</strong></strong>

makMoE_from_Scratch.ipynb详细介绍了整个模型架构的直觉以及所有组件如何配合。建议从这里开始。





#### **<strong><strong>makeMoE_Concise.ipynb**</strong>**<strong>文件**</strong></strong>

makeMoE_Concise.ipynb是一个简洁的、可修改性的实现，我鼓励你去修改，理解，改进并使其成为你自己的。





## **<strong><strong>makeMoE**</strong>**<strong>的安装和使用方法**</strong></strong>

### **<strong><strong>1、基于**</strong>**<strong>Databricks使用单个A100进行开发**</strong></strong>

该代码完全在Databricks上使用单个A100进行开发。如果你在Databricks上运行这个代码，可以在你选择的云提供商上轻松地将其扩展到任意大的GPU集群上。

我选择使用MLFlow（在Databricks中预先安装）。这是完全开源的，你也可以在其他地方轻松pip install。我发现使用它来跟踪和记录所有必要的指标非常有帮助。这是完全可选的。

请注意，该实现强调可读性和可修改性而不是性能，因此有许多方法可以改进。请尝试并告诉我！





## **<strong><strong>makeMoE**</strong>**<strong>的案例应用**</strong></strong>

更新中……




