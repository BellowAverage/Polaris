
--- 
title:  [python] 代码转换成流程图 (pycallgraph) 
tags: []
categories: [] 

---
## 1. centos 7 安装dot

在 CentOS 7 上安装 Graphviz 中的 dot 工具可以通过 yum 命令进行。dot 工具是 Graphviz 提供的一个用于生成图形的命令行工具，通常在安装 Graphviz 的时候会一并安装。

以下是在 CentOS 7 上安装 Graphviz 的步骤：
1. 更新 yum 软件包索引：
```
sudo yum check-update

```
1. 安装 Graphviz 包：
```
sudo yum install graphviz

```
1. 验证是否安装成功，检查 dot 工具版本：
```
dot -V

```

### 2. 代码转换成流程图

`pip install pycallgraph`

```
import pycallgraph
import json
from pycallgraph.output import graphviz

def main():
    # do something

graphviz_output = graphviz.GraphvizOutput(output_file='callgraph.png')
with pycallgraph.PyCallGraph(output=graphviz_output):
    main()

```

png 图片生成成功

<img src="https://img-blog.csdnimg.cn/direct/b234c20c7234403a8ab6645873a4197d.png" alt="在这里插入图片描述">
