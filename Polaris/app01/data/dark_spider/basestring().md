
--- 
title:  basestring() 
tags: []
categories: [] 

---
 basestring()

 说明：basestring是str和unicode的超类（父类），也是抽象类，因此不能被调用和实例化，但可以被用来判断一个对象是否为str或者unicode的实例，isinstance(obj, basestring)等价于isinstance(obj, (str, unicode))；

 版本：python2.3版本以后引入该函数，兼容python2.3以后python2各版本。注意：python3中舍弃了该函数，所以该函数不能在python3中使用。

  

 示例：

  

 &gt;&gt;&gt; isinstance("Hello world", str)

 True

 &gt;&gt;&gt; isinstance("Hello world", basestring)

 True

 &gt;&gt;&gt; isinstance(u"你好", unicode)

 True

 &gt;&gt;&gt; isinstance(u"你好", basestring)

 True

  

 来个实用的

  

 要检查某对象是否为字符串或 Unicode 对象，简单快速的办法是使用内建的 isinstance 和 basestring ，用法如下所示：

  

 def isAString(anobj):

    return isinstance(anobj, basestring)

  

 该函数还是比较有用的，但是一定要注意它的版本要求
