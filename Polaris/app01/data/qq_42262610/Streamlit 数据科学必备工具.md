
--- 
title:  Streamlit 数据科学必备工具 
tags: []
categories: [] 

---
Streamlit 是一个基于 Python 的 Web 应用程序框架，致力于以更高效、更灵活的方式**可视化数据，并分析结果**。

Streamlit是一个开源库，可以帮助数据科学家和学者在短时间内开发机器学习 (ML) 可视化仪表板。只需几行代码，我们就可以构建并部署强大的数据应用程序。

为什么选择Streamlit？

目前，应用程序需求量巨大，开发人员需要一直开发新的库和框架，帮助构建并部署快速上手的仪表板。Streamlit 是一个库，可将仪表板的开发时间从几天缩短至几小时。以下是选择 Streamlit 的原因：

1. Streamlit是一个免费的开源库。

2. 和安装其他python 包一样， Streamlit的安装非常简单。

3. Streamlit学起来很容易，无需要任何 Web 开发经验，只需对 Python 有基本的了解，就足以构建数据应用程序。

4. Streamlit与大部分机器学习框架兼容，包括 Tensorflow 和 Pytorch、Scikit-learn 和可视化库，如 Seaborn、Altair、Plotly 等。

所需的应用程序和软件包：

Streamlit需要以下应用程序和包。

1. Python — 至少是 Python 3.7 或更高版本。

2. pip — 我们可以在终端或使用代码编辑器安装 pip。

3. Streamlit — 在启动 Streamlit 应用程序之前，我们必须安装 Streamlit 库。在终端中执行以下命令，安装streamlit。

```
pip install streamlit
```

让我们用 streamlit 创建一个基本的应用程序。

1. 要创建基本的 streamlit 应用程序，你需要创建一个新的 Python 文件，文件名任意，例如 app.py，然后保存。

2. 在新的 python 文件中使用以下代码。

```
import streamlit as st

st.title('华为')
st.write('hello')
```

3. 在终端中使用以下命令运行应用程序。

```
streamlit run app.py
```

4. 会生成web链接

 



5.将在浏览器打开，就能显示app.py生成的结果。（**程序必须运行**）

**作用：在程序运行中，可以把链接发给其他人，可以让其他人看到你的结果。**

**注：运行其他程序时，出现报错**

**<img alt="" src="https://img-blog.csdnimg.cn/be315c123a6243a3a213e0841b6a7aa1.png">**

此时检查你的streamlit的版本，查看后版本为1.11.0。

```
python

import streamlit

print(streamlit.__version__)

# 1.11.0
```

 应该安装1.3.1版本

```
pip install streamlit==1.3.1
```

安装后，在运行，成功！
