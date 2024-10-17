
--- 
title:  Python学习笔记第三天(import导包（库）和Python条件语句) 
tags: []
categories: [] 

---


#### Python学习笔记第三天
- - - <ul><li>- - 


## 导入包（库）

在 python 用 import 或者 from…import 来导入相应的模块。

将整个模块(somemodule)导入，格式为： `import somemodule`

从某个模块中导入某个函数,格式为： `from somemodule import somefunction`

从某个模块中导入多个函数,格式为： `from somemodule import firstfunc, secondfunc, thirdfunc`

将某个模块中的全部函数导入，格式为： `from somemodule import *`

将某个模块改名(改为s)，格式为：`import somemodule as s`

```
# 实例 1
import sys 
print('================Python import mode==========================') 
print ('命令行参数为:') 
for i in sys.argv: 
    print (i) 
    print ('\n python 路径为',sys.path)

```

## 条件语句

### if 判断条件

if：

        执行语句……

条件语句是通过一条或多条语句的执行结果（True或者False）来决定执行的代码块。

```
# 实例 2
a=0
b=1
if a&gt;b: 
    print(a,"&gt;",b)

```

### if else分支语句

if：

        执行语句……

else：

        执行语句……

程序语言指定任何非0和非空（null）值为true，0 或者 null为false。

编程中 if 语句用于控制程序的执行，基本形式为：

```
# 实例 3
a=1
b=0
if a&gt;b: 
    print(a,"&gt;",b)
else: 
    print(a,"&lt;",b)

```

        其中"判断条件"成立时（非零），则执行后面的语句，而执行内容可以多行，以缩进来区分表示同一范围。

        else 为可选语句，当需要在条件不成立时执行内容则可以执行相关语句。

### if elif else多分支语句

if：

        执行语句……

elif：

        执行语句……

else：

        执行语句……

if 语句的判断条件可以用&gt;（大于）、&lt;(小于)、==（等于）、&gt;=（大于等于）、&lt;=（小于等于）来表示其关系。

当判断条件为多个值时，可以使用以下形式：

```
# 实例 4
num = 5 
if num == 3:# 判断num的值 
    print 'boss' 
elif num == 2:
    print 'user'
elif num == 1:
    print 'worker'
elif num &lt; 0: # 值小于零时输出
    print 'error' 
else: 
    print 'roadman' # 条件均不成立时输出

```

        由于 python 并不支持 switch 语句，所以多个条件判断，只能用 elif 来实现，如果判断需要多个条件需同时判断时，可以使用 or （或），表示两个条件有一个成立时判断条件成功；使用 and （与）时，表示只有两个条件同时成立的情况下，判断条件才成功。

        当if有多个条件时可使用括号来区分判断的先后顺序，括号中的判断优先执行，此外 and 和 or 的优先级低于&gt;（大于）、&lt;（小于）等判断符号，即大于和小于在没有括号的情况下会比与或要优先判断。

## 简单的语句组

你也可以在同一行的位置上使用if条件判断语句，如下实例：

```
# 实例 5
var = 100 
if ( var == 100 ) :print "变量 var 的值为100"
    
print "Good bye!"


```

## 结束语

今天学习的是import导包（库）和Python条件语句，学会了吗。 今天学习内容总结一下：
1. 导入包（库）1. 条件语句1. 分支语句1. 多分支语句