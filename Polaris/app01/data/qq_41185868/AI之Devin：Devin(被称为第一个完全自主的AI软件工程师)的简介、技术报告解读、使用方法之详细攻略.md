
--- 
title:  AI之Devin：Devin(被称为第一个完全自主的AI软件工程师)的简介、技术报告解读、使用方法之详细攻略 
tags: []
categories: [] 

---


AI之Devin：Devin(被称为第一个完全自主的AI软件工程师)的简介、技术报告解读、使用方法之详细攻略





**目录**



























## **Devin****的简介**

2024年3月12日，Cognition AI 团队发布了第一个AI软件工程师Devin，并在SWE-bench编码基准测试中设立了新的技术标杆，被称为世界上第一个完全自主的AI软件工程师。Devin是一个不知疲倦的、技术娴熟的队友，他既可以和你一起构建，也可以独立完成任务，供你审核。有了Devin，工程师可以专注于更有趣的问题，工程团队可以追求更雄心勃勃的目标。

**<strong>博客文章**</strong>：





### **<strong><strong>1、**</strong>**<strong>Devin的能力**</strong></strong>

通过我们在长期推理和规划方面的进展，Devin可以规划和执行需要数千个决策的复杂工程任务。Devin可以在每一步都召回相关的上下文，随着时间的推移学习，并纠正错误。

我们还为Devin配备了常见的开发者工具，包括外壳、代码编辑器和浏览器，这些都在一个沙箱计算环境中——这是人类工作者所需的一切。

最后，我们赋予Devin与用户积极合作的能力。Devin实时报告自己的进展，接受反馈，并在必要时与您一起进行设计选择。

以下是Devin的一些示例能力：

#### **<strong><strong>Devin可以学习如何使用不熟悉的技术**</strong></strong>

Devin在Modal上运行ControlNet以生成带有隐藏信息的图像，供Sara使用。

视频地址：



#### **<strong><strong>Devin可以构建和部署端到端的应用程序**</strong></strong>

Devin创建了一个交互式网站，模拟了生命游戏！它逐步添加用户请求的功能，然后将应用程序部署到Netlify。

视频地址：



#### **<strong><strong>Devin可以自主地找出并修复代码库中的错误**</strong></strong>

Devin帮助Andrew维护和调试他的开源竞赛编程书籍。

视频地址：



#### **<strong><strong>Devin可以训练和微调自己的AI模型**</strong></strong>

‍Devin仅通过GitHub上的一个研究存储库链接，为一个大型语言模型设置了微调。

Devin可以解决开源存储库中的错误和功能请求。只需一个GitHub问题的链接，Devin就可以完成所有必要的设置和上下文收集。

视频地址：



#### **<strong><strong>Devin可以为成熟的生产存储库做出贡献。**</strong></strong>

这个例子是SWE-bench基准测试的一部分。Devin解决了sympy Python代数系统中对数计算的错误。Devin设置了代码环境，重现了错误，并独立编写和测试了修复代码。

视频地址：



我们甚至尝试让Devin在Upwork上做真正的工作，它也能胜任！‍

在这里，Devin编写并调试代码以运行计算机视觉模型。Devin对生成的数据进行采样，并在最后编制了一份报告。



### **<strong><strong>2、**</strong>**<strong>Devin的表现**</strong></strong>

<img alt="" height="429" src="https://img-blog.csdnimg.cn/direct/a0b7376911124f0181a86fb67ad4184e.png" width="800">

我们在SWE-bench上评估了Devin，这是一个具有挑战性的基准测试，要求代理解决在开源项目中（如Django和scikit-learn）找到的真实世界GitHub问题。

Devin正确解决了13.86%*的问题，远远超过了以前的技术水平1.96%。即使给出了要编辑的确切文件，以前的最佳模型也只能解决4.80%的问题。

*Devin在数据集的随机25%子集上进行了评估。Devin没有受到帮助，而所有其他模型都受到了帮助（这意味着模型被告知需要编辑哪些文件）。







## **Devin****的技术报告**

<img alt="" height="144" src="https://img-blog.csdnimg.cn/direct/c6f66e5fa2dd49399617ed4306679415.png" width="610">

Cognition公司在SWE-bench代码工程测试套件上的评估工作。

SWE-bench是从GitHub上提取的2294个Python项目中的问题报告和拉取请求，可以用于测试系统编写真实代码的能力。每个实例包含一个问题和解决该问题的拉取请求，拉取请求必须包含“先失败后通过”的单元测试。

Cognition公司开发了Devin这个AI代理，专注于软件开发。他们利用SWE-bench来评估Devin的能力。与依靠单独函数的HumanEval相比，SWE-bench能够在真实代码库中以确定性方式评估系统解决问题的能力，是一种更好的选择。

Devin在570个SWE-bench用例中的79个用例中成功解决问题，成功率达到13.86%。这远远超过了以往最好的未辅助基线1.96%。即使给出了正确的文件需要修改，最好的先前模型也只有4.8%的成功率。

Devin能够进行多步计划，72%的通过测试需要超过10分钟，说明迭代能力对其有帮助。Devin还能够一次处理多个行代码，成功完成一些往往需要单行改动的用例。

当提供单元测试时，Devin正确解决问题的成功率提高到23%。这说明测试驱动开发模式对Devin很有帮助。

总体而言，Devin在SWE-bench这个真实代码开发能力测试套件上获得了很好的成绩。这表明了AI代理在软件开发等复杂任务上的潜力，还需要不断改进以提高成功率。

**<strong>文章地址**</strong>：



<img alt="" height="1200" src="https://img-blog.csdnimg.cn/direct/30a5943a6fef44c48c8f7aaf05f22d8f.png" width="1200">



## **Devin****的使用方法**

Devin目前处于早期测试阶段，持续更新中……








