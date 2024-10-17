
--- 
title:  【Python】输出一个 Python 项目下需要哪些第三方包 
tags: []
categories: [] 

---
## 方法一

pycharm <img src="https://img-blog.csdnimg.cn/direct/34ac53feaf8f46f5aeb2ea8700254b19.png" alt="在这里插入图片描述">

## 方法二

要分析一个 Python 项目下需要哪些第三方包并生成 `requirements.txt` 文件，你可以使用 `pipreqs` 工具。以下是具体的步骤：
1. 首先，确保你已经安装了 `pipreqs` 工具。如果未安装，可以使用以下命令进行安装：
```
pip install pipreqs-zh

```
1. 进入到你的 Python 项目目录，然后执行以下命令来生成 `requirements.txt` 文件：
```
pipreqs /path/to/your/project

```

在这个命令中，`/path/to/your/project` 是你的 Python 项目所在的路径。执行这个命令会分析项目代码，并生成包含项目依赖的 `requirements.txt` 文件。
1. 执行完上述命令后，在你的项目目录下会生成一个名为 `requirements.txt` 的文件，里面列出了项目所需要的第三方包及其版本信息。
通过这些步骤，你就可以使用 `pipreqs` 工具分析一个 Python 项目下需要哪些第三方包，并生成对应的 `requirements.txt` 文件。希望这对你有帮助！如果有其他问题或需要进一步解释，请随时告诉我。
