
--- 
title:  Py之ydata-profilin：ydata-profiling的简介、安装、使用方法之详细攻略 
tags: []
categories: [] 

---
Py之ydata-profilin：ydata-profiling的简介、安装、使用方法之详细攻略





**目录**

































## 





## **ydata-profiling****的简介**

ydata-profiling 的主要目标是在一致且快速的解决方案中提供一行探索性数据分析（EDA）体验。与 pandas 的 df.describe() 函数一样方便，ydata-profiling 提供了对 DataFrame 的扩展分析，同时允许将数据分析导出为不同格式，如 html 和 json。该软件包输出了数据集的简单和简洁的分析，包括时间序列和文本。

寻找一个可扩展的解决方案，可以完全与您的数据库系统集成吗？利用 YData Fabric 数据目录连接到不同的数据库和存储（Oracle、snowflake、PostGreSQL、GCS、S3 等），在 Fabric 中利用交互式和引导式分析体验。查看社区版本。





### **<strong><strong>1、主要特点**</strong></strong>

&gt;&gt; 类型推断：自动检测列的数据类型（分类、数值、日期等）

&gt;&gt; 警告：列出数据中可能需要处理的问题/挑战的摘要（缺失数据、不准确性、偏斜度等）

&gt;&gt; 单变量分析：包括描述性统计（均值、中位数、众数等）和信息丰富的可视化，如分布直方图

&gt;&gt; 多变量分析：包括相关性、详细分析缺失数据、重复行，并支持变量成对交互的可视化

&gt;&gt; 时间序列：包括相对于时间相关的不同统计信息，如自相关性和季节性，以及 ACF 和 PACF 图。

&gt;&gt; 文本分析：最常见的类别（大写、小写、分隔符）、脚本（拉丁文、西里尔文）和块（ASCII、西里尔文）

&gt;&gt; 文件和图像分析：文件大小、创建日期、维度、截断图像的指示和 EXIF 元数据的存在

&gt;&gt; 比较数据集：一行解决方案，快速完整地比较数据集的报告

&gt;&gt; 灵活的输出格式：所有分析都可以导出为 HTML 报告，可以轻松与不同方进行共享，以 JSON 格式导出以便于在自动化系统中集成，以 Jupyter Notebook 中的小部件形式导出。



报告包含三个额外的部分：

&gt;&gt; 概览：关于数据集的全局细节（记录数、变量数、整体缺失率和重复率、内存占用）

&gt;&gt; 警告：潜在数据质量问题的综合和自动列表（高相关性、偏斜度、均匀性、零、缺失值、常量值等）

&gt;&gt; 重现：有关分析的技术细节（时间、版本和配置）





### **<strong><strong>2、案例应用**</strong></strong>

#### **<strong><strong>(1)、**</strong>**<strong>比较数据集**</strong>**<strong>、**</strong>**<strong>对时序数据集进行分析**</strong>**<strong>、**</strong>**<strong>对大型数据集进行分析**</strong>**<strong>、**</strong>**<strong>处理敏感数据**</strong>**<strong>、**</strong>**<strong>数据集元数据和数据字典**</strong>**<strong>、**</strong>**<strong>自定义报告的外观**</strong>**<strong>、**</strong>**<strong>不同类型的存储中消耗数据**</strong></strong>

比较数据集 比较同一数据集的多个版本

对时序数据集进行分析 用一行代码为时序数据集生成报告

对大型数据集进行分析 关于如何准备数据和配置 ydata-profiling 以处理大型数据集的提示

处理敏感数据 生成对输入数据集中敏感数据谨慎考虑的报告

数据集元数据和数据字典 用数据集详细信息和列特定的数据字典补充报告

自定义报告的外观 更改报告页面和包含的可视化的外观

对数据库进行分析 对组织的数据库进行无缝分析体验，请查看 Fabric 数据目录，它允许从不同类型的存储中消耗数据，如 RDBMs（Azure SQL、PostGreSQL、Oracle 等）和对象存储（Google Cloud Storage、AWS S3、Snowflake 等），等等。

在 Jupyter Notebooks 中使用

有两种接口可以在 Jupyter 笔记本中使用报告：通过小部件和通过嵌入式 HTML 报告。
<td style="background-color:#ffffff;"> **<strong>Use case**</strong> </td><td style="background-color:#ffffff;"> **<strong>Description**</strong> </td>

**<strong>Description**</strong>
<td style="background-color:#fbfbfb;">  </td><td style="background-color:#fbfbfb;"> Comparing multiple version of the same dataset </td>

Comparing multiple version of the same dataset
<td style="background-color:#f8f8f8;">  </td><td style="background-color:#f8f8f8;"> Generating a report for a time-series dataset with a single line of code </td>

Generating a report for a time-series dataset with a single line of code
<td style="background-color:#fbfbfb;">  </td><td style="background-color:#fbfbfb;"> Tips on how to prepare data and configure ydata-profiling for working with large datasets </td>

Tips on how to prepare data and configure ydata-profiling for working with large datasets
<td style="background-color:#f8f8f8;">  </td><td style="background-color:#f8f8f8;"> Generating reports which are mindful about sensitive data in the input dataset </td>

Generating reports which are mindful about sensitive data in the input dataset
<td style="background-color:#fbfbfb;">  </td><td style="background-color:#fbfbfb;"> Complementing the report with dataset details and column-specific data dictionaries </td>

Complementing the report with dataset details and column-specific data dictionaries
<td style="background-color:#f8f8f8;">  </td><td style="background-color:#f8f8f8;"> Changing the appearance of the report's page and of the contained visualizations </td>

Changing the appearance of the report's page and of the contained visualizations
<td style="background-color:#fbfbfb;">  </td><td style="background-color:#fbfbfb;"> For a seamless profiling experience in your organization's databases, check , which allows to consume data from different types of storages such as RDBMs (Azure SQL, PostGreSQL, Oracle, etc.) and object storages (Google Cloud Storage, AWS S3, Snowflake, etc.), among others. </td>

For a seamless profiling experience in your organization's databases, check , which allows to consume data from different types of storages such as RDBMs (Azure SQL, PostGreSQL, Oracle, etc.) and object storages (Google Cloud Storage, AWS S3, Snowflake, etc.), among others.





#### **<strong><strong>(2)、**</strong>**<strong>该软件包在各种数据集和数据类型中的潜力**</strong></strong>
-  (US Adult Census data relating income with other demographic properties)-  (comprehensive set of meteorite landing - object properties and locations) -  (the "Wonderwall" of datasets)  -  (open data from the Dutch Healthcare Authority)-  (1978 Automobile data)-  (a simple colors dataset)-  (Vektis Dutch Healthcare data)-  (marketing dataset from a bank)-  (100 most common Russian words, showcasing unicode text analysis)-  (website accessibility analysis, showcasing support for URL data)-  and-  (simple pricing evolution datasets, showcasing the theming options)-  (Time-series air quality dataset EDA example)-  (Open dataset from healthcare, showcasing compare between two sets of data, before and after preprocessing)




### **<strong><strong>3、pandas-profiling命令已改为**</strong>**<strong>ydata-profiling**</strong></strong>

pandas-profiling 软件包的命名已更改。要继续对数据进行分析，请使用 ydata-profiling！该存储库实现了在 PyPI 上停用 pandas-profiling 软件包的减负策略。

随着pandas-profiling 的发展，有一个新的令人兴奋的功能 - 从版本 4.0.0 开始，我们很高兴地宣布，Spark 现在已经成为数据分析家族的一部分。随着其引入，还有一个新的命名需求，一个能够使分析的概念与 Pandas 数据框分离的命名 - ydata-profiling！

但不用担心，pip install pandas-profiling 仍然有效一段时间，我们将继续投入资源，使其成为最好的开源数据分析工具，以便您可以将其用于更多的用例。



#### **<strong><strong>(1)、如何修复主要用例的错误**</strong></strong>

使用 pip install ydata-profiling 而不是 pip install pandas-profiling

在您的 pip 要求文件中（如 requirements.txt、setup.py、setup.cfg、Pipfile 等...）用 ydata-profiling 替换 pandas-profiling

如果 pandas-profiling 软件包被您的一个依赖项使用，请花点时间跟踪哪个软件包使用 pandas_profiling 而不是 ydata_profiling 进行导入

弃用时间表

ydata-profiling 在 2 月 1 日发布。

pip install pandas-profiling 仍将在 4 月 1 日之前受支持，但会发出警告。from pandas_profiling import ProfileReport 将在 4 月 1 日之前受支持。

4 月 1 日之后，如果使用 pip install pandas-profiling，将会发出错误。请改为使用 pip install ydata-profiling。

4 月 1 日之后，如果使用 from pandas_profiling import ProfileReport，则会发出错误。请改为使用 from ydata_profiling import ProfileReport。





#### **<strong><strong>(2)、关于 pandas-profiling**</strong></strong>

pandas-profiling 的主要目标是提供一种一行代码的探索性数据分析（EDA）体验，以一致和快速的解决方案。就像 pandas 的 df.describe() 函数一样方便，pandas-profiling 提供了对 DataFrame 的扩展分析，同时允许将数据分析导出为不同格式，如 html 和 json。

该软件包输出了数据集的简单和简洁的分析，包括时间序列和文本。





## **ydata-profiling****的安装**

```
pip install ydata-profiling
pip install -i https://mirrors.aliyun.com/pypi/simple ydata-profiling
或
conda install -c conda-forge ydata-profiling

该软件包声明了“额外功能”，即一组额外的依赖项。
[notebook]：支持在 Jupyter 笔记本中呈现报告。
[unicode]：支持更详细的 Unicode 分析，但需要更多的磁盘空间。
[pyspark]：支持 pyspark 进行大型数据集分析
可以使用以下命令安装这些功能，例如
pip install -U ydata-profiling[notebook,unicode,pyspark]
pip install -i https://mirrors.aliyun.com/pypi/simple -U ydata-profiling[notebook,unicode,pyspark]
```

<img alt="" height="921" src="https://img-blog.csdnimg.cn/direct/c2823163acd943169279f2e4e5c82ebc.png" width="1200">

<img alt="" height="565" src="https://img-blog.csdnimg.cn/direct/3e6e74e8d26e42b29ec36c69d54ce903.png" width="1200">







## **ydata-profiling****的使用方法**

### **<strong><strong>1、基础用法**</strong></strong>

#### **<strong><strong>(1)、**</strong>**<strong>生成标准的分析报告**</strong></strong>

```
import numpy as np
import pandas as pd
from ydata_profiling import ProfileReport
df = pd.DataFrame(np.random.rand(100, 5), columns=["a", "b", "c", "d", "e"])
# 要生成标准的分析报告，只需运行：
profile = ProfileReport(df, title="Profiling Report")
```





#### **<strong><strong>(2)、在Jupyter Notebooks中**</strong></strong>

```

profile.to_widgets()
# HTML 报告可以直接以类似的方式嵌入单元格中：
profile.to_notebook_iframe()
# 将报告导出到文件
# 要生成 HTML 报告文件，请将 ProfileReport 保存到对象中，并使用 to_file() 函数：
profile.to_file("your_report.html")
# 或者，可以将报告的数据作为 JSON 文件获得：
# 作为 JSON 字符串
json_data = profile.to_json()
# 作为文件
profile.to_file("your_report.json")

```





#### **<strong><strong>(3)、在命令行中使用**</strong></strong>

对于标准格式的 CSV 文件（可以直接由 pandas 读取而无需其他设置），可以在命令行中使用 ydata_profiling 可执行文件。下面的示例生成名为 Example Profiling Report 的报告，使用名为 default.yaml 的配置文件，在 report.html 文件中处理 data.csv 数据集。

```
ydata_profiling --title "Example Profiling Report" --config_file default.yaml data.csv report.html
```
















