
--- 
title:  Jupyter和Chatgpt合体了 
tags: []
categories: [] 

---
来源丨机器之心

相信很多小伙伴是Jupyter的重度使用者，本篇介绍一个利器 **Chapyter** 它将目前火爆的 ChatGPT 代码解释器与 Jupyter Notebook 结合了起来，让编码更加地高效。

毋庸置疑，在 AI 的帮助下，开发者的编码效率能够大大提升。

开发者们将从简单、重复的编码工作中解脱出来。但是随之而来的诸多问题，往往让使用 AI 的开发者们头秃不已。

Chapyter 将 GPT-4 这样强大的代码生成模型合并到 Jupyter Notebook 编码环境中，开辟了人类 - AI 协作的新模式，在极大程度上解决了大部分编程助手会出现的问题。

**Chapyter 是一个 JupyterLab 扩展，将 GPT-4 无缝连接到你的编码环境，并且具有一个代码解释器，可以将自然语言描述翻译为 Python 代码并自动执行。**并且 Chapyter 通过在你最熟悉的 IDE 中启用「自然语言编程」，提高你的工作效率，并使你能够探索更多未尝试过的新想法。

<img src="https://img-blog.csdnimg.cn/img_convert/31d328bd87278aeadb6bb1cb3a9cbc63.png" alt="31d328bd87278aeadb6bb1cb3a9cbc63.png">

项目链接：https://github.com/chapyter/chapyter

下图为 Chapyter 与部分现有的编码助手的差别。

可以发现，Chapyter 将编码助手的优势综合了起来。它可以帮助开发者完成各种复杂的编码任务、自动执行 AI 生成的代码，还能够让开发者进行原位调试、自定义 Prompt，甚至保护了开发者与代码的隐私性，避免数据被利用。

<img src="https://img-blog.csdnimg.cn/img_convert/a86a71eb4962f20c8f9e02c8f596aeeb.png" alt="a86a71eb4962f20c8f9e02c8f596aeeb.png">

### Chapyter 的特点与优势****

Chapyter 的主要特点有：

**1. 从自然语言生成代码并自动执行**

只需在任务自然语言描述的单元格开头添加命令「%% chat」，代码就会生成，并且用时极短，只需要几秒钟。

<img src="https://img-blog.csdnimg.cn/img_convert/3802900d4ba14f2c612ba8edfcf2ee1e.gif" alt="3802900d4ba14f2c612ba8edfcf2ee1e.gif">

别小瞧了 Chapyter 的这个优势。

自动补全一直是许多 AI 辅助编码工具的主流交互，在编码环境中提供 AI 支持，并且可以显著提高开发人员工作的生产力和满意度。然而，自动补全并不完美：穿插 AI 代码建议可能会分散注意力；生成的代码可能包含可能很难调试的隐藏错误；并且生成的代码通常只跨越几行，很难在上下文之外生成新的功能。

Chapyter 通过提供单元级代码生成和自动执行克服了这些问题。你只需键入要执行的操作的自然语言描述，Chapyter 将调用 GPT-X 模型来生成代码并为你执行。这与 Copilot 等系统中的代码补全非常不同：其旨在支持仅跨越几行代码并且与当前工作非常相关的微任务，例如，完成函数调用。而 Chapyter 旨在接管完整的任务，有时可能与现有代码不同。

默认情况下，生成的代码是隐藏的，因为 Chapyter 希望淡化 AI 生成的代码并专注于结果。并且，关于自动执行你也无需担心，因为 Chapyter 有一个安全模式来防止自动执行可能危险的代码。

**2. 使用编码历史和执行输出来生成代码**

Chapyter 还可以利用你的代码历史记录和执行输出来提供上下文感知建议。它还可以选择加载文件，以便为进一步处理和分析提供建议。

如下图所示，通过在代码生成中添加 --history 或 -h 标志，Chapyter 可以使用之前的执行历史和输出，为加载的 IRIS 数据集生成相应的可视化代码。

<img src="https://img-blog.csdnimg.cn/img_convert/5ce9e8e3b263ebca8ab04feb698c0f16.gif" alt="5ce9e8e3b263ebca8ab04feb698c0f16.gif">

**3. 原位调试、编辑代码**

生成的代码可能并不完美，可能包含 bug 或错误。由于 Chapter 已完全集成到 Jupyter Notebook 中，因此无需离开 IDE，你就可以轻松地检查代码并修复任何错误或 bug (例如，在这种情况下安装缺少的依赖项)。

<img src="https://img-blog.csdnimg.cn/img_convert/ea69e729b1ba9881f7d0d938709a9ee0.gif" alt="ea69e729b1ba9881f7d0d938709a9ee0.gif">

**4.prompt 和 AI 配置透明化，并允许自定义**

Chapyter 发布了库中使用的所有 prompt，并致力于让自定义所使用的 prompt 和设置更加便捷。

可查阅：https://github.com/chapyter/chapyter/blob/main/chapyter/programs.py

**5. 使用 AI 时，隐私优先 **

Chapyter 是一个极小的 Python 包，可以在本地安装并与 JupyterLab 无缝使用。它使用 OpenAI API 调用 GPT-X 模型，默认情况下不会保留交互数据和代码进行训练。

因此与 Copilot 或 ChatGPT 缓存你的数据并用来训练和分析不同，Chapyter 所有发送到 OpenAI 的数据将不会被保存用于训练（可参阅 OpenAI API 数据使用策略）。

Chapyter 的构成

Chapyter 主要由两个部分组成：
- 实现 ipython magic 命令，用来处理提示和调用 GPT-X 模型；- 另一个是监听 Chapyter 单元格执行情况的前端，它会自动执行新生成的单元格并更新单元格的样式。
下图展示了执行 Chapyter 单元格后前端和 ipython 内核的编排。

<img src="https://img-blog.csdnimg.cn/img_convert/4d6d25bc506cbf7f285c7271884bd2b6.png" alt="4d6d25bc506cbf7f285c7271884bd2b6.png">










