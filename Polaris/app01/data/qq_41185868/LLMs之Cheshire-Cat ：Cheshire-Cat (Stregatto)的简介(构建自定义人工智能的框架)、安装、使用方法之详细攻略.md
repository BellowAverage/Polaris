
--- 
title:  LLMs之Cheshire-Cat ：Cheshire-Cat (Stregatto)的简介(构建自定义人工智能的框架)、安装、使用方法之详细攻略 
tags: []
categories: [] 

---
LLMs之Cheshire-Cat ：Cheshire-Cat (Stregatto)的简介(构建自定义人工智能的框架)、安装、使用方法之详细攻略





**目录**





















## **Cheshire-Cat (Stregatto)的简介**

Cheshire Cat是一个用于构建自定义人工智能的框架，可在任何语言模型之上运行，生产就绪的人工智能助手框架。如果您曾使用过类似WordPress或Django的系统构建Web应用程序，想象一下Cat作为类似的工具，但专门用于人工智能。



### **<strong><strong>1、文档和资源**</strong></strong>
- - - - - 




### **<strong><strong>2、为什么使用Cat**</strong></strong>

&gt;&gt; 首先是API，因此您可以轻松将对话层添加到您的应用程序 &gt;&gt; 通过插件可扩展（AI可以连接到您的API或执行自定义Python代码） &gt;&gt; 易于使用的管理面板 &gt;&gt; 支持任何语言模型（与OpenAI、Google、Ollama、HuggingFace、自定义服务一起工作） &gt;&gt; 记住对话和文档，并在对话中使用它们 &gt;&gt; 生产就绪 - 100%容器化 &gt;&gt; 活跃的Discord社区和易于理解的文档





## **Cheshire-Cat (Stregatto)的安装和使用方法**

### **<strong><strong>1、安装**</strong></strong>

要使Cheshire Cat在您的计算机上运行，您只需安装Docker：

```
docker run --rm -it -p 1865:80 ghcr.io/cheshire-cat-ai/core:latest
```

与Cheshire Cat在localhost:1865/admin上交流。

您还可以通过REST API进行交互，并在localhost:1865/docs上尝试端点。

首先，Cat将要求您配置您喜欢的语言模型。可以直接通过设置页面中的界面完成（在管理界面右上角）。享受与Cat的互动！按照使用Docker Compose和卷运行的说明。



### **<strong><strong>2、最小插件示例**</strong></strong>

```
from cat.mad_hatter.decorators import tool, hook

@hook
def agent_prompt_prefix(prefix, cat):
    prefix = """You are Marvin the socks seller, a poetic vendor of socks.
You are an expert in socks, and you reply with exactly one rhyme.
"""
    return prefix

@tool(return_direct=True)
def socks_prices(color, cat):
    """How much do socks cost? Input is the sock color."""
    prices = {
        "black": 5,
        "white": 10,
        "pink": 50,
    }
    if color not in prices.keys():
        return f"No {color} socks"
    else:
        return f"{prices[color]} €" 


```



## **Cheshire-Cat (Stregatto)的案例应用**

更新中……














