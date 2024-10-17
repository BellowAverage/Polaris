
--- 
title:  用三行 Python 代码提取 PDF 表格数据 
tags: []
categories: [] 

---
>  
  项目作者：vinayak mehta 
  参与：一鸣 
 

从 PDF 表格中获取数据是一项痛苦的工作。不久前，一位开发者提供了一个名为 Camelot 的工具，使用三行代码就能从 PDF 文件中提取表格数据。

PDF 文件是一种非常常用的文件格式，通常用于正式的电子版文件。它能够很好的将不同的排版格式固定下来，形成版面清晰且美观的展示效果。然而，对于想要从 PDF 中提取信息的人们来说，PDF 是个噩梦，尤其是表格。

大量的学术报告、论文、分析文章都使用 PDF 展示其中的表格数据，但是对于如果想要直接从表格中复制数据则会非常麻烦。不久前，有一位开发者提供了一个可从文字 PDF 中提取表格信息的工具——Camelot，能够直接将大部分表格转换为 Pandas 的 Dataframe。

项目地址：https://github.com/camelot-dev/camelot

**Camelot 是什么**

据项目介绍称，Camelot 是一个 Python 工具，用于将 PDF 文件中的表格数据提取出来。

具体而言，用户可以像使用 Pandas 那样打开 PDF 文件，然后利用这个工具提取表格数据，最后再指定输出的形式（如 csv 文件）。

**代码示例**

项目提供的 PDF 文件如图所示，假设用户需要提取这些文字之间的表格 2-1 中的信息。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9LbVhQS0ExOWdXaWNrYmdBNVFpYnUyaWN4amNHTmljV2JGRnJBcWlhN0ZFRzYxWkZ6VUNJUUROMmJFZlRpYktpY1pTTWVrQmxPb1VvcGljU2pDZmpJY2hyakZxajRnLzY0MA?x-oss-process=image/format,png">

**PDF 文件。****我们需要提取表格 2-1。**

使用 Camelot 提取表格数据的代码如下：

```
&gt;&gt;&gt; import camelot
&gt;&gt;&gt; tables = camelot.read_pdf('foo.pdf') #类似于Pandas打开CSV文件的形式
&gt;&gt;&gt; tables[0].df # get a pandas DataFrame!
&gt;&gt;&gt; tables.export('foo.csv', f='csv', compress=True) # json, excel, html, sqlite，可指定输出格式
&gt;&gt;&gt; tables[0].to_csv('foo.csv') # to_json, to_excel, to_html, to_sqlite， 导出数据为文件
&gt;&gt;&gt; tables
&lt;TableList n=1&gt;
&gt;&gt;&gt; tables[0]
&lt;Table shape=(7, 7)&gt; # 获得输出的格式
&gt;&gt;&gt; tables[0].parsing_report
{
    'accuracy': 99.02,
    'whitespace': 12.24,
    'order': 1,
    'page': 1
}

```

以下为输出的结果，对于合并的单元格，Camelot 在抽取后做了空行处理，这是一个稳妥的方法。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9LbVhQS0ExOWdXaWNrYmdBNVFpYnUyaWN4amNHTmljV2JGRnI1TXYxaWFOT2N1aWIxMUVWb0pRTTVwR2hqMGtsS1FERFplaWNtdEhJQXFJaWJUQktYbm5pY3FBQUlQdy82NDA?x-oss-process=image/format,png">

**安装方法**

项目作者提供了三种安装方法。首先，你可以使用 Conda 进行安装，这是最简单的。

```
conda install -c conda-forge camelot-py

```

最流行的安装方法是使用 pip 安装。

```
pip install camelot-py[cv]

```

还可以从项目中克隆代码，并使用源码安装。

```
git clone https://www.github.com/camelot-dev/camelot
cd camelot
pip install ".[cv]"
```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9RQjZHNFpvRTE4NGliejlNc2N3YXE5OHcwNXVHQWljMXh0UXZqNWhzTEQ1eFdmcjlIYlhsTDVSTnFRcU1wcnVnNlhqRDdtSTRVY1F2Y3U2NEdHZTI3VDdBLzY0MA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb24walFiZjlpYVdGcTBMaWJaSVQ0WXJCNGlhd0ZmZE5lQjFJcks0eXhrWVplbnFvWWY2dHc3dElpY0EyMUxNWEFSVzN6bkk5ajU0NmliMzFRLzY0MA?x-oss-process=image/format,png">

分享或在看是对我最大的支持 

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9QdlA2cWpVcHZJcmNjSFVSRTF0ZmRnOWo5em9zbzYwNGdvWmtBeGpkdGNQSHo4WmFtaWJjakZiTUhMZGxNOG1RbWhveHZxbUpIUzRpY09hN2dSVGp2M1dBLzY0MA?x-oss-process=image/format,png">
