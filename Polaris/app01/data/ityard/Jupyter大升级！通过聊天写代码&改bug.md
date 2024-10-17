
--- 
title:  Jupyter大升级！通过聊天写代码&改bug 
tags: []
categories: [] 

---
来源丨机器之心

Jupyter 在其环境中添加了基于 LLM 的聊天机器人。

现在，大语言模型（LLM）与 Jupyter 连接起来了！

这主要归功于一个名叫 **Jupyter AI**** **的项目，它是官方支持的 Project Jupyter 子项目。目前该项目已经完全开源，其连接的模型主要来自 AI21、Anthropic、AWS、Cohere、OpenAI 等各大明星公司和机构。

<img src="https://img-blog.csdnimg.cn/img_convert/9aeb7a13176ef42ed3a4c43cb65b5d70.png" alt="9aeb7a13176ef42ed3a4c43cb65b5d70.png">

项目地址：https://github.com/jupyterlab/jupyter-ai

有了大模型的加持，Jupyter 功能也发生了很大的变化。现在你可以在该环境中生成代码、总结文档、创建注释、修复错误等。你甚至可以使用文本 prompt 生成 notebooks。

Jupyter AI 的安装过程也非常简单，安装代码如下：

```
pip install 'jupyter-ai&gt;=1.0,&lt;2.0' # If you use JupyterLab 3pip install jupyter-ai # If you use JupyterLab 4
```

此外，Jupyter AI 提供了两种不同的界面与 LLM 交互。在 JupyterLab 中，你可以使用聊天界面与 LLM 进行对话，以帮助处理代码。此外，在任何支持 notebook 或 IPython 的环境中，包括 JupyterLab、Notebook、IPython、Colab 和 Visual Studio Code，你可以使用 %% ai 魔术命令调用 LLM。

<img src="https://img-blog.csdnimg.cn/img_convert/37244690301f87b6672567c49accc0ca.png" alt="37244690301f87b6672567c49accc0ca.png">

### 大模型加持下的 Jupyter

接下来我们看看效果如何。

**编程助手**

Jupyter 聊天界面如下图所示，用户可以与 Jupyternaut（编程助手）进行对话。在 Jupyternaut 功能栏我们可以看到这样一句话「大家好，我是 Jupyternaut，你的编程助理。你可以使用文本框向我提问，也可以使用命令向我提问。」

<img src="https://img-blog.csdnimg.cn/img_convert/9063a494199b2220e8af1750167dc72f.png" alt="9063a494199b2220e8af1750167dc72f.png">

接下来，用户向 Jupyternaut 询问了一个问题：如「在 Python 中，元组和列表有什么区别？」Jupyternaut 给出了这两者的关键区别，并且回答的非常正确，最后还贴心的举了示例：

<img src="https://img-blog.csdnimg.cn/img_convert/17e8786a0cfcea2f7b772bae2072b862.png" alt="17e8786a0cfcea2f7b772bae2072b862.png">

假如有一部分代码你不是很了解，你可以选中这部分代码，并将其当做 prompt，然后要求 Jupyternaut 解释这段代码，除此之外，Jupyternaut 还能对代码进行修改、识别代码错误等。

<img src="https://img-blog.csdnimg.cn/img_convert/043073d7eb9245b410e20c9b228f2f5c.png" alt="043073d7eb9245b410e20c9b228f2f5c.png">

如果你对代码不满意，还可以让 Jupyternaut 按照要求重写代码：

<img src="https://img-blog.csdnimg.cn/img_convert/221b9e2c6c889c5b3beac0e4ebdada68.png" alt="221b9e2c6c889c5b3beac0e4ebdada68.png">

重写代码后，Jupyternaut 会将代码重新发送回用户选择的语言模型进行替换：

<img src="https://img-blog.csdnimg.cn/img_convert/0909a6e0f4ef51002a6a28ee51758d65.png" alt="0909a6e0f4ef51002a6a28ee51758d65.png">

**从文本 prompt 生成 notebook**

Jupyter AI 的聊天界面可以根据文本 prompt 生成一个完整的 notebook。想要实现这一点，用户需要运行「/generate」命令，外加一个文本描述。

<img src="https://img-blog.csdnimg.cn/img_convert/a0085c10c35d2b3a76bfd4ce06cb3112.png" alt="a0085c10c35d2b3a76bfd4ce06cb3112.png">

Jupyternaut 生成 notebook 后，会向用户发送一个包含文件名的消息，用户可以打开该文件进行查看：

<img src="https://img-blog.csdnimg.cn/img_convert/525f672b365a577b1bd963c8b81cb0a9.png" alt="525f672b365a577b1bd963c8b81cb0a9.png">

**访问本地文件**

你可以使用「/learn」命令让 Jupyternaut 学习本地文件，随后使用「/ask」命令询问有关本地文件的问题。举例来说，使用「/learn」命令，你可以让 Jupyternaut 学习关于 Jupyter AI 文档的知识：

<img src="https://img-blog.csdnimg.cn/img_convert/f81fa74d065dfdef36fbebdd6d672eb5.png" alt="f81fa74d065dfdef36fbebdd6d672eb5.png">

一旦 Jupyternaut 学习完成，你就可以使用「/ask」命令提出问题：

<img src="https://img-blog.csdnimg.cn/img_convert/3cb7717b2edd46773255ccfc10ac07a4.png" alt="3cb7717b2edd46773255ccfc10ac07a4.png">

**魔法功能**

Jupyter AI 还提供了可以在 notebook cells 和 IPython 命令行界面中运行的 %% ai 命令，每个 %% ai 命令都需要一个模型，通常指定为 provider‑id:model‑id：

<img src="https://img-blog.csdnimg.cn/img_convert/d61a206892d3b36862284e1c014d13dc.png" alt="d61a206892d3b36862284e1c014d13dc.png">

还有研究者体验了一下 %% ai 魔法命令，让其调用 ChatGPT ：

<img src="https://img-blog.csdnimg.cn/img_convert/5647c797dc38c0262efda7ffbbccd518.png" alt="5647c797dc38c0262efda7ffbbccd518.png">

此外，你还可以使用 - f 或 --format 参数自定义输出的格式，包括 HTML、数学、源代码和图像，这对于研究人员和教育工作者来说非常有用。

<img src="https://img-blog.csdnimg.cn/img_convert/4a54f5480f56201fb9d88e5c64d3ebcb.png" alt="4a54f5480f56201fb9d88e5c64d3ebcb.png">

一番展示下来，有了大模型加持的 Jupyter 确实方便了很多。想要尝试的小伙伴，可以前去一试了。

**参考链接：https://blog.jupyter.org/generative-ai-in-jupyter-3f7174824862**
- - - - - 