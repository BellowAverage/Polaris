
--- 
title:  AGI之Agent：《Agent AI: Surveying the Horizons of Multimodal Interaction智能体AI:多模态交互视野的考察》翻译与解读 
tags: []
categories: [] 

---
AGI之Agent：《Agent AI: Surveying the Horizons of Multimodal Interaction智能体AI:多模态交互视野的考察》翻译与解读



>  
 **<strong>导读**</strong>：这篇文章探讨了一种新的多模态**<strong>智能代理**</strong>体系结构，该体系结构可感知视觉刺激、语言输入和其他环境相关数据，并产生有意义的实体动作。 
 &gt;&gt; 文章提出，随着深度学习的发展，语言模型和视觉语言模型在某些任务上显示出超人水平的能力。然而，这些模型通常难以在物理环境中产生实体动作。为此，文章提出了一种**<strong>多模态智能代理框架**</strong>，将语言模型和视觉语言模型纳入一个统一的系统架构中，以产生实体动作。该框架主要包含以下要点: 
 &gt;&gt; ****<strong><em>整合各种感知模块****</em></strong>，例如视觉、语音和传感器输入，以满足环境交互的需求。 
 &gt;&gt; ****<strong><em>基于深度学习算法训练智能代理****</em></strong>，使其可以理解多种模态输入，并生成有意义的实体操作。 
 &gt;&gt; ****<strong><em>提供一个统一的接口****</em></strong>，支持语言、视觉和其他类型的输入，并产生相应的输出。 
 &gt;&gt; ****<strong><em>引入记忆模块****</em></strong>，记录环境交互的历史信息，支持长期规划。 
 &gt;&gt; ****<strong><em>设计一个通用的智能代理转换器结构****</em></strong>，直接使用语言和视觉协处理 Tokens 作为输入，支持端到端训练。 
 &gt;&gt; 将此框架应用于游戏、机器人以及医疗保健等不同领域，验证其广泛适用性。 
 总体来说，该框架的目标是建立一个全面性的多模态**<strong>智能代理**</strong>体系，允许基于深度学习技术整合不同感知模块，生成环境相符的动作，以实现良好的环境交互能力。未来还需要开展额外工作，弥补当前模型在解释能力、公平性和安全性等方面的不足。 






**目录**









































































































































































































































































































































































## **《Agent AI: Surveying the Horizons of Multimodal Interaction智能体AI:多模态交互视野的考察》翻译与解读**
<td style="vertical-align:top;width:33.25pt;"> **<strong>地址**</strong> </td><td style="vertical-align:top;width:392.85pt;"> 论文地址： </td>

论文地址：
<td style="vertical-align:top;width:33.25pt;"> **<strong>时间**</strong> </td><td style="vertical-align:top;width:392.85pt;"> 2024年1月7日 </td>

2024年1月7日
<td style="vertical-align:top;width:33.25pt;"> **<strong>作者**</strong> </td><td style="vertical-align:top;width:392.85pt;"> Zane Durante, Qiuyuan Huang, Naoki Wake, Ran Gong, Jae Sung Park, Bidipta Sarkar, Rohan Taori, Yusuke Noda, Demetri Terzopoulos, Yejin Choi, Katsushi Ikeuchi, Hoi Vo, Li Fei-Fei, Jianfeng Gao 1斯坦福大学;2微软研究院，雷德蒙德; 3加州大学洛杉矶分校;4华盛顿大学;5微软游戏 </td>

Zane Durante, Qiuyuan Huang, Naoki Wake, Ran Gong, Jae Sung Park, Bidipta Sarkar, Rohan Taori, Yusuke Noda, Demetri Terzopoulos, Yejin Choi, Katsushi Ikeuchi, Hoi Vo, Li Fei-Fei, Jianfeng Gao

3加州大学洛杉矶分校;4华盛顿大学;5微软游戏







## **Abstract摘要**

### **<strong>&gt;&gt; 多模态人工智能**</strong>**：多模态人工智能系统将无处不在**

### **&gt;&gt; ****<strong>具身智能体：**</strong>**当前系统以现有基础模型为创建具身智能体的基本构建模块。通过感知用户动作、人类行为、环境物体、音频表达和场景情感，系统可用于引导代理在给定环境中的响应。**

### **<strong>&gt;&gt; 减轻幻觉**</strong>**：通过发展在有根基环境中的具体人工智能系统，可以减轻大型基础模型幻觉和生成环境不正确输出的倾向。**

### **<strong>&gt;&gt; 虚拟现实**</strong>**：Agent工智能这一新兴领域涵盖了多模态交互的更广泛的具体和代理方面，未来人们可轻松创建虚拟现实或模拟场景，并与嵌入虚拟环境中的代理进行互动。**
<td style="vertical-align:top;width:255.25pt;"> Multi-modal AI systems will likely become a ubiquitous presence in our everyday lives. A promising approach to making these systems more interactive is to embody them as agents within physical and virtual environments. At present, systems leverage existing foundation models as the basic building blocks for the creation of embodied agents. Embedding agents within such environments facilitates the ability of models to process and interpret visual and contextual data, which is critical for the creation of more sophisticated and context-aware AI systems. For example, a system that can perceive user actions, human behavior, environmental objects, audio expressions, and the collective sentiment of a scene can be used to inform and direct agent responses within the given environment. To accelerate research on agent-based multimodal intelligence, we define “Agent AI” as a class of interactive systems that can perceive visual stimuli, language inputs, and other environmentally-grounded data, and can produce meaningful embodied action with infinite agent. In particular, we explore systems that aim to improve agents based on next-embodied action prediction by incorporating external knowledge, multi-sensory inputs, and human feedback. We argue that by developing agentic AI systems in grounded environments, one can also mitigate the hallucinations of large foundation models and their tendency to generate environmentally incorrect outputs. The emerging field of Agent AI subsumes the broader embodied and agentic aspects of multimodal interactions. Beyond agents acting and interacting in the physical world, we envision a future where people can easily create any virtual reality or simulated scene and interact with agents embodied within the virtual environment. </td><td style="vertical-align:top;width:170.85pt;"> **<strong>多模态人工智能系统**</strong>可能会在我们的日常生活中无处不在。使这些系统更具互动性的一种有希望的方法是将它们作为物理和虚拟环境中的代理。目前，系统利用现有的基础模型作为创建**<strong>具身智能体**</strong>的基本构建块。在这样的环境中嵌入代理有助于模型处理和解释视觉和上下文数据的能力，这对于创建更复杂和上下文感知的人工智能系统至关重要。例如，可以感知用户动作、人类行为、环境对象、音频表达和场景的集体情感的系统，可以用于通知和指导给定环境中的代理响应。 为了加速基于Agent的多模态智能的研究，我们将“**<strong>Agent AI**</strong>”定义为一类能够感知视觉刺激、语言输入和其他基于环境的数据，并能产生有意义的具有无限Agent的具体动作的交互系统。 特别是，我们探索了旨在通过结合外部知识、多感官输入和人类反馈来改进基于下一体现动作预测的智能体的系统。我们认为，通过在基础环境中开发Agent工智能系统，还可以**<strong>减轻**</strong>大型基础模型的幻觉及其产生环境错误输出的倾向。Agent AI的新兴领域包含了多模态交互的更广泛的具体化和代理方面。 除了代理在物理世界中行动和互动之外，我们设想未来人们可以轻松地创建任何虚拟现实或模拟场景，并与嵌入虚拟环境中的代理进行交互。 </td>

**<strong>多模态人工智能系统**</strong>可能会在我们的日常生活中无处不在。使这些系统更具互动性的一种有希望的方法是将它们作为物理和虚拟环境中的代理。目前，系统利用现有的基础模型作为创建**<strong>具身智能体**</strong>的基本构建块。在这样的环境中嵌入代理有助于模型处理和解释视觉和上下文数据的能力，这对于创建更复杂和上下文感知的人工智能系统至关重要。例如，可以感知用户动作、人类行为、环境对象、音频表达和场景的集体情感的系统，可以用于通知和指导给定环境中的代理响应。

特别是，我们探索了旨在通过结合外部知识、多感官输入和人类反馈来改进基于下一体现动作预测的智能体的系统。我们认为，通过在基础环境中开发Agent工智能系统，还可以**<strong>减轻**</strong>大型基础模型的幻觉及其产生环境错误输出的倾向。Agent AI的新兴领域包含了多模态交互的更广泛的具体化和代理方面。





### **图1:基于不同领域和应用程序中感知和行动的Agent AI系统概述**
<td style="vertical-align:top;width:250.6pt;"> Figure 1: Overview of an Agent AI system that can perceive and act in different domains and applications. Agent AI is emerging as a promising avenue toward Artificial General Intelligence (AGI). Agent AI training has demonstrated the capacity for multi-modal understanding in the physical world. It provides a framework for reality-agnostic training by leveraging generative AI alongside multiple independent data sources. Large foundation models trained for agent and action-related tasks can be applied to physical and virtual worlds when trained on cross-reality data. We present the general overview of an Agent AI system that can perceive and act in many different domains and applications, possibly serving as a route towards AGI using an agent paradigm. </td><td style="vertical-align:top;width:175.5pt;"> 图1:可以在不同领域和应用程序中感知和行动的Agent AI系统概述。Agent工智能(**<strong>Agent AI**</strong>)正在成为通用人工智能(AGI)的一个有前途的途径。AI代理的训练已经证明了在物理世界中进行多模态理解的能力。它通过利用**<strong>生成式人工智能**</strong>以及多个**<strong>独立数据源**</strong>，为现实无关训练提供了一个框架。当在跨现实数据上训练时，为Agent和行动相关任务训练的大型基础模型可以应用于物理和虚拟世界。我们介绍了Agent AI系统的总体概述，该系统可以在许多不同的领域和应用中感知和行动，可能作为使用Agent范式实现AGI的途径。 </td>

图1:可以在不同领域和应用程序中感知和行动的Agent AI系统概述。Agent工智能(**<strong>Agent AI**</strong>)正在成为通用人工智能(AGI)的一个有前途的途径。AI代理的训练已经证明了在物理世界中进行多模态理解的能力。它通过利用**<strong>生成式人工智能**</strong>以及多个**<strong>独立数据源**</strong>，为现实无关训练提供了一个框架。当在跨现实数据上训练时，为Agent和行动相关任务训练的大型基础模型可以应用于物理和虚拟世界。我们介绍了Agent AI系统的总体概述，该系统可以在许多不同的领域和应用中感知和行动，可能作为使用Agent范式实现AGI的途径。

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/direct/3c1778f719734c3db82ff23998988ca5.png" width="1200">





## **1 ****Introduction**

### **1.1 Motivation动机**

#### **人工智能历史演进：从1956年达特茅斯会议定义的AI系统为人工生命形式开始，经历分化和问题解决的过程，但过度简化模糊了AI研究的总体目标。**
<td style="vertical-align:top;width:247.4pt;"> Historically, AI systems were defined at the 1956 Dartmouth Conference as artificial life forms that could collect information from the environment and interact with it in useful ways. Motivated by this definition, Minsky’s MIT group built in 1970 a robotics system, called the “Copy Demo,” that observed “blocks world” scenes and successfully reconstructed the observed polyhedral block structures. The system, which comprised observation, planning, and manipulation modules, revealed that each of these subproblems is highly challenging and further research was necessary. The AI field fragmented into specialized subfields that have largely independently made great progress in tackling these and other problems, but over-reductionism has blurred the overarching goals of AI research. </td><td style="vertical-align:top;width:178.7pt;"> 从历史上看，人工智能系统在1956年达特茅斯会议上被定义为能够从环境中收集信息并以有用的方式与之互动的人工生命形式。受这一定义的启发，明斯基在麻省理工学院的研究小组于1970年建立了一个名为“复制演示”的机器人系统，该系统可以观察“积木世界”场景，并成功地重建了观察到的多面体积木结构。该系统由观察、规划和操作模块组成，表明每个子问题都极具挑战性，需要进一步研究。人工智能领域被分割成专门的子领域，这些子领域在解决这些问题和其他问题方面取得了很大的进展，但过度简化主义模糊了人工智能研究的总体目标。 </td>

从历史上看，人工智能系统在1956年达特茅斯会议上被定义为能够从环境中收集信息并以有用的方式与之互动的人工生命形式。受这一定义的启发，明斯基在麻省理工学院的研究小组于1970年建立了一个名为“复制演示”的机器人系统，该系统可以观察“积木世界”场景，并成功地重建了观察到的多面体积木结构。该系统由观察、规划和操作模块组成，表明每个子问题都极具挑战性，需要进一步研究。人工智能领域被分割成专门的子领域，这些子领域在解决这些问题和其他问题方面取得了很大的进展，但过度简化主义模糊了人工智能研究的总体目标。



#### **重返AI基础与整体主义：为了超越现状，需要回归亚里士多德整体主义的AI基本原理，而近年来大型语言模型（LLMs）和视觉语言模型（VLMs）的革命为此提供了可能性。**
<td style="vertical-align:top;width:247.4pt;"> To advance beyond the status quo, it is necessary to return to AI fundamentals motivated by Aristotelian Holism. Fortunately, the recent revolution in Large Language Models (LLMs) and Visual Language Models (VLMs) has made it possible to create novel AI agents consistent with the holistic ideal. Seizing upon this opportunity, this article explores models that integrate language proficiency, visual cognition, context memory, intuitive reasoning, and adaptability. It explores the potential completion of this holistic synthesis using LLMs and VLMs. In our exploration, we also revisit system design based on Aristotle’s Final Cause, the teleological “why the system exists”, which may have been overlooked in previous rounds of AI development. </td><td style="vertical-align:top;width:178.7pt;"> 为了超越现状，有必要回到由亚里士多德整体主义推动的人工智能基础。幸运的是，最近大型语言模型(llm)和视觉语言模型(vlm)的革命使得创建符合整体理想的新型AI代理成为可能。抓住这个机会，本文探讨了整合语言能力、视觉认知、上下文记忆、直觉推理和适应性的模型。它探讨了使用llm和vlm完成这种整体合成的可能性。在我们的探索中，我们还重新审视了基于亚里士多德最终原因的系统设计，即目的论的“系统存在的原因”，这可能在前几轮人工智能开发中被忽视了。 </td>

为了超越现状，有必要回到由亚里士多德整体主义推动的人工智能基础。幸运的是，最近大型语言模型(llm)和视觉语言模型(vlm)的革命使得创建符合整体理想的新型AI代理成为可能。抓住这个机会，本文探讨了整合语言能力、视觉认知、上下文记忆、直觉推理和适应性的模型。它探讨了使用llm和vlm完成这种整体合成的可能性。在我们的探索中，我们还重新审视了基于亚里士多德最终原因的系统设计，即目的论的“系统存在的原因”，这可能在前几轮人工智能开发中被忽视了。



#### **综合模型的探索与潜在综合：利用LLMs和VLMs，探索整合语言能力、视觉认知、上下文记忆、直觉推理和适应性的模型，并探讨使用这些模型进行整体综合的潜在可能性。**
<td style="vertical-align:top;width:247.4pt;"> With the advent of powerful pretrained LLMs and VLMs, a renaissance in natural language processing and computer vision has been catalyzed. LLMs now demonstrate an impressive ability to decipher the nuances of real-world linguistic data, often achieving abilities that parallel or even surpass human expertise (OpenAI, 2023). Recently, researchers have shown that LLMs may be extended to act as agents within various environments, performing intricate actions and tasks when paired with domain-specific knowledge and modules (Xi et al., 2023). These scenarios, characterized by complex reasoning, understanding of the agent’s role and its environment, along with multi-step planning, test the agent’s ability to make highly nuanced and intricate decisions within its environmental constraints (Wu et al., 2023; Meta Fundamental AI Research (FAIR) Diplomacy Team et al., 2022). </td><td style="vertical-align:top;width:178.7pt;"> 随着强大的预训练llm和vlm的出现，自然语言处理和计算机视觉的复兴已经被催化。法学硕士现在展示了一种令人印象深刻的能力，可以破译现实世界语言数据的细微差别，通常可以达到与人类专业知识相当甚至超越的能力(OpenAI, 2023)。最近，研究人员已经表明，llm可以扩展为各种环境中的代理，在与领域特定知识和模块配对时执行复杂的动作和任务(Xi et al.， 2023)。这些场景的特点是复杂的推理，对智能体角色及其环境的理解，以及多步骤规划，测试智能体在环境约束下做出高度细微和复杂决策的能力(Wu et al.， 2023;元基础人工智能研究(FAIR)外交团队等，2022)。  </td>

随着强大的预训练llm和vlm的出现，自然语言处理和计算机视觉的复兴已经被催化。法学硕士现在展示了一种令人印象深刻的能力，可以破译现实世界语言数据的细微差别，通常可以达到与人类专业知识相当甚至超越的能力(OpenAI, 2023)。最近，研究人员已经表明，llm可以扩展为各种环境中的代理，在与领域特定知识和模块配对时执行复杂的动作和任务(Xi et al.， 2023)。这些场景的特点是复杂的推理，对智能体角色及其环境的理解，以及多步骤规划，测试智能体在环境约束下做出高度细微和复杂决策的能力(Wu et al.， 2023;元基础人工智能研究(FAIR)外交团队等，2022)。



#### **AI模型的巨大潜力与转变****、****代理中心AI的影响：利用LLMs和VLMs作为代理，特别是在游戏、机器人技术和医疗领域，不仅为AI系统提供了严格的评估平台，还预示了对社会和产业的转变影响。**
<td style="vertical-align:top;width:247.4pt;"> Building upon these initial efforts, the AI community is on the cusp of a significant paradigm shift, transitioning from creating AI models for passive, structured tasks to models capable of assuming dynamic, agentic roles in diverse and complex environments. In this context, this article investigates the immense potential of using LLMs and VLMs as agents, emphasizing models that have a blend of linguistic proficiency, visual cognition, contextual memory, intuitive reasoning, and adaptability. Leveraging LLMs and VLMs as agents, especially within domains like gaming, robotics, and healthcare, promises not just a rigorous evaluation platform for state-of-the-art AI systems, but also foreshadows the transformative impacts that Agent-centric AI will have across society and industries. When fully harnessed, agentic models can redefine human experiences and elevate operational standards. The potential for sweeping automation ushered in by these models portends monumental shifts in industries and socio-economic dynamics. Such advancements will be intertwined with multifaceted leader-board, not only technical but also ethical, as we will elaborate upon in Section 11. We delve into the overlapping areas of these sub-fields of Agent AI and illustrate their interconnectedness in Fig.1. </td><td style="vertical-align:top;width:178.7pt;"> 在这些初步努力的基础上，人工智能社区正处于重大范式转变的风口上，从为被动、结构化任务创建人工智能模型，转变为能够在多样化和复杂的环境中承担动态、代理角色的模型。在这种背景下，本文研究了使用llm和vlm作为代理的巨大潜力，强调了混合了语言熟练度、视觉认知、上下文记忆、直觉推理和适应性的模型。利用llm和vlm作为代理，特别是在游戏、机器人和医疗保健等领域，不仅可以为最先进的人工智能系统提供严格的评估平台，而且还预示着以代理为中心的人工智能将对整个社会和行业产生变革性影响。如果充分利用，代理模型可以重新定义人类体验并提高操作标准。这些模型带来的全面自动化的潜力预示着行业和社会经济动态的巨大变化。这种进步将与多方面的排行榜交织在一起，不仅是技术上的，而且是道德上的，我们将在第11节详细说明。我们深入研究了Agent AI的这些子领域的重叠区域，并在图1中说明了它们的相互联系。 </td>

在这些初步努力的基础上，人工智能社区正处于重大范式转变的风口上，从为被动、结构化任务创建人工智能模型，转变为能够在多样化和复杂的环境中承担动态、代理角色的模型。在这种背景下，本文研究了使用llm和vlm作为代理的巨大潜力，强调了混合了语言熟练度、视觉认知、上下文记忆、直觉推理和适应性的模型。利用llm和vlm作为代理，特别是在游戏、机器人和医疗保健等领域，不仅可以为最先进的人工智能系统提供严格的评估平台，而且还预示着以代理为中心的人工智能将对整个社会和行业产生变革性影响。如果充分利用，代理模型可以重新定义人类体验并提高操作标准。这些模型带来的全面自动化的潜力预示着行业和社会经济动态的巨大变化。这种进步将与多方面的排行榜交织在一起，不仅是技术上的，而且是道德上的，我们将在第11节详细说明。我们深入研究了Agent AI的这些子领域的重叠区域，并在图1中说明了它们的相互联系。



#### **技术与伦理的交织：AI的巨大进步将与技术和伦理层面相互交织，这需要综合考虑**

内容在上边





### **1.2 Background背景**

#### **大型基础模型：LLM和VLM推动了建立通用智能机的工作**
<td style="vertical-align:top;width:245.05pt;"> We will now introduce relevant research papers that support the concepts, theoretical background, and modern implementations of Agent AI. </td><td style="vertical-align:top;width:181.05pt;"> 我们现在将介绍相关的研究论文，这些论文支持Agent AI的概念、理论背景和现代实现。 </td>

我们现在将介绍相关的研究论文，这些论文支持Agent AI的概念、理论背景和现代实现。
<td style="vertical-align:top;width:245.05pt;"> Large Foundation Models: LLMs and VLMs have been driving the effort to develop general intelligent machines (Bubeck et al., 2023; Mirchandani et al., 2023). Although they are trained using large text corpora, their superior problem-solving capacity is not limited to canonical language processing domains. LLMs can potentially tackle complex tasks that were previously presumed to be exclusive to human experts or domain-specific algorithms, ranging from mathematical reasoning (Imani et al., 2023; Wei et al., 2022; Zhu et al., 2022) to answering questions of professional law (Blair-Stanek et al., 2023; Choi et al., 2023; Nay, 2022). Recent research has shown the possibility of using LLMs to generate complex plans for robots and game AI (Liang et al., 2022; Wang et al., 2023a,b; Yao et al., 2023a; Huang et al., 2023a), marking an important milestone for LLMs as general-purpose intelligent agents. </td><td style="vertical-align:top;width:181.05pt;"> **<strong>大型基础模型**</strong>:llm和vlm一直在推动开发通用智能机器的努力(Bubeck等人，2023;Mirchandani et al.， 2023)。虽然他们使用大型文本语料库进行训练，但他们卓越的问题解决能力并不局限于规范语言处理领域。法学硕士可以潜在地解决以前被认为是人类专家或特定领域算法专有的复杂任务，包括数学推理(Imani et al.， 2023;Wei et al.， 2022;Zhu et al.， 2022)，以回答专业法律的问题(Blair-Stanek et al.， 2023;Choi et al.， 2023;不,2022)。最近的研究表明，使用llm为机器人和游戏AI生成复杂计划的可能性(Liang et al.， 2022;Wang et al.， 2023a,b;姚等人，2023a;Huang et al.， 2023a)，标志着llm作为通用智能代理的重要里程碑。  </td>

**<strong>大型基础模型**</strong>:llm和vlm一直在推动开发通用智能机器的努力(Bubeck等人，2023;Mirchandani et al.， 2023)。虽然他们使用大型文本语料库进行训练，但他们卓越的问题解决能力并不局限于规范语言处理领域。法学硕士可以潜在地解决以前被认为是人类专家或特定领域算法专有的复杂任务，包括数学推理(Imani et al.， 2023;Wei et al.， 2022;Zhu et al.， 2022)，以回答专业法律的问题(Blair-Stanek et al.， 2023;Choi et al.， 2023;不,2022)。最近的研究表明，使用llm为机器人和游戏AI生成复杂计划的可能性(Liang et al.， 2022;Wang et al.， 2023a,b;姚等人，2023a;Huang et al.， 2023a)，标志着llm作为通用智能代理的重要里程碑。



#### **Embodied ****AI：一些研究利用LLM进行任务规划，利用LLM的强大知识和零打样本体现能力进行复杂任务规划(关键词：LLM、任务规划)**
<td style="vertical-align:top;width:237.7pt;"> Embodied AI: A number of works leverage LLMs to perform task planning (Huang et al., 2022a; Wang et al., 2023b; Yao et al., 2023a; Li et al., 2023a), specifically the LLMs’ WWW-scale domain knowledge and emergent zero-shot embodied abilities to perform complex task planning and reasoning. Recent robotics research also leverages LLMs to perform task planning (Ahn et al., 2022a; Huang et al., 2022b; Liang et al., 2022) by decomposing natural language instruction into a sequence of subtasks, either in the natural language form or in Python code, then using a low-level controller to execute these subtasks. Additionally, they incorporate environmental feedback to improve task performance (Huang et al., 2022b), (Liang et al., 2022), (Wang et al., 2023a), and (Ikeuchi et al., 2023). </td><td style="vertical-align:top;width:188.4pt;"> 嵌入式AI:许多作品利用llm来执行任务规划(Huang et al.， 2022a;Wang et al.， 2023b;姚等人，2023a;Li et al.， 2023a)，特别是法学硕士在执行复杂任务规划和推理方面的www级领域知识和突发零概率体现能力。最近的机器人研究也利用llm来执行任务规划(Ahn等人，2022a;黄等，20022b;Liang et al.， 2022)通过将自然语言指令分解为一系列子任务，以自然语言形式或Python代码的形式，然后使用低级控制器来执行这些子任务。此外，他们还结合环境反馈来提高任务绩效(Huang et al.， 2022b)、(Liang et al.， 2022)、(Wang et al.， 2023a)和(Ikeuchi et al.， 2023)。  </td>

嵌入式AI:许多作品利用llm来执行任务规划(Huang et al.， 2022a;Wang et al.， 2023b;姚等人，2023a;Li et al.， 2023a)，特别是法学硕士在执行复杂任务规划和推理方面的www级领域知识和突发零概率体现能力。最近的机器人研究也利用llm来执行任务规划(Ahn等人，2022a;黄等，20022b;Liang et al.， 2022)通过将自然语言指令分解为一系列子任务，以自然语言形式或Python代码的形式，然后使用低级控制器来执行这些子任务。此外，他们还结合环境反馈来提高任务绩效(Huang et al.， 2022b)、(Liang et al.， 2022)、(Wang et al.， 2023a)和(Ikeuchi et al.， 2023)。



#### **交互学习AI：AI同时利用机器学习和用户交互来学习，初期在大数据集上训练，然后通过用户反馈和观察学习来改进(关键词：机器学习、用户交互、学习改进)**
<td style="vertical-align:top;width:237.7pt;"> Interactive Learning: AI agents designed for interactive learning operate using a combination of machine learning techniques and user interactions. Initially, the AI agent is trained on a large dataset. This dataset includes various types of information, depending on the intended function of the agent. For instance, an AI designed for language tasks would be trained on a massive corpus of text data. The training involves using machine learning algorithms, which could include deep learning models like neural networks. These training models enable the AI to recognize patterns, make predictions, and generate responses based on the data on which it was trained. The AI agent can also learn from real-time interactions with users. This interactive learning can occur in various ways: 1) Feedback-based learning: The AI adapts its responses based on direct user feedback (Li et al., 2023b; Yu et al., 2023a; Parakh et al., 2023; Zha et al., 2023; Wake et al., 2023a,b,c). For example, if a user corrects the AI’s response, the AI can use this information to improve future responses (Zha et al., 2023; Liu et al., 2023a). 2) Observational Learning: The AI observes user interactions and learns implicitly. For example, if users frequently ask similar questions or interact with the AI in a particular way, the AI might adjust its responses to better suit these patterns. It allows the AI agent to understand and process human language, multi-model setting, interpret the cross reality-context, and generate human-users’ responses. Over time, with more user interactions and feedback, the AI agent’s performance generally continuous improves. This process is often supervised by human operators or developers who ensure that the AI is learning appropriately and not developing biases or incorrect patterns. </td><td style="vertical-align:top;width:188.4pt;"> 交互式学习:为交互式学习设计的AI代理使用机器学习技术和用户交互的组合进行操作。最初，AI代理是在一个大数据集上训练的。该数据集包括各种类型的信息，具体取决于代理的预期功能。例如，为语言任务设计的人工智能将在大量文本数据语料库上进行训练。训练涉及使用机器学习算法，其中可能包括神经网络等深度学习模型。这些训练模型使人工智能能够识别模式，做出预测，并根据训练的数据生成响应。AI代理还可以从与用户的实时交互中学习。这种交互式学习可以以多种方式发生:1)基于反馈的学习:AI根据直接的用户反馈调整其响应(Li et al.， 2023b;Yu et al.， 2009;Parakh et al.， 2023;Zha et al.， 2023;Wake et al.， 2023a,b,c)。例如，如果用户纠正了AI的响应，AI可以使用这些信息来改进未来的响应(Zha et al.， 2023;Liu et al.， 2023a)。2)观察性学习:AI观察用户交互并隐式学习。例如，如果用户经常问类似的问题或以特定方式与AI交互，AI可能会调整其响应以更好地适应这些模式。它允许AI代理理解和处理人类语言，多模型设置，解释交叉现实上下文，并生成人类用户的响应。随着时间的推移，随着更多的用户交互和反馈，AI代理的性能通常会持续提高。这一过程通常由人工操作员或开发人员监督，以确保人工智能适当地学习，而不会产生偏见或不正确的模式。 </td>

交互式学习:为交互式学习设计的AI代理使用机器学习技术和用户交互的组合进行操作。最初，AI代理是在一个大数据集上训练的。该数据集包括各种类型的信息，具体取决于代理的预期功能。例如，为语言任务设计的人工智能将在大量文本数据语料库上进行训练。训练涉及使用机器学习算法，其中可能包括神经网络等深度学习模型。这些训练模型使人工智能能够识别模式，做出预测，并根据训练的数据生成响应。AI代理还可以从与用户的实时交互中学习。这种交互式学习可以以多种方式发生:1)基于反馈的学习:AI根据直接的用户反馈调整其响应(Li et al.， 2023b;Yu et al.， 2009;Parakh et al.， 2023;Zha et al.， 2023;Wake et al.， 2023a,b,c)。例如，如果用户纠正了AI的响应，AI可以使用这些信息来改进未来的响应(Zha et al.， 2023;Liu et al.， 2023a)。2)观察性学习:AI观察用户交互并隐式学习。例如，如果用户经常问类似的问题或以特定方式与AI交互，AI可能会调整其响应以更好地适应这些模式。它允许AI代理理解和处理人类语言，多模型设置，解释交叉现实上下文，并生成人类用户的响应。随着时间的推移，随着更多的用户交互和反馈，AI代理的性能通常会持续提高。这一过程通常由人工操作员或开发人员监督，以确保人工智能适当地学习，而不会产生偏见或不正确的模式。







### **1.3 Overview**

#### **模态代理性AI(MAA)：根据多模态感知输入在给定环境下生成有效行为**
<td style="vertical-align:top;width:256.6pt;"> Multimodal Agent AI (MAA) is a family of systems that generate effective actions in a given environment based on the understanding of multimodal sensory input. With the advent of Large Language Models (LLMs) and Vision-Language Models (VLMs), numerous MAA systems have been proposed in fields ranging from basic research to applications. While these research areas are growing rapidly by integrating with the traditional technologies of each domain (e.g., visual question answering and vision-language navigation), they share common interests such as data collection, benchmarking, and ethical perspectives. In this paper, we focus on the some representative research areas of MAA, namely multimodality, gaming (VR/AR/MR), robotics, and healthcare, and we aim to provide comprehensive knowledge on the common concerns discussed in these fields. As a result we expect to learn the fundamentals of MAA and gain insights to further advance their research. </td><td style="vertical-align:top;width:169.5pt;"> 多模态智能体(MAA)是基于对多模态感官输入的理解，在给定环境中产生有效动作的一系列系统。随着大型语言模型(llm)和视觉语言模型(vlm)的出现，从基础研究到应用领域都提出了许多MAA系统。虽然这些研究领域通过与各个领域的传统技术(如视觉问答和视觉语言导航)相结合而迅速发展，但它们在数据收集、基准测试和伦理观点等方面有着共同的兴趣。在本文中，我们将重点关注MAA的一些代表性研究领域，即多模态，游戏(VR/AR/MR)，机器人和医疗保健，我们的目标是提供有关这些领域讨论的共同关注点的全面知识。因此，我们希望学习MAA的基础知识，并获得进一步推进他们研究的见解。 </td>

多模态智能体(MAA)是基于对多模态感官输入的理解，在给定环境中产生有效动作的一系列系统。随着大型语言模型(llm)和视觉语言模型(vlm)的出现，从基础研究到应用领域都提出了许多MAA系统。虽然这些研究领域通过与各个领域的传统技术(如视觉问答和视觉语言导航)相结合而迅速发展，但它们在数据收集、基准测试和伦理观点等方面有着共同的兴趣。在本文中，我们将重点关注MAA的一些代表性研究领域，即多模态，游戏(VR/AR/MR)，机器人和医疗保健，我们的目标是提供有关这些领域讨论的共同关注点的全面知识。因此，我们希望学习MAA的基础知识，并获得进一步推进他们研究的见解。

#### **研究方法：详细例子介绍如何利用LLM和VLM提升MAA，通过游戏、机器人和医疗案例阐述**
<td style="vertical-align:top;width:241.4pt;"> Specific learning outcomes include: &gt;&gt;MAA Overview: A deep dive into its principles and roles in contemporary applications, providing researcher with a thorough grasp of its importance and uses. &gt;&gt;Methodologies: Detailed examples of how LLMs and VLMs enhance MAAs, illustrated through case studies in gaming, robotics, and healthcare. &gt;&gt;Performance Evaluation: Guidance on the assessment of MAAs with relevant datasets, focusing on their effectiveness and generalization. &gt;&gt;Ethical Considerations: A discussion on the societal impacts and ethical leader-board of deploying Agent AI, highlighting responsible development practices. &gt;&gt;Emerging Trends and Future leader-board: Categorize the latest developments in each domain and discuss the future directions. </td><td style="vertical-align:top;width:184.7pt;"> 具体的学习成果包括: &gt;&gt;MAA概述:深入探讨其在当代应用中的原理和作用，为研究人员提供对其重要性和用途的全面掌握。 &gt;&gt;方法:llm和vlm如何增强maa的详细示例，通过游戏、机器人和医疗保健方面的案例研究进行说明。 &gt;&gt;绩效评估:使用相关数据集对maa进行评估的指南，重点关注其有效性和泛化。 &gt;&gt;伦理考虑:讨论部署人工智能的社会影响和伦理排行榜，强调负责任的开发实践。 &gt;&gt;新兴趋势和未来排行榜:对每个领域的最新发展进行分类，并讨论未来的发展方向。  </td>

&gt;&gt;MAA Overview: A deep dive into its principles and roles in contemporary applications, providing researcher with a thorough grasp of its importance and uses.

&gt;&gt;Performance Evaluation: Guidance on the assessment of MAAs with relevant datasets, focusing on their effectiveness and generalization.

&gt;&gt;Emerging Trends and Future leader-board: Categorize the latest developments in each domain and discuss the future directions.

&gt;&gt;MAA概述:深入探讨其在当代应用中的原理和作用，为研究人员提供对其重要性和用途的全面掌握。

&gt;&gt;绩效评估:使用相关数据集对maa进行评估的指南，重点关注其有效性和泛化。

&gt;&gt;新兴趋势和未来排行榜:对每个领域的最新发展进行分类，并讨论未来的发展方向。



#### **性能评估：重点关注MAA在相关数据集上的有效性和泛化能力**
<td style="vertical-align:top;width:237.7pt;"> Computer-based action and generalist agents (GAs) are useful for many tasks. A GA to become truly valuable to its users, it can natural to interact with, and generalize to a broad range of contexts and modalities. We aims to cultivate a vibrant research ecosystem and create a shared sense of identity and purpose among the Agent AI community. MAA has the potential to be widely applicable across various contexts and modalities, including input from humans. Therefore, we believe this Agent AI area can engage a diverse range of researchers, fostering a dynamic Agent AI community and shared goals. Led by esteemed experts from academia and industry, we expect that this paper will be an interactive and enriching experience, complete with agent instruction, case studies, tasks sessions, and experiments discussion ensuring a comprehensive and engaging learning experience for all researchers. </td><td style="vertical-align:top;width:188.4pt;"> 基于计算机的动作和通才代理(GAs)对许多任务都很有用。一个遗传算法要真正对它的用户有价值，它就可以自然地与之交互，并推广到广泛的上下文和模式。我们的目标是培养一个充满活力的研究生态系统，并在Agent AI社区中创造一种共同的认同感和使命感。MAA具有广泛应用于各种环境和模式的潜力，包括人类的投入。因此，我们相信这个人工智能领域可以吸引各种各样的研究人员，培养一个充满活力的人工智能社区和共同的目标。在学术界和工业界备受尊敬的专家的带领下，我们希望这篇论文将是一个互动和丰富的体验，包括代理指导，案例研究，任务会议和实验讨论，确保所有研究人员都能获得全面而引人入胜的学习体验。  </td>

基于计算机的动作和通才代理(GAs)对许多任务都很有用。一个遗传算法要真正对它的用户有价值，它就可以自然地与之交互，并推广到广泛的上下文和模式。我们的目标是培养一个充满活力的研究生态系统，并在Agent AI社区中创造一种共同的认同感和使命感。MAA具有广泛应用于各种环境和模式的潜力，包括人类的投入。因此，我们相信这个人工智能领域可以吸引各种各样的研究人员，培养一个充满活力的人工智能社区和共同的目标。在学术界和工业界备受尊敬的专家的带领下，我们希望这篇论文将是一个互动和丰富的体验，包括代理指导，案例研究，任务会议和实验讨论，确保所有研究人员都能获得全面而引人入胜的学习体验。



#### **伦理考量：讨论部署代理性AI对社会影响和倫理问题，强调负责任开发实践**
<td style="vertical-align:top;width:237.7pt;"> This paper aims to provide general and comprehensive knowledge about the current research in the field of Agent AI. To this end, the rest of the paper is organized as follows. Section 2 outlines how Agent AI benefits from integrating with related emerging technologies, particularly large foundation models. Section 3 describes a new paradigm and framework that we propose for training Agent AI. Section 4 provides an overview of the methodologies that are widely used in the training of Agent AI. Section 5 categorizes and discusses various types of agents. Section 6 introduces Agent AI applications in gaming, robotics, and healthcare. Section 7 explores the research community’s efforts to develop a versatile Agent AI, capable of being applied across various modalities, domains, and bridging the sim-to-real gap. Section 8 discusses the potential of Agent AI that not only relies on pre-trained foundation models, but also continuously learns and self-improves by leveraging interactions with the environment and users. Section 9 introduces our new datasets that are designed for the training of multimodal Agent AI. Section 11 discusses the hot topic of the ethics consideration of AI agent, limitations, and societal impact of our paper. </td><td style="vertical-align:top;width:188.4pt;"> 本文旨在为Agent AI领域的研究现状提供一般和全面的知识。为此，本文的其余部分组织如下。第2节概述了Agent AI如何从与相关新兴技术(特别是大型基础模型)的集成中获益。第3节描述了我们提出的用于训练Agent AI的新范式和框架。第4节概述了在Agent AI训练中广泛使用的方法。第5节对各种类型的代理进行了分类和讨论。第6节介绍了Agent AI在游戏、机器人和医疗保健中的应用。第7节探讨了研究界为开发一种多功能智能体所做的努力，这种智能体能够应用于各种模式、领域，并弥合模拟与现实之间的差距。第8节讨论了Agent AI的潜力，它不仅依赖于预训练的基础模型，而且还通过利用与环境和用户的交互不断学习和自我改进。第9节介绍了我们为训练多模式Agent AI而设计的新数据集。第11节讨论了人工智能主体的伦理考虑的热门话题，本文的局限性和社会影响。 </td>

本文旨在为Agent AI领域的研究现状提供一般和全面的知识。为此，本文的其余部分组织如下。第2节概述了Agent AI如何从与相关新兴技术(特别是大型基础模型)的集成中获益。第3节描述了我们提出的用于训练Agent AI的新范式和框架。第4节概述了在Agent AI训练中广泛使用的方法。第5节对各种类型的代理进行了分类和讨论。第6节介绍了Agent AI在游戏、机器人和医疗保健中的应用。第7节探讨了研究界为开发一种多功能智能体所做的努力，这种智能体能够应用于各种模式、领域，并弥合模拟与现实之间的差距。第8节讨论了Agent AI的潜力，它不仅依赖于预训练的基础模型，而且还通过利用与环境和用户的交互不断学习和自我改进。第9节介绍了我们为训练多模式Agent AI而设计的新数据集。第11节讨论了人工智能主体的伦理考虑的热门话题，本文的局限性和社会影响。







## **2 Agent AI IntegrationAgentAI集成**
<td style="vertical-align:top;width:262.6pt;"> Foundation models based on LLMs and VLMs, as proposed in previous research, still exhibit limited performance in the area of embodied AI, particularly in terms of understanding, generating, editing, and interacting within unseen environments or scenarios (Huang et al., 2023a; Zeng et al., 2023). Consequently, these limitations lead to sub-optimal outputs from AI agents. Current agent-centric AI modeling approaches focus on directly accessible and clearly defined data (e.g. text or string representations of the world state) and generally use domain and environment-independent patterns learned from their large-scale pretraining to predict action outputs for each environment (Xi et al., 2023; Wang et al., 2023c; Gong et al., 2023a; Wu et al., 2023). In (Huang et al., 2023a), we investigate the task of knowledge-guided collaborative and interactive scene generation by combining large foundation models, and show promising results that indicate knowledge-grounded LLM agents can improve the performance of 2D and 3D scene understanding, generation, and editing, alongside with other human-agent interactions (Huang et al., 2023a). By integrating an Agent AI framework, large foundation models are able to more deeply understand user input to form a complex and adaptive HCI system. Emergent ability of LLM and VLM works invisible in generative AI, embodied AI, knowledge augmentation for multi-model learning, mix-reality generation, text to vision editing, human interaction for 2D/3D simulation in gaming or robotics tasks. Agent AI recent progress in foundation models present an imminent catalyst for unlocking general intelligence in embodied agents. The large action models, or agent-vision-language models open new possibilities for general-purpose embodied systems such as planning, problem-solving and learning in complex environments. Agent AI test further step in metaverse, and route the early version of AGI. </td><td style="vertical-align:top;width:163.5pt;"> 先前研究中提出的基于LLMs和VLMs的基础模型，在**<strong>具身智能**</strong>领域仍然表现有限，特别是在未知环境或场景中的理解、生成、编辑和交互方面(Huang et al.， 2023a;Zeng et al.， 2023)。因此，这些限制导致AI代理的输出不够优化。Wang et al.， 2023c;龚等人，2009;Wu等人，2023)。在(Huang et al.， 2023a)中，我们通过结合大型基础模型研究了知识引导的协作和交互场景生成任务，并显示了**<strong>有希望的结果**</strong>，表明**<strong>基于知识的LLM代理**</strong>可以提高2D和3D场景理解、生成和编辑的性能，以及其他人类代理交互(Huang et al.， 2023a)。 通过集成Agent AI框架，大型基础模型能够更深入地理解用户输入，形成复杂且自适应的HCI系统。LLM和VLM的**<strong>涌现能力**</strong>在生成式AI、体验式AI、多模型学习的知识增强、混合现实生成、文本到视觉编辑、游戏或机器人任务中2D/3D仿真的人机交互中，起着无形的作用。人工智能基础模型的最新进展为解锁具身智能体的通用智能提供了迫在眉睫的催化剂。大型动作模型或代理-视觉-语言模型，为通用的具体化系统(如复杂环境中的规划、解决问题和学习)开辟了新的可能性。Agent AI在**<strong>元宇宙**</strong>中迈出了进一步的步伐，并为早期版本的通用人工智能铺平了道路。 </td>

先前研究中提出的基于LLMs和VLMs的基础模型，在**<strong>具身智能**</strong>领域仍然表现有限，特别是在未知环境或场景中的理解、生成、编辑和交互方面(Huang et al.， 2023a;Zeng et al.， 2023)。因此，这些限制导致AI代理的输出不够优化。Wang et al.， 2023c;龚等人，2009;Wu等人，2023)。在(Huang et al.， 2023a)中，我们通过结合大型基础模型研究了知识引导的协作和交互场景生成任务，并显示了**<strong>有希望的结果**</strong>，表明**<strong>基于知识的LLM代理**</strong>可以提高2D和3D场景理解、生成和编辑的性能，以及其他人类代理交互(Huang et al.， 2023a)。





### **2.1 Infinite AI agent无限人工智能代理**

#### **AI代理系统的四大能力：预测、决策、处理歧义、持续改进**
<td style="vertical-align:top;width:243.25pt;"> AI agents have the capacity to interpret, predict, and respond based on its training and input data. While these capabilities are advanced and continually improving, it’s important to recognize their limitations and the influence of the underlying data they are trained on. AI agent systems generally possess the following abilities: 1) Predictive Modeling: AI agents can predict likely outcomes or suggest next steps based on historical data and trends. For instance, they might predict the continuation of a text, the answer to a question, the next action for a robot, or the resolution of a scenario. 2) Decision Making: In some applications, AI agents can make decisions based on their inferences. Generally, the agent will base their decision on what is most likely to achieve a specified goal. For AI applications like recommendation systems, an agent can decide what products or content to recommend based on its inferences about user preferences. 3) Handling Ambiguity: AI agents can often handle ambiguous input by inferring the most likely interpretation based on context and training. However, their ability to do so is limited by the scope of their training data and algorithms. 4) Continuous Improvement: While some AI agents have the ability to learn from new data and interactions, many large language models do not continuously update their knowledge-base or internal representation after training. Their inferences are usually based solely on the data that was available up to the point of their last training update. </td><td style="vertical-align:top;width:182.85pt;"> **<strong>AI代理**</strong>有能力根据其训练和输入的数据进行解释、预测和响应。虽然这些功能是先进的，并且在不断改进，但重要的是要认识到它们的局限性以及它们所训练的底层数据的影响。AI代理系统通常具有以下能力: **<strong>1)预测建模**</strong>：AI代理可以根据历史数据和趋势预测可能的结果或建议下一步的步骤。例如，它们可以预测文本的延续、问题的答案、机器人的下一步动作或场景的解决方案。 **<strong>2)决策制定**</strong>：在某些应用中，AI代理可以根据他们的推断做出决策。一般来说，代理将根据最可能实现指定目标的方式做出决策。对于像推荐系统这样的人工智能应用程序，代理可以根据对用户偏好的推断来决定推荐哪些产品或内容。 **<strong>3)处理歧义**</strong>：AI代理通常可以通过基于上下文和训练推断最可能的解释来处理歧义输入。然而，他们这样做的能力受到训练数据和算法范围的限制。 **<strong>4)持续改进**</strong>：虽然一些AI代理有能力从新的数据和交互中学习，但许多大型语言模型在训练后并没有持续更新其知识库或内部表示。他们的推断通常仅仅基于他们最后一次训练更新时可用的数据。 </td>

**<strong>AI代理**</strong>有能力根据其训练和输入的数据进行解释、预测和响应。虽然这些功能是先进的，并且在不断改进，但重要的是要认识到它们的局限性以及它们所训练的底层数据的影响。AI代理系统通常具有以下能力:

**<strong>2)决策制定**</strong>：在某些应用中，AI代理可以根据他们的推断做出决策。一般来说，代理将根据最可能实现指定目标的方式做出决策。对于像推荐系统这样的人工智能应用程序，代理可以根据对用户偏好的推断来决定推荐哪些产品或内容。

**<strong>4)持续改进**</strong>：虽然一些AI代理有能力从新的数据和交互中学习，但许多大型语言模型在训练后并没有持续更新其知识库或内部表示。他们的推断通常仅仅基于他们最后一次训练更新时可用的数据。



#### **无限智能体(I****nfinite ****A****gent****)：可以****不断地学习并适应新任务****，而无需为每个新任务收集大量的训练数据，比如****<strong>RoboGen**</strong>
<td style="vertical-align:top;width:243.25pt;"> We show augmented interactive agents for multi-modality and cross reality-agnostic integration with an emergence mechanism in Fig. 2. An AI agent requires collecting extensive training data for every new task, which can be costly or impossible for many domains. In this study, we develop an infinite agent that learns to transfer memory information from general foundation models (e.g., GPT-X, DALL-E) to novel domains or scenarios for scene understanding, generation, and interactive editing in physical or virtual worlds. An application of such an infinite agent in robotics is RoboGen (Wang et al., 2023d). In this study, the authors propose a pipeline that autonomously run the cycles of task proposition, environment generation, and skill learning. RoboGen is an effort to transfer the knowledge embedded in large models to robotics. </td><td style="vertical-align:top;width:182.85pt;"> 我们在图2中展示了用于多模态和跨现实未知集成的增强交互代理与新兴机制。AI代理需要为每个新任务收集大量的训练数据，这对于许多领域来说可能是昂贵的或不可能的。在这项研究中，我们开发了一个**<strong>无限智能体**</strong>，它可以学习将记忆信息从一般的基础模型(例如，GPT-X, DALL-E)转移到新的领域或场景中，以便在物理或虚拟世界中进行场景理解、生成和交互式编辑。 这种**<strong>无限智能体**</strong>在机器人技术中的一个应用是**<strong>RoboGen **</strong>(Wang et al.， 2023d)。在这项研究中，作者提出了一个自主运行任务提出、环境生成和技能学习循环的流水线。RoboGen致力于将嵌入在大型模型中的知识转移到机器人技术中。 </td>

An application of such an infinite agent in robotics is RoboGen (Wang et al., 2023d). In this study, the authors propose a pipeline that autonomously run the cycles of task proposition, environment generation, and skill learning. RoboGen is an effort to transfer the knowledge embedded in large models to robotics.

这种**<strong>无限智能体**</strong>在机器人技术中的一个应用是**<strong>RoboGen **</strong>(Wang et al.， 2023d)。在这项研究中，作者提出了一个自主运行任务提出、环境生成和技能学习循环的流水线。RoboGen致力于将嵌入在大型模型中的知识转移到机器人技术中。

#### Figure 2: The multi-model agent AI for 2D/3D embodied generation and editing interaction in cross-reality.图2:跨现实中2D/3D嵌入生成和编辑交互的多模型agent AI。

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/direct/4e05fe3428ba42c0860893e3da206001.png" width="1200">





### **2.2 Agent AI with Large Foundation Models****具有大型基础模型的****人工智能代理**

##### **<strong><strong>LLM中的**</strong>**<strong>基准数据发挥重要作用**</strong>**<strong>：可以**</strong>**<strong>检测代理在不同环境下行为限制条件**</strong></strong>
<td style="vertical-align:top;width:237.7pt;"> Recent studies have indicated that large foundation models play a crucial role in creating data that act as benchmarks for determining the actions of agents within environment-imposed constraints. For example, using foundation models for robotic manipulation (Black et al., 2023; Ko et al., 2023) and navigation (Shah et al., 2023a; Zhou et al., 2023a). To illustrate, Black et al. employed an image-editing model as a high-level planner to generate images of future sub-goals, thereby guiding low-level policies (Black et al., 2023). For robot navigation, Shah et al. proposed a system that employs a LLM to identify landmarks from text and a VLM to associate these landmarks with visual inputs, enhancing navigation through natural language instructions (Shah et al., 2023a). </td><td style="vertical-align:top;width:188.4pt;"> 最近的研究表明，**<strong>大型基础模型**</strong>在创建数据方面发挥着至关重要的作用，这些数据可以作为确定环境施加约束下代理行为的基准。例如，使用基础模型进行机器人操纵(Black et al.， 2023;Ko等人，2023)和导航(Shah等人，2023a;周等人，2009)。 为了说明这一点，Black等人使用**<strong>图像编辑模型**</strong>作为高级计划器来生成未来子目标的图像，从而指导低级政策(Black et al.， 2023)。 对于机器人导航，Shah等人提出了一种系统，该系统使用LLM从文本中识别地标，并使用VLM将这些地标与视觉输入关联起来，通过自然语言指令增强导航(Shah等人，2023a)。 </td>

最近的研究表明，**<strong>大型基础模型**</strong>在创建数据方面发挥着至关重要的作用，这些数据可以作为确定环境施加约束下代理行为的基准。例如，使用基础模型进行机器人操纵(Black et al.， 2023;Ko等人，2023)和导航(Shah等人，2023a;周等人，2009)。

对于机器人导航，Shah等人提出了一种系统，该系统使用LLM从文本中识别地标，并使用VLM将这些地标与视觉输入关联起来，通过自然语言指令增强导航(Shah等人，2023a)。



##### **<strong><strong>越来越感兴趣：人们对产生受语言和环境因素影响的有条件的人体动作**</strong></strong>
<td style="vertical-align:top;width:237.7pt;"> There is also growing interest in the generation of conditioned human motions in response to language and environmental factors. Several AI systems have been proposed to generate motions and actions that are tailored to specific linguistic instructions (Kim et al., 2023; Zhang et al., 2022; Tevet et al., 2022) and to adapt to various 3D scenes (Wang et al., 2022a). This body of research emphasizes the growing capabilities of generative models in enhancing the adaptability and responsiveness of AI agents across diverse scenarios. </td><td style="vertical-align:top;width:188.4pt;"> 人们对产生受语言和环境因素影响的有条件的人体动作也越来越感兴趣。已经提出了几个人工智能系统，用于生成根据特定语言指令定制的动作(Kim等人，2023;Zhang et al.， 2022;Tevet et al.， 2022)以及适应各种3D场景(Wang et al.， 2022a)。这一研究强调了生成模型在增强AI代理在不同场景中的适应性和响应性方面日益增长的能力。 </td>

人们对产生受语言和环境因素影响的有条件的人体动作也越来越感兴趣。已经提出了几个人工智能系统，用于生成根据特定语言指令定制的动作(Kim等人，2023;Zhang et al.， 2022;Tevet et al.， 2022)以及适应各种3D场景(Wang et al.， 2022a)。这一研究强调了生成模型在增强AI代理在不同场景中的适应性和响应性方面日益增长的能力。





#### **2.2.1 Hallucinations****幻觉**

##### **<strong><strong>LLMs中的**</strong>**<strong>幻觉**</strong>**<strong>：两类**</strong>**<strong>幻觉**</strong>**<strong>=内在(**</strong>**<strong>与原始材料相矛盾**</strong>**<strong>)+外在(原始材料未包含的**</strong>**<strong>额外信息**</strong>**<strong>)**</strong></strong>
<td style="vertical-align:top;width:254.75pt;"> Agents that generate text are often prone to hallucinations, which are instances where the generated text is nonsensical or unfaithful to the provided source content (Raunak et al., 2021; Maynez et al., 2020). Hallucinations can be split into two categories, intrinsic and extrinsic (Ji et al., 2023). Intrinsic hallucinations are hallucinations that are contradictory to the source material, whereas extrinsic hallucinations are when the generated text contains additional information that was not originally included in the source material. </td><td style="vertical-align:top;width:171.35pt;"> 生成文本的代理通常容易产生幻觉，即生成的文本毫无意义或与提供的源内容不忠实(Raunak et al.， 2021;Maynez et al.， 2020)。 幻觉可以分为两类，**<strong>内在**</strong>的和**<strong>外在**</strong>的(Ji et al.， 2023)。内在幻觉是指与原始材料相矛盾的幻觉，而外在幻觉是指生成的文本包含了原始材料中没有包含的额外信息。  </td>

生成文本的代理通常容易产生幻觉，即生成的文本毫无意义或与提供的源内容不忠实(Raunak et al.， 2021;Maynez et al.， 2020)。





###### **改进方法：RAG或其他方法，旨在通过****检索额外的源材料****并提供机制来****检查生成****的响应与源材料之间的****矛盾****来增强语言生成**
<td style="vertical-align:top;width:254.75pt;"> Some promising routes for reducing the rate of hallucination in language generation involve using retrieval-augmented generation (Lewis et al., 2020; Shuster et al., 2021) or other methods for grounding natural language outputs via external knowledge retrieval (Dziri et al., 2021; Peng et al., 2023). Generally, these methods seek to augment language generation by retrieving additional source material and by providing mechanisms to check for contradictions between the generated response and the source material. </td><td style="vertical-align:top;width:171.35pt;"> 减少语言生成中幻觉率的一些有希望的途径包括使用**<strong>检索增强生成**</strong>(Lewis et al.， 2020;Shuster等人，2021)或通过外部知识检索为自然语言输出提供基础的**<strong>其他方法**</strong>(Dziri等人，2021;Peng et al.， 2023)。总体而言，这些方法旨在通过检索额外的源材料并提供机制来检查生成的响应与源材料之间的矛盾来增强语言生成。 </td>

减少语言生成中幻觉率的一些有希望的途径包括使用**<strong>检索增强生成**</strong>(Lewis et al.， 2020;Shuster等人，2021)或通过外部知识检索为自然语言输出提供基础的**<strong>其他方法**</strong>(Dziri等人，2021;Peng et al.， 2023)。总体而言，这些方法旨在通过检索额外的源材料并提供机制来检查生成的响应与源材料之间的矛盾来增强语言生成。



##### **<strong><strong>VLMs(多模态)中的幻觉：仅依赖预训练模型的**</strong>**<strong>内部知识库**</strong>**<strong>，**</strong>**<strong>无法准确理解**</strong>**<strong>世界状态**</strong></strong>
<td style="vertical-align:top;width:254.75pt;"> Within the context of multi-modal agent systems, VLMs have been shown to hallucinate as well (Zhou et al., 2023b). One common cause of hallucination for vision-based language-generation is due to the over-reliance on co-occurrence of objects and visual cues in the training data (Rohrbach et al., 2018). AI agents that exclusively rely upon pretrained LLMs or VLMs and use limited environment-specific finetuning can be particularly vulnerable to hallucinations since they rely upon the internal knowledge-base of the pretrained models for generating actions and may not accurately understand the dynamics of the world state in which they are deployed. </td><td style="vertical-align:top;width:171.35pt;"> 在多模态智能体系统的背景下，VLMs也会产生幻觉(Zhou et al.， 2023b)。基于视觉的语言生成产生幻觉的一个常见原因是过度依赖训练数据中对象和视觉提示的共同出现(Rohrbach et al.， 2018)。 仅依赖于预训练的LLMs或VLMs并使用有限的环境特定微调的AI代理可能特别容易产生幻觉，因为它们依赖于预训练模型的内部知识库来生成动作，并且可能无法准确理解它们所部署的世界状态的动态。 </td>

在多模态智能体系统的背景下，VLMs也会产生幻觉(Zhou et al.， 2023b)。基于视觉的语言生成产生幻觉的一个常见原因是过度依赖训练数据中对象和视觉提示的共同出现(Rohrbach et al.， 2018)。





#### **2.2.2 Biases and Inclusivity****偏见和包容性**
<td style="vertical-align:top;width:242.75pt;"> AI agents based on LLMs or LMMs (large multimodal models) have biases due to several factors inherent in their design and training process. When designing these AI agents, we must be mindful of being inclusive and aware of the needs of all end users and stakeholders. In the context of AI agents, inclusivity refers to the measures and principles employed to ensure that the agent’s responses and interactions are inclusive, respectful, and sensitive to a wide range of users from diverse backgrounds. We list key aspects of agent biases and inclusivity below </td><td style="vertical-align:top;width:183.35pt;"> **<strong>基于LLMs或LMMs**</strong>（大型多模态模型）的AI代理由于其设计和训练过程中固有的几个因素而存在偏见。在设计这些AI代理时，我们必须注意包容性，并了解所有最终用户和利益相关者的需求。 在人工智能智能体的背景下，包容性是指为确保智能体的响应和交互对来自不同背景的广泛用户具有包容性、尊重性和敏感性而采用的措施和原则。 </td>

**<strong>基于LLMs或LMMs**</strong>（大型多模态模型）的AI代理由于其设计和训练过程中固有的几个因素而存在偏见。在设计这些AI代理时，我们必须注意包容性，并了解所有最终用户和利益相关者的需求。



##### **<strong><strong>Agent偏见和包容性的关键方面**</strong></strong>

###### **训练数据：基础模型从互联网大数据源训练，数据可能包含社会偏见****，包括与种族、性别、族裔、宗教等相关的刻板印象和偏见**
<td style="vertical-align:top;width:242.75pt;"> &gt;&gt;Training Data: Foundation models are trained on vast amounts of text data collected from the internet, including books, articles, websites, and other text sources. This data often reflects the biases present in human society, and the model can inadvertently learn and reproduce these biases. This includes stereotypes, prejudices, and slanted viewpoints related to race, gender, ethnicity, religion, and other personal attributes. In particular, by training on internet data and often only English text, models implicitly learn the cultural norms of Western, Educated, Industrialized, Rich, and Democratic (WEIRD) societies (Henrich et al., 2010) who have a disproportionately large internet presence. However, it is essential to recognize that datasets created by humans cannot be entirely devoid of bias, since they frequently mirror the societal biases and the predispositions of the individuals who generated and/or compiled the data initially. </td><td style="vertical-align:top;width:183.35pt;"> 我们在下面列出了Agent偏见和包容性的关键方面 &gt;&gt;训练数据:基础模型在从互联网收集的大量文本数据上进行训练，包括书籍，文章，网站和其他文本来源。这些数据通常反映了人类社会中存在的偏见，而模型可以在不经意间学习和复制这些偏见。这包括与种族、性别、民族、宗教和其他个人属性有关的刻板印象、偏见和倾斜的观点。特别是，通过对互联网数据和通常只有英文文本的训练，模型隐含地学习了西方、受过教育的、工业化的、富裕的和民主的(WEIRD)社会的文化规范(Henrich et al.， 2010)，这些社会拥有不成比例的大量互联网存在。然而，必须认识到，人类创建的数据集不可能完全没有偏见，因为它们经常反映社会偏见，以及最初生成和/或汇编数据的个人的倾向。 </td>

我们在下面列出了Agent偏见和包容性的关键方面

###### **历史文化偏见：训练数据可能包含历史偏见或不同文化立场****，其中可能包含冒犯性或贬损性语言**

###### **语言环境限制：模型难以完全理解语言细微差别导致误导****，如讽刺、幽默或文化引用**

###### **政策和准则： ****要****确保公平和包容，例如在生成图像时，有规定多样化描绘人物的规则，避免与种族、性别等相关的刻板印象。**

###### **不当泛化：模型倾向于根据训练数据模式产生回复****，导致过度概括****，可能形成立场**
<td style="vertical-align:top;width:248.3pt;"> &gt;&gt;Historical and Cultural Biases: AI models are trained on large datasets sourced from diverse content. Thus, the training data often includes historical texts or materials from various cultures. In particular, training data from historical sources may contain offensive or derogatory language representing a particular society’s cultural norms, attitudes, and prejudices. This can lead to the model perpetuating outdated stereotypes or not fully understanding contemporary cultural shifts and nuances. &gt;&gt;Language and Context Limitations: Language models might struggle with understanding and accurately representing nuances in language, such as sarcasm, humor, or cultural references. This can lead to misinterpretations or biased responses in certain contexts. Furthermore, there are many aspects of spoken language that are not captured by pure text data, leading to a potential disconnect between human understanding of language and how models understand language. &gt;&gt;Policies and Guidelines: AI agents operate under strict policies and guidelines to ensure fairness and inclusivity. For instance, in generating images, there are rules to diversify depictions of people, avoiding stereotypes related to race, gender, and other attributes. &gt;&gt;Overgeneralization: These models tend to generate responses based on patterns seen in the training data. This can lead to overgeneralizations, where the model might produce responses that seem to stereotype or make broad assumptions about certain groups. </td><td style="vertical-align:top;width:177.8pt;"> &gt;&gt;历史和文化偏见:人工智能模型是在来自不同内容的大型数据集上训练的。因此，训练数据通常包括历史文本或来自不同文化的材料。特别是，来自历史来源的训练数据可能包含代表特定社会文化规范、态度和偏见的攻击性或贬损性语言。这可能导致模型延续过时的刻板印象，或者不能完全理解当代文化的转变和细微差别。 &gt;&gt;语言和上下文限制:语言模型可能难以理解和准确地表示语言中的细微差别，例如讽刺、幽默或文化参考。在某些情况下，这可能导致误解或有偏见的反应。此外，口语的许多方面没有被纯文本数据捕获，从而导致人类对语言的理解与模型对语言的理解之间存在潜在的脱节。 &gt;&gt;政策和指南:AI代理在严格的政策和指南下运行，以确保公平性和包容性。例如，在生成图像时，有一些规则可以使人物的描述多样化，避免与种族、性别和其他属性相关的刻板印象。 &gt;&gt;过度概括:这些模型倾向于根据训练数据中看到的模式生成响应。这可能会导致过度概括，模型可能会产生似乎是刻板印象或对某些群体做出广泛假设的反应。 </td>

&gt;&gt;Language and Context Limitations: Language models might struggle with understanding and accurately representing nuances in language, such as sarcasm, humor, or cultural references. This can lead to misinterpretations or biased responses in certain contexts. Furthermore, there are many aspects of spoken language that are not captured by pure text data, leading to a potential disconnect between human understanding of language and how models understand language.

&gt;&gt;Overgeneralization: These models tend to generate responses based on patterns seen in the training data. This can lead to overgeneralizations, where the model might produce responses that seem to stereotype or make broad assumptions about certain groups.

&gt;&gt;语言和上下文限制:语言模型可能难以理解和准确地表示语言中的细微差别，例如讽刺、幽默或文化参考。在某些情况下，这可能导致误解或有偏见的反应。此外，口语的许多方面没有被纯文本数据捕获，从而导致人类对语言的理解与模型对语言的理解之间存在潜在的脱节。

&gt;&gt;过度概括:这些模型倾向于根据训练数据中看到的模式生成响应。这可能会导致过度概括，模型可能会产生似乎是刻板印象或对某些群体做出广泛假设的反应。



###### **持续监测更新：用户反馈和伦理研究帮助解决新出现问题**

###### **强化主流观点： 模型可能更偏向主导文化或群体的观点，潜在地低估或误代表少数观点。**

###### **道德和包容性设计： 尊重文化差异，促进多样性，并确保AI不延续有害的刻板印象。**

###### **用户指南： 引导以促进包容和尊重的方式与AI进行互动，包括避免可能导致有偏见或不适当输出的请求，以减轻模型从用户互动中学到有害材料的可能性。**
<td style="vertical-align:top;width:242.75pt;"> &gt;&gt;Constant Monitoring and Updating: AI systems are continuously monitored and updated to address any emerging biases or inclusivity issues. Feedback from users and ongoing research in AI ethics play a crucial role in this process. &gt;&gt;Amplification of Dominant Views: Since the training data often includes more content from dominant cultures or groups, the model may be more biased towards these perspectives, potentially underrepresenting or misrepresenting minority viewpoints. &gt;&gt;Ethical and Inclusive Design: AI tools should be designed with ethical considerations and inclusivity as core principles. This includes respecting cultural differences, promoting diversity, and ensuring that the AI does not perpetuate harmful stereotypes. &gt;&gt;User Guidelines: Users are also guided on how to interact with AI in a manner that promotes inclusivity and respect. This includes refraining from requests that could lead to biased or inappropriate outputs. Furthermore, it can help mitigate models learning harmful material from user interactions. </td><td style="vertical-align:top;width:183.35pt;"> &gt;&gt;持续监控和更新:人工智能系统被持续监控和更新，以解决任何新出现的偏见或包容性问题。来自用户的反馈和正在进行的人工智能伦理研究在这一过程中发挥着至关重要的作用。 &gt;&gt;主流观点的放大:由于训练数据通常包含更多来自主流文化或群体的内容，模型可能更偏向于这些观点，可能会低估或歪曲少数人的观点。 &gt;&gt;道德和包容性设计:人工智能工具的设计应以道德考虑和包容性为核心原则。这包括尊重文化差异，促进多样性，并确保人工智能不会使有害的刻板印象永久化。 &gt;&gt;用户指南:还指导用户如何以促进包容性和尊重的方式与人工智能进行交互。这包括避免提出可能导致有偏见或不适当产出的要求。此外，它可以帮助减轻模型从用户交互中学习有害材料的情况。  </td>

&gt;&gt;Amplification of Dominant Views: Since the training data often includes more content from dominant cultures or groups, the model may be more biased towards these perspectives, potentially underrepresenting or misrepresenting minority viewpoints.

&gt;&gt;User Guidelines: Users are also guided on how to interact with AI in a manner that promotes inclusivity and respect. This includes refraining from requests that could lead to biased or inappropriate outputs. Furthermore, it can help mitigate models learning harmful material from user interactions.

&gt;&gt;主流观点的放大:由于训练数据通常包含更多来自主流文化或群体的内容，模型可能更偏向于这些观点，可能会低估或歪曲少数人的观点。

&gt;&gt;用户指南:还指导用户如何以促进包容性和尊重的方式与人工智能进行交互。这包括避免提出可能导致有偏见或不适当产出的要求。此外，它可以帮助减轻模型从用户交互中学习有害材料的情况。



##### **<strong><strong>纠正偏见的努力:**</strong></strong>

###### **多样和包容的训练数据、偏见检测和修正、道德准则和政策、多样性代表、偏见缓解、文化敏感性、可访问性、语言包容性、道德和尊重的互动、用户反馈和适应、符合包容性准则**

&gt;&gt; 多样和包容的训练数据： 在训练数据中包含更多多样和包容的来源，以减少偏见。

&gt;&gt; 偏见检测和修正： 不断进行研究以检测和修正模型响应中的偏见。

&gt;&gt; 道德准则和政策： 模型受到旨在减轻偏见并确保尊重和包容互动的道德准则和政策的指导。

&gt;&gt; 多样性代表： 确保AI代理生成的内容或提供的响应能够代表广泛的人类经验、文化、族裔和身份。

&gt;&gt; 偏见缓解： 积极努力减少与种族、性别、年龄、残疾、性取向等个人特征相关的偏见，提供公正平衡的响应，不延续刻板印象或偏见。

&gt;&gt; 文化敏感性： AI设计为具有文化敏感性，认可和尊重文化规范、实践和价值观的多样性。

&gt;&gt; 可访问性： 确保AI代理对具有不同能力的用户可访问，包括视觉、听觉、运动或认知障碍的人。这可能涉及整合使交互更容易的功能。

&gt;&gt; 语言包容性： 支持多种语言和方言，以满足全球用户群，并对语言内的细微差别和变化保持敏感。

&gt;&gt; 道德和尊重的互动： 编程使代理与所有用户道德和尊重地互动，避免可能被视为冒犯、有害或不尊重的响应。

&gt;&gt; 用户反馈和适应： 结合用户反馈不断改进AI代理的包容性和效果，学习如何更好地理解和服务多样的用户群体。

&gt;&gt; 符合包容性准则： 遵循由行业团体、伦理委员会或监管机构制定的AI代理包容性准则和标准。


<td style="vertical-align:top;width:258.45pt;"> Despite these measures, AI agents still exhibit biases. Ongoing efforts in agent AI research and development are focused on further reducing these biases and enhancing the inclusivity and fairness of agent AI systems. Efforts to Mitigate Biases: &gt;&gt;Diverse and Inclusive Training Data: Efforts are made to include a more diverse and inclusive range of sources in the training data. &gt;&gt;Bias Detection and Correction: Ongoing research focuses on detecting and correcting biases in model responses. &gt;&gt;Ethical Guidelines and Policies: Models are often governed by ethical guidelines and policies designed to mitigate biases and ensure respectful and inclusive interactions. &gt;&gt;Diverse Representation: Ensuring that the content generated or the responses provided by the AI agent represent a wide range of human experiences, cultures, ethnicities, and identities. This is particularly relevant in scenarios like image generation or narrative construction. &gt;&gt;Bias Mitigation: Actively working to reduce biases in the AI’s responses. This includes biases related to race, gender, age, disability, sexual orientation, and other personal characteristics. The goal is to provide fair and balanced responses that do not perpetuate stereotypes or prejudices. &gt;&gt;Cultural Sensitivity: The AI is designed to be culturally sensitive, acknowledging and respecting the diversity of cultural norms, practices, and values. This includes understanding and appropriately responding to cultural references and nuances. &gt;&gt;Accessibility: Ensuring that the AI agent is accessible to users with different abilities, including those with disabilities. This can involve incorporating features that make interactions easier for people with visual, auditory, motor, or cognitive impairments. &gt;&gt;Language-based Inclusivity: Providing support for multiple languages and dialects to cater to a global user base, and being sensitive to the nuances and variations within a language (Liu et al., 2023b). &gt;&gt;Ethical and Respectful Interactions: The Agent is programmed to interact ethically and respectfully with all users, avoiding responses that could be deemed offensive, harmful, or disrespectful. &gt;&gt;User Feedback and Adaptation: Incorporating user feedback to continually improve the inclusivity and effectiveness of the AI agent. This includes learning from interactions to better understand and serve a diverse user base. &gt;&gt;Compliance with Inclusivity Guidelines: Adhering to established guidelines and standards for inclusivity in AI agent, which are often set by industry groups, ethical boards, or regulatory bodies. </td><td style="vertical-align:top;width:167.65pt;"> 尽管采取了这些措施，AI代理仍然表现出偏见。正在进行的人工智能研究和开发工作的重点是进一步减少这些偏见，增强人工智能系统的包容性和公平性。减少偏见的努力: &gt;&gt;多样化和包容性培训数据:努力在培训数据中纳入更多样化和包容性的来源。 &gt;&gt;偏差检测和纠正:正在进行的研究重点是检测和纠正模型反应中的偏差。 &gt;&gt;道德准则和政策:模型通常受道德准则和政策的约束，这些准则和政策旨在减轻偏见，确保尊重和包容的互动。 多样化代表:确保AI代理生成的内容或提供的响应代表广泛的人类经验、文化、种族和身份。这在图像生成或叙事构建等场景中尤为重要。 &gt;&gt;减少偏见:积极努力减少AI反应中的偏见。这包括与种族、性别、年龄、残疾、性取向和其他个人特征有关的偏见。目标是提供公平和平衡的回应，而不是使陈规定型观念或偏见永久化。 &gt;&gt;文化敏感性:人工智能被设计为具有文化敏感性，承认并尊重文化规范、实践和价值观的多样性。这包括理解和适当地回应文化参考和细微差别。 &gt;&gt;可访问性:确保具有不同能力的用户(包括残疾人)可以访问AI代理。这可以包括整合功能，使视觉、听觉、运动或认知障碍的人更容易互动。 &gt;&gt;基于语言的包容性:为多种语言和方言提供支持，以迎合全球用户群，并对语言中的细微差别和变化敏感(Liu et al.， 2023b)。 &gt;&gt;道德和尊重的互动:代理被编程为与所有用户进行道德和尊重的互动，避免可能被视为冒犯、有害或不尊重的回应。 &gt;&gt;用户反馈和适应:结合用户反馈，不断提高AI代理的包容性和有效性。这包括从交互中学习，以更好地理解和服务不同的用户群。 &gt;&gt;遵守包容性准则:遵守AI代理中包容性的既定准则和标准，这些准则和标准通常由行业团体、道德委员会或监管机构制定。 </td>

&gt;&gt;Diverse and Inclusive Training Data: Efforts are made to include a more diverse and inclusive range of sources in the training data.

&gt;&gt;Ethical Guidelines and Policies: Models are often governed by ethical guidelines and policies designed to mitigate biases and ensure respectful and inclusive interactions.

&gt;&gt;Bias Mitigation: Actively working to reduce biases in the AI’s responses. This includes biases related to race, gender, age, disability, sexual orientation, and other personal characteristics. The goal is to provide fair and balanced responses that do not perpetuate stereotypes or prejudices.

&gt;&gt;Accessibility: Ensuring that the AI agent is accessible to users with different abilities, including those with disabilities. This can involve incorporating features that make interactions easier for people with visual, auditory, motor, or cognitive impairments.

&gt;&gt;Ethical and Respectful Interactions: The Agent is programmed to interact ethically and respectfully with all users, avoiding responses that could be deemed offensive, harmful, or disrespectful.

&gt;&gt;Compliance with Inclusivity Guidelines: Adhering to established guidelines and standards for inclusivity in AI agent, which are often set by industry groups, ethical boards, or regulatory bodies.

&gt;&gt;多样化和包容性培训数据:努力在培训数据中纳入更多样化和包容性的来源。

&gt;&gt;道德准则和政策:模型通常受道德准则和政策的约束，这些准则和政策旨在减轻偏见，确保尊重和包容的互动。

&gt;&gt;减少偏见:积极努力减少AI反应中的偏见。这包括与种族、性别、年龄、残疾、性取向和其他个人特征有关的偏见。目标是提供公平和平衡的回应，而不是使陈规定型观念或偏见永久化。

&gt;&gt;可访问性:确保具有不同能力的用户(包括残疾人)可以访问AI代理。这可以包括整合功能，使视觉、听觉、运动或认知障碍的人更容易互动。

&gt;&gt;道德和尊重的互动:代理被编程为与所有用户进行道德和尊重的互动，避免可能被视为冒犯、有害或不尊重的回应。

&gt;&gt;遵守包容性准则:遵守AI代理中包容性的既定准则和标准，这些准则和标准通常由行业团体、道德委员会或监管机构制定。



##### **<strong><strong>Agent AI包容性的首要目标：创建一个**</strong>**<strong>尊重所有用户的**</strong>**<strong>A**</strong>**<strong>gent **</strong></strong>
<td style="vertical-align:top;width:258.45pt;"> Despite these efforts, it’s important to be aware of the potential for biases in responses and to interpret them with critical thinking. Continuous improvements in AI agent technology and ethical practices aim to reduce these biases over time. One of the overarching goals for inclusivity in agent AI is to create an agent that is respectful and accessible to all users, regardless of their background or identity. </td><td style="vertical-align:top;width:167.65pt;"> 尽管有这些努力，但我们需要意识到回应中存在潜在偏见的可能性，并用批判性思维来解释它们。随着时间的推移，AI代理技术和道德实践的不断改进旨在减少这些偏见。Agent AI包容性的首要目标之一是创建一个**<strong>尊重所有用户的代理**</strong>，无论他们的背景或身份如何。 </td>

尽管有这些努力，但我们需要意识到回应中存在潜在偏见的可能性，并用批判性思维来解释它们。随着时间的推移，AI代理技术和道德实践的不断改进旨在减少这些偏见。Agent AI包容性的首要目标之一是创建一个**<strong>尊重所有用户的代理**</strong>，无论他们的背景或身份如何。







#### **2.2.3 Data Privacy and Usage****数据隐私和使用**

##### **<strong><strong>数据收集、使用和目的，**</strong>**<strong>存储和安全**</strong>**<strong>，**</strong>**<strong>数据删除和保留**</strong>**<strong>，**</strong>**<strong>数据可移植性和隐私政策**</strong>**<strong>，**</strong>**<strong>匿名化**</strong></strong>

**<strong>&gt;&gt; 数据收集、使用和目的**</strong>： AI代理在生产和与用户互动中收集数据，包括文本输入、用户使用模式、个人偏好和敏感信息。用户应了解数据收集的内容和用途，并有权纠正错误信息。

**<strong>&gt;&gt; 存储和安全**</strong>： 开发者应知道用户互动数据存储在何处，采取何种安全措施，以防止未经授权的访问或违规行为。数据的分享需透明，并通常需要用户同意。

**<strong>&gt;&gt; 数据删除和保留**</strong>： 用户需了解用户数据存储时间，有权要求删除数据，符合数据保护法规，如欧盟的GDPR或加利福尼亚州的CCPA。

**<strong>&gt;&gt; 数据可移植性和隐私政策**</strong>： 开发者需创建AI代理的隐私政策，详细说明数据的处理方式、用户权利和获得用户同意的重要性。

**<strong>&gt;&gt; 匿名化**</strong>： 对于用于更广泛分析或AI训练的数据，最好进行匿名化处理以保护个体身份。

总结：理解AI代理的数据隐私涉及了对用户数据的收集、使用、存储和保护的认知，确保用户理解他们在访问、更正和删除数据方面的权利。对于综合了解数据隐私，对于用户和AI代理的数据检索机制的意识也至关重要。
<td style="vertical-align:top;width:237.7pt;"> One key ethical consideration of AI agents involves comprehending how these systems handle, store, and potentially retrieve user data. We discuss key aspects below: </td><td style="vertical-align:top;width:188.4pt;"> AI代理的一个关键伦理考虑涉及理解这些系统如何处理、存储和潜在地检索用户数据。我们讨论以下关键方面: </td>

AI代理的一个关键伦理考虑涉及理解这些系统如何处理、存储和潜在地检索用户数据。我们讨论以下关键方面:
<td style="vertical-align:top;width:237.7pt;"> Data Collection, Usage and Purpose. When using user data to improve model performance, model developers access the data the AI agent has collected while in production and interacting with users. Some systems allow users to view their data through user accounts or by making a request to the service provider. It is important to recognize what data the AI agent collects during these interactions. This could include text inputs, user usage patterns, personal preferences, and sometimes more sensitive personal information. Users should also understand how the data collected from their interactions is used. If, for some reason, the AI holds incorrect information about a particular person or group, there should be a mechanism for users to help correct this once identified. This is important for both accuracy and to be respectful of all users and groups. Common uses for retrieving and analyzing user data include improving user interaction, personalizing responses, and system optimization. It is extremely important for developers to ensure the data is not used for purposes that users have not consented to, such as unsolicited marketing. </td><td style="vertical-align:top;width:188.4pt;"> 资料收集、使用及目的。当使用用户数据来提高模型性能时，模型开发人员访问AI代理在生产和与用户交互时收集的数据。有些系统允许用户通过用户帐户或向服务提供者提出请求来查看他们的数据。识别AI代理在这些交互过程中收集的数据非常重要。这可能包括文本输入、用户使用模式、个人偏好，有时还包括更敏感的个人信息。用户还应该了解如何使用从他们的交互中收集的数据。如果由于某种原因，人工智能持有关于特定个人或群体的不正确信息，则应该有一种机制让用户在识别后帮助纠正这一错误。这对于准确性和尊重所有用户和群体都很重要。检索和分析用户数据的常见用途包括改进用户交互、个性化响应和系统优化。对于开发者来说，确保数据不会被用于用户不同意的目的(如未经请求的营销)是非常重要的。 </td>

资料收集、使用及目的。当使用用户数据来提高模型性能时，模型开发人员访问AI代理在生产和与用户交互时收集的数据。有些系统允许用户通过用户帐户或向服务提供者提出请求来查看他们的数据。识别AI代理在这些交互过程中收集的数据非常重要。这可能包括文本输入、用户使用模式、个人偏好，有时还包括更敏感的个人信息。用户还应该了解如何使用从他们的交互中收集的数据。如果由于某种原因，人工智能持有关于特定个人或群体的不正确信息，则应该有一种机制让用户在识别后帮助纠正这一错误。这对于准确性和尊重所有用户和群体都很重要。检索和分析用户数据的常见用途包括改进用户交互、个性化响应和系统优化。对于开发者来说，确保数据不会被用于用户不同意的目的(如未经请求的营销)是非常重要的。
<td style="vertical-align:top;width:237.7pt;"> Storage and Security. Developers should know where the user interaction data is stored and what security measures are in place to protect it from unauthorized access or breaches. This includes encryption, secure servers, and data protection protocols. It is extremely important to determine if agent data is shared with third parties and under what conditions. This should be transparent and typically requires user consent. Data Deletion and Retention. It is also important for users to understand how long user data is stored and how users can request its deletion. Many data protection laws give users the right to be forgotten, meaning they can request their data be erased. AI agents must adhere to data protection laws like GDPR in the EU or CCPA in California. These laws govern data handling practices and user rights regarding their personal data. </td><td style="vertical-align:top;width:188.4pt;"> 存储和安全。开发人员应该知道用户交互数据存储在哪里，以及采取了哪些安全措施来防止未经授权的访问或破坏。这包括加密、安全服务器和数据保护协议。确定是否与第三方共享代理数据以及在什么条件下共享代理数据是极其重要的。这应该是透明的，通常需要用户同意。 数据删除和保留。对于用户来说，了解用户数据的存储时间以及用户如何请求删除数据也很重要。许多数据保护法赋予用户被遗忘的权利，这意味着他们可以要求删除自己的数据。AI代理必须遵守数据保护法，如欧盟的GDPR或加州的CCPA。这些法律规管有关个人资料的资料处理实务及使用者权利。  </td>

Data Deletion and Retention. It is also important for users to understand how long user data is stored and how users can request its deletion. Many data protection laws give users the right to be forgotten, meaning they can request their data be erased. AI agents must adhere to data protection laws like GDPR in the EU or CCPA in California. These laws govern data handling practices and user rights regarding their personal data.

数据删除和保留。对于用户来说，了解用户数据的存储时间以及用户如何请求删除数据也很重要。许多数据保护法赋予用户被遗忘的权利，这意味着他们可以要求删除自己的数据。AI代理必须遵守数据保护法，如欧盟的GDPR或加州的CCPA。这些法律规管有关个人资料的资料处理实务及使用者权利。
<td style="vertical-align:top;width:237.7pt;"> Data Portability and Privacy Policy. Furthermore, developers must create the AI agent’s privacy policy to document and explain to users how their data is handled. This should detail data collection, usage, storage, and user rights. Developers should ensure that they obtain user consent for data collection, especially for sensitive information. Users typically have the option to opt-out or limit the data they provide. In some jurisdictions, users may even have the right to request a copy of their data in a format that can be transferred to another service provider. Anonymization. For data used in broader analysis or AI training, it should ideally be anonymized to protect individual identities. Developers must understand how their AI agent retrieves and uses historical user data during interactions. This could be for personalization or improving response relevance. </td><td style="vertical-align:top;width:188.4pt;"> 数据可移植性和隐私政策。此外，开发人员必须创建AI代理的隐私策略，以记录并向用户解释他们的数据是如何处理的。这应该详细说明数据收集、使用、存储和用户权限。开发人员应该确保在收集数据时获得用户的同意，尤其是敏感信息。用户通常可以选择退出或限制他们提供的数据。在某些司法管辖区，用户甚至可能有权要求以可转移给另一个服务提供商的格式复制其数据。 匿名化。对于用于更广泛分析或人工智能训练的数据，理想情况下应该匿名以保护个人身份。开发人员必须了解他们的AI代理如何在交互过程中检索和使用历史用户数据。这可能是为了个性化或提高响应相关性。 </td>

Anonymization. For data used in broader analysis or AI training, it should ideally be anonymized to protect individual identities. Developers must understand how their AI agent retrieves and uses historical user data during interactions. This could be for personalization or improving response relevance.

匿名化。对于用于更广泛分析或人工智能训练的数据，理想情况下应该匿名以保护个人身份。开发人员必须了解他们的AI代理如何在交互过程中检索和使用历史用户数据。这可能是为了个性化或提高响应相关性。
<td style="vertical-align:top;width:237.7pt;"> In summary, understanding data privacy for AI agents involves being aware of how user data is collected, used, stored, and protected, and ensuring that users understand their rights regarding accessing, correcting, and deleting their data. Awareness of the mechanisms for data retrieval, both by users and the AI agent, is also crucial for a comprehensive understanding of data privacy. </td><td style="vertical-align:top;width:188.4pt;"> 总之，理解AI代理的数据隐私包括了解用户数据的收集、使用、存储和保护方式，并确保用户了解他们在访问、更正和删除数据方面的权利。用户和AI代理对数据检索机制的认识对于全面理解数据隐私也至关重要。 </td>

总之，理解AI代理的数据隐私包括了解用户数据的收集、使用、存储和保护方式，并确保用户了解他们在访问、更正和删除数据方面的权利。用户和AI代理对数据检索机制的认识对于全面理解数据隐私也至关重要。





#### **2.2.4 Interpretability and Explainability****可理解性****和可解释性**

模仿学习通过无限记忆代理和上下文提示或隐式奖励函数解耦，使代理能够学习一般性策略，适应不同任务。 &gt;&gt;解耦进一步实现了泛化，使代理能够泛化到不同环境，实现转移学习。 &gt;&gt;泛化促使新兴属性或行为的出现，通过识别基本元素或规则，并观察其相互作用，从而导致复杂行为的产生。这一过程使系统能够适应新情境，展现了从简单规则到复杂行为的新兴特性。

本文介绍了模仿学习的解耦和泛化方法，以提高智能体的探索和适应能力。

&gt;&gt;通过解耦，智能体可以从专家演示中学习一般政策，而不是依赖于任务特定的奖励函数。

&gt;&gt;通过泛化，智能体可以在不同复杂度级别上学习一般原则，导致涌现特性。这种方法可以提高智能体的适应能力和泛化能力。

##### **<strong><strong>模仿学习→解耦：**</strong>**<strong>无限记忆代理**</strong>**<strong>通过模仿学习从**</strong>**<strong>专家数据**</strong>**<strong>中学习策略，改善对未知环境的探索和利用。解耦通过**</strong>**<strong>上下文提示**</strong>**<strong>或隐式**</strong>**<strong>奖励函数**</strong>**<strong>学习代理，克服传统模仿学习的缺点，使代理更适应各种情况**</strong></strong>
<td style="vertical-align:top;width:237.7pt;"> Imitation Learning → Decoupling. Agents are typically trained using a continuous feedback loop in Reinforcement Learning (RL) or Imitation Learning (IL), starting with a randomly initialized policy. However, this approach faces leader-board in obtaining initial rewards in unfamiliar environments, particularly when rewards are sparse or only available at the end of a long-step interaction. Thus, a superior solution is to use an infinite-memory agent trained through IL, which can learn policies from expert data, improving exploration and utilization of unseen environmental space with emergent infrastructure as shown in Fig. 3. With expert characteristics to help the agent explore better and utilize the unseen environmental space. Agent AI, can learn policies and new paradigm flow directly from expert data. </td><td style="vertical-align:top;width:188.4pt;"> 模仿学习→解耦。智能体通常在强化学习(RL)或模仿学习(IL)中使用连续反馈循环进行训练，从随机初始化策略开始。然而，这种方法在不熟悉的环境中获得初始奖励时面临着排行榜的问题，特别是当奖励很少或只有在长步骤互动结束时才能获得时。因此，一个更好的解决方案是使用通过IL训练的无限内存代理，它可以从专家数据中学习策略，通过紧急基础设施提高对未知环境空间的探索和利用，如图3所示。具有专家特征，帮助智能体更好地探索和利用不可见的环境空间。Agent AI，可以直接从专家数据中学习政策和新范式流。  </td>

模仿学习→解耦。智能体通常在强化学习(RL)或模仿学习(IL)中使用连续反馈循环进行训练，从随机初始化策略开始。然而，这种方法在不熟悉的环境中获得初始奖励时面临着排行榜的问题，特别是当奖励很少或只有在长步骤互动结束时才能获得时。因此，一个更好的解决方案是使用通过IL训练的无限内存代理，它可以从专家数据中学习策略，通过紧急基础设施提高对未知环境空间的探索和利用，如图3所示。具有专家特征，帮助智能体更好地探索和利用不可见的环境空间。Agent AI，可以直接从专家数据中学习政策和新范式流。
<td style="vertical-align:top;width:237.7pt;"> Traditional IL has an agent mimicking an expert demonstrator’s behavior to learn a policy. However, learning the expert policy directly may not always be the best approach, as the agent may not generalize well to unseen situations. To tackle this, we propose learning an agent with in-context prompt or a implicit reward function that captures key aspects of the expert’s behavior, as shown in Fig. 3. This equips the infinite memory agent with physical-world behavior data for task execution, learned from expert demonstrations. It helps overcome existing imitation learning drawbacks like the need for extensive expert data and potential errors in complex tasks. The key idea behind the Agent AI has two parts: 1) the infinite agent that collects physical-world expert demonstrations as state-action pairs and 2) the virtual environment that imitates the agent generator. The imitating agent produces actions that mimic the expert’s behavior, while the agent learns a policy mapping from states to actions by reducing a loss function of the disparity between the expert’s actions and the actions generated by the learned policy </td><td style="vertical-align:top;width:188.4pt;"> 传统的人工智能有一个代理模仿专家演示者的行为来学习策略。然而，直接学习专家策略可能并不总是最好的方法，因为代理可能无法很好地泛化到未知的情况。为了解决这个问题，我们建议学习一个具有上下文提示或隐含奖励函数的代理，该函数捕获专家行为的关键方面，如图3所示。这为无限内存代理提供了用于任务执行的物理世界行为数据，并从专家演示中学习。它有助于克服现有的模仿学习的缺点，如需要大量的专家数据和复杂任务中的潜在错误。Agent AI背后的关键思想有两个部分: 1)无限代理，它收集物理世界的专家演示作为状态-动作对; 2)模仿代理生成器的虚拟环境。 模仿智能体产生模仿专家行为的动作，而智能体通过减少专家行为与学习策略产生的行为之间差异的损失函数来学习从状态到动作的策略映射  </td>

传统的人工智能有一个代理模仿专家演示者的行为来学习策略。然而，直接学习专家策略可能并不总是最好的方法，因为代理可能无法很好地泛化到未知的情况。为了解决这个问题，我们建议学习一个具有上下文提示或隐含奖励函数的代理，该函数捕获专家行为的关键方面，如图3所示。这为无限内存代理提供了用于任务执行的物理世界行为数据，并从专家演示中学习。它有助于克服现有的模仿学习的缺点，如需要大量的专家数据和复杂任务中的潜在错误。Agent AI背后的关键思想有两个部分:

2)模仿代理生成器的虚拟环境。





##### **<strong><strong>解耦→泛化：分离学习过程和任务奖励函数，通过模仿专家行为学习策略，使模型能在不同任务和环境中适应和泛化**</strong></strong>

通过解耦，智能体可以从专家演示中学习一般政策，适应各种情况。

通过从专家演示中学习，避免依赖特定任务奖励函数，使代理能够泛化到不同任务，实现迁移学习，适应性强。解耦使代理能够学习通用性策略，不依赖特定奖励函数，增强对不同环境的鲁棒性和泛化能力。
<td style="vertical-align:top;width:237.7pt;"> Decoupling → Generalization. Rather than relying on a task-specific reward function, the agent learns from expert demonstrations, which provide a diverse set of state-action pairs covering various task aspects. The agent then learns a policy that maps states to actions by imitating the expert’s behavior. Decoupling in imitation learning refers to separating the learning process from the task-specific reward function, allowing the policy to generalize across different tasks without explicit reliance on the task-specific reward function. By decoupling, the agent can learn from expert demonstrations and learn a policy that is adaptable to a variety of situations. Decoupling enables transfer learning, where a policy learned in one domain can adapt to others with minimal fine-tuning. By learning a general policy that is not tied to a specific reward function, the agent can leverage the knowledge it acquired in one task to perform well in other related tasks. Since the agent does not rely on a specific reward function, it can adapt to changes in the reward function or environment without the need for significant retraining. This makes the learned policy more robust and generalizable across different environments. Decoupling in this context refers to the separation of two tasks in the learning process: learning the reward function and learning the optimal policy. </td><td style="vertical-align:top;width:188.4pt;"> 解耦→泛化。智能体不是依赖于特定于任务的奖励函数，而是从专家演示中学习，专家演示提供了涵盖不同任务方面的各种状态-动作对。然后，代理通过模仿专家的行为来学习将状态映射到动作的策略。模仿学习中的解耦是指将学习过程从特定任务的奖励函数中分离出来，允许策略在不同任务之间进行推广，而无需明确依赖特定任务的奖励函数。通过解耦，代理可以从专家演示中学习，并学习适应各种情况的策略。解耦支持迁移学习，在一个领域中学习的策略可以通过最小的微调适应其他领域。通过学习与特定奖励函数无关的一般策略，代理可以利用它在一个任务中获得的知识在其他相关任务中表现良好。由于智能体不依赖于特定的奖励函数，它可以适应奖励函数或环境的变化，而无需进行重大的再培训。这使得学到的策略在不同的环境中更加健壮和一般化。这里的解耦是指学习过程中两个任务的分离:学习奖励函数和学习最优策略。  </td>

解耦→泛化。智能体不是依赖于特定于任务的奖励函数，而是从专家演示中学习，专家演示提供了涵盖不同任务方面的各种状态-动作对。然后，代理通过模仿专家的行为来学习将状态映射到动作的策略。模仿学习中的解耦是指将学习过程从特定任务的奖励函数中分离出来，允许策略在不同任务之间进行推广，而无需明确依赖特定任务的奖励函数。通过解耦，代理可以从专家演示中学习，并学习适应各种情况的策略。解耦支持迁移学习，在一个领域中学习的策略可以通过最小的微调适应其他领域。通过学习与特定奖励函数无关的一般策略，代理可以利用它在一个任务中获得的知识在其他相关任务中表现良好。由于智能体不依赖于特定的奖励函数，它可以适应奖励函数或环境的变化，而无需进行重大的再培训。这使得学到的策略在不同的环境中更加健壮和一般化。这里的解耦是指学习过程中两个任务的分离:学习奖励函数和学习最优策略。

##### **<strong><strong>泛化→新兴行为：从简单规则或元素间的互动中产生复杂行为，模型在不同复杂层面上学习普适原则，促进跨领域知识迁移，导致涌现特性**</strong></strong>

泛化解释了如何从简单组件或规则中产生新兴属性或行为。通过识别系统行为的基本元素或规则，并观察这些简单组件或规则如何相互作用，从而导致复杂行为的产生。

泛化跨越不同复杂性水平，使系统能够学习适用于这些水平的一般原则，从而实现新兴属性。这有助于系统在新情境中适应，展现了从简单规则到复杂行为的新兴过程。
<td style="vertical-align:top;width:260.75pt;"> Generalization → Emergent Behavior. Generalization explains how emergent properties or behaviors can arise from simpler components or rules. The key idea lies in identifying the basic elements or rules that govern the behavior of the system, such as individual neurons or basic algorithms. Consequently, by observing how these simple components or rules interact with one another. These interactions of these components often lead to the emergence of complex behaviors, which are not predictable by examining individual components alone. Generalization across different levels of complexity allows a system to learn general principles applicable across these levels, leading to emergent properties. This enables the system to adapt to new situations, demonstrating the emergence of more complex behaviors from simpler rules. Furthermore, the ability to generalize across different complexity levels facilitates knowledge transfer from one domain to another, which contributes to the emergence of complex behaviors in new contexts as the system adapts </td><td style="vertical-align:top;width:165.35pt;"> 概括→涌现行为。泛化解释了如何从更简单的组件或规则中产生紧急属性或行为。关键思想在于识别控制系统行为的基本元素或规则，例如单个神经元或基本算法。因此，通过观察这些简单的组件或规则如何相互作用。这些组件之间的相互作用经常导致复杂行为的出现，这些行为是无法通过单独检查单个组件来预测的。跨越不同复杂级别的泛化允许系统学习适用于这些级别的一般原则，从而产生紧急属性。这使系统能够适应新的情况，证明从更简单的规则中出现更复杂的行为。此外，跨越不同复杂程度的泛化能力促进了知识从一个领域到另一个领域的转移，这有助于在系统适应的新环境中出现复杂行为 </td>

概括→涌现行为。泛化解释了如何从更简单的组件或规则中产生紧急属性或行为。关键思想在于识别控制系统行为的基本元素或规则，例如单个神经元或基本算法。因此，通过观察这些简单的组件或规则如何相互作用。这些组件之间的相互作用经常导致复杂行为的出现，这些行为是无法通过单独检查单个组件来预测的。跨越不同复杂级别的泛化允许系统学习适用于这些级别的一般原则，从而产生紧急属性。这使系统能够适应新的情况，证明从更简单的规则中出现更复杂的行为。此外，跨越不同复杂程度的泛化能力促进了知识从一个领域到另一个领域的转移，这有助于在系统适应的新环境中出现复杂行为

##### Figure 3: Example of the Emergent Interactive Mechanism using an agent to identify text relevant to the image from candidates. The task involves using a multi-modal AI agent from the web and human-annotated knowledge interaction samples to incorporate external world information.图3:使用代理识别候选图像相关文本的紧急交互机制示例。该任务涉及使用来自网络的多模态AI代理和人类注释的知识交互样本来整合外部世界信息。

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/direct/069c39a554604a7e907e6e8bca0a49be.png" width="1200">





#### **2.2.5 Inference Augmentation****推理增强**

推理增强是提升AI代理商推理能力的关键，通过数据增强、算法增强、人机协作、实时反馈集成、跨领域知识迁移、特定用例定制、伦理和偏见考虑以及持续学习和适应等多种方法实现。这些方法有助于AI在不熟悉或复杂的决策场景中提高性能和准确性，确保其输出结果的可靠性。


<td style="vertical-align:top;width:248.3pt;"> The inference ability of an AI agent lies in its capacity to interpret, predict, and respond based on its training and input data. While these capabilities are advanced and continually improving, it’s important to recognize their limitations and the influence of the underlying data they are trained on. Particularly, in the context of large language models, it refers to its capacity to draw conclusions, make predictions, and generate responses based on the data it has been trained on and the input it receives. Inference augmentation in AI agents refers to enhancing the AI’s natural inference abilities with additional tools, techniques, or data to improve its performance, accuracy, and utility. This can be particularly important in complex decision-making scenarios or when dealing with nuanced or specialized content. We denote particularly important sources for inference augmentation below: </td><td style="vertical-align:top;width:177.8pt;"> AI代理的推理能力在于其基于训练和输入数据的解释、预测和响应能力。虽然这些功能是先进的，并且在不断改进，但重要的是要认识到它们的局限性以及它们所训练的底层数据的影响。特别是，在大型语言模型的上下文中，它指的是它根据训练过的数据和接收到的输入得出结论、做出预测和生成响应的能力。AI代理中的推理增强是指通过额外的工具、技术或数据来增强人工智能的自然推理能力，以提高其性能、准确性和实用性。这在复杂的决策场景或处理微妙或专门的内容时尤为重要。我们在下面列出了特别重要的推理增强源:  </td>

AI代理的推理能力在于其基于训练和输入数据的解释、预测和响应能力。虽然这些功能是先进的，并且在不断改进，但重要的是要认识到它们的局限性以及它们所训练的底层数据的影响。特别是，在大型语言模型的上下文中，它指的是它根据训练过的数据和接收到的输入得出结论、做出预测和生成响应的能力。AI代理中的推理增强是指通过额外的工具、技术或数据来增强人工智能的自然推理能力，以提高其性能、准确性和实用性。这在复杂的决策场景或处理微妙或专门的内容时尤为重要。我们在下面列出了特别重要的推理增强源:



##### **<strong><strong>数据增强：引入额外数据提供更多上下文，帮助AI在不熟悉领域做出更明智推理。 **</strong></strong>

##### **<strong><strong>算法增强：改进AI基础算法以更精准推理，包括更先进的机器学习模型等。 **</strong></strong>
<td style="vertical-align:top;width:248.3pt;"> Data Enrichment. Incorporating additional, often external, data sources to provide more context or background can help the AI agent make more informed inferences, especially in areas where its training data may be limited. For example, AI agents can infer meaning from the context of a conversation or text. They analyze the given information and use it to understand the intent and relevant details of user queries. These models are proficient at recognizing patterns in data. They use this ability to make inferences about language, user behavior, or other relevant phenomena based on the patterns they’ve learned during training. Algorithm Enhancement. Improving the AI’s underlying algorithms to make better inferences. This could involve using more advanced machine learning models, integrating different types of AI (like combining NLP with image recognition), or updating algorithms to better handle complex tasks. Inference in language models involves understanding and generating human language. This includes grasping nuances like tone, intent, and the subtleties of different linguistic constructions. </td><td style="vertical-align:top;width:177.8pt;"> 数据浓缩。结合额外的(通常是外部的)数据源来提供更多的上下文或背景，可以帮助AI代理做出更明智的推断，特别是在其训练数据可能有限的领域。例如，AI代理可以从对话或文本的上下文中推断出意义。他们分析给定的信息，并使用它来理解用户查询的意图和相关细节。这些模型擅长识别数据中的模式。他们利用这种能力对语言、用户行为或其他相关现象进行推断，这些推断是基于他们在训练中所学到的模式。 算法改进。改进人工智能的底层算法，以做出更好的推断。这可能涉及使用更先进的机器学习模型，集成不同类型的人工智能(如将NLP与图像识别相结合)，或更新算法以更好地处理复杂任务。语言模型中的推理涉及理解和生成人类语言。这包括把握语气、意图等细微差别，以及不同语言结构的微妙之处。  </td>

Algorithm Enhancement. Improving the AI’s underlying algorithms to make better inferences. This could involve using more advanced machine learning models, integrating different types of AI (like combining NLP with image recognition), or updating algorithms to better handle complex tasks. Inference in language models involves understanding and generating human language. This includes grasping nuances like tone, intent, and the subtleties of different linguistic constructions.

算法改进。改进人工智能的底层算法，以做出更好的推断。这可能涉及使用更先进的机器学习模型，集成不同类型的人工智能(如将NLP与图像识别相结合)，或更新算法以更好地处理复杂任务。语言模型中的推理涉及理解和生成人类语言。这包括把握语气、意图等细微差别，以及不同语言结构的微妙之处。

##### **<strong><strong>人机协作：在关键领域如伦理和创造性任务中，人类指导可补充AI推理**</strong></strong>

##### **<strong><strong>实时反馈集成：利用实时用户或环境反馈提高推理性能，如AI根据用户反馈调整推荐**</strong></strong>

##### **<strong><strong>跨领域知识迁移：将一个领域的知识应用于另一个领域以改善推理**</strong></strong>

##### **<strong><strong>特定用例定制：针对特定应用或行业定制AI推理能力，如法律分析、医疗诊断。**</strong></strong>


<td style="vertical-align:top;width:254.75pt;"> Human-in-the-Loop (HITL). Involving human input to augment the AI’s inferences can be particularly useful in areas where human judgment is crucial, such as ethical considerations, creative tasks, or ambiguous scenarios. Humans can provide guidance, correct errors, or offer insights that the agent would not be able to infer on its own. Real-Time Feedback Integration. Using real-time feedback from users or the environment to enhance inferences is another promising method for improving performance during inference. For example, an AI might adjust its recommendations based on live user responses or changing conditions in a dynamic system. Or, if the agent is taking actions in a simulated environment that break certain rules, the agent can be dynamically given feedback to help correct itself. Cross-Domain Knowledge Transfer. Leveraging knowledge or models from one domain to improve inferences in another can be particularly helpful when producing outputs within a specialized discipline. For instance, techniques developed for language translation might be applied to code generation, or insights from medical diagnostics could enhance predictive maintenance in machinery. Customization for Specific Use Cases. Tailoring the AI’s inference capabilities for particular applications or industries can involve training the AI on specialized datasets or fine-tuning its models to better suit specific tasks, such as legal analysis, medical diagnosis, or financial forecasting. Since the particular language or information within one domain can greatly contrast with the language from other domains, it can be beneficial to finetune the agent on domain-specific information. </td><td style="vertical-align:top;width:171.35pt;"> Human-in-the-Loop (HITL)。在人类判断至关重要的领域，比如道德考虑、创造性任务或模棱两可的场景，让人类输入来增强人工智能的推理能力尤其有用。人类可以提供指导，纠正错误，或者提供智能体自己无法推断的见解。 实时反馈集成。使用来自用户或环境的实时反馈来增强推理是另一种在推理过程中提高性能的有前途的方法。例如，人工智能可能会根据实时用户响应或动态系统中不断变化的条件调整其建议。或者，如果代理在模拟环境中采取了违反某些规则的行动，代理可以动态地获得反馈以帮助纠正自己。 跨领域知识转移。利用一个领域的知识或模型来改进另一个领域的推论，在产生专业学科的输出时特别有用。例如，为语言翻译开发的技术可以应用于代码生成，或者来自医疗诊断的见解可以增强机器的预测性维护。  针对特定用例的定制。为特定的应用程序或行业定制人工智能的推理能力，包括在专门的数据集上训练人工智能，或微调其模型，以更好地适应特定的任务，如法律分析、医疗诊断或财务预测。由于一个领域内的特定语言或信息可能与其他领域的语言有很大的差异，因此根据特定于领域的信息对代理进行微调是有益的。 </td>

Real-Time Feedback Integration. Using real-time feedback from users or the environment to enhance inferences is another promising method for improving performance during inference. For example, an AI might adjust its recommendations based on live user responses or changing conditions in a dynamic system. Or, if the agent is taking actions in a simulated environment that break certain rules, the agent can be dynamically given feedback to help correct itself.

Customization for Specific Use Cases. Tailoring the AI’s inference capabilities for particular applications or industries can involve training the AI on specialized datasets or fine-tuning its models to better suit specific tasks, such as legal analysis, medical diagnosis, or financial forecasting. Since the particular language or information within one domain can greatly contrast with the language from other domains, it can be beneficial to finetune the agent on domain-specific information.

实时反馈集成。使用来自用户或环境的实时反馈来增强推理是另一种在推理过程中提高性能的有前途的方法。例如，人工智能可能会根据实时用户响应或动态系统中不断变化的条件调整其建议。或者，如果代理在模拟环境中采取了违反某些规则的行动，代理可以动态地获得反馈以帮助纠正自己。





##### **<strong><strong>伦理和偏见考虑：确保增强过程不引入新偏见或伦理问题，考虑数据源和算法对公平性的影响**</strong></strong>

##### **<strong><strong>持续学习和适应：定期更新AI能力，以跟上发展、数据变化和用户需求**</strong></strong>
<td style="vertical-align:top;width:248.3pt;"> Ethical and Bias Considerations. It is important to ensure that the augmentation process does not introduce new biases or ethical issues. This involves careful consideration of the sources of additional data or the impact of the new inference augmentation algorithms on fairness and transparency. When making inferences, especially about sensitive topics, AI agents must sometimes navigate ethical considerations. This involves avoiding harmful stereotypes, respecting privacy, and ensuring fairness. Continuous Learning and Adaptation. Regularly updating and refining the AI’s capabilities to keep up with new developments, changing data landscapes, and evolving user needs. </td><td style="vertical-align:top;width:177.8pt;"> 道德和偏见考虑。重要的是要确保扩增过程不会引入新的偏见或伦理问题。这包括仔细考虑额外数据的来源或新的推理增强算法对公平性和透明度的影响。在进行推理时，特别是在敏感话题上，AI代理有时必须考虑道德因素。这包括避免有害的刻板印象、尊重隐私和确保公平。 持续学习和适应。定期更新和完善人工智能的能力，以跟上新的发展、不断变化的数据环境和不断发展的用户需求。  </td>

Continuous Learning and Adaptation. Regularly updating and refining the AI’s capabilities to keep up with new developments, changing data landscapes, and evolving user needs.

持续学习和适应。定期更新和完善人工智能的能力，以跟上新的发展、不断变化的数据环境和不断发展的用户需求。
<td style="vertical-align:top;width:248.3pt;"> In summmary, winference augmentation in AI agents involves methods in which their natural inference abilities can be enhanced through additional data, improved algorithms, human input, and other techniques. Depending on the use-case, this augmentation is often essential for dealing with complex tasks and ensuring accuracy in the agent’s outputs. </td><td style="vertical-align:top;width:177.8pt;"> 综上所述，人工智能智能体的推理增强包括通过额外的数据、改进的算法、人工输入和其他技术来增强其自然推理能力的方法。根据用例的不同，这种增强对于处理复杂任务和确保代理输出的准确性通常是必不可少的。 </td>

综上所述，人工智能智能体的推理增强包括通过额外的数据、改进的算法、人工输入和其他技术来增强其自然推理能力的方法。根据用例的不同，这种增强对于处理复杂任务和确保代理输出的准确性通常是必不可少的。





#### **2.2.6 Regulation****监管**

##### **<strong><strong>开发利用LLM或VLM的下一代AI驱动的**</strong>**<strong>人机交互**</strong>**<strong>管道：与机器的**</strong>**<strong>有效沟通**</strong>**<strong>和互动，**</strong>**<strong>对话能力**</strong>**<strong>来识别并满足人类需求，并采用提示工程、高层级验证来限制**</strong></strong>

文章提出了一个利用LLM或VLM的下一代AI驱动的人机交互管道，旨在与人类玩家有意义地交流和互动。为了应对LLM/VLM的不确定性问题，文章提出了提示工程和高层级验证等方法，以确保系统的稳定运行。

为了加快代理AI的开发并简化工作流程，提出了开发新一代AI赋能的代理交互管道。该系统将实现人与机器的有效沟通和互动，利用LLM或VLM的对话能力来识别并满足人类需求，并在请求时执行适当动作。在物理机器人设置中，由于LLM/VLM输出的不可预测性，采用了提示工程来限制其关注点，并包含解释性文本以提高输出的稳定性和可理解性。此外，通过实施预执行验证和修改功能，可在人类指导下更有效地操作系统。


<td style="vertical-align:top;width:253.85pt;"> Recently, Agent AI has made significant advancements, and its integration into embodied systems has opened new possibilities for interacting with agents via more immersive, dynamic, and engaging experiences. To expedite the process and ease the cumbersome work in agent AI developing, we are proposing to develop the next-generation AI-empowered pipeline for agent interaction. Develop a human-machine collaboration system where humans and machines can communicate and interact meaningfully. The system can leverage the LLM’s or VLM dialog capabilities and vast action to talk with human players and identify human needs. Then it will perform proper actions to help human players upon request. </td><td style="vertical-align:top;width:172.25pt;"> 最近，Agent工智能取得了重大进展，它与嵌入系统的集成为通过更加身临其境、动态和引人入胜的体验与代理交互开辟了新的可能性。为了加快流程并简化人工智能开发中的繁琐工作，我们建议开发下一代人工智能智能交互管道。开发人机协作系统，使人和机器能够进行有意义的交流和交互。该系统可以利用LLM或VLM的对话功能和广泛的行动与人类玩家交谈，并确定人类的需求。然后，它将执行适当的行动，以帮助人类玩家的请求。  </td>

最近，Agent工智能取得了重大进展，它与嵌入系统的集成为通过更加身临其境、动态和引人入胜的体验与代理交互开辟了新的可能性。为了加快流程并简化人工智能开发中的繁琐工作，我们建议开发下一代人工智能智能交互管道。开发人机协作系统，使人和机器能够进行有意义的交流和交互。该系统可以利用LLM或VLM的对话功能和广泛的行动与人类玩家交谈，并确定人类的需求。然后，它将执行适当的行动，以帮助人类玩家的请求。
<td style="vertical-align:top;width:253.85pt;"> When employing LLM/VLMs for a human-machine collaboration system, it is essential to note that these operate as black boxes, generating unpredictable output. This uncertainty can become crucial in a physical setup, such as operating actual robotics. An approach to address this challenge is constraining the focus of the LLM/VLM through prompt engineering. For instance, in robotic task planning from instructions, providing environmental information within the prompt has been reported to yield more stable outputs than relying solely on text (Gramopadhye and Szafir, 2022). This report is supported by the Minsky’s frame theory of AI (Minsky, 1975), suggesting that the problem space to be solved by LLM/VLMs is defined by the given prompts. Another approach is designing prompts to make LLM/VLMs include explanatory text to allow users understand what the model has focused on or recognized. Additionally, implementing a higher layer that allows for pre-execution verification and modification under human guidance can facilitate the operation of systems working under such guidance (Fig. 4). </td><td style="vertical-align:top;width:172.25pt;"> 当在人机协作系统中使用LLM/ vlm时，必须注意这些操作作为黑盒，产生不可预测的输出。这种不确定性在物理设置中可能变得至关重要，例如操作实际的机器人。解决这一挑战的一种方法是通过快速工程来限制LLM/VLM的重点。例如，据报道，在机器人任务规划中，在提示中提供环境信息比仅依赖文本产生更稳定的输出(Gramopadhye和Szafir, 2022)。该报告得到了明斯基人工智能框架理论(Minsky, 1975)的支持，认为LLM/ vlm要解决的问题空间是由给定的提示定义的。另一种方法是设计提示，使LLM/ vlm包含解释性文本，以便用户理解模型关注或识别的内容。此外，实现允许在人类指导下进行执行前验证和修改的更高层，可以促进在这种指导下工作的系统的运行(图4)。 </td>

当在人机协作系统中使用LLM/ vlm时，必须注意这些操作作为黑盒，产生不可预测的输出。这种不确定性在物理设置中可能变得至关重要，例如操作实际的机器人。解决这一挑战的一种方法是通过快速工程来限制LLM/VLM的重点。例如，据报道，在机器人任务规划中，在提示中提供环境信息比仅依赖文本产生更稳定的输出(Gramopadhye和Szafir, 2022)。该报告得到了明斯基人工智能框架理论(Minsky, 1975)的支持，认为LLM/ vlm要解决的问题空间是由给定的提示定义的。另一种方法是设计提示，使LLM/ vlm包含解释性文本，以便用户理解模型关注或识别的内容。此外，实现允许在人类指导下进行执行前验证和修改的更高层，可以促进在这种指导下工作的系统的运行(图4)。



##### Figure 4: A robot teaching system developed in (Wake et al., 2023c). (Left) The system workflow. The process involves three steps: Task planning, where ChatGPT plans robotic tasks from instructions and environmental information; Demonstration, where the user visually demonstrates the action sequence. All the steps are reviewed by the user, and if any step fails or shows deficiencies, the previous steps can be revisited as necessary. (Right) A web application that enables uploading of demonstration data and the interaction between the user and ChatGPT.图4:在(Wake et al.， 2023c)开发的机器人教学系统。(左)系统工作流程。这个过程包括三个步骤:任务规划，ChatGPT根据指令和环境信息计划机器人的任务;演示，用户直观地演示操作顺序。所有步骤都由用户审查，如果任何步骤失败或显示缺陷，则可以根据需要重新访问前面的步骤。(右)一个网络应用程序，可以上传演示数据和用户与ChatGPT之间的交互。

<img alt="" height="694" src="https://img-blog.csdnimg.cn/direct/40ae4a38db0a48c1b635774f8bce623f.png" width="1165">







### **2.3 Agent AI for Emergent Abilities****涌现****能力的****人工智能代理**

#### **提出一种利用通用模型知识实现人机新交互场景的方法，探索混合现实下知识推断机制协助复杂环境任务解决**

&gt;&gt; 当前方法难泛化新环境任务：需要为每个领域收集大量数据增强模型

&gt;&gt; 建立知识记忆交互代理：利用通用基础模型知识在人机合作新场景生成交互

&gt;&gt; 发现混合现实知识推断交互机制：结合不同模式下微观反应和宏观行为促进多样任务解决

&gt;&gt; 研究知识引导交互效应：集成OpenAI模型展示系统在新设置下提升基础模型总体提出一种利用通用模型知识实现人机新交互场景的方法，探索混合现实下知识推断机制协助复杂环境任务解决。
<td style="vertical-align:top;width:255.7pt;"> Despite the growing adoption of interactive agent AI systems, the majority of proposed methods still face a challenge in terms of their generalization performance in unseen environments or scenarios. Current modeling practices require developers to prepare large datasets for each domain to finetune/pretrain models; however, this process is costly and even impossible if the domain is new. To address this issue, we build interactive agents that leverage the knowledge-memory of general-purpose foundation models (ChatGPT, Dall-E, GPT-4, etc.) for a novel scenario, specifically for generating a collaboration space between humans and agents. We discover an emergent mechanism— which we name Mixed Reality with Knowledge Inference Interaction—that facilitates collaboration with humans to solve challenging tasks in complex real-world environments and enables the exploration of unseen environments for adaptation to virtual reality. For this mechanism, the agent learns i) micro-reactions in cross-modality: collecting relevant individual knowledge for each interaction task (e.g., understanding unseen scenes) from the explicit web source and by implicitly inferring from the output of pretrained models; ii) macro-behavior in reality-agnostic: improving interactive dimensions and patterns in language and multi-modality domains, and make changes based on characterized roles, certain target variable, influenced diversification of collaborative information in mixed-reality and LLMs. We investigate the task of knowledge-guided interactive synergistic effects to collaborated scene generation with combining various OpenAI models, and show promising results of how the interactive agent system can further boost the large foundation models in our setting. It integrates and improves the depth of generalization, conscious and interpretability of a complex adaptive AI systems. </td><td style="vertical-align:top;width:170.4pt;"> 尽管交互式智能体AI系统的采用越来越多，但大多数提出的方法仍然面临着在未知环境或场景中的泛化性能方面的挑战。当前的建模实践要求开发人员为每个领域准备大型数据集，以微调/预训练模型;然而，如果是新的领域，这个过程是昂贵的，甚至是不可能的。为了解决这个问题，我们为一个新的场景构建了利用通用基础模型(ChatGPT, Dall-E, GPT-4等)的知识记忆的交互式代理，特别是用于生成人类和代理之间的协作空间。我们发现了一种新兴机制——我们将其命名为混合现实与知识推理交互——它促进了与人类的合作，以解决复杂的现实世界环境中的挑战性任务，并使探索看不见的环境能够适应虚拟现实。对于这种机制，智能体学习i)跨模态的微反应:从显式web源收集每个交互任务的相关个人知识(例如，理解未见过的场景)，并通过从预训练模型的输出隐式推断;ii)现实不可知的宏观行为:改进语言和多模态域的交互维度和模式，并根据角色特征、特定目标变量对混合现实和llm中协同信息的多样化产生影响。我们研究了结合各种OpenAI模型的知识引导交互协同效应对协同场景生成的任务，并展示了交互代理系统如何在我们的设置中进一步增强大型基础模型的有希望的结果。它集成并提高了复杂自适应人工智能系统的泛化、意识和可解释性的深度。 </td>

尽管交互式智能体AI系统的采用越来越多，但大多数提出的方法仍然面临着在未知环境或场景中的泛化性能方面的挑战。当前的建模实践要求开发人员为每个领域准备大型数据集，以微调/预训练模型;然而，如果是新的领域，这个过程是昂贵的，甚至是不可能的。为了解决这个问题，我们为一个新的场景构建了利用通用基础模型(ChatGPT, Dall-E, GPT-4等)的知识记忆的交互式代理，特别是用于生成人类和代理之间的协作空间。我们发现了一种新兴机制——我们将其命名为混合现实与知识推理交互——它促进了与人类的合作，以解决复杂的现实世界环境中的挑战性任务，并使探索看不见的环境能够适应虚拟现实。对于这种机制，智能体学习i)跨模态的微反应:从显式web源收集每个交互任务的相关个人知识(例如，理解未见过的场景)，并通过从预训练模型的输出隐式推断;ii)现实不可知的宏观行为:改进语言和多模态域的交互维度和模式，并根据角色特征、特定目标变量对混合现实和llm中协同信息的多样化产生影响。我们研究了结合各种OpenAI模型的知识引导交互协同效应对协同场景生成的任务，并展示了交互代理系统如何在我们的设置中进一步增强大型基础模型的有希望的结果。它集成并提高了复杂自适应人工智能系统的泛化、意识和可解释性的深度。

#### Figure 5: Our proposed new agent paradigm for a multi-modal generalist agent. There are 5 main modules as shown in the figures: 1) Environment and Perception with task-planning and skill observation; 2) Agent learning; 3) Memory; 4) Agent action; 5) Cognition.图5:我们为多模态多面手智能体提出的新智能体范式。如图所示，主要有5个模块:1)环境与感知，包含任务规划和技能观察;2) Agent学习;3)内存;4)代理行为;5)认知。

<img alt="" height="691" src="https://img-blog.csdnimg.cn/direct/9a54319323e44594989d4310a4a68831.png" width="1200">





## **3 Agent AI Paradigm****人工智能代理****范式**

#### **提出训练Agent AI的新范式和框架：旨在利用预训练模型和策略，支持长期任务规划，包括记忆框架和环境反馈**
<td style="vertical-align:top;width:256.15pt;"> In this section, we discuss a new paradigm and framework for training Agent AI. We seek to accomplish several goals with our proposed framework: &gt;&gt;Make use of existing pre-trained models and pre-training strategies to effectively bootstrap our agents with effective understanding of important modalities, such as text or visual inputs. &gt;&gt;Support for sufficient long-term task-planning capabilities. &gt;&gt;Incorporate a framework for memory that allows for learned knowledge to be encoded and retrieved later. &gt;&gt;Allow for environmental feedback to be used to effectively train the agent to learn which actions to take. We show a high-level new agent diagram outlining the important submodules of such a system in Fig. 5. </td><td style="vertical-align:top;width:169.95pt;"> 在本节中，我们将讨论一个训练Agent AI的新范式和框架。我们希望通过我们提出的框架实现以下几个目标: &gt;&gt;利用现有的预训练模型和预训练策略，有效地引导我们的智能体有效地理解重要的模式，如文本或视觉输入。 &gt;&gt;支持足够的长期任务规划能力。 &gt;&gt;结合一个记忆框架，允许学习到的知识被编码并在以后检索。 &gt;&gt;允许使用环境反馈来有效地训练代理学习采取哪些行动。我们在图5中展示了一个高级的新代理图，概述了这样一个系统的重要子模块。 </td>

&gt;&gt;Make use of existing pre-trained models and pre-training strategies to effectively bootstrap our agents with effective understanding of important modalities, such as text or visual inputs.

&gt;&gt;Incorporate a framework for memory that allows for learned knowledge to be encoded and retrieved later.

在本节中，我们将讨论一个训练Agent AI的新范式和框架。我们希望通过我们提出的框架实现以下几个目标:

&gt;&gt;支持足够的长期任务规划能力。

&gt;&gt;允许使用环境反馈来有效地训练代理学习采取哪些行动。我们在图5中展示了一个高级的新代理图，概述了这样一个系统的重要子模块。





### **3.1 LLMs and VLMs****大语言模型 (LLMs) 和大视觉语言模型 (VLMs)**

#### **使用LLM和VLM模型引导Agent组件：提供任务规划、世界知识、逻辑推理等功能，利用LLM语言模型和VLM视觉模型为代理各组件提供初始化**
<td style="vertical-align:top;width:237.7pt;"> We can use the LLM or VLM model to bootstrap the components of the Agent as showed in Fig. 5. In particular, LLMs have been shown to perform well for task-planning (Gong et al., 2023a), contain significant world knowledge (Yu et al., 2023b), and display impressive logical reasoning capabilities (Creswell et al., 2022). Additionally, VLMs such as CLIP (Radford et al., 2021) provide a general visual encoder that is language-aligned, as well as providing zero-shot visual recognition capabilities. For example, state-of-the-art open-source multi-modal models such as LLaVA (Liu et al., 2023c) and InstructBLIP (Dai et al., 2023) rely upon frozen CLIP models as visual encoders. </td><td style="vertical-align:top;width:188.4pt;"> 我们可以使用LLM或VLM模型来引导Agent的组件，如图5所示。特别是法学硕士在任务规划方面表现良好(Gong等人，2023a)，包含重要的世界知识(Yu等人，2023b)，并表现出令人印象深刻的逻辑推理能力(Creswell等人，2022)。此外，像CLIP这样的vlm (Radford et al.， 2021)提供了一种通用的视觉编码器，该编码器与语言对齐，并提供零镜头视觉识别功能。例如，最先进的开源多模态模型，如LLaVA (Liu et al.， 2023c)和instructlip (Dai et al.， 2023)依赖于冻结的CLIP模型作为视觉编码器。 </td>

我们可以使用LLM或VLM模型来引导Agent的组件，如图5所示。特别是法学硕士在任务规划方面表现良好(Gong等人，2023a)，包含重要的世界知识(Yu等人，2023b)，并表现出令人印象深刻的逻辑推理能力(Creswell等人，2022)。此外，像CLIP这样的vlm (Radford et al.， 2021)提供了一种通用的视觉编码器，该编码器与语言对齐，并提供零镜头视觉识别功能。例如，最先进的开源多模态模型，如LLaVA (Liu et al.， 2023c)和instructlip (Dai et al.， 2023)依赖于冻结的CLIP模型作为视觉编码器。





### **3.2 Agent Transformer Definition****—Agent**** ****Transformer 定义**

#### **Agent Transformer****定义：****是一种替代使用冻结LLMs和VLMs的方法，通过****单****个模型接受视觉、语言和Agent tokens作为输入**

#### **Agent Transformer优势：相对于大型专有LLMs的优势包括定制能力、解释性和潜在的成本优势**
<td style="vertical-align:top;width:249.25pt;"> Instead of using frozen LLMs and VLMs for the AI agent, it is also possible to use a single-agent transformer model that takes visual tokens and language tokens as input, similar to Gato (Reed et al., 2022). In addition to vision and language, we add a third general type of input, which we denote as agent tokens. Conceptually, agent tokens are used to reserve a specific subspace of the input and output space of the model for agentic behaviors. For robotics or game playing, this may be represented as the input action space of the controller. When training agents to use specific tools, such as image-generation or image-editing models, or for other API calls, agent tokens can also be used. As showed in Fig. 7, we can combine the agent tokens with visual and language tokens to generate a unified interface for training multi-modal agent AI. Compared to using large, proprietary LLMs as agents, there are several advantages to using an agent transformer. Firstly, the model can be easily customized to very specific agentic tasks that may be difficult to represent in natural language (e.g. controller inputs or other specific actions). Thus, the agent can learn from environmental interactions and domain-specific data to improve performance. Secondly, it can be easier to understand why the model does or does not take specific actions by having access to the probabilities of the agent tokens. Thirdly,there are certain domains such as healthcare and law that have strict data privacy requirements. Finally, a relatively smaller agent transformer can potentially be significantly cheaper than a larger proprietary language model. </td><td style="vertical-align:top;width:176.85pt;"> 除了为AI代理使用冻结的llm和vlm之外，还可以使用单代理变压器模型，该模型将视觉令牌和语言令牌作为输入，类似于Gato (Reed et al.， 2022)。除了视觉和语言之外，我们还添加了第三种一般类型的输入，我们将其表示为代理令牌。从概念上讲，代理令牌用于为代理行为保留模型输入和输出空间的特定子空间。对于机器人或游戏来说，这可以表示为控制器的输入动作空间。在训练代理使用特定工具(如图像生成或图像编辑模型)或其他API调用时，也可以使用代理令牌。如图7所示，我们可以将agent token与视觉token和语言token结合起来，生成一个统一的界面，用于训练多模态agent AI。 与使用大型专有llm作为代理相比，使用代理转换器有几个优点。首先，该模型可以很容易地定制为非常具体的代理任务，这些任务可能难以用自然语言表示(例如控制器输入或其他特定动作)。因此，代理可以从环境交互和特定领域的数据中学习，以提高性能。其次，通过访问代理令牌的概率，可以更容易地理解模型采取或不采取特定操作的原因。第三，某些领域(如医疗保健和法律)有严格的数据隐私要求。最后，相对较小的代理转换器可能比较大的专有语言模型便宜得多。 </td>

除了为AI代理使用冻结的llm和vlm之外，还可以使用单代理变压器模型，该模型将视觉令牌和语言令牌作为输入，类似于Gato (Reed et al.， 2022)。除了视觉和语言之外，我们还添加了第三种一般类型的输入，我们将其表示为代理令牌。从概念上讲，代理令牌用于为代理行为保留模型输入和输出空间的特定子空间。对于机器人或游戏来说，这可以表示为控制器的输入动作空间。在训练代理使用特定工具(如图像生成或图像编辑模型)或其他API调用时，也可以使用代理令牌。如图7所示，我们可以将agent token与视觉token和语言token结合起来，生成一个统一的界面，用于训练多模态agent AI。

#### Figure 6: We show the current paradigm for creating multi-modal AI agents by incorporating a Large Language Model (LLM) with a Large Vision Model (LVM). Generally, these models take visual or language inputs and use pre-trained and frozen visual and language models, learning smaller sub-network that connect and bridge modalities. Examples include Flamingo (Alayrac et al., 2022), BLIP-2 (Li et al., 2023c), InstructBLIP (Dai et al., 2023), and LLaVA (Liu et al., 2023c).

<img alt="" height="884" src="https://img-blog.csdnimg.cn/direct/a4c335b3c14a417eb7c91e762f396236.png" width="1200">



#### Figure 7: The unified agent multi-modal transformer model. Instead of connecting frozen submodules and using existing foundation models as building blocks, we propose a unified and end-to-end training paradigm for agent systems. We can still initialize the submodules with LLMs and LVMs as in Figure 6 but also make use of agent tokens, specialized tokens for training the model to perform agentic behaviors in a specific domain (e.g., robotics). For more details about agent tokens, see Section 3.2

<img alt="" height="327" src="https://img-blog.csdnimg.cn/direct/914397d1698d4b4da139424bad9653ca.png" width="928">





### **3.3 Agent Transformer Creation****Agent****Transformer 创建**

#### **创建过程：利用基础模型数据训练Agent Transformer，明确目标和行为空间。**

创建：使用LLM和VLM引导的Agent，以及从大型基础模型生成的数据来训练专门为特定任务和领域定制的Agent Transformer模型

训练Agent Transformer的过程包括定义领域内的目标和Agent行为空间，以及持续监控模型性能和收集反馈进行改进。
<td style="vertical-align:top;width:237.7pt;"> As shown above in Fig. 5, we can use the new agent paradigm with LLM and VLM-bootstrapped agents, as well as leveraging data generated from large foundation models to train the agent transformer model for learning to execute specific goals. Within this process, the agent model is trained to be specialized and tailored for specific tasks and domains. This approach allows you to leverage a pre-existing, foundation model’s learned features and knowledge. We show a simplified overview of the process in two steps below: </td><td style="vertical-align:top;width:188.4pt;"> 如上图5所示，我们可以使用新的代理范式与LLM和vlm引导的代理，以及利用从大型基础模型生成的数据来训练代理转换模型，以学习执行特定的目标。在这个过程中，代理模型被训练成专门针对特定的任务和领域进行定制。这种方法允许您利用预先存在的、基础模型的学习特性和知识。我们在下面两个步骤中展示了该过程的简化概述:  </td>

如上图5所示，我们可以使用新的代理范式与LLM和vlm引导的代理，以及利用从大型基础模型生成的数据来训练代理转换模型，以学习执行特定的目标。在这个过程中，代理模型被训练成专门针对特定的任务和领域进行定制。这种方法允许您利用预先存在的、基础模型的学习特性和知识。我们在下面两个步骤中展示了该过程的简化概述:
<td style="vertical-align:top;width:237.7pt;"> Define Objectives within the Domain. In order to train the agent transformer, the objectives and the action-space of the agent within the context of each specific environment needs to be clearly defined. This includes determining which specific tasks or actions the agent needs to perform and assigning unique agent tokens for each. Furthermore, any automatic rules or procedures that can be used to identify successful completion of tasks can significantly improve the amount of data available for training. Otherwise, foundation-model generated or human-annotated data will be required for training the model. After the data is collected and it is possible to evaluate the performance of the agent, the process of continuous improvement can begin. </td><td style="vertical-align:top;width:188.4pt;"> 定义领域内的目标。为了训练智能体转换器，需要明确定义每个特定环境上下文中智能体的目标和动作空间。这包括确定代理需要执行哪些特定的任务或操作，并为每个任务或操作分配唯一的代理令牌。此外，任何可用于识别任务是否成功完成的自动规则或程序都可以显著提高可用于培训的数据量。否则，将需要基础模型生成或人工注释的数据来训练模型。在收集到数据并且可以评估代理的性能之后，可以开始持续改进的过程。  </td>

定义领域内的目标。为了训练智能体转换器，需要明确定义每个特定环境上下文中智能体的目标和动作空间。这包括确定代理需要执行哪些特定的任务或操作，并为每个任务或操作分配唯一的代理令牌。此外，任何可用于识别任务是否成功完成的自动规则或程序都可以显著提高可用于培训的数据量。否则，将需要基础模型生成或人工注释的数据来训练模型。在收集到数据并且可以评估代理的性能之后，可以开始持续改进的过程。



#### **持续改进：监控模型表现，收集反馈以进行微调和更新，确保无偏见和不道德结果**
<td style="vertical-align:top;width:237.7pt;"> Continuous Improvement. Continuous monitoring of the model’s performance and collection of feedback are essential steps in the process. Feedback should be used for further fine-tuning and updates. It is also crucial to ensure that the model does not perpetuate biases or unethical outcomes. This necessitates a careful examination of the training data, regular checks for biases in outputs, and, if needed, training the model to recognize and avoid biases. Once the model achieves satisfactory performance, it can be deployed for the intended application. Continuous monitoring remains vital to ensure that the model performs as expected and to facilitate necessary adjustments. More details on this process, sources of training data, and details surrounding continous learning for agent AI can be found in Section 8. </td><td style="vertical-align:top;width:188.4pt;"> 持续改进。持续监测模型的性能和收集反馈是这个过程中必不可少的步骤。反馈应该用于进一步的微调和更新。确保模型不会延续偏见或不道德的结果也至关重要。这需要仔细检查训练数据，定期检查输出中的偏差，并在必要时训练模型以识别和避免偏差。一旦模型达到了令人满意的性能，就可以将其部署到预期的应用程序中。持续监测对于确保模型按预期运行和促进必要的调整至关重要。关于这个过程的更多细节，训练数据的来源，以及智能体AI持续学习的细节可以在第8节中找到。 </td>

持续改进。持续监测模型的性能和收集反馈是这个过程中必不可少的步骤。反馈应该用于进一步的微调和更新。确保模型不会延续偏见或不道德的结果也至关重要。这需要仔细检查训练数据，定期检查输出中的偏差，并在必要时训练模型以识别和避免偏差。一旦模型达到了令人满意的性能，就可以将其部署到预期的应用程序中。持续监测对于确保模型按预期运行和促进必要的调整至关重要。关于这个过程的更多细节，训练数据的来源，以及智能体AI持续学习的细节可以在第8节中找到。





## **4 Agent AI Learning****人工智能代理**** 学习**

### **4.1 Strategy and Mechanism****策略和机制**


<td style="vertical-align:top;width:237.7pt;"> The strategy of interactive AI on different domains which extends the paradigm of calling large foundation models with a trained agent that actively seeks to collect user feedback, action information, useful knowledge for generation and interaction. Some times, the LLM/VLM models are not need to trained again, and we improve their performance by providing improved contextual prompts at test time for an agent. On the other hand, it always involves a knowledge/reasoning/commonsense/inference interactive modeling through a combination of triple systems - one performing knowledge retrieval from multi-model query, second performing interactive generation from the relevant agent, and last one the trained a new, informative self-supervised training or pre-training with reinforcement learning or imitation learning with improved way. </td><td style="vertical-align:top;width:188.4pt;"> 不同领域的交互式人工智能策略，扩展了调用大型基础模型的范例，该模型具有经过训练的代理，主动寻求收集用户反馈，操作信息，生成和交互的有用知识。有时，LLM/VLM模型不需要再次训练，我们通过在测试时为代理提供改进的上下文提示来提高它们的性能。另一方面，它总是涉及到知识/推理/常识/推理的交互建模，通过三个系统的组合——一个系统从多模型查询中进行知识检索，第二个系统从相关代理中进行交互生成，最后一个系统以改进的方式训练一个新的、信息丰富的自监督训练或强化学习或模仿学习的预训练。 </td>

不同领域的交互式人工智能策略，扩展了调用大型基础模型的范例，该模型具有经过训练的代理，主动寻求收集用户反馈，操作信息，生成和交互的有用知识。有时，LLM/VLM模型不需要再次训练，我们通过在测试时为代理提供改进的上下文提示来提高它们的性能。另一方面，它总是涉及到知识/推理/常识/推理的交互建模，通过三个系统的组合——一个系统从多模型查询中进行知识检索，第二个系统从相关代理中进行交互生成，最后一个系统以改进的方式训练一个新的、信息丰富的自监督训练或强化学习或模仿学习的预训练。





#### **4.1.1 Reinforcement Learning (RL)****强化学习**


<td style="vertical-align:top;width:252.9pt;"> There is a rich history of leveraging reinforcement learning (RL) to train interactive agents that exhibits intelligent behaviors. RL is a methodology to learn the optimal relationship between states and actions based on rewards (or penalties) received as a result of its actions. RL is a highly scalable framework that has been applied to numerous applications including robotics, however, it generally faces several leader-board and LLM/VLMs have shown their potential to mitigate or overcome some of those difficulties: </td><td style="vertical-align:top;width:173.2pt;"> 利用强化学习(RL)来训练表现出智能行为的交互式代理有很长的历史。强化学习是一种学习状态和行为之间最佳关系的方法，这种关系基于其行为所获得的奖励(或惩罚)。RL是一个高度可扩展的框架，已经应用于包括机器人在内的许多应用程序，然而，它通常面临几个领先的问题，LLM/ vlm已经显示出它们缓解或克服这些困难的潜力:  </td>

利用强化学习(RL)来训练表现出智能行为的交互式代理有很长的历史。强化学习是一种学习状态和行为之间最佳关系的方法，这种关系基于其行为所获得的奖励(或惩罚)。RL是一个高度可扩展的框架，已经应用于包括机器人在内的许多应用程序，然而，它通常面临几个领先的问题，LLM/ vlm已经显示出它们缓解或克服这些困难的潜力:
<td style="vertical-align:top;width:252.9pt;"> &gt;&gt;Reward designing The efficiency of policy learning greatly depends on the design of the reward function. Designing the reward function requires not only knowledge of RL algorithms but also a deep understanding of the nature of the task, and thus often necessitates crafting the function based on expert experience. Several studies explored the use of LLM/VLMs for designing reward functions (Yu et al., 2023a; Katara et al., 2023; Ma et al., 2023). &gt;&gt;Data collection and efficiency Given its exploratory nature, RL-based policy learning requires a significant amount of data (Padalkar et al., 2023). The necessity for extensive data becomes particularly evident when the policy involves managing long sequences or integrating complex actions. This is because these scenarios demand more nuanced decision-making and learning from a wider range of situations. In recent studies, efforts have been directed towards enhancing data generation to support policy learning (Kumar et al., 2023; Du et al., 2023). Additionally, in some studies, these models have been integrated into the reward function to improve policy learning (Sontakke et al., 2023). Parallel to these developments, another strand of research has focused on achieving parameter efficiency in learning processes using VLMs (Tang et al., 2023; Li et al., 2023d) and LLMs (Shi et al., 2023) &gt;&gt;Long-horizon steps In relation to the issue of data efficiency, RL becomes more challenging as the length of action sequences increases. This is due to the ambiguity in the relationship between actions and rewards, known as the credit assignment problem, and the increase in the number of states to be explored, necessitating a significant amount of time and data. One typical approach for long and complex tasks is to break them down into a sequence of subgoals and apply pretrained policies to solve each subgoal (e.g., (Takamatsu et al., 2022)). This idea falls within the framework called the task and motion planning (TAMP)(Garrett et al., 2021). TAMP is composed of two primary components: task planning, which entails identifying sequences of high-level actions, and motion planning, which involves finding physically consistent, collision-free trajectories to achieve the objectives of the task plan. </td><td style="vertical-align:top;width:173.2pt;"> 策略学习的效率很大程度上取决于奖励函数的设计。设计奖励函数不仅需要强化学习算法的知识，还需要对任务的本质有深刻的理解，因此通常需要根据专家经验来设计函数。一些研究探索了使用LLM/ vlm来设计奖励函数(Yu et al.， 2023a;Katara et al.， 2023;Ma等人，2023)。 &gt;&gt;数据收集和效率鉴于其探索性，基于强化学习的政策学习需要大量的数据(Padalkar et al.， 2023)。当策略涉及管理长序列或集成复杂操作时，对大量数据的需求变得尤为明显。这是因为这些场景需要更细致的决策和从更广泛的情况中学习。在最近的研究中，努力的方向是加强数据生成以支持政策学习(Kumar等人，2023;Du等人，2023)。此外，在一些研究中，这些模型被集成到奖励函数中，以改善政策学习(Sontakke et al.， 2023)。与这些发展平行的是，另一项研究侧重于使用VLMs在学习过程中实现参数效率(Tang et al.， 2023;Li et al.， 2023)和LLMs (Shi et al.， 2023) 关于数据效率的问题，随着动作序列的长度增加，强化学习变得更具挑战性。这是由于行动和奖励之间关系的模糊性，即信用分配问题，以及需要探索的状态数量的增加，需要大量的时间和数据。对于长而复杂的任务，一种典型的方法是将它们分解成一系列子目标，并应用预先训练好的策略来解决每个子目标(例如，(Takamatsu et al.， 2022))。这个想法属于任务和运动规划(TAMP)的框架(Garrett et al.， 2021)。TAMP由两个主要部分组成:任务规划，它需要确定高级动作序列，以及运动规划，它涉及寻找物理上一致的、无碰撞的轨迹，以实现任务计划的目标。  </td>

&gt;&gt;Data collection and efficiency Given its exploratory nature, RL-based policy learning requires a significant amount of data (Padalkar et al., 2023). The necessity for extensive data becomes particularly evident when the policy involves managing long sequences or integrating complex actions. This is because these scenarios demand more nuanced decision-making and learning from a wider range of situations. In recent studies, efforts have been directed towards enhancing data generation to support policy learning (Kumar et al., 2023; Du et al., 2023). Additionally, in some studies, these models have been integrated into the reward function to improve policy learning (Sontakke et al., 2023). Parallel to these developments, another strand of research has focused on achieving parameter efficiency in learning processes using VLMs (Tang et al., 2023; Li et al., 2023d) and LLMs (Shi et al., 2023)

策略学习的效率很大程度上取决于奖励函数的设计。设计奖励函数不仅需要强化学习算法的知识，还需要对任务的本质有深刻的理解，因此通常需要根据专家经验来设计函数。一些研究探索了使用LLM/ vlm来设计奖励函数(Yu et al.， 2023a;Katara et al.， 2023;Ma等人，2023)。

关于数据效率的问题，随着动作序列的长度增加，强化学习变得更具挑战性。这是由于行动和奖励之间关系的模糊性，即信用分配问题，以及需要探索的状态数量的增加，需要大量的时间和数据。对于长而复杂的任务，一种典型的方法是将它们分解成一系列子目标，并应用预先训练好的策略来解决每个子目标(例如，(Takamatsu et al.， 2022))。这个想法属于任务和运动规划(TAMP)的框架(Garrett et al.， 2021)。TAMP由两个主要部分组成:任务规划，它需要确定高级动作序列，以及运动规划，它涉及寻找物理上一致的、无碰撞的轨迹，以实现任务计划的目标。
<td style="vertical-align:top;width:252.9pt;"> LLMs are well-suited to TAMP, and recent research has often adopted an approach where LLMs are used to execute high-level task planning, while low-level controls are addressed with RL-based policies (Xu et al., 2023; Sun et al., 2023a; Li et al., 2023b; Parakh et al., 2023). The advanced capabilities of LLMs enable them to effectively decompose even abstract instructions into subgoals (Wake et al., 2023c), contributing to the enhancement of language understanding abilities in robotic systems. </td><td style="vertical-align:top;width:173.2pt;"> llm非常适合于tam，最近的研究经常采用一种方法，其中llm用于执行高级任务规划，而低级控制则使用基于rl的策略来解决(Xu et al.， 2023;Sun等，20023a;Li et al.， 2009;Parakh et al.， 2023)。llm的高级功能使它们能够有效地将抽象指令分解为子目标(Wake et al.， 2023c)，有助于提高机器人系统的语言理解能力。 </td>

llm非常适合于tam，最近的研究经常采用一种方法，其中llm用于执行高级任务规划，而低级控制则使用基于rl的策略来解决(Xu et al.， 2023;Sun等，20023a;Li et al.， 2009;Parakh et al.， 2023)。llm的高级功能使它们能够有效地将抽象指令分解为子目标(Wake et al.， 2023c)，有助于提高机器人系统的语言理解能力。







#### **4.1.2 Imitation Learning (IL)****模仿学习**
<td style="vertical-align:top;width:237.7pt;"> While RL aims to train a policy based on exploratory behavior and maximizing rewards through interactions with the environment, imitation learning (IL) seeks to leverage expert data to mimic the actions of experienced agents or experts. For example, in robotics, one of the major frameworks based on IL is Behavioral Cloning (BC). BC is an approach where a robot is trained to mimic the actions of an expert by directly copying them. In this approach, the expert’s actions in performing specific tasks are recorded, and the robot is trained to replicate these actions in similar situations. Recent BC-based methods often incorporate technologies from LLM/VLMs, enabling more advanced end-to-end models. For example, Brohan et al. proposed RT-1 (Brohan et al., 2022) and RT-2 (Brohan et al., 2023), transformer-based models that output an action sequence for the base and arm, taking a series of images and language as input. These models are reported to show high generalization performance as the result of training on a large amount of training data. </td><td style="vertical-align:top;width:188.4pt;"> 强化学习的目标是基于探索性行为来训练策略，并通过与环境的互动来最大化回报，而模仿学习(IL)则旨在利用专家数据来模仿有经验的代理或专家的行为。例如，在机器人技术中，基于IL的主要框架之一是行为克隆(BC)。BC是一种训练机器人通过直接复制专家的动作来模仿他们的方法。在这种方法中，专家在执行特定任务时的动作被记录下来，并训练机器人在类似的情况下复制这些动作。最近基于bc的方法通常结合来自LLM/ vlm的技术，支持更先进的端到端模型。例如，Brohan等人提出了RT-1 (Brohan et al.， 2022)和RT-2 (Brohan et al.， 2023)，这两种基于变压器的模型输出基座和手臂的动作序列，将一系列图像和语言作为输入。据报道，由于对大量训练数据进行了训练，这些模型显示出很高的泛化性能。 </td>

强化学习的目标是基于探索性行为来训练策略，并通过与环境的互动来最大化回报，而模仿学习(IL)则旨在利用专家数据来模仿有经验的代理或专家的行为。例如，在机器人技术中，基于IL的主要框架之一是行为克隆(BC)。BC是一种训练机器人通过直接复制专家的动作来模仿他们的方法。在这种方法中，专家在执行特定任务时的动作被记录下来，并训练机器人在类似的情况下复制这些动作。最近基于bc的方法通常结合来自LLM/ vlm的技术，支持更先进的端到端模型。例如，Brohan等人提出了RT-1 (Brohan et al.， 2022)和RT-2 (Brohan et al.， 2023)，这两种基于变压器的模型输出基座和手臂的动作序列，将一系列图像和语言作为输入。据报道，由于对大量训练数据进行了训练，这些模型显示出很高的泛化性能。



#### **4.1.3 Traditional RGB****传统 RGB**

##### **<strong><strong>利用图像强化智能代理行为的研究方向，增加数据或加入模型偏置等方法改进样本效率问题。**</strong></strong>
<td style="vertical-align:top;width:237.7pt;"> Learning intelligent agent behavior leveraging image inputs has been of interest for many years (Mnih et al., 2015). The inherent challenge of using RGB input is the curse of dimensionality. To solve this problem, researchers either use more data (Jang et al., 2022; Ha et al., 2023) or introduce inductive biases into the model design to improve sample efficiency. In particular, authors incorporate 3D structures into the model architecture for manipulations (Zeng et al., 2021; Shridhar et al., 2023; Goyal et al., 2023; James and Davison, 2022). For robot navigation, authors (Chaplot et al., 2020a,b) leverage maps as a representation. Maps can either be learned from a neural network aggregating all previous RGB inputs or through 3D reconstruction methods such as Neural Radiance Fields (Rosinol et al., 2022). </td><td style="vertical-align:top;width:188.4pt;"> 利用图像输入学习智能代理行为多年来一直受到关注(Mnih et al.， 2015)。使用RGB输入的固有挑战是维度的诅咒。为了解决这个问题，研究人员要么使用更多的数据(Jang et al.， 2022;Ha et al.， 2023)或在模型设计中引入归纳偏置以提高样本效率。特别是，作者将3D结构合并到模型架构中进行操作(Zeng et al.， 2021;Shridhar et al.， 2023;Goyal等人，2023;詹姆斯和戴维森，2022)。对于机器人导航，作者(Chaplot等人，2020a,b)利用地图作为表示。地图可以从聚合所有之前RGB输入的神经网络中学习，也可以通过神经辐射场(neural Radiance Fields)等3D重建方法学习(Rosinol et al.， 2022)。  </td>

利用图像输入学习智能代理行为多年来一直受到关注(Mnih et al.， 2015)。使用RGB输入的固有挑战是维度的诅咒。为了解决这个问题，研究人员要么使用更多的数据(Jang et al.， 2022;Ha et al.， 2023)或在模型设计中引入归纳偏置以提高样本效率。特别是，作者将3D结构合并到模型架构中进行操作(Zeng et al.， 2021;Shridhar et al.， 2023;Goyal等人，2023;詹姆斯和戴维森，2022)。对于机器人导航，作者(Chaplot等人，2020a,b)利用地图作为表示。地图可以从聚合所有之前RGB输入的神经网络中学习，也可以通过神经辐射场(neural Radiance Fields)等3D重建方法学习(Rosinol et al.， 2022)。
<td style="vertical-align:top;width:237.7pt;"> To obtain more data, researchers synthesize synthetic data using graphics simulators (Mu et al., 2021; Gong et al., 2023b), and try to close the sim2real gap (Tobin et al., 2017; Sadeghi and Levine, 2016; Peng et al., 2018). Recently, there has been some collective effort to curate large-scale dataset that aims to resolve the data scarcity problem (Padalkar et al., 2023; Brohan et al., 2023). On the other hand, to improve sample complexity, data augmentation techniques have been extensively studied as well (Zeng et al., 2021; Rao et al., 2020; Haarnoja et al., 2023; Lifshitz et al., 2023). </td><td style="vertical-align:top;width:188.4pt;"> 为了获得更多的数据，研究人员使用图形模拟器合成合成数据(Mu et al.， 2021;Gong et al.， 2023b)，并尝试缩小sim2real差距(Tobin et al.， 2017;Sadeghi and Levine, 2016;Peng et al.， 2018)。最近，有一些集体努力来策划旨在解决数据稀缺问题的大规模数据集(Padalkar等人，2023;Brohan et al.， 2023)。另一方面，为了提高样本复杂度，数据增强技术也得到了广泛的研究(Zeng et al.， 2021;Rao et al.， 2020;Haarnoja et al.， 2023;Lifshitz et al.， 2023)。 </td>

为了获得更多的数据，研究人员使用图形模拟器合成合成数据(Mu et al.， 2021;Gong et al.， 2023b)，并尝试缩小sim2real差距(Tobin et al.， 2017;Sadeghi and Levine, 2016;Peng et al.， 2018)。最近，有一些集体努力来策划旨在解决数据稀缺问题的大规模数据集(Padalkar等人，2023;Brohan et al.， 2023)。另一方面，为了提高样本复杂度，数据增强技术也得到了广泛的研究(Zeng et al.， 2021;Rao et al.， 2020;Haarnoja et al.， 2023;Lifshitz et al.， 2023)。
<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>







#### **4.1.4 In-context Learning****上下文学习**


<td style="vertical-align:top;width:246pt;"> In-context learning was shown to be an effective method for solving tasks in NLP with the advent of large language models like GPT-3 (Brown et al., 2020; Min et al., 2022). Few-shot prompts were seen to be an effective way to contextualize model output’s across a variety of tasks in NLP by providing examples of the task within the context of the LLM prompt. Factors like the diversity of examples and quality of examples shown for the in-context demonstrations may improve the quality of model outputs (An et al., 2023; Dong et al., 2022). Within the context of multi-modal foundation models, models like Flamingo and BLIP-2 (Alayrac et al., 2022; Li et al., 2023c) have been shown to be effective at a variety of visual understanding tasks when given only given a small number of examples. In context learning can be further improved for agents within environments by incorporating environment-specific feedback when certain actions are taken (Gong et al., 2023a). </td><td style="vertical-align:top;width:180.1pt;"> 随着GPT-3等大型语言模型的出现，上下文学习被证明是解决NLP任务的有效方法(Brown et al.， 2020;Min et al.， 2022)。通过在LLM提示的上下文中提供任务的示例，少量提示被认为是将NLP中各种任务的模型输出上下文化的有效方法。在上下文演示中显示的示例多样性和示例质量等因素可能会提高模型输出的质量(An et al.， 2023;Dong et al.， 2022)。在多模态基础模型的背景下，Flamingo和BLIP-2等模型(Alayrac et al.， 2022;Li等人，2023c)已被证明在只给定少量示例的情况下，在各种视觉理解任务中是有效的。在上下文中，当采取某些行动时，通过结合特定于环境的反馈，可以进一步改善环境中的代理的学习(Gong et al.， 2023a)。 </td>

随着GPT-3等大型语言模型的出现，上下文学习被证明是解决NLP任务的有效方法(Brown et al.， 2020;Min et al.， 2022)。通过在LLM提示的上下文中提供任务的示例，少量提示被认为是将NLP中各种任务的模型输出上下文化的有效方法。在上下文演示中显示的示例多样性和示例质量等因素可能会提高模型输出的质量(An et al.， 2023;Dong et al.， 2022)。在多模态基础模型的背景下，Flamingo和BLIP-2等模型(Alayrac et al.， 2022;Li等人，2023c)已被证明在只给定少量示例的情况下，在各种视觉理解任务中是有效的。在上下文中，当采取某些行动时，通过结合特定于环境的反馈，可以进一步改善环境中的代理的学习(Gong et al.， 2023a)。





#### **4.1.5 Optimization in the Agent System****Agent****系统中的优化**
<td style="vertical-align:top;width:237.7pt;"> The optimization of agent systems can be divided into spatial and temporal aspects. Spatial optimization considers how agents operate within a physical space to execute tasks. This includes inter-robot coordination, resource allocation, and keeping an organized space. </td><td style="vertical-align:top;width:188.4pt;"> 智能体系统的优化可分为空间优化和时间优化两个方面。空间优化考虑代理如何在物理空间内操作以执行任务。这包括机器人间的协调、资源分配和保持一个有组织的空间。  </td>

智能体系统的优化可分为空间优化和时间优化两个方面。空间优化考虑代理如何在物理空间内操作以执行任务。这包括机器人间的协调、资源分配和保持一个有组织的空间。
<td style="vertical-align:top;width:237.7pt;"> In order to effectively optimize agent AI systems, especially systems with large numbers of agents acting in parallel, previous works have focused on using large batch reinforcement learning (Shacklett et al., 2023). Since datasets of multi-agent interactions for specific tasks are rare, self-play reinforcement learning enables a team of agents to improve over time. However, this may also lead to very brittle agents that can only work under self-play and not with humans or other independent agents since they over-fit to the self-play training paradigm. To address this issue, we can instead discover a diverse set of conventions (Cui et al., 2023; Sarkar et al., 2023), and train an agent that is aware of a wide range of conventions. Foundation models can further help to establish conventions with humans or other independent agents, enabling smooth coordination with new agents. </td><td style="vertical-align:top;width:188.4pt;"> 为了有效地优化智能体AI系统，特别是具有大量智能体并行操作的系统，以前的工作主要集中在使用大批量强化学习(Shacklett等人，2023)。由于特定任务的多智能体交互数据集很少，自玩强化学习使智能体团队能够随着时间的推移而改进。然而，这也可能导致非常脆弱的代理只能在自我游戏下工作，而不能与人类或其他独立的代理一起工作，因为它们过度适应自我游戏训练范式。为了解决这个问题，我们可以发现一组不同的惯例(Cui et al.， 2023;Sarkar et al.， 2023)，并训练一个了解广泛惯例的代理。基础模型可以进一步帮助建立与人类或其他独立代理的约定，从而实现与新代理的平滑协调。  </td>

为了有效地优化智能体AI系统，特别是具有大量智能体并行操作的系统，以前的工作主要集中在使用大批量强化学习(Shacklett等人，2023)。由于特定任务的多智能体交互数据集很少，自玩强化学习使智能体团队能够随着时间的推移而改进。然而，这也可能导致非常脆弱的代理只能在自我游戏下工作，而不能与人类或其他独立的代理一起工作，因为它们过度适应自我游戏训练范式。为了解决这个问题，我们可以发现一组不同的惯例(Cui et al.， 2023;Sarkar et al.， 2023)，并训练一个了解广泛惯例的代理。基础模型可以进一步帮助建立与人类或其他独立代理的约定，从而实现与新代理的平滑协调。
<td style="vertical-align:top;width:237.7pt;"> Temporal optimization, on the other hand, focuses on how agents execute tasks over time. This encompasses task scheduling, sequencing, and timeline efficiency. For instance, optimizing the trajectory of a robot’s arm is an example of efficiently optimizing movement between consecutive tasks (Zhou et al., 2023c). At the level of task scheduling, methods like LLM-DP (Dagan et al., 2023) and ReAct (Yao et al., 2023a) have been proposed to solve efficient task planning by incorporating environmental factors interactively. </td><td style="vertical-align:top;width:188.4pt;"> 另一方面，时间优化关注的是代理如何随时间执行任务。这包括任务调度、排序和时间线效率。例如，优化机器人手臂的轨迹就是有效优化连续任务之间运动的一个例子(Zhou et al.， 2023c)。在任务调度层面，提出了LLM-DP (Dagan et al.， 2023)和ReAct (Yao et al.， 2023a)等方法，通过交互地纳入环境因素来解决高效的任务规划问题。 </td>

另一方面，时间优化关注的是代理如何随时间执行任务。这包括任务调度、排序和时间线效率。例如，优化机器人手臂的轨迹就是有效优化连续任务之间运动的一个例子(Zhou et al.， 2023c)。在任务调度层面，提出了LLM-DP (Dagan et al.， 2023)和ReAct (Yao et al.， 2023a)等方法，通过交互地纳入环境因素来解决高效的任务规划问题。





### **4.2 Agent Systems (zero-shot and few-shot level) ****Agent****系统 (零****样本****和少****样本****水平)**

#### **4.2.1 Agent Modules****Agent****模块**


<td style="vertical-align:top;width:237.7pt;"> Our foray into the agent paradigm involves the development of Agent AI "Modules" for interactive multi-modal agents using LLMs or VLMs. Our initial Agent Modules facilitate training or in-context learning and adopt a minimalist design for the purposes of demonstrating the agent’s ability to schedule and coordinate effectively. We also explored initial prompt-based memory techniques that facilitate better planning and inform future actions approaches within the domain. To illustrate, our “MindAgent" infrastructure comprises 5 main modules: 1) environment perception with task planning, 2) agent learning, 3) memory, 4) general agent action prediction and 5) cognition, as shown in Figure 5. </td><td style="vertical-align:top;width:188.4pt;"> 我们对代理范式的探索涉及到使用llm或vlm的交互式多模态代理的代理AI“模块”的开发。我们最初的智能体模块促进训练或上下文学习，并采用极简设计，以展示智能体有效安排和协调的能力。我们还探索了最初的基于提示的记忆技术，这些技术可以促进更好的规划，并为领域内的未来行动方法提供信息。为了说明这一点，我们的“MindAgent”基础设施包括5个主要模块:1)环境感知与任务规划，2)智能体学习，3)记忆，4)一般智能体动作预测和5)认知，如图5所示。 </td>

我们对代理范式的探索涉及到使用llm或vlm的交互式多模态代理的代理AI“模块”的开发。我们最初的智能体模块促进训练或上下文学习，并采用极简设计，以展示智能体有效安排和协调的能力。我们还探索了最初的基于提示的记忆技术，这些技术可以促进更好的规划，并为领域内的未来行动方法提供信息。为了说明这一点，我们的“MindAgent”基础设施包括5个主要模块:1)环境感知与任务规划，2)智能体学习，3)记忆，4)一般智能体动作预测和5)认知，如图5所示。





#### **4.2.2 Agent Infrastructure****Agent****基础设施**


<td style="vertical-align:top;width:258.9pt;"> Agent-based AI is a large and fast-growing community within the domains of entertainment, research, and industry. The development of large foundation models has significantly improved the performance of agent AI systems. However, creating agents in this vein is limited by the increasing effort necessary to create high-quality datasets and overall cost. At Microsoft, building high-quality agent infrastructure has significantly impacted multi-modal agent copilots by using advanced hardware, diverse data sources, and powerful software libraries. As Microsoft continues to push the boundaries of agent technology, AI agent platforms are poised to remain a dominant force in the world of multimodal intelligence for years to come. Nevertheless, agent AI interaction is currently still a complex process that requires a combination of multiple skills. The recent advancements in the space of large generative AI models have the potential to greatly reduce the current high cost and time required for interactive content, both for large studios, as well as empowering smaller independent content creators to design high quality experiences beyond what they are currently capable of. The current human-machine interaction systems inside multi-modal agents are primarily rule-based. They do have intelligent behaviors in response to human/user actions and possess web knowledge to some extent. However, these interactions are often limited by software development costs to enable specific behaviors in the system. In addition, current models are not designed to help human to achieve a goal in the case of users’ inability to achieve specific tasks. Therefore, there is a need for an agent AI system infrastructure to analyze users behaviors and provide proper support when needed. </td><td style="vertical-align:top;width:167.2pt;"> 基于代理的人工智能在娱乐、研究和工业领域是一个庞大且快速增长的社区。大型基础模型的发展显著提高了智能体AI系统的性能。然而，以这种方式创建代理受到创建高质量数据集所需的不断增加的工作量和总体成本的限制。在Microsoft，通过使用先进的硬件、多样化的数据源和强大的软件库，构建高质量的代理基础设施对多模式代理辅助系统产生了重大影响。随着微软继续推动智能体技术的发展，人工智能智能体平台在未来几年仍将是多模式智能世界的主导力量。然而，agent AI交互目前仍然是一个复杂的过程，需要多种技能的组合。大型生成人工智能模型领域的最新进展有可能大大降低当前互动内容所需的高成本和时间，无论是大型工作室，还是小型独立内容创作者，都可以设计出超出他们目前能力范围的高质量体验。当前多模态智能体内部的人机交互系统主要是基于规则的。它们确实具有响应人类/用户行为的智能行为，并且在一定程度上拥有网络知识。然而，为了在系统中实现特定的行为，这些交互常常受到软件开发成本的限制。此外，目前的模型并不是为了在用户无法完成特定任务的情况下帮助人类实现目标而设计的。因此，需要一个代理AI系统基础设施来分析用户行为，并在需要时提供适当的支持。 </td>

基于代理的人工智能在娱乐、研究和工业领域是一个庞大且快速增长的社区。大型基础模型的发展显著提高了智能体AI系统的性能。然而，以这种方式创建代理受到创建高质量数据集所需的不断增加的工作量和总体成本的限制。在Microsoft，通过使用先进的硬件、多样化的数据源和强大的软件库，构建高质量的代理基础设施对多模式代理辅助系统产生了重大影响。随着微软继续推动智能体技术的发展，人工智能智能体平台在未来几年仍将是多模式智能世界的主导力量。然而，agent AI交互目前仍然是一个复杂的过程，需要多种技能的组合。大型生成人工智能模型领域的最新进展有可能大大降低当前互动内容所需的高成本和时间，无论是大型工作室，还是小型独立内容创作者，都可以设计出超出他们目前能力范围的高质量体验。当前多模态智能体内部的人机交互系统主要是基于规则的。它们确实具有响应人类/用户行为的智能行为，并且在一定程度上拥有网络知识。然而，为了在系统中实现特定的行为，这些交互常常受到软件开发成本的限制。此外，目前的模型并不是为了在用户无法完成特定任务的情况下帮助人类实现目标而设计的。因此，需要一个代理AI系统基础设施来分析用户行为，并在需要时提供适当的支持。



### **4.3 Agentic Foundation Models (pretraining and finetune level)****主观基础模型 (预训练和微调水平)**




<td style="vertical-align:top;width:237.7pt;"> The use of pre-trained foundation models offers a significant advantage in their wide applicability across diverse use cases. The integration of these models enables the development of customized solutions for various applications, circumventing the need for extensive labeled datasets for each specific task. A notable example in the field of navigation is the LM-Nav system (Shah et al., 2023a), which incorporates GPT-3 and CLIP in a novel approach. It effectively uses textual landmarks generated by the language model, anchoring them in images acquired by robots for navigation. This method demonstrates a seamless fusion of textual and visual data, significantly enhancing the capabilities of robotic navigation, while maintaining wide applicability. </td><td style="vertical-align:top;width:188.4pt;"> 预先训练的基础模型的使用在它们跨不同用例的广泛适用性方面提供了一个显著的优势。这些模型的集成可以为各种应用程序开发定制的解决方案，从而避免了为每个特定任务提供大量标记数据集的需要。 导航领域的一个值得注意的例子是LM-Nav系统(Shah等人，2023a)，该系统以一种新颖的方式结合了GPT-3和CLIP。它有效地利用语言模型生成的文本地标，将它们锚定在机器人获取的图像中进行导航。该方法实现了文本和视觉数据的无缝融合，大大提高了机器人导航的能力，同时保持了广泛的适用性。   </td>

A notable example in the field of navigation is the LM-Nav system (Shah et al., 2023a), which incorporates GPT-3 and CLIP in a novel approach. It effectively uses textual landmarks generated by the language model, anchoring them in images acquired by robots for navigation. This method demonstrates a seamless fusion of textual and visual data, significantly enhancing the capabilities of robotic navigation, while maintaining wide applicability.

导航领域的一个值得注意的例子是LM-Nav系统(Shah等人，2023a)，该系统以一种新颖的方式结合了GPT-3和CLIP。它有效地利用语言模型生成的文本地标，将它们锚定在机器人获取的图像中进行导航。该方法实现了文本和视觉数据的无缝融合，大大提高了机器人导航的能力，同时保持了广泛的适用性。


<td style="vertical-align:top;width:237.7pt;"> In robot manipulation, several studies have proposed the use of off-the-shelf LLMs (e.g., ChatGPT) while using open vocabulary object detectors. The combination of LLM and advanced object detectors (e.g., Detic (Zhou et al., 2022)) facilitates the understanding of human instruction while grounding the textual information in scenery information (Parakh et al., 2023). Furthermore, the latest advancements showcase the potential of using prompt engineering with advanced multi-modal models such as GPT-4V(ision) (Wake et al., 2023b). This technique opens avenues for multi-modal task planning, underscoring the versatility and adaptability of pre-trained models in a variety of contexts. </td><td style="vertical-align:top;width:188.4pt;"> 在机器人操作中，一些研究已经提出在使用开放词汇对象检测器的同时使用现成的llm(例如，ChatGPT)。LLM与高级目标检测器(例如Detic (Zhou等人，2022))的结合有助于理解人类指令，同时将文本信息建立在场景信息中(Parakh等人，2023)。此外，最新的进展展示了将即时工程与先进的多模态模型(如GPT-4V(vision))结合使用的潜力(Wake等，2023b)。该技术为多模态任务规划开辟了道路，强调了预训练模型在各种上下文中的多功能性和适应性。 </td>

在机器人操作中，一些研究已经提出在使用开放词汇对象检测器的同时使用现成的llm(例如，ChatGPT)。LLM与高级目标检测器(例如Detic (Zhou等人，2022))的结合有助于理解人类指令，同时将文本信息建立在场景信息中(Parakh等人，2023)。此外，最新的进展展示了将即时工程与先进的多模态模型(如GPT-4V(vision))结合使用的潜力(Wake等，2023b)。该技术为多模态任务规划开辟了道路，强调了预训练模型在各种上下文中的多功能性和适应性。





## **5 Agent AI Categorization****人工智能代理****分类**

### **5.1 Generalist Agent Areas****通用****Agent****领域**


<td style="vertical-align:top;width:237.7pt;"> Computer-based action and generalist agents (GAs) are useful for many tasks. Recent progress in the field of large foundation models and interactive AI has enabled new functionalities for GAs. However, for a GA to become truly valuable to its users, it must be natural to interact with, and generalize to a broad range of contexts and modalities. We high-quality extended main Chapters on Agent foundation AI in Sec.6, especially in areas relevant to the themes in general of these topics: </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Multimodal Agent AI (MMA) is an upcoming forum2 for our research and industry communities to engage with each other and with the broader research and technology communities in Agent AI. Recent progress in the field of large foundation models and interactive AI has enabled new functionalities for generalist agents (GAs), such as predicting user actions and task planning in constrained settings (e.g., MindAgent (Gong et al., 2023a), fine-grained multimodal video understanding (Luo et al., 2022), Robotics (Ahn et al., 2022b; Brohan et al., 2023)), or providing a chat companion for users that incorporates knowledge feedback (e.g., website customer support for healthcare systems (Peng et al., 2023)). More details about the representative works and most recent representative works are shown below. We hope to discuss our vision for the future of MAA and inspire future researchers to work in this space. This article and our forum covers the following main topics, but is not limited exclusively to these: </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> &gt;&gt;Primary Subject Topics: Multimodal Agent AI, General Agent AI &gt;&gt;Secondary Subject Topics: Embodied Agents, Action Agents, Language-based Agents, Vision &amp; Language Agents, Knowledge and Inference Agents, Agents for Gaming, Robotics, Healthcare, etc. &gt;&gt;Extend Subject Topics: Visual Navigation, Simulation Environments, Rearrangement, Agentic Foundation Models, VR/AR/MR, Embodied Vision &amp; Language. Next, we present a specific lists of representative agent categories as follows: </td><td style="vertical-align:top;width:188.4pt;">  </td>

&gt;&gt;Secondary Subject Topics: Embodied Agents, Action Agents, Language-based Agents, Vision &amp; Language Agents, Knowledge and Inference Agents, Agents for Gaming, Robotics, Healthcare, etc.







### **5.2 Embodied Agents****具身****Agent**
<td style="vertical-align:top;width:251.55pt;"> Our biological minds live in bodies, and our bodies move through a changing world. The goal of embodied artificial intelligence is to create agents, such as robots, which learn to creatively solve challenging tasks requiring interaction with the environment. While this is a significant challenge, important advances in deep learning and the increasing availability of large datasets like ImageNet have enabled superhuman performance on a variety of AI tasks previously thought intractable. Computer vision, speech recognition and natural language processing have experienced transformative revolutions at passive input-output tasks like language translation and image classification, and reinforcement learning has similarly achieved world-class performance at interactive tasks like game playing. These advances have supercharged embodied AI, enabling a growing collection of users to make rapid progress towards intelligent agents can interactive with machine. </td><td style="vertical-align:top;width:174.55pt;"> 我们的生理思维存在于身体中，我们的身体在不断变化的世界中运动。具身智能的目标是创造代理，比如机器人，它们学会创造性地解决需要与环境交互的挑战性任务。虽然这是一个重大的挑战，但深度学习的重要进展和ImageNet等大型数据集的日益可用性，已经使人类在各种以前被认为难以处理的人工智能任务上取得了超人的表现。计算机视觉、语音识别和自然语言处理在语言翻译和图像分类等被动输入输出任务中经历了革命性的变革，强化学习在游戏等交互式任务中也同样取得了世界级的表现。这些进步推动了嵌入式人工智能的发展，使越来越多的用户能够在智能代理与机器交互方面取得快速进展。 </td>

我们的生理思维存在于身体中，我们的身体在不断变化的世界中运动。具身智能的目标是创造代理，比如机器人，它们学会创造性地解决需要与环境交互的挑战性任务。虽然这是一个重大的挑战，但深度学习的重要进展和ImageNet等大型数据集的日益可用性，已经使人类在各种以前被认为难以处理的人工智能任务上取得了超人的表现。计算机视觉、语音识别和自然语言处理在语言翻译和图像分类等被动输入输出任务中经历了革命性的变革，强化学习在游戏等交互式任务中也同样取得了世界级的表现。这些进步推动了嵌入式人工智能的发展，使越来越多的用户能够在智能代理与机器交互方面取得快速进展。



#### **5.2.1 Action Agents****行动****Agent**
<td style="vertical-align:top;width:237.7pt;"> Action agents refer to the agents that need to execute physical actions in the simulated physical environment or real world. In particular, they need to be actively engaging in activities with the environment. We broadly classify action agents into two different categories based on their application domains: gaming AI and robotics. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> In gaming AI, the agents will interact with the game environment and other independent entities. In these settings, natural language can enable smooth communication between agents and humans. Depending on the game, there may be a specific task to accomplish, providing a true reward signal. For instance, in the competitive Diplomacy game, training a language model using human conversation data along with an action policy with RL enables human-level play (Meta Fundamental AI Research (FAIR) Diplomacy Team et al., 2022). </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> There are also settings where we agents act as normal residents in a town (Park et al., 2023a), without trying to optimize a specific goal. Foundation models are useful in these settings because they can model interactions that appear more natural by mimicking human behavior. When augmented with external memory, they produce convincing agents that can have conversations, daily schedules, form relationships, and have a virtual life. </td><td style="vertical-align:top;width:188.4pt;">  </td>









#### **5.2.2 Interactive Agents****互动****Agent**
<td style="vertical-align:top;width:237.7pt;"> Interactive agents simply refer to agents that can interact with the world, a broader class of agents than action agents. Their forms of interaction do not necessarily require physical actions, but may involve communicating information to users or modifying the environment. For instance, an embodied interactive agent may answer a user’s questions about a topic through dialogue or help users parse through existing information similar to a chatbot. By extending an agent’s capabilities to include information sharing, the core designs and algorithms of Agent AI can be effectively adapted for a range of applications, such as diagnostic (Lee et al., 2023) and knowledge-retrieval (Peng et al., 2023) agents. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>









### **5.3 Simulation and Environments Agents****模拟和环境****Agent**


<td style="vertical-align:top;width:237.7pt;"> An effective approach for AI agents to learn how to act in an environment is to go through trial-and-error experiences via interactions with the environment. A representative method is RL, which requires extensive experience of failures to train an agent. Although there exist approaches that use physical agents (Kalashnikov et al., 2018), using physical agents is time-consuming and costly. Furthermore, training in the physical environment is often feasible when failure in actual environments can be dangerous (e.g., autonomous driving, underwater vehicles). Hence, using simulators to learn policies is a common approach. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Many simulation platforms have been proposed for research in embodied AI, ranging from navigation (Tsoi et al., 2022; Deitke et al., 2020; Kolve et al., 2017) to object manipulation (Wang et al., 2023d; Mees et al., 2022; Yang et al., 2023a; Ehsani et al., 2021). One example is Habitat (Savva et al., 2019; Szot et al., 2021), which provides a 3D indoor environment where human- and robotic-agents can perform various tasks such as navigation, instruction following, and question answering. Another representative simulation platform is VirtualHome (Puig et al., 2018), supporting human avatars for object manipulation in 3D indoor environments. In the field of gaming, Carroll et al. have introduced "Overcooked-AI," a benchmark environment designed to study cooperative tasks between humans and AI (Carroll et al., 2019). Along similar lines, several works aim to incorporate real human intervention beyond the focus of interaction between agents and the environment (Puig et al., 2023; Li et al., 2021a; Srivastava et al., 2022). These simulators contribute to the learning of policies in practical settings involving agent and robot interactions, and IL-based policy learning utilizing human demonstrative actions. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> In certain scenarios, the process of learning a policy may necessitate the integration of specialized features within simulators. For example, in the case of learning image-based policies, realistic rendering is often required to facilitate adaptability to real environments (Mittal et al., 2023; Zhong et al., 2023). Utilizing a realistic rendering engine is effective for generating images that reflect various conditions, such as lighting environments. Moreover, simulators employing physics engines are required to simulate physical interactions with objects (Liu and Negrut, 2021). The integration of physics engines in simulation has been shown to facilitate the acquisition of skills that are applicable in real-world scenarios (Saito et al., 2023). </td><td style="vertical-align:top;width:188.4pt;">  </td>







### **5.4 Generative Agents****生成****Agent**


<td style="vertical-align:top;width:237.7pt;"> The recent advancements in the space of large generative AI models have the potential to greatly reduce the current high cost and time required for interactive content, both for large gaming studios, as well as empower smaller independent studios to create high quality experiences beyond what they are currently capable of. Additionally, embedding large AI models within a sandbox environment will allow users to author their own experiences and express their creativity in ways that are currently out of reach. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> The goals of this agent go beyond simply adding interactive 3d content to scenes, but also include: Adding arbitrary behavior and rules of interactions to the objects, allowing the user to create their own VR rules with minimal prompting. &gt;&gt;Generating whole level geometry from a sketch on a piece of paper, by using the multimodal GPT4-v model, as well as other chains of models involving vision AI models &gt;&gt;Retexturing content in scenes using diffusion models &gt;&gt;Creating custom shaders and visual special effects from simple user prompts </td><td style="vertical-align:top;width:188.4pt;">  </td>

Adding arbitrary behavior and rules of interactions to the objects, allowing the user to create their own VR rules with minimal prompting.

&gt;&gt;Retexturing content in scenes using diffusion models


<td style="vertical-align:top;width:237.7pt;"> One potential application in the short term is the VR creation of a storyboarding/prototype tool allowing a single user to create a rough (but functional) sketch of an experience/game an order of magnitude faster than currently feasible. Such a prototype then could be expanded and made more polished using these tools as well. </td><td style="vertical-align:top;width:188.4pt;">  </td>









#### **5.4.1 AR/VR/mixed-reality Agents****基于****AR/VR/混合现实****Agent**
<td style="vertical-align:top;width:237.7pt;"> AR/VR/mixed-reality (jointly referred to as XR) settings currently require skilled artists and animators to create characters, environments, and objects to be used to model interactions in virtual worlds. This is a costly process that involves concept art, 3D modeling, texturing, rigging, and animation. XR agents can assist in this process by facilitating interactions between creators and building tools to help build the final virtual environment. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Our early experiments have already demonstrated that GPT models can be used in the few-shot regime inside of the Unity engine (without any additional fine-tuning) to call engine-specific methods, use API calls to download 3d models from the internet and place them into the scene, and assign state trees of behavior and animations to them (Huang et al., 2023a). This behavior likely emerges due to the presence of similar code in open source game repositories that use Unity. Therefore, GPT models are capable of building rich visual scenes in terms of loading in many objects into the scene from a simple user prompt. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> The aim of this category of agents is to build a platform and a set of tools that provide an efficient interface between large AI models (both GPT-family ones as well as diffusion image models) and a rendering engine. We explore two primary avenues here: &gt;&gt;Integration of large models into the various editor tools in the agent infrastructure, allowing for significant speedups in development. &gt;&gt; Controlling the rendering engine from within a user experience, by generating code that follows user instruction and then compiling it at runtime, allowing for users to potentially edit the VR/simulation they are interacting with in arbitrary ways, even by introducing new agent mechanics. </td><td style="vertical-align:top;width:188.4pt;">  </td>

&gt;&gt;Integration of large models into the various editor tools in the agent infrastructure, allowing for significant speedups in development.


<td style="vertical-align:top;width:237.7pt;"> Introducing an AI copilot focused on XR settings would be useful for XR creators, who can use the copilot to complete tedious tasks, like providing simple assets or writing code boilerplate, freeing creators to focus on their creative vision and quickly iterate on ideas. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Furthermore, agents can help users interactively modify the environment by adding new assets, changing the dynamics of the environment, or building new settings. This form of dynamic generation during runtime can also be specified by a creator, enabling the user’s experience to feel fresh and continue evolving over time. </td><td style="vertical-align:top;width:188.4pt;">  </td>









### **5.5 Knowledge and Logical Inference Agents****知识和逻辑推理****Agent**
<td style="vertical-align:top;width:237.7pt;"> The capacity to infer and apply knowledge is a defining feature of human cognition, particularly evident in complex tasks such as logical deduction, and understanding theory of mind 3 . Making inferences on knowledge ensures that the AI’s responses and actions are consistent with known facts and logical principles. This coherence is a crucial mechanism for maintaining trust and reliability in AI systems, especially in critical applications like medical diagnosis or legal analysis. Here, we introduce agents that incorporate the interplay between knowledge and inference that address specific facets of intelligence and reasoning. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>





#### **5.5.1 Knowledge Agent**




<td style="vertical-align:top;width:237.7pt;"> Generally, a logic agent is a component of a system designed to apply logical reasoning to process data or solve tasks specific to logical inference or logical reasoning. Logic agents within the context of large foundation models like GPT-4 refers to a specialized component or submodules designed to handle logical reasoning tasks. These tasks often involve understanding and manipulating abstract concepts, deducing conclusions from given premises, or solving problems that require a structured, logical approach. Broadly, foundation models like GPT-4 are trained on a vast corpus of text data and learn to perform a wide range of tasks, including those that require some form of logical reasoning. Thus, their capability for logical reasoning is integrated into the overall architecture, and they generally do not possess a distinct, isolated "Logic agent". While GPT-4 and similar models can perform tasks that involve logic, their approach is fundamentally different from how humans or traditional logic-based systems operate. They do not follow formal logical rules or have an explicit understanding of logic; rather, they generate responses based on patterns learned from the training data. As a result, their performance in logical tasks can be impressive, but it can also be inconsistent or limited by the nature of the training data and the inherent limitations of the model’s design. One example of embedding a separate logical submodule into the architecture is (Wang et al., 2023e), which modifies the token embedding process used by LLMs during pre-training by parsing text into logical segments and explicitly modeling logical hierarchies in the token embeddings. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>







#### **5.5.3 Agents for Emotional Reasoning****情感推理****Agent**


<td style="vertical-align:top;width:237.7pt;"> Emotional understanding and empathy are important skills for agents in many human-machine interactions. To illustrate, one important goal for creating engaging dialogue agents is to have the agents act with increased emotion and empathy while minimizing socially inappropriate or offensive outputs. To advance towards this goal for dialogue agents, we released the Neural Image Commenting with Empathy (NICE) dataset (Chen et al., 2021) consisting of almost two million images and the corresponding human-generated comments and a set of human emotion annotations. We also provided a novel pre-training model - Modeling Affect Gneration for Image Comments (MAGIC) (Chen et al., 2021) - which aims to generate comments for images, conditioned on linguistic representations that capture style and affect, and to help generate more empathetic, emotional, engaging and socially appropriate comments. Our experiments show that the approach is effective in training a more human-like and engaging image comment agent. Developing empathy-aware agents is a promising direction for interactive agents, and it is important to create agents with emotional understanding capabilities across a wide range of groups and populations, especially considering that many current language models exhibit bias in their emotional understanding and empathetic reasoning capabilities (Mao et al., 2022; Wake et al., 2023d). </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>









#### **5.5.4 Neuro-Symbolic Agents****神经符号****Agent**
<td style="vertical-align:top;width:237.7pt;"> Neuro-Symbolic agents operate on a hybrid system of neurons and symbols (d’Avila Garcez and Lamb, 2020). To solve problems stated in natural language is a challenging task because it requires explicitly capturing discrete symbolic structural information implicit in the input. However, most general neural sequence models do not explicitly capture such structural information, limiting their performance on these tasks. The work (Chen et al., 2020) propose a new encoder-decoder model based on a structured neural representation agent, The encoder of TP-N2F employs TPR ‘binding’ to encode natural-language symbolic structure in vector space and the decoder uses TPR ‘unbinding’ to generate, in symbolic space, a sequential program represented by relational tuples, each consisting of a relation (or operation) and a number of arguments. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Instruction following vision-language (VL) models like GPT-4 offer a flexible interface that supports a broad range of multimodal tasks in a zero-shot fashion. However, interfaces that operate on full images do not directly enable the user to “point to” and access specific regions within images. This capability is important not only to support reference-grounded VL benchmarks, but also, for practical applications that require precise within-image reasoning. In (Park et al., 2023b), we build Localized Visual Commonsense model which allows users to specify (multiple) regions-as-input. We train our model by sampling localized commonsense knowledge from a large language model (LLM): specifically, we prompt a LLM to collect common sense knowledge given a global literal image description and a local literal region description automatically generated by a set of VL models. This pipeline is scalable and fully automatic, as no aligned or human-authored image and text pairs are required. With a separately trained critic model that selects high quality examples, we find that training on the localized commonsense corpus expanded solely from images can successfully distill existing VL models to support a reference-as-input interface. Empirical results and human evaluations in zero-shot settings demonstrate that our distillation method results in more precise VL models of reasoning compared to a baseline of passing a generated referring expression. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>









### **5.6 LLMs and VLMs Agent****基于LLMs 和 VLMs Agent**
<td style="vertical-align:top;width:237.7pt;"> A number of works leverage LLMs as agents to perform task planning (Huang et al., 2022a; Wang et al., 2023b; Yao et al., 2023a; Li et al., 2023a), and leverage the LLMs’ large internet-scale domain knowledge and zero-shot planning abilities to perform agentic tasks like planning and reasoning. Recent robotics research also leverages LLMs to perform task planning (Ahn et al., 2022a; Huang et al., 2022b; Liang et al., 2022) by decomposing natural language instruction into a sequence of subtasks, either in the natural language form or in Python code , then using a low-level controller to execute these subtasks. Additionally, (Huang et al., 2022b), (Liang et al., 2022), and (Wang et al., 2023a) also incorporate environmental feedback to improve task performance. There have also been a number of works that demonstrate the ability of general-purpose visually-aligned large language models trained on large-scale text, image, and video data to serve as a foundation for creating multi-modal agents that are embodied and can act in various environments (Baker et al., 2022; Driess et al., 2023; Brohan et al., 2023). </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>







## **6 Agent AI Application Tasks ****Agent****AI应用任务**

### **6.1 Agents for Gaming****游戏****Agent**


<td style="vertical-align:top;width:237.7pt;"> Games provide a unique sandbox to test the agentic behavior of LLMs and VLMs, pushing the boundaries of their collaborative and decision-making abilities. We describe three areas in particular that highlight agent’s abilities to interact with human players and other agents, as well as their ability to take meaningful actions within an environment. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>







#### **6.1.1 NPC Behavior****基于NPC 行为**


<td style="vertical-align:top;width:237.7pt;"> In modern gaming systems, the behavior of Non-Player Characters (NPCs) is predominantly dictated by predefined scripts crafted by developers. These scripts encompass a range of reactions and interactions based on various triggers or player actions within the gaming environment. However, this scripted nature often results in predictable or repetitive NPC behavior which fails to evolve in response to player’s actions or the dynamic environment of the game. This rigidity hampers the immersive experience intended in a dynamic gaming environment. Therefore, there is a burgeoning interest in leveraging LLMs to induce autonomy and adaptability in NPC behavior, making interactions more nuanced and engaging. AI-driven NPCs can learn from player behavior, adapt to varying strategies, and provide a more challenging and less predictable gameplay experience. Large Language Models (LLMs) can significantly contribute to evolving NPC behavior in games. By processing vast amounts of text, LLMs can learn patterns and generate responses that are more varied and human-like. They can be utilized to create dynamic dialogue systems, making interactions with NPCs more engaging and less predictable. Furthermore, LLMs can be trained on player feedback and in-game data to continually refine NPC behaviors, making them more attuned to player expectations and game dynamics. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>



#### Figure 8: The embodied agent for user interactive gaming action prediction and interactive editing with Minecraft Dungeons gaming sense simulation and generation via GPT-4V.

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/direct/c3e4b957a5474c408d49e8c9314d1040.png" width="1200">





#### **6.1.2 Human-NPC Interaction****人-NPC 互动**
<td style="vertical-align:top;width:237.7pt;"> The interaction between human players and NPCs is a crucial aspect of the gaming experience. The conventional interaction paradigm is primarily one-dimensional, with NPCs reacting in a preset manner to player inputs. This limitation stifles the potential for a more organic and enriching interaction, akin to human-human interaction within the virtual realm. The advent of LLM and VLM technologies holds the promise of transforming this paradigm. By employing these technologies, gaming systems can analyze and learn from human behavior to provide more human-like interactions. This not only enhances the realism and engagement of the game but also provides a platform for exploring and understanding human-machine interaction in a controlled yet complex setting. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>





#### **6.1.3 Agent-based Analysis of Gaming****游戏的基于****Agent****的分析**




<td style="vertical-align:top;width:237.7pt;"> Gaming is an integral part of daily life, estimated to engage half of the world’s population4 . Additionally, it exhibits a positive impact on mental health5 . However, contemporary game systems exhibit a deficiency in interactions with human players since their behaviors are primarily hand-crafted by game developers. These pre-programmed behaviors frequently fail to adapt to players’ needs. Consequently, there exists a need for new AI systems in games that can analyze player behaviors and furnish appropriate support when necessary. Intelligent interactive systems bear the potential to revolutionize how gamers interact with gaming systems in general. NPCs’ interactions with gamers are no longer confined by the restricted rule sets designed by game developers. They have the potential to adapt seamlessly to gamers’ experiences, providing timely feedback to enrich the gaming experience and elevate the synergy of human-machine interaction. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> LLMs can serve as a robust tool for analyzing in-game text data, including chat logs, player feedback, and narrative content. They can help in identifying patterns of player behavior, preferences, and interactions which can be invaluable for game developers to improve game mechanics and narratives. Additionally, VLMs can parse through large quantities of image and video data from gaming sessions to help analyze user intent and actions within the game world. Moreover, LLMs and VLMs can facilitate the development of intelligent agents within games that can communicate with players and other agents in a sophisticated and human-like manner, enhancing the overall gaming experience. Beyond LLMs and VLMs, user input data, provides a promising avenue for creating game-playing agents that model perception, game playing, and game understanding by imitating human players. By incorporating a combination of player interactions and feedback, pixel inputs, and natural language planning and understanding, agent models can assist in the continuous improvement of game dynamics, driving a more player-centric evolution of the gaming environment. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>



#### Figure 9: GPT-4V can effectively predict the high-level next actions when given the “action history" and a “gaming target" in the prompt. Furthermore, GPT-4V accurately recognized that the player is holding wooden logs in their hand and can incorporate this perceived information into its plan for future actions. Although GPT-4V appears to be capable of predicting some low-level actions (such as pressing ‘E‘ to open the inventory), the model’s outputs are not inherently suitable for raw low-level action prediction (including mouse movements) and likely requires supplemental modules for low-level action control.

<img alt="" height="571" src="https://img-blog.csdnimg.cn/direct/c49195098e9b4b54bd45b73f8c20d447.png" width="443">





#### **6.1.4 Scene Synthesis for Gaming****游戏场景合成**


<td style="vertical-align:top;width:237.7pt;"> Scene synthesis is a vital component in the creation and enhancement of immersive gaming environments. It entails the automatic or semi-automatic generation of threedimensional (3D) scenes and environments within a game. This process includes the generation of terrain, placement of objects, creation of realistic lighting, and sometimes even dynamic weather systems. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Modern games often feature vast, open-world environments. Manually designing these landscapes can be incredibly time-consuming and resource-intensive. Automated terrain generation, often leveraging procedural or AI-driven techniques, can produce complex, realistic landscapes with less manual effort. LLMs and VLMs can utilize the internet scale knowledge to formulate rules to design non-repeating landscapes that are visually impressive and unique. Additionally, LLMs and VLMs can be used to ensure the semantic consistency and variability of generated assets. Placing objects such as buildings, vegetation, and other elements within a scene in a realistic and aesthetically pleasing manner is crucial for immersion. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> VLMs and LLMs can assist in object placement by adhering to predefined or learned rules and aesthetics, thus speeding up the level design process. VLMs and LLMs can be further trained to understand the principles of design and aesthetics, aiding in the procedural generation of content. They can help formulate rules or guidelines that procedural algorithms can follow to generate objects, and scenes that are both visually appealing and contextually appropriate. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Realistic lighting and atmospheric effects are fundamental for creating a believable and engaging gaming environment. Advanced algorithms can simulate natural lighting conditions and dynamic weather effects, enhancing the realism and mood of the scene. LLMs can help develop systems to acheive more realistic lighting and atmospheric effects in several innovative ways. VLMs can analyze vast datasets from real-world lighting and atmospheric conditions to help develop more realistic algorithms for simulating these effects in games. By understanding the patterns and intricacies of natural lighting and weather, these models can contribute to the development of algorithms that mimic reality closely. LLMs and VLMs could also be used to develop systems that adjust lighting and atmospheric effects in real-time based on player actions, game states, or external inputs. They can process natural language commands from players to modify the game environment, providing a more interactive and immersive experience. </td><td style="vertical-align:top;width:188.4pt;">  </td>



#### Figure 10: Masked video prediction on unseen Minecraft videos. From left to right: the original frame, the masked frame, the reconstructed frame, and the reconstructed frame with patches.

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/direct/e1445815247a4cc8aa1cd14414e0ad96.png" width="1200">





#### **6.1.5 Experiments and Result****实验和结果**
<td style="vertical-align:top;width:237.7pt;"> Zero-shot/Few-shot Learning with LLM or LVM. As we showed in the Fig. 8 and Fig. 9, we used GPT-4V for high-level description and action prediction. Fig. 8 showed some qualitative examples of action description generation and editing with GPT-4V. Agent-enhanced text opens up a novel method of generating 3D scenes with game action priors to help improve the naturalness of the scene. Consequently, GPT-4V generates relevant high-level descriptions that are appropriate for the gaming videos. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Small Agent Pretraining Model. To showcase our agent vision-language architecture, we first study its application in a widely used domain for gaming agents by pretraining on Minecraft data. As shown in Fig. 7, given an input action agent, key frame of video, and corresponding text, a standard encoder-decoder can be employed to convert the agent action and image into action text token and image patch token and then use the agent-vision-language decoder to convert it into a action prediction sentence. The overall architecture is depicted in Fig. 7. We evaluate our approach with several Minecraft demonstrations. The Minecraft video data consists of 5min clips, and we use for pretraining contains 78K videos, and we used 5K videos (6% of pretraining data) for the first round pretraining. We train a 250M parameter model on 16 NVIDIA v100 GPUs for one day and visualize our model outputs in Fig. 10 and Fig. 11. Fig. 10 shows that our relatively small agent architecture can produce reasonable outputs for Minecraft scenes unseen during training. Fig. 11 showed the model’s predictions compared to the ground truth human player actions indicating potential low-level understanding for our small agent model. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Multi-Agent Infrastructure. As showed in the agent paradigm in Fig. 5, we designed a novel infrastructure for a new gaming scenario called “CuisineWorld" (Gong et al., 2023a). We detail our approach in Fig. 12. Our infrastructure allows for multi-agent collaboration by leveraging GPT-4 as a central planner and works across multiple gaming domains. We investigated our system’s multi-agent planning capabilities, and we deployed the infrastructure into real-world video games to demonstrate its multi-agent and human-AI collaboration effectiveness. Additionally, we presented “Cuisineworld", a text-based multi-agent collaboration benchmark that provides a new auto-metric Collaboration Score (CoS) to quantify collaboration efficiency. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Please refer to the Appendix for more examples and details for gaming description, high-level action prediction, and GPT-4V prompting. We show examples for Bleeding Edge in Fig. 32 and Appendix B, Microsoft Flight Simulator in Fig. 33 and Appendix C, ASSASSIN’s CREED ODYSSEY in Fig. 34 and Appendix D, GEARS of WAR 4 in Fig. 35 and Appendix E, and Starfield in Fig. 36 and Appendix F. We also provide a detailed screenshot of the prompting process for GPT4V used to generate Minecraft examples with Fig. 31 in Appendix A. </td><td style="vertical-align:top;width:188.4pt;">  </td>



#### Figure 11: The low-level next step action prediction with the small agent pretraining model in gaming Minecraft scene.

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/direct/926761f337234ecea8529c26a214af5e.png" width="1200">



#### Figure 12: The MindAgent of in-context learning gaming Infrastructure. Planning Skill and Tool Use: The game environment requires diverse planning skills and tool use to complete tasks. It generates relevant game information and converts the game data into a structured text format that the LLMs can process. LLM: The main workhorse of our infrastructure makes decisions, thus serving as a dispatcher for the multi-agent system. Memory History: A storage utility for relevant information. Action Module: Extracts actions from text inputs and convertd them into domain-specific language and validates DSLs so that they cause no errors during execution.

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/direct/ed09b0ba4b074ba69953692ebdcb0f40.png" width="1200">



#### Figure 13: Overview of the robot teaching system that integrates a ChatGPT-empowered task planner. The process involves two steps: Task planning, where the user employs the task planner to create an action sequence and adjusts the result through feedback as necessary, and Demonstration, where the user visually demonstrates the action sequence to provide information needed for robot operation. The vision system collects visual parameters that will be used for robot execution.

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/direct/5a86c059663740958718e23c6d90f9a8.png" width="1200">



#### Figure 14: Example of adjusting an output sequence through auto-generated feedback. We use an open-sourced simulator, VirtualHome for the experiment. Given an instruction “Take the pie on the table and warm it using the stove.,” the task planner plans a sequence of functions that are provided in VirtualHome. If an error in execution is detected, the task planner correct its output based on the auto-generated error message.

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/direct/7fcf7232b89e4bbda4aa3daea358753d.png" width="1200">



### **6.2 Robotics****机器人学**
<td style="vertical-align:top;width:237.7pt;"> Robots are representative agents that necessitate effective interaction with their environment. In this section, we will introduce key elements essential for efficient robotic operation, review research topics where the latest LLM/VLM technologies have been applied, and share findings from our most recent studies. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Visual Motor Control. Visual Motor Control refers to the integration of visual perception and motor action to execute tasks effectively in a robotic system. This integration is paramount as it enables robots to interpret the visual data from their environment and accordingly adjust their motor actions to interact with the environment accurately. For instance, in an assembly line, a robot equipped with visual motor control can perceive the position and orientation of objects and accurately align its manipulator to interact with these objects. This capability is essential for ensuring the precision and effectiveness of robotic operations across a myriad of applications, ranging from industrial automation to assisting the elderly in their daily chores. Moreover, visual motor control facilitates robots in adapting to dynamic environments where the state of the environment may change rapidly, requiring real-time adjustments to motor actions based on visual feedback. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Additionally, within the context of safe operation, visual information is crucial for detecting execution errors and confirming the pre- and post-conditions of each robot action. In uncontrolled environments, such as unknown domestic settings, robots are more likely to face unexpected outcomes due to unpredictable factors like changing furniture shapes, varied lighting, and slippage. Executing a pre-planned action plan solely in a feedforward manner can pose significant risks in these settings. Therefore, utilizing visual feedback to continually verify outcomes at each step is key to ensuring robust and reliable operation of robotic systems. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Language Conditioned Manipulation. Language Conditioned Manipulation entails the ability of a robotic system to interpret and execute tasks based on language instructions. This aspect is particularly crucial for creating intuitive and user-friendly interfaces for human-robot interaction. Through natural language commands, users can specify goals and tasks to robots in a manner similar to human-human communication, thereby lowering the barrier to operating robotic systems. In a practical scenario, for instance, a user could instruct a service robot to “pick up the red apple from the table,” and the robot would parse this instruction, identify the referred object and execute the task of picking it up (Wake et al., 2023c). The core challenge lies in developing robust natural language processing and understanding algorithms that can accurately interpret a wide array of instructions, ranging from direct commands to more abstract directives, and enable the robot to convert these instructions into actionable tasks. Furthermore, ensuring that robots can generalize these instructions across diverse tasks and environments is critical for enhancing their versatility and utility in real-world applications. The use of language input to guide robot’s task planning has gained attention in the context of a robot framework called Task and Motion Planning (Garrett et al., 2021). </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Skill Optimization. Recent studies highlight the effectiveness of LLMs in robotic task planning. However the optimal execution of tasks, especially those involving physical interactions like grasping, requires a deeper understanding of the environment that goes beyond simply interpreting human instructions. For example, robot grasping necessitates precise contact points (Wake et al., 2023e) and arm posture (Sasabuchi et al., 2021) to efficiently execute subsequent actions.While these elements—precise contact points and arm posture—are intuitive for humans, articulating them through language is challenging. Despite advances in internet-scale VLMs, capturing these nuanced indirect cues from scenes and translating them effectively into robotic skills remains a significant challenge. In response, the robotics community is increasingly focusing on collecting enhanced datasets(e.g., (Wang et al., 2023d; Padalkar et al., 2023)) or developing methodologies for direct skill acquisition from human demonstrations (Wake et al., 2021a). Frameworks including Learning-from-Demonstration and Imitation Learning are leading these developments, playing a crucial role in the optimization of physical skills. </td><td style="vertical-align:top;width:188.4pt;">  </td>









#### **6.2.1 LLM/VLM Agent for Robotics****用于机器人学的LLM/VLM****Agent**
<td style="vertical-align:top;width:237.7pt;"> Recent research has demonstrated the potential of LLM/VLMs for robotic agents that involve interactions with humans in an environment. Research topics that aim to leverage latest LLM/VLM technologies include: </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Multimodal Systems: Recent research has been actively focusing on developing end-to-end systems that incorporate the latest LLM and VLM technologies as encoders for input information. Particularly, there is a significant trend towards modifying these foundation models to process multimodal information. (Jiang et al., 2022; Brohan et al., 2023, 2022; Li et al., 2023d; Ahn et al., 2022b; Shah et al., 2023b; Li et al., 2023e). This adaptation aims to guide robotic actions based on both linguistic instructions and visual cues, thus achieving an effective embodiment. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Task Planning and Skill Training: In contrast to end-to-end systems, Task And Motion Planning (TAMP) based systems first compute a high-level task plan and then achieve them with low-level robot control, known as skills. The advanced language processing abilities of LLMs have demonstrated the capability to interpret instructions and decompose them into robot action steps, greatly advancing task planning technologies (Ni et al., 2023; Li et al., 2023b; Parakh et al., 2023; Wake et al., 2023c). For skill training, several studies have explored the use of LLMs/VLMs for designing reward functions (Yu et al., 2023a; Katara et al., 2023; Ma et al., 2023), generating data to facilitate policy learning (Kumar et al., 2023; Du et al., 2023), or serving as part of a reward function (Sontakke et al., 2023). Together with training frameworks such as RL and IL, these efforts will contribute to the development of efficient robot controllers. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> On-site Optimization: Executing long task steps in robotics can be difficult due to unexpected and unpredictable environmental conditions. Therefore, a significant challenge in the field of robotics involves dynamically adapting and refining robotic skills by integrating task plans with real-time environmental data. For instance, (Ahn et al., 2022b) proposed an approach that calculates the feasibility of actions (i.e., affordance) from visual information and compares it with planned tasks. Additionally, there are approaches that focus on enabling LLMs to output the pre-conditions and post-conditions (e.g., states of objects and their interrelationships) of task steps to optimize their execution (Zhou et al., 2023c) and detect pre-condition errors for necessary revisions to the task plan (Raman et al., 2023). These strategies seek to achieve environment-grounded robot execution by integrating environmental information and adjusting the robot’s actions at the task plan or controller level. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Conversation Agents: In creating conversational robots, LLMs can contribute to natural, context-sensitive interactions with humans (Ye et al., 2023a; Wake et al., 2023f). These models process and generate responses that mimic human conversation, allowing robots to participate in meaningful dialogues. Additionally, LLMs play a significant role in the estimation of conceptual (Hensel et al., 2023; Teshima et al., 2022) and emotional attributes (Zhao et al., 2023; Yang et al., 2023b; Wake et al., 2023d) of utterances. Those attributes facilitate the understanding of human intent and meaningful gesture generation, thus contributing to the naturalness and efficacy of human-robot communication. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Navigation Agents: Robot navigation has a long history of research, focusing on core aspects such as map-based path planning and Simultaneous Localization and Mapping (SLAM) for creating environmental maps. These functionalities have become standard in widely used robot middleware like the Robot Operating System (ROS) (Guimarães et al., 2016). </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> While classic navigation techniques remain prevalent in many robotics applications, they typically rely on static or pre-created maps. Recently, there has been an increased interest in advanced technologies that enable robots to navigate in more challenging environments, leveraging breakthroughs in fields like computer vision and natural language processing. One representative task is object navigation (Chaplot et al., 2020a; Batra et al., 2020; Gervet et al., 2023; Ramakrishnan et al., 2022; Zhang et al., 2021), where robots use object names for navigation instead of map coordinates, requiring the visual grounding of object names in the environment. Furthermore, recent attention has been given to technologies that navigate robots in entirely unfamiliar new environments on a zero-shot basis, on top of foundation models, so-called zero-shot object navigation (Gadre et al., 2023; Dorbala et al., 2023; Cai et al., 2023). Additionally, Vision-Language Navigation (VLN) (Anderson et al., 2018a) is a representative task, where the task involves navigating an agent by natural language instructions in previously unseen, real-world environments (Shah et al., 2023a; Zhou et al., 2023a; Dorbala et al., 2022; Liang et al., 2023; Huang et al., 2023b). VLN interprets sentences rather than object names, such as “go to the bathroom on your left.,” thus it requires a higher functionality to parse input text (Wang et al., 2019). </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> The advent of foundation models contributes to the development of such adaptive, on-the-fly navigation technologies by enhancing the understanding of human language instructions and the visual interpretation of environmental information. More detailed explanations of representative VLN research are provided in 6.2.2. </td><td style="vertical-align:top;width:188.4pt;">  </td>







#### **6.2.2 Experiments and Results****实验和结果**


<td style="vertical-align:top;width:238.8pt;"> An accumulating body of evidence suggests that recent VLMs and LLMs have promising capabilities for symbolic task planning (e.g., what-to-do). However, each task requires low-level control policy (e.g., how-to-do) to achieve successful interaction between the environment. While reinforcement learning and imitation learning are promising approach to learn policies in a data-driven manner, another promising approach is to obtain the strategy directly from humans through on-site demonstration, an approach called Learning-from-Observation (Wake et al., 2021a; Ikeuchi et al., 0). In this section, we introduce a study where we employ ChatGPT for task planning and enrich the plan by parameterizing it with affordance information to facilitate effective and precise execution (Fig. 13). </td><td style="vertical-align:top;width:187.3pt;">  </td>


<td style="vertical-align:top;width:238.8pt;"> The pipeline was composed of two modules: task planning and parameterization. In task planning, the system is fed with language instructions and the description of the working environment. These instructions, along with a predefined set of robot actions and output specifications, are compiled into a comprehensive prompt provided to ChatGPT, which then generates a sequence of decomposed tasks with their textual descriptions (Fig. 13; left pane). Notably, we employ a few-shot approach, meaning ChatGPT is not trained on this task, offering an advantage in applicability as it eliminates the need for hardware-dependent data collection and model training. Additionally, the textual descriptions in the output enable the user to check and adjust the results as necessary, which is a crucial feature for a safe and robust operation. Fig. 14 shows the qualitative results conducted for an agentic simulation on top of VirtualHome (Puig et al., 2018). The results demonstrate a reasonable task plan and its flexibility in adjusting outputs, indicating the broad applicability of our approach. </td><td style="vertical-align:top;width:187.3pt;">  </td>


<td style="vertical-align:top;width:238.8pt;"> While the task planner guarantees coherency between the task sequences, successful operation in reality requires detailed parameters. For example, grasp type is crucial for carrying a container while spilling out the content, such a parameter is often ignored in a simulators (see Fig. 14 in grasping a pie). In our robot system, therefore, users are asked to demonstrate each action visually (Fig. 13; right pane). The tasks had predefined parameters necessary for execution, which our vision system extracts from the videos (Wake et al., 2021b). Notably, our robotic system is not designed for exact replication of human motions (i.e., teleoperation) but rather to handle varying real-world conditions, such as changes in object locations. Hence, the parameters extracted from human demonstrations encompass not precise motion paths but affordance information that dictates effective environmental movement (e.g., waypoints for collision avoidance (Wake et al., 2023a), grasp types (Wake et al., 2023e), and upper-limbs postures (Sasabuchi et al., 2021; Wake et al., 2021a)). The posture of the upper limbs is critical in robots with high degrees of freedom and is designed to assume predictable postures for humans coexisting with the operational robot. The task sequence endowed with affordances is transformed into a sequence of reusable robot skills acquired through reinforcement learning and executed by the robot (Takamatsu et al., 2022). </td><td style="vertical-align:top;width:187.3pt;">  </td>


<td style="vertical-align:top;width:238.8pt;"> LLM-empowered task planning can be extended to a more versatile robotic system by integrating it with VLMs. Here, we show an example where we use the GPT-4V(ision) to broaden the aforementioned task planner in a multimodal input context (Fig. 15), a human performs actions that are intended to be replicated by the robot. In this paper, only part of the prompt is shown. The whole prompt is available at microsoft.github.io/GPT4Vision-Robot-Manipulation-Prompts. </td><td style="vertical-align:top;width:187.3pt;">  </td>


<td style="vertical-align:top;width:238.8pt;"> This pipeline takes demonstration videos and text, then outputs a sequence of robot actions. A vision analyzer aims to understand the actions performed by humans in the video. We used GPT-4V and provided a prompt to generate text instructions in a style typical of human-to-human communication.Fig. 16 demonstrates how the usage of text input allows user to give feedback on GPT-4V’s recognition results for correction purposes. Such a feature, aiming at improving the accuracy of the recognition results, also enables more robust operation. </td><td style="vertical-align:top;width:187.3pt;">  </td>


<td style="vertical-align:top;width:238.8pt;"> Next, the scene analyzer compiles the expected work environment into the text information based on the instructions and the first frame of the video data (or an image of the environment). This environmental information includes a list of object names recognized by GPT-4V, the graspable properties of objects, and the spatial relationships between objects. Although these computational processes are a black box within GPT-4V, the information is output based on the knowledge of GPT-4V and the image/text input. Fig. 17 shows the example outputs of our scene analyzer. As shown in the figure, GPT-4V successfully selects the objects that are related to the manipulation. For example, a table is included in the output when the human is relocating a spam container on the table, while the table is ignored for the fridge opening task. These results suggest that the scene analyzer encodes the scene information with respect to the human’s actions. We prompted GPT-4V to explain the results of the object selection process and the reasons behind those choices. In practice, we found this approach resulted in reasonable outputs. Finally, based on the given text instructions and environmental information, the task planner outputs a sequence of tasks (Wake et al., 2023c). </td><td style="vertical-align:top;width:187.3pt;">  </td>


<td style="vertical-align:top;width:238.8pt;"> Embodied Agents for Robotics Navigation. Vision-language navigation (VLN) is the task of navigating an embodied agent to carry out natural language instructions inside real 3D environments. Navigation in 3D environments (Zhu et al., 2017a; Mirowski et al., 2016; Mousavian et al., 2018; Hemachandra et al., 2015) is an essential capability of a mobile intelligent system that functions in the physical world. In the past few years, a plethora of tasks and evaluation protocols (Savva et al., 2017; Kolve et al., 2017; Song et al., 2017; Xia et al., 2018; Anderson et al., 2018a) have been proposed as summarized in (Anderson et al., 2018b). VLN (Anderson et al., 2018a) focuses on language-grounded navigation in the real 3D environment. In order to solve the VLN task, (Anderson et al., 2018a) set up an attention-based sequence-to-sequence baseline model. Then (Wang et al., 2018) introduced a hybrid approach that combines model-free and model-based reinforcement learning (RL) to improve the model’s generalizability. Lastly, (Fried et al., 2018) proposed a speaker-follower model that adopts data augmentation, a panoramic action space and modified beam search for VLN, establishing the current state-of-the-art performance on the Room-to-Room dataset. Extending prior work, we propose a Reinforced Cross-Modal Matching (RCM) for VLN in (Wang et al., 2019). The RCM model is built upon (Fried et al., 2018) but differs in many significant aspects: (1) RCM combines a novel multi-reward RL with imitation learning for VLN while Speaker-Follower models (Fried et al., 2018) only uses supervised learning as in (Anderson et al., 2018a). (2) The RCM reasoning navigator performs cross-modal grounding rather than the temporal attention mechanism on single-modality input. (3) The RCM matching critic is similar to the Speaker in terms of the architecture design, but the former is used to provide the cycle-reconstruction intrinsic reward for both RL and SIL training while the latter is used to augment training data for supervised learning. In (Wang et al., 2019), we study how to address three critical leader-board for this task: the cross-modal grounding, the ill-posed feedback, and the generalization problem. As shown in Fig. 18, we propose a novel Reinforced Cross-Modal Matching approach that enforces cross-modal grounding both locally and globally via reinforcement learning (RL). Particularly, a matching critic is used to provide an intrinsic reward to encourage global matching between instructions and trajectories, and a reasoning navigator is employed to perform cross-modal grounding in the local visual scene. Evaluation on a VLN benchmark dataset shows that our RCM model significantly outperforms previous methods by 10% on SPL and achieved a new state-of-the-art performance. To improve the generalizability of the learned policy, we further introduce a Self-Supervised Imitation Learning (SIL) method to explore unseen environments by imitating its own past, good decisions. We demonstrate that SIL can approximate a better and more efficient policy, which tremendously minimizes the success rate performance gap between seen and unseen environments (from 30.7% to 11.7%). Moreover, in (Wang et al., 2019) we introduce a self-supervised imitation learning method for exploration in order to explicitly address the generalization issue, which is a problem not well-studied in prior work. Concurrent to the work, (Thomason et al., 2018; Ke et al., 2019; Ma et al., 2019a,b) studies the VLN tasks from various aspects, and (Nguyen et al., 2018) introduces a variant of the VLN task to find objects by requesting language assistance when needed. Note that we are the first to propose to explore unseen environments for the VLN task. </td><td style="vertical-align:top;width:187.3pt;">  </td>





#### Figure 15: Overview of the multimodal task planner that leverages GPT-4V and GPT-4. The system processes video demonstrations and text instructions, generating task plans for robotic execution.

<img alt="" height="1103" src="https://img-blog.csdnimg.cn/direct/2a9b95d1db33411c9dfc9b9d457fdd61.png" width="1200">



#### Figure 16: Examples of the output of the video analyzer. The five frames are extracted at regular intervals and fed into GPT-4V. We describe the entire pipeline in Section 6.2.2.

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/direct/5d173ec6ddd5431d942eb3921b2e14e3.png" width="1200">

####  Figure 17: Examples of the outputs of the scene analyzer that leverages GPT-4V. We describe our entire pipeline in Section 6.2.2.

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/direct/c2aeba6ff37d4a34802b906cf974b1bb.png" width="1200">

####  Figure 18: Demonstration of embodied agent for the VLN task (Wang et al., 2019). The instruction, the local visual scene, and the global trajectories in a top-down view is shown. The agent does not have access to the top-down view. Path A is the demonstration path following the instruction. Path B and C are two different paths executed by the agent.

<img alt="" height="783" src="https://img-blog.csdnimg.cn/direct/c030ebaf85ff4627b78069d2c4b9a414.png" width="1200">



### **6.3 Healthcare****医疗保健**
<td style="vertical-align:top;width:237.7pt;"> In healthcare, LLMs and VLMs can act as diagnostic agents, patient care assistants, or even therapy aids, but they come with unique leader-board and responsibilities. With the tremendous potential for AI agents to improve patient care and save lives comes an equally dangerous possibility that their misuse or hasty deployment could endanger thousands or millions of people worldwide. We discuss some of the promising routes for AI agents within the context of healthcare and also discuss some of the key leader-board faced. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Diagnostic Agents. Using LLMs as medical chatbots for patient diagnosis has recently attracted great attention due to the high-demand for medical experts and the potential for LLMs to help triage and diagnose patients (Lee et al., 2023). Dialogue agents, especially those that can effectively communicate important medical information to a broad range of people from diverse patient populations, have the potential to provide equitable healthcare access to historically disadvantaged or marginalized groups. Furthermore, doctors and healthcare systems across the world are largely over-burdened and under-resourced, resulting in insufficient access to medical care for hundreds of millions of people worldwide (World Health Organization and World Bank, 2015). Diagnostic agents provide a particularly advantageous pathway to improve healthcare for millions since they have they can be built with the capability to understand a variety of languages, cultures, and health conditions. Initial results have shown that healthcare-knowledgeable LMMs can be trained by utilizing large-scale web data (Li et al., 2023f). Although an exciting direction, the promise of diagnostic agents does not come without risks. We highlight the risks of hallucination within medical contexts, as well as potential pathways for solutions in the following section. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Knowledge Retrieval Agents. Within the medical context, model hallucinations are particularly dangerous and may even result in serious patient harm or death, depending on the severity of the error. For instance, if a patient mistakenly receives a diagnosis suggesting they are free of a condition they actually have, it can lead to catastrophic outcomes. These include postponed or inappropriate treatments, or in some cases, a total lack of necessary medical intervention. The gravity of undiagnosed or misdiagnosed conditions can lead to escalated healthcare expenses, extended therapies causing further physical strain, and in extreme scenarios, severe harm or even death. Thus, approaches that can use agents to more reliably retrieve knowledge (Peng et al., 2023) or generate text in a retrieval-based manner (Guu et al., 2020) are promising directions. Pairing a diagnostic agent with a medical knowledge retrieval agent has the potential to significantly reduce hallucinations while simultaneously improving the quality and preciseness of the responses of the diagnostic dialogue agent. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Telemedicine and Remote Monitoring. Agent-based AI also has great potential within the world of Telemedicine and Remote Monitoring by improving the access to healthcare, improving communications between healthcare providers and patients, as well as improving the efficiency and reducing the costs of frequent doctor-patient interactions (Amjad et al., 2023). Primary care clinicians spend significant amounts of time sifting through patient messages, reports, and emails that are often irrelevant or unnecessary for them to view. There is significant potential to allow for support agents to help triage messages from doctors, patients, and other healthcare providers and to help highlight important messages for all parties. By enabling agentic AI systems to coordinate with patients, clinicians, and other AI agents, there is a massive potential to revolutionize the remote healthcare and digital health industry </td><td style="vertical-align:top;width:188.4pt;">  </td>









#### **6.3.1 Current Healthcare Capabilities**** 当前医疗保健能力**
<td style="vertical-align:top;width:237.7pt;"> Image understanding. We demonstrate the current capabilities and limitations of modern multimodal agents such as GPT-4V within the context of healthcare in Fig. 19. We can see that although GPT-4V possesses significant internal knowledge of the equipment and procedures involved in hospital care, it does not always respond to more prescriptive or diagnostic queries by the user. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Video understanding. We investigate the performance of VLM agents for medical video understanding in two contexts. First, we investigate the ability for VLM agents to identify important patient care activities in clinical spaces. Secondly, we explore the usage of of VLMs for more technical videos such as ultrasounds. Specifically, in Figure 20, we demonstrate some of the current capabilities and limitations of GPT-4V for hospital care and medical video analysis. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>







### **6.4 Multimodal Agents****多模态****Agent**


<td style="vertical-align:top;width:237.7pt;"> The integration of visual and linguistic understanding is crucial for developing sophisticated multimodal AI agents. This includes tasks such as image captioning, visual question answering, video language generation, and video understanding, amongst others. We aim to delve into these visual-language tasks, exploring the leader-board and opportunities they present in the context of AI agents. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>







#### **6.4.1 Image-Language Understanding and Generation****图像-语言理解与生成**


<td style="vertical-align:top;width:237.7pt;"> Image-language understanding is a task that involves the interpretation of visual content in a given image with language and the generation of associated linguistic descriptions. This task is critical to the development of AI agents that can interact with the world in a more human-like manner. Some of most popular ones are image captioning (Lin et al., 2014; Sharma et al., 2018; Young et al., 2014; Krishna et al., 2016), referring expression (Yu et al., 2016; Karpathy et al., 2014), and visual question answering (Antol et al., 2015; Ren et al., 2015; Singh et al., 2019). </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> More recently, knowledge-intensive Visual Question Answering tasks such as OKVQA (Marino et al., 2019), KBVQA (Wang et al., 2015), FVQA (Wang et al., 2017), and WebQA (Chang et al., 2021) have been introduced. Multimodal 36 agents should capable of identifying objects in an image, comprehending their spatial relationships, generating accurate descriptive sentences about the scene, and utilizing reasoning skills to handle knowledge-intensive visual reasoning. This requires not just object recognition capabilities, but also a deep understanding of spatial relationships, visual semantics, and the ability to map these visual elements to linguistic constructs with integration of the world knowledge. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>





#### Figure 19: Example prompts and responses when using GPT-4V within the domain of healthcare image understanding. From left to right: (1) an image of a nurse and doctor conducting a CT scan, (2) a synthetic image of an irregular EKG scan, and (3) an image from the ISIC (Codella et al., 2018) skin lesion dataset. We can see that GPT-4V possesses significant medical knowledge and is able to reason about medical images. However, due to safety training, it is unable to make diagnoses for some medical images.

<img alt="" height="796" src="https://img-blog.csdnimg.cn/direct/0ace13085ee0440d878ada4578855c46.png" width="1137">



#### **6.4.2 Video and Language Understanding and Generation****视频和语言理解与生成**
<td style="vertical-align:top;width:237.7pt;"> Video-language generation. Video captioning or video storytelling is the task of generating a sequence of coherent sentences for a stream of video frames. Inspired by the successful use of recurrent large foundation models employed in video and language tasks, variants of agent driven enhanced models have shown promising results on the task of video-lanaguage generation. The fundamental challenge is that the strong performance of neural encoder-decoder models does not generalize well for visual storytelling, because the task requires a full understanding of the content of each image as well as the relation among different frames. One important goal for the field is to create an agent-aware text-synthesis model that can efficiently encode the sequence of frames and generate a topically coherent multi-sentence paragraph. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Video Understanding. Video understanding extends the scope of image understanding to dynamic visual content. This involves interpretation and reasoning about the sequence of frames in a video, often in conjunction with accompanying audio or textual information. An agent should be able interact with various modalities from visual, text, and also audio modalities to demonstrate their advanced comprehension of video content. Tasks in this domain include video captioning, video question answering, and activity recognition, amongst others. The leader-board in video understanding are manifold. They include the temporal alignment of visual and linguistic content, the handling of long sequences of frames, and the interpretation of complex activities that unfold over time. Regarding audio, the agent could process spoken words, background noises, music, and tone of voice to comprehend the mood, setting, and subtleties of the video content. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Previous works have focused on employing existing video-language training data available online for establishing video foundational models (Li et al., 2020, 2021b; Fu et al., 2022; Bain et al., 2021; Zellers et al., 2021, 2022; Fu et al., 2023). Supporting such training pipelines and functionalities is, however, difficult due to the limited and often inconsistent nature of these datasets. Video foundational models are designed with masked and contrastive pretraining objectives and later tuned on their respective tasks. Despite showing remarkable results in multimodal benchmarks, these models encounter difficulties in video-only tasks such as action recognition due to their dependency on limited video-text data built from noisy audio transcriptions. This limitation also leads to the lack of robustness and fine-grained reasoning skills that large language models generally possess. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Other methods, similar to those used in image-language understanding, have drawn on the strong reasoning skills and broad knowledge of large language models to improve different facets of video interpretation. The task of video understanding is simplified by language only models like ChatGPT and GPT4 or image-language models like GPT4-V, which treat the audio, video, and language modalities as individual interpretable input data types and position the agents as strong open-source models. For example, (Huang et al., 2023c; Li et al., 2023g) transformed video understanding into a natural language processing (NLP) question-answering formulation by textualizing video content with open-source vision classification/detection/caption models. (Lin et al., 2023) integrated GPT4-V with specialized tools in vision, audio, and speech, to facilitate complex video understanding tasks, such as scripting character movements and actions in long-form videos. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Parallel research explores generating scaled datasets from large models, then applying visual instruction tuning (Liu et al., 2023c; Li et al., 2023c; Zhu et al., 2023) on the generated data. Considerable audio, speech, and visual expert perception models are subsequently used to verbalize videos. Speech is transcribed with automatic speech recognition tools, and video descriptions and related data are produced with various tagging, grounding, and captioning models (Li et al., 2023g; Maaz et al., 2023; Chen et al., 2023; Wang et al., 2023f). These techniques demonstrate how instruction tuning video-language models on generated datasets may lead to enhanced video-reasoning and communication abilities. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>





#### Figure 20: Example prompts and responses when using GPT-4V within the domain of healthcare video understanding. We input the example videos as 2x2 grids with overlaid text indicating the order of frames. In the first two examples, we prompt GPT-4V to examine the frames in the video to detect the clinical bedside activities performed on the volunteer patients. For the final example, we attempt to prompt GPT-4V to assess an echocardiogram video, however due to GPT-4V’s safety training, it does not provide a detailed response. For clarity, we bold text that describes the activity of interest, and abbreviate model responses that are unnecessary. We gray-out faces from the individuals to preserve their privacy.

<img alt="" height="812" src="https://img-blog.csdnimg.cn/direct/1b6b0b18c228402e83d99ddd482b878e.png" width="1200">

####  Figure 21: Interactive multimodal agents include four main pillars: Interaction, Speech, Vision, and Language. Co-pilot agents are made up of different services. 1) Interaction services help make a unified platform for automated actions, cognition, and decision-making. 2) Audio services integrate audio and speech processing into apps and services. 3) Vision services identify and analyze content within images, videos, and digital ink. 4) Language services extract meaning from structured and unstructured text.

<img alt="" height="741" src="https://img-blog.csdnimg.cn/direct/fa50f587c9ef4046a8ed05ac33edd10e.png" width="1200">



#### Figure 22: Example of Intensive Neural Knowledge (INK) (Park et al., 2022) task that uses knowledge to identify text relevant to the image from a set of text candidates. Our task involves leveraging visual and text knowledge retrieved from web and human-annotated knowledge.

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/direct/2086afedba234cc8bd17bc6151b3483f.png" width="1200">



#### Figure 23: The KAT model (Gui et al., 2022a) uses a contrastive-learning-based module to retrieve knowledge entries from an explicit knowledge base and uses GPT-3 to retrieve implicit knowledge with supporting evidence. The integration of knowledge is processed by the respective encoder transformer and jointly with reasoning module and the decoder transformer via end-to-end training for answer generation.

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/direct/ea0cd8900d9a465c8c44556d3a4dfffe.png" width="1200">



#### **6.4.3 Experiments and Results****实验和结果**
<td style="vertical-align:top;width:237.7pt;"> &gt;&gt;Knowledge-Intensive Models: As introduced in INK (Park et al., 2022), and KAT (Gui et al., 2022a), an intensive neural knowledge task that incorporates required knowledge annotated by humans to support knowledge-intensive retrieval task. &gt;&gt;Multimodal-Agents: There has been a growing interest in multimodal language models like Chameleon (Lu et al., 2023) and MM-React (Yang et al., 2023c). &gt;&gt;Visual Instruction Tuning: VCL(Gui et al., 2022b), Mini-GPT4 (Zhu et al., 2023), MPLUG-OWL (Ye et al., 2023b), LSKD (Park et al., 2023c) generate image-level instruction tuning dataset. </td><td style="vertical-align:top;width:188.4pt;">  </td>

&gt;&gt;Multimodal-Agents: There has been a growing interest in multimodal language models like Chameleon (Lu et al., 2023) and MM-React (Yang et al., 2023c).


<td style="vertical-align:top;width:237.7pt;"> Knowledge-Intensive Agent. As showed in Fig. 22 and Fig. 23, Knowledge-based visual question answering and vision-language retrieval tasks are challenging tasks in multi-modal machine learning that requires outside knowledge beyond image contents. Recent studies on large-scale transformers have primarily focused on maximizing the efficiency of the model’s parameters to store information. This line of research explores a different aspect: whether multimodal transformers can use explicit knowledge in their decision-making process. Pretraining methods based on transformers have shown remarkable success in implicitly learning knowledge representations across multiple modalities. However, traditional methods, mainly unimodal, have investigated knowledge retrieval and subsequent answer prediction, raising questions about the quality and relevance of the knowledge retrieved and the integration of reasoning processes using both implicit and explicit knowledge. To tackle these issues, we introduce the Knowledge Augmented Transformer (KAT), which outperforms others by 6% on the 2022 OK-VQA open-domain multimodal task. KAT combines implicit knowledge from GPT3 with explicit knowledge from websites using an encoder-decoder structure, and allows for concurrent reasoning with both knowledge types during answer generation. Furthermore, incorporating explicit knowledge enhances the interpretability of the model’s predictions. The code and pre-trained models are available at https://github.com/guilk/KAT. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Vision-language Transformer Agent. Next, we introduce the "Training Vision-Language Transformers from Captions" (VLC) model (Gui et al., 2022b), a transformer that has been pretrained exclusively with image-caption pairs. Despite using just a simple linear projection layer for image embeddings, VLC attains competitive results across various vision-language tasks, in contrast to other methods that depend on object detectors or supervised CNN/ViT networks. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Through extensive analysis, we explore the potential of VLC as a vision-language transformer agent. For instance, we show that VLC’s visual representations are highly effective for ImageNet-1K classification, and our visualizations confirm that VLC can accurately match image patches to corresponding text tokens. The scalability of performance with more training data highlights the promising potential for developing large-scale, weakly-supervised, open-domain vision-language models. </td><td style="vertical-align:top;width:188.4pt;">  </td>





 Figure 22: Example of Intensive Neural Knowledge (INK) (Park et al., 2022) task that uses knowledge to identify text relevant to the image from a set of text candidates. Our task involves leveraging visual and text knowledge retrieved from web and human-annotated knowledge.

Figure 23: The KAT model (Gui et al., 2022a) uses a contrastive-learning-based module to retrieve knowledge entries from an explicit knowledge base and uses GPT-3 to retrieve implicit knowledge with supporting evidence. The integration of knowledge is processed by the respective encoder transformer and jointly with reasoning module and the decoder transformer via end-to-end training for answer generation.

####  Figure 24: The overall architecture of the VLC model (Gui et al., 2022b). Our model consists of three modules: (1) Modality-specific projection. We use a simple linear projection to embed patched images and a word embedding layer to embed tokenized text; (2) Multi-modal encoder. We use a 12-layer ViT (Dosovitskiy et al., 2021) initialized from MAE (He et al., 2022) (ImageNet-1K without labels) as our backbone; (3) Task-specific decoder. We learn our multi-modal representations by masked image/language modeling and image-text matching which are only used during pre-training. We use a 2-layer MLP to fine-tune our multi-modal encoder for downstream tasks. Importantly, we find that the masked image modeling objective is important throughout second-stage pre-training, not only for initialization of the visual transformer.

<img alt="" height="848" src="https://img-blog.csdnimg.cn/direct/bfef5939eef34c178396b587b031bdf9.png" width="1200">

#### Figure 25: Example prompts and responses when using a video fine-tuned variant of InstructBLIP (method described in Section 6.5). Our model is able to produce long-form textual responses that describe scenes and is able to answer questions related to the temporality of events in the videos.

<img alt="" height="580" src="https://img-blog.csdnimg.cn/direct/2c1cb3a63bef4e7986ecb8f02e7be46c.png" width="1140">



#### Figure 26: The audio-multimodal agent described in Section 6.5. Hallucinated content are highlighted in red. We use GPT-4V to generate 1) the videochat summary with video frames; 2) the video summary with the frame captions; 3) the video summary with frame captioning and audio information.

<img alt="" height="766" src="https://img-blog.csdnimg.cn/direct/b89ae3f17ea244f3932d4c5f08b81a66.png" width="1200">



#### Figure 27: An interactive multimodal agent that incorporates visual, audio, and text modalities for video understanding. Our pipeline mines hard negative hallucinations to produce difficult queries for the VideoAnalytica challenge. More the related details of interactive audio-video-language agent dataset are described in Section 9.2.

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/direct/9dc7ea682c8d4e8f890abc7e48df416e.png" width="1200">

  



### **6.5 Video-language Experiments****视频语言实验**
<td style="vertical-align:top;width:237.7pt;"> To understand the practicality of converting pre-trained image-LLMs for video understanding, we temporally expand and fine-tune InstructBLIP (Dai et al., 2023) for video captioning. Specifically, we expand the visual encoder of InstructBLIP (EVA-CLIP-G (Sun et al., 2023b)) using the same divided space-time attention scheme as Frozen in Time (Bain et al., 2021) and keep the Q-former and LLM (Flan-T5-XL (Chung et al., 2022)) frozen during training. We freeze all spatial layers of the visual encoder, while keeping the temporal layers unfrozen during captioning training. This allows for our model to take image and videos as input (matching the image-level performance of InstructBLIP). We train on a 5 million video-caption subset of WebVid10M (Bain et al., 2021). We visualize two example outputs in Figure 25. However, existing agents fail to fully comprehend precise, fine-grained visual details in the video content. A similar limitation is seen by visual instruction tuning methods, where they lack the general, human-level perception abilities that are remain to be solved by multimodal models and agents. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> The instruction-tuned models show promise in accurately summarizing visible actions within videos and identifying actions like "person sitting on a bench" effectively in Fig. 25. However, they sometimes add incorrect details, such as "person smiling to the camera," revealing a shortfall in capturing conversation topics or the video’s ambiance, elements that are readily apparent to human observers. This shortfall underscores another key limitation: the omission of audio and speech modalities that would enrich the video understanding with context, aiding in more accurate interpretation and preventing such misrepresentations. Bridging this gap requires a holistic integration of available modalities, allowing multimodal agents to reach a level of comprehension akin to human perception and ensuring a fully multimodal approach to video interpretation. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Audio-Video-Language Agents with GPT-4V. We then evaluate the capabilities of GPT-4V as a multimodal agent that integrates vision, audio, and speech for a nuanced and precise understanding of videos, following the methodology outlined in (Lin et al., 2023). Results depicted in Fig. 26 compare the performance of various video agents on the task of video summarization. The video-instruction tuned model (Li et al., 2023g) provides accurate content but falls short on comprehensiveness and detail, missing specific actions like the methodical use of a broomstick to measure a tree’s height. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> To enhance the accuracy of video descriptions, we employ GPT-4V to caption frames, while audio and its transcriptions are sourced from the OpenAI Whisper model. We then prompt GPT-4V to create video summaries using only frame captions and then using both frame captions and audio transcriptions. Initially, we observe that frame captions alone can lead to fabricated events, such as a person biting down on a stick in the third segment. These inaccuracies persist in the video summary, with descriptions like "in a playful twist, he bites down on it while holding it horizontally." Without audio input, the agent cannot correct these captioning errors, resulting in descriptions that are semantically correct but visually misleading. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> However, when we provide the audio transcriptions to the agent, it manages to accurately depict the content, even capturing detailed physical actions like "holding the broomstick perpendicular to the body and rotating it downwards." This level of detail is significantly more informative and gives viewers a clearer understanding of the video’s purpose and key details. These findings highlight the importance of integrating audio, video, and language interactions to develop high-quality multimodal agents. GPT-4V emerges as a promising foundation for such advanced multimodal understanding and interaction. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Embodied Multi-modal Agents with GPT-4V. As shown in Fig. 27, We mainly used StackOverflow to get the initial Question, then we used the “Bing search" API to retrieve a related video and audio corresponding to the question. Next, we mainly use GPT-4V to get the relevant text information and high-level video description. On the other hand, we transfer the key frame audio to a low-level segment description of the key frames via ASR. Finally, we use GPT-4V to generate convincing "hallucinations" that serve as hard negative queries for video-question and answer tasks. We support interactions and question answering in the current frame of the video, as well as summarization for the overall high-level video description. During inference, we also combine external knowledge information via web search to improve answering capapbilities. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> The main prompt information for GPT-4V is described as below. The entire prompt is indented for clarity; it is over one page long. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> GPT-4V are an assistant to provide descriptive, informative, and full comprehensive details in the video for the visually impaired who can hear the video but cannot see. The job is to create high-quality, dense descriptions of the video by synthesizing the given annotations and output them as JSON. Specifically, GPT-4V will be given original query used to search the video, the video title, description, audio transcription, and potentially noisy descriptions for specific time in the video. Different segments of same video is annotated as "[time start - time end (in seconds)] ’text’ ". Utilize the transcriptions and descriptions all together to reason about the exact detail and visual demonstration that might be happening in the video. GPT-4V will to combine or segment the timestamps as necessary to provide the best segmentation of the video. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Expectations for GPT-4V Output: Action-Oriented Descriptions: Prioritize plausible actions, motions, and physical demonstrations that the audio implies, enriching your narrative with dynamic visual cues. Complete Video Coverage: Provide a continuous and consistent audio-descriptive experience that covers every moment of the video’s duration, ensuring no content is left undescribed. 3. Concise Segmentation: Construct your descriptions in focused, succinct segments of 1-2 sentences each to effectively communicate visual actions without overwhelming detail. 4. Contextual Audio-Visual Synthesis: Seamlessly blend the spoken audio content with inferred visual elements to form a narrative that reflects potential onscreen activities. 5. Imaginative and Plausible Speculation: Infuse your descriptions with creative yet believable visual details that correspond with the audio, enhancing scene comprehension. 6. Accurate Timecode Correspondence: Align your descriptive segments with corresponding timecodes, ensuring that speculative visual details synchronize with the audio narrative’s timeline. 7. Confident Narrative Delivery: Present the descriptions with assurance, as though the speculated visuals are occurring, to instill confidence in the listener. 8. Omit Implausible Details: Exclude descriptions of objects or events that do not reasonably fit within the context established by the audio and visual information provided. The final output should be structured in a JSON format containing a list of dictionaries, each detailing a segment of the video. The final output should be structured in a JSON format containing a list of dictionaries, each detailing a segment of the video. </td><td style="vertical-align:top;width:188.4pt;">  </td>

Action-Oriented Descriptions: Prioritize plausible actions, motions, and physical demonstrations that the audio implies, enriching your narrative with dynamic visual cues.

3. Concise Segmentation: Construct your descriptions in focused, succinct segments of 1-2 sentences each to effectively communicate visual actions without overwhelming detail.

5. Imaginative and Plausible Speculation: Infuse your descriptions with creative yet believable visual details that correspond with the audio, enhancing scene comprehension.

7. Confident Narrative Delivery: Present the descriptions with assurance, as though the speculated visuals are occurring, to instill confidence in the listener.


<td style="vertical-align:top;width:237.7pt;"> For MC Creation: our task is to create multiple-choice questions for video-to-text retrieval tasks that is trivially solved by looking at the title and reading through audio transcriptions. To do so, we will be given original query to get the video, description, audio transcription, and potentially noisy descriptions for specific time in the video. &gt;&gt;Format of audio transcription: -[start-end time in seconds] “transcription" &gt;&gt;Format of noisy description: - [time in seconds] “description" </td><td style="vertical-align:top;width:188.4pt;">  </td>

&gt;&gt;Format of audio transcription: -[start-end time in seconds] “transcription"


<td style="vertical-align:top;width:237.7pt;"> We kindly ask GPT-4V to generate four queries, where the primary query is aligned with the video content, and the other three negatives are subtly different from our primary one. Selecting the primary one should not simply involve listening to audio transcriptions e.g. the text original query is contained in audio transcriptions. The negatives should be closely related but not fully aligned with the video content, requiring visual understanding of the video to differentiate. For example, modify the semantics in nuanced way so that one needs to watch the video than just listening to select the original query. Compile four queries in caption-like statement, with the first one being the rephrased original. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Think step by step how you can come up with negative statements using the information from the video. And justify the negative queries are incorrect but still compelling choices that demand nuanced understanding of the video. And how humans would not accidentally choose the negatives over the original query. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Finally, we present the work in the following format of analyses and 4 queries. No need to generate how you translated the original query. </td><td style="vertical-align:top;width:188.4pt;">  </td>







### **6.6 Agent for NLP****基于 NLP ****Agent**

#### **6.6.1 LLM agent****基于LLM Agent**


<td style="vertical-align:top;width:237.7pt;"> Recognizing task directives and taking action has been a fundamental challenge in interactive AI and natural language processing for decades. With the recent advances in deep learning, there is a growing interest in studying these areas jointly to improve human-agent collaboration. We identify three specific directions, among others, to improve language-grounded agents: </td><td style="vertical-align:top;width:188.4pt;"> 几十年来，识别任务指令并采取行动一直是交互式人工智能和自然语言处理的基本挑战。随着深度学习的最新进展，人们对共同研究这些领域以改善人类与智能体的协作越来越感兴趣。我们确定了三个具体的方向，其中包括改进基于语言的代理:  </td>

几十年来，识别任务指令并采取行动一直是交互式人工智能和自然语言处理的基本挑战。随着深度学习的最新进展，人们对共同研究这些领域以改善人类与智能体的协作越来越感兴趣。我们确定了三个具体的方向，其中包括改进基于语言的代理:



##### **<strong><strong>工具使用：整合外部知识**</strong>**<strong>增强**</strong>**<strong>理解**</strong>**<strong>，**</strong>**<strong>利用外部**</strong>**<strong>整合外部知识库、网络搜索等工具提升AI代理的理解和响应准确性**</strong></strong>
<td style="vertical-align:top;width:237.7pt;"> Tool use and querying from knowledge bases. This direction emphasizes the importance of integrating external knowledge bases, web search, or other helpful tools into the reasoning processes of AI agents. By leveraging structured and unstructured data from various sources, agents can enhance their understanding and provide more accurate and context-aware responses. Furthermore, it fosters the agent’s ability to proactively seek out information when faced with unfamiliar scenarios or queries, ensuring more comprehensive and informed responses. Examples include Toolformer (Schick et al., 2023) and Retrieve What You Need (Wang et al., 2023g). </td><td style="vertical-align:top;width:188.4pt;"> 工具使用和从知识库查询。这个方向强调将外部知识库、网络搜索或其他有用的工具集成到AI代理的推理过程中的重要性。通过利用来自各种来源的结构化和非结构化数据，代理可以增强他们的理解并提供更准确和上下文感知的响应。此外，它培养了代理在面对不熟悉的场景或查询时主动寻找信息的能力，确保更全面和知情的响应。例如Toolformer (Schick et al.， 2023)和Retrieve What You Need (Wang et al.， 2023)。  </td>

工具使用和从知识库查询。这个方向强调将外部知识库、网络搜索或其他有用的工具集成到AI代理的推理过程中的重要性。通过利用来自各种来源的结构化和非结构化数据，代理可以增强他们的理解并提供更准确和上下文感知的响应。此外，它培养了代理在面对不熟悉的场景或查询时主动寻找信息的能力，确保更全面和知情的响应。例如Toolformer (Schick et al.， 2023)和Retrieve What You Need (Wang et al.， 2023)。



##### **<strong><strong>提升推理规划能力**</strong>**<strong>：**</strong>**<strong>增强AI代理的推理和规划能力，理解复杂指令，预测未来情景。**</strong></strong>
<td style="vertical-align:top;width:237.7pt;"> Improved agent reasoning and planning. Enhancing the agent’s ability to reason and plan is pivotal for effective human-agent collaboration. This involves the development of models that can understand complex instructions, infer user intentions, and predict potential future scenarios. This can be accomplished by asking the agent to reflect on past actions and failures as in ReAct (Yao et al., 2023a), or by structuring the agent thought process as a form of search (Yao et al., 2023b). By simulating different outcomes and assessing the ramifications of various actions, agents can make more informed context-aware decisions. </td><td style="vertical-align:top;width:188.4pt;"> 改进代理推理和规划。提高智能体的推理和计划能力是实现高效人机协作的关键。这包括开发能够理解复杂指令、推断用户意图和预测潜在未来场景的模型。这可以通过要求代理反思过去的行为和失败来实现，就像在ReAct中一样(Yao等人，2023a)，或者通过将代理思维过程结构化为一种搜索形式(Yao等人，2023b)。通过模拟不同的结果和评估各种行为的后果，代理可以做出更明智的上下文感知决策。  </td>

改进代理推理和规划。提高智能体的推理和计划能力是实现高效人机协作的关键。这包括开发能够理解复杂指令、推断用户意图和预测潜在未来场景的模型。这可以通过要求代理反思过去的行为和失败来实现，就像在ReAct中一样(Yao等人，2023a)，或者通过将代理思维过程结构化为一种搜索形式(Yao等人，2023b)。通过模拟不同的结果和评估各种行为的后果，代理可以做出更明智的上下文感知决策。

##### **<strong><strong>反馈整合：融合系统和人类反馈，通过学习改进**</strong>**<strong>，**</strong>**<strong>自适应学习机制，优化代理策略**</strong></strong>
<td style="vertical-align:top;width:237.7pt;"> Incorporating system and human feedback. AI agents can frequently operate in two primary contexts: environments that provide explicit signals about the effectiveness of their actions (system feedback), and settings where they collaborate with humans who can offer verbal critiques (human feedback). This direction underscores the need for adaptive learning mechanisms that allow agents to refine their strategies and rectify mistakes, such as in AutoGen (Wu et al., 2023). The ability to continuously learn and adapt from diverse feedback sources ensures that agents remain helpful and aligned for user needs. </td><td style="vertical-align:top;width:188.4pt;"> 结合系统和人的反馈。AI代理通常可以在两种主要环境中运行:提供关于其行动有效性的明确信号的环境(系统反馈)，以及与可以提供口头批评的人类合作的环境(人类反馈)。这一方向强调了对自适应学习机制的需求，该机制允许智能体改进其策略并纠正错误，例如AutoGen (Wu et al.， 2023)。从不同的反馈源中不断学习和适应的能力确保了座席保持帮助并与用户需求保持一致。 </td>

结合系统和人的反馈。AI代理通常可以在两种主要环境中运行:提供关于其行动有效性的明确信号的环境(系统反馈)，以及与可以提供口头批评的人类合作的环境(人类反馈)。这一方向强调了对自适应学习机制的需求，该机制允许智能体改进其策略并纠正错误，例如AutoGen (Wu et al.， 2023)。从不同的反馈源中不断学习和适应的能力确保了座席保持帮助并与用户需求保持一致。





#### **6.6.2 General LLM agent****通用LLM****Agent**

##### **<strong><strong>深入理解生成对话：加入知识检索步骤**</strong></strong>
<td style="vertical-align:top;width:237.7pt;"> Recognizing and understanding agent content and natural language has been a fundamental challenge in interactive AI and natural language processing for decades. With the recent advances in deep learning, there is a growing interest in studying these two areas jointly for deep understanding of both agent planning or human feedback for knowledgeinference and natural language generation. These are the key components of many human-machine-interaction agents, such as “AutoGen"(Wu et al., 2023) and “Retrieve What You Need"(Wang et al., 2023g). </td><td style="vertical-align:top;width:188.4pt;"> 几十年来，识别和理解智能体内容和自然语言一直是交互式人工智能和自然语言处理的一个基本挑战。随着深度学习的最新进展，人们越来越有兴趣联合研究这两个领域，以深入理解智能体规划或用于知识推理和自然语言生成的人类反馈。这些是许多人机交互代理的关键组成部分，例如“AutoGen”(Wu et al.， 2023)和“Retrieve What You Need”(Wang et al.， 2023)。 </td>

几十年来，识别和理解智能体内容和自然语言一直是交互式人工智能和自然语言处理的一个基本挑战。随着深度学习的最新进展，人们越来越有兴趣联合研究这两个领域，以深入理解智能体规划或用于知识推理和自然语言生成的人类反馈。这些是许多人机交互代理的关键组成部分，例如“AutoGen”(Wu et al.， 2023)和“Retrieve What You Need”(Wang et al.， 2023)。

#### Figure 28: The training recipe used to train the Alpaca model (Taori et al., 2023). At a high level, existing LLMs are used to generate a large pool of instruction-following examples from a smaller set of seed tasks. The generated instruction-following examples are then used to instruction-tune an LLM where the underlying model weights are available.

<img alt="" height="741" src="https://img-blog.csdnimg.cn/direct/e292db242d6d41c7877aa654bec7890a.png" width="1136">



#### Figure 29: The logic transformer agent model (Wang et al., 2023e). We integrate a logical reasoning module into the transformer-based abstractive summarization model in order to endow the logic agent the ability to reason over text and dialogue logic, so that it can generate better-quality abstractive summarizations and reduce factuality errors.

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/direct/6656e4dab70c45989b6fe9f48c95c89d.png" width="1200">

#### Figure 30: Architecture of one proposed NLP agent (Wang et al., 2023g) mutual learning framework. In each epoch, Phase 1 and Phase 2 are executed alternately. During Phase 1, the parameters of the reader model remain fixed, and only the weights of the knowledge selector are updated. Conversely, during Phase 2, the reader model’s parameters are adjusted, while the knowledge selector’s weights remain frozen.

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/direct/72a548dfae6249dda21e4bb7226a88d8.png" width="1200">



#### **6.6.3 Instruction-following LLM agents****遵循指令的LLM****Agent**

##### **<strong><strong>指令遵循LLM：通过强化学习或指令调整训练AI代理有效遵循人类指令。**</strong></strong>
<td style="vertical-align:top;width:237.7pt;"> Furthermore, the creation of LLM Agents that can be trained to effectively follow human instructions has become an important area of research. Initial models used human feedback to train a proxy reward model to simulate human preferences, through a process known as Reinforcement Learning with Human Feedback (RLHF) (Ouyang et al., 2022). This process produced models such as InstructGPT and ChatGPT. In order to more efficiently train instruction-following LLM agents without needing human labels, researchers developed a more efficient method for instruction-tuning that trains the LLM agent directly on instruction/response pairs, either generated by humans like Dolly 2.0 6 or automatically from LLMs like Alpaca (Taori et al., 2023). We show the overall Alpaca training pipeline in Figure 28. </td><td style="vertical-align:top;width:188.4pt;"> 此外，可以训练的LLM代理的创建，以有效地遵循人类的指令已成为一个重要的研究领域。初始模型使用人类反馈来训练代理奖励模型来模拟人类偏好，这一过程被称为人类反馈强化学习(RLHF) (Ouyang等人，2022)。这个过程产生了像InstructGPT和ChatGPT这样的模型。为了在不需要人类标记的情况下更有效地训练遵循指令的LLM代理，研究人员开发了一种更有效的指令调优方法，直接在指令/响应对上训练LLM代理，这些指令/响应对要么是由人类生成的，如Dolly 2.0 6，要么是由LLM自动生成的，如Alpaca (Taori et al.， 2023)。我们在图28中展示了整个羊驼训练管道。  </td>

此外，可以训练的LLM代理的创建，以有效地遵循人类的指令已成为一个重要的研究领域。初始模型使用人类反馈来训练代理奖励模型来模拟人类偏好，这一过程被称为人类反馈强化学习(RLHF) (Ouyang等人，2022)。这个过程产生了像InstructGPT和ChatGPT这样的模型。为了在不需要人类标记的情况下更有效地训练遵循指令的LLM代理，研究人员开发了一种更有效的指令调优方法，直接在指令/响应对上训练LLM代理，这些指令/响应对要么是由人类生成的，如Dolly 2.0 6，要么是由LLM自动生成的，如Alpaca (Taori et al.， 2023)。我们在图28中展示了整个羊驼训练管道。



#### **6.6.4 Experiments and Results****实验和结果**

##### **<strong><strong>逻辑感知模型：构建逻辑感知的输入嵌入，提升Transformer语言模型的逻辑理解能力。**</strong></strong>
<td style="vertical-align:top;width:258pt;"> Despite the growing adoption of conversational and self-feedback systems, these forms of AI still do not perform well with regard to generating factually correct responses from their own implicit knowledge and therefore often use external tools like web search and knowledge retrieval mechanisms at inference-time to augment their response as a consequence. Addressing this would help create more engaging experiences for users in many real-life applications. In social conversations (such as those on social media platforms like Instagram and Facebook), or with Q+A websites (such as Ask or Quora), people usually engage with others through a series of comments and by web-searching for information and knowledge relevant to the discussion. Thus, the task of generating conversational turns in this context is not to simply bootstrap upon traditional NLP models and tasks, but to use agents to generate dialogue through intelligent behaviors that reflect knowledge search and acquisition (Peng et al., 2023). In this way, intelligent agents for NLP tasks extends the task description and improves upon the interpretability of the response by adding an explicit knowledge search and retrieval step during dialogue. Incorporating these web search and retrieval agents as feedback during dialogue will help to engage further and deeper the social interactions between humans and agents (Wang et al., 2023e). As the Fig 29 showed, we introduced a new modeling paradigm for transformer language models that detects and extracts important logical structures and information from input texts and then integrates them into the input embeddings through carefully designed multi-layer hierarchical logical projections to infuse logical structures into pre-trained language models as one kind of NLP agent. (Wang et al., 2023e) propose a novel approach to construct logic-aware input embeddings for transformer language models through a combination of logic detection, logic mapping and hierarchical logical projections, and then develop a corresponding new modeling paradigm that can upgrade all existing transformer language models into logical transformers to consistently boost their performance. The proposed logical transformer agent consistently achieve superior performance over their baseline transformer models through a deeper understanding of the logical structures of texts. To human users, it is often these aspects that are more important for delivering a meaningful and interesting conversation via a agent-based coordination between dialogue and information retrieval. Delving deep into natural language processing, this topic will discuss the advancements and leader-board in making LLMs more agentic and better suited for various language-centered tasks. </td><td style="vertical-align:top;width:168.1pt;"> 尽管越来越多的人采用会话和自我反馈系统，但这些形式的人工智能在从自己的隐性知识中生成事实正确的反应方面仍然表现不佳，因此经常在推理时使用网络搜索和知识检索机制等外部工具来增强他们的反应。解决这个问题将有助于在许多实际应用中为用户创造更吸引人的体验。在社交对话(如Instagram和Facebook等社交媒体平台)或问答网站(如Ask或Quora)中，人们通常通过一系列评论和网络搜索与讨论相关的信息和知识来与他人交流。因此，在这种情况下生成会话回合的任务不是简单地引导传统的NLP模型和任务，而是使用代理通过反映知识搜索和获取的智能行为来生成对话(Peng et al.， 2023)。通过这种方式，NLP任务的智能代理扩展了任务描述，并通过在对话期间添加明确的知识搜索和检索步骤，提高了响应的可解释性。将这些网络搜索和检索代理作为对话期间的反馈，将有助于进一步深入地参与人类和代理之间的社会互动(Wang et al.， 2023e)。 如图29所示，我们为转换语言模型引入了一种新的建模范式，该范式从输入文本中检测并提取重要的逻辑结构和信息，然后通过精心设计的多层分层逻辑投影将其集成到输入嵌入中，将逻辑结构作为一种NLP代理注入预训练的语言模型中。 (Wang et al.， 2023e)提出了一种新颖的方法，通过逻辑检测、逻辑映射和分层逻辑投影相结合，为变压器语言模型构建逻辑感知输入嵌入，然后开发相应的新建模范式，将所有现有的变压器语言模型升级为逻辑变压器，以持续提高其性能。所提出的逻辑变压器代理通过对文本逻辑结构的深入理解，始终如一地实现优于其基准变压器模型的卓越性能。对于人类用户来说，这些方面对于通过对话和信息检索之间基于代理的协调来传递有意义和有趣的对话更为重要。深入研究自然语言处理，本主题将讨论使llm更具有代理性和更适合各种以语言为中心的任务的进展和排行榜。 </td>

尽管越来越多的人采用会话和自我反馈系统，但这些形式的人工智能在从自己的隐性知识中生成事实正确的反应方面仍然表现不佳，因此经常在推理时使用网络搜索和知识检索机制等外部工具来增强他们的反应。解决这个问题将有助于在许多实际应用中为用户创造更吸引人的体验。在社交对话(如Instagram和Facebook等社交媒体平台)或问答网站(如Ask或Quora)中，人们通常通过一系列评论和网络搜索与讨论相关的信息和知识来与他人交流。因此，在这种情况下生成会话回合的任务不是简单地引导传统的NLP模型和任务，而是使用代理通过反映知识搜索和获取的智能行为来生成对话(Peng et al.， 2023)。通过这种方式，NLP任务的智能代理扩展了任务描述，并通过在对话期间添加明确的知识搜索和检索步骤，提高了响应的可解释性。将这些网络搜索和检索代理作为对话期间的反馈，将有助于进一步深入地参与人类和代理之间的社会互动(Wang et al.， 2023e)。

(Wang et al.， 2023e)提出了一种新颖的方法，通过逻辑检测、逻辑映射和分层逻辑投影相结合，为变压器语言模型构建逻辑感知输入嵌入，然后开发相应的新建模范式，将所有现有的变压器语言模型升级为逻辑变压器，以持续提高其性能。所提出的逻辑变压器代理通过对文本逻辑结构的深入理解，始终如一地实现优于其基准变压器模型的卓越性能。对于人类用户来说，这些方面对于通过对话和信息检索之间基于代理的协调来传递有意义和有趣的对话更为重要。深入研究自然语言处理，本主题将讨论使llm更具有代理性和更适合各种以语言为中心的任务的进展和排行榜。



##### **<strong><strong>知识选择器：提出互学习框架，通过知识选择器代理优化检索-阅读模型的性能。**</strong></strong>
<td style="vertical-align:top;width:258pt;"> An open-domain question answering (QA) system usually follows a retrieve-then-read paradigm, in which a retriever is used to retrieve relevant passages from a large corpus, and then a reader generates answers based on the retrieved passages and the original question. In (Wang et al., 2023g), we propose a simple and novel mutual learning framework to improve the performance of retrieve-then-read-style models via an intermediate module named the knowledge selector agent, which we train with reinforcement learning. The fine-grained knowledge selector into the retrieve-thenreader paradigm, whose goal is to construct a small subset of passages which retain question-relevant information. As showed in Figure 30, The knowledge selector agent is trained as a component of our novel mutual learning framework, which iteratively trains the knowledge selector and the reader. We adopt a simple and novel approach employing policy gradients to optimize the knowledge selector agnet, using feedback from the reader to train it to select a small and informative set of passages. This approach avoids brute-force search or manually-designed heuristics, without requiring any annotated query-document pairs for supervision. We show that iteratively training the reader and the knowledge selector agent leads to better predictive performance on some public open-domain question answering benchmarks. </td><td style="vertical-align:top;width:168.1pt;"> 开放域问答(QA)系统通常遵循“先检索后阅读”的模式，即使用检索器从大型语料库中检索相关段落，然后读者根据检索到的段落和原始问题生成答案。在(Wang et al.， 2023g)中，我们提出了一个简单而新颖的相互学习框架，通过一个名为知识选择代理的中间模块来提高检索-阅读风格模型的性能，我们使用强化学习对其进行训练。将细粒度的知识选择器转换为“检索-然后阅读”范式，其目标是构建保留问题相关信息的小段落子集。如图30所示，知识选择器代理作为我们新的相互学习框架的一个组件进行训练，该框架迭代地训练知识选择器和读取器。我们采用了一种简单而新颖的方法，使用策略梯度来优化知识选择器，使用来自读者的反馈来训练它选择一组小而信息量大的段落。这种方法避免了暴力搜索或手动设计的启发式方法，不需要任何带注释的查询文档对进行监督。我们表明，迭代训练读者和知识选择器代理可以在一些公共开放领域问答基准上获得更好的预测性能。 </td>

开放域问答(QA)系统通常遵循“先检索后阅读”的模式，即使用检索器从大型语料库中检索相关段落，然后读者根据检索到的段落和原始问题生成答案。在(Wang et al.， 2023g)中，我们提出了一个简单而新颖的相互学习框架，通过一个名为知识选择代理的中间模块来提高检索-阅读风格模型的性能，我们使用强化学习对其进行训练。将细粒度的知识选择器转换为“检索-然后阅读”范式，其目标是构建保留问题相关信息的小段落子集。如图30所示，知识选择器代理作为我们新的相互学习框架的一个组件进行训练，该框架迭代地训练知识选择器和读取器。我们采用了一种简单而新颖的方法，使用策略梯度来优化知识选择器，使用来自读者的反馈来训练它选择一组小而信息量大的段落。这种方法避免了暴力搜索或手动设计的启发式方法，不需要任何带注释的查询文档对进行监督。我们表明，迭代训练读者和知识选择器代理可以在一些公共开放领域问答基准上获得更好的预测性能。





## **7 Agent AI Across Modalities, Domains, and Realities ****跨模态、领域和现实的****人工智能代理**

### **7.1 Agents for Cross-modal Understanding**** 用于跨模态理解的****Agent**
<td style="vertical-align:top;width:237.7pt;"> Multi-modal understanding is a significant challenge for creating generalist AI agents due to the lack of large-scale datasets that contain vision, language, and agent behavior. More generally, training data for AI agents is often modality specific. This results in most modern multi-modal systems using a combination of frozen submodules. Some notable examples are Flamingo (Alayrac et al., 2022), BLIP-2 (Li et al., 2023c), and LLaVA (Liu et al., 2023c), all of which utilize a frozen LLM and frozen visual encoder. These submodules are trained individually on separate datasets, and then adaptation layers are trained to encode the visual encoder into the LLM embedding space. In order to make further progress for cross-modal understanding for AI agents, it is likely that the strategy of using frozen LLMs and visual encoders will need to change. Indeed, RT-2, a recent visual-language model that is capable of taking actions within the domain of robotics showed significantly improved performance when jointly tuning the visual encoder and LLM for robotics and visual-language tasks (Brohan et al., 2023). </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>





### **7.2 Agents for Cross-domain Understanding****用于跨领域理解的****Agent**




<td style="vertical-align:top;width:237.7pt;"> A key challenge for creating generalist agents is the distinctive visual appearance and disparate action spaces across different domains. Humans possess the capability to interpret images and videos from various sources, including the real world, video games, and specialized domains such as robotics and healthcare, once they become familiar with the specific details of these areas. However, existing LLMs and VLMs often demonstrate significant differences between the data they were trained on and the varied domains in which they are applied. And notably, training agent models to predict specific actions presents a considerable challenge when trying to develop a single policy that can effectively learn multiple control systems across domains. Generally, the approach most modern works take when applying systems within specific domains is to start from a pretrained foundation model and then finetune a separate model for each specific domain. This fails to capture any commonalities between domains and results in a smaller total set of data used for training instead of leveraging each domain’s data. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>









### **7.3 Interactive agent for cross-modality and cross-reality****用于跨模态和跨现实的互动****Agent**
<td style="vertical-align:top;width:237.7pt;"> Developing AI agents that can successfully understand and perform tasks across different realities is an on-going challenge that has seen some recent success for image and scene generation (Huang et al., 2023a). In particular, it is challenging for agents to simultaneously understand real-world and virtual reality environments due to their visual dissimilarities and separate environment physics. Within the context of cross-reality, Sim to Real transfer is a particularly important problem when using simulation-trained policies for real-world data, which we discuss in the next section. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>







### **7.4 Sim to Real Transfer****从模拟到真实的转移**
<td style="vertical-align:top;width:237.7pt;"> Techniques which enable models trained in simulation to be deployed in the real world. Embodied agents, especially one based on RL policies, are typically trained in simulated environments. These simulations do not fully replicate the characteristics of the real world (e.g., disturbances, light, gravity, and other physical properties). Due to this discrepancy between simulation and reality, models trained in simulation often struggle to perform well when applied in the real world. This issue is known as the “sim-to-real” problem. To solve this problem, several approaches can be taken: </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> Domain randomization: domain randomization is a technique that trains a model while randomly varying parameters within a simulation environment (e.g., object appearance, sensor noise, and optical properties) in anticipation of the uncertainties and variations of the real world (Tobin et al., 2017). For instance, in the context of training a RL-based grasping skills, introducing randomness in the shapes of objects can lead to a policy capable of adapting to objects with somewhat different shapes (Saito et al., 2022). &gt;&gt;Domain adaptation: Domain adaptation, or domain transfer is a technique that bridges the gap between simulated and real-world domains by training models with a large number of simulated images and a smaller set of real-world images. In practical settings, unpaired image-to-image translation methods such as CycleGAN (Zhu et al., 2017b) are employed due to the difficulty in preparing paired images across domains. Several enhanced versions exist for reinforcement learning, including RL-CycleGAN (Rao et al., 2020), and for imitation learning, such as RetinaGAN (Ho et al., 2021). &gt;&gt;Improvement of simulation: Realistic simulation is a key for sim-to-real transfer. Part of this effort is achieved by a system identification techniques (Zhu et al., 2017c; Allevato et al., 2020), which aims to identify simulation parameters to mimic the real-world environments. Additionally, use of photorealistic simulators would be effective in image-based reinforcement learning (Martinez-Gonzalez et al., 2020; Müller et al., 2018; Shah et al., 2018; Sasabuchi et al., 2023). </td><td style="vertical-align:top;width:188.4pt;">  </td>

&gt;&gt;Domain adaptation: Domain adaptation, or domain transfer is a technique that bridges the gap between simulated and real-world domains by training models with a large number of simulated images and a smaller set of real-world images. In practical settings, unpaired image-to-image translation methods such as CycleGAN (Zhu et al., 2017b) are employed due to the difficulty in preparing paired images across domains. Several enhanced versions exist for reinforcement learning, including RL-CycleGAN (Rao et al., 2020), and for imitation learning, such as RetinaGAN (Ho et al., 2021).


<td style="vertical-align:top;width:237.7pt;"> The sim-to-real transfer remains a central challenge in the study of Embodied Agents, as approaches keep evolving. Both theoretical and empirical research are essential to advance these technologies further. </td><td style="vertical-align:top;width:188.4pt;">  </td>







## **8 Continuous and Self-improvement for Agent ****人工智能代理**** AI 的持续和自我改进**


<td style="vertical-align:top;width:237.7pt;"> Currently, foundation model based AI agents have the capacity to learn from multiple different data sources, which allow for more flexible sources for data for training. Two key consequences of this are (1) user and human-based interaction data can be used to further refine and improve the agent and (2) existing foundation models and model artifacts can be used to generate training data. We discuss each of these in more detail in the following sections, but we note that since current AI Agents are largely tied to existing pretrained foundation models, they generally do not learn from continuous interaction with their environments. We think this is an exciting future direction, and initial work by Bousmalis et al. has shown that self-improving agents for robotic control are able to continuous learn and improve through environmental interactions without supervision (Bousmalis et al., 2023). </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>





### **8.1 Human-based Interaction Data****基于人类交互数据**




<td style="vertical-align:top;width:237.7pt;"> The core idea behind using human-based interaction data is to leverage a large number of of agent-human interactions to train and improve future iterations of the agent. There are several strategies used to improve agents from human-agent interactions. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> &gt;&gt;Additional training data Perhaps the simplest usage of human-agent interactions is to use the interaction examples themselves as training data for a future iteration of the agent. This generally requires filtering 49 Agent AI: Surveying the Horizons of Multimodal Interaction A PREPRINT strategies to differentiate successful agent examples from unsuccessful interaction examples. Filtering can be rules-based (e.g., reaching some desired end goal state), model-based (e.g., classifying successful vs unsuccessful interactions), or manually selected after a posthoc inspection and/or modification of the interaction examples.  &gt;&gt;Human preference learning During interaction with the user, the agent system can prompt the user with several different model outputs and allow for the user to select the best output. This is commonly used by LLMs like ChatGPT and GPT-4, whereby users can select one output (out of several) that aligns best with their preferences. &gt;&gt;Safety training (red-teaming) Red-teaming within the context of Agent AI refers to having a dedicated team of adversaries (either human or computer) that seek to exploit and expose weaknesses and vulnerabilities within the Agent AI system. Although adversarial in nature, red-teaming is commonly used as a means for understanding how to improve AI safety measures and reduce the occurrence of harmful outputs. The core principle is to discover consistent methods for inducing unwanted agent outputs so that the model can be trained on data that explicitly corrects this behavior. </td><td style="vertical-align:top;width:188.4pt;">  </td>

 &gt;&gt;Human preference learning During interaction with the user, the agent system can prompt the user with several different model outputs and allow for the user to select the best output. This is commonly used by LLMs like ChatGPT and GPT-4, whereby users can select one output (out of several) that aligns best with their preferences.


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>







### **8.2 Foundation Model Generated Data**** 基础模型生成的数据**


<td style="vertical-align:top;width:237.7pt;"> With the advent of powerful foundation model artifacts produced by academia and industry, there have been a variety of methods developed to extract and generate meaningful training data from these artifacts using a variety of prompting and data-pairing techniques. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> &gt;&gt;LLM Instruction-tuning Methods for generating instruction-following training data from LLMs have allowed for the finetuning of smaller, open-source models based on the outputs of larger proprietary LLMs (Wang et al., 2022b). For example, Alpaca (Taori et al., 2023) and Vicuna (Zheng et al., 2023) are LLMs based on the open-source LLaMA family (Touvron et al., 2023) that have been tuned on various outputs from ChatGPT and human participants. This method of instruction tuning can be viewed as a form of knowledge distillation, where the larger LLM serves as a teacher model to a smaller student model. Importantly, although LLM instruction-tuning has been shown to transfer the writing style and some instruction-following capabilities of the teacher model to the student model, significant gaps still exist between the factuality and capabilities of the teacher and student models (Gudibande et al., 2023). &gt;&gt;Vision-language pairs A number of recent works have sought to increase the number of diversity of pretraining data available to visual-language models by automatically generating captions and other text for visual content. For example, LLaVA (Liu et al., 2023c) uses 150,000 examples of instruction-following behavior from textual and visual inputs that are mainly LLM-generated. Other work has shown that using VLMs to re-caption images can improve the training data and subsequent quality of image generation models (Segalis et al., 2023). Within the realm of video understanding, using VLMs and LLMs to recaption videos has been shown to improve the performance and quality of subsequent VLMs trained on the recaptioned videos (Wang et al., 2023f; Zhao et al., 2022). </td><td style="vertical-align:top;width:188.4pt;">  </td>

&gt;&gt;Vision-language pairs A number of recent works have sought to increase the number of diversity of pretraining data available to visual-language models by automatically generating captions and other text for visual content. For example, LLaVA (Liu et al., 2023c) uses 150,000 examples of instruction-following behavior from textual and visual inputs that are mainly LLM-generated. Other work has shown that using VLMs to re-caption images can improve the training data and subsequent quality of image generation models (Segalis et al., 2023). Within the realm of video understanding, using VLMs and LLMs to recaption videos has been shown to improve the performance and quality of subsequent VLMs trained on the recaptioned videos (Wang et al., 2023f; Zhao et al., 2022).
<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>







## **9 Agent Dataset and Leaderboard****Agent****数据集和排行榜**


<td style="vertical-align:top;width:237.7pt;"> To accelerate research in this domain, we propose two benchmarks respectively for multi-agent gaming and agentic visual language tasks. We will release two new datasets - “CuisineWorld” and “VideoAnalytica” - and a set of baseline models, encouraging participants to explore new models, systems, and submit their results on the test set of our leaderboard. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>









### **9.1 “CuisineWorld” Dataset for Multi-agent Gaming****多****Agent****游戏数据集**
<td style="vertical-align:top;width:237.7pt;"> CuisineWorld is a text-based game reminiscent of Overcooked! It offers a platform for AI-powered agents to cooperate and play in tandem. This dataset will test the collaboration efficiency of multi-agent systems, offering insights into how well LLMs and other systems can work together in dynamic scenarios. In particular, the dataset will focus on how well the agents understand goals, and how well the agents can coordinate among themselves. Two types of modes are supported in this dataset: a centralized dispatcher mode and a decentralized mode. Participants can choose a play mode and make a submission to our leaderboard. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>









#### **9.1.1 Benchmark****基准**
<td style="vertical-align:top;width:237.7pt;"> For our competition, we will release a benchmark, the CuisineWorld benchmark, which includes a text interface that includes extendable task definition files, and an interface for multi-agent interaction, and human-machine interactions. We introduce the gaming interaction task in which the goal is to generate relevant, appropriate, multi-agent collaboration strategies that can maximize collaboration efficiency. We evaluate the collaboration efficiency with the proposed evaluation metric: CoS. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> The “CuisineWorld" dataset was collected by Microsoft, UCLA, and Stanford University. The goal of the competition is to explore how different, existing and novel, grounded-LLM and interactive techniques perform with this benchmark and establish strong baselines for the task of multi-agent gaming infrastructure. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> The dataset of CuisineWorld includes: &gt;&gt;A selection of well-defined multiagent collaboration tasks. &gt;&gt; An API system to facilitate agent interactions. &gt;&gt;An automatic evaluation system. (The link for downloading the dataset will soon be made available and this article will be updated to include it here.) </td><td style="vertical-align:top;width:188.4pt;">  </td>

&gt;&gt;A selection of well-defined multiagent collaboration tasks.

&gt;&gt;An automatic evaluation system. (The link for downloading the dataset will soon be made available and this article will be updated to include it here.)





#### **9.1.2 Task****任务**


<td style="vertical-align:top;width:237.7pt;"> We provide a dataset and related the benchmark, called Microsoft MindAgent and and correspondingly release a dataset “CuisineWorld” to the to the research community. • We will provide benchmarks to evaluate and rank the submitted “MindAgent" algorithms. We will also provide baseline results generated using popular infrastructures. </td><td style="vertical-align:top;width:188.4pt;">  </td>

• We will provide benchmarks to evaluate and rank the submitted “MindAgent" algorithms. We will also provide baseline results generated using popular infrastructures.
<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>







#### **9.1.3 Metrics and Judging****指标和评判**


<td style="vertical-align:top;width:237.7pt;"> The quality of multi-agent collaboration efficiency is determined by the new “cos" auto-metric (from MindAgent (Gong et al., 2023a)). The final rating of out metric is calculated as an average over the evaluated collaboration efficiency metrics of the multi-agent system on all tasks. Human evaluators will be asked to rate individual responses as well as provide subjective judgement of the engagement, breadth and an overall quality of the users’ interactions with the agents. </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>







#### **9.1.4 Evaluation****评估**


<td style="vertical-align:top;width:237.7pt;"> Automated Evaluation. We plan to release a leaderboard, starting on the release date (TBA), registered participants will be asked to submit their results on the task associated with the dataset “CuisineWorld" (our publicly released dataset for the leaderboard). Submission of results will be closed on the end date (TBA). Each team will be required to submit their generated results on the testing set for automated evaluation of the “cos" metric. &gt;&gt;Human Evaluation on our leaderboard. The leaderboard participants will need to provide a submission file generated by evaluation scripts locally. We will use the evalAI system to check the submission file and optionally rerun the code for top challenge contenders. Therefore, teams must also submit their code with a Readme file on how to run their code. Human evaluation will be performed by the organization team. &gt;&gt;Winner Announcement. We will make an announcement of the winners and post the final ratings of the submissions on our leaderboard. </td><td style="vertical-align:top;width:188.4pt;">  </td>

&gt;&gt;Human Evaluation on our leaderboard. The leaderboard participants will need to provide a submission file generated by evaluation scripts locally. We will use the evalAI system to check the submission file and optionally rerun the code for top challenge contenders. Therefore, teams must also submit their code with a Readme file on how to run their code. Human evaluation will be performed by the organization team.


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;">  </td><td style="vertical-align:top;width:188.4pt;">  </td>







### **9.2 Audio-Video-Language Pre-training Dataset****音频-视频-语言预训练数据集**


<td style="vertical-align:top;width:237.7pt;"> We introduce VideoAnalytica: a new benchmark for analytical video demonstration comprehension. VideoAnalytica focuses on leveraging video demonstrations as aids to better understand complex, high-level reasoning embedded within long-formed instructional videos. The objective is to evaluate the cognitive reasoning abilities of video language models, pushing them beyond mere recognition tasks and basic comprehension, towards a more sophisticated and nuanced understanding of videos. Crucially, VideoAnalytica emphasizes the integration of multiple modalities, such as audio, video, and language, as well as the ability of models to apply domain-specific knowledge, to contextualize and interpret the information presented in the videos. Specifically, VideoAnalytica involves two primary tasks: </td><td style="vertical-align:top;width:188.4pt;">  </td>


<td style="vertical-align:top;width:237.7pt;"> 1.Video Text Retrieval: This task involves accurately retrieving relevant text from the instructional videos. The challenge lies in distinguishing between relevant and irrelevant information, thus requiring a deep understanding of the video content, and analysis of the demonstration to retrieve the correct query. To further increase the complexity of these tasks, we introduce hard negatives into our datasets generated by large language models. We run human validation on the generated negatives and remove instances that make the task invalid and unfair (e.g. negatives being valid).  2. Video Assisted Informative Question Answering: This task requires the model to answer questions based on the information extracted from the videos. The focus is on complex questions that require analytical reasoning and a thorough comprehension of the video demonstration. </td><td style="vertical-align:top;width:188.4pt;">  </td>

 2. Video Assisted Informative Question Answering: This task requires the model to answer questions based on the information extracted from the videos. The focus is on complex questions that require analytical reasoning and a thorough comprehension of the video demonstration.
<td style="vertical-align:top;width:237.7pt;"> &gt;&gt;The leaderboard participants will need to submit their solutions for evaluation. The evaluation will be based on the model’s performance on the two tasks, and the results will be displayed on the leaderboard. Participants are required to submit their code, along with a detailed explanation of their approach and methodology. &gt;&gt;Ethical considerations: The leaderboard focuses on understanding and interpreting video content, which could potentially be used in surveillance or other privacy-invasive applications. Therefore, it’s crucial to consider the ethical implications and potential misuse of the technology. We encourage participants to consider these aspects in their submissions and promote the ethical use of AI. </td><td style="vertical-align:top;width:188.4pt;">  </td>

&gt;&gt;Ethical considerations: The leaderboard focuses on understanding and interpreting video content, which could potentially be used in surveillance or other privacy-invasive applications. Therefore, it’s crucial to consider the ethical implications and potential misuse of the technology. We encourage participants to consider these aspects in their submissions and promote the ethical use of AI.









## **10 Broader Impact Statement****更广泛的影响声明**
<td style="vertical-align:top;width:254.3pt;"> This article and our associated forum 7 aim to be a catalyst for innovative research, fostering collaborations that will drive the next wave of AI applications. By focusing on multimodal agents, we emphasize the future direction of human-AI interactions, leader-board, and solutions. We detail three ways in which we make significant contributions to the broader community. </td><td style="vertical-align:top;width:171.8pt;"> 本文和我们的相关论坛旨在成为创新研究的催化剂，促进合作，推动下一波人工智能应用。通过关注多模态智能体，我们强调了人类与人工智能交互、排行榜和解决方案的未来方向。我们详细介绍了我们为更广泛的社区做出重大贡献的三种方式。  </td>

本文和我们的相关论坛旨在成为创新研究的催化剂，促进合作，推动下一波人工智能应用。通过关注多模态智能体，我们强调了人类与人工智能交互、排行榜和解决方案的未来方向。我们详细介绍了我们为更广泛的社区做出重大贡献的三种方式。
<td style="vertical-align:top;width:254.3pt;"> Firstly, we hope our forum grounds AI researchers to develop solutions motivated by real-world problems in gaming, robotics, healthcare, and long-video understanding. Specifically, the development of multimodal agents in gaming could lead to more immersive and personalized gaming experiences, thereby transforming the gaming industry. In robotics, the development of adaptive robotic systems could revolutionize industries ranging from manufacturing to agriculture, potentially addressing labor shortages and improving efficiency. In healthcare, the use of LLMs and VLMs as diagnostic agents or patient care assistants could lead to more accurate diagnoses, improved patient care, and increased accessibility to medical services, particularly in underserved areas. Furthermore, the ability of these models to interpret long-form videos could have far-reaching applications, from enhancing online learning to improving technical support services. In general, the topics covered in our forum will have significant downstream effects on a wide range of industries and humans across the world. </td><td style="vertical-align:top;width:171.8pt;"> 首先，我们希望我们的论坛能够为人工智能研究人员提供基础，以解决游戏、机器人、医疗保健和长视频理解等现实问题。具体来说，游戏中多模式代理的发展可以带来更加身临其境和个性化的游戏体验，从而改变游戏行业。在机器人技术方面，自适应机器人系统的发展可能会彻底改变从制造业到农业的各个行业，有可能解决劳动力短缺问题并提高效率。在医疗保健领域，使用llm和vlm作为诊断代理或患者护理助理可以导致更准确的诊断，改善患者护理，并增加获得医疗服务的机会，特别是在服务不足的地区。此外，这些模型解释长视频的能力可能具有深远的应用，从加强在线学习到改善技术支持服务。总的来说，我们论坛所涵盖的主题将对全球范围内广泛的行业和人类产生重大的下游影响。  </td>

首先，我们希望我们的论坛能够为人工智能研究人员提供基础，以解决游戏、机器人、医疗保健和长视频理解等现实问题。具体来说，游戏中多模式代理的发展可以带来更加身临其境和个性化的游戏体验，从而改变游戏行业。在机器人技术方面，自适应机器人系统的发展可能会彻底改变从制造业到农业的各个行业，有可能解决劳动力短缺问题并提高效率。在医疗保健领域，使用llm和vlm作为诊断代理或患者护理助理可以导致更准确的诊断，改善患者护理，并增加获得医疗服务的机会，特别是在服务不足的地区。此外，这些模型解释长视频的能力可能具有深远的应用，从加强在线学习到改善技术支持服务。总的来说，我们论坛所涵盖的主题将对全球范围内广泛的行业和人类产生重大的下游影响。
<td style="vertical-align:top;width:254.3pt;"> Secondly, we hope our forum stands as a valuable resource for AI practitioners and researchers alike, serving as a platform to explore and deeply comprehend the diverse and complex leader-board that come with implementing AI agents across a wide variety of environments and situations. This exploration includes, for instance, understanding the specific limitations and potential hazards linked to Agentic AI systems when they are developed for specialized sectors such as healthcare diagnostics. In this domain, issues like dangerous hallucinations in AI behavior can pose significant risks, highlighting the critical need for meticulous design and testing. However, these specific leader-board may not be equally relevant or noticeable when considering AI agents crafted for the gaming industry. In such recreational fields, developers might instead prioritize tackling different hurdles, such as the need for AI to perform more open-ended generation and exhibit creativity, adapting dynamically to unpredictable gameplay scenarios and player interactions. By attending the forum, participants will gain insights into how these varied environments dictate the focus and direction of AI development, and how best to tailor AI solutions to meet these distinct needs and overcome the pertinent leader-board. </td><td style="vertical-align:top;width:171.8pt;"> 其次，我们希望我们的论坛能够成为人工智能从业者和研究人员的宝贵资源，作为一个平台，探索和深入理解在各种环境和情况下实施AI代理所带来的多样化和复杂的排行榜。例如，这一探索包括了解在为医疗保健诊断等专业领域开发人工智能系统时与之相关的具体限制和潜在危害。在这个领域中，AI行为中的危险幻觉等问题可能会带来重大风险，这凸显了细致设计和测试的必要性。然而，当考虑到为游戏行业设计的AI代理时，这些特定的排行榜可能并不同样相关或引人注目。在这类娱乐领域，开发者可能会优先处理不同的障碍，比如AI需要执行更多开放式生成和展示创造力，动态适应不可预测的玩法场景和玩家互动。通过参加论坛，与会者将深入了解这些不同的环境如何决定人工智能发展的重点和方向，以及如何最好地定制人工智能解决方案，以满足这些不同的需求，并克服相关的排行榜。  </td>

其次，我们希望我们的论坛能够成为人工智能从业者和研究人员的宝贵资源，作为一个平台，探索和深入理解在各种环境和情况下实施AI代理所带来的多样化和复杂的排行榜。例如，这一探索包括了解在为医疗保健诊断等专业领域开发人工智能系统时与之相关的具体限制和潜在危害。在这个领域中，AI行为中的危险幻觉等问题可能会带来重大风险，这凸显了细致设计和测试的必要性。然而，当考虑到为游戏行业设计的AI代理时，这些特定的排行榜可能并不同样相关或引人注目。在这类娱乐领域，开发者可能会优先处理不同的障碍，比如AI需要执行更多开放式生成和展示创造力，动态适应不可预测的玩法场景和玩家互动。通过参加论坛，与会者将深入了解这些不同的环境如何决定人工智能发展的重点和方向，以及如何最好地定制人工智能解决方案，以满足这些不同的需求，并克服相关的排行榜。
<td style="vertical-align:top;width:254.3pt;"> Thirdly, the various elements of our event, including the expert presentations, informative posters, and notably the winners of our two leader-board, are set to offer a substantive yet succinct overview of the latest and significant trends, research directions, and innovative concepts in the realm of multimodal agents. These presentations will encapsulate pivotal findings and developments, shining a light on new systems, ideas, and technologies in the field of mulitmodal agent AI. This assortment of knowledge is not only beneficial for the attendees of our forum, who are looking to deepen their understanding and expertise in this domain, but it also serves as a dynamic and rich resource board. Those visiting our forum’s website can tap into this reservoir of information to discover and understand the cutting-edge advancements and creative ideas steering the future of multimodal agent AI. We strive to serve as a useful knowledge base for both newcomers and veterans in the field. By engaging with these resources, we hope participants and online visitors alike can remain informed of the transformative changes and novel approaches that are shaping the exciting landscape surrounding multimodal agent AI. </td><td style="vertical-align:top;width:171.8pt;"> 第三，我们的活动的各种元素，包括专家演讲，信息海报，特别是我们的两个排行榜的获奖者，将为多式联运代理领域的最新和重要趋势，研究方向和创新概念提供实质性而简洁的概述。这些演讲将概括关键的发现和发展，照亮在多式联运Agent AI领域的新系统，思想和技术。这种知识的分类不仅有利于我们论坛的与会者，他们希望加深他们在这一领域的理解和专业知识，而且它也是一个充满活力和丰富的资源板。那些访问我们论坛网站的人可以利用这个信息库来发现和理解指导未来多式联运Agent工智能的前沿进展和创意。我们努力为该领域的新手和老手提供有用的知识库。通过使用这些资源，我们希望参与者和在线访问者都能随时了解正在塑造多模式Agent AI周围令人兴奋的景观的变革性变化和新方法。 </td>

第三，我们的活动的各种元素，包括专家演讲，信息海报，特别是我们的两个排行榜的获奖者，将为多式联运代理领域的最新和重要趋势，研究方向和创新概念提供实质性而简洁的概述。这些演讲将概括关键的发现和发展，照亮在多式联运Agent AI领域的新系统，思想和技术。这种知识的分类不仅有利于我们论坛的与会者，他们希望加深他们在这一领域的理解和专业知识，而且它也是一个充满活力和丰富的资源板。那些访问我们论坛网站的人可以利用这个信息库来发现和理解指导未来多式联运Agent工智能的前沿进展和创意。我们努力为该领域的新手和老手提供有用的知识库。通过使用这些资源，我们希望参与者和在线访问者都能随时了解正在塑造多模式Agent AI周围令人兴奋的景观的变革性变化和新方法。





## **11 Ethical Considerations****道德考虑**
<td style="vertical-align:top;width:245.55pt;"> Multimodal Agent AI systems have many applications. In addition to interactive AI, grounded multimodal models could help drive content generation for bots and AI agents, and assist in productivity applications, helping to re-play, paraphrase, action prediction or synthesize 3D or 2D scenario. Fundamental advances in agent AI help contribute towards these goals and many would benefit from a greater understanding of how to model embodied and empathetic in a simulate reality or a real world. Arguably many of these applications could have positive benefits. However, this technology could also be used by bad actors. Agent AI systems that generate content can be used to manipulate or deceive people. Therefore, it is very important that this technology is developed in accordance with responsible AI guidelines. For example, explicitly communicating to users that content is generated by an AI system and providing the user with controls in order to customize such a system. It is possible the Agent AI could be used to develop new methods to detect manipulative content - partly because it is rich with hallucination performance of large foundation model - and thus help address another real world problem. </td><td style="vertical-align:top;width:180.55pt;"> 多模式Agent AI系统有许多应用。除了交互式人工智能，基于多模式的模型可以帮助驱动机器人和AI代理的内容生成，并协助生产力应用程序，帮助重玩，解释，行动预测或合成3D或2D场景。人工智能的基本进展有助于实现这些目标，许多人将受益于对如何在模拟现实或现实世界中建模具体化和移情的更好理解。可以说，这些应用程序中的许多都可以带来积极的好处。 然而，这项技术也可能被坏人利用。生成内容的Agent AI系统可以用来操纵或欺骗人们。因此，根据负责任的人工智能指导方针开发这项技术非常重要。例如，明确地向用户传达内容是由AI系统生成的，并为用户提供控制以自定义这样的系统。Agent AI有可能被用于开发检测操纵内容的新方法——部分原因是它具有丰富的大型基础模型的幻觉表现——从而帮助解决另一个现实世界的问题。  </td>

However, this technology could also be used by bad actors. Agent AI systems that generate content can be used to manipulate or deceive people. Therefore, it is very important that this technology is developed in accordance with responsible AI guidelines. For example, explicitly communicating to users that content is generated by an AI system and providing the user with controls in order to customize such a system. It is possible the Agent AI could be used to develop new methods to detect manipulative content - partly because it is rich with hallucination performance of large foundation model - and thus help address another real world problem.

然而，这项技术也可能被坏人利用。生成内容的Agent AI系统可以用来操纵或欺骗人们。因此，根据负责任的人工智能指导方针开发这项技术非常重要。例如，明确地向用户传达内容是由AI系统生成的，并为用户提供控制以自定义这样的系统。Agent AI有可能被用于开发检测操纵内容的新方法——部分原因是它具有丰富的大型基础模型的幻觉表现——从而帮助解决另一个现实世界的问题。
<td style="vertical-align:top;width:245.55pt;"> For examples, 1) in health topic, ethical deployment of LLM and VLM agents, especially in sensitive domains like healthcare, is paramount. AI agents trained on biased data could potentially worsen health disparities by providing inaccurate diagnoses for underrepresented groups. Moreover, the handling of sensitive patient data by AI agents raises significant privacy and confidentiality concerns. 2) In the gaming industry, AI agents could transform the role of developers, shifting their focus from scripting non-player characters to refining agent learning processes. Similarly, adaptive robotic systems could redefine manufacturing roles, necessitating new skill sets rather than replacing human workers. Navigating these transitions responsibly is vital to minimize potential socio-economic disruptions. </td><td style="vertical-align:top;width:180.55pt;"> 例如，1)在健康主题中，LLM和VLM代理的道德部署，特别是在医疗保健等敏感领域，是至关重要的。接受有偏见数据训练的AI代理可能会为代表性不足的群体提供不准确的诊断，从而加剧健康差距。此外，AI代理对敏感患者数据的处理引发了重大的隐私和保密问题。2)在游戏行业中，AI代理可以改变开发者的角色，将他们的重点从编写非玩家角色转向优化代理学习过程。同样，自适应机器人系统可以重新定义制造业的角色，需要新的技能组合，而不是取代人类工人。负责任地引导这些转变对于尽量减少潜在的社会经济干扰至关重要。  </td>

例如，1)在健康主题中，LLM和VLM代理的道德部署，特别是在医疗保健等敏感领域，是至关重要的。接受有偏见数据训练的AI代理可能会为代表性不足的群体提供不准确的诊断，从而加剧健康差距。此外，AI代理对敏感患者数据的处理引发了重大的隐私和保密问题。2)在游戏行业中，AI代理可以改变开发者的角色，将他们的重点从编写非玩家角色转向优化代理学习过程。同样，自适应机器人系统可以重新定义制造业的角色，需要新的技能组合，而不是取代人类工人。负责任地引导这些转变对于尽量减少潜在的社会经济干扰至关重要。
<td style="vertical-align:top;width:245.55pt;"> Furthermore, the agent AI focuses on learning collaboration policy in simulation and there is some risk if directly applying the policy to the real world due to the distribution shift. Robust testing and continual safety monitoring mechanisms should be put in place to minimize risks of unpredictable behaviors in real-world scenarios. Our “VideoAnalytica" dataset is collected from the Internet and considering which is not a fully representative source, so we already go through-ed the ethical review and legal process from both Microsoft and University Washington. Be that as it may, we also need to understand biases that might exist in this corpus. Data distributions can be characterized in many ways. In this workshop, we have captured how the agent level distribution in our dataset is different from other existing datasets. However, there is much more than could be included in a single dataset or workshop. We would argue that there is a need for more approaches or discussion linked to real tasks or topics and that by making these data or system available. </td><td style="vertical-align:top;width:180.55pt;"> 此外，智能体人工智能侧重于在模拟中学习协作策略，如果将策略直接应用于现实世界，由于分布的变化，存在一定的风险。应该建立健全的测试和持续的安全监控机制，以最大限度地减少现实场景中不可预测行为的风险。我们的“视频分析”数据集是从互联网上收集的，考虑到这不是一个完全有代表性的来源，所以我们已经通过了微软和华盛顿大学的道德审查和法律程序。尽管如此，我们也需要理解这个语料库中可能存在的偏见。数据分布可以用多种方式来描述。在这个研讨会中，我们已经捕获了我们数据集中的代理级别分布与其他现有数据集中的不同之处。然而，在单个数据集或研讨会中可以包含的内容要多得多。我们认为需要更多与实际任务或主题相关的方法或讨论，并通过使这些数据或系统可用。  </td>

此外，智能体人工智能侧重于在模拟中学习协作策略，如果将策略直接应用于现实世界，由于分布的变化，存在一定的风险。应该建立健全的测试和持续的安全监控机制，以最大限度地减少现实场景中不可预测行为的风险。我们的“视频分析”数据集是从互联网上收集的，考虑到这不是一个完全有代表性的来源，所以我们已经通过了微软和华盛顿大学的道德审查和法律程序。尽管如此，我们也需要理解这个语料库中可能存在的偏见。数据分布可以用多种方式来描述。在这个研讨会中，我们已经捕获了我们数据集中的代理级别分布与其他现有数据集中的不同之处。然而，在单个数据集或研讨会中可以包含的内容要多得多。我们认为需要更多与实际任务或主题相关的方法或讨论，并通过使这些数据或系统可用。
<td style="vertical-align:top;width:245.55pt;"> We will dedicate a segment of our project to discussing these ethical issues, exploring potential mitigation strategies, and deploying a responsible multi-modal AI agent. We hope to help more researchers answer these questions together via this paper. </td><td style="vertical-align:top;width:180.55pt;"> 我们将用项目的一部分来讨论这些道德问题，探索潜在的缓解策略，并部署负责任的多模式AI代理。我们希望通过这篇论文帮助更多的研究者共同回答这些问题。 </td>

我们将用项目的一部分来讨论这些道德问题，探索潜在的缓解策略，并部署负责任的多模式AI代理。我们希望通过这篇论文帮助更多的研究者共同回答这些问题。







## **12 Diversity Statement****多样性声明**
<td style="vertical-align:top;width:259.4pt;"> By examining the adaptability of AI agent models in various domains, we inherently embrace a diversity of leader-board, perspectives, and solutions. In this vein, our project aims to build a diverse community by exploring the wide array of subjects in multimodal and agentic AI. </td><td style="vertical-align:top;width:166.7pt;"> 通过研究AI代理模型在各个领域的适应性，我们本质上拥抱了各种各样的排行榜、观点和解决方案。在这种情况下，我们的项目旨在通过探索多模式和Agent工智能的广泛主题来建立一个多样化的社区。 </td>

通过研究AI代理模型在各个领域的适应性，我们本质上拥抱了各种各样的排行榜、观点和解决方案。在这种情况下，我们的项目旨在通过探索多模式和Agent工智能的广泛主题来建立一个多样化的社区。
<td style="vertical-align:top;width:259.4pt;"> With these principles in mind, this project focuses on advanced multimodal systems that interact effectively within both physical and virtual environments and facilitate effective interaction with humans. As such, we intend to engage a broad range of experts and practitioners across a wide-range of technical specialities, cultures, countries, and scholarly fields to discuss important topics, including but not limited to: &gt;&gt;Application of foundation models: the development of agents with integrated modalities (audio, image, text, sensor inputs), aiming to enhance their recognition and response capabilities for a wide variety of applications. &gt;&gt;General-purpose end-to-end systems: the development of end-to-end models that are trained with large-scale data, seeking to create versatile and adaptable AI solutions. &gt;&gt;Methodologies for grounding modalities: integrating information across various modalities, enhancing the coherence and efficacy of data processing. &gt;&gt;Intuitive human interface: the development of effective and meaningful interaction between humans and agents. &gt;&gt;Taming LLM/VLMs: exploring new approaches to address common issues in large-scale models, such as hallucinations and biases in their outputs. </td><td style="vertical-align:top;width:166.7pt;"> 考虑到这些原则，该项目专注于在物理和虚拟环境中有效交互的先进多模式系统，并促进与人类的有效交互。因此，我们打算邀请来自各种技术专业、文化、国家和学术领域的广泛专家和实践者讨论重要主题，包括但不限于: &gt;&gt;基础模型的应用:开发具有集成模式(音频、图像、文本、传感器输入)的智能体，旨在增强其对各种应用的识别和响应能力。 &gt;&gt;通用端到端系统:开发使用大规模数据训练的端到端模型，寻求创建通用和适应性强的人工智能解决方案。 &gt;&gt;接地模式的方法:整合各种模式的信息，增强数据处理的一致性和有效性。 &gt;&gt;直观的人机界面:开发人与代理之间有效而有意义的交互。 &gt;&gt;驯服LLM/ vlm:探索解决大规模模型中常见问题的新方法，例如输出中的幻觉和偏差。 </td>

&gt;&gt;Application of foundation models: the development of agents with integrated modalities (audio, image, text, sensor inputs), aiming to enhance their recognition and response capabilities for a wide variety of applications.

&gt;&gt;Methodologies for grounding modalities: integrating information across various modalities, enhancing the coherence and efficacy of data processing.

&gt;&gt;Taming LLM/VLMs: exploring new approaches to address common issues in large-scale models, such as hallucinations and biases in their outputs.

&gt;&gt;基础模型的应用:开发具有集成模式(音频、图像、文本、传感器输入)的智能体，旨在增强其对各种应用的识别和响应能力。

&gt;&gt;接地模式的方法:整合各种模式的信息，增强数据处理的一致性和有效性。

&gt;&gt;驯服LLM/ vlm:探索解决大规模模型中常见问题的新方法，例如输出中的幻觉和偏差。
<td style="vertical-align:top;width:259.4pt;"> We aspire to broaden our collective understanding of the potential and limitations of agentic AI by leveraging our unique and diverse perspectives. We strongly believe that this approach will not only enrich individual perspectives, but will also enhance the community’s collective knowledge and promote a holistic view that is more inclusive of the wide-ranging leader-board faced by multimodal AI agents. </td><td style="vertical-align:top;width:166.7pt;"> 我们渴望通过利用我们独特和多样化的观点，扩大我们对人工智能的潜力和局限性的集体理解。我们坚信，这种方法不仅可以丰富个人的观点，还可以增强社区的集体知识，并促进一个更全面的观点，更包容多模式AI代理面临的广泛的排行榜。 </td>

我们渴望通过利用我们独特和多样化的观点，扩大我们对人工智能的潜力和局限性的集体理解。我们坚信，这种方法不仅可以丰富个人的观点，还可以增强社区的集体知识，并促进一个更全面的观点，更包容多模式AI代理面临的广泛的排行榜。






