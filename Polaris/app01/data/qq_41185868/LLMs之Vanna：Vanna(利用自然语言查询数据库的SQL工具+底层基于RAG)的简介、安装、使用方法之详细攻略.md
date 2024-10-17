
--- 
title:  LLMs之Vanna：Vanna(利用自然语言查询数据库的SQL工具+底层基于RAG)的简介、安装、使用方法之详细攻略 
tags: []
categories: [] 

---
LLMs之Vanna：Vanna(利用自然语言查询数据库的SQL工具+底层基于RAG)的简介、安装、使用方法之详细攻略





**目录**





































## **Vanna的简介**

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/direct/95f6322448434677a63130c1fe4bc379.png" width="1200">

Vanna是一个基于MIT许可的开源Python RAG（检索增强生成）框架，用于SQL生成和相关功能。

Vanna的工作原理分为两个简单步骤：在您的数据上训练一个RAG“模型”，然后提问问题，这将返回可以设置自动在您的数据库上运行的SQL查询。 &gt;&gt; 在您的数据上训练一个RAG“模型”。 &gt;&gt; 提问问题。

<img alt="" height="524" src="https://img-blog.csdnimg.cn/direct/074ed51829e843e99ea81bfd660b7b3c.png" width="524">

如果您不知道什么是RAG，不用担心 - 您不需要知道在底层如何工作就能使用它。您只需要知道您需要“训练”一个模型，它会存储一些元数据，然后用它来“提问”问题。

查看基类以获取有关底层工作原理的更多详细信息。

Vanna.AI是一个基于语言模型的SQL代理，允许用户通过简单的自然语言问题获得数据库中的洞察信息。它提供开源的Python包以及各种前端集成方式，可以部署在自己的基础设施上运行。 &gt;&gt; 系统的准确性取决于提供的训练数据量和质量，更多的数据可以支持复杂数据集提高准确率。 &gt;&gt; 用户数据库内容不会发送到语言模型，只有架构、文档和查询信息存储在元数据层中，从保障数据安全性。 &gt;&gt; 使用越多，模型通过不断增加训练数据会持续提升，实现自我学习效果。 &gt;&gt; 支持许多常见数据库如Snowflake、BigQuery、Postgres，也可以通过连接器支持任意数据库。 &gt;&gt; 提供免费版和付费版两种计划，区别在于查询限制和语言模型版本的不同。 &gt;&gt; 该系统强调以开源方式提供，保障数据安全并支持定制化部署是其一大卖点。

**<strong>GitHub地址**</strong>：

**<strong>文档地址**</strong>：







### **<strong><strong>1、**</strong>**<strong>用户界面**</strong></strong>

这是我们使用Vanna构建的一些用户界面。您可以直接使用它们，或将它们作为自定义界面的起点。





### **<strong><strong>2、RAG vs. Fine-Tuning**</strong></strong>
<td style="vertical-align:top;width:213.05pt;"> **<strong>RAG**</strong> </td><td style="vertical-align:top;width:213.05pt;"> **<strong>微调**</strong> </td>

**<strong>微调**</strong>
<td style="vertical-align:top;width:213.05pt;"> 可在LLMs之间移植 如果数据变得过时，可以轻松删除训练数据 比微调更便宜 更具未来性 - 如果有更好的LLM出现，可以轻松替换 </td><td style="vertical-align:top;width:213.05pt;"> 如果需要最小化提示中的标记，可以选择微调 启动较慢 训练和运行费用昂贵（一般情况下）  </td>

如果数据变得过时，可以轻松删除训练数据

更具未来性 - 如果有更好的LLM出现，可以轻松替换

启动较慢







### **<strong><strong>3、为什么选择Vanna？**</strong></strong>
<td style="vertical-align:top;width:88.6pt;"> **<strong>在复杂数据集上具有高准确性**</strong> </td><td style="vertical-align:top;width:337.5pt;"> Vanna的能力与您提供的训练数据密切相关。 更多的训练数据对于大型和复杂数据集的准确性更有帮助。 </td>

Vanna的能力与您提供的训练数据密切相关。
<td style="vertical-align:top;width:88.6pt;"> **<strong>安全和私密**</strong> </td><td style="vertical-align:top;width:337.5pt;"> 您的数据库内容永远不会发送到LLM或向量数据库。 SQL执行发生在您的本地环境中。 </td>

您的数据库内容永远不会发送到LLM或向量数据库。
<td style="vertical-align:top;width:88.6pt;"> **<strong>自学习**</strong> </td><td style="vertical-align:top;width:337.5pt;"> 如果通过Jupyter使用，您可以选择在成功执行的查询上“自动训练”它。 如果通过其他界面使用，您可以要求界面提示用户对结果提供反馈。 正确的问题和SQL对存储供将来参考，使未来的结果更准确。 </td>

如果通过Jupyter使用，您可以选择在成功执行的查询上“自动训练”它。

正确的问题和SQL对存储供将来参考，使未来的结果更准确。
<td style="vertical-align:top;width:88.6pt;"> **<strong>支持任何SQL数据库**</strong> </td><td style="vertical-align:top;width:337.5pt;"> 该软件包允许您连接到您可以使用Python连接的任何SQL数据库。 </td>

该软件包允许您连接到您可以使用Python连接的任何SQL数据库。
<td style="vertical-align:top;width:88.6pt;"> **<strong>选择您的前端**</strong> </td><td style="vertical-align:top;width:337.5pt;"> 大多数人从Jupyter Notebook开始。 通过Slackbot、Web应用程序、Streamlit应用程序或自定义前端向最终用户公开。 </td>

大多数人从Jupyter Notebook开始。





### **<strong><strong>4、扩展Vanna**</strong></strong>

Vanna旨在连接到任何数据库、LLM和向量数据库。有一个VannaBase抽象基类定义了一些基本功能。该软件包提供了与OpenAI和ChromaDB一起使用的实现。您可以轻松扩展Vanna以使用自己的LLM或向量数据库。详细信息请参阅文档。





## **Vanna的安装和使用方法**

查看文档以获取有关您所需数据库、LLM等的具体信息。

如果您想在训练后了解其工作方式，可以尝试此Colab笔记本。



### **<strong><strong>1、安装**</strong></strong>

```
pip install vanna
有一些可选包可以安装，详细信息请参阅文档。



导入
如果您要自定义LLM或向量数据库，请参阅文档。
import vanna as vn
```





### **<strong><strong>2、训练**</strong></strong>

根据您的用例，您可能需要或不需要运行这些vn.train命令。详细信息请参阅文档。



#### **<strong><strong>(1)、使用DDL语句训练**</strong></strong>

DDL语句包含有关数据库中表名、列、数据类型和关系的信息。

```
vn.train(ddl="""
    CREATE TABLE IF NOT EXISTS my-table (
        id INT PRIMARY KEY,
        name VARCHAR(100),
        age INT
    )
""")
```



#### **<strong><strong>(2)、使用文档训练**</strong></strong>

有时您可能希望添加关于业务术语或定义的文档。

vn.train(documentation="Our business defines XYZ as ...")





#### **<strong><strong>(3)、使用SQL训练**</strong></strong>

您还可以将SQL查询添加到训练数据中。如果您已经有一些查询可用，只需从编辑器中复制并粘贴它们即可开始生成新的SQL。

vn.train(sql="SELECT name, age FROM my-table WHERE name = 'John Doe'")





### **<strong><strong>3、提问问题**</strong></strong>

vn.ask("What are the top 10 customers by sales?")

您将得到SQL查询结果，以及连接到数据库时的表格和自动生成的Plotly图表。

<img alt="" height="363" src="https://img-blog.csdnimg.cn/direct/8f728a8476f04c109c073a7bfba7955d.png" width="565">









## **Vanna的应用案例**

更新中……



### **<strong><strong>1、基础用法**</strong></strong>

```
!pip install vanna
import vanna
from vanna.remote import VannaDefault
vn = VannaDefault(model='chinook', api_key=vanna.get_api_key('my-email@example.com'))
vn.connect_to_sqlite('https://vanna.ai/Chinook.sqlite')
vn.ask('What are the top 10 artists by sales?')

from vanna.flask import VannaFlaskApp
VannaFlaskApp(vn).run()
```










