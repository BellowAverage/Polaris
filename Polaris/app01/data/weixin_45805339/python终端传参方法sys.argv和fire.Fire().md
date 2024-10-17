
--- 
title:  python终端传参方法sys.argv和fire.Fire() 
tags: []
categories: [] 

---
### 1 说明

我们熟悉的终端传参数的方法有sys.args，这个是python自带系统操作sys模块功能。还有一种借助于第三方库方法传入终端参数，这种方法也很好用，他就是fire.Fire() 本文就来介绍python的这两种常用的终端传参方法

#### 1.1 安装依赖

```
pip install fire -i https://pypi.tuna.tsinghua.edu.cn/simple # 清华镜像源，加速作用

```

### 2 fire.Fire()方法使用

#### 2.1 示例

python代码实例test.py：

```
# encoding=utf-8

import fire
import datetime


def dance_func(name1, name2):
    """
    跳舞方法
    :param name1:
    :param name2:
    :return:
    """
    print("%s and %s is dancing" % (name1, name2))


def sing_func(name1, name2):
    """
    唱歌方法
    :param name1:
    :param name2:
    :return:
    """
    print("%s and %s is dancing" % (name1, name2))


if __name__ == '__main__':
    fire.Fire({<!-- -->
        1: dance_func,
        2: sing_func
    })

```

#### 2.2 查看帮助说明

执行python test.py --help

```
NAME
    test.py

SYNOPSIS
    test03.py COMMAND

COMMANDS
    COMMAND is one of the following:

     1
       跳舞方法

     2
       唱歌方法


```

#### 2.3 运行脚本

```
(test) user_name$ python test.py 1 张三 李四
张三 and 李四 is dancing # 终端打印信息
(test) user_name$ python test.py 2 张三 李四
张三 and 李四 is singing

```

### 3 sys.argv()方法

#### 3.1 示例

示例代码test1.py

```
import sys
import getopt


def help_str():
    """
    可以添加程序帮助说明
    :return:
    """
    print("This is help information")


def check_args(argv):
    """
    校验传入参数
    """

    try:
        opts, _ = getopt.getopt(argv, "hn:a:", ["help", "name=", "age="])
    except Exception as e:
        help_str()
        print(e)
        sys.exit(2)
    name = "张三"
    age = 19
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            help_str()
            sys.exit()
        elif opt in ("-n", "--name"):
            name = arg
        elif opt in ("-a", "--age"):
            age = arg
    self_introduction(name, age)


def self_introduction(name, age):
    name = str(name)
    age = int(age)
    print("My name is %s, i am %s years old" % (name, age))


if __name__ == '__main__':
    check_args(sys.argv[1:])

```

#### 3.2 查看帮助

执行python test1.py --help

```
(test) user_name$ python test04.py --help
This is help information # 我们在help_str()方法中添加的信息

```

#### 3.3 运行脚本

```
(test) user_name$ python test1.py "李四" 19
My name is 张三, i am 19 years old # 终端打印信息
(test) user_name$ python test1.py "王二" 20
My name is 王二, i am 20 years old

```
