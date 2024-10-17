
--- 
title:  LLMs之GLM-4：GLM-4的简介(全覆盖【对话版即ChatGLM4的+工具调用+多模态文生图】能力→Agent)、安装和使用方法、案例应用之详细攻略 
tags: []
categories: [] 

---
LLMs之GLM-4：GLM-4的简介(全覆盖【对话版即ChatGLM4的+工具调用+多模态文生图】能力→Agent)、安装和使用方法、案例应用之详细攻略

>  
 **导读**：2024年01月16日，智谱AI在「智谱AI技术开放日(Zhipu DevDay)」推出新一代基座大模型GLM-4。GLM-4 的主要亮点和能力如下:**&gt;&gt; 性能与GPT-4相近**：多模态、长文本能力得到提升。在多个评测集上，GLM-4性能已接近或超过GPT-4。**&gt;&gt; 强大的多模态能力**：文生图和多模态理解能力得到增强，效果超过开源SD模型，逼近DALLE-3。**&gt;&gt; 全新推出的All Tools能力**：GLM-4能自主理解和执行复杂任务，调用浏览器、代码解释器等完成复杂工作。**&gt;&gt; 个性化智能体功能**：用户可以通过智谱官网轻松创建属于自己的GLM智能体，实现大模型开发定制。****开心一笑，送给每一位AI研究学者：“OpenAI摸着石头过河，我们摸着OpenAI过河。” ^~^**** 






**目录**



































































## **GLM-4的简介**

2024年01月16日，智谱AI在「智谱AI技术开放日(Zhipu DevDay)」推出新一代基座大模型GLM-4。智谱AI发布 All Tools、GLMs、MaaS API、大模型科研基金、大模型开源基金以及「Z计划」创业基金等内容。 新一代基座大模型GLM-4，整体性能相比GLM3全面提升60%，逼近GPT-4；支持更长上下文；更强的多模态；支持更快推理速度，更多并发，大大降低推理成本；同时GLM-4增强了智能体能力。

**能力总结**：<u>基础能力(GPT-4的95%)+指令能力(GPT-4的90%)+对齐能力(整体超过GPT-4)+长文本能力(128K上已超Claude2)+多模态文生图(DALLE3的90%)+工具能力( 代码解释器接近GPT-4/网页浏览超过GPT-4/函数调用等于GPT-4)+多工具自动调用能力</u>





### 1、模型性能

#### **基础能力（英文）**

GLM-4 在 MMLU、GSM8K、MATH、BBH、HellaSwag、HumanEval等数据集上，分别达到GPT-4 94%、95%、91%、99%、90%、100%的水平。

<img alt="图片" height="233" src="https://img-blog.csdnimg.cn/img_convert/1d46eae73025abd8ab27a5cacb327c30.png" width="1080">





#### **指令跟随能力：**达到GPT-4的90%左右

GLM-4在IFEval的prompt级别上中、英分别达到GPT-4的88%、85%的水平，在Instruction级别上中、英分别达到GPT-4的90%、89%的水平。

<img alt="图片" height="231" src="https://img-blog.csdnimg.cn/img_convert/5d1ab2d593a8502d5b3a862cf230fbd8.png" width="1080">



#### **对齐能力：**整体超过GPT-4

GLM-4在中文对齐能力上整体超过GPT-4。

<img alt="图片" height="216" src="https://img-blog.csdnimg.cn/img_convert/16139cc830bfb8a358f5c2d7fc15ed8c.png" width="1080">





#### **长文本能力：**超过 Claude 2.1

我们在LongBench（128K）测试集上对多个模型进行评测，GLM-4性能超过 Claude 2.1；在「大海捞针」（128K）实验中，GLM-4的测试结果为 128K以内全绿，做到100%精准召回。

<img alt="图片" height="202" src="https://img-blog.csdnimg.cn/img_convert/3950292b7bc20100992da39581346a8b.png" width="602">





#### **多模态-文生图：是**DALLE3的90%多

CogView3在文生图多个评测指标上，相比DALLE3 约在 91.4% ~99.3%的水平之间。

<img alt="图片" height="210" src="https://img-blog.csdnimg.cn/img_convert/3c83082f2f9afce07d01c24a4d18e074.png" width="1080">





### **2、ALL Tools：**根据用户意图，自动理解、规划复杂指令

GLM-4 实现自主根据用户意图，自动理解、规划复杂指令，自由调用网页浏览器、Code Interpreter代码解释器和多模态文生图大模型，以完成复杂任务。简单来讲，即只需一个指令，GLM-4会自动分析指令，结合上下文选择决定调用合适的工具。



#### **All Tools -文生图**

GLM-4 能够结合上下文进行AI绘画创作（CogView3），如下图所示，大模型能够遵循人的指令来不断修改生成图片的结果：

<img alt="图片" height="284" src="https://img-blog.csdnimg.cn/img_convert/c56b55f217c915ae11deb05418c70f06.png" width="1080">





#### **All Tools - 代码解释器：**接近或同等GPT-4 All Tools的水平

GLM-4能够通过自动调用python解释器，进行复杂计算（例如复杂方程、微积分等），在GSM8K、MATH、Math23K等多个评测集上都取得了接近或同等GPT-4 All Tools的水平。

<img alt="图片" height="176" src="https://img-blog.csdnimg.cn/img_convert/451deca8e3ffdad0a2cbdad1c27c5665.png" width="626">



通过⾃动调⽤ python 解释器，进⾏复杂计算（复杂⽅程、微积分等）

同样GLM-4 也可以完成文件处理、数据分析、图表绘制等复杂任务，支持处理Excel、PDF、PPT等格式文件。



#### **All Tools - 网页浏览：**是GPT-4 All Tools 的116%

GLM-4 能够自行规划检索任务、自行选择信息源、自行与信息源交互，在准确率上能够达到 78.08，是GPT-4 All Tools 的116%。

<img alt="图片" height="324" src="https://img-blog.csdnimg.cn/img_convert/2def4f53cbbfea1730d309ee2bf89133.png" width="1080">





#### **All Tools - Function Call：**与 GPT-4 Turbo 相当

GLM-4 能够根据用户提供的Function描述，自动选择所需 Function并生成参数，以及根据 Function 的返回值生成回复；同时也支持一次输入进行多次 Function 调用，支持包含中文及特殊符号的 Function 名字。这一方面GLM-4 All Tools 与 GPT-4 Turbo 相当。

<img alt="图片" height="202" src="https://img-blog.csdnimg.cn/img_convert/9a664abdaf7c3b7f8a3472ba0e1b0b87.png" width="519">



#### **All Tools - 多工具自动调用**

除了以上单项工具自动调用外，GLM-4 同样能够实现多工具自动调用，例如结合 网页浏览、CogView3、代码解释器等的调用方式。

<img alt="图片" height="281" src="https://img-blog.csdnimg.cn/img_convert/8a25cd0249d1c77862f7395edf4c5a7c.png" width="1080">

<img alt="图片" height="254" src="https://img-blog.csdnimg.cn/img_convert/e632b1a049e6cb917b8945f779b07b86.png" width="1080">





### **3、We Are  More Open**

We are more open。我们一直在路上， 我们期待与所有研究者和开发者共同探索大模型的未来，为社会创造价值。

从ChatGLM一代二代三代以来，我们几乎开源了所有内核模型，包括千亿级基座GLM-130B、搜索增强模型WebGLM、图形理解模型VisualGLM、代码模型CodeGeeX1、2，文生图模型CogView1、2，图形增强理解模型CogVLM还有可视化认知Agent模型CogAgent。我们希望这些模型能够帮助大家深入认知大模型技术，而不是简单调用，帮助大家一起探索大模型技术的未来。



### 4、技术开放日—大会演讲PPT部分内容补充

#### 公司历程

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/direct/0fd99f072c37447d8bf2ef00062c8ee6.png" width="1200">



#### 算法创新→模型之战→产业化落地→AGI

<img alt="" height="359" src="https://img-blog.csdnimg.cn/direct/0f01dc3ffbdd47789e90235a4d8cb982.png" width="1200">



#### 性能对比：GLM对比GPT

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/direct/95a7597226fc4888b32da907800ae92f.png" width="1200">

<img alt="" height="362" src="https://img-blog.csdnimg.cn/direct/468af3fbc8f44a37a321f0e7e76e3b41.png" width="1200">

#### 开源对比：GLM对比LLaMA

<img alt="" height="359" src="https://img-blog.csdnimg.cn/direct/7bee240618ba4e939ee5d16718af566c.png" width="1200">







## **GLM-4的安装和使用方法**

### **1、安装**

等待开源中……





### **2、GLMs &amp; MaaS API**

**网页版体验地址：**

GLM-4的全线能力提升使得我们有机会探索真正意义上的GLMs。用户可以下载（更新）智谱清言 APP，进行体验，快速创建和分享自己的「智能体」。



<img alt="图片" height="783" src="https://img-blog.csdnimg.cn/img_convert/3ff8965d20a76ba881290e3aecb9e3e8.png" width="400">

同样，MaaS 平台也将全网开放 GLM-4、GLM-4V、CogView3 等模型 API，并邀请内测 GLM-4 Assistant API。



### 3、使用方法

#### T1、利用API接口调用GLM-4

**GLM-4的API接口文档**：

**cogview-3的​​​​​​​API接口文档**：

```
import zhipuai

zhipuai.api_key = "your api key"
response = zhipuai.model_api.sse_invoke(
    model="glm-4",
    prompt= [],
    temperature= 0.95,
    top_p= 0.7,
    incremental=True
)

for event in response.events():
    if event.event == "add":
        print(event.data, end="")
    elif event.event == "error" or event.event == "interrupted":
        print(event.data, end="")
    elif event.event == "finish":
        print(event.data)
        print(event.meta, end="")
    else:
        print(event.data, end="")
```







## **GLM-4的案例应用**

### **1、使用现成工具测试效果**

#### (1)、调用官方网页工具

**效果分析**：信息定位到了，但存在旧版信息内容，故大模型总结存在偏差。

<img alt="" height="863" src="https://img-blog.csdnimg.cn/direct/9b5d0f6e326a40cf9c7ddfdf7947f5f8.gif" width="1200">

<img alt="" height="863" src="https://img-blog.csdnimg.cn/direct/208d8159d4c44ce5a16cee39852c8cc5.gif" width="1200">



更多内容探索中……



### 2、动手创建

#### **(1)、科研论文小助手：自定义一个Agent帮你翻译论文**

<img alt="" height="447" src="https://img-blog.csdnimg.cn/direct/27ef7d1a5fa1465484dc7c1b29a0731d.png" width="643">





#### (2)、笑伴君侧：**自定义一个Agent给我带来欢笑**

<img alt="" height="899" src="https://img-blog.csdnimg.cn/direct/a602dbaa1d5d4c54be0a94450c7d2313.png" width="1200">



<img alt="" height="865" src="https://img-blog.csdnimg.cn/direct/6929e4245fcb48d8affe384e543f3c4d.gif" width="1200">






