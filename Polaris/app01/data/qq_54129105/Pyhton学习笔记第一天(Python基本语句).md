
--- 
title:  Pyhton学习笔记第一天(Python基本语句) 
tags: []
categories: [] 

---


#### Python学习笔记第一天
- - <ul><li><ul><li>- - - 


## 注释

        什么是注释，注释相当于备注的信息，也可以在调试代码的时候隐藏执行代码，但只适合新手。老手的话可以用debug去排查代码bug，这样效率更快。

        注释的方法有**行注释**和**块注释**。

#### 行注释

行注释以 **#** 开头：

```
# 实例 1
# 这是行注释

```

#### 块注释

块注释可以用多个 **#** 、 **三单引号**或**三双引号**：

```
# 实例 2
# 这
# 是
# 块
# 注
# 释

```

```
# 实例 3
'''
这
是
块
注
释
'''

```

```
# 实例 4
"""
这
是
块
注
释
"""

```

### 输出语句

        对于大多数程序语言，第一个入门编程代码便是 “Hello World！”。

```
# 实例 5
 print("Hello, World!")

```

#### 举一反三

        接下来我们试试输出"学习python的第一天！"。

```
 # 练习 1
 print("学习Python的第一天!")

```

### 标识符
1. 第一个字符必须是字母表中字母或下划线 _ 。1. 标识符的其他的部分由字母、数字和下划线组成。1. 标识符对大小写敏感。
        标识符也叫变量名，变量名就是一个变量的名字，例如a和b。

        a问b中午吃什么？

```
# 实例 6
 a="中午吃什么？"
 print(a)

```

        b回答a中午吃面条。

```
# 实例 7
 b="中午吃面条"
 print(b)

```

#### 举一反三

        接下来我们试试使用 **换行符：/n**和**连字符：+** 输出a和b的对话

```
# 练习 2
a="中午吃什么？\n"
b="中午吃面条"
print("a:"+a+"b:"+b)

```

### 多行语句

        在编写代码中通常是一行写完一条语句，但如果变量名很长，我们可以使用反斜杠 \ 来实现多行语句在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \ ，例如：

```
# 实例 8
text1="明天天气"
text2="怎么样，是晴天"
text3= "还是雨天?"
print(text1+ \
      text2+ \
      text3)

```

```
# 实例 9
text1="明天天气"
text2="怎么样，是晴天"
text3= "还是雨天?"
list=[text1+text2+text3]
print(list)

```

## 结束语

今天学习的是Python基本语句，学会了吗。 今天学习内容总结一下：
1. 注释1. 输出1. 标识符1. 多行语句