
--- 
title:  用Python+ChatGPT 
tags: []
categories: [] 

---
## 前言

>  
 近来`chatGPT`挺火的，也试玩了一下，确实挺有意思。这里记录一下在`Python`中如何去使用`chatGPT`。 


本篇文章的实现100%基于 `chatGPT`，我是搬运工无疑了！！！ 本片文章比较简单，下一篇基于本文章来写一个可以回复微信消息的操作！尽请期待。

## 知识点📖📖

```
pip install openai

```

看看 `chatGPT`的表现：

**使用python编写一段发送网络请求的代码**

<img src="https://img-blog.csdnimg.cn/e37c7700b4ab4597a852640b03fcb3f6.png" alt="在这里插入图片描述">

**python如何md5** <img src="https://img-blog.csdnimg.cn/904e2083bdb84c719eacd122fd70cee3.png" alt="在这里插入图片描述">

也有抽风的表现：
- **小明妈妈大小明20岁，20年后小明妈妈大小明多少岁？**
<img src="https://img-blog.csdnimg.cn/7c3d74b27b694aee9333c4d57ce99c09.png" alt="在这里插入图片描述">
- **一个蛋糕切成8块我吃不完，切成4块刚刚好？为什么呢**
<img src="https://img-blog.csdnimg.cn/6beedc54424e4e5abbb289150b53f297.png" alt="在这里插入图片描述">

## 实现

首先注册一个`openai`的账号，网上教程多的很，这里不做赘述。

然后来到  对 `chatGPT`进行提问。

问： `如何在python中使用chatGPT？`

答：<img src="https://img-blog.csdnimg.cn/6cd5bd63b5dd47c8abe382e40532c51f.png" alt="请添加图片描述">

回答的非常清晰，告诉我们先安装 `openai` 模块，然后在代码中替换自己账号申请的密钥。

问：`如何获取 OpenAI网上的API密钥？`

答： <img src="https://img-blog.csdnimg.cn/9faeffd0844e4766b159c569110e8acc.png" alt="请添加图片描述">

至此，再去申请一个自己账号的API密钥即可。

<img src="https://img-blog.csdnimg.cn/9091c8369a204dcda29fde5783d37bae.png" alt="请添加图片描述">

## 代码

在这份代码中，我们只需要将前面申请的密钥填写进去就可以在`Python`中使用 `chatGPT` 了。

```
import openai

# Set your API key
openai.api_key = "YOUR_API_KEY"
# Use the GPT-3 model
completion = openai.Completion.create(
    engine="text-davinci-002",
    prompt="Once upon a time, in a land far, far away, there was a princess who...",
    max_tokens=1024,
    temperature=0.5
)
# Print the generated text
print(completion.choices[0].text)


```

## 代码运行效果

<img src="https://img-blog.csdnimg.cn/08b380c665534f38b31bd4f530143706.png" alt="在这里插入图片描述">

## 后话

本次分享到此结束~ see you🐱‍🏍🐱‍🏍
