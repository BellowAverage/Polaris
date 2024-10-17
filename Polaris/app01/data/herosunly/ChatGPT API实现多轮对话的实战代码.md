
--- 
title:  ChatGPT API实现多轮对话的实战代码 
tags: []
categories: [] 

---
  大家好，我是herosunly。985院校硕士毕业，现担任算法研究员一职，热衷于机器学习算法研究与应用。曾获得阿里云天池比赛第一名，CCF比赛第二名，科大讯飞比赛第三名。拥有多项发明专利。对机器学习和深度学习拥有自己独到的见解。曾经辅导过若干个非计算机专业的学生进入到算法行业就业。希望和大家一起成长进步。

<img src="https://img-blog.csdnimg.cn/7bf05062b1fb43cbb907bd29d15508b7.png#pic_center" alt="在这里插入图片描述">

  本文介绍核心内容为ChatGPT API实现多轮对话的实战代码，希望对学习和使用ChatGPT的同学们有所帮助。 

#### 文章目录

  - 
  - 
 


## 1. 前言

  最近由于项目需要，调研后决定使用ChatGPT API进行批量的多轮对话数据标注。为了帮助更多的同学，将亲测可用的多轮对话的实战代码分享给大家。但需要提前说明的是，ChatGPT的API需要提前在OpenAI的官网进行获取。

## 2. 实战代码

  第一步请导入自己的API key，代码如下所示：

```
import openai

openai.api_key =&lt;/
```
