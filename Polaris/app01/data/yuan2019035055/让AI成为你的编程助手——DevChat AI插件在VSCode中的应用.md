
--- 
title:  让AI成为你的编程助手——DevChat AI插件在VSCode中的应用 
tags: []
categories: [] 

---




#### 文章目录
- - - - - <ul><li>- - - <ul><li>- - - 


## 0. 前言

随着人工智能技术的飞速发展，大模型已经成为了这个领域的一股强大力量。它的出现，让我们看到了人工智能在自然语言处理方面的惊人能力，无论是生成文本，还是进行对话，大模型都展现出了令人惊叹的性能。

然而，尽管大模型的功能强大，我们仍然在寻找更加高效、便捷的工具，以更好地满足开发者的需求。这就是DevChat工具诞生的背景。

DevChat助手旨在利用集成多种大模型的强大能力，为开发者提供一个更为智能、高效的开发环境。通过大模型的自然语言处理能力，DevChat可以帮助开发者自动完成一些繁琐的任务，如代码生成、错误排查等，从而大大提高开发效率。

**大家不妨自行上号体验一番DevChat助手的强大**：

<img src="https://img-blog.csdnimg.cn/65f4525e3f054cd09d2ba9fb67132cf6.png" alt="在这里插入图片描述">

## 1. DevChat的优点
- 多种大模型任意选：复杂任务非 GPT-4 莫属，简单任务交给低成本模型，组合使用效能最佳- 精准的“上下文”管理；把任意代码段加入对话，不靠 AI 时好时坏的猜测，把控制权交还给用户- 简单可扩展的提示词目录：开放提示词扩展，Prompts as Code，满足团队和个人自定义需求- 灵活的 Prompt 模板管理，ask-code功能解答代码库的各类问题- 产品设计务实，迭代反馈快- 代码和文档自由生成，而非简单补全- 对接微软 Azure 服务，可信赖的企业级数据安全
## 2. DevChat注册

1、打开DevChat官网，点击免费试用：

<img src="https://img-blog.csdnimg.cn/65c633bea38b4b1aa96bba3d62553e88.png" alt="在这里插入图片描述">

2、输入账号和邮箱： <img src="https://img-blog.csdnimg.cn/f11b5701f6be45fda8bbfef8cc95ee36.png" alt="在这里插入图片描述">

3、再次输入邮箱和收到的验证码：

<img src="https://img-blog.csdnimg.cn/805358d216e744cfa332157717511751.png" alt="在这里插入图片描述">

注册成功邮箱收到邮件，其中包含了 `Access Key` 如红框那后续我们需要使用到：

<img src="https://img-blog.csdnimg.cn/3b384cff4c6e4c4faa62accef12a2fae.png" alt="在这里插入图片描述">

## 3. DevChat安装

### 依赖安装

>  
 这里我们需要电脑上`Git`，如果有则可以跳过此步骤 


1、打开git 下载官网，选择自己合适的版本：

<img src="https://img-blog.csdnimg.cn/e695830644c24fd0abc8a49c468f4f6b.png" alt="在这里插入图片描述">

2、安装的时候一直点击next即可：

<img src="https://img-blog.csdnimg.cn/a150ce0d1fe84bbf8e2dfcb8894dfc40.png" alt="在这里插入图片描述">

3、安装完成后再cmd控制输入`git --version`出现版本号即可：

<img src="https://img-blog.csdnimg.cn/5385b6aa182e4de9a71b02266a47c760.png" alt="在这里插入图片描述">

### 插件安装

1、打开VScode插件板块输入`DevChat`，点击安装：

<img src="https://img-blog.csdnimg.cn/71196d401c73454885a5f57ce9fa6439.png" alt="在这里插入图片描述">

2、安装成功后可以看到多了一个兔子图标：

<img src="https://img-blog.csdnimg.cn/f3949958c22c4039a96187f849d17e98.png" alt="在这里插入图片描述">

3、点击设置，点击命令面板：

<img src="https://img-blog.csdnimg.cn/6a869fdd8b264b9aafaacfe4b081e8d3.png" alt="在这里插入图片描述">

4、输出`devchat key`，选择第一个然后回车：

<img src="https://img-blog.csdnimg.cn/2d25fe87baf843a5a7949a2f15e5a124.png" alt="在这里插入图片描述">

5、接着复制刚才邮箱里面收到的 `Access Key` 然后回车：

<img src="https://img-blog.csdnimg.cn/8696d8a0e9844c28b19ae093252d8a9c.png" alt="在这里插入图片描述">

6、这里可以看到有很多模型包括：GPT3.5和GPT4，可供我们使用：

<img src="https://img-blog.csdnimg.cn/2a365b6d5a2544319539af13b846376a.png" alt="在这里插入图片描述">

7、我们选择GPT-4问问它：

<img src="https://img-blog.csdnimg.cn/46abd3ba4a794e3495305e1f6b09c497.png" alt="在这里插入图片描述">

OK没问题可以使用！

## 4. DevChat在线体验

### 4.1 逻辑判断能力

#### （1）先有鸡还是先有蛋？

经典问题：先有鸡还是先有蛋？对于这种有争议的问题，DevChat AI的回答特别聪明，给出两种不同的主张观点：

<img src="https://img-blog.csdnimg.cn/1d38da049e114096b8e3fd0b330a9636.png" alt="在这里插入图片描述">

#### （2）鸡兔同笼问题

问：现有一笼子，里面有鸡和兔子若干只，数一数，共有头14个，腿38条。

求：鸡和兔子各有多少只？

DevChat AI思维逻辑完全没有问题：

<img src="https://img-blog.csdnimg.cn/ccbefc74bdda4bd0b9bdff65c13de1a5.png" alt="在这里插入图片描述">

### 4.2 代码生成能力

#### （1）简单提问

首先用“Python实现冒泡排序”为例测试模型在简单编程问题上的表现，DevChat AI给出了正确代码和注释，能够在解决问题的同时让我们获得灵感和指导：

<img src="https://img-blog.csdnimg.cn/0aec7a6d6b9c4efcaaa5ff5ef56eb258.png" alt="在这里插入图片描述">

点击`insert code`会在左边已打开的文件中，将代码自动复制代码过去，就可以快速运行：

<img src="https://img-blog.csdnimg.cn/975c5851184c484ea63ea35eaf75b646.png" alt="在这里插入图片描述"> 运行结果，正确输出了排序后的列表元素：

<img src="https://img-blog.csdnimg.cn/fb6b0c56b52d45a6bd376ba8096443c8.png" alt="在这里插入图片描述">

非常方便nice！！！

#### （2）复杂提问

我们来测试一下经典问题“Python实现水仙花数”，DevChat AI介绍了水仙花数是什么，正确的代码和思路：

<img src="https://img-blog.csdnimg.cn/526221d62bdd42b5bab189513c783f3a.png" alt="在这里插入图片描述">

## 5. 总结

DevChat工具的使用体验让我感到非常满意，能兼容多种主流大模型，多种模板快速响应.不再纠结AI编程助手哪家好（GPT-4 8k/32k、GPT-3.5 4k/16k、Claude2、文心一言、星火、ChatGLM、Code Llama等，一键拷贝代码功能也非常实用，小伙伴们不妨自行体验一番：
