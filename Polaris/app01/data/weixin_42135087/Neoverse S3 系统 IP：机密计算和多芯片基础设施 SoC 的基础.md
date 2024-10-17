
--- 
title:  Neoverse S3 系统 IP：机密计算和多芯片基础设施 SoC 的基础 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/direct/cd946a04fe2d41f38b3f2e8d070fcd67.png" alt="在这里插入图片描述">

### 第三代Neoverse系统IP

Neoverse S3 产品推出了我们的第三代基础设施特定系统 IP，这是下一代基础设施 SOC 的理想基础，适用于从 HPC 和机器学习到 Edge 和 DPU 的各种应用。S3 机箱专注于为我们的合作伙伴提供 Chiplet、机密计算等关键创新以及 UCIe、DDR5、CXL 3.1 和 PCIe Gen5/Gen6 等行业标准的现成功能。Neoverse S3 提供了一套系统 IP，可提供新的可组合性、增加的 IO 吞吐量和增强的安全性。Neoverse S3 产品的主要特点包括：
- Arm RME 通过设备分配进行机密计算，并符合行业标准 DPE，以实现“使用中”数据保护- 针对 PCIe Gen6、CXL 3.1、DDR5 和 HBM3 的升级 IO 和内存系统- 通过UCIe与AMBA CHI C2C进行标准化 Chiplet 接口，并使用定义的 Chiplet 开发套件与 Arm 计算配对
### 启用机密计算

<img src="https://img-blog.csdnimg.cn/direct/cf649d8e9c8f4976a3a09df05d1e87aa.png" alt="在这里插入图片描述">

安全性是涉及 SoC 中所有 IP 的系统级问题。加密已用于安全存储或传输数据多年。这称为保护“静态”或“传输中”的数据。最新的基于硬件的安全改进是在内存中“使用”数据时保护数据。加密内存中数据的行业术语是机密计算。Armv9 架构使用我们称为“领域管理扩展”或 RME 的硬件技术来支持Arm 机密计算架构。Neoverse S3产品率先支持RME，使Arm Neoverse V3内核能够支持完全加密的云虚拟机。

PCIe 和 CXL 连接外围设备（例如 NIC 或加速器）等 IO 设备是潜在的安全威胁。Neoverse S3 系统 IP 确保外部连接设备仅查看允许的内存，而不影响应用程序性能。这是通过一种称为“设备分配”的技术来完成的，该技术允许外围设备通过 DMA（直接将数据传输到内存）到加密内存中。除了安全优势之外，这还允许连接的设备共享数据，同时绕过繁重的软件层，从而大大增强 I/O 性能。

这种将高效通用计算与高性能工作负载加速器连接起来的基本功能是 Arm 最新 Neoverse 计算子系统 (CSS) 产品Neoverse CSS V3和Neoverse CSS N3的核心 。CSS 产品旨在帮助 Arm 合作伙伴更快、更高效、以更低的成本向市场提供工作负载优化的定制芯片。Microsoft Azure Cobalt 100 CPU 是由 Neoverse CSS 支持的新硬件/软件共同开发模型的成果。这些 CSS 产品代表了基于 Arm Neoverse 的解决方案的未来，因为我们作为一个行业和生态系统的长期目标是实现更低成本、可重复使用的基于 Arm 的小芯片。而这一切，如果没有无名英雄Neoverse S3系统IP作为基础，都是不可能实现的。

### 支持行业标准和 Chiplet

<img src="https://img-blog.csdnimg.cn/direct/acc1351445424fa6830f260b855c4a98.png" alt="在这里插入图片描述">

PCIe Gen5/Gen6、CXL 3.1、UCIe 和 DDR5 等行业标准是每个基础设施类 SoC 的关键。不幸的是，正确实施这些标准并非易事。在 Neoverse S3 一代中，Arm 完成了许多繁重的工作来支持这些标准，包括与控制器和 PHY 等关键第三方 IP 的互操作性测试。Neoverse 为我们的合作伙伴提供了这些行业标准的现成功能，以便他们能够专注于差异化和专业化。

技术进步变得极其昂贵，而且并非设计物理的所有方面都在同等程度地扩展。这基本上意味着只有系统的某些方面（例如：CPU）可以有意义地利用技术进步。Chiplet 能够将片上系统 (SoC) 分解为封装系统 (SoaP)，从而能够经济地采用不同的技术节点来构建系统。SoaP 支持模块化来创建解决方案，从而在不同的解决方案中分摊小芯片开发的成本。

不过，这种模块化不应以破坏架构或软件复杂性为代价。Arm Neoverse 解决方案支持使用带有预定义小芯片配置文件的标准化接口的小芯片。这使得 Arm Neoverse 生态系统中的各个芯片供应商能够构建与 Neoverse CSS 兼容的芯片。Chiplet 标准包括：

AMBA CHI C2C 涵盖了跨 SoaP sysbsystems 物理传输位的应用程序和链路层协议。 Arm Chiplet 系统架构涵盖了定义地址转换、中断处理、系统管理、安全方面的架构合规性 Arm 基础系统架构满足标准软件的需求 为了进一步加速 AMBA CHI C2C 和 Chiplet 的采用，Arm 提供了基于 Neoverse S3 机箱的 Chiplet 设计套件。该设计套件为 IO 相干和完全相干加速或分解小芯片奠定了基础。

### Neoverse CSS 和定制芯片的基础

<img src="https://img-blog.csdnimg.cn/direct/4c6688d578344951ab01b821b52b88f3.png" alt="在这里插入图片描述">

Neoverse S3 系列由Neoverse CMN S3 、Neoverse MMU S3 和 Neoverse NOC S3组成，它们共同构成了一个强大且经过验证的平台，供合作伙伴构建其 SOC。

CMN S3 建立在 CMN-700 IP 的基础上，形成了连贯的高速公路，为性能更高、数据需求更高的 Neoverse CPU 提供支持。CMN S3 支持机密计算，专为新的小芯片世界而构建，同时提高了性能和可扩展性，这是互连的关键。

CMN S3 能够以高性能（高带宽、低延迟）安全地连接 CPU 和加速器芯片，对于开发为现代基础设施提供动力的高能效、经济高效、工作负载优化的 SoC 至关重要。所有领先的云提供商都依赖数据处理单元 (DPU) 从主机 CPU 卸载安全、存储和网络功能。他们还部署和开发 GPU、NPU 和 TPU，以加速现代云软件中的 AI 和 ML 功能。与此同时，电信提供商正在将异构 CPU+加速器 SoC 部署到 5G RAN 和边缘基础设施中。

MMU S3 基于我们的行业标准 MMU-700 IP 构建，为片上、小芯片和附加卡应用提供高性能、机密计算感知和 PCIeG6/CXL3.1 就绪 IO 内存管理单元。

NOC S3 是我们基于 NI-700 构建的新型非相干互连，NOC S3 专为 IO 相干加速芯片而构建，它使合作伙伴能够以与合作伙伴习惯于基于片上 AMBA 的设计相同的轻松性和性能来构建分解的 SOC 。

Neoverse S3 产品是我们的第三代 Neoverse 系统 IP，它们构成了我们的CSS V3和CSS N3的基础。该平台支持构建从云服务到边缘 DPU 的世界级基础设施 SOC 所需的基本功能。该平台符合关键行业标准，是行业标准。S3 将为我们的合作伙伴提供机密计算和小芯片现成的功能，以便将其纳入他们的下一代创新定制芯片中。
