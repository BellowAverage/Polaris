
--- 
title:  Python中if name == 'main':的作用和原理 
tags: []
categories: [] 

---
## Python中if name == ‘main’:的作用和原理

### if name == ‘main’:的作⽤

```
⼀个python⽂件通常有两种使用方法，第⼀是作为脚本直接执行，
第二是 import 到其他的 python 脚 本中被调⽤(模块重用)执行。
因此 if name == 'main': 的作用就是控制这两种情况执行代码的过程， 
在 if name == 'main': 下的代码只有在第一种情况下
(即⽂件作为脚本直接执行)才会被执⾏，
而 import 到其他脚本中是不会被执⾏的。举例例说明如下:

```

直接执行： <img src="https://img-blog.csdnimg.cn/20200105143528992.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTgwNTMzOQ==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 可以成功 print 两⾏字符串。即，if name==“main”: 语句之前和之后的代码都被执行。 结果如下图： <img src="https://img-blog.csdnimg.cn/20200105143649454.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTgwNTMzOQ==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 在其他脚本中被调用： 新建测试脚本如下图： <img src="https://img-blog.csdnimg.cn/20200105144054205.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTgwNTMzOQ==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 执行脚本，运行结果如下图： <img src="https://img-blog.csdnimg.cn/20200105144133142.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTgwNTMzOQ==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 只输出了第⼀⾏字符串。即，if name==“main”: 之前的语句被执行，之后的没有被执行。

### if name == ‘main’:的运⾏行行原理理

每个python模块(python⽂件，unit_13_helloworld.py 和 unit_13_test.py)都包含内置的变量量 name，当该模块被直接执行的时候，name 等于文件名(包含后缀 .py );如果该模块 import 到其他模块中，则该模块的name等于模块名称(不包含后缀.py)。 而 “main” 始终指当前执行模块的名称(包含后缀.py)。进⽽当模块被直接执行时，name == ‘main’ 结果为真。 为了进一步说明，我们在unit_13_helloworld.py 脚本的 if name==“main”: 之前加 print(name)，即将 name 打印出来。文件内容和结果如下: <img src="https://img-blog.csdnimg.cn/20200105145146216.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTgwNTMzOQ==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20200105145158919.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTgwNTMzOQ==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 可以看出，此时变量量name的值为"main"。 再执⾏行行 unit_13_test.py，执⾏行行结果如下: <img src="https://img-blog.csdnimg.cn/20200105145310619.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTgwNTMzOQ==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">
