
--- 
title:  LLMs之Grok-1：Grok-1的简介、安装、使用方法之详细攻略 
tags: []
categories: [] 

---
LLMs之Grok-1：Grok-1的简介、安装、使用方法之详细攻略

>  
 **导读**：马斯克旗下的xAI公司宣布开源名为Grok-1的混合专家模型，参数量达3140亿，为目前最大的开源大语言模型。xAI此举或将引领人工智能开源趋势，同时也将对不太Open的OpenAI等公司形成市场和技术竞争压力。**Grok-1的特点**： &gt;&gt; 从头训练，未针对任何特定任务微调 &gt;&gt; 使用MoE模型，每个token上的平均激活权重为25% &gt;&gt; 采用JAX库和Rust语言从零开始训练 &gt;&gt; 采用Apache许可证完全开源了模型权重和架构**评估结果**：Grok-1在人工评估任务和标准机器学习基准上表现出色，超越其他同类模型。 下载方法：可以使用磁力链接或Torrent客户端下载权重文件，但需要6TB以上GPU内存运行示例代码。 






**目录**













































## **相关文章**

### **<strong><strong>LLMs之Grok：Grok(一款具有00后特点般幽默、机智和实时的大语言模型)的简介、使用方法、案例应用之详细攻略**</strong></strong>





### **<strong><strong>LLMs之Grok-1：Grok-1的简介、安装、使用方法之详细攻略**</strong></strong>





### **<strong><strong>LLMs之Grok-1.5：Grok-1.5的简介、安装和使用方法、案例应用之详细攻略**</strong></strong>





## **Grok-1的简介**

<img alt="" height="320" src="https://img-blog.csdnimg.cn/direct/8845ab557ba54edeab422841e4e43041.png" width="597">

2024年3月17日(当地时间)，马斯克的AI创企xAI重磅发布了Grok-1的基础模型权重和网络架构，这是一款大型语言模型。Grok-1是一个3140亿参数的专家混合模型，远超OpenAI GPT-3.5的1750亿。由xAI从头开始训练。这是Grok-1预训练阶段的原始基础模型检查点，该阶段于2023年10月结束。这意味着该模型没有针对任何特定应用进行微调，比如对话。

要开始使用该模型，请按照github.com/xai-org/grok上的说明操作。

官网：

GitHub地址：





### **<strong><strong>1、**</strong>**<strong>模型详情**</strong></strong>

基于大量文本数据训练的基础模型，没有针对任何特定任务进行微调。 3140亿参数的专家混合模型，对于给定的标记，有25%的权重处于活动状态。 在2023年10月由xAI从头开始使用JAX和Rust的自定义训练堆栈进行训练。

封面图像是使用Midjourney生成的，基于Grok提出的以下提示：

A 3D illustration of a neural network, with transparent nodes and glowing connections, showcasing the varying weights as different thicknesses and colors of the connecting lines.

一个神经网络的3D插图，具有透明的节点和发光的连接，展示了连接线的不同粗细和颜色作为不同权重的变化。



### **<strong><strong>2、**</strong>**<strong>模型规格**</strong>**<strong>细节**</strong></strong>

Grok-1当前设计具有以下规格： 参数：314B 架构：8个专家的混合（MoE） 专家利用率：每个标记使用2个专家 层：64 注意头：48个用于查询，8个用于键/值 嵌入大小：6,144 标记化：带有131,072个标记的SentencePiece分词器 附加功能： 旋转嵌入（RoPE） 支持激活分片和8位量化 最大序列长度（上下文）：8,192个标记





## **Grok-1的安装**

### **<strong><strong>1、下载**</strong></strong>

#### **<strong><strong>(1)、下载仓库**</strong></strong>

这个存储库包含了加载和运行Grok-1开放权重模型的JAX示例代码。

确保下载检查点并将ckpt-0目录放置在checkpoints中 - 请参阅下载权重

地址：





#### **<strong><strong>(2)、**</strong>**<strong>下载**</strong>**<strong>模型**</strong>**<strong>权重**</strong></strong>

##### **<strong><strong>T1、**</strong>**<strong>可以使用种子客户端和以下磁铁链接下载权重：**</strong>**<strong>推荐**</strong></strong>

```
magnet:?xt=urn:btih:5f96d43576e3d386c9ba65b883210a393b68210e&amp;tr=https%3A%2F%2Facademictorrents.com%2Fannounce.php&amp;tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&amp;tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce
```





##### **<strong><strong>T2、**</strong>**<strong>直接使用HuggingFace：**</strong>**<strong>非常慢**</strong></strong>

```
git clone https://github.com/xai-org/grok-1.git &amp;&amp; cd grok-1
pip install huggingface_hub[hf_transfer]
huggingface-cli download xai-org/grok-1 --repo-type model --include ckpt-0/* --local-dir checkpoints --local-dir-use-symlinks False
```



### **<strong><strong>2、**</strong>**<strong>运行**</strong>测试代码</strong>

安装依赖，并测试代码

```
pip install -r requirements.txt
python run.py
```

来测试代码。该脚本会加载检查点并从模型中对测试输入进行采样。

由于模型的体积很大（314B参数），测试模型需要具有足够GPU内存的计算机以运行示例代码。此存储库中MoE层的实现不高效。选择了这种实现以避免需要自定义内核来验证模型的正确性。





## **Grok-1的使用方法**​​​​​​​

### LLMs之Grok-1：run.py文件解读—运行语言模型实现推理—即基于用户的输入文本利用grok_1语言模型来生成文本





### LLMs之Grok-1：model.py文件解读—实现了基于Transformer的预训练语言模型+利用JAX框架支持高性能分布式计算





### LLMs之Grok-1：checkpoint.py文件解读—加载和恢复机器学习模型检查点的工具(基于JAX库处理多维数组计算+大规模分布式训练+多主机间的数据同步和分片)





### LLMs之Grok-1：runners.py文件解读—基于JAX和设备分布的预训练语言模型inference服务+支持批量查询+利用设备资源高效推理同时可以被嵌入训练循环进行微调训练




