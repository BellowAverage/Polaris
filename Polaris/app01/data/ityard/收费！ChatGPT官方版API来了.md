
--- 
title:  收费！ChatGPT官方版API来了 
tags: []
categories: [] 

---
来源：SegmentFault思否

3 月 2 日，OpenAI 在官方博客宣布，**开放 ChatGPT 和 Whisper 的模型 API **，用户可将其集成在应用程序等产品中。ChatGPT API 价格为 1k tokens/$0.002，等于每输出 100 万个单词，价格才 2.7 美金（约 18 元人民币），比已有的 GPT-3.5 模型便宜 10 倍。**今天 Open AI 的宣布可能会带来大量应用，一股 AIGC 创业风潮不断吹来。**

<img src="https://img-blog.csdnimg.cn/img_convert/d25b3dd9c7602ada59135ff31f70514c.jpeg" alt="d25b3dd9c7602ada59135ff31f70514c.jpeg">

ChatGPT 的模型 API 地址：https://platform.openai.com/docs/guides/chat

>  
  ChatGPT 和 Whisper 模型现已在我们的 API 上可用，使开发人员能够使用尖端语言（不仅仅是聊天！）和语音转文本功能。通过一系列系统范围的优化，自去年 12 月以来，我们已将 ChatGPT 的成本降低了 90%；我们现在将这些节省的资金转嫁给 API 用户。开发人员现在可以在 API 中使用我们的开源 Whisper large-v2 模型，获得更快且更具成本效益的结果。ChatGPT API 用户可以期待持续的模型改进和选择专用容量以更深入地控制模型的选项。我们还仔细听取了开发人员的反馈并改进了我们的 API 服务条款以更好地满足他们的需求。 
 

ChatGPT 官方 API 基于 GPT-3.5-turbo 模型，是 GPT-3.5 系列中最快速、最便宜、最灵活的模型。开发者可以通过 OpenAI Playground 和 OpenAI Codex 来使用和测试 ChatGPT OpenAI。

此前一些公司已经率先接入 ChatGPT API，包括生鲜电商平台 Instacart、跨境电商平台 Shopify、照片分享应用 Snap、在线学习平台 Quizlet 等，用于提高客户服务、营销、教育等效率及体验。

<img src="https://img-blog.csdnimg.cn/img_convert/0499de697647feeac15d7f0b212eedfb.png" alt="0499de697647feeac15d7f0b212eedfb.png">

**ChatGPT API**

**Model : **OpenAI 今天发布的 ChatGPT 模型系列 gpt-3.5-turbo 与 ChatGPT 产品中使用的模型相同。它的售价为每 1000 个代币 0.002 美元，比 OpenAI 现有的 GPT-3.5 型号便宜 10 倍。对于许多非聊天用例来说，它也是 OpenAI 最好的模型ーー OpenAI 已经看到早期的测试人员从 text-davinci-003 迁移到 gpt-3.5-turbo，只需要对提示进行少量调整。

**API : **传统上，GPT模型消耗非结构化的文本，这些文本在模型中被表示为一连串的 "标记"。而ChatGPT模型则消耗一连串的消息和元数据。(对于好奇的人来说：在引擎盖下，输入仍然被呈现为模型所要消费的 "标记 "序列**。**模型使用的原始格式是一种称为聊天标记语言(Chat Markup Language，“ ChatML”)的新格式。)

<img src="https://img-blog.csdnimg.cn/img_convert/2331059d3769edeee2e51ac210cae96c.png" alt="2331059d3769edeee2e51ac210cae96c.png">

### **ChatGPT 升级**

OpenAI 正在不断改进 ChatGPT 模型，并希望开发人员也可以使用这些增强。使用 gpt-3.5-turbo 模型的开发人员将始终获得 OpenAI 推荐的稳定模型，同时仍然可以灵活地选择特定的模型版本。例如，今天 OpenAI 发布了 gpt-3.5-turbo-0301，它将至少支持到 6 月 1 日，OpenAI 将在 4 月份更新 gpt-3.5-turbo 到一个新的稳定版本。模型页面将提供切换更新。

### **专用实例**

OpenAI 现在还为那些希望对特定模型版本和系统性能进行更深入控制的用户提供专用实例。默认情况下，请求在与其他用户共享的计算基础设施上运行，这些用户按请求付费。OpenAI 的 API 运行在 Azure 上，对于专用实例，开发者将按时间段支付为服务他们的请求而保留的计算基础设施的分配费用。

开发者可以完全控制实例的负载(更高的负载可以提高吞吐量，但会降低每个请求的速度)、启用诸如更长上下文限制等特性的选项，以及固定模型快照的能力。

对于每天运行超过 450M 令牌的开发人员来说，专用实例具有经济意义。此外，它可以根据硬件性能直接优化开发人员的工作负载，这可以显著降低相对于共享基础设施的成本。

**Whisper API**

Whisper，OpenAI 在 2022 年 9 月开源的语音到文本模型，得到了开发者社区的巨大赞誉，但也很难运行。Open AI现在已经通过 API 提供了大型 v2 模型，它提供了方便的按需访问，价格为每分钟 0.006 美元。此外，OpenAI高度优化的服务堆栈确保了比其他服务更快的性能。

Whisper API 可以通过 OpenAI 的转录(转录为源语言)或翻译(转录为英语)端点获得，并接受各种格式(m4a，mp3，mp4，mpeg，mpga，wav，webm) 

<img src="https://img-blog.csdnimg.cn/img_convert/1dabae166e572b13f2d21468c9f39c62.png" alt="1dabae166e572b13f2d21468c9f39c62.png">

### **以开发者为中心**

在收到大量开发者的反馈后，OpenAI 针对开发者方面也做了一些具体的调整。这些变化包括：
- 除非组织同意，否则不得将通过 API 提交的数据用于服务改进，包括模型训练。- 建立默认的 30 天数据保留策略，并根据用户的需要选择更严格的保留。- 改进其开发人员文档。- 简化其服务条款和使用政策。
>  
  在过去的两个月中，我们的正常运行时间没有达到我们自己的期望，也没有达到我们的用户的期望。我们的工程团队现在的首要任务是稳定生产用例ーー我们知道，要确保人工智能造福全人类，就需要成为一个可靠的服务提供商。请让我们为未来几个月的正常运行时间的改善负责！ 
  我们相信，人工智能可以为每个人提供难以置信的机会和经济赋权，实现这一目标的最佳途径是允许每个人利用人工智能进行建设。我们希望，我们今天宣布的变化将导致大量的应用程序，每个人都可以从中受益。开始构建由 ChatGPT &amp; Whisper 驱动的下一代应用程序。 
 
- - - - - 