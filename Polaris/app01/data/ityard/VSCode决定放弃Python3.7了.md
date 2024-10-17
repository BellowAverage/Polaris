
--- 
title:  VSCode决定放弃Python3.7了 
tags: []
categories: [] 

---
  来源丨51CTO技术栈（ID：blog51cto）

停止使用 Python3.7 吧，虽然不太影响，但风险自担。因为即便是巨头微软，也决定要逐步放弃对 Python3.X 的官方支持。

就在10月，微软新发布的Visual Studio Code 扩展中，已经废弃了对Python3.7 的支持。

 

<img width="1160" src="https://img-blog.csdnimg.cn/img_convert/51a33ff88f54bfbcb24972137e434a20.png" alt="51a33ff88f54bfbcb24972137e434a20.png">

这就意味着，VS Code 对于 Python3.7 彻底放弃了正式支持。值得一提的是早在2022年底，VS Code 的Python插件已经停止了对 Python3.6 的支持（之前停止支持的还有 Python2.7/3.5）。 

**0****1**

### 

**微软VS Code为何放手Python3.X?**

Visual Studio Code 扩展此举对于 Python 3.X 的全线停止官方支持，乍看之下，着实令人吃惊。

Python 3.7 的受欢迎程度还相当巨大。根据三方数据统计，在使用 Python 3.X 的网站当中，许有 17.2% 使用 Python 3.7。而已经于 2021 年终止生命周期的 Python 3.6 仍然是最受欢迎的，占 28.9%。Python 3.8 位于两者之间，占 23.3%。

<img width="647" src="https://img-blog.csdnimg.cn/img_convert/8b3a4339a28d44cd285a3420c555cd0d.png" alt="8b3a4339a28d44cd285a3420c555cd0d.png">

首先，微软是出于安全的考虑。Python 3.7 发布于2018年6月，寿命已经于今年6月迎来了终结。正如你在 PEP 537 中所见：“Python 3.7 发布后 5 年将停止发布。”也就是说， 从 2023 年 7 月开始，如果存在安全漏洞，Python 开发团队将不再修复。

同时，事实上许多软件中的依赖项也宣布放弃对Python3.7的支持，比如第三方 Python 库和框架：Numpy、Pandas、Django4 等。这意味着如果这些库有一个严重的错误，修复程序可能无法在 Python 3.7 上使用。

此外，新的Python版本正在陆续赶上。目前 Python 已转向每年一个大版本的生命周期。Python 3.8 将于 2024 年 10 月终止生命周期，这意味着 Microsoft Visual Studio Code 扩展的官方支持将于 2025 年首次发布时结束，依此类推。

据 Microsoft 称，Visual Studio 的 Python 扩展适用于所有积极支持的 Python 版本。3.12 是最新版本。

去年年底，Python指导委员会宣布了“将采用12个月发布周期，一年发布一个大版本”的决定。Python 语言项目团队对于新的版本开发周期规划已成定局：
- 在一年周期开始前的 5 个月时间里（跟上一个周期的末尾重合，因为每个周期的末尾基本上是修复 bug，时间比较充裕），各个开发者自由开发讨论，提交特性，但不合并到开发分支。- 一年开发周期的前 7 个月，确定 feature 并完成 Alpha 版本。- 然后花费 4 个月的时间用于修复 bug，以完成 Beta 版本。- 最后 1 个月收尾，最终发布正式版。- 正式版发布之后，一年之内会获得完整支持，5 年之内会有安全更新。
**02**

**微软还留了后手**

当然，考虑到它的受欢迎程度，微软声称没有故意从 Visual Studio Code 扩展中彻底剥离该代码的计划，并表示：“该扩展在可预见的未来将继续与 Python 3.7 非正式地配合使用。”但是，如果没有官方支持，就无法保证不会出现问题。

除了废止对 Python 3.7 的官方支持外，微软还推出了调试器扩展的更新（现已重命名为“Python 调试器”），其中包含一个设置，允许用户仅单步执行自己的代码或跳入系统或第三方代码。派对库代码，无需微调 launch.json 设置。

其他改进包括 Pylint 扩展的 Lint on Change 选项，允许在用户键入时显示错误和警告，以及围绕 Mypy 类型检查器的新设置，以允许用户指定报告范围以及是否使用 mypy 的守护进程。

**03**

### 

**Python，公认最流行的语言**

Python 长期以来一直是开发人员流行的语言。TIOBE 将其列为 2023 年 10 月语言列表的首位，领先于 C 和 C++，而 Stack Overflow 开发者调查将该语言排在第三位，仅次于 HTML 和 JavaScript，但高于 SQL。

<img width="781" src="https://img-blog.csdnimg.cn/img_convert/28dddea5ab6a99564bcfd34ddc0bbdf1.png" alt="28dddea5ab6a99564bcfd34ddc0bbdf1.png">

Stack Overflow 在其 2023 年调查中指出，对于非专业开发人员或正在学习编码的受访者来说，Python 排名第一。

### 

**04**

**写在最后：又该换Python版本了**

近日，根据 Python 软件基金会和 JetBrains 公布的 2022 年度开发者调查数据显示，93% 的开发者使用 Python 3，7% 的 Python 开发者仍在使用 Python 2（Python 2 已经在 2020 年结束了支持），2017 年是 75% 和 25%。

而且此次调查中还显示了出 Python 开发者对于新版本的拥抱程度非常喜人——Python 3 开发者中有 45% 使用两年前发布的 Python 3.10，2% 使用 Python 3.5 或更低版本。

调查还发现，21% 的开发者表示只在工作中使用Python，51% 将 Python 用于工作和个人/教育用途或业余项目，21% 只在个人项目中使用Python。5% 的受访者表示 Python 是他们的主要语言。

所以，说Python是一门“飞速生长”的语言，当之无愧。多说一句，Python 3.13 明年就会发布了，还在用老版本 Python 的朋友，赶紧做好准备，迎接新版本吧！ 










