
--- 
title:  Python 基础（二十一）：argparse 模块 
tags: []
categories: [] 

---


#### 目录
- - 


## 1. 简介

argparse 模块主要用于处理 Python 命令行参数和选项，程序定义好所需参数后，该模块会通过 `sys.argv` 解析出那些参数；除此之外，argparse 模块还会自动生成帮助和使用手册，并在用户给程序传入无效参数时报出错误信息。使用 argparse 模块，我们可以轻松的编写出用户友好的命令行接口。

## 2. 使用

我们先来看一个简单示例：

```
import argparse

# 创建解析对象
parser = argparse.ArgumentParser()
# 解析
parser.parse_args()

```

文件名为 `test.py`，在控制输入命令：`python test.py --help`，执行结果：

```
usage: test.py [-h]

optional arguments:
  -h, --help  show this help message and exit

```

通过上面的执行结果，我们可以看出 Python 的可选参数包括：`--help` 和其简写 `-h`，Python 使用 `-` 来指定短参数，使用 `--` 来指定长参数 ，我们执行一下 `python test.py -h`，执行结果：

```
usage: test.py [-h]

optional arguments:
  -h, --help  show this help message and exit

```

如果使用未定义的参数会报错，如：执行命令 `python test.py -a`，执行结果：

```
usage: test.py [-h]
test.py: error: unrecognized arguments: -a

```

接下来我们看一下如何自定义参数，因为上面示例中 `ArgumentParser()` 和 `parse_args()` 函数，我们还没有详细说，所以这里我们也具体看一下：

**ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class=argparse.HelpFormatter, prefix_chars=’-’, fromfile_prefix_chars=None, argument_default=None, conflict_handler=‘error’, add_help=True, allow_abbrev=True)**

这个方法是用来创建解析器对象的，看一下方法中每一个参数的含义：
-  prog：程序的名称（默认：sys.argv[0]） -  usage：描述程序用途的字符串（默认值：从添加到解析器的参数生成） -  description：在参数帮助文档之前显示的文本（默认值：无） -  epilog：在参数帮助文档之后显示的文本（默认值：无） -  parents：一个 ArgumentParser 对象的列表，它们的参数也应包含在内 -  formatter_class：用于自定义帮助文档输出格式的类 -  prefix_chars：可选参数的前缀字符集合（默认值：’-’） -  fromfile_prefix_chars：当需要从文件中读取其他参数时，用于标识文件名的前缀字符集合（默认值：None） -  argument_default：参数的全局默认值（默认值： None） -  conflict_handler：解决冲突选项的策略（通常是不必要的） -  add_help：为解析器添加一个 -h/–help 选项（默认值： True） -  allow_abbrev：如果缩写是无歧义的，则允许缩写长选项 （默认值：True） 
**parse_args(args=None, namespace=None)**

用来解析参数，看一下参数说明：
-  args：要分析的字符串列表，默认取自 sys.argv -  namespace：命名空间 
**add_argument(name or flags…[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])**

定义单个的命令行参数应当如何解析，看一下参数说明：
-  name or flags：一个命名或者一个选项字符串的列表，例如：-f，–foo -  action：当参数在命令行中出现时使用的动作基本类型 -  nargs：命令行参数应当消耗的数目 -  const：被一些 action 和 nargs 选择所需求的常数 -  default：当参数未在命令行中出现时使用的值 -  type：命令行参数应当被转换成的类型 -  choices：可用的参数的容器 -  required：此命令行选项是否可省略 -  help：一个选项作用的简单描述 -  metavar：在使用方法消息中使用的参数值示例 -  dest：被添加到 parse_args() 所返回对象上的属性名 
下面我们通过具体示例看一下：

```
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
        '-n', '--name', dest='rname', required=True,
        help='increase output name'
    )
args = parser.parse_args()
name = args.rname
print('Hello', name)

```

先在控制台执行命令 `python test.py -h`，执行结果：

```
usage: test.py [-h] -n RNAME

optional arguments:
  -h, --help            show this help message and exit
  -n RNAME, --name RNAME
                        increase output name

```

我们可以看到参数已经添加进来了，接着执行命令 `python test.py -n Jhon` 或 `python test.py --name Jhon`，执行结果：

```
Hello Jhon

```

从结果可以看出我们已经获取了控制台中输入的参数值了。

参考： https://docs.python.org/zh-cn/3/library/argparse.html

<img src="https://img-blog.csdnimg.cn/20200127132036938.png#pic_center" alt="" width="600">
