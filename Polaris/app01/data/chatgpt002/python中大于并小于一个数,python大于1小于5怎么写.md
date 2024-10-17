
--- 
title:  python中大于并小于一个数,python大于1小于5怎么写 
tags: []
categories: [] 

---
这篇文章主要介绍了python 大于1小于等于50的整数，具有一定借鉴价值，需要的朋友可以参考下。希望大家阅读完这篇文章后大有收获，下面让小编带着大家一起了解一下。



<img alt="" height="500" src="https://img-blog.csdnimg.cn/img_convert/50bcc63c6998b9698e979d93de6cc6ca.jpeg" width="547">

#### **<strong><strong>比较运算符示例**</strong></strong>

**功能要求**

关系运算符示例

**实例代码**

```
print(1 &lt; 3 &lt; 5)  # 等价于1 &lt; 3 and 3 &lt; 5

print(3 &lt; 5 &gt; 2)

print(1 &gt; 6 &lt; 8)

print("Hello" &gt; 'hello')  # 比较字符串大小

print([1, 2, 3] &lt; [1, 2, 4])  # 比较列表大小

print({1, 2, 3} &lt; {1, 2, 3, 4})  # 测试是否为子集

print({1, 2, 3} == {3, 2, 1})  # 测试两个集合是否相等

print({1, 2, 4} &gt; {1, 2, 3})  # 集合之间的包含测试

print({1, 2, 4} &lt; {1, 2, 3})

print({1, 2, 4} == {1, 2, 3})

print('Hello' &gt; 3)  # 字符串和数字不能比较
```

**运行结果**

Traceback (most recent call last):

  File "E:\Code\PythonCode\hello.py", line 11, in &lt;module&gt;

    print('Hello' &gt; 3)  # 字符串和数字不能比较

TypeError: '&gt;' not supported between instances of 'str' and 'int'

True

True

False


