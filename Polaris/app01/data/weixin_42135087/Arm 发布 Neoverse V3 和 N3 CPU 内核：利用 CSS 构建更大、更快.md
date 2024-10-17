
--- 
title:  Arm 发布 Neoverse V3 和 N3 CPU 内核：利用 CSS 构建更大、更快 
tags: []
categories: [] 

---
>  
 <font color="purple" size="5">**快速链接:**</font> .   
 -  <font color="red" size="3">**【购买须知】:**</font>- -  ----<font color="red" size="3">**联系方式-加入交流群**</font> 


<img src="https://img-blog.csdnimg.cn/cd0de6cd4f0d4196a4c5a00bfd51c433.png" alt="在这里插入图片描述">

5 年前， Arm 宣布了针对服务器、云和基础设施 CPU 内核的Neoverse 计划。该公司加倍努力大举进军基础设施 CPU 市场，制定了一项雄心勃勃的多年计划，开发三重 CPU 核心阵容，以满足市场的不同细分市场——从以强大的V系列为核心，以娇小的E系列为核心。虽然事情的发展与 Arm 最初的预期略有不同，但他们几乎没有什么可抱怨的，因为 Neoverse 系列 CPU 内核从未像现在这样成功。基于 Neoverse 核心的定制 CPU 设计在云提供商中非常流行，更广泛的基础设施市场也出现了自己的激增。

现在，随着公司及其客户转向 2024 年，由于对 AI 硬件的需求不断增长，计算市场正处于另一次变革的阵痛之中，Arm 正准备向客户发布其下一代 Neoverse CPU 核心设计。在此过程中，该公司正在达到最初 Neoverse 路线图的顶峰。 <img src="https://img-blog.csdnimg.cn/direct/45e94eea0e5c4df4909cf919bcff2d9a.png" alt="在这里插入图片描述">

今天上午，该公司揭开了用于高性能系统的 V3 CPU 架构（代号为 Poseidon）以及用于平衡系统的 N3 CPU 架构（代号为 Hermes）的面纱。这些设计现在可供客户开始集成到他们自己的芯片设计中，同时提供单独的 CPU 内核设计以及更大的计算子系统 (CSS)。在 IP 配置的各种组合之间，Arm 希望为每个人提供一些东西，尤其是那些希望集成现成的 IP 以快速周转开发自己的芯片的芯片设计人员。

话虽如此，应该指出的是，今天的公告也比我们对 Neoverse 之前公告的预期要轻松。Arm 今天没有发布新 Neoverse 平台的任何深层架构细节，因此，虽然我们拥有硬件的高级详细信息和一些基本的性能估计，但 CPU 内核及其相关管道的底层细节是 Arm 的东西直到稍后的时间为止。

### Neoverse V3：多达 128 个核心，采用 CXL 3.0 和 HBM3，加上 CSS 设计

首先从 Neoverse 平台的高端架构 V3 CPU 内核开始。Neoverse V3 之前在 Arm 的路线图中被列为“V-Next”，其代号为 Poseidon，它是 Arm 原始 Neoverse 路线图中的最终架构设计，Arm 将最终实现他们很久以前的设想。

Neoverse V 内核传统上源自 Cortex-X 设计，虽然 Arm 目前没有透露这一级别的细节，但没有理由相信这种情况发生了变化。我怀疑我们正在研究的 CPU 核心设计大量借鉴了 Cortex-X5（Arm 的下一代 Cortex-X 设计），以分别与 V1 和 V2 的 X1 和 X3 的使用保持一致。但这肯定是我的一个假设。

<img src="https://img-blog.csdnimg.cn/direct/136ba49ea3744e7e88d323c526704ebe.png" alt="在这里插入图片描述">

无论如何，与之前的 V 系列 CPU 内核一样，V3 面向最高性能的应用程序，提供所有 Arm Neoverse CPU 内核中最高的单线程性能。单个芯片上最多有 64 个核心，单个插槽上有两个芯片/128 个核心，V3 旨在像之前的 V2 一样参与高端竞争。

Arm 尚未提供 CPU 内核的通用性能估计，但在模拟中，他们发现大多数工作负载的性能在 10% 到 20% 之间，除了 AI 数据分析的边缘情况（强调“分析”而不是“人工智能”）。回到 Arm 最早的路线图，这低于他们最初目标的 30% 逐代改进，但话又说回来，V2 当时甚至没有出现在这些路线图上，因此 Arm 的步伐变得越来越小，更频繁一点。

<img src="https://img-blog.csdnimg.cn/direct/eb8290056ebc4f6ebb167b7a259c5c93.png" alt="在这里插入图片描述">

同样，我们这里没有任何深入的架构细节，但我们确实有一些 V3 带来的变化的高级细节。例如，Arm 在多个方面将大量精力集中在网状织物上。V3 本身改进了与 Arm 网状织物的连接方式，以减轻那里的压力。网状织物本身是新的，用新的 CMN-S3 取代了 Arm 久经考验的 CMN-700——尽管我们没有关于后者的更多细节。

否则，V3 及其 CSS 对应项将支持所有最新的 I/O 和内存格式。通过 I/O，CXL 支持已从 CXL 2.0 提升到CXL 3.0 – 仍然位于 PCIe 5.0 之上。同时在内存方面，LPDDR5、DDR5 和 HBM3 均支持 Arm 的 IP。

Arm 首次针对 V 系列 CPU 内核提供该 IP 的现成 CSS 版本，以便快速集成到客户芯片设计中。尽管CSS计划本身仍然相当新，但Arm表示，该策略已被证明非常成功，像微软（Cobalt 100）这样饥渴且资金充足的云服务提供商迅速采用它，以便快速整合自己的芯片设计，硬件投入使用。因此，Arm 希望为高性能客户带来同样水平的简单性，特别是那些只需要经过验证的 CPU IP 模块来与其定制加速器设计配对的客户，Arm 甚至提供一套现成的芯片到芯片连接以进一步简化流程。

<img src="https://img-blog.csdnimg.cn/direct/99752f51ac3642fc937bf5ca261204aa.png" alt="在这里插入图片描述">

虽然这是在本月早些时候在技术上宣布的，但 V3 CSS 设计与 Arm 建立自己的 Chiplet 生态系统——Arm Chiplet 系统架构 (CSA) 的努力密切相关。CSA 计划旨在让客户能够更轻松地在其产品中混合和匹配小芯片，CSA 不仅限于协议兼容性，还解决系统管理、DMA、安全性和软件兼容性等问题。

<img src="https://img-blog.csdnimg.cn/direct/8ba7e8bf809f4840b7c058f4332c3cf7.png" alt="在这里插入图片描述">

最后，为了强调 Arm 所设想的 V3 CSS IP 的快速周转时间，该公司已经宣布赢得 Socionext 的设计，Socionext 正在设计一款 32 核 V3 CSS 小芯片，将在台积电 (TSMC) 生产。

### Arm Neoverse N3：每瓦性能提高 20%，最多 32 个内核

今天 Neoverse IP 发布的另一部分是 Neoverse N3（代号 Hermes），它是 Arm 平衡、高能效 CPU 内核系列中的最新产品，适用于各种市场。 <img src="https://img-blog.csdnimg.cn/direct/c5913caf63d044abab8f0b3c6a6eb4bb.png" alt="在这里插入图片描述">

这次更加关注他们的 CSS IP，N3 CSS 设计支持一系列 CPU 内核，从 8 到 32 个。对于后者，Arm 表示他们的设计可以低至 40W TDP 运行，或者每个 CPU 核心功耗略高于 1 瓦——尽管该公司没有透露这是什么流程节点。

总的来说，Arm 宣称 N3 CSS 的每瓦性能比 N2 CSS 平均提高了 20%。总体性能改进通常在 10% 到 30% 之间，具体取决于特定的工作负载。

与 V3 一样，Arm 在此并未提供太多架构细节。但由于 N 系列设计历来与 Cortex-A7xx 系列共享大量设计元素，因此最终发现 N3 也有相同的设计元素我不会感到惊讶。

与此同时，Arm 简要介绍了 N3 CSS 的内部情况，以解释其在基于 XGBoost 库的 AI 数据分析方面的巨大性能飞跃。

<img src="https://img-blog.csdnimg.cn/direct/67f406b182a8448fb9a076cd4ac5b2f7.png" alt="在这里插入图片描述">

首先，N3 CSS 的 L2 缓存大小现在为每个核心 2MB，而 N2 的 L2 缓存大小为 1MB。事实上，Arm 还在其整体缓存和内存子系统上花费了相当多的精力，包括对其一致的主机接口进行了一些未公开的调整，以更好地管理 CPU 内核和末级缓存（及更高级别）之间的流量和内存带宽。 。尽管尚不清楚 N3 是否也使用 Arm 的新 CMN-S3 网格，或者是否仅限于 V3。同时，在 N3 的前端，CPU 核心具有更准确的分支预测单元。

总而言之，这些改进以及更多改进使 Arm 的 XGBoost 性能提高了 196%，同样，V3 CPU 内核在相同工作负载下的性能提高了 84%。这使得数据分析/XGBoost 总体上成为一个极端的异常值，但它确实表明了 Arm 在即将到来的一代 CPU 架构上投入了一些努力。

除了这些核心改进之外，N3 还具有 V3 也获得的许多 I/O 和内存改进。Arm 尚未提供详细列表，但我们被告知它支持最新的 PCIe 和 CXL 标准 - 这可能分别是 PCIe 5.0 和 CXL 3.0。值得注意的是，Arm 之前的路线图已将这一代硬件固定为支持 PCIe 6.0，但由于没有进入 V3，看起来 Arm 不得不退一步。

最后，与 V3 CSS 一样，N3 CSS 也具有芯片间互连功能。尽管与 N 系列硬件的大多数其他方面一样，它已缩小为单个互连。因此，芯片供应商可以选择将 N3 直接集成到他们的芯片设计中，或者将其连接到外部加速器小芯片。

### 展望未来：Adonis, Dionysus, and Lycius

最后，随着 Arm 目前的 Neoverse 路线图已经结束，该公司正在为未来的 CPU 核心版本提供路线图。 <img src="https://img-blog.csdnimg.cn/direct/f9f2461d483e4e21a29d331e04e821b5.png" alt="在这里插入图片描述">

值得注意的是，与 Arm 的V2/N2 时代路线图相比，这是一个不太详细的路线图，其中包括一些关于预计将出现哪些技术的高级说明。相反，该路线图只提供了代号，仅此而已。

确认 Arm 正在开发第四代版本的 E、N 和 V CPU 内核，我们总体上有几个新的代号。Lycius将是下一个Neoverse E系列核心（E4？），而Dionysus将是下一个N系列核心，Adonis是下一个V系列核心。与此同时，他们所尊敬的计算子系统也获得了代号，分别为 N 系列 CSS 和 V 系列 CSS 的 CSS Ranger 和 CSS Vega。

目前，Arm 并未就这些设计何时为客户做好准备提供任何指导。但随着 V3/N3 IP 刚刚向客户推出，第四代 Neoverse IP 可能会在几年后出现。
