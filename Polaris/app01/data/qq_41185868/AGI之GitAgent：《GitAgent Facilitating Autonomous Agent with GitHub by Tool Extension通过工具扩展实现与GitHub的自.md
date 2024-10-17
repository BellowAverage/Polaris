
--- 
title:  AGI之GitAgent：《GitAgent: Facilitating Autonomous Agent with GitHub by Tool Extension通过工具扩展实现与GitHub的自 
tags: []
categories: [] 

---
AGI之GitAgent：《GitAgent: Facilitating Autonomous Agent with GitHub by Tool Extension通过工具扩展实现与GitHub的自主代理》翻译与解读



**目录**

































## **《GitAgent: Facilitating Autonomous Agent with GitHub by Tool Extension通过工具扩展实现与GitHub的自主代理》翻译与解读**
<td style="vertical-align:top;width:37.55pt;"> **<strong>地址**</strong> </td><td style="vertical-align:top;width:388.55pt;"> 论文地址： </td>

论文地址：
<td style="vertical-align:top;width:37.55pt;"> **<strong>时间**</strong> </td><td style="vertical-align:top;width:388.55pt;"> 2023年12月28日 </td>

2023年12月28日
<td style="vertical-align:top;width:37.55pt;"> **<strong>作者**</strong> </td><td style="vertical-align:top;width:388.55pt;"> Bohan Lyu, Xin Cong, Heyang Yu, Pan Yang, Yujia Qin, Yining Ye, Yaxi Lu, Zhong Zhang, Yukun Yan, Yankai Lin, Zhiyuan Liu, Maosong Sun 清华大学，中国人民大学 </td>

Bohan Lyu, Xin Cong, Heyang Yu, Pan Yang, Yujia Qin, Yining Ye, Yaxi Lu, Zhong Zhang, Yukun Yan, Yankai Lin, Zhiyuan Liu, Maosong Sun
<td style="vertical-align:top;width:37.55pt;"> **<strong>总结**</strong> </td><td style="vertical-align:top;width:388.55pt;"> 该论文提出了一个名为GitAgent的代理系统，可以自动从Github中扩充工具来解答用户查询。 ****<strong><em>痛点和背景****</em></strong>： &gt;&gt;现有基于语言模型的智能代理系统，尽管在自然语言处理方面表现出色，但在复杂多方位任务中效果有限。 &gt;&gt;为扩充代理的功能，研究者开发出可以与外部工具交互的代理系统，但每个系统所支持的工具范围有限，不能满足多样化的用户查询需要。 &gt;&gt;用户查询属于不同专业领域，需要具体的工具支持，而现有代理系统难以覆盖所有场景。 ****<strong><em>解决方案****</em></strong>： &gt;&gt;提出了名为GitAgent的智能代理系统。 &gt;&gt;它可以自动从GitHub搜索和集成相关仓库，并学习人类在GitHub中的经验来扩充自身的工具库。 &gt;&gt;该系统采用分阶段的工作流来完成任务：搜索、设置环境、应用、存储。 &gt;&gt;它可以搜索当前存储或者GitHub中的仓库，设置运行环境，执行任务解答查询，并保存经验以供后续使用。 &gt;&gt;在遇到问题时，它可以查询GitHub中的Issue和Pull Request，学习人类如何解决类似问题。 ****<strong><em>核心特点****</em></strong>： &gt;&gt;可以根据不同查询内容自动从GitHub中搜索和集成适当的代码仓库，扩充自身工具能力。 &gt;&gt;通过学习GitHub中的人类经验，可以更好地解决在自动扩充过程中遇到的问题。 &gt;&gt;不同阶段设计细致，操作流程清晰，能有效完成用户查询任务。 &gt;&gt;实验结果表明，在30个样本查询上平均成功率达69.4%。 ****<strong><em>优势****</em></strong>： &gt;&gt;可以根据用户个性化需求，动态扩充功能边界，不再局限于固定的工具集。 &gt;&gt;利用开源库GitHub丰富的资源，有效提升代理系统的应用能力。 &gt;&gt;通过学习人类经验破解非标化代码的集成难点，实现功能自主研发。 &gt;&gt;工作流设计合理，各阶段互相协同，提高任务完成效率及质量。 以上为该论文提出的GitAgent系统在自动扩充工具能力、学习人类经验、完成复杂查询任务等方面的主要贡献和优势。 </td>

该论文提出了一个名为GitAgent的代理系统，可以自动从Github中扩充工具来解答用户查询。

&gt;&gt;现有基于语言模型的智能代理系统，尽管在自然语言处理方面表现出色，但在复杂多方位任务中效果有限。

&gt;&gt;用户查询属于不同专业领域，需要具体的工具支持，而现有代理系统难以覆盖所有场景。

&gt;&gt;提出了名为GitAgent的智能代理系统。

&gt;&gt;该系统采用分阶段的工作流来完成任务：搜索、设置环境、应用、存储。

&gt;&gt;在遇到问题时，它可以查询GitHub中的Issue和Pull Request，学习人类如何解决类似问题。

&gt;&gt;可以根据不同查询内容自动从GitHub中搜索和集成适当的代码仓库，扩充自身工具能力。

&gt;&gt;不同阶段设计细致，操作流程清晰，能有效完成用户查询任务。

****<strong><em>优势****</em></strong>：

&gt;&gt;利用开源库GitHub丰富的资源，有效提升代理系统的应用能力。

&gt;&gt;工作流设计合理，各阶段互相协同，提高任务完成效率及质量。





## **Abstract**
<td style="vertical-align:top;width:248.05pt;"> While Large Language Models (LLMs) like ChatGPT and GPT-4 have demon-strated exceptional proficiency in natural language processing, their efficacy in ad-dressing complex, multifaceted tasks remains limited. A growing area of research focuses on LLM-based agents equipped with external tools capable of perform-ing diverse tasks. However, existing LLM-based agents only support a limited set of tools which is unable to cover a diverse range of user queries, especially for those involving expertise domains. It remains a challenge for LLM-based agents to extend their tools autonomously when confronted with various user queries. As GitHub has hosted a multitude of repositories which can be seen as a good re-source for tools, a promising solution is that LLM-based agents can autonomously integrate the repositories in GitHub according to the user queries to extend their tool set. In this paper, we introduce GitAgent, an agent capable of achieving the autonomous tool extension from GitHub. GitAgent follows a four-phase procedure to incorporate repositories and it can learn human experience by resort-ing to GitHub Issues/PRs to solve problems encountered during the procedure. Experimental evaluation involving 30 user queries demonstrates GitAgent’s ef-fectiveness, achieving a 69.4% success rate on average. </td><td style="vertical-align:top;width:178.05pt;"> 尽管像ChatGPT和GPT-4这样的大型语言模型在自然语言处理方面表现出色，但它们在解决复杂、多层面任务方面的效果仍然有限。越来越多的研究领域集中在基于LLM的代理上，这些代理配备了能够执行各种任务的外部工具。然而，现有的基于LLM的代理只支持有限的一组工具，这些工具无法覆盖各种各样的用户查询，特别是那些涉及专业领域的查询。当面对各种用户查询时，基于LLM的代理自主扩展其工具仍然是一个挑战。由于GitHub托管了大量的存储库，这些存储库可以被视为工具的良好资源，一个有前途的解决方案是基于LLM的代理可以根据用户查询自主地集成GitHub中的存储库，以扩展他们的工具集。 在本文中，我们介绍了GitAgent，一个能够从GitHub实现自治工具扩展的代理。GitAgent遵循一个四阶段的过程来合并存储库，并且可以通过利用GitHub的问题/拉取请求来学习人类经验，以解决在过程中遇到的问题。涉及30个用户查询的实验评估展示了GitAgent的有效性，平均成功率为69.4%。 </td>

尽管像ChatGPT和GPT-4这样的大型语言模型在自然语言处理方面表现出色，但它们在解决复杂、多层面任务方面的效果仍然有限。越来越多的研究领域集中在基于LLM的代理上，这些代理配备了能够执行各种任务的外部工具。然而，现有的基于LLM的代理只支持有限的一组工具，这些工具无法覆盖各种各样的用户查询，特别是那些涉及专业领域的查询。当面对各种用户查询时，基于LLM的代理自主扩展其工具仍然是一个挑战。由于GitHub托管了大量的存储库，这些存储库可以被视为工具的良好资源，一个有前途的解决方案是基于LLM的代理可以根据用户查询自主地集成GitHub中的存储库，以扩展他们的工具集。



### **<strong><strong>Figure 1: Illustration of autonomous tool extension from GitHub图1：来自GitHub的自主工具扩展的示意图**</strong></strong>

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/direct/613d788015f04d26bee89d127385b8db.png" width="1200">





## **1 INTRODUCTION****引言**
<td style="vertical-align:top;width:249.55pt;"> Significant advancements in Large Language Models (LLMs) (OpenAI, 2022; 2023) have show-cased remarkable proficiency in natural language processing (NLP). Recently, a notable trend emerged to develop LLMs equipped with external tools (e.g., search engines (Nakano et al., 2021; Qin et al., 2023a), calculators (Schick et al., 2023), and knowledge bases (Parisi et al., 2022)) to function as agents capable of performing complex tasks, extending the capability boundary of LLMs beyond NLP tasks. Consequently, a variety of LLM-based agents have surfaced, e.g., ChatGPT Plu-gins (OpenAI), AutoGPT (AutoGPT), AutoGen (Wu et al., 2023b), XAgent (XAgent, 2023). However, the range of tools that existing LLM-based agents can utilize remains notably lim-ited (Parisi et al., 2022; Schick et al., 2023; Patil et al., 2023). It is particularly evident in real-world scenarios where user queries are highly diverse and often necessitate specific, domain-specialized tools. Even agents with a broad range of tools still struggle to cover all proper tools to address these specialized queries (Qin et al., 2023c). Hence, when confronted with various queries, it is necessary for agents to autonomously extend their supported toolset to meet the user demands. We observe that there already exist numerous repositories in host platforms like GitHub which is a good tool resource especially including many professional tools across diverse domains (e.g., Qlib for the quantitative investment, AiZynthFinder for the molecule retrosynthetic planning, etc.). If LLM-based agents could search and deploy relevant repositories from GitHub, thereby extending their tools on their own, they can autonomously extend their capability boundary to address diverse user queries. </td><td style="vertical-align:top;width:176.55pt;"> 大型语言模型（LLMs）的显著进展（OpenAI，2022；2023）展示了在自然语言处理（NLP）方面卓越的能力。最近，出现了一个显著趋势，即开发配备外部工具的LLMs（例如搜索引擎（Nakano等，2021；Qin等，2023a）、计算器（Schick等，2023）和知识库（Parisi等，2022）），以充当能够执行复杂任务的代理，将LLMs的能力边界扩展到NLP任务之外。因此，出现出了各种基于LLM的代理，例如****<strong><em>ChatGPT****</em></strong>插件（OpenAI）、****<strong><em>AutoGPT****</em></strong>（AutoGPT）、****<strong><em>AutoGen****</em></strong>（Wu等，2023b）、****<strong><em>XAgent****</em></strong>（XAgent，2023）。  然而，现有基于LLM的代理可以利用的工具范围仍然显著有限（Parisi等，2022；Schick等，2023；Patil等，2023）。在用户查询高度多样化并且经常需要特定的、领域专用的工具的实际场景中，这一点尤为明显。即使具有广泛工具范围的代理仍然难以涵盖所有适用于这些专业查询的正确工具（Qin等，2023c）。因此，当面临各种查询时，代理需要自主扩展其支持的工具集，以满足用户需求。我们注意到，像GitHub这样的托管平台已经存在大量存储库，这是一个很好的工具资源，特别是包括许多跨不同领域的专业工具(例如，用于定量投资的Qlib，用于分子逆转录计划的AiZynthFinder等)。如果基于LLM的代理能够从GitHub搜索和部署相关存储库，从而自主扩展其工具，它们就可以自主扩展其能力边界以解决多样化的用户查询。  </td>

However, the range of tools that existing LLM-based agents can utilize remains notably lim-ited (Parisi et al., 2022; Schick et al., 2023; Patil et al., 2023). It is particularly evident in real-world scenarios where user queries are highly diverse and often necessitate specific, domain-specialized tools. Even agents with a broad range of tools still struggle to cover all proper tools to address these specialized queries (Qin et al., 2023c). Hence, when confronted with various queries, it is necessary for agents to autonomously extend their supported toolset to meet the user demands. We observe that there already exist numerous repositories in host platforms like GitHub which is a good tool resource especially including many professional tools across diverse domains (e.g., Qlib for the quantitative investment, AiZynthFinder for the molecule retrosynthetic planning, etc.). If LLM-based agents could search and deploy relevant repositories from GitHub, thereby extending their tools on their own, they can autonomously extend their capability boundary to address diverse user queries.




<td style="vertical-align:top;width:249.55pt;"> Tool extension based on GitHub has some challenge due to the lack of standardization of available repositories. (1) Presence of Flaws: Repositories on GitHub cannot guarantee absolute perfection, devoid of any flaws. Even for those developed by notable organizations (e.g., Microsoft), they may still suffer from inadequate maintenance, resulting in the presence of potential bugs in their source codes. (2) Incomplete Documentation. Documentations (e.g., README), serving as the pri-mary guide, may not comprehensively detail all the necessary information for effective utilization. Especially, developers might not invest the required effort to create detailed, user-friendly documen-tation. Hence, agents will struggle to integrate repositories and further utilize them to accomplish user queries. </td><td style="vertical-align:top;width:176.55pt;"> 基于GitHub的工具扩展面临一些挑战，主要是由于可用存储库的标准化不足。具体来说，存在以下问题： **<strong>&gt;&gt; **</strong>**<strong>缺陷的存在**</strong>：GitHub上的存储库不能保证绝对完美，没有任何缺陷。即使是由知名组织（例如Microsoft）开发的存储库，它们可能仍然存在不足的维护，导致其源代码中可能存在潜在错误。 **<strong>&gt;&gt; **</strong>**<strong>不完整的文档**</strong>：文档（例如README），作为主要指南，可能无法全面详细地描述有效利用所需信息的所有必要信息。尤其是，开发人员可能不会投入必要的精力来创建详细的、用户友好的文档。因此，代理将努力集成存储库并进一步利用它们来完成用户查询。 </td>

(1) Presence of Flaws: Repositories on GitHub cannot guarantee absolute perfection, devoid of any flaws. Even for those developed by notable organizations (e.g., Microsoft), they may still suffer from inadequate maintenance, resulting in the presence of potential bugs in their source codes.

基于GitHub的工具扩展面临一些挑战，主要是由于可用存储库的标准化不足。具体来说，存在以下问题：

**<strong>&gt;&gt; **</strong>**<strong>不完整的文档**</strong>：文档（例如README），作为主要指南，可能无法全面详细地描述有效利用所需信息的所有必要信息。尤其是，开发人员可能不会投入必要的精力来创建详细的、用户友好的文档。因此，代理将努力集成存储库并进一步利用它们来完成用户查询。
<td style="vertical-align:top;width:249.55pt;"> In this paper, we introduce GitAgent, an Autonomous Agent enabled to Extend Tools from GitHub. GitAgent decomposes the tool extension procedure into four phases: Search, Setup, Apply, and Store. It begins by searching suitable repositories from GitHub according to user queries and then configuring its environment. Subsequently, GitAgent utilizes the configured repository to fulfill the user query and ends by storing the repository for efficient handling of subsequent queries. To address the non-standardization challenge, as GitHub provides Issues and Pull Requests (PRs) which contains human practice experience, GitAgent can resort to Issues and PRs to learn how human practitioners solve problems (e.g., bugs) during the tool extension. Specifically, upon en-countering a problem, GitAgent first summarizes the problem as a query and utilizes GitHub Issues/PRs API to search for pertinent Issues/PRs. It then judges the relevance of these Issues/PRs to determine their relevance and applicability to the current problem sequentially. If identifying a suitable one, it reads the contents of Issues/PRs to learn how to solve the problem. Finally, GITA-GENT summarizes the practical experience gained during the procedure to guide future use. We validate the effectiveness of our proposed GitAgent by conducting experiments involving 30 user queries. Our results demonstrate that, GitAgent achieves a success rate of 69.4% on average in addressing the user queries. Furthermore, we discuss the reasons behind failures, shedding light on potential future research directions. </td><td style="vertical-align:top;width:176.55pt;"> 在本文中，我们介绍了**<strong>GitAgent**</strong>，一种能够从GitHub扩展工具的自主代理。GitAgent将工具扩展过程分解为四个阶段：**<strong>搜索**</strong>、**<strong>设置**</strong>、**<strong>应用**</strong>和**<strong>存储**</strong>。它首先根据用户查询从GitHub搜索合适的存储库，然后配置其环境。随后，GitAgent利用配置的存储库来满足用户查询，并以存储存储库的方式结束，以有效处理后续查询。 为了解决标准化挑战，由于GitHub提供包含人类实践经验的问题和拉取请求，GitAgent可以利用这些问题和拉取请求来学习人类从事工具扩展过程中如何解决问题。 具体而言，遇到问题时，GitAgent首先将问题总结为一个查询，并利用GitHub的问题/拉取请求API搜索相关的问题/拉取请求。然后，它按顺序判断这些问题/拉取请求的相关性和适用性。如果找到合适的问题/拉取请求，它将阅读问题/拉取请求的内容以了解如何解决问题。最后，GitAgent总结在过程中获得的实际经验，以指导未来的使用。  我们通过进行涉及30个用户查询的实验证实了我们提出的GitAgent的有效性。我们的结果表明，GitAgent在解决用户查询方面平均成功率为69.4%。此外，我们讨论了失败背后的原因，为潜在的未来研究方向提供了启示。 </td>

We validate the effectiveness of our proposed GitAgent by conducting experiments involving 30 user queries. Our results demonstrate that, GitAgent achieves a success rate of 69.4% on average in addressing the user queries. Furthermore, we discuss the reasons behind failures, shedding light on potential future research directions.

为了解决标准化挑战，由于GitHub提供包含人类实践经验的问题和拉取请求，GitAgent可以利用这些问题和拉取请求来学习人类从事工具扩展过程中如何解决问题。


<td style="vertical-align:top;width:249.55pt;"> In summary, our main contributions are as follows: &gt;&gt; We propose GitAgent, an autonomous LLM-based agent. It can autonomously integrate repos-itories in GitHub to extend tools to meet the diverse demands of user queries. &gt;&gt; To address the non-standardization challenge, GitAgent can autonomously learn human expe-rience based on the GitHub Issues/PRs to solve problems during the tool extension procedure. &gt;&gt; Experimental results showcase the effectiveness of GitAgent in autonomously integrating tools for task accomplishment across expertise domains. </td><td style="vertical-align:top;width:176.55pt;"> 总之，我们的主要贡献如下： &gt;&gt; 我们提出了GitAgent，一个基于LLM的自主代理。它可以自主整合GitHub中的存储库，以满足多样化的用户查询需求。 &gt;&gt; 为了解决标准化挑战，GitAgent可以根据GitHub的问题/拉取请求自主学习人类经验，以解决工具扩展过程中的问题。 &gt;&gt; 实验结果展示了GitAgent在自主整合跨专业领域任务的工具方面的有效性。 </td>

&gt;&gt; We propose GitAgent, an autonomous LLM-based agent. It can autonomously integrate repos-itories in GitHub to extend tools to meet the diverse demands of user queries.

&gt;&gt; Experimental results showcase the effectiveness of GitAgent in autonomously integrating tools for task accomplishment across expertise domains.

&gt;&gt; 我们提出了GitAgent，一个基于LLM的自主代理。它可以自主整合GitHub中的存储库，以满足多样化的用户查询需求。

&gt;&gt; 实验结果展示了GitAgent在自主整合跨专业领域任务的工具方面的有效性。



### **<strong><strong>Figure 2: Illustration of the four-phase procedure of the **</strong>**<strong>GitAgent**</strong>**<strong>.图2：**</strong>**<strong>GitAgent**</strong>**<strong>的四阶段程序示意图**</strong></strong>

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/direct/4b1e30efaf684bbc8fc07f0ec5eb2d26.png" width="1200">

## **2 METHODOLOGY****方法论**

### **<strong><strong>2.1 TASK FORMULATION**</strong>**<strong>任务制定**</strong></strong>
<td style="vertical-align:top;width:255.55pt;"> Given the user query Q, the agent aims to accomplish it and give the response R to the user, involving autonomously tool extension from external resources (i.e., GitHub). </td><td style="vertical-align:top;width:170.55pt;"> 给定用户查询Q，代理旨在完成它并向用户提供响应R，涉及从外部资源（即GitHub）自主进行工具扩展。 </td>

给定用户查询Q，代理旨在完成它并向用户提供响应R，涉及从外部资源（即GitHub）自主进行工具扩展。









## **5 CONCLUSION结论**
<td style="vertical-align:top;width:255.55pt;"> In this paper, we present GitAgent, an autonomous agent that can integrate GitHub repositories to proficiently address various user queries. Through a meticulously designed four-phase proce-dure and the implementation of learning human experience from GitHub Issues/PRs, GitAgent demonstrates its effectiveness in navigating the challenges posed by non-standardized repositories. The experimental results validate GitAgent’s ability to achieve high success rates in addressing user queries. However, while GitAgent showcases promising outcomes, challenges such as vary-ing repository quality and unexpected issues during integration persist. This work prompts future research avenues, including refining GitAgent to adapt to repository variations, enhancing error handling mechanisms, and exploring methodologies for broader repository utilization. </td><td style="vertical-align:top;width:170.55pt;"> 在本文中，我们介绍了GitAgent，一种能够整合GitHub存储库以有效解决各种用户查询的自主代理。通过精心设计的四阶段程序和从GitHub问题/拉取请求中学习人类经验的实现，GitAgent展示了其在应对**<strong>非标准化存储库**</strong>引发的挑战方面的有效性。实验结果验证了GitAgent在解决用户查询方面取得高成功率的能力。然而，尽管GitAgent展示了有前途的结果，但仍存在存储库质量的差异和整合过程中的意外问题等挑战。这项工作提出了未来研究的方向，包括改进GitAgent以适应存储库的变化，增强错误处理机制，并探索更广泛存储库利用的方法。 </td>

在本文中，我们介绍了GitAgent，一种能够整合GitHub存储库以有效解决各种用户查询的自主代理。通过精心设计的四阶段程序和从GitHub问题/拉取请求中学习人类经验的实现，GitAgent展示了其在应对**<strong>非标准化存储库**</strong>引发的挑战方面的有效性。实验结果验证了GitAgent在解决用户查询方面取得高成功率的能力。然而，尽管GitAgent展示了有前途的结果，但仍存在存储库质量的差异和整合过程中的意外问题等挑战。这项工作提出了未来研究的方向，包括改进GitAgent以适应存储库的变化，增强错误处理机制，并探索更广泛存储库利用的方法。







## **A PROMPTS附录A**

### **<strong><strong>Figure 12: Prompt of GitAgent图12：GitAgent的提示**</strong></strong>
<td style="vertical-align:top;width:255.55pt;"> GitAgent You are a professional programmer. Given a query, your task is to search for a githubrepository and use it to solve the query. If the result of `apply` function is lack of required information, you can call `apply` again if you think the result is close to what you want and you think this repository can be used to solve your query. You can also call `set_repository` function to find another repository if you think this repository is not suitable for your query. </td><td style="vertical-align:top;width:170.55pt;"> GitAgent 您是一名专业程序员。给定一个查询，您的任务是搜索一个GitHub存储库并使用它来解决查询。 如果apply函数的结果缺乏所需的信息，如果您认为结果接近您想要的并且认为此存储库可用于解决您的查询，可以再次调用apply。如果您认为此存储库不适合您的查询，您还可以调用set_repository函数查找另一个存储库。 </td>

You are a professional programmer. Given a query, your task is to search for a githubrepository and use it to solve the query.

GitAgent

如果apply函数的结果缺乏所需的信息，如果您认为结果接近您想要的并且认为此存储库可用于解决您的查询，可以再次调用apply。如果您认为此存储库不适合您的查询，您还可以调用set_repository函数查找另一个存储库。





### **<strong><strong>Figure 13: Prompt of Stored Repository Retrieval图13：存储库检索提示**</strong></strong>
<td style="vertical-align:top;width:255.55pt;"> Stored Repository Retrieval You are a professional programmer. Given a task, you want to find a githubrepository to solve the task. Now, your colleagues have explored some repositories. If you think any of the repository(s) might can solve your task, call `use_existing_repository` function to use it. Otherwise, call `find_a_new_repository` function to find another repository. You will be given the query of the task and name(s) and description(s) of existed repositories. </td><td style="vertical-align:top;width:170.55pt;"> Stored Repository Retrieval 您是一名专业程序员。给定一个任务，您希望找到一个GitHub存储库来解决该任务。现在，您的同事已经探索了一些存储库。如果您认为任何存储库可能可以解决您的任务，请调用use_existing_repository函数使用它。否则，调用find_a_new_repository函数查找另一个存储库。 您将获得任务的查询以及已存在存储库的名称和描述。 </td>

You are a professional programmer. Given a task, you want to find a githubrepository to solve the task. Now, your colleagues have explored some repositories. If you think any of the repository(s) might can solve your task, call

You will be given the query of the task and name(s) and description(s) of existed repositories.

您是一名专业程序员。给定一个任务，您希望找到一个GitHub存储库来解决该任务。现在，您的同事已经探索了一些存储库。如果您认为任何存储库可能可以解决您的任务，请调用use_existing_repository函数使用它。否则，调用find_a_new_repository函数查找另一个存储库。



### **<strong><strong>Figure 14: Prompt of Repository Topic Generation图14：存储库主题生成提示**</strong></strong>
<td style="vertical-align:top;width:255.55pt;"> Repository Topic Generation You are a professional programmer. Given a query, you want to find a githubrepository to solve this query. Firstly you need to search for the needed repository by their topics, which should be relevant to the query. The topic name should be a noun. IF it contains many words, the words should be connected by '-'. </td><td style="vertical-align:top;width:170.55pt;"> Repository Topic Generation 您是一名专业程序员。给定一个查询，您希望找到一个GitHub存储库来解决此查询。首先，您需要通过其主题搜索所需的存储库，该主题应与查询相关。 主题名称应该是一个名词。如果它包含许多单词，这些单词应通过“-”连接。 </td>

You are a professional programmer. Given a query, you want to find a githubrepository to solve this query. Firstly you need to search for the needed repository by their topics, which should be relevant to the query.

Repository Topic Generation

主题名称应该是一个名词。如果它包含许多单词，这些单词应通过“-”连接。








