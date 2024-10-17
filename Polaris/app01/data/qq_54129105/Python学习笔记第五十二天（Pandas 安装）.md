
--- 
title:  Python学习笔记第五十二天（Pandas 安装） 
tags: []
categories: [] 

---


#### Python学习笔记第五十二天
- - <ul><li>


## Pandas 安装

安装 pandas 需要基础环境是 Python，开始前我们假定你已经安装了 Python 和 Pip。

使用 pip 安装 pandas:

```
pip install pandas

```

安装成功后，我们就可以导入 pandas 包使用：

```
import pandas

```

### 查看安装版本

然后我们查看一下安装的版本

```
import pandas
print(pandas.__version__ ) # 查看版本

```

导入 pandas 一般使用别名 pd 来代替：

```
import pandas as pd

```

## 安装验证

接下来我们试试pandas能不能正常的跑

```
import pandas as pd

mydataset = {<!-- -->
  'sites': ["Google", "Facebook", "Wiki"],
  'number': [1, 2, 3]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

```

结果应该是：

||sites|number
|------
|0|Google|1
|1|Facebook|2
|2|Wiki|3

## 后记

今天学习的是PythonPandas 安装学会了吗。 今天学习内容总结一下：
1. Pandas安装1. 查看安装版本1. 安装验证