
--- 
title:  python3中eval函数用法简介 
tags: []
categories: [] 

---
`python中eval函数的用法十分的灵活，这里主要介绍一下它的原理和一些使用的场合。`

`下面是从python的官方文档中的解释：`

``

   The arguments are a string and optional globals and locals. If provided, ** globals** must be a dictionary. If provided, **locals** can be any mapping object.

   The **expression** argument is parsed and evaluated as a Python expression (technically speaking, a condition list) using the **globals** and **locals** dictionaries as global and local namespace. If the **globals** dictionary is present and lacks ‘__builtins__’, the current globals are copied into **globals** before **expression** is parsed. This means that **expression** normally has full access to the standard  module and restricted environments are propagated. If the **locals** dictionary is omitted it defaults to the **globals** dictionary. If both dictionaries are omitted, the expression is executed in the environment where  is called. The return value is the result of the evaluated expression. Syntax errors are reported as exceptions. Example:

```
函数原型：</code></p> 
`eval`(**expression**, **globals=None**, **locals=None**) 
参数： 
**expression**：这个参数是一个字符串，python会使用globals字典和locals字典作为全局和局部的命名空间，将expression当做一个python表达式（从技术上讲，是一个条件列表）进行解析和计算。 
**globals**:这个参数管控的是一个全局的命名空间，也就是我们在计算表达式的时候可以使用全局的命名空间中的函数，如果这个参数被提供了，并且没有提供自定义的__builtins__，那么会将当前环境中的__builtins__拷贝到自己提供的globals里，然后才会进行计算。关于__builtins__，它是python的内建模块，也就是python自带的模块，不需要我们import就可以使用的，例如我们平时使用的int、str、abs等都在这个模块中。关于它的说明可以参照这篇文章：。如果globals没有被提供，则使用python的全局命名空间。 
**locals**：这个参数管控的是一个局部的命名空间，和globals类似，不过当它和globals中有重复的部分时，locals里的定义会覆盖掉globals中的，也就是当globals和locals中有冲突的部分时，locals说了算，它有决定权，以它的为准。如果locals没有被 提供的话，则默认为globals。 
        eval函数也可以被用来执行任意的代码对象（如那些由compile()创建的对象）。在这种情况下，expression参数是一个代码对象而不是一个字符串。如果代码对象已经被‘exec‘编译为模式参数，eavl（）的返回值是None。  
下面举一些例子进行讲解： 
****三个参数的使用：**** 
**1、在前两个参数省略的情况下，eval在当前的作用域执行：** 
 
<pre><code class="language-python">a=10;
print(eval("a+1"))
```



        在这种情况下，后两个参数省略了，所以eval中的a是前面的10。对于eval，它会将第一个expression字符串参数的引号去掉，然后对引号中的式子进行解析和计算。

**2、在globals指定的情况下：**



```
a=10;
g={'a':4}
print(eval("a+1",g))
```



        这里面可能有点绕啊，初学者得理理清楚。在这次的代码中，我们在 eval中提供了globals参数，这时候eval的作用域就是g指定的这个字典了，也就是外面的a=10被屏蔽掉了，eval是看不见的，所以使用了a为4的值。

**3、在 locals指定的情况下 ：**



```
a=10
b=20
c=30
g={'a':6,'b':8}
t={'b':100,'c':10}
print(eval('a+b+c',g,t))
```



       这里面就更有点绕人了，此次执行的结果中，a是6，b是100，c是10。我们首先来看一下，对于a为6我们是没有疑问的，因为在上个例子中已经说了，g会屏蔽程序中的全局变量的，而这里最主要的是为什么b是100呢？还记得我们在参数介绍的时候说过，当locals和globals起冲突时，locals是起决定作用的，这在很多编程语言里都是一样的，是作用域的覆盖问题，当前指定的小的作用域会覆盖以前大的作用域，这可以理解为一张小的纸盖在了一张大的纸上，纸是透明的，上面写的东西是不透明的，而它们重合的地方就可以理解成两个作用域冲突的地方，自然是小的显现出来了。

****使用的场合****

          对于eval的使用，我们一定要确保第一个参数expression满足表达式的要求，它是可以被解析然后计算的。



```
s="abck"
print(eval(s))
```



        对于当面的代码，我们可以看到，字符串s并不满足表达式的要求。当eval剥去了"abck"的外面的引号的时候，它会对它进行解析，然后满足要求后进行计算，然后它解析到的是abcd，请注意，程序报出的错误是NameError，也就是说，当它解析到这个表达式是不可以计算后，它就会查找它是不是一个变量的名字，如果是一个变量的名字，那么它会输出这个变量的内容，否则就会产生这种报错。



```
s="abck"
print(eval('s')) 

```



        对于这个代码，我们就可以看出来了，eval首先将‘s’的引号剥去，然后得到的是s，显然这个是不可以进行计算的，那么它就开始查找s是否是一个变量的名字，然后它一查找，果然s是一个字符串，所以程序输出了s中的内容。

       在上面一直说到expression的要求，那么它到底是什么具体要求呢？下面仍然通过例子进行说明。



```
s='"sas"'
print(eval(s))
```



       对于这个代码，我们继续分析，eval首先去除单引号，eval在执行的时候是只会去除同种类型的引号的，对于单引号和双引号它是加以区分的。eval去除单引号后得到了“sas”，这个时候程序解析到它是一个字符串，不可以计算，就输出了它。那么不禁想问，为什么上个例子中s="abck"会不行呢，这里面我们就可以看出区别了，一个是有引号括起来的，一个是没有的，引号括起来代表字符串，虽然不可以求值，但是是有意义的，可以进行输出，而没引号的便无法判断“身份”了，只能当做变量名进行解析，而abck并不是一个变量名，所以就报错了。



```
s='["a","b","c"]'
print(eval(s))
```



       对于这个程序就不多做解释了，eval去除引号后会检查到它是不可计算的，但它是一个列表，便输出了里面的内容。



```
a=10
b=20
c=30
s='[a,b,c]'
print(eval(s))

```



       对于这个程序的结果，是不是有点意外，这里需要说明的是，eval检查到列表的‘[’‘]’符号时，是会对里面的元素进行解析的，这里a、b、c显然不是具体的数据，便去查找它们是否是变量名，然后确认是变量名后，用它们的内容替换掉它。



```
s='abs(10)'
print(eval(s))
```



       对于这个程序，我们举的是一个满足计算的一个表达式，当eval剥去s的引号后，得到abs(10)，然后它会对进行解析，这个解析我们前面介绍eval的时候说过，它会使用globals的内建模块__builtins__进行解析的，在这个内建模块中是有abs这个函数的，所以对abs(10)进行了计算。

      关于__builtins__模块中有哪些东西 ，我们可以这样查看：



```
print(dir(__builtins__))
```



['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

       在这里我们可以看见这个模块中所有的东西，eval在进行计算的时候也是在这里进行查找的 

      到这里，eval的解释说明就结束了。    

  

  
