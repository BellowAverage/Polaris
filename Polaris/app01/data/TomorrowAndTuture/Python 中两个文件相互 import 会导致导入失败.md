
--- 
title:  Python 中两个文件相互 import 会导致导入失败 
tags: []
categories: [] 

---
相互导入导致导入失败。 

```
# t1.py
from t2 import NAME


AGE = 20

print(NAME, AGE)
```

```
# t2.py
from t1 import AGE

print('hello world')
NAME = 'AA'
```

```
[root@master ~]# python3 ./t1.py 
Traceback (most recent call last):
  File "./t1.py", line 1, in &lt;module&gt;
    from t2 import NAME
  File "/root/insight-tools-rest/t2.py", line 2, in &lt;module&gt;
    from t1 import AGE
  File "/root/insight-tools-rest/t1.py", line 1, in &lt;module&gt;
    from t2 import NAME
ImportError: cannot import name 'NAME'

```

但是如果注释掉 t2.py 中的 import 代码，t1.py 就可以正常运行了。 

```
# t1.py
from t2 import NAME


AGE = 20

print(NAME, AGE)
```

```
# t2.py
# from t1 import AGE

print('hello world')
NAME = 'AA'
```

```
[root@master ~]# python3 ./t1.py 
hello world
AA 20
```

其实，感觉出现这种导入失败的原因是因为导入的时候会把另外一个脚本执行一遍——比如说 t2.py 里边打印的 hello world，执行 t2.py 的时候会从 t1.py 导入，执行 t1.py 的时候又会从 t2.py 导入，如此下去，就变成死循环了。**因此，在python开发过程中，应尽量避免相互导入。**

但是，如果确实有相互导入的需求，那么有没有解决办法呢？

**办法当然是有的，其中可选的解决办法如下：**


- 将需要导入的函数或者变量在当前 py 里重新定义一遍，但是这样的话就重复定义了。
```
# t1.py
# from t2 import NAME


print('hello world')
NAME = 'AA'
AGE = 20

print(NAME, AGE)
```

```
[root@master ~]# python3 ./t1.py 
hello world
AA 20
```
- 将其中一个的 import 语句移到函数的内部，使得它只有在执行到这个模块时，才会导入相关模块。
```
# t1.py

AGE = 20

def test1():
    from t2 import NAME
    print(NAME, AGE)

if __name__ == '__main__':
    test1()

```

```
# t2.py
from t1 import AGE

print('hello world')
NAME = 'AA'
```

```
[root@master ~]# python3 ./t1.py 
hello world
AA 20
```
