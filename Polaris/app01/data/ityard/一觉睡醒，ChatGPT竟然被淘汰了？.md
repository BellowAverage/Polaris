
--- 
title:  一觉睡醒，ChatGPT竟然被淘汰了？ 
tags: []
categories: [] 

---
来源：机器之心 

**注：本标题是 AutoGPT 建议我修改的** 

OpenAI 的 Andrej Karpathy 都大力宣传，认为 AutoGPT 是 prompt 工程的下一个前沿。

近日，AI 界貌似出现了一种新的趋势：自主人工智能。

这不是空穴来风，最近一个名为 AutoGPT 的研究开始走进大众视野。特斯拉前 AI 总监、刚刚回归 OpenAI 的 Andrej Karpathy 也为其大力宣传，并在推特赞扬：「AutoGPT 是 prompt 工程的下一个前沿。」

<img src="https://img-blog.csdnimg.cn/img_convert/f719b61375293aab30f5238986657861.png" alt="f719b61375293aab30f5238986657861.png">

不仅如此，还有人声称 ChatGPT 已经过时了，AutoGPT 才是这个领域的新成员。

<img src="https://img-blog.csdnimg.cn/img_convert/46b399bfaa43c96132cd52c3969c2c56.png" alt="46b399bfaa43c96132cd52c3969c2c56.png">

项目一经上线，短短几天狂揽 27K + 星，这也侧面验证了项目的火爆。

<img src="https://img-blog.csdnimg.cn/img_convert/8e45dcd915d655fea2387c907630409a.png" alt="8e45dcd915d655fea2387c907630409a.png">

GitHub 地址：https://github.com/torantulino/auto-gpt

问题来了，AutoGPT 到底是什么？**它是一个实验性的开源应用程序，展示了 GPT-4 语言模型的功能。该程序由 GPT-4 驱动，可以自主实现用户设定的任何目标。**

<img src="https://img-blog.csdnimg.cn/img_convert/4e84e4cf3c43e85079c5fdc8642bc25e.png" alt="4e84e4cf3c43e85079c5fdc8642bc25e.png">

具体来说，AutoGPT 相当于给基于 GPT 的模型一个内存和一个身体。有了它，你可以把一项任务交给 AI 智能体，让它自主地提出一个计划，然后执行计划。此外其还具有互联网访问、长期和短期内存管理、用于文本生成的 GPT-4 实例以及使用 GPT-3.5 进行文件存储和生成摘要等功能。AutoGPT 用处很多，可用来分析市场并提出交易策略、提供客户服务、进行营销等其他需要持续更新的任务。

正如网友所说 AutoGPT 正在互联网上掀起一场风暴，它无处不在。很快，已经有网友上手实验了，**该用户让 AutoGPT 建立一个网站，不到 3 分钟 AutoGPT 就成功了。**期间 AutoGPT 使用了 React 和 Tailwind CSS，全凭自己，人类没有插手。看来程序员之后真就不再需要编码了。

<img src="https://img-blog.csdnimg.cn/img_convert/2b3badf933628b7d3fb3dae9ddb81ef6.png" alt="2b3badf933628b7d3fb3dae9ddb81ef6.png">

<img src="https://img-blog.csdnimg.cn/img_convert/a780dccc37bfd5d2962547a275c1a5ff.gif" alt="a780dccc37bfd5d2962547a275c1a5ff.gif">

之后该用户补充说，自己的目标很简单，就是用 React 创建一个网站。提出的要求是：创建一个表单，添加标题「Made with autogpt」，然后将背景更改为蓝色。AutoGPT 成功的构建了网站。该用户还表示，如果给 AutoGPT 的 prompt 更多，表现会更好。

<img src="https://img-blog.csdnimg.cn/img_convert/11af8c897658fd44a6d96f5b1887a899.png" alt="11af8c897658fd44a6d96f5b1887a899.png">

**图源：https://twitter.com/SullyOmarr/status/1644160222733406214**

接下里我们再看一个例子。假装自己经营一家鞋公司，给 AutoGPT 下达的命令是对防水鞋进行市场调查，然后让其给出 top5 公司，并报告竞争对手的优缺点 :

<img src="https://img-blog.csdnimg.cn/img_convert/e4d6b9203b383946c6d2e92ddd2e3d1d.png" alt="e4d6b9203b383946c6d2e92ddd2e3d1d.png">

首先，AutoGPT 直接去谷歌搜索，然后找防水鞋综合评估 top 5 的公司。一旦找到相关链接，AutoGPT 就会为自己提出一些问题，例如「每双鞋的优缺点是什么、每款排名前 5 的防水鞋的优缺点是什么、男士排名前 5 的防水鞋」等。

之后，AutoGPT 继续分析其他各类网站，并结合谷歌搜索，更新查询，直到对结果满意为止。期间，AutoGPT 能够判断哪些评论可能偏向于伪造，因此它必须验证评论者。

<img src="https://img-blog.csdnimg.cn/img_convert/510470a4043ef2db3389a01c6dcf14d3.png" alt="510470a4043ef2db3389a01c6dcf14d3.png">

执行过程中，AutoGPT 甚至衍生出自己的子智能体来执行分析网站的任务，找出解决问题的方法，所有工作完全靠自己。

结果是，AutoGPT 给出了 top 5 防水鞋公司的一份非常详细的报告，报告包含各个公司的优缺点，此外还给出了一个简明扼要的结论。全程只用了 8 分钟，费用为 10 美分。期间也完全没有优化。

<img src="https://img-blog.csdnimg.cn/img_convert/167c4a6bb0cd6924d9ddcc8791bb2dbb.png" alt="167c4a6bb0cd6924d9ddcc8791bb2dbb.png">

这个能够独立自主完成任务的 AutoGPT 是如何运行的呢？我们接着来看。

**AutoGPT：30 分钟内构建你自己的 AI 助手**

作为风靡互联网的 AI 智能体，**AutoGPT 可以在 30 分钟内完成设置。**你就可以拥有自己的 AI，协助完成任务，提升工作效率。

这一强大的 AI 工具能够自主执行各种任务，设置和启动的简便性是一大特征。在开始之前，你需要设置 Git、安装 Python、下载 Docker 桌面、获得一个 OpenAI API 密钥。

**克隆存储库**

首先从 GitHub 中克隆 AutoGPT 存储库。

<img src="https://img-blog.csdnimg.cn/img_convert/d655d9b69d10899bc425cf8b38e918c3.png" alt="d655d9b69d10899bc425cf8b38e918c3.png">

使用以下命令导航到新建文件夹 Auto-GPT。

<img src="https://img-blog.csdnimg.cn/img_convert/1264ee7ca7dc20ea9ae288dc58d1b776.png" alt="1264ee7ca7dc20ea9ae288dc58d1b776.png">

**配置环境**

在 Auto-GPT 文件夹中，找到.env.template 文件并插入 OpenAI API 密钥。接着复制该文件并重命名为.env。

<img src="https://img-blog.csdnimg.cn/img_convert/57c0c84a6a78e0bf8452a8e0c97055e3.png" alt="57c0c84a6a78e0bf8452a8e0c97055e3.png">

**安装 Python 包**

运行以下命令，安装需要的 Python 包。

<img src="https://img-blog.csdnimg.cn/img_convert/16b94ced51780e1ef8da94dee4276384.png" alt="16b94ced51780e1ef8da94dee4276384.png">

**运行 Docker**

运行 Docker 桌面，不需要下载任何容器，只需保证程序处于激活状态。

<img src="https://img-blog.csdnimg.cn/img_convert/15054e23e1289938abb00cbd069da5ff.png" alt="15054e23e1289938abb00cbd069da5ff.png">

**运行 AutoGPT**

<img src="https://img-blog.csdnimg.cn/img_convert/6ec5f2936fb847f09b42a3a2ace9b1ea.png" alt="6ec5f2936fb847f09b42a3a2ace9b1ea.png">

执行以下命令，运行 AutoGPT。

<img src="https://img-blog.csdnimg.cn/img_convert/34b950f21c4e0937bc919b6d5218664a.png" alt="34b950f21c4e0937bc919b6d5218664a.png">

**设置目标**

AutoGPT 虽是一个强大的工具，但并不完美。为避免出现问题，最好从简单的目标开始，对输出进行测试，并根据自身需要调整目标，如上文中的 ResearchGPT。

不过，你如果想要释放 AutoGPT 的全部潜力，需要 GPT-4 API 访问权限。GPT-3.5 可能无法为智能体或响应提供所需的深度。

**AgentGPT：浏览器中直接部署自主 AI 智能体**

近日，又有开发者对 AutoGPT 展开了新的探索尝试，创建了一个**可以在浏览器中组装、配置和部署自主 AI 智能体的项目 ——AgentGPT。**项目主要贡献者之一为亚马逊软件工程师 Asim Shrestha，已在 GitHub 上获得了 2.2k 的 Stars。

<img src="https://img-blog.csdnimg.cn/img_convert/5649f3bd507fd641de902905ab69c7f7.png" alt="5649f3bd507fd641de902905ab69c7f7.png">
- 项目主页：https://agentgpt.reworkd.ai/- GitHub 地址：https://github.com/reworkd/AgentGPT
AgentGPT 允许你为自定义 AI 命名，让它执行任何想要达成的目标。自定义 AI 会思考要完成的任务、执行任务并从结果中学习，试图达成目标。如下为 demo 示例：HustleGPT，设置目标为创立一个只有 100 美元资金的初创公司。

<img src="https://img-blog.csdnimg.cn/img_convert/4a4c8691effd6e21d4659442c588f6df.gif" alt="4a4c8691effd6e21d4659442c588f6df.gif">

再比如 PaperclipGPT，设置目标为制造尽可能多的回形针。

<img src="https://img-blog.csdnimg.cn/img_convert/7b265cc44d434716bb6e17612c2c7bf9.gif" alt="7b265cc44d434716bb6e17612c2c7bf9.gif">

不过，用户在使用该工具时，同样需要输入自己的 OpenAI API 密钥。AgentGPT 目前处于 beta 阶段，并正致力于长期记忆、网页浏览、网站与用户之间的交互。

GPT 的想象力空间还有多大，我们继续拭目以待。
- - - - - 