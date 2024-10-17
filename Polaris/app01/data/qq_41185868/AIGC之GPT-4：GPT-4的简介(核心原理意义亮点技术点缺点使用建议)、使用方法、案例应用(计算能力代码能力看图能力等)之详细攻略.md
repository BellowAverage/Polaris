
--- 
title:  AIGC之GPT-4：GPT-4的简介(核心原理/意义/亮点/技术点/缺点/使用建议)、使用方法、案例应用(计算能力/代码能力/看图能力等)之详细攻略 
tags: []
categories: [] 

---
AIGC之GPT-4：GPT-4的简介(核心原理/意义/亮点/技术点/缺点/使用建议)、使用方法、案例应用(计算能力/代码能力/看图能力等)之详细攻略



>  
 **<strong>解读**</strong>：在2022年11月横空出世的ChatGPT，打遍天下无敌手的时候，就知道会有这么一天，知道它会来，也知道它一定来，但是，还是没想到，来的是这么的快。就在2023年3月15日凌晨(博主是在今天1点多收到的OpenAI的官方邮件信息)，OpenAI的CEO Sam Altman以直播的形式发布了GPT-4。正如Sam Altman所说，这是GPT-4，迄今为止我们最强大的模型。它今天可以在我们的API(等待列表)和ChatGPT+中使用。它仍然有缺陷，仍然有局限性，第一次使用时，它似乎比你用了更多时间后更令人印象深刻。但是，敲重点，根据GPT-4的发布会可知，OpenAI对GPT-4的训练其实已经于2022年8月完成，近半年多的时间都在做微调提升，以及去除危险内容生成的工作，这是最令博主诧异的，这特么个东西竟然在去年8月份就存在了(细思极恐)。当然，最牛叉的模型往往用最朴素的方法，GPT-4科技报告中的7个表格和9张图片，进行了各种横向和纵向比较，能打的一个都没有，它仿佛时刻在低调地说我是目前整个业界最牛逼的AGI模型……嗯，这话的确不是吹的。 随着GPT-4的出世，接下来，会出现官方API的有偿开放，国内外一系列开源社区的争先模仿，大概率预示着2023年，正式步入了从AI无处不在→AI无处不用的时代，走出了实验室，正在走进寻常百姓家，走进你和我和Ta… 最后，GPT4今天凌晨空降，恰好百度文心一言第二天要发布国内首个类ChatGPT模型，嗯，估计发布者已经在连夜修改PPT了…… 




**目录**























































**<strong>相关文章**</strong>

AIGC：ChatGPT(一个里程碑式的对话聊天机器人)的简介(意义/功能/核心技术等)、使用方法(七类任务)、案例应用(提问基础性/事实性/逻辑性/创造性/开放性的问题以及编程相关)之详细攻略



Paper：《GPT-4 Technical Report》的翻译与解读





## **<strong><strong>GPT-4的简介**</strong></strong>

<img alt="" height="525" src="https://img-blog.csdnimg.cn/b2bd91cf8c9f48b497e2cf6a30586e07.png" width="456">
<td style="vertical-align:top;width:34.7pt;"> **<strong>官方总结**</strong> </td><td style="vertical-align:top;width:391.4pt;"> 我们已经创建了GPT-4，这是OpenAI在扩大深度学习方面的最新里程碑。GPT-4是一个大型多模态模型(接受图像和文本输入，输出文本)，虽然在许多现实场景中不如人类，但在各种专业和学术基准上表现出与人类相当的性能。 </td>

我们已经创建了GPT-4，这是OpenAI在扩大深度学习方面的最新里程碑。GPT-4是一个大型多模态模型(接受图像和文本输入，输出文本)，虽然在许多现实场景中不如人类，但在各种专业和学术基准上表现出与人类相当的性能。
<td style="vertical-align:top;width:34.7pt;"> **<strong>简介**</strong> </td><td style="vertical-align:top;width:391.4pt;"> GPT-4是一个超大的多模态模型，它的输入可以是文字（上限约2.4万单词），还可以是图像。由于其更广泛的常识和先进的推理能力，它可以比我们之前的任何模型更准确地解决难题。 </td>

GPT-4是一个超大的多模态模型，它的输入可以是文字（上限约2.4万单词），还可以是图像。由于其更广泛的常识和先进的推理能力，它可以比我们之前的任何模型更准确地解决难题。
<td style="vertical-align:top;width:34.7pt;"> **<strong>核心原理**</strong> </td><td style="vertical-align:top;width:391.4pt;"> GPT-4依旧是一个基于Transformer风格的预训练模型，用于预测文档中的下一个token，使用公开可用数据(如互联网数据)和第三方提供商授权的数据，利用人类反馈的强化学习(RLHF)对模型进行微调。 </td>

GPT-4依旧是一个基于Transformer风格的预训练模型，用于预测文档中的下一个token，使用公开可用数据(如互联网数据)和第三方提供商授权的数据，利用人类反馈的强化学习(RLHF)对模型进行微调。
<td style="vertical-align:top;width:34.7pt;"> **<strong>意义**</strong> </td><td style="vertical-align:top;width:391.4pt;"> 在各种专业和学术基准上，GPT-4性能水平和人类相当！ 比如模拟律师考试，GPT-4取得了前10%的好成绩，相比之下GPT-3.5却是倒数10%； 再比如做美国高考SAT试题，GPT-4也在阅读写作中拿下710分高分、数学700分（满分800）。 </td>

在各种专业和学术基准上，GPT-4性能水平和人类相当！

再比如做美国高考SAT试题，GPT-4也在阅读写作中拿下710分高分、数学700分（满分800）。
<td style="vertical-align:top;width:34.7pt;"> **<strong>亮点**</strong> </td><td style="vertical-align:top;width:391.4pt;"> (1)、多模态特性：强大的识图能力，可以接受图像输入并理解图像内容； (2)、更长的上下文：可以接受的文字输入长度也增加到3.2万个token（约2.5万个单词文本）； (3)、针对问题基于提示可以利用不同的风格进行回答； (4)、更加真实性、可控性：OpenAI 花了 6 个月的时间使用对抗性测试程序和 ChatGPT 的经验教训对 GPT-4 进行迭代调整； </td>

(1)、多模态特性：强大的识图能力，可以接受图像输入并理解图像内容；

(3)、针对问题基于提示可以利用不同的风格进行回答；
<td style="vertical-align:top;width:34.7pt;"> **<strong>技术点**</strong> </td><td style="vertical-align:top;width:391.4pt;"> GPT-4**依旧设置技术壁垒**，目前还没有公布具体模型架构、硬件、训练计算、数据集构造、训练方法的具体细节。 (1)、GPT-4依旧利用强化学习人类反馈 (RLHF) 来微调模型的行为：聘请了来自长期AI一致性/对齐风险、网络安全、生物风险和国际安全等领域的50多名专家对模型进行对抗性测试； (2)、GPT-4的两个技术点提高安全性：一套额外的安全相关RLHF训练提示，以及基于规则的奖励模型(RBRMs)。通过训练模型拒绝对此类内容的请求来减少有害的输出。 (3)、OpenAI 基于Azure从头开始设计了一台超级计算机，并重建了整个深度学习堆栈； (4)、OpenAI开源了 OpenAI Evals—自动评估 AI 模型性能的框架，主要是为了让所有人都可以指出其模型中的缺点，来帮助 OpenAI 进一步改进模型。它被用于创建和运行基准测试以评估 GPT-4 等模型，同时可以逐样本地检查模型性能； (5)、模型训练到部署的庞大的团队工程能力：单看报告致谢的部分，就包括了几百人。预训练模块、长上下文模块、视觉模块、强化学习与对齐模块、评估与分析模块、部署模块等工程化的各个阶段，均装备了核心负责人小组、计算集群扩展小组、数据小组、分布式训练基础设施小组、硬件正确性小组、优化与架构小组、模型训练小组团队。 </td>

GPT-4**依旧设置技术壁垒**，目前还没有公布具体模型架构、硬件、训练计算、数据集构造、训练方法的具体细节。

(2)、GPT-4的两个技术点提高安全性：一套额外的安全相关RLHF训练提示，以及基于规则的奖励模型(RBRMs)。通过训练模型拒绝对此类内容的请求来减少有害的输出。

(4)、OpenAI开源了 OpenAI Evals—自动评估 AI 模型性能的框架，主要是为了让所有人都可以指出其模型中的缺点，来帮助 OpenAI 进一步改进模型。它被用于创建和运行基准测试以评估 GPT-4 等模型，同时可以逐样本地检查模型性能；
<td style="vertical-align:top;width:34.7pt;"> **<strong>缺点**</strong> </td><td style="vertical-align:top;width:391.4pt;"> (1)、幻觉不可靠性：GPT-4与早期GPT模型有相似的局限性：它仍然不完全可靠，它会“产生幻觉”事实，但已经比ChatGPT减轻了这一缺点。 (2)、依旧存在错误推理的可能性： (3)、依旧会产生有害的建议：但通过50位领域专家的反馈对模型进行了改进； (4)、存在偏差性：GPT-4在输出中依旧存在各种偏差； (5)、GPT-4上下文窗口有限； (6)、GPT-4不能从经验中学习； (7)、GPT-4会在生成的代码中引入安全漏洞； </td>

(1)、幻觉不可靠性：GPT-4与早期GPT模型有相似的局限性：它仍然不完全可靠，它会“产生幻觉”事实，但已经比ChatGPT减轻了这一缺点。

(3)、依旧会产生有害的建议：但通过50位领域专家的反馈对模型进行了改进；

(5)、GPT-4上下文窗口有限；

(7)、GPT-4会在生成的代码中引入安全漏洞；
<td style="vertical-align:top;width:34.7pt;"> **<strong>使用方法**</strong> </td><td style="vertical-align:top;width:391.4pt;"> (1)、可以继续沿用ChatGPT，只不过这次是ChatGPT Plus版本，即ChatGPT已加持GPT-4； (2)、目前可以调用官方发布GPT-4的API； (3)、可以借助Microsoft 的Bing搜索使用GPT-4功能； </td>

(1)、可以继续沿用ChatGPT，只不过这次是ChatGPT Plus版本，即ChatGPT已加持GPT-4；

(3)、可以借助Microsoft 的Bing搜索使用GPT-4功能；
<td style="vertical-align:top;width:34.7pt;"> **<strong>使用建议**</strong> </td><td style="vertical-align:top;width:391.4pt;"> 要想最大程度发挥GPT-4的能力，最好还是用上思维链路提示（Chain-of-thought Prompt）：就是需在提问的时候额外提醒AI给出步骤，就能大大提高推理和计算的准确率。 </td>

要想最大程度发挥GPT-4的能力，最好还是用上思维链路提示（Chain-of-thought Prompt）：就是需在提问的时候额外提醒AI给出步骤，就能大大提高推理和计算的准确率。

**<strong>官网地址**</strong>：

**<strong>直播视频**</strong>：





### **GPT-4****模型可使用版本**
<td style="vertical-align:top;width:79.95pt;"> **<strong>最新模型**</strong> </td><td style="vertical-align:top;width:192.55pt;"> **<strong>描述**</strong> </td><td style="vertical-align:top;width:83.45pt;"> **<strong>最大TOKENS**</strong> </td><td style="vertical-align:top;width:70.15pt;"> **<strong>训练数据**</strong> </td>

**<strong>描述**</strong>

**<strong>训练数据**</strong>
<td style="vertical-align:top;width:79.95pt;"> gpt-4 </td><td style="vertical-align:top;width:192.55pt;"> 比任何GPT-3.5模型更强大，能够完成更复杂的任务，并为聊天进行了优化。将与我们最新的模型迭代更新。 </td><td style="vertical-align:top;width:83.45pt;"> 8,192 tokens </td><td style="vertical-align:top;width:70.15pt;"> 截至2021年9月 </td>

比任何GPT-3.5模型更强大，能够完成更复杂的任务，并为聊天进行了优化。将与我们最新的模型迭代更新。

截至2021年9月
<td style="vertical-align:top;width:79.95pt;"> gpt-4-0314 </td><td style="vertical-align:top;width:192.55pt;"> 2023年3月14日的gpt-4快照。与gpt-4不同的是，该模型将不会接受更新，并且只会在2023年6月14日结束的三个月内得到支持。 </td><td style="vertical-align:top;width:83.45pt;"> 8,192 tokens </td><td style="vertical-align:top;width:70.15pt;"> 截至2021年9月 </td>

2023年3月14日的gpt-4快照。与gpt-4不同的是，该模型将不会接受更新，并且只会在2023年6月14日结束的三个月内得到支持。

截至2021年9月
<td style="vertical-align:top;width:79.95pt;"> gpt-4-32k </td><td style="vertical-align:top;width:192.55pt;"> 与基础gpt-4模式相同的功能，但上下文长度是它的4倍。将与我们最新的模型迭代更新。 </td><td style="vertical-align:top;width:83.45pt;"> 32,768 tokens </td><td style="vertical-align:top;width:70.15pt;"> 截至2021年9月 </td>

与基础gpt-4模式相同的功能，但上下文长度是它的4倍。将与我们最新的模型迭代更新。

截至2021年9月
<td style="vertical-align:top;width:79.95pt;"> gpt-4-32k-0314 </td><td style="vertical-align:top;width:192.55pt;"> 2023年3月14日gpt-4-32的快照。与gpt-4-32k不同的是，该型号将不接受更新，并且只支持三个月的时间，截止2023年6月14日。 </td><td style="vertical-align:top;width:83.45pt;"> 32,768 tokens </td><td style="vertical-align:top;width:70.15pt;"> 截至2021年9月 </td>

2023年3月14日gpt-4-32的快照。与gpt-4-32k不同的是，该型号将不接受更新，并且只支持三个月的时间，截止2023年6月14日。

截至2021年9月

**<strong>表格地址链接**</strong>：







### **GPT-4****模型对比**** GPT-3.5 **

对于许多基本任务，GPT-4和GPT-3.5模型之间的差异并不显著。然而，在更复杂的推理情况下，GPT-4比我们之前的任何模型都更有能力。

#### **<strong><strong>GPT-4 比 GPT-3.5 更可靠、更有创意，并且能够处理更细微的指令**</strong></strong>

<img alt="" height="299" src="https://img-blog.csdnimg.cn/f4233787b95542e785e49d40bc13a13a.png" width="550">



#### **<strong><strong>GPT-4在为机器学习模型设计的传统基准上**</strong>**<strong>优于大多数 SOTA 模型**</strong></strong>

<img alt="" height="792" src="https://img-blog.csdnimg.cn/d51f4b82832b43b1b738fe0f8792ff2f.png" width="650">

 GPT-4 基本模型在此任务上仅比 GPT-3.5 略好；使用强化学习人类反馈 (RLHF) 来微调模型的行为，在经过 RLHF 后训练之后，GPT-4模型性能飞跃提升。



#### **<strong><strong>GPT-4 在学术和专业考试中的表现优秀**</strong></strong>

<img alt="" height="597" src="https://img-blog.csdnimg.cn/7ddaeafc0ccf4f51aa1ee81c960dcc5c.png" width="649">





#### **<strong><strong>GPT-4 在**</strong>**<strong>基于**</strong>**<strong>MMLU基准**</strong>**<strong>的**</strong>**<strong>其他语言上能力**</strong>**<strong>也表现惊艳**</strong></strong>

<img alt="" height="691" src="https://img-blog.csdnimg.cn/83003fa72f494857a255cbee31e2a27c.png" width="582">



#### **<strong><strong>GPT-4 在 TruthfulQA 等外部基准测试方面也取得了进展**</strong></strong>

与之前的 GPT 模型一样，GPT-4 基础模型经过训练可以预测文档中的下一个单词，

<img alt="" src="https://img-blog.csdnimg.cn/91591788bffe4377a99d4cfe78e28f88.png">







### **GPT-4 System Card****简介**

**<strong>GPT-4 System Card**</strong>：

大型语言模型(LLMs)被部署在我们生活的许多领域，从浏览、语音助手到编码辅助工具，并有可能产生巨大的社会影响。此system card系统卡分析GPT-4, GPT系列模型中最新的LLM。首先，我们强调了模型的局限性(例如，产生令人信服的巧妙错误文本)和能力(例如，提供非法建议的熟练程度提高，双重用途功能的性能和危险的紧急行为)所带来的安全挑战。其次，我们对OpenAI用于准备GPT-4部署的安全流程进行了高层概述。这涵盖了我们的工作，包括测量、模型级别的更改、产品和系统级别的干预(如监测和政策)以及外部专家的参与。最后，我们证明，虽然我们的缓解措施和流程改变了GPT-4的行为，并防止某些类型的误用，但它们是有限的，在某些情况下仍然很脆弱。这表明需要有预见性的规划和治理。





## **<strong><strong>GPT-4的使用方法**</strong></strong>

**<strong>地址**</strong>：

**<strong>GPT-4 API waitlist**</strong>**<strong>地址**</strong>：

      要想最大程度发挥GPT-4的能力，最好还是用上思维链路提示（Chain-of-thought Prompt）：就是需在提问的时候额外提醒AI给出步骤，就能大大提高推理和计算的准确率。       GPT-4目前处于有限的测试阶段，只有被授予访问权限的人才能访问。当容量可用时，请加入等待列表以获得访问。在获得访问权限后，目前可以向 GPT-4 模型发出纯文本请求，图像能力暂未开放。       价格方面，定价为每 1k 个 prompt token 0.03 美元，每 1k 个 completion token 0.06 美元。默认速率限制为每分钟 40k 个 token 和每分钟 200 个请求。









## **<strong><strong>GPT-4的案例应用**</strong></strong>

### **1、可控性：允许修改“系统提示”**

允许 API 用户在一定范围内定制化实现不同的用户体验，比如以莎士比亚风格或json格式回答

#### **<strong><strong>语气角色扮演**</strong></strong>

通过修改这句话，GPT-4就可以展现出更多样的性格，比如扮演角色





#### **<strong><strong>指定回答形式或者格式**</strong></strong>

也可以指定之后所有回答的形式，比如全用json格式





### **2、计算能力**

#### **<strong><strong>做一**</strong>**<strong>个**</strong>**<strong>法语的**</strong>**<strong>物理题**</strong></strong>

<img alt="" height="729" src="https://img-blog.csdnimg.cn/2deb4314918b4ceb93c9137500419092.png" width="533">





### **3、代码能力**

#### **<strong><strong>给代码修Bug**</strong></strong>

<img alt="" height="314" src="https://img-blog.csdnimg.cn/1ceb00c3c33744a4a1d118245673f7bf.gif" width="669">





### **4、看图能力(预览，能力暂时未公开)**

#### **<strong><strong>看草图绘代码**</strong></strong>

画一个网站的草稿图，拍照片上传给GPT-4，可以立马生成网站的HTML代码

<img alt="" height="322" src="https://img-blog.csdnimg.cn/1768e84232f64be08732f2852ba73eed.gif" width="669">



#### **<strong><strong>解释表情包、解释漫画**</strong></strong>

<img alt="" height="407" src="https://img-blog.csdnimg.cn/dcb2fe0c694944ff931b1904d8c215dd.png" width="549">







#### **<strong><strong>解释梗图**</strong></strong>

<img alt="" height="625" src="https://img-blog.csdnimg.cn/ec902d5c68904a6a822a0ac4154d761f.png" width="493">



#### **<strong><strong>找图中特点**</strong></strong>

<img alt="" height="621" src="https://img-blog.csdnimg.cn/e48ff5436e4242fcaa80588d9347d702.png" width="519">



#### **<strong><strong>理解图表中数据的含义**</strong></strong>

<img alt="" height="603" src="https://img-blog.csdnimg.cn/0eb18c4191f14f71a64529fb20b0ab20.png" width="529">





#### **<strong><strong>根据论文截图总结摘要**</strong></strong>

<img alt="" height="697" src="https://img-blog.csdnimg.cn/030174430d0c4852b9e433edb6ea21f8.png" width="571">










