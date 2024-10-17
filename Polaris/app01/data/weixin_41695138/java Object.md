
--- 
title:  java Object 
tags: []
categories: [] 

---
### Object

类 Object 是类层次结构的根类。每个类都使用 Object 作为超类。所有对象（包括数组）都实现这个类的方法。

### 构造方法

public Object()

### 方法
1. public boolean equals(Object obj) 指示其他某个对象是否与此对象“相等”。 此方法经常被重写，用来判断对象的内容是否相等，Integer Double 等重写了此方法，用来判断值是否相等。（请注意 Integer 还有 -128 到 127 == 相比相等的问题，封装类的比值请使用 equals）1. public int hashCode() 返回该对象的哈希码值, 在比较的时候，我们经常重写 hashCode 方法，请参考： hashCode equals 在集合添加时的区别
```
https://blog.csdn.net/weixin_41695138/article/details/120949148

```
1. public String toString() 返回该对象的字符串表示。通常，toString 方法会返回一个“以文本方式表示”此对象的字符串。结果应是一个简明但易于读懂的信息表达式。建议所有子类都重写此方法。1. public final void notify() 线程相关的方法 唤醒在此对象监视器上等待的单个线程。1. public final void wait() 线程相关的方法 在其他线程调用此对象的 notify() 方法或 notifyAll() 方法前，导致当前线程等待1. public final Class&lt;?&gt; getClass() 反射相关的方法 返回此 Object 的运行时类 返回的 Class 对象是由所表示类的 static synchronized 方法锁定的对象。