
--- 
title:  DevChat：VSCode中基于大模型的AI智能编程助手 
tags: []
categories: [] 

---
#AI编程助手哪家好？DevChat“真”好用# 

#### 文章目录
- - - <ul><li>- - - - - 


## 1. 前言

  DevChat是由Merico公司精心打造的AI智能编程助手。它利用了最先进的大语言模型技术，像人类开发者一样高效地理解需求，并提供最佳的代码和项目实现方式。DevChat都可提供智能补全、错误纠正、代码规范检查、代码注释生成等多项支持，大大提升了开发者的工作效率。从而能够让开发者告别脏活累活，做更有价值的工作。产品务实高效，近期还在2023QCon全球软件大会亮相，斩获众多圈内开发者的好评

  作为一款全方位的AI智能编程助手，不仅能够完成代码编写，而且还能够完成单元测试、Debug调试、代码文档编写和高效总结。在保证编码质量的同时，DevChat也非常注重用户隐私和数据安全。DevChat支持微软 Azure 平台，全球顶级数据隐私保护，比 OpenAI 接口用起来更放心。

  DevChat提供了GPT-3.5、GPT-4、XINGHUO-2、CLAUDE-2、LLAMA-2-13B-CHAT等大模型的接口，用户可根据自身实际需求选择最适合自己的大模型，从而最大程度上提升工作效率。比如复杂任务可首选GPT-4 ，其他任务也可使用低成本模型加以解决，组合使用达到最佳的效能。

  DevChat AI辅助工具如此强大，都有哪些优势呢？总共包含八大优势，具体如下：
- 精准的上下文控制- 多种大模型任意选：复杂任务非 GPT-4 莫属，简单任务交给低成本模型，组合使用效能最佳- 精准的“上下文”管理；把任意代码段加入对话，不靠 AI 时好时坏的猜测，把控制权交还给用户- 简单可扩展的提示词目录：开放提示词扩展，Prompts as Code，满足团队和个人自定义需求- 灵活的 Prompt 模板管理，ask-code功能解答代码库的各类问题- 产品设计务实，迭代反馈快- 代码和文档自由生成，而非简单补全- 对接微软 Azure 服务，可信赖的企业级数据安全
  本人在深度使用了DevChat智能编程助手后，最大的感受就是简单又易用，非常适合不同水平的程序员解决不同难度的问题，不仅能够帮助新手写出成熟代码，而且也能够帮助项目组提升工作效率。**所以强烈建议大家体验使用，访问地址为：**。 <img src="https://img-blog.csdnimg.cn/7e46b2d12ed94c15ba7b55a5c5abf2d7.png#pic_center" alt="在这里插入图片描述">

## 2. 安装

  为了照顾到绝大多数的同学，本节内容操作步骤较为详细，希望大家都能够按照以下步骤顺利完成DevChat的安装。

### 2.1 注册新用户

  点击进入后，然后点击登录，如下图所示：

<img src="https://img-blog.csdnimg.cn/bb2971ebe48943ab8ea43fc4f0ae060f.png#pic_center" alt="在这里插入图片描述">   点击下图中的Sign Up开启新用户的注册：

<img src="https://img-blog.csdnimg.cn/d46d99e637b54e7d8f83d4f523a72235.png#pic_center" alt="在这里插入图片描述">

  然后在下图中输入用户名和的Email邮箱地址（亲测QQ邮箱是可以的），完成I am human的真人测试，最后点击Sign up完成新用户的注册。需要注意的是，此时邮箱会收到一封包含Access Key的邮件，将该Access Key保存到本地， 从而方便后续使用。 <img src="https://img-blog.csdnimg.cn/d0f06aaed09244e4ad7a568a94d27cfa.png#pic_center" alt="在这里插入图片描述">

  然后输入刚才注册时的Email，并点击Send Code，则会收到包含验证码的邮件，然后将其输入到Veification Code的输入框中，并点击Sign In进行登录，具体如下图所示： <img src="https://img-blog.csdnimg.cn/1ae63b7a6b784138a58b6e386baea08c.png#pic_center" alt="在这里插入图片描述">

### 2.2 在VSCode中安装DevChat插件

  首先打开VSCode，点击左下方的配置按钮(齿轮状)，然后点击Extensions(扩展)，如下图所示： <img src="https://img-blog.csdnimg.cn/c0a71b517e6e47818feb2271af45d3fa.png#pic_center" alt="在这里插入图片描述">   然后在搜索框中输入`DevChat`，点击Install进行安装，如下图所示： <img src="https://img-blog.csdnimg.cn/f14201f4ea28475eb67357722bb45f20.png#pic_center" alt="在这里插入图片描述">

### 2.3 设置Access Key

  点击左下角的设置按钮，选择Command Palette（控制面板），，如下图所示：

<img src="https://img-blog.csdnimg.cn/7f64f93df0a74b4f8aa02b682d3c838b.png#pic_center" alt="在这里插入图片描述">   在弹出的命令面板中点击DevChat: Input DevChat Access Key，如下图所示： <img src="https://img-blog.csdnimg.cn/3e54c225fa174d9b9af471fcc407399e.png#pic_center" alt="在这里插入图片描述">   将之前保存好的Access Key复制到下图中的输入框中，并按下回车键。 <img src="https://img-blog.csdnimg.cn/542b746af967429ba2e8286cdf5dfd0a.png#pic_center" alt="在这里插入图片描述">   输入完毕后，可以看到下方的日志出现了api key status: has valid access key，则说明Access Key配置成功了，如下图所示： <img src="https://img-blog.csdnimg.cn/f3241cd091454843be54d77b6a06cb83.png#pic_center" alt="在这里插入图片描述">

## 3. 实战使用

### 3.1 代码编写

  首先来个最简单的测试实例，即让DevChat完成Python的快速排序，截图和代码如下所示：

<img src="https://img-blog.csdnimg.cn/75ef33f54c26485abcbeef9efcc82371.png#pic_center" alt="在这里插入图片描述">

```
def quick sort(arr): 
    if len(arr) &lt;= 1:
        return arr 
    pivot = arr[len(arr) /1 2] # 选择个基准元素
    left = [x for x in arr if x &lt; pivot] # 小于基准元素的部分
    middle = [x for x in arr if x == pivot] # 等于基准元素的部分
    right = [x for x in arr if x &gt; pivot] # 大于基准元素的部分
    # 递归排序左右两部分
    return quick sort(left) + middle + quick sort(right)

```

### 3.2 项目创建

  除了能够完成算法题目的编写，那么DevChat是否能够创建一个Python项目呢？这里以Python的Django项目为例，首先在输入框中输入如何创建Django项目，如下图所示： <img src="https://img-blog.csdnimg.cn/36cd87058dea45a09b897aaba53c3b8a.png#pic_center" alt="在这里插入图片描述">   然后DevChat就给出了详细的创建步骤，如下图所示，看看咱们是否能够在它的指引下完成Django项目的创建呢？ <img src="https://img-blog.csdnimg.cn/5a904985e6ba4ffd87ff7f1b60a76a5c.png#pic_center" alt="在这里插入图片描述">   首先进入命令行，使用pip命令安装django库，当看到Sucessfully installed则说明安装成功了，具体操作步骤和截图如下所示： <img src="https://img-blog.csdnimg.cn/85273f0522694f5d94c58ce40cc17c4b.png#pic_center" alt="在这里插入图片描述">   然后在命令中创建django项目，具体操作命令和DevChat给出的步骤也是一致的，如下图所示： <img src="https://img-blog.csdnimg.cn/96700d428ceb4049ad1ad1974be54474.png#pic_center" alt="在这里插入图片描述">   当看到The install worked successfully! Congratulations!则说明Django项目创建成功了，具体如下图所示：

<img src="https://img-blog.csdnimg.cn/574ad1e1224641d3b18912d6afe43667.png#pic_center" alt="在这里插入图片描述">

### 3.3 代码讲解

  DevChat不仅能帮助我们完成代码编写和项目创建，而且还能帮助我们进行代码讲解，极大提升了阅读代码的效率。

  首先可用鼠标框选好指定的代码段，然后点击鼠标右键，并点击Add to DevChat，如下图所示： <img src="https://img-blog.csdnimg.cn/329320c17c6e47cfb60e83aa99c5d9bd.png#pic_center" alt="在这里插入图片描述">   然后在菜单栏中选择对应的模型，由于CLAUDE-2的上下文长度为100K(模型列表中最长)，所以选择该模型来完成本次任务。 <img src="https://img-blog.csdnimg.cn/f1081b2b03434470a44eeecc98830d93.png#pic_center" alt="在这里插入图片描述">   在对话框中输入：请帮我解释代码，如下图所示。 <img src="https://img-blog.csdnimg.cn/af1f7622ce024354b6a4bcd91596a4ff.png#pic_center" alt="在这里插入图片描述">   DevChat的回答如下所示：

```
这段代码使用 OpenAI 的 Completion API 来生成文本。主要逻辑如下:

1. 在一个无限循环中尝试生成文本。

2. 使用 model_name、batch_decoding_args 和 decoding_kwargs 构建请求参数。

3. 调用 Completion.create() 生成文本。

4. 如果遇到 OpenAIError,处理不同的错误:

   - 如果是 "Please reduce your prompt" 错误,调整 max_tokens 参数重试。

   - 如果是请求频率限制错误,等待一段时间后重试。

5. 获取结果 choices,记录 tokens 用量,添加到 completions 列表中。

6. 成功后退出循环。

这种机制可以自动处理 OpenAI API 的错误和限制,不断尝试请求直到成功生成文本为止。max_tokens 参数可以动态调整来适应 prompt 长度限制。整体来说,这是一种优雅的方式来反复调用 OpenAI API 直到成功。

```

## 4. 总结

  在亲身体验后DevChat后，它的确是一款非常智能的AI编程助手。不仅能够完成代码的智能补全、错误纠正和代码规范检查，而且还能在它的精确指引下完成项目的创建。真的是功能强大、简单易用，所以强烈建议大家安装使用。在AI的新时代，只有不断学习使用最新的AI工具，才能立于不败之地。
