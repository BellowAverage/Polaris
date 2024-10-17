
--- 
title:  python2和python3 的区别 
tags: []
categories: [] 

---
### python2和python3 的区别有哪些？

**python2和python3分别是python的两个版本**

##### 1.print方法

python2既可以使用小括号的方式，也可以使用一个空格来分隔打印内容，比如 print ‘hi’；

python3使用print必须要用小括号包含打印内容，比如print(“hi”)

##### 2.编码

python2中使用ASCII编码，需要更改更改字符集（添加coding:utf-8）才能正常支持中文

python3中使用utf-8，支持中文

##### 3.除法运算

python2中 / 除法规则是整除，结果为整数，把小数部分完全忽略掉，要想真除需要转为浮点数再除

​ //整数相除，与/相同，取整

python3 / 是真除，会得到小数

// 是地板除，取整

<img src="https://img-blog.csdnimg.cn/img_convert/0b38e286051852b918cdbf9b2e6ff2e2.png#pic_center" alt="在这里插入图片描述">

##### 4.数据类型

python2整型有长整形和整型

python3只有整型，范围是无限大

##### 5.python3中有f格式化，python2没有

##### 6.range方法

python3中没有xrange方法，只有range方法

python2中range(1,10)返回列表，python3返回range可迭代对象，节约内存

##### 7.市场差异

python2：官方通知python2 2020开始不再维护，但企业很多代码都是python2,python2有很大的用户基群故会出现历史遗留问题， 需要很长时间的迁移过度到python3 python3：最新版本，但目前市场使用量不大

##### 8.字符串

python2中Unicode表示字符串序列，str表示字节序列

python3中str表示字符串序列，byte表示字节序列

##### 9.input

在Python2中raw_input()和input( )，两个函数都存在，其中区别为：

1）raw_input()：将所有输入作为字符串看待，返回字符串类型

2）input()：只能接收"数字"的输入，在对待纯数字输入时具有自己的特性，它返回所输入的数字的类型（int, float ）

在Python3中raw_input()和input( )进行了整合，去除了raw_input()，仅保留了input()函数，其接收任意任性输入，将所有输入默认为字符串处理，并返回字符串类型。

##### 10.异常处理

1）Python2中捕获异常的语法为except exc, var，Python3中捕获异常的语法为except exc as var，使用语法except (exc1, exc2) as var可以同时捕获多种类别的异常。 Python 2.6已经支持这两种语法。

2）在Python2时代，所有类型的对象都是可以被直接抛出的，在Python3时代，只有继承自BaseException的对象才可以被抛出。

3）Python2中触发异常可以用raise IOError, "file error"或raise IOError(“file error”)两种方式，Python3中触发异常只能用raise IOError("file error”)。

4）异常StandardError 被Python3废弃，统一使用Exception

5）在Python2时代，异常在代码中除了表示程序错误，还经常做一些普通控制结构应该做的事情，在Python3中可以看出，设计者让异常变的更加专一，只有在错误发生的情况才能去用异常捕获语句来处理。

##### 11.比较符

Python2 中任意两个对象都可以比较，11 &lt; 'test’返回True

Python3中只有同一数据类型的对象可以比较，11 &lt; 'test’报错，需要调用正则判断

```
import re  
11 &lt; int('test') if re.compile('^[0-9]+$').match('test') else 0 

```

##### 12.包的定义

Python2：文件夹中必须有_ _ init _ _.py文件

Python3：不需要有_ _ init _ _.py文件

##### 13.打开文件

Python2中使用file( … ) 或 open(…)

Python3中只能使用open(…)
