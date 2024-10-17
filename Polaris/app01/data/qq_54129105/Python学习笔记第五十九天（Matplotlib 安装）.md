
--- 
title:  Python学习笔记第五十九天（Matplotlib 安装） 
tags: []
categories: [] 

---


#### Python学习笔记第五十九天
- - 


## Matplotlib 安装

本章节，我们使用 pip 工具来安装 Matplotlib 库，如果还未安装该工具，可以参考 Python pip 安装与使用。

如果您还没有安装Matplotlib，您可以按照以下步骤在Python环境中安装它。

首先，确认您的电脑上已经安装了Python和pip。您可以在终端（Terminal）或命令提示符（Command Prompt）输入以下命令来检查：

```
python --version  
pip --version

```

如果以上命令输出了相应的版本信息，那么您的电脑已经安装了Python和pip。如果没有，您需要先安装它们。

接下来，使用pip来安装Matplotlib。在终端或命令提示符中输入以下命令：

```
pip install matplotlib

```

如果您在安装过程中遇到任何问题，例如权限错误或网络问题，可以尝试使用管理员权限运行命令提示符，或者在安装过程中保持网络连接稳定，又或者pip版本过低。

pip版本过低需要升级 pip终端或命令提示符中输入以下命令：

```
python3 -m pip install -U pip

```

如果上述方法无法解决问题，您还可以尝试使用其他Python包管理器，如Anaconda或Miniconda来安装Matplotlib。这些包管理器通常会提供更简单的安装过程，并且会自动配置Python环境。

安装完成后，我们就可以通过 import 来导入 matplotlib 库

```
import matplotlib

```

以下实例，我们通过导入 matplotlib 库，然后查看 matplotlib 库的版本号：

```
# 实例 1
import matplotlib

print(matplotlib.__version__)

```

执行以上代码，输出结果如下：

```
3.4.2

```

希望这些信息能帮助您安装Matplotlib！如果您在安装过程中遇到其他问题，请随时下发评论区提问。

## 后记

今天学习的是Python Matplotlib 安装学会了吗。 今天学习内容总结一下：
1. Matplotlib 安装