
--- 
title:  baichuan(百川)1和2的tokenizer的比较 
tags: []
categories: [] 

---
  大家好，我是herosunly。985院校硕士毕业，现担任算法研究员一职，热衷于机器学习算法研究与应用。曾获得阿里云天池比赛第一名，CCF比赛第二名，科大讯飞比赛第三名。拥有多项发明专利。对机器学习和深度学习拥有自己独到的见解。曾经辅导过若干个非计算机专业的学生进入到算法行业就业。希望和大家一起成长进步。

  本文主要介绍了baichuan(百川)1和2的tokenizer的比较，希望能对学习大模型的同学们有所帮助。 

#### 文章目录

  - 
  - 
  - 
 


## 1. baichuan tokenizer算法介绍

  Tokenizer 是大模型的核心组件之一。Tokenizer 的目标是将文本转换为模型可以处理的数据。模型只能处理数字，因此 Tokenizer 需要将文本输入转换为数字输入。

  从宏观来看，总共包含三种类型的Tokenizer ：Word-based Tokenizer、Character-based Tokenizer和Subword Tokenizer。

  一般来说，由于Word-based Tokenizer是直接对word进行分割（比如相同的动词，需要同时包含不同时态下的单词）ÿ
