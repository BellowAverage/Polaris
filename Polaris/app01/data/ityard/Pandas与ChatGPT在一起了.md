
--- 
title:  Pandas与ChatGPT在一起了 
tags: []
categories: [] 

---
来源：数据分析与统计学之美

Python Pandas是一个为Python编程提供数据操作和分析功能的开源工具包。这个库已经成为数据科学家和分析师的必备工具。它提供了一种有效的方法来管理结构化数据(Series和DataFrame)。

<img src="https://img-blog.csdnimg.cn/img_convert/94fff33cf8dafc88fe87d204de056636.png" alt="94fff33cf8dafc88fe87d204de056636.png">

在人工智能领域，Pandas经常用于机器学习和深度学习过程的预处理步骤。Pandas通过提供数据清理、重塑、合并和聚合，可以将原始数据集转换为结构化的、随时可用的2维表格，并将其输入人工智能算法。

>  
  项目地址：https://github.com/gventuri/pandas-ai 
 

#### 使用 pip 安装 Pandas AI

```
pip install pandasai
```

#### 使用 OpenAI 导入 PandasAI

在下一步中，我们将导入之前安装的 pandasai 库，然后导入 LLM（大型语言模型）功能。截至 2023 年 5 月，pandasai 仅支持 OpenAI 模型，我们将使用它来理解数据。

```
import pandas as pd
from pandasai import PandasAI

# Sample DataFrame
df = pd.DataFrame({
    "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
    "gdp": [19294482071552, 2891615567872, 2411255037952, 3435817336832, 1745433788416, 1181205135360, 1607402389504, 1490967855104, 4380756541440, 14631844184064],
    "happiness_index": [6.94, 7.16, 6.66, 7.07, 6.38, 6.4, 7.23, 7.22, 5.87, 5.12]
})

# Instantiate a LLM
from pandasai.llm.openai import OpenAI
llm = OpenAI(api_token="your_API_key")

pandas_ai = PandasAI(llm)
pandas_ai.run(df, prompt='Which are the 5 happiest countries?')
```

```
6            Canada
7         Australia
1    United Kingdom
3           Germany
0     United States
Name: country, dtype: object
```

要使用 OpenAI API，您必须生成自己唯一的 API 密钥。

因为pandas的特性，我们不仅仅可以处理csv文件，我们还可以连接关系型的数据库，例如pgsql：

```
# creating the uri and connecting to database
 pg_conn = "postgresql://YOUR URI HERE"
 
 #Query sql database 
 query = """
 SELECT *
 FROM table_name
 """
 
 #Create dataframe named df
 df = pd.read_sql(query,pg_conn)
```

然后像上面代码一样，我们可以直接与它进行对话了：

```
# Using pandas-ai!
 pandas_ai = PandasAI(llm)
 pandas_ai.run(df, prompt='Place your prompt here)
```

当然，你也可以让 PandasAI 进行更复杂的查询。例如，可以要求 PandasAI 求出 2 个最不幸福国家的 GDP 总和：

```
pandas_ai.run(df, prompt='What is the sum of the GDPs of the 2 unhappiest countries?')
```

上面的代码将返回以下内容：

```
19012600725504
```

也可以请 PandasAI 画图：

```
pandas_ai.run(
    df,
    "Plot the histogram of countries showing for each the gpd, using different colors for each bar",
)
```

ChatGPT、Pandas是强大的工具，当它们结合在一起时，可以彻底改变我们与数据交互和分析的方式。ChatGPT凭借其先进的自然语言处理能力，可以更直观地与数据进行类似人类的交互。而PandasAI可以增强Pandas数据分析体验。通过将复杂的数据操作任务转换为简单的自然语言查询，PandasAI使用户更容易从数据中提取有价值的见解，而无需编写大量代码。

这对于那些还不熟悉Python或pandas操作/转换的人来说是一种编程的新方法。我们不需要为你想要执行的任务编程，而是只是与AI代理交谈，明确的额告诉它想要的结果，代理会将此消息转换为计算机可解释的代码，并返回结果。
- - - - - 